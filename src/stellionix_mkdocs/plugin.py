from __future__ import annotations

from importlib.resources import files

from mkdocs.config import config_options as c
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File

CSS_DEST_URI = "assets/stylesheets/stellionix-extra.css"
DEFAULT_FEATURES = [
    "navigation.sections",
    "navigation.top",
    "navigation.instant",
    "navigation.tracking",
    "content.code.copy",
    "search.suggest",
    "search.highlight",
]
DEFAULT_PALETTE = [
    {
        "media": "(prefers-color-scheme: light)",
        "scheme": "default",
        "primary": "teal",
        "accent": "amber",
        "toggle": {
            "icon": "material/weather-night",
            "name": "Switch to dark mode",
        },
    },
    {
        "media": "(prefers-color-scheme: dark)",
        "scheme": "slate",
        "primary": "cyan",
        "accent": "amber",
        "toggle": {
            "icon": "material/weather-sunny",
            "name": "Switch to light mode",
        },
    },
]
DEFAULT_MARKDOWN_EXTENSIONS = [
    "admonition",
    "attr_list",
    "md_in_html",
    "tables",
]


class SharedDocsPlugin(BasePlugin):
    config_scheme = (
        ("inject_css", c.Type(bool, default=True)),
        ("apply_material_defaults", c.Type(bool, default=True)),
        ("apply_markdown_defaults", c.Type(bool, default=True)),
        ("enable_mike_version_provider", c.Type(bool, default=True)),
    )

    def on_config(self, config):
        if self.config["apply_material_defaults"]:
            self._apply_theme_defaults(config)

        if self.config["apply_markdown_defaults"]:
            self._apply_markdown_defaults(config)

        if self.config["enable_mike_version_provider"]:
            self._apply_extra_defaults(config)

        if self.config["inject_css"]:
            extra_css = list(config.get("extra_css", []))
            if CSS_DEST_URI not in extra_css:
                extra_css.append(CSS_DEST_URI)
            config["extra_css"] = extra_css

        return config

    def on_files(self, files, config):
        if not self.config["inject_css"]:
            return files

        css_content = (
            files_package("stellionix_mkdocs")
            .joinpath("assets", "stylesheets", "extra.css")
            .read_text(encoding="utf-8")
        )
        files.append(File.generated(config, CSS_DEST_URI, content=css_content))
        return files

    def _apply_theme_defaults(self, config):
        theme = config.get("theme")

        if isinstance(theme, str):
            if theme == "mkdocs":
                config["theme"] = {"name": "material"}
                theme = config["theme"]
            else:
                return

        if theme is None:
            config["theme"] = {"name": "material"}
            theme = config["theme"]

        if hasattr(theme, "setdefault"):
            theme.setdefault("name", "material")
            theme.setdefault("language", "en")
            theme.setdefault("features", list(DEFAULT_FEATURES))
            theme.setdefault("palette", list(DEFAULT_PALETTE))

    def _apply_markdown_defaults(self, config):
        markdown_extensions = list(config.get("markdown_extensions", []))
        for extension in DEFAULT_MARKDOWN_EXTENSIONS:
            if extension not in markdown_extensions:
                markdown_extensions.append(extension)
        config["markdown_extensions"] = markdown_extensions

  def _apply_extra_defaults(self, config):
      extra = dict(config.get("extra", {}) or {})
      version = dict(extra.get("version", {}) or {})
      version.setdefault("provider", "mike")
      extra["version"] = version

      social = list(extra.get("social", []) or [])
      if not social:
          social = [
              {
                  "icon": "fontawesome/brands/github",
                  "link": "https://github.com/Stellionix",
              },
              {
                  "icon": "fontawesome/brands/discord",
                  "link": "https://discord.com/invite/jCsvJxS",
              },
          ]
      extra["social"] = social
      config["extra"] = extra

      if not config.get("copyright"):
          config["copyright"] = "Copyright © Stellionix"


def files_package(package_name: str):
    return files(package_name)
