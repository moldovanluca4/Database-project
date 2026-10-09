# Web log analysis

The original web log evaluation scripts and their CSV files remain together because the scripts use filenames relative to the current working directory.

Install the analysis dependencies from the repository root with `python -m pip install ".[analytics]"` in an activated virtual environment. The `all` installation option includes these dependencies as well.

Run from this directory:

```sh
cd tools/log_analysis
python3 analyze_logs.py
python3 statistics.py
```

`analyze_logs.py` uses Python's standard library. It reads `/var/log/apache2/access_log` and `/var/log/apache2/error_log`, filters the original campus deployment traffic, and writes `statistics_access.csv` and `statistics_error.csv` in the current directory. Running it replaces those CSV files with results from the available logs.

`statistics.py` reads the CSV files and displays plots using pandas, Matplotlib, and NumPy. It can also be run directly against the included datasets without rerunning log extraction.

The submitted figures and PDF are retained in [docs/evidence/log-analysis](../../docs/evidence/log-analysis/). The scripts keep their original Apache paths, deployment filter, and behavior.
