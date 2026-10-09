# Campus Information Center

A database course project for managing university buildings, venues, events, and campus resources. The repository includes a Flask application, relational database definitions and sample data, earlier implementations, and coursework evidence.

The database uses ISA hierarchies to represent specialized building, venue, and event types. The web application provides maintenance forms, resource searches, registration, and autocomplete endpoints.

## Tech stack

| Layer | Technologies | Role |
| --- | --- | --- |
| Runtime | Python 3.11+ | Runs the Flask applications and log analysis tools. |
| Web backend | Flask | HTTP routing, form handling, registration, search, and JSON autocomplete endpoints. |
| Database | MySQL / MariaDB, SQL | Stores campus entities using relational tables, foreign keys, and ISA hierarchies. |
| Database access | MySQL Connector/Python | Direct database access in `app_v2.py`. |
| Alternative database access | MariaDB Connector/Python; Flask-SQLAlchemy, SQLAlchemy, PyMySQL | Drivers and ORM integration used by earlier and alternative application versions. |
| Frontend | HTML, CSS, Jinja2, JavaScript | Server-rendered pages, forms, styling, and interactive searches. The standalone autocomplete prototype uses jQuery UI. |
| Log analysis | pandas, Matplotlib, NumPy | Processes CSV datasets and visualizes web access and error statistics. |
| Historical implementation | PHP | Earlier form-based implementation preserved in the archive. |
| Dependency installation | pip, `pyproject.toml`, setuptools | Declares and installs Python dependencies, with optional groups for other implementations and tools. |
| Code checks and tests | Ruff, pytest, GitHub Actions | Lints Python code, checks test formatting, and runs automated application tests. |

## Repository layout

```text
.
├── apps/
│   └── campus_information_center/   # Flask entry points, templates, and static assets
├── database/
│   ├── schema/                      # Building, venue, and event definitions
│   ├── seeds/                       # Sample data by domain
│   ├── queries/                     # Query examples by domain
│   ├── security/                    # User table definition
│   └── examples/joins/              # Separate join exercise and its dataset
├── docs/
│   ├── architecture.md              # Component boundaries and relocation guide
│   ├── schema/                      # ER diagram sources, exports, and description
│   ├── coursework/                  # Assignment PDFs
│   ├── deployment/                  # Original landing page reference
│   └── evidence/                    # Query screenshots and log analysis figures
├── tools/
│   └── log_analysis/                # Log processing scripts and CSV datasets
├── archive/
│   ├── assignment-05/              # Earlier Flask and PHP implementations
│   └── prototypes/                 # Autocomplete experiment and public_html design
├── tests/                          # Main Flask application regression tests
├── .github/workflows/checks.yml     # Automated lint and test checks
└── pyproject.toml                  # Python dependency installation configuration
```

## Installation

The [pyproject.toml](pyproject.toml) file is read by pip. From the repository root, create a virtual environment and install the main application's dependencies:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install .
```

On Windows PowerShell, activate the environment with `.venv\Scripts\Activate.ps1`.

To install **all Python dependencies** for the application variants and log analysis tools, use:

```sh
python -m pip install ".[all]"
```

You can also install only the additional components you need:

| Command | Additional dependencies |
| --- | --- |
| `python -m pip install ".[sqlalchemy]"` | SQLAlchemy application variants, including the archived Flask application. |
| `python -m pip install ".[legacy]"` | MariaDB driver used by `app_v1.py`. |
| `python -m pip install ".[analytics]"` | pandas, Matplotlib, and NumPy for log analysis. |
| `python -m pip install ".[dev]"` | Ruff and pytest for development checks. |

The `legacy` and `all` installations retain MariaDB Connector/Python 1.x compatibility. If a source build is required, install MariaDB Connector/C 3.3.1+, Python development headers, and a C compiler first; these are operating system dependencies. See the [MariaDB installation guidance](https://mariadb.com/docs/connectors/mariadb-connector-python/faq).

The TOML configuration installs Python libraries. Supply a MySQL/MariaDB database server and application credentials separately; the archived PHP implementation also requires a PHP runtime. Run the applications from this checkout using the commands below.

## Working with the application

The main application lives in [apps/campus_information_center](apps/campus_information_center/README.md). `app_v2.py` is the newest numbered entry point in the repository; `app_v1.py` and the SQLAlchemy variant remain available in the same directory because they share templates and static assets.

After installing dependencies, provide an accessible MySQL-compatible database and a local `apps/campus_information_center/config.py` defining `DB_HOST`, `DB_USER`, `DB_PASS`, and `DB_NAME`. This file is excluded from version control. For example:

```python
DB_HOST = "localhost"
DB_USER = "campus_user"
DB_PASS = "replace-with-your-database-password"
DB_NAME = "campus_information_center"
```

With those prerequisites available, run from the repository root:

```sh
cd apps/campus_information_center
python app_v2.py
```

The existing entry point starts Flask with debug mode enabled. The repository does not include a production server configuration, a dependency lockfile, or a complete automated database bootstrap.

## Code checks and tests

In your activated virtual environment, run these commands from the repository root:

```sh
python -m pip install ".[dev]"
python -m ruff check .
python -m ruff format --check tests
python -m pytest
```

For all runtime dependencies plus development tools, install `".[all,dev]"`.

[Ruff](https://docs.astral.sh/ruff/linter/) checks Python code for lint errors; [pytest](https://docs.pytest.org/en/stable/) runs the behavior tests. Both are configured in `pyproject.toml`. Ruff checks the application, tools, and tests while excluding the historical archive. Existing one-line conditionals, unused imports, and unused variables have exceptions limited to the affected files and rules so the original application source remains unchanged. Test files use the full configured lint rules and formatting check.

The tests cover public page rendering, static assets, route and method errors, autocomplete JSON responses and parameter binding, and commit, rollback, and resource cleanup for major submissions. Tests inject dummy configuration, mock database access, and fail if a real connection is attempted. They run without credentials or a database server; they do not verify SQL execution against a real schema or exercise the archived applications and log analysis scripts.

The [GitHub Actions workflow](.github/workflows/checks.yml) runs these checks on pushes, pull requests, and manual dispatches using Python 3.11 and 3.14. Its installation needs only the main application and development dependencies.

## Database and supporting material

- [Database guide](database/README.md): schema, sample data, queries, and separate SQL exercises.
- [Architecture and relocation guide](docs/architecture.md): component responsibilities and old-to-new paths.
- [Schema description](docs/schema/schema-description.txt) and [ER diagram](docs/schema/schema.png).
- [Log analysis guide](tools/log_analysis/README.md): working directory, inputs, and dependencies.
- [Archive guide](archive/README.md): previous implementations and prototypes.

## Contributors

The original schema implementation credits Luca with buildings and events, Stefan with venues. The original coursework and implementation notes are retained alongside the corresponding artifacts.
