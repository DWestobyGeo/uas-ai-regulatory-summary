# State UAS Research Site Design System

**UI version:** 1.4.0

**Agent scope:** `web-ux-ui-editor` v1.4.0

**Applies to:** the public GitHub Pages site under `docs/`

## Purpose

This design system keeps every state research page visually consistent, readable, accessible, and maintainable. It is deliberately content-first: visual treatments clarify evidence, AI interpretation, uncertainty, and navigation without implying flight approval or legal certainty.

## How every state inherits the design

There are no separate handwritten HTML pages for Alaska, Texas, or any other state. Every state uses the same shared presentation layer:

```text
docs/index.html       shared semantic page shell
docs/style.css        shared tokens, components, responsive rules, and print rules
docs/app.js           shared state renderer, TOC generator, filters, and interactions
docs/data/v1/*.json   state-specific research content only
```

`build_data.py` converts each state’s Markdown and CSV source files into the JSON consumed by the shared renderer. When a state is added to `docs/data/v1/index.json`, it automatically appears in the state selector and is rendered through the same HTML, JavaScript, and stylesheet as every existing state.

Consequences:

- Changing a design token or component in `docs/style.css` changes every state.
- Changing a shared interaction in `docs/app.js` changes every state.
- New states must provide data, not new page templates.
- State research files must not contain layout-specific HTML or inline styling.
- `scripts/validate_site.py` and the repository workflow verify the shared contract on every push and pull request.

## Product boundaries

- The site is an AI research and interpretation library, not a flight-clearance system.
- No human-review, legal-approval, or operational-signoff workflow belongs in the interface.
- Do not use color or status labels to imply “legal to fly.”
- Do not collect project, client, location, aircraft, or approval information.
- Keep language neutral to AEC organizations; do not name a specific company.
- The current product scope is state and state-agency research.

## Design principles

### Evidence before decoration

The authority, citation, objective summary, practical interpretation, research notes, source link, and verification status are the primary content. Decorative elements should never compete with them.

### Long-document orientation

State summaries are reference documents, not landing pages. Use a desktop table of contents, mobile disclosure, stable anchors, current-section highlighting, readable line lengths, and clearly separated sections.

### Calm distinction

Differentiate sections with low-saturation surfaces, borders, and spacing. Reserve high-contrast warnings for the AI/not-legal-advice limitation. Never use a red/yellow/green clearance scheme.

### Progressive disclosure

Keep the state narrative visible. Keep source-register records collapsed until requested on screen, while expanding them in print.

### One source of truth

Use shared CSS classes and renderer functions. Do not copy component styles into state files, add inline styles, or create state-specific HTML.

## Design tokens

All reusable values live in `:root` in `docs/style.css`.

### Color families

| Token family | Purpose |
|---|---|
| `--ink-*` | Text hierarchy |
| `--canvas`, `--surface*` | Page, cards, and subtle section backgrounds |
| `--line*` | Borders and dividers |
| `--accent*` | Links, focus context, state navigation, and active TOC state |
| `--teal`, `--sand`, `--violet` | Restrained role and content distinctions |
| `--critical*` | AI/not-legal-advice limitation, and the not-current-law authority flag (see Authority cards) |
| `--news`, `--surface-news` | The conditional "Related news" element (see Authority cards) -- deliberately distinct from `--teal`/`--sand`/`--violet`/`--accent`, which are reserved for the four AI-perspective roles |
| `--focus` | High-visibility keyboard focus |

Confidence colors are deliberately blue, violet, and muted rose rather than traffic-light colors. Confidence remains text-labeled and is never approval.

### Spacing and sizing

- `--space-1` through `--space-7` form the spacing scale.
- `--content-width` limits the primary reading measure to approximately 82 characters.
- `--page-width` controls the overall desktop canvas.
- `--toc-width` controls the navigation rail.
- `--radius-*` and `--shadow-*` provide consistent card depth.

Do not introduce one-off spacing or colors when a token already represents the intent.

## Page anatomy

### Research notice

The compact notice at the top identifies the site as AI-generated research and links to the full disclaimer. It is prominent but not sticky.

### Global header

Contains the product identity and links to the disclaimer, API, and actual repository. It remains organization-neutral.

### State/action bar

Contains the state selector, available-state count, print action, and JSON/CSV downloads. On large screens it may remain visible while reading; on smaller screens it returns to normal document flow.

### Scope status

Reports the current number of included state summaries and the maintenance-first scope. It is not a progress-to-50 indicator.

### State overview

Uses a high-contrast header card for the state name, last update, source count, schema version, and AI-research status.

