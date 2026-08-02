(function () {
  "use strict";

  var INDEX_URL = "data/v1/index.json";
  var select = document.getElementById("state-select");
  var emptyState = document.getElementById("empty-state");
  var content = document.getElementById("state-content");
  var titleEl = document.getElementById("state-title");
  var subEl = document.getElementById("state-sub");
  var summaryPanel = document.getElementById("summary-panel");
  var registerList = document.getElementById("register-list");
  var registerNoResults = document.getElementById("register-no-results");
  var registerSearch = document.getElementById("register-search");
  var registerFilterConfidence = document.getElementById("register-filter-confidence");
  var registerFilterRelevance = document.getElementById("register-filter-relevance");
  var registerCount = document.getElementById("register-count");
  var expandAllBtn = document.getElementById("expand-all-btn");
  var collapseAllBtn = document.getElementById("collapse-all-btn");
  var countLabel = document.getElementById("state-count-label");
  var printBtn = document.getElementById("print-btn");
  var downloadJsonBtn = document.getElementById("download-json-btn");
  var downloadCsvBtn = document.getElementById("download-csv-btn");

  var currentStateData = null;
  var currentRecords = [];

  function levelClass(value) {
    if (!value) return "";
    var v = value.toLowerCase();
    if (v.indexOf("high") === 0) return "high";
    if (v.indexOf("moderate") === 0) return "moderate";
    if (v.indexOf("low") === 0) return "low";
    return "";
  }

  function badgeFor(value, extraClass) {
    if (!value) return "";
    var cls = "badge " + levelClass(value) + (extraClass ? " " + extraClass : "");
    return '<span class="' + cls + '">' + escapeHtml(value) + "</span>";
  }

  function plainBadge(value) {
    if (!value) return "";
    return '<span class="badge plain">' + escapeHtml(value) + "</span>";
  }

  function escapeHtml(s) {
    if (s === null || s === undefined) return "";
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  function getQueryParam(name) {
    var params = new URLSearchParams(window.location.search);
    return params.get(name);
  }

  function setQueryParam(name, value) {
    var url = new URL(window.location.href);
    if (value) {
      url.searchParams.set(name, value);
    } else {
      url.searchParams.delete(name);
    }
    window.history.replaceState({}, "", url);
  }

  function loadIndex() {
    fetch(INDEX_URL)
      .then(function (r) { return r.json(); })
      .then(function (data) {
        populateSelect(data.states);
        var requested = getQueryParam("state");
        if (requested) {
          select.value = requested.toUpperCase();
          if (select.value) {
            loadState(select.value);
          }
        }
      })
      .catch(function (err) {
        emptyState.innerHTML = "<p>Could not load the state index (data/v1/index.json). If you're viewing this file locally (file://), run it through a local web server instead — browsers block fetch() on local files.</p>";
        console.error(err);
      });
  }

  function populateSelect(states) {
    select.innerHTML = '<option value="">— Select a state —</option>';
    states.forEach(function (s) {
      var opt = document.createElement("option");
      opt.value = s.state_abbr;
      opt.textContent = s.state + " (" + s.state_abbr + ")";
      select.appendChild(opt);
    });
    countLabel.textContent = states.length + " state" + (states.length === 1 ? "" : "s") + " available";
  }

  function loadState(abbr) {
    if (!abbr) {
      content.classList.remove("visible");
      emptyState.style.display = "";
      setQueryParam("state", null);
      return;
    }
    fetch("data/v1/" + abbr + ".json")
      .then(function (r) {
        if (!r.ok) throw new Error("Not found: " + abbr);
        return r.json();
      })
      .then(function (data) {
        currentStateData = data;
        renderState(data);
        setQueryParam("state", abbr);
      })
      .catch(function (err) {
        console.error(err);
        alert("Could not load data for " + abbr + ".");
      });
  }

  function renderState(data) {
    emptyState.style.display = "none";
    content.classList.add("visible");

    titleEl.textContent = data.state + " (" + data.state_abbr + ")";
    subEl.textContent =
      "Last updated " + data.last_updated + " · " + data.record_count + " source record" +
      (data.record_count === 1 ? "" : "s") + " · schema v" + data.schema_version;

    // Render markdown summary
    if (window.marked) {
      summaryPanel.innerHTML = marked.parse(data.summary_markdown || "");
    } else {
      var pre = document.createElement("pre");
      pre.textContent = data.summary_markdown || "";
      summaryPanel.innerHTML = "";
      summaryPanel.appendChild(pre);
    }

    currentRecords = data.records || [];
    registerSearch.value = "";
    registerFilterConfidence.value = "";
    registerFilterRelevance.value = "";
    renderRegisterList();
  }

  // Builds one accordion card for a source-register record.
  function buildCard(rec, index) {
    var card = document.createElement("div");
    card.className = "reg-card";
    card.dataset.index = index;

    var header = document.createElement("button");
    header.type = "button";
    header.className = "reg-card-header";
    header.setAttribute("aria-expanded", "false");

    var idSpan = '<span class="reg-id">' + escapeHtml(rec.record_id || "") + "</span>";
    var titleBlock =
      '<span class="reg-title-block">' +
        '<span class="reg-title">' + escapeHtml(rec.source_title || "(untitled source)") + "</span>" +
        '<span class="reg-citation">' + escapeHtml(rec.citation || "") + "</span>" +
      "</span>";
    var badges =
      '<span class="reg-badges">' +
        plainBadge(rec.source_type) +
        plainBadge(rec.status) +
        badgeFor(rec.aec_relevance, "aec") +
        badgeFor(rec.confidence_level, "conf") +
      "</span>";
    var chevron = '<span class="reg-chevron">▸</span>';

    header.innerHTML = idSpan + titleBlock + badges + chevron;

    var body = document.createElement("div");
    body.className = "reg-card-body";
    body.hidden = true;

    body.innerHTML =
      metaRow("Jurisdiction", [rec.jurisdiction_name, rec.jurisdiction_type, rec.geographic_scope].filter(Boolean).join(" · ")) +
      metaRow("Issuing authority", rec.issuing_authority) +
      metaRow("Topic", rec.uas_topic) +
      metaRow("Regulated party / activity", [rec.regulated_party, rec.regulated_activity].filter(Boolean).join(" — ")) +
      metaRow("Requirement", [rec.requirement_type, rec.permit_or_approval_required ? "Permit/approval: " + rec.permit_or_approval_required : ""].filter(Boolean).join(" · ")) +
      '<div class="reg-block"><h4>Objective Summary</h4><p>' + escapeHtml(rec.summary || "") + "</p></div>" +
      '<div class="reg-block"><h4>Practical Interpretation</h4>' +
        '<p><strong>AEC Industry UAS Expert:</strong> ' + escapeHtml(rec.practical_interpretation_aec_expert || "") + "</p>" +
        '<p><strong>AEC Industry Legal Counsel:</strong> ' + escapeHtml(rec.practical_interpretation_legal_counsel || "") + "</p>" +
      "</div>" +
      (rec.notes ? '<div class="reg-block"><h4>Notes</h4><p>' + escapeHtml(rec.notes) + "</p></div>" : "") +
      '<div class="reg-footer">' +
        (rec.source_url ? '<a href="' + escapeHtml(rec.source_url) + '" target="_blank" rel="noopener noreferrer">Open original source ↗</a>' : "<span></span>") +
        '<span class="reg-footer-meta">' +
          (rec.date_accessed ? "Accessed " + escapeHtml(rec.date_accessed) + " · " : "") +
          "Verification: " + escapeHtml(rec.verification_status || "—") +
        "</span>" +
      "</div>";

    header.addEventListener("click", function () {
      var isOpen = !body.hidden;
      body.hidden = isOpen;
      card.classList.toggle("open", !isOpen);
      header.setAttribute("aria-expanded", String(!isOpen));
    });

    card.appendChild(header);
    card.appendChild(body);
    return card;
  }

  function metaRow(label, value) {
    if (!value) return "";
    return '<div class="reg-meta-row"><span class="reg-meta-label">' + escapeHtml(label) + '</span><span class="reg-meta-value">' + escapeHtml(value) + "</span></div>";
  }

  function matchesFilters(rec, query, confidence, relevance) {
    if (confidence && levelClass(rec.confidence_level) !== confidence) return false;
    if (relevance && levelClass(rec.aec_relevance) !== relevance) return false;
    if (query) {
      var haystack = [
        rec.source_title, rec.citation, rec.uas_topic, rec.summary,
        rec.issuing_authority, rec.regulated_party, rec.regulated_activity,
        rec.practical_interpretation_aec_expert, rec.practical_interpretation_legal_counsel,
        rec.record_id, rec.notes
      ].join(" ").toLowerCase();
      if (haystack.indexOf(query.toLowerCase()) === -1) return false;
    }
    return true;
  }

  function renderRegisterList() {
    var query = registerSearch.value.trim();
    var confidence = registerFilterConfidence.value;
    var relevance = registerFilterRelevance.value;

    registerList.innerHTML = "";
    var shown = 0;
    currentRecords.forEach(function (rec, i) {
      if (!matchesFilters(rec, query, confidence, relevance)) return;
      registerList.appendChild(buildCard(rec, i));
      shown++;
    });

    registerNoResults.style.display = shown === 0 ? "" : "none";
    registerCount.textContent = shown === currentRecords.length
      ? shown + " source" + (shown === 1 ? "" : "s")
      : shown + " of " + currentRecords.length + " sources";
  }

  registerSearch.addEventListener("input", renderRegisterList);
  registerFilterConfidence.addEventListener("change", renderRegisterList);
  registerFilterRelevance.addEventListener("change", renderRegisterList);

  expandAllBtn.addEventListener("click", function () {
    registerList.querySelectorAll(".reg-card").forEach(function (card) {
      card.classList.add("open");
      card.querySelector(".reg-card-body").hidden = false;
      card.querySelector(".reg-card-header").setAttribute("aria-expanded", "true");
    });
  });

  collapseAllBtn.addEventListener("click", function () {
    registerList.querySelectorAll(".reg-card").forEach(function (card) {
      card.classList.remove("open");
      card.querySelector(".reg-card-body").hidden = true;
      card.querySelector(".reg-card-header").setAttribute("aria-expanded", "false");
    });
  });

  select.addEventListener("change", function () {
    loadState(this.value);
  });

  printBtn.addEventListener("click", function () {
    if (!currentStateData) {
      alert("Select a state first.");
      return;
    }
    window.print();
  });

  downloadJsonBtn.addEventListener("click", function () {
    if (!currentStateData) { alert("Select a state first."); return; }
    var blob = new Blob([JSON.stringify(currentStateData, null, 2)], { type: "application/json" });
    triggerDownload(blob, currentStateData.state_abbr + ".json");
  });

  downloadCsvBtn.addEventListener("click", function () {
    if (!currentStateData) { alert("Select a state first."); return; }
    window.location.href = currentStateData.source_files.source_register_csv;
  });

  function triggerDownload(blob, filename) {
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  loadIndex();
})();
