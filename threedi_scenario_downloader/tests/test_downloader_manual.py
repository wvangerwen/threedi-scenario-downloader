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
            "06c38953-31ec-4f6d-ae1f-ccdf31a348ae",
            "EPSG:28992",
            1000,
            None,
            "C:/Users/emiel.verstegen/Downloads/max_waterdepth.tif",
        )


def test_download_waterdepth_raster():
    if True:
        downloader.download_waterdepth_raster(
            "06c38953-31ec-4f6d-ae1f-ccdf31a348ae",
            "EPSG:28992",
            1000,
            "2016-01-05T03:25:00Z",
            None,
            "C:/Users/emiel.verstegen/Downloads/waterdepth.tif",
        )
