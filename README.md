# OCRSpace

## Development

Run the complete offline response-contract suite from the repository root:

```sh
uv run --isolated --no-project --with requests python -B -m unittest discover -v
```

All HTTP calls are mocked and image inputs are in-memory fixtures. The tests
exercise the real wrapper without uploading files, retrieving URLs or validating
service credentials.

Build the existing setuptools package without publishing it:

```sh
uv build
```

CI runs the complete suite and build on Linux with CPython 3.13, then requires
both the wheel and source distribution.
