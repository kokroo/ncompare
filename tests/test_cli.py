# Copyright 2024 United States Government as represented by the Administrator of the
# National Aeronautics and Space Administration. All Rights Reserved.
#
# This software calls the following third-party software,
# which is subject to the terms and conditions of its licensor, as applicable.
# Users must license their own copies; the links are provided for convenience only.
#
# dask - https://github.com/dask/dask/blob/main/LICENSE.txt
# netCDF4 - https://github.com/Unidata/netcdf4-python/blob/master/LICENSE
# numpy - https://github.com/numpy/numpy/blob/main/LICENSE.txt
# xarray - https://github.com/pydata/xarray/blob/main/LICENSE
# Python Standard Library - https://docs.python.org/3/license.html#psf-license
#
# The STITCHEE: STITCH by Extending a dimEnsion platform is licensed under the
# Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

import os

from ncompare.console import _cli


def test_console_version():
    exit_status = os.system('ncompare --version')
    assert exit_status == 0


def test_console_help():
    exit_status = os.system('ncompare --help')
    assert exit_status == 0


def test_arg_parser():
    parsed = _cli(["first_netcdf.nc", "second_netcdf.nc"])

    assert getattr(parsed, "nc_a") == "first_netcdf.nc"
    assert getattr(parsed, "nc_b") == "second_netcdf.nc"
    assert getattr(parsed, "show_attributes") is False
    assert getattr(parsed, "show_chunks") is False
    assert getattr(parsed, "only_diffs") is False
