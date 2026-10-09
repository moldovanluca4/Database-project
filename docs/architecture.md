# Repository architecture

## Component responsibilities

The repository separates executable applications, database assets, documentation, supporting tools, and historical material.

- **Application:** `apps/campus_information_center/` holds the Flask entry points and their shared UI resources. Request handling and database access remain in the original Python modules.
- **Database:** `database/` holds schema definitions, sample data, queries, user-table SQL, and an independent join exercise.
- **Documentation:** `docs/` holds schema design material, coursework PDFs, deployment references, and submitted execution evidence.
- **Tools:** `tools/log_analysis/` holds the log analysis scripts with the datasets they read and write.
- **Archive:** `archive/` holds previous implementations and experiments, each with its own resources.

## Runtime boundaries

Flask discovers templates and static resources relative to each entry point's directory. Every application was moved together with its `templates/` and `static/` directories. The main Flask variants remain siblings so their shared resources and local `config` import continue to use the same relative layout.

The PHP implementation retains its page filenames, shared includes, stylesheet, and image directory. Log analysis scripts retain their CSV files in the same working directory. Python, PHP, HTML, CSS, JavaScript embedded in HTML, SQL, datasets, and submitted assets were relocated without editing their contents.

This is a repository organization change. It does not introduce an application factory, service layer, new database migrations, dependency upgrades, or changes to routes and queries. Such changes would require a separate code refactor.

## Relocation guide

| Previous location | Current location |
| --- | --- |
| `The flask app/` | [apps/campus_information_center/](../apps/campus_information_center/) |
| `ISA hierarchies implementation/` | [database/schema/](../database/schema/) |
| `Data/` | [database/seeds/](../database/seeds/) |
| SQL files in `Queries/` | [database/queries/](../database/queries/) |
| `Join/` | [database/examples/joins/](../database/examples/joins/) |
| `User Handling - Assignment 7 - Security II/` | [database/security/](../database/security/) |
| `Database scheme/` | [docs/schema/](schema/) |
| PDFs in `Assignments/` | [docs/coursework/](coursework/) |
| Building query execution logs | [docs/evidence/queries/buildings/](evidence/queries/buildings/) |
| Event query execution logs | [docs/evidence/queries/events/](evidence/queries/events/) |
| Venue query execution logs | [docs/evidence/queries/venues/](evidence/queries/venues/) |
| Scripts and CSVs in `Assignment 8 - Web Log Evaluation/` | [tools/log_analysis/](../tools/log_analysis/) |
| Figures and PDF in `Assignment 8 - Web Log Evaluation/` | [docs/evidence/log-analysis/](evidence/log-analysis/) |
| `Assignment 5 - Campus Information Center (correct)/` | [archive/assignment-05/flask/](../archive/assignment-05/flask/) |
| `Assignments/Assignment 5/` | [archive/assignment-05/php/](../archive/assignment-05/php/) |
| `Assignment 9 - Autocomplete/` | [archive/prototypes/autocomplete/](../archive/prototypes/autocomplete/) |
| `public_html/` | [archive/prototypes/public_html/](../archive/prototypes/public_html/) |
| `Project landing page URL.odt` | [docs/deployment/landing-page.odt](deployment/landing-page.odt) |

### File naming

Schema, seed, and query files now use `buildings.sql`, `venues.sql`, and `events.sql` within their respective directories. The join exercise uses `schema.sql`, `data.sql`, and `queries.sql`; the user-table definition uses `users.sql`.

Schema diagram artifacts use `schema.drawio`, `schema.png`, and `schema.html`; the written description uses `schema-description.txt`. The original draw.io backup is retained. Coursework PDFs use `assignment-01-team-els.pdf` and `assignment-04-cd.pdf`. Original runtime filenames, screenshot names, and report filenames are preserved.

### Repository hygiene

Tracked `.DS_Store` files, Python bytecode caches, and local IntelliJ project metadata were removed. Ignore rules exclude regenerated metadata, Python environments, credentials, and local database configuration. The shared VS Code live-server setting is retained.

## Running after relocation

Update local launch commands or external deployment configuration that referenced an old repository path to use the paths above. Application entry point filenames, internal resource layout, routes, and the scripts' historical server paths are unchanged. No external server configuration was edited as part of this reorganization.
