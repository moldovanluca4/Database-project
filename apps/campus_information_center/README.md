# Flask application

This directory contains the application previously stored in `The flask app/`.

| Entry point | Database integration | Notes |
| --- | --- | --- |
| `app_v2.py` | `mysql.connector` | Latest numbered version; includes autocomplete API routes. |
| `app_v1.py` | `mariadb` | Previous numbered version. |
| `the_app_using_sqlalchemy_notforserver.py` | Flask-SQLAlchemy and PyMySQL | Original alternate implementation, labeled as not for the server. |

All three entry points share `templates/` and `static/`. Keep those directories adjacent to the Python files so Flask's default resource discovery continues to work. Run an entry point from this directory with its existing Python dependencies installed.

Install dependencies from the repository root using `python -m pip install .` for v2, `python -m pip install ".[legacy]"` for v1, or `python -m pip install ".[sqlalchemy]"` for the SQLAlchemy variant. `python -m pip install ".[all]"` includes every variant and the log analysis tools. See the root [installation guide](../../README.md#installation) for virtual environment setup and operating system prerequisites.

Each entry point imports a local `config` module. Provide a private `config.py` here with `DB_HOST`, `DB_USER`, `DB_PASS`, and `DB_NAME`. Configuration and credentials are not part of the tracked application.

Application source, routes, SQL statements, templates, and static assets retain their original contents. Existing template naming inconsistencies and database prerequisites are outside this structural reorganization.
