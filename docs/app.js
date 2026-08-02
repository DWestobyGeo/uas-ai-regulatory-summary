(function () {
  "use strict";

  var INDEX_URL = "data/v1/index.json";
  var select = document.getElementById("state-select");
  var emptyState = document.getElementById("empty-state");
  var content = document.getElementById("state-content");
  var titleEl = document.getElementById("state-title");
  var subEl = document.getElementById("state-sub");
  var summaryPanel = document.getElementById("summary-panel");
  var registerTable = document.getElementById("register-table");
  var countLabel = document.getElementById("state-count-label");
  var printBtn = document.getElementById("print-btn");
  var downloadJsonBtn = document.getElementById("download-json-btn");
  var downloadCsvBtn = document.getElementById("download-csv-btn");

  var currentStateData = null;

  // Columns shown in the register table, in order, with friendly headers.
  var COLUMNS = [
    ["record_id", "ID"],
    ["source_title", "Source"],
    ["citation", "Citation"],
    ["source_type", "Type"],
    ["status", "Status"],
    ["binding_level", "Binding Level"],
    ["uas_topic", "Topic"],
    ["aec_relevance", "AEC Relevance"],
    ["confidence_level", "Confidence"],
    ["summary", "Objective Summary"],
    ["practical_interpretation_aec_expert", "AEC Expert Interpretation"],
    ["practical_interpretation_legal_counsel", "Legal Counsel Interpretation"],
    ["source_url", "Source URL"],
    ["date_accessed", "Accessed"],
    ["notes", "Notes"]
  ];

  function badgeFor(value) {
    if (!value) return "";
    var v = value.toLowerCase();
    var cls = "badge";
    if (v.indexOf("high") === 0) cls += " high";
    else if (v.indexOf("moderate") === 0) cls += " moderate";
    else if (v.indexOf("low") === 0) cls += " low";
    return '<span class="' + cls + '">' + escapeHtml(value) + "</span>";
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

    renderRegisterTable(data.records || []);
  }

  function renderRegisterTable(records) {
    var thead = registerTable.querySelector("thead");
    var tbody = registerTable.querySelector("tbody");
    thead.innerHTML = "";
    tbody.innerHTML = "";

    var headRow = document.createElement("tr");
    COLUMNS.forEach(function (col) {
      var th = document.createElement("th");
      th.textContent = col[1];
      headRow.appendChild(th);
    });
    thead.appendChild(headRow);

    records.forEach(function (rec) {
      var tr = document.createElement("tr");
      COLUMNS.forEach(function (col) {
        var td = document.createElement("td");
        var key = col[0];
        var val = rec[key];
        if (key === "confidence_level" || key === "aec_relevance") {
          td.innerHTML = badgeFor(val);
        } else if (key === "source_url" && val) {
          var a = document.createElement("a");
          a.href = val;
          a.target = "_blank";
          a.rel = "noopener noreferrer";
          a.textContent = "source ↗";
          td.appendChild(a);
        } else {
          td.textContent = val || "";
        }
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });
  }

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
