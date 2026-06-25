# baseline
 
**A production-ready Python project template — tests, CI, Docker, pre-commit, and a production-readiness checklist baked in — so every new project starts shaped right instead of being retrofitted later.**
 
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?style=flat&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
 
> 📋 **This is a template repository.** Click **"Use this template"** to start a new project from it, or clone it directly. Everything below is wired up and ready — the point is that a fresh project is production-shaped from commit one.
 
---
 
## Why this exists
 
The difference between a student repo and a repo a team would trust isn't the feature — it's the scaffolding around it: tests that actually run in CI, a one-command Docker setup, config that isn't hardcoded, and the discipline to take *one* thing all the way to done. Those habits are easy to skip when you're starting fresh and slow to bolt on later.
 
`baseline` makes them the default. Start here and you can't forget the unglamorous parts, because they're already there.
 
---
 
## What's included
 
- **Test suite wired into CI** — `pytest` configured, with a sample unit test and an integration-test layout, so "add a test" is the path of least resistance rather than an afterthought.
- **GitHub Actions CI** — lint, format-check, and test on every push and PR. A green check that actually means something.
- **Dockerfile + docker-compose** — `docker compose up` runs the app (and a Postgres service, ready to delete or keep) with no local setup.
- **Pre-commit hooks** — `black`, `ruff`, and basic hygiene run before every commit, so formatting and lint never reach CI.
- **Config via environment** — a `.env.example` and a typed settings loader; no secrets or hostnames hardcoded.
- **Makefile** — `make test`, `make lint`, `make run`, `make docker` so the common commands are discoverable and identical for everyone.
- **The checklist below** — the part that's actually worth more than any single config file.
---
 
## The production-readiness checklist
 
This is the real payload. Run a project against it before you call it "done." It's the same standard whether the project is a backtester, a matching engine, or a web app — adapt the language specifics, keep the intent.
 
**Tests**
- [ ] Core logic has unit tests, and they run in CI on every push
- [ ] At least one integration test exercises the real boundary (real DB, real file, real request) — not a mock of everything
- [ ] Tests are deterministic (seeded) and don't depend on network or wall-clock time
**Build & run**
- [ ] A newcomer can run it with one documented command (`docker compose up` or equivalent)
- [ ] Dependencies are pinned; the build is reproducible
- [ ] No hardcoded secrets, paths, or hostnames — everything that varies lives in config/env
**Data (if it has any)**
- [ ] Schema changes are versioned migrations, not manual SQL
- [ ] Indexes match the actual query patterns; foreign keys enforce integrity
- [ ] Money/precision uses exact types, never floats
**Quality**
- [ ] Linter and formatter run in CI and pass
- [ ] Errors are handled and logged, not swallowed
- [ ] The README explains what it is, how to run it, and one honest limitation
**Shipping**
- [ ] CI is green and visible (a badge that reflects reality)
- [ ] If it's user-facing, there's a deployed live demo linked at the top of the README
- [ ] One project taken *all the way* here beats five left at 80%
---
 
## Project structure
 
```
baseline/
├── src/
│   └── app/                 # your code goes here
│       ├── __init__.py
│       ├── config.py        # typed settings loaded from env
│       └── main.py
├── tests/
│   ├── unit/
│   └── integration/
├── .github/workflows/ci.yml # lint + format + test
├── .pre-commit-config.yaml
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── pyproject.toml           # deps + tool config (black, ruff, pytest)
└── README.md
```
 
---
 
## Usage
 
```bash
# 1. Start a new project from this template (or clone it)
git clone https://github.com/a0merr/baseline.git myproject
cd myproject
 
# 2. Install dev tooling + hooks
make install        # installs deps and pre-commit hooks
 
# 3. Verify everything's wired up
make test           # runs the suite
make lint           # runs black + ruff
make run            # runs the app
 
# 4. Or bring up the whole thing in Docker
docker compose up --build
```
 
Then rename `src/app/`, gut the sample code, and start building — the scaffolding stays.
 
---
 
## What's in CI
 
The `ci.yml` workflow runs on every push and pull request:
 
1. **Format check** — `black --check`
2. **Lint** — `ruff`
3. **Test** — `pytest` with coverage
The badge at the top of a project using this template reflects that pipeline — so when it's green, it actually means the code is formatted, linted, and tested.
 
---
 
## License
 
Released under the MIT License — see [LICENSE](LICENSE).
 
## Contact
 
**Andrew Merritt** — [GitHub](https://github.com/a0merr) · [LinkedIn](https://www.linkedin.com/in/andrew-merritt-ab425537a) · a0merr05@louisville.edu
