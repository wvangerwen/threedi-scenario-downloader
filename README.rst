threedi-scenario-downloader
==========================================

The threedi-scenario-downloader package includes functions in order to
automate most used download actions on the 3Di results.

Example methods are:

- Download raw results.
- Download logging.
- Download maximum waterdepth (non-temporal raster).
- Download waterdepth (temporal raster, supply timestamp for snapshot).
- Find all scenarios model slug or scenario name.

Examples
========================================
Start importing the package
  
  $ from threedi_scenario_downloader import downloader as dl

Set headers for authentication to the Lizard API
  
  $ dl.set_headers('your_username','your_password')

Find scenarios based on a model slug (unique model identifier) or scenario name. Returns last 10 matching results unless told otherwise.

  $ scenarios = dl.find_scenarios_by_model_slug('enter your model_uuid',limit=10
  
or

  $ scenarios = dl.find_scenarios_by_name('my_first_scenario',limit=100)

Do you want to download the raw 3Di-results (.nc and .h5 files) of a specific scenario? Use the following methods:

  $ download_raw_results('scenario_uuid')
  $ download_grid_administration('scenario_uuid')


  or

  $ download_raw_results('scenario_uuid',pathname='save_under_different_name.nc')
  $ download_grid_administration('scenario_uuid',pathname='save_under_different_name.nc')
  

Installation
------------

We can be installed with::

  $ pip install threedi-scenario-downloader


Development installation of this project itself
-----------------------------------------------

We're installed with `pipenv <https://docs.pipenv.org/>`_, a handy wrapper
around pip and virtualenv. Install that first with ``pip install
pipenv``. Then run::

  $ PIPENV_VENV_IN_PROJECT=1 pipenv --three
  $ pipenv install --dev

In order to get nicely formatted python files without having to spend manual
work on it, run the following command periodically::

  $ pipenv run black threedi_scenario_downloader

Run the tests regularly. This also checks with pyflakes, black and it reports
coverage. Pure luxury::

  $ pipenv run pytest

The tests are also run automatically `on travis-ci
<https://travis-ci.com/nens/threedi-scenario-downloader>`_, you'll see it in
the pull requests. There's also `coverage reporting
<https://coveralls.io/github/nens/threedi-scenario-downloader>`_ on
coveralls.io.

If you need a new dependency (like `requests`), add it in `setup.py` in
`install_requires`. Afterwards, run install again to actuall install your
dependency::

  $ pipenv install --dev