### Reading layout

- Desktop: sticky TOC rail plus main reading column. The `.reading-layout` grid must use
  the default `align-items: stretch` (do not set `align-items: start`) -- the sticky TOC
  is `position: sticky` on its *own* element (`.page-toc details`), but that only has room
  to hold in place if its grid-item parent (`.page-toc`) stretches to the full row height.
  `start` alignment shrinks the parent to the TOC's own content height, silently breaking
  the stick with no visible error -- it simply scrolls away with the page.
- The current section is tracked with an `IntersectionObserver` and marked both with a
  bold `.active` style and `aria-current="location"` on the corresponding TOC link.
- Tablet/mobile: one column with an “On this page” disclosure.
- The TOC is generated from rendered `h2` and `h3` headings and always includes the Source Register.
- Heading IDs are deterministic and duplicate-safe.

### Summary introduction

Contains document metadata, scope notes, process notes, and the full in-content AI research notice. The state Markdown title is visually presented as a document label rather than a second page-level `h1`.

### Major summary sections

Major `h2` groups receive alternating blue, teal, and sand surfaces. The rotation communicates document structure only; it does not encode legal status.

### Authority cards

Each `h3` authority and its following content is wrapped by the renderer into one card. Objective summaries use a teal edge. AI perspectives use four restrained top-border accents:

- AEC Industry UAS Expert: blue
- Agency Practitioner: teal
- UAS Procurement Expert: sand
- AEC Industry Legal Counsel: violet

These colors distinguish roles only. The surrounding UI must continue to identify them as AI perspectives.

#### Related news (conditional fifth element)

A source-register record may carry an optional `news` array, populated by the
`news-aggregator` role (`agents/roles/news-aggregator.md`) into a per-state, opt-in
`States/XX_StateName/XX_UAS_News.yaml` file and merged onto matching `record_id`s by
`build_data.py`. This is deliberately **not** a fifth AI-perspective panel:

