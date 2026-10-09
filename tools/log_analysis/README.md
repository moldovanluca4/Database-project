# Web log analysis

Install analysis dependencies from the repository root with `python -m pip install ".[analytics]"` in an activated virtual environment.

The checked-in CSV datasets are sanitized: clients and routes are represented by keyed pseudonyms, browser strings are reduced to families, and error messages are reduced to categories. Column names retain compatibility with the plotting script.

To display the included data:

```sh
cd tools/log_analysis
python statistics.py
```

To analyze private logs, provide your own paths and deployment filters:

```sh
python analyze_logs.py \
  --access-log /private/access.log \
  --error-log /private/error.log \
  --site-url https://campus.example/ \
  --app-path /srv/campus \
  --output-dir output
```

The exporter never copies raw client IPs, route names, full browser strings, or exception details to its CSV output. It uses HMAC-SHA256 pseudonyms with a random key per export. To compare client identities across multiple exports, provide a private `LOG_ANONYMIZATION_KEY` of at least 32 characters through the environment. Keep this key private and separate from exported data. Pseudonymous records still require appropriate access controls.

Exports go into the ignored `output/` directory by default. Plot an export with `cd output` followed by `python ../statistics.py`. The extraction script requires only Python's standard library; plotting uses pandas, Matplotlib, and NumPy.

Sanitized figures are in [docs/evidence/log-analysis](../../docs/evidence/log-analysis/). The historical PDF containing raw client and deployment identifiers was removed.
