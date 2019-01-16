threedi-scenario-downloader
==========================================

Introduction

Usage, etc.


Installation
------------

We can be installed with::

  $ pip install threedi-scenario-downloader

(TODO: after the first release has been made)


Development installation of this project itself
-----------------------------------------------

We're installed with `pipenv <https://docs.pipenv.org/>`_, a handy wrapper
around pip and virtualenv. Install that first with ``pip install
pipenv``. Then run::

    $ PIPENV_VENV_IN_PROJECT=1 pipenv --three
    $ pipenv install --dev

There will be a script you can run like this::

    $ pipenv run run-threedi-scenario-downloader

It runs the `main()` function in `threedi-scenario-downloader/scripts.py`,
adjust that if necessary. The script is configured in `setup.py` (see
`entry_points`).

In order to get nicely formatted python files without having to spend manual
work on it, run the following command periodically::

  $ pipenv run black hydxlib

Run the tests regularly. This also checks with pyflakes, black and it reports
coverage. Pure luxury::

  $ pipenv run pytest

The tests are also run automatically on "travis", you'll see it in the pull
requests. There's also `coverage reporting
<https://coveralls.io/github/nens/threedi-scenario-downloader>`_ on
coveralls.io (once it has been set up).


Steps to do after generating with cookiecutter
----------------------------------------------

- Add a new project on https://github.com/nens/ with the same name. Set
  visibility to "public" and do not generate a license or readme.

  Note: "public" means "don't put customer data or sample data with real
  persons' addresses on github"!

- Follow the steps you then see (from "git init" to "git push origin master")
  and your code will be online.

- Go to
  https://github.com/nens/threedi-scenario-downloader/settings/collaboration
  and add the teams with write access (you might have to ask someone with
  admin rights to do it).

- Update this readme. Use `.rst
  <http://www.sphinx-doc.org/en/stable/rest.html>`_ as the format.

- Ask Reinout to configure travis and coveralls.

- Remove this section as you've done it all :-)
