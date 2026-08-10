# Site Connectivity Checker

Site Connectivity Checker is a small Python CLI that checks whether one or more websites are reachable.

## What it does

- Accepts one or more URLs from the command line
- Reads URLs from an input file
- Performs a lightweight HTTP HEAD check against the target host
- Prints whether each site appears online or offline

## Usage

Run the checker directly with one or more URLs:

```bash
python3 -m rpchecker -u example.com github.com
```

Or provide a file containing URLs:

```bash
python3 -m rpchecker -f urls.txt
```

Each line in the input file should contain a single URL.

## Dependencies

The project uses only the Python standard library for runtime behavior. Test support is provided through pytest.

## Testing

Run the test suite with:

```bash
python3 -m pytest -q
```