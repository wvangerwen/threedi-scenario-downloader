# -*- coding: utf-8 -*-
"""TODO Docstring, used in the command line help text."""
import requests

LIZARD_URL = "https://demo.lizard.net/api/v3/"
RESULT_LIMIT = 10
REQUESTS_HEADERS = {}


def get_headers():
    return REQUESTS_HEADERS


def set_headers(username, password):
    REQUESTS_HEADERS["username"] = username
    REQUESTS_HEADERS["password"] = password
    REQUESTS_HEADERS["Content-Type"] = "application/json"


def find_scenarios_by_model_slug(model_uuid):
    """Find all 3Di scenario's produced by the supplied model. User needs to be authorized to view the model results."""
    url = "{}scenarios/?model_name__icontains={}&limit={}".format(
        LIZARD_URL, model_uuid, RESULT_LIMIT
    )
    r = requests.get(url=url, headers=get_headers()).json()["results"]
    return r


def find_scenarios_by_name(name):
    """Find all 3Di scenario's matching the supplied name that the user is authorized for"""
    url = "{}scenarios/?name__icontains={}&limit={}".format(
        LIZARD_URL, name, RESULT_LIMIT
    )
    r = requests.get(url=url, headers=get_headers()).json()["results"]
    return r


def get_netcdf_link(scenario_uuid):
    """Returns the link to the netcdf file of the supplied scenario"""
    r = requests.get(
        url="{}scenarios/{}".format(LIZARD_URL, scenario_uuid), headers=get_headers()
    ).json()
    for result in r["result_set"]:
        if result["result_type"]["code"] == "results-3di":
            url = result["attachment_url"]
            return url


def get_raster(scenario_uuid, raster_code):
    """Returns the raster json object given the scenario-uuid and the requested raster type"""
    r = requests.get(
        url="{}scenarios/{}".format(LIZARD_URL, scenario_uuid), headers=get_headers()
    ).json()
    try:
        for result in r["result_set"]:
            if result["result_type"]["code"] == raster_code:
                return result["raster"]
    except:
        print("No results for given scenario_uuid and raster_code:")
        raise


def create_raster_task(raster, target_srs, resolution, bounds=None, time=None):
    """
    Create a task on the Lizard server to prepare a raster with given SRS and resolution
    Full extent will be used if the bounds are not supplied
    """
    if bounds == None:
        bounds = raster["spatial_bounds"]

    e = bounds["east"]
    w = bounds["west"]
    n = bounds["north"]
    s = bounds["south"]

    source_srs = "EPSG:4326"

    bbox = "POLYGON+(({}+{},{}+{},{}+{},{}+{},{}+{}))".format(
        w, n, e, n, e, s, w, s, w, n
    )

    url = "{}rasters/{}/data/?cellsize={}&geom={}&srs={}&target_srs={}&format=geotiff&async=true".format(
        LIZARD_URL, raster["uuid"], resolution, bbox, source_srs, target_srs
    )
    r = requests.get(url=url, headers=get_headers()).json()
    return r
