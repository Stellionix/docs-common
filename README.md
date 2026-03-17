# docs-common

Shared Python package for multiple `MkDocs` + `Material` documentation sites.

The goal is to centralize, in one place:

- shared CSS
- shared MkDocs/Material defaults
- the plugin that injects those defaults
- minimal templates to keep in each plugin repository

## Contents

- `pyproject.toml`: the `stellionix-mkdocs` package
- `src/stellionix_mkdocs/plugin.py`: shared MkDocs plugin
- `src/stellionix_mkdocs/assets/stylesheets/extra.css`: shared CSS
- `templates/mkdocs.plugin.yml`: example minimal `mkdocs.yml` for a plugin repository
- `templates/docs.workflow.yml`: example minimal GitHub Actions workflow for a plugin repository
- `requirements.txt`: development dependencies for working on this repository

## How It Works

Each plugin repository only keeps:

- `docs/*.md`
- a minimal `mkdocs.yml`
- a minimal docs workflow

The shared layer is installed through `pip`, for example:

```bash
pip install "stellionix-mkdocs @ git+https://github.com/<owner>/docs-common.git@main"
```

Or using a tagged version:

```bash
pip install "stellionix-mkdocs @ git+https://github.com/<owner>/docs-common.git@v0.1.0"
```

## Expected Structure In A Plugin Repository

```text
my-plugin/
  docs/
    index.md
    installation.md
    configuration.md
  mkdocs.yml
  .github/workflows/docs.yml
```

## Example Minimal `mkdocs.yml`

```yml
site_name: MyPlugin Documentation
site_url: https://<owner>.github.io/MyPlugin/
repo_url: https://github.com/<owner>/MyPlugin
repo_name: <owner>/MyPlugin

theme:
  name: material

plugins:
  - search
  - stellionix-shared-docs

nav:
  - Home: index.md
  - Installation: installation.md
  - Configuration: configuration.md
```

## What The Plugin Does

The `stellionix-shared-docs` plugin:

- injects the shared CSS into the build
- applies Material defaults when they are missing
- enables common Markdown extensions when they are missing
- sets `extra.version.provider: mike` when nothing else is defined

It is intentionally conservative and does not overwrite values already defined in the plugin repository.

## Recommended Workflow

The plugin repository workflow should:

- check out the plugin repository
- install `mike`
- install `stellionix-mkdocs` from the dedicated shared repository
- read the project version
- run `mike`

The template is available in `templates/docs.workflow.yml`.
