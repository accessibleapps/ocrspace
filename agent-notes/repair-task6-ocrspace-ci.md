# Host the existing offline response contracts and package build

## Goal

Add minimal hosted full-test/build coverage to feature PR #1. No source, dependency, provider policy or runtime/support changes. Approximately 35 workflow lines plus command documentation and this living note.

## State

- Verified origin git@github.com:accessibleapps/ocrspace.git; fresh master 3d13e393a7d050613467b9c1fea9c25c4c89704a contains only ocrspace.py/setup.py, with no tests/workflow.
- Original local and published feature heads both 66ce14cc8aaa5e0c476ce46a35ff818f00f87a83. Named backup refs backup/task6-ocrspace-local-before-ci and backup/task6-ocrspace-published-before-ci retain both. Canonical and original feature worktrees clean and unchanged.
- Isolated task-root worktrees/ocrspace-ci on repair/task6-ocrspace-ci starts at the published feature tip. Actual existing tests live only on that feature; no empty baseline prerequisite is appropriate.
- Read global instructions, repair prompts, repository-ci, complete source/setup.py/test and original branch note. No repository/nested guidance/.agents skills found. Actions enabled verified read-only; no settings changed.

## Decisions and why

- Original full four-method unittest suite patches requests.post and uses BytesIO fixture inputs. It exercises actual wrapper behavior for successful/partial pages, missing/empty top-level errors, and existing page errors without any real HTTP operation or credential.
- Use isolated Requests environment from existing setup.py's sole declared runtime dependency. No new lock, manifest version, major dependency update or mock-test rewrite.
- Coordinator explicitly settled narrow build authority: uv build the existing setuptools setup.py package, require exact wheel/source artifacts. This is a nonpublishing package gate, no new build system.
- One Linux/Python 3.13 job on PR/master push, read-only permission, no persisted checkout credentials, no cache/secrets, timeout and concurrency. Immutable action pins and uv 0.13.4 verified from official release metadata/manifests during this session.

## Surprises

Missing CI is a verification gap, not a demonstrated default source/test failure. No new behavioral red regression claimed; no live provider checks.

## Next step

Final new YAML passed actionlint 1.7.12 syntax/expression audit and zizmor 1.31.1 --offline --pedantic with zero findings; optional actionlint shellcheck/pyflakes integrations disabled. Complete added workflow/README/note inspected; source/setup.py/test unchanged from original feature. Commit named files and return exact head for coordinator review before any existing-feature leased publication. Prior full 4-test green results are in the original feature note; no unnecessary local full rerun. Hosted final-head test/build execution awaits publication authority. Actual Claude review is separately coordinated. No push/merge/rebase/settings/release action here.
