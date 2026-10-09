# Security fixes and credential recovery

## Current code and data

- Python and PHP application source no longer contains database passwords or fixed Flask signing keys.
- All Flask entry points require a private signing key of at least 32 characters, disable debug mode by default, and use HttpOnly cookies with SameSite=Lax.
- Feedback messages escape HTML and return a generic failure message rather than database or exception details.
- PHP database access uses environment settings; display errors are disabled and uncaught exceptions produce generic responses.
- SQLAlchemy URLs are constructed without string interpolation, and SQL parameter values are hidden in SQLAlchemy error representations.
- Checked-in log datasets and regenerated figures use pseudonymous identifiers and general error categories. New exports use keyed HMAC pseudonyms; generated output and raw `.log` files are ignored.

Use `.env.example` and `apps/campus_information_center/config.example.py` as configuration templates. Supply private values through the server's environment or an ignored local configuration file. Generate a unique signing key for each deployment; never reuse the previously published key. Existing sessions will be invalidated when the key changes.

For production, use HTTPS and a production WSGI server. Configure `SESSION_COOKIE_SECURE=True` in the deployment's Flask settings when serving HTTPS. Avoid enabling Flask's debug mode on exposed servers. See the [Flask configuration guidance](https://flask.palletsprojects.com/en/stable/config/).

## Database credentials already exposed

Historical `config.py` files and the archived PHP connection file contained database credentials. Their present validity was not tested. A code change cannot revoke a password at the database server.

The account owner must rotate or revoke every previously committed database password, update the private deployment settings, and review the affected accounts' access. Replace the old signing key independently. No new production credential is generated or committed by this repository.

## Git history cleanup

Deleting files and adding ignore rules do not remove their previous versions from Git history. A sanitized repository copy is prepared separately for review before replacing the existing history. Cleanup removes historical configuration files and bytecode, raw log datasets and reports, and replaces known exposed credential values in the remaining historical source.

Applying the sanitized history changes commit identifiers. Publishing it requires a coordinated replacement of affected remote refs, followed by fresh clones for collaborators. Cached pull request refs, forks, and other copies may still retain old data. Database credential rotation is required even after history cleanup.

Follow [GitHub's sensitive data removal procedure](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) when applying the reviewed rewrite. Do not force-push until the affected collaborators and repository owner have agreed on the replacement.
