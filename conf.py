# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Borneo-IoT Project'
copyright = '2024-2025, Wei Li. All rights reserved'
author = 'Wei Li'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_wagtail_theme',
    "sphinx_design",
    "sphinxcontrib.googleanalytics",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

googleanalytics_id = "G-L9QEFR1ELW"
googleanalytics_enabled = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_wagtail_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

html_js_files = [
    'custom.js',
]

html_logo = "_static/borneo-logo.png"
html_show_copyright = True
html_show_sphinx = False

default_dark_mode = False

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
#    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]


html_theme_options = dict(
    project_name = "Borneo-IoT Project",
    logo = "borneo-logo.png",
    logo_alt = "Wagtail",
    logo_height = 59,
    logo_url = "/",
    logo_width = 45,
    github_url = "https://github.com/borneo-iot/docs.borneoiot.com/",

    header_links = "Website|https://www.borneoiot.com, GitHub Project|https://github.com/oldrev/borneo",

    footer_links = "",
    #, ",".join([
    #    "About Us|http://example.com/",
    #    "Contact|http://example.com/contact",
    #    "Legal|http://example.com/dev/null",
    #]),

)