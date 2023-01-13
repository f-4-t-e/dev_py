"""Sphinx configuration."""
project = "Dev_Py"
author = "f4te"
copyright = "2023, f4te"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