- It is structurally distinct from the four fixed AI-perspective panels (dashed
  left border, a document-icon kicker, and an explicit "informational only, not a
  legal source" disclaimer line) rather than merely a fifth accent color, so the
  difference in kind -- aggregated news items, not an AI interpretive opinion --
  does not depend on color alone.
- Unlike the four fixed perspectives, which governance (Section 6.8) requires to
  always render even as "Not applicable," a record with no genuinely on-topic,
  verified news simply has no `news` array and the section is omitted entirely.
  This is the intentional "revolving cast, hide what has nothing useful" exception
  the four fixed roles do not get -- news is either found or it is not, and an
  empty "no news found" placeholder on the large majority of records that will
  never have any would be noise, not signal.
- Each item shows an explicit **in-state / out-of-state** badge (text label plus a
  solid-vs-dashed border distinction, not color alone) so a reader never mistakes
  another state's news for this state's own. Out-of-state items name the state.
- Each item's `relevance_note` must tie the story specifically to the record's own
  regulatory subject matter -- the role's governing instructions require precision
  over recall (an on-topic story from a related-but-different regulation, e.g. a
  hunting-and-drones story attached to a critical-infrastructure record, must never
  be attached) and require it be omitted rather than force a loose match.
- Rendered only in the Source Register accordion for the matching `record_id` in
  this iteration; the freeform narrative "Statewide"/"State Agency" sections are
  authored/generated Markdown without a structured per-record attachment point, so
  the news element does not yet appear there. A future pass could extend this once
  every state's narrative reliably carries an unambiguous authority-to-record link.

#### Not-current-law flag

An authority whose subtitle line or heading already declares it is not enacted -- using
the register's own established conventions ("Proposed or pending authority", "Repealed,
expired, or superseded authority", a heading ending "-- not current law" or "-- did not
pass") -- is flagged in both the authority card heading and its table-of-contents entry
with the `--critical` color plus a visible "Not current law" text badge. This reads a
classification the research process already wrote into the content; it is not a new
editorial judgment, and it does not use color alone (Section 8). It is a distinct concept
from flight-legality traffic-light styling, which remains prohibited (Section 6.7): this
flag describes the status of the *cited authority itself* (was it ever enacted?), not
whether any activity is permitted.

### Source register

Each record is a keyboard-operable accordion. The collapsed view emphasizes record ID, title, citation, source/status class, relevance, and confidence. The expanded view contains metadata, objective summary, four AI perspectives, research notes, cited source, access date, and verification text.

### Linking model

Links support orientation and evidence verification without overwhelming the research text.

- Internal table-of-contents links target deterministic `h2` and selected useful `h3` anchors.
- State deep links preserve both the selected-state query and section hash.
- Source-register records use stable record-ID anchors when practical.
- A restrained authority-to-record link may be shown only when the renderer can establish the relationship without guessing.
- External evidence links use URLs already present in the state data and descriptive labels such as “View cited source.”
- Do not link every repeated citation or mention; one logical verification link is normally enough.
- Preserve source classification. A link to a normalized publisher, news item, or discovery lead must not be styled or described as official primary authority.
- Missing URLs remain unlinked and are reported to the research role; the presentation layer does not research replacements.
- Link text, focus, visited state, contrast, keyboard behavior, target behavior, and print output must remain accessible.

## Typography

- Use the system UI font stack; do not add remote fonts.
- Body text remains approximately 16 pixels with a 1.65 line height.
- Primary reading content uses a maximum measure near 82 characters.
- Labels use uppercase sparingly for short metadata and section kickers.
- Do not reduce research text below 0.82rem on screen.
- Code and record IDs use the shared monospace token.

## Accessibility standard

Target WCAG 2.2 AA.

- Preserve the skip link and semantic landmarks.
- Use one page-level `h1` for the selected state.
- Maintain a valid heading hierarchy.
- All controls require visible focus and accessible names.
- TOC links use `aria-current="location"` for the active section.
- Source toggles use `aria-expanded` and `aria-controls`.
- State and filter changes announce results through a polite live region.
- Do not use color alone to communicate role, confidence, status, or uncertainty.
- Maintain approximately 44-pixel touch targets.
- Support reflow at 200% zoom and honor reduced-motion preferences.
- Wrap wide tables in a keyboard-focusable scroll region.

## Responsive behavior

| Range | Behavior |
|---|---|
| 1040px and wider | Two-column reading layout with sticky TOC |
| 761–1039px | One-column layout; TOC becomes a disclosure and may use two columns internally |
| 431–760px | Stacked controls, one-column perspectives, stacked source metadata |
| 320–430px | Single-column actions and state metadata |

Breakpoints support content; do not add device-specific overrides without testing all existing ranges.

## Print behavior

- Hide navigation, filters, interactive-only actions, TOC, and decorative controls.
- Print the state overview, research summary, AI limitation, full source register, and print disclaimer.
- Force source records open.
- Avoid separating headings from their first content or splitting compact authority cards when practical.
- Preserve understanding in grayscale and when background printing is disabled.
- Target Letter portrait as the baseline while remaining usable with browser-default paper sizes.

## Editorial style

- Prefer “state research,” “source register,” “AI interpretation,” and “cited source.”
- Do not describe all source links as official when an approved normalized legal publisher may be used.
- Use direct action labels such as “Print view,” “Download JSON,” and “Download CSV.”
- State limitations plainly without repeating full warning copy in every control area.
- Do not write expansion marketing. State current coverage and maintenance priority factually.
- Do not change objective summaries, subjective interpretations, citations, confidence, or verification findings through the UI layer.

## Adding a state

1. Add the state Markdown and CSV source files under `States/XX_StateName/`.
2. Run `build_data.py` to regenerate the shared JSON data.
3. Run `python scripts/validate_site.py`.
4. Serve `docs/` locally and open `?state=XX`.
5. Verify the TOC, long headings, authority cards, tables, source accordion, filters, narrow viewport, and print view.
6. Commit the state source and generated data. Do not create a state-specific HTML or CSS file.

## Changing the design system

1. Change shared tokens or components in `docs/style.css`.
2. Change shared structure in `docs/index.html` only when necessary.
3. Change shared rendering behavior in `docs/app.js`.
4. Increment `ui_version` in `docs/ui-release.json`, the `<html data-ui-version>` attribute, the `style.css?v=` and `app.js?v=` asset URLs, the `UI_VERSION` constant, and the CSS header comment. The asset query versions prevent a newly deployed shell from using stale cached CSS or JavaScript.
5. Update this document when a token, component contract, breakpoint, or content rule changes.
6. Run `python scripts/validate_site.py`.
7. Test at least one short, one medium, and one long state at desktop and mobile widths, plus print.

## Required quality gate

The repository workflow runs `scripts/validate_site.py` for pushes and pull requests that affect the site, state data, build process, agent instructions, or validator. It checks:

- shared stylesheet and JavaScript references;
- required semantic UI hooks;
- synchronized UI version identifiers;
- state-index and JSON integrity;
- record counts and abbreviations;
- presence of the shared design documentation;
- absence of company-specific naming in published/site-governance text.

Passing automation does not replace rendered browser testing for layout changes.
