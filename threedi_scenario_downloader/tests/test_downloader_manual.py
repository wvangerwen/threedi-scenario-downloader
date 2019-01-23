# -*- coding: utf-8 -*-
"""Tests for downloader.py"""
from threedi_scenario_downloader import downloader
import configparser


def test_set_headers():
    config = configparser.ConfigParser()
    config.read("threedi_scenario_downloader/tests/testdata/realconfig.ini")
    downloader.set_headers(
        config["credentials"]["username"], config["credentials"]["password"]
    )


def test_download_maximum_waterdepth_raster():
    if True:
        downloader.download_maximum_waterdepth_raster(
            "b41dbf9a-a9ed-4ef3-8929-5e35242fd059",
            "EPSG:28992",
            500,
            None,
            "C:/Users/emiel.verstegen/Downloads/waterdepth.tif",
        )

