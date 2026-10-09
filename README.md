# Epochegret

Exact offline UTC Unix timestamp conversion. Python 3.9+, no dependencies. Published in a private GitHub repository. Download its ZIP while signed into the owner account, extract it and open a terminal inside the source folder. Not verified as store-installed.

```text
python3 epochegret.py
python3 epochegret.py --json
python3 -m unittest -v
bash app-store.sh install
bash app-store.sh run
```

Interactive menu converts integer Unix seconds, integer Unix milliseconds, or ISO datetime. Choose unit explicitly: never guesses based on digits. Signed integer epoch values up to 18 digits accepted, subject to Python datetime years 1..9999. UTC epoch is 1970-01-01T00:00:00Z. Negative values supported.

ISO form: YYYY-MM-DDTHH:MM:SS[.ffffff]Z or signed HH:MM offset. Uppercase T/Z required. Exactly 1..6 fractional digits when fraction used. Rejects missing offset, date-only, leap seconds and normalized invalid offsets. Uses that numeric offset, not IANA zones or local DST rules. No scheduling, current-clock lookup or timezone inference.

Output UTC ISO plus integer epoch seconds/milliseconds/microseconds. Seconds or milliseconds are null/None if timestamp isn't exactly representable in that integer unit. Never silently rounds, including negative epochs. --json puts the object on stdout; interactive prompts on stderr. No files, saved history, network or clock changes. Bounds errors return 2; exit menu 0 cancels.

17 tests cover epoch zero, positive/negative units, exact precision, offsets, leap date, naive rejection, overflow and invalid syntax. Linux tested; Pi/non-Linux untested. Marker/version1.0.0 published. The current public-only Pi App Store cannot discover private repositories; authenticated store support is not verified.

Fullscreen update: Store interactive launch uses terminal-sized board cells or wrapped full-terminal utility input/results with PgUp/PgDn scrolling. Original core rules and direct CLI commands remain unchanged. Ctrl+C cancels utility entry, result Enter returns; no new dependency downloads. Linux PTY resize/restoration checked; physical Pi untested.
