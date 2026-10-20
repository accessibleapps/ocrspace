# Report provider processing errors through APIError

## Goal

Handle documented top-level OCR error responses before indexing ParsedResults. Smallest slice: read the JSON payload once and check IsErroredOnProcessing in each existing method (approximately eight source lines), a local mocked response regression file, and this note. No endpoint, credentials, upload, OCR engine, dependency or public return-shape change.

## State

- Fresh default/base: `3d13e393a7d050613467b9c1fea9c25c4c89704a`; isolated branch modernize/task6-ocrspace in task-6/worktrees/ocrspace. Canonical git-conversions checkout and same-name non-Git user directory remain untouched.
- Read complete ocrspace.py/setup.py (version0.1; requests dependency), actual Chicken Nugget OCR initializer and interface.py:1253-1296 consumer/error handling.
- No local guidance, notes, existing tests, hosted CI, lock, hooks configuration or documented full-check command exists at base.
- Primary schema: https://ocr.space/ocrapi documents top-level IsErroredOnProcessing/ErrorMessage separately from per-page ParsedResults. Provider support evidence https://forum.ui.vision/t/internal-processing-error/5180 contains an actual processing-error response without ParsedResults. Tests use that response shape, not a live service.
- All HTTP calls are patched; file inputs are local BytesIO fixtures. No file upload, URL retrieval, API-key validation or OCR request is performed.
- Red: `python -B -m unittest -v test_ocrspace.py` ran the entire sole suite on CPython3.13.6. Both documented provider-error subcases raised KeyError('ParsedResults') instead of APIError; existing success-shape and per-page-error characterization cases passed (3 tests,2 errors).
- Green: the same complete sole-suite command passed all3 tests in0.002s after the two method checks. No dependency resolver, build or live API operation was run.

## Decisions and why

Use the existing APIError with the provider's original ErrorMessage before page indexing. Keep existing per-page errors and successful URL single-result/file list returns. Do not introduce a shared response abstraction or change partial-page handling beyond the provider's explicit error flag.

## Next step

Inspect and commit only ocrspace.py, test_ocrspace.py and this note, then send the exact patch for coordinator review before publication. Focused mocked tests do not claim live OCR/provider interoperability.
