# Earlier implementations and prototypes

These directories preserve earlier coursework and experiments separately from the main application.

| Directory | Original material |
| --- | --- |
| [assignment-05/flask](assignment-05/flask/) | The earlier Campus Information Center Flask/SQLAlchemy implementation. |
| [assignment-05/php](assignment-05/php/) | The PHP test implementation, including its forms, feedback pages, shared includes, and images. |
| [prototypes/autocomplete](prototypes/autocomplete/) | The standalone autocomplete HTML experiment. |
| [prototypes/public_html](prototypes/public_html/) | The original `public_html` tree, including the `new_design` Flask prototype. |

Each implementation retains its own templates, styles, assets, and entry point. Relative paths inside each implementation are preserved. Security fixes now apply to the archived code too: Flask entry points require a private `FLASK_SECRET_KEY`, debug mode is disabled, and feedback suppresses error details and escapes messages.

The archived SQLAlchemy application requires a private `config.py`; use the environment loader from `apps/campus_information_center/config.example.py`. The PHP implementation reads `DB_HOST`, `DB_USER`, `DB_PASS`, and `DB_NAME` from its process environment and returns generic error responses. It requires PHP with the mysqli extension. No database credentials are included in its source.

`public_html` is preserved as a historical deployment artifact; moving it here does not change any externally hosted copy. The original implementation notes remain in their respective directories.
