(function () {
  "use strict";

  var INDEX_URL = "data/v1/index.json";
  var UI_VERSION = "1.1.1";

  var select = document.getElementById("state-select");
  var emptyState = document.getElementById("empty-state");
  var content = document.getElementById("state-content");
  var titleEl = document.getElementById("state-title");
  var updatedEl = document.getElementById("state-updated");
  var recordCountEl = document.getElementById("state-record-count");
  var researchStatusEl = document.getElementById("state-research-status");
  var schemaEl = document.getElementById("state-schema");
  var summaryPanel = document.getElementById("summary-panel");
  var tocNav = document.getElementById("toc-nav");
  var tocDisclosure = document.getElementById("toc-disclosure");
  var registerList = document.getElementById("register-list");
  var registerNoResults = document.getElementById("register-no-results");
  var registerSearch = document.getElementById("register-search");
  var registerFilterConfidence = document.getElementById("register-filter-confidence");
  var registerFilterRelevance = document.getElementById("register-filter-relevance");
  var registerCount = document.getElementById("register-count");
  var expandAllBtn = document.getElementById("expand-all-btn");
  var collapseAllBtn = document.getElementById("collapse-all-btn");
  var countLabel = document.getElementById("state-count-label");
  var scopeCount = document.getElementById("coverage-progress-count");
  var pageStatus = document.getElementById("page-status");
  var printBtn = document.getElementById("print-btn");
  var downloadJsonBtn = document.getElementById("download-json-btn");
  var downloadCsvBtn = document.getElementById("download-csv-btn");

  var currentStateData = null;
  var currentRecords = [];
  var sectionObserver = null;
  var tocMedia = window.matchMedia("(min-width: 1040px)");

  var DISCLAIMER_BANNER_HTML =
    '<aside class="ai-disclaimer-banner" role="note" aria-label="AI-generated content notice">' +
      '<span class="ai-disclaimer-label">AI research notice</span>' +
      '<p><strong>Everything below, including the source register, was produced by an AI research process and has not been reviewed or approved by a licensed attorney.</strong> ' +
      'It may be incomplete, outdated, or wrong and is not legal advice. Verify cited material and obtain any external professional review appropriate to your use. ' +
      '<a href="disclaimer.html">Read the full disclaimer</a>.</p>' +
    '</aside>';

  function escapeHtml(value) {
    if (value === null || value === undefined) return "";
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function announce(message) {
    pageStatus.textContent = "";
    window.setTimeout(function () {
      pageStatus.textContent = message;
    }, 20);
  }

  var RESEARCH_STATUS_LABELS = {
    current_method_complete: "Current method (complete)",
    current_method_in_progress: "Current method (in progress)",
    legacy_needs_retrofit: "Legacy — not yet retrofitted",
    legacy_retrofit_in_progress: "Legacy retrofit in progress",
    legacy_retrofit_complete: "Retrofit complete"
  };

  function researchStatusBadge(status) {
    var label = RESEARCH_STATUS_LABELS[status] || "Not recorded";
    var cls = (status && status.indexOf("current_method") === 0) || status === "legacy_retrofit_complete"
      ? "current-method"
      : "legacy";
    return '<span class="badge ' + cls + '" title="See the Research method note in the disclaimer for what this means.">' + escapeHtml(label) + "</span>";
  }

  function levelClass(value) {
    if (!value) return "";
    var normalized = String(value).toLowerCase();
    if (normalized.indexOf("high") === 0) return "high";
    if (normalized.indexOf("moderate") === 0) return "moderate";
    if (normalized.indexOf("low") === 0) return "low";
    return "";
  }

  function badgeFor(value, extraClass) {
    if (!value) return "";
    var className = "badge " + levelClass(value) + (extraClass ? " " + extraClass : "");
    return '<span class="' + className + '">' + escapeHtml(value) + "</span>";
  }

  function plainBadge(value) {
    if (!value) return "";
    return '<span class="badge plain">' + escapeHtml(value) + "</span>";
  }

  function getQueryParam(name) {
    return new URLSearchParams(window.location.search).get(name);
  }

  function setQueryParam(name, value) {
    var url = new URL(window.location.href);
    if (value) url.searchParams.set(name, value);
    else url.searchParams.delete(name);
    window.history.replaceState({}, "", url);
  }

  function clearHash() {
    if (!window.location.hash) return;
    var url = new URL(window.location.href);
    url.hash = "";
    window.history.replaceState({}, "", url);
  }

  function slugify(text) {
    var slug = String(text || "section")
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "");
    return slug || "section";
  }

  function assignHeadingIds() {
    var used = Object.create(null);
    Array.prototype.forEach.call(summaryPanel.querySelectorAll("h2, h3"), function (heading) {
      var base = "section-" + slugify(heading.textContent);
      var count = used[base] || 0;
      used[base] = count + 1;
      heading.id = count ? base + "-" + (count + 1) : base;
      heading.tabIndex = -1;
    });
  }

  function classifySummaryContent() {
    Array.prototype.forEach.call(summaryPanel.querySelectorAll("strong"), function (strong) {
      var label = strong.textContent.trim().replace(/:$/, "");
      var paragraph = strong.closest("p");
      if (label === "Objective Summary" && paragraph) paragraph.classList.add("objective-summary");
      if (label === "Practical Interpretation" && paragraph) {
        paragraph.classList.add("interpretation-heading");
        if (paragraph.nextElementSibling && paragraph.nextElementSibling.tagName === "UL") {
          paragraph.nextElementSibling.classList.add("perspectives-list");
        }
      }

      var item = strong.closest("li");
      if (!item) return;
      if (label === "AEC Industry UAS Expert") item.classList.add("perspective-aec");
      if (label === "Agency Practitioner") item.classList.add("perspective-agency");
      if (label === "UAS Procurement Expert") item.classList.add("perspective-procurement");
      if (label === "AEC Industry Legal Counsel") item.classList.add("perspective-legal");
    });

    Array.prototype.forEach.call(summaryPanel.querySelectorAll("table"), function (table) {
      if (table.parentElement && table.parentElement.classList.contains("table-wrap")) return;
      var wrapper = document.createElement("div");
      wrapper.className = "table-wrap";
      wrapper.tabIndex = 0;
      wrapper.setAttribute("role", "region");
      wrapper.setAttribute("aria-label", "Scrollable data table");
      table.parentNode.insertBefore(wrapper, table);
      wrapper.appendChild(table);
    });
  }

  // These are the register's own established conventions for flagging an authority
  // that is not currently enacted/binding law (see e.g. States/MO_Missouri and
  // States/WA_Washington's "Repealed, expired, or superseded authority (never
  // enacted)" and "Proposed or pending authority (died in committee)" subtitles, and
  // headings ending "-- not current law" / "-- did not pass"). This reads content the
  // research process already wrote; it does not add a new editorial judgment.
  var NOT_CURRENT_LAW_SUBTITLE_PREFIXES = [
    "proposed or pending authority",
    "repealed, expired, or superseded authority"
  ];
  var NOT_CURRENT_LAW_TITLE_MARKERS = [
    "not current law",
    "did not pass"
  ];

  function titleAlreadyDeclaresNotCurrent(heading) {
    var title = (heading.textContent || "").toLowerCase();
    return NOT_CURRENT_LAW_TITLE_MARKERS.some(function (m) { return title.indexOf(m) !== -1; });
  }

  function subtitleDeclaresNotCurrent(subtitleText) {
    var subtitle = (subtitleText || "").trim().toLowerCase();
    return NOT_CURRENT_LAW_SUBTITLE_PREFIXES.some(function (m) { return subtitle.indexOf(m) === 0; });
  }

  function flagNotCurrentLaw(card, heading) {
    // Checked separately (not merged into one boolean) because the two cases need
    // different treatment below: when the heading's own wording already says "not
    // current law" / "did not pass", that text is the flag -- appending another
    // "Not current law" badge would duplicate it in the heading's accessible name and
    // in the generated heading ID (assignHeadingIds() runs after this, from
    // heading.textContent). Only add the separate badge when the title doesn't already
    // say it.
    var titleAlreadySays = titleAlreadyDeclaresNotCurrent(heading);
    var subtitleEl = card.querySelector("p > em:only-child, p > em:first-child");
    var subtitleSays = subtitleDeclaresNotCurrent(subtitleEl ? subtitleEl.textContent : "");
    if (!titleAlreadySays && !subtitleSays) return;
    card.classList.add("not-current-law");
    heading.classList.add("not-current-law");
    if (!titleAlreadySays && !heading.querySelector(".not-current-law-flag")) {
      var flag = document.createElement("span");
      flag.className = "not-current-law-flag";
      flag.textContent = "Not current law";
      heading.appendChild(flag);
    }
  }

  function wrapAuthorityCards() {
    var headings = Array.prototype.slice.call(summaryPanel.querySelectorAll("h3"));
    headings.forEach(function (heading) {
      if (heading.closest(".authority-card")) return;
      var parent = heading.parentNode;
      var card = document.createElement("section");
      card.className = "authority-card";
      parent.insertBefore(card, heading);

      var node = heading;
      while (node) {
        var next = node.nextSibling;
        if (node !== heading && node.nodeType === 1 && (node.tagName === "H2" || node.tagName === "H3")) break;
        card.appendChild(node);
        node = next;
      }
      flagNotCurrentLaw(card, heading);
    });
  }

  function wrapMajorSections() {
    var headings = Array.prototype.slice.call(summaryPanel.children).filter(function (element) {
      return element.tagName === "H2";
    });

    headings.forEach(function (heading, index) {
      if (heading.parentNode !== summaryPanel) return;
      var section = document.createElement("section");
      section.className = "summary-section section-tone-" + ((index % 3) + 1);
      summaryPanel.insertBefore(section, heading);

      var node = heading;
      while (node) {
        var next = node.nextSibling;
        if (node !== heading && node.nodeType === 1 && node.tagName === "H2") break;
        section.appendChild(node);
        node = next;
      }
    });

    var firstSection = summaryPanel.querySelector(":scope > .summary-section");
    if (!firstSection || firstSection === summaryPanel.firstElementChild) return;
    var intro = document.createElement("section");
    intro.className = "summary-intro";
    summaryPanel.insertBefore(intro, summaryPanel.firstChild);
    var current = intro.nextSibling;
    while (current && current !== firstSection) {
      var next = current.nextSibling;
      intro.appendChild(current);
      current = next;
    }
  }

  function enhanceSummary() {
    var renderedTitle = summaryPanel.querySelector("h1");
    if (renderedTitle) {
      var titleLabel = document.createElement("p");
      titleLabel.className = "summary-document-title";
      titleLabel.innerHTML = renderedTitle.innerHTML;
      renderedTitle.parentNode.replaceChild(titleLabel, renderedTitle);
    }
    classifySummaryContent();
    wrapAuthorityCards();
    wrapMajorSections();
    assignHeadingIds();
  }

  function buildTableOfContents() {
    tocNav.innerHTML = "";
    var list = document.createElement("ol");
    list.className = "toc-list";

    Array.prototype.forEach.call(summaryPanel.querySelectorAll("h2[id], h3[id]"), function (heading) {
      var item = document.createElement("li");
      item.className = heading.tagName === "H3" ? "toc-level-3" : "toc-level-2";
      var link = document.createElement("a");
      link.href = "#" + heading.id;
      var isFlagged = heading.classList.contains("not-current-law");
      link.textContent = heading.textContent.replace(/[\s\u2014-]*\(?(not current law|did not pass)\)?\s*$/i, "");
      if (isFlagged) {
        link.classList.add("not-current-law");
        var tocFlag = document.createElement("span");
        tocFlag.className = "toc-status-flag";
        tocFlag.textContent = "Not current law";
        link.appendChild(tocFlag);
      }
      item.appendChild(link);
      list.appendChild(item);
    });

    var sourceItem = document.createElement("li");
    sourceItem.className = "toc-level-2 toc-source-link";
    var sourceLink = document.createElement("a");
    sourceLink.href = "#source-register";
    sourceLink.textContent = "Source Register";
    sourceItem.appendChild(sourceLink);
    list.appendChild(sourceItem);
    tocNav.appendChild(list);
  }

  function setActiveTocLink(id) {
    Array.prototype.forEach.call(tocNav.querySelectorAll("a"), function (link) {
      var isActive = link.getAttribute("href") === "#" + id;
      link.classList.toggle("active", isActive);
      if (isActive) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
  }

  function setupSectionObserver() {
    if (sectionObserver) sectionObserver.disconnect();
    if (!("IntersectionObserver" in window)) return;

    var headings = Array.prototype.slice.call(summaryPanel.querySelectorAll("h2[id]"));
    var sourceHeading = document.getElementById("source-register");
    if (sourceHeading) headings.push(sourceHeading);

    sectionObserver = new IntersectionObserver(function (entries) {
      var visible = entries.filter(function (entry) { return entry.isIntersecting; });
      if (!visible.length) return;
      visible.sort(function (a, b) { return a.boundingClientRect.top - b.boundingClientRect.top; });
      setActiveTocLink(visible[0].target.id);
    }, { rootMargin: "-20% 0px -68% 0px", threshold: [0, 1] });

    headings.forEach(function (heading) { sectionObserver.observe(heading); });
  }

  function syncTocDisclosure() {
    tocDisclosure.open = tocMedia.matches;
  }

  function restoreHashTarget() {
    if (!window.location.hash) return;
    var id = decodeURIComponent(window.location.hash.slice(1));
    var target = document.getElementById(id);
    if (!target) return;

    var sourceCard = target.closest ? target.closest(".reg-card") : null;
    if (sourceCard) setCardOpen(sourceCard, true);
    window.requestAnimationFrame(function () {
      target.scrollIntoView({ block: "start" });
      if (target.matches("h2, h3")) target.focus({ preventScroll: true });
    });
  }

  function loadIndex() {
    fetch(INDEX_URL)
      .then(function (response) {
        if (!response.ok) throw new Error("State index request failed");
        return response.json();
      })
      .then(function (data) {
        populateSelect(data.states || []);
        var requested = getQueryParam("state");
        if (requested) {
          select.value = requested.toUpperCase();
          if (select.value) loadState(select.value, true);
        }
      })
      .catch(function (error) {
        emptyState.innerHTML = '<span class="empty-kicker">Unable to load research</span><h1>State index unavailable</h1><p>Try refreshing the page. When viewing a local copy, use a local web server rather than opening the file directly.</p>';
        console.error(error);
        announce("The state index could not be loaded.");
      });
  }

  function populateSelect(states) {
    select.innerHTML = '<option value="">— Select a state —</option>';
    states.forEach(function (state) {
      var option = document.createElement("option");
      option.value = state.state_abbr;
      option.textContent = state.state + " (" + state.state_abbr + ")";
      select.appendChild(option);
    });
    var label = states.length + " state" + (states.length === 1 ? "" : "s") + " available";
    countLabel.textContent = label;
    scopeCount.textContent = label;
  }

  function loadState(abbr, preserveHash) {
    if (!abbr) {
      content.classList.remove("visible");
      emptyState.hidden = false;
      setQueryParam("state", null);
      document.title = "State UAS Regulatory Summaries — AEC Reference";
      return;
    }

    select.disabled = true;
    announce("Loading " + abbr + " state research.");
    fetch("data/v1/" + abbr + ".json")
      .then(function (response) {
        if (!response.ok) throw new Error("State data not found: " + abbr);
        return response.json();
      })
      .then(function (data) {
        currentStateData = data;
        renderState(data, preserveHash);
        setQueryParam("state", abbr);
        announce(data.state + " research loaded. " + data.record_count + " source records available.");
      })
      .catch(function (error) {
        console.error(error);
        emptyState.hidden = false;
        emptyState.innerHTML = '<span class="empty-kicker">State unavailable</span><h1>Could not load ' + escapeHtml(abbr) + '</h1><p>Choose another state or refresh the page.</p>';
        content.classList.remove("visible");
        announce("Could not load data for " + abbr + ".");
      })
      .finally(function () {
        select.disabled = false;
      });
  }

  function renderState(data, preserveHash) {
    emptyState.hidden = true;
    content.classList.add("visible");

    titleEl.textContent = data.state + " (" + data.state_abbr + ")";
    updatedEl.textContent = data.last_updated || "Not provided";
    researchStatusEl.innerHTML = researchStatusBadge(data.research_status);
    recordCountEl.textContent = data.record_count + " source record" + (data.record_count === 1 ? "" : "s");
    schemaEl.textContent = "v" + data.schema_version;
    document.title = data.state + " UAS Regulatory Summary — AEC Reference";

    if (window.marked) {
      var rendered = marked.parse(data.summary_markdown || "");
      var firstSection = rendered.indexOf("<h2");
      summaryPanel.innerHTML = firstSection === -1
        ? DISCLAIMER_BANNER_HTML + rendered
        : rendered.slice(0, firstSection) + DISCLAIMER_BANNER_HTML + rendered.slice(firstSection);
    } else {
      var pre = document.createElement("pre");
      pre.textContent = data.summary_markdown || "";
      summaryPanel.innerHTML = DISCLAIMER_BANNER_HTML;
      summaryPanel.appendChild(pre);
    }

    enhanceSummary();
    buildTableOfContents();
    setupSectionObserver();
    syncTocDisclosure();

    currentRecords = data.records || [];
    registerSearch.value = "";
    registerFilterConfidence.value = "";
    registerFilterRelevance.value = "";
    renderRegisterList();

    if (preserveHash) restoreHashTarget();
    else window.scrollTo({ top: 0, behavior: "auto" });
  }

  function metaRow(label, value) {
    if (!value) return "";
    return '<div class="reg-meta-row"><dt>' + escapeHtml(label) + '</dt><dd>' + escapeHtml(value) + "</dd></div>";
  }

  function perspectivePanel(label, value, className) {
    return '<div class="perspective-panel ' + className + '"><h5>' + escapeHtml(label) + '</h5><p>' + escapeHtml(value || "Not provided") + "</p></div>";
  }

  function buildCard(record, index) {
    var card = document.createElement("article");
    card.className = "reg-card";
    card.dataset.index = index;
    card.id = "source-" + slugify(record.record_id || String(index + 1));

    var header = document.createElement("button");
    header.type = "button";
    header.className = "reg-card-header";
    header.id = card.id + "-toggle";
    header.setAttribute("aria-expanded", "false");
    header.setAttribute("aria-controls", card.id + "-details");

    header.innerHTML =
      '<span class="reg-id">' + escapeHtml(record.record_id || "") + "</span>" +
      '<span class="reg-title-block"><span class="reg-title">' + escapeHtml(record.source_title || "Untitled source") + '</span><span class="reg-citation">' + escapeHtml(record.citation || "Citation not provided") + "</span></span>" +
      '<span class="reg-badges">' + plainBadge(record.source_type) + plainBadge(record.status) + badgeFor(record.aec_relevance, "aec") + badgeFor(record.confidence_level, "conf") + "</span>" +
      '<span class="reg-chevron" aria-hidden="true"></span>';

    var body = document.createElement("div");
    body.className = "reg-card-body";
    body.id = card.id + "-details";
    body.setAttribute("aria-labelledby", header.id);
    body.hidden = true;

    body.innerHTML =
      '<dl class="reg-meta-grid">' +
        metaRow("Jurisdiction", [record.jurisdiction_name, record.jurisdiction_type, record.geographic_scope].filter(Boolean).join(" · ")) +
        metaRow("Issuing authority", record.issuing_authority) +
        metaRow("Topic", record.uas_topic) +
        metaRow("Regulated party / activity", [record.regulated_party, record.regulated_activity].filter(Boolean).join(" — ")) +
        metaRow("Requirement", [record.requirement_type, record.permit_or_approval_required ? "Permit/approval: " + record.permit_or_approval_required : ""].filter(Boolean).join(" · ")) +
      "</dl>" +
      '<section class="reg-block objective-block"><h4>Objective Summary</h4><p>' + escapeHtml(record.summary || "") + "</p></section>" +
      '<section class="reg-block interpretation-block"><h4>AI Practical Interpretation</h4><div class="perspective-grid">' +
        perspectivePanel("AEC Industry UAS Expert", record.practical_interpretation_aec_expert, "perspective-aec") +
        perspectivePanel("Agency Practitioner", record.practical_interpretation_agency_practitioner, "perspective-agency") +
        perspectivePanel("UAS Procurement Expert", record.practical_interpretation_uas_procurement_expert, "perspective-procurement") +
        perspectivePanel("AEC Industry Legal Counsel", record.practical_interpretation_legal_counsel, "perspective-legal") +
      "</div></section>" +
      (record.notes ? '<section class="reg-block notes-block"><h4>Research Notes</h4><p>' + escapeHtml(record.notes) + "</p></section>" : "") +
      '<footer class="reg-footer">' +
        (record.source_url ? '<a href="' + escapeHtml(record.source_url) + '" target="_blank" rel="noopener noreferrer">Open cited source <span aria-hidden="true">↗</span></a>' : '<span class="source-missing">Source URL not provided</span>') +
        '<span class="reg-footer-meta">' +
          (record.date_accessed ? "Accessed " + escapeHtml(record.date_accessed) + " · " : "") +
          "Verification: " + escapeHtml(record.verification_status || "Not provided") +
        "</span>" +
      "</footer>";

    header.addEventListener("click", function () {
      setCardOpen(card, body.hidden);
    });

    card.appendChild(header);
    card.appendChild(body);
    return card;
  }

  function setCardOpen(card, open) {
    var body = card.querySelector(".reg-card-body");
    var header = card.querySelector(".reg-card-header");
    if (!body || !header) return;
    body.hidden = !open;
    card.classList.toggle("open", open);
    header.setAttribute("aria-expanded", String(open));
  }

  function matchesFilters(record, query, confidence, relevance) {
    if (confidence && levelClass(record.confidence_level) !== confidence) return false;
    if (relevance && levelClass(record.aec_relevance) !== relevance) return false;
    if (!query) return true;

    var haystack = [
      record.source_title, record.citation, record.uas_topic, record.summary,
      record.issuing_authority, record.regulated_party, record.regulated_activity,
      record.practical_interpretation_aec_expert, record.practical_interpretation_agency_practitioner,
      record.practical_interpretation_uas_procurement_expert, record.practical_interpretation_legal_counsel,
      record.record_id, record.notes
    ].join(" ").toLowerCase();
    return haystack.indexOf(query.toLowerCase()) !== -1;
  }

  function renderRegisterList() {
    var query = registerSearch.value.trim();
    var confidence = registerFilterConfidence.value;
    var relevance = registerFilterRelevance.value;
    var fragment = document.createDocumentFragment();
    var shown = 0;

    currentRecords.forEach(function (record, index) {
      if (!matchesFilters(record, query, confidence, relevance)) return;
      fragment.appendChild(buildCard(record, index));
      shown++;
    });

    registerList.replaceChildren(fragment);
    registerNoResults.hidden = shown !== 0;
    registerCount.textContent = shown === currentRecords.length
      ? shown + " source" + (shown === 1 ? "" : "s")
      : shown + " of " + currentRecords.length + " sources";
  }

  function announceFilterResult() {
    window.setTimeout(function () {
      announce(registerCount.textContent + " shown in the source register.");
    }, 30);
  }

  registerSearch.addEventListener("input", function () {
    renderRegisterList();
    announceFilterResult();
  });
  registerFilterConfidence.addEventListener("change", function () {
    renderRegisterList();
    announceFilterResult();
  });
  registerFilterRelevance.addEventListener("change", function () {
    renderRegisterList();
    announceFilterResult();
  });

  expandAllBtn.addEventListener("click", function () {
    Array.prototype.forEach.call(registerList.querySelectorAll(".reg-card"), function (card) { setCardOpen(card, true); });
    announce("All visible source records expanded.");
  });

  collapseAllBtn.addEventListener("click", function () {
    Array.prototype.forEach.call(registerList.querySelectorAll(".reg-card"), function (card) { setCardOpen(card, false); });
    announce("All visible source records collapsed.");
  });

  select.addEventListener("change", function () {
    clearHash();
    loadState(this.value, false);
  });

  printBtn.addEventListener("click", function () {
    if (!currentStateData) {
      announce("Select a state before opening the print view.");
      select.focus();
      return;
    }
    window.print();
  });

  downloadJsonBtn.addEventListener("click", function () {
    if (!currentStateData) {
      announce("Select a state before downloading JSON.");
      select.focus();
      return;
    }
    var blob = new Blob([JSON.stringify(currentStateData, null, 2)], { type: "application/json" });
    triggerDownload(blob, currentStateData.state_abbr + ".json");
  });

  downloadCsvBtn.addEventListener("click", function () {
    if (!currentStateData) {
      announce("Select a state before downloading CSV.");
      select.focus();
      return;
    }
    var sourceFiles = currentStateData.source_files || {};
    if (!sourceFiles.source_register_csv) {
      announce("The CSV source register is unavailable for this state.");
      return;
    }
    window.location.href = sourceFiles.source_register_csv;
  });

  function triggerDownload(blob, filename) {
    var url = URL.createObjectURL(blob);
    var link = document.createElement("a");
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }

  if (tocMedia.addEventListener) tocMedia.addEventListener("change", syncTocDisclosure);
  else tocMedia.addListener(syncTocDisclosure);

  document.documentElement.dataset.uiVersion = UI_VERSION;
  syncTocDisclosure();
  loadIndex();
})();
