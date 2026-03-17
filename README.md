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

# docs-common

Shared documentation infrastructure for multiple plugin repositories using `MkDocs`, `Material`, and `mike`.

The goal is to centralize, in one place:

- shared MkDocs behavior
- shared styling and assets
- shared deployment workflow
- minimal templates for plugin repositories

## Package Usage

Each plugin repository can install the shared package with `pip`:

```bash
pip install "stellionix-mkdocs @ git+https://github.com/Stellionix/docs-common.git@main"
```

Or from a tagged release:

```bash
pip install "stellionix-mkdocs @ git+https://github.com/Stellionix/docs-common.git@v0.1.0"
```

A minimal plugin-side `mkdocs.yml` looks like this:

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

## Reusable GitHub Actions Workflow

This repository can also centralize the docs deployment workflow itself.

Add the reusable workflow at:

```text
.github/workflows/deploy-docs.yml
```

Then, in each plugin repository, keep only the local triggers and call the shared workflow:

```yml
name: Deploy Docs

on:
  push:
    branches:
      - master
    paths:
      - "docs/**"
      - "mkdocs.yml"
      - "requirements.txt"
      - "build.gradle.kts"
      - "deadchest-plugin/build.gradle.kts"
      - "deadchest-plugin/src/main/resources/plugin.yml"
      - ".github/workflows/docs.yml"
  workflow_dispatch:

jobs:
  deploy:
    uses: Stellionix/docs-common/.github/workflows/deploy-docs.yml@main
```

This keeps plugin repositories focused on:

- local docs content
- local `mkdocs.yml`
- local workflow triggers

And moves the execution logic into `docs-common`:

- checkout
- Python setup
- Java setup
- Gradle setup
- dependency installation
- project version resolution
- `mike` deployment

## Supported Workflow Inputs

The reusable workflow supports these optional inputs:

- `python-version`
- `java-version`
- `working-directory`
- `requirements-path`
- `version-command`
- `deploy-alias`

Example with explicit overrides:

```yml
jobs:
  deploy:
    uses: Stellionix/docs-common/.github/workflows/deploy-docs.yml@main
    with:
      python-version: "3.12"
      java-version: "17"
      working-directory: "."
      requirements-path: "requirements.txt"
      version-command: "./gradlew -q printVersion"
      deploy-alias: "latest"
```
