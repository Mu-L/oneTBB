# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

SOURCE_DIR = os.path.dirname(__file__)
LATEX_DIR = os.path.join(SOURCE_DIR, '_latex')
PREAMBLE_FILE = os.path.join(LATEX_DIR, 'preamble.tex')
TITLE_PAGE_FILE = os.path.join(LATEX_DIR, 'title_page.tex')

BUILD_TYPE = os.getenv("BUILD_TYPE")

# -- Project information -----------------------------------------------------

if BUILD_TYPE == 'oneapi' or BUILD_TYPE == 'dita':
    project = u'Intel® oneAPI Threading Building Blocks (oneTBB)'
else:
    project = u'oneTBB'
copyright = u'UXL Foundation Contributors'
author = u''

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages', 
    'sphinx_design'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['main/_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
#master_doc = 'main/title_main'
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# Syntax highlighting for the :: directive
highlight_language = 'cpp' 

if BUILD_TYPE == 'oneapi' or BUILD_TYPE == 'dita':
    rst_prolog = """
.. |full_name| replace:: Intel\ |reg|\  oneAPI Threading Building Blocks (oneTBB)
.. |short_name| replace:: oneTBB
.. |product| replace:: oneTBB
.. |reg| unicode:: U+000AE
.. |copy| unicode:: U+000A9
.. |base_tk| replace:: Intel\ |reg|\  oneAPI Base Toolkit
.. |dpcpp| replace:: Intel\ |reg|\  oneAPI DPC++/C++ Compiler
    """
else:
    rst_prolog = """
.. |full_name| replace:: oneAPI Threading Building Blocks (oneTBB)
.. |short_name| replace:: oneTBB
.. |product| replace:: oneTBB
.. |reg| unicode:: U+000AE
.. |copy| unicode:: U+000A9
.. |base_tk| replace:: Intel\ |reg|\  oneAPI Base Toolkit
.. |dpcpp| replace:: Intel\ |reg|\  oneAPI DPC++/C++ Compiler
    """

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

html_theme = 'sphinx_book_theme'

if BUILD_TYPE == 'dita':
    html_theme_options = {
        'repository_url': 'https://github.com/uxlfoundation/oneTBB',
        'path_to_docs': 'doc',
        'repository_branch': 'master'
    }
else:
    html_theme_options = {
        'repository_url': 'https://github.com/uxlfoundation/oneTBB',
        'path_to_docs': 'doc',
        'use_issues_button': True,
        'use_edit_page_button': True,
        'repository_branch': 'master',

    }

    
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

if BUILD_TYPE == 'oneapi'  or BUILD_TYPE == 'dita':
    html_context = {
        'css_files': [
            '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
    }
else:
    html_js_files = ['custom.js']

html_theme_options["logo"] = {"text": "oneTBB Documentation"}
    
html_logo = '_static/oneAPI-rgb-rev-100.png'
html_favicon = '_static/favicons.png'


# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'sphinx-infodevdoc'


# -- Options for LaTeX output ------------------------------------------------

#latex_engine = 'xelatex'
#PDF_TITLE = 'Information Development Template'
#
#with open(PREAMBLE_FILE, 'r', encoding='utf-8') as f:
#    PREAMBLE = f.read()
#
#with open(TITLE_PAGE_FILE, 'r', encoding='utf-8') as f:
#    TITLE_PAGE = f.read().replace('<PDF_TITLE>', PDF_TITLE)
#
#
#latex_elements = {
#    # The paper size ('letterpaper' or 'a4paper').
#    #
#    'extraclassoptions': 'openany,oneside',
#    'babel' : '\\usepackage[english]{babel}',
#    'papersize': 'a4paper',
#    'releasename':" ",
#    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
#    # 'fncychap': '\\usepackage[Lenny]{fncychap}',
#    'fncychap':  '',
#    #'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',
#
#    'figure_align':'htbp',
#    # The font size ('10pt', '11pt' or '12pt').
#    #
#    'pointsize': '12pt',
#
#    # Additional stuff for the LaTeX preamble.
#    #
#    'preamble': PREAMBLE,
#
#    'maketitle': TITLE_PAGE,
#    # Latex figure (float) alignment
#    #
#    # 'figure_align': 'htbp',
#    'sphinxsetup': \
#        'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
#        verbatimwithframe=true, \
#        TitleColor={rgb}{0,0.686,0.941}, \
#        HeaderFamily=\\rmfamily\\bfseries, \
#        InnerLinkColor={rgb}{0,0.686,0.941}, \
#        OuterLinkColor={rgb}{0,0.686,0.941}',
#
#    'tableofcontents':' '
#}
#
#latex_logo = '_latex/intel_logo.png'
## Grouping the document tree into LaTeX files. List of tuples
## (source start file, target name, title,
##  author, documentclass [howto, manual, or own class]).
#latex_documents = [
#    (master_doc, 'sphinx-infodev.tex', u'sphinx-infodev Documentation',
#     u'Intel', 'manual'),
#]

#breathe_projects = {                                       #todd-mod
#    project: "../doxygen/xml"
#}
#breathe_default_project = project

# Setup the exhale extension
#exhale_args = {                                            #todd-mod
#    # These arguments are required
#    "containmentFolder":     "./api",
#    "rootFileName":          "library_root.rst",
#    "rootFileTitle":         "Library API",
#    "doxygenStripFromPath":  "..",
#    "fullApiSubSectionTitle": 'Full API'
#}


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'sphinx-infodev', u'sphinx-infodev Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'sphinx-infodev', u'sphinx-infodev Documentation',
     author, 'sphinx-infodev', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
