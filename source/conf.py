# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'notes'
copyright = '2021, Vinay Keerthi'
author = 'Vinay Keerthi'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.todo",
    "sphinx_inline_tabs",
    "sphinx_panels",
    "sphinx_copybutton",
    "sphinx.ext.githubpages",
    "matplotlib.sphinxext.plot_directive",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = "_static/images/stonecharioteer-banner.png"
html_title = "Stonecharioteer's Notes"
serif_fonts = "Newsreader, Garamond, Helvetica, Times New Roman, Serif"
html_theme_options = {
    "navigation_with_keys": True,
    "light_css_variables": {
        "font-stack": serif_fonts
    },
    "dark_css_variables": {
        "font-stack": serif_fonts,
    }
}
html_css_files = ["css/custom.css"]
html_last_updated_fmt = ""

todo_include_todos = True
html_extra_path = ["CNAME"]
