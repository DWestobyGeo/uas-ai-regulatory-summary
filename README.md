# State UAS Regulatory Summaries (AEC Reference)

A state-by-state reference on **commercial UAS (drone) regulation** relevant to architecture, engineering, environmental consulting, surveying, GIS, construction, infrastructure inspection, and aerial mapping ("AEC") work — compiled with AI-assisted research.

**⚠️ This is AI-compiled research, not legal advice.** See [`docs/disclaimer.html`](docs/disclaimer.html) (or the "Disclaimer" link on the live site) before using anything in this repository. Every claim is sourced and confidence-rated, but has not been reviewed by an attorney.

**Working on this repo as an AI agent?** Read [`SESSIONS.md`](SESSIONS.md) first -- it is
the session ledger and handoff point for this repo, which is actively edited by more than
one independent AI session.

## Live site

**https://dwestobygeo.github.io/uas-ai-regulatory-summary/**

The site lets you pick a state, navigate a linked table of contents, read its regulatory summary, compare four labeled AI interpretation perspectives, browse and filter the source register, download the underlying data, and switch to a printable view. You can also link directly to a state and section, e.g. [`?state=TX`](https://dwestobygeo.github.io/uas-ai-regulatory-summary/?state=TX).

## What's covered per state

Each completed state has two data products, generated from the same research pass:

- **Regulatory Summary** (Markdown → rendered on the site) — a concise narrative covering statewide statutes/regulations and state-agency requirements, each with an objective summary plus labeled practical interpretation from an AEC industry expert, agency practitioner, UAS procurement expert, and legal counsel.
- **Source Register** (CSV → also exposed as JSON via the API) — one row per authority, with citation, status, binding level, confidence level, and a link to the cited source.

Coverage is currently **state and state-agency level only** — municipal, county, and tribal regulation is deferred to a later research phase and is explicitly noted as out of scope in each state's summary.

[`Agent_Instructions.v6.md`](Agent_Instructions.v6.md) is the high-level governance document: it defines product scope, phase gates, evidence standards, structured-data ownership, provenance, revision control, and quality gates.

Each agent role has separate versioned operating instructions under [`agents/roles/`](agents/roles/). The role directory identifies the fields and document sections each role governs, what it may change, and how it must document record changes. Each subjective practical-interpretation opinion is normally one to three sentences, but may be longer when a material ambiguity, multi-step process, phased requirement, or other genuinely relevant complexity needs additional explanation.

The website role may improve presentation, internal document navigation, restrained links to already-cited sources, accessibility, and responsive behavior, but may not alter regulatory research or add human-review/approval workflows.

## Shared website design system

All states use one shared page shell, renderer, and stylesheet: [`docs/index.html`](docs/index.html), [`docs/app.js`](docs/app.js), and [`docs/style.css`](docs/style.css). State folders supply data, not separate webpages, so improvements to the shared design automatically apply to every existing and future state.

The component standards, design tokens, responsive behavior, accessibility rules, print behavior, and new-state process are documented in [`docs/DESIGN_SYSTEM.md`](docs/DESIGN_SYSTEM.md). Run `python scripts/validate_site.py` after site or state-data changes; the same validation runs automatically in GitHub Actions.

## Repository structure

```
agents/
  roles/
    README.md                       ← role directory, ownership table, and metadata template
    ROLE_TEMPLATE.md                ← template for future role documents
    research-expert.md              ← objective evidence and source-register owner
    aec-industry-uas-expert.md      ← AEC operational interpretation
    agency-practitioner.md          ← agency-process interpretation
    uas-procurement-expert.md       ← acquisition and fleet interpretation
    aec-industry-legal-counsel.md   ← AI legal-risk interpretation
    state-uas-regulatory-burden-analyst.md ← state comparison and burden-index assessment
    editorial-qa-reviewer.md        ← independent AI quality review
    web-ux-ui-editor.md             ← presentation, links, accessibility, and print
Agent_Instructions.v6.md            ← high-level repository governance
methodologies/
  README.md                       ← methodology ownership and change rules
  state-uas-compliance-burden-index.md ← versioned comparative measurement rules
  preflight/
    scbi-v0.1-preflight.md        ← documented test and revision of the provisional method
.github/workflows/
  site-quality.yml                  ← validates roles, shared UI, and state-data contract
docs/                     ← published by GitHub Pages (this is the whole website)
  index.html              ← main state-picker / viewer / print view
  DESIGN_SYSTEM.md        ← design tokens, components, and inheritance process
  ui-release.json         ← UI version and agent provenance
  disclaimer.html          ← full legal disclaimer
  app.js, style.css
  api/
    index.html            ← human-readable API docs; also serves ?state=XX as JSON
    v1/index.html          ← stable alias for the current API version
  data/v1/
    index.json             ← list of all available states
    {STATE}.json            ← full data for one state (summary + source register), used by both the site and the API
    sources/                ← original Markdown + CSV files per state, for download/transparency
build_data.py               ← regenerates docs/data/v1/*.json from the source /States folders (run this after adding/updating a state)
scripts/validate_site.py    ← shared-style and state-data quality gate
scripts/validate_roles.py   ← role metadata, ownership, and governance-link quality gate
scripts/validate_methodologies.py ← methodology ownership, weights, version, and preflight quality gate
```

## Adding a new state

1. Drop the new state's `XX_UAS_Regulatory_Summary.md` and `XX_UAS_Source_Register.csv` into a `States/XX_StateName/` folder (same format as the existing states — see any existing state for the CSV column schema).
2. Run `python3 build_data.py` to regenerate the JSON data and index.
3. Run `python scripts/validate_site.py` and inspect the new state locally at `?state=XX` on desktop, mobile, and print.
4. Commit and push — the live site picks up the new state and applies the shared design automatically (no state-specific HTML/CSS changes needed).

## API

See [`docs/api/index.html`](docs/api/index.html) (or the "API" link on the live site) for full documentation. Short version: it's a static, read-only, versioned JSON API served straight from files in this repo — `GET /data/v1/{STATE}.json` for a given state, or `GET /data/v1/index.json` to discover which states are available. A convenience wrapper at `/api/index.html?state=TX` returns the same data. Point/extent (lat-lon, bounding-box) queries are on the roadmap but not yet implemented — see the API docs for details.

## Disclaimer

This project is generated by an AI research agent. It is not legal advice, carries no warranty of accuracy, and must not be relied on without independently verifying each cited source. Full terms: [`docs/disclaimer.html`](docs/disclaimer.html).
