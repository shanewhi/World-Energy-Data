# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#Created on Wed Mar 20 13:56:43 2024

#@author: shanewhite
"""


###############################################################################
#
# Module: user_globals.py
#
# Description:
# Globals definitions for application world_energy_data.py.
#
###############################################################################


# Import Python modules.
from enum import Enum


# Define custom class of an energy system.
class Energy_System:
    def __init__(
            self,
            name, # Country name.
            co2_Mt,
            ffprod_EJ,
            primary_PJ,
            primary_final_category_shares,
            primary_final_fuel_shares,
            elecprod_TWh,
            elecprod_final_category_shares,
            elecprod_final_fuel_shares,
            consumption_PJ,
            consumption_final_shares
            ):
        self.name = name
        self.co2_Mt = co2_Mt
        self.ffprod_EJ = ffprod_EJ
        self.primary_PJ = primary_PJ
        self.primary_final_category_shares = primary_final_category_shares
        self.primary_final_fuel_shares = primary_final_fuel_shares
        self.elecprod_TWh = elecprod_TWh
        self.elecprod_final_category_shares = elecprod_final_category_shares
        self.elecprod_final_fuel_shares = elecprod_final_fuel_shares
        self.consumption_PJ = consumption_PJ
        self.consumption_final_shares = consumption_final_shares
        # Final share dataframes are required by treemap function.
        # Better to seperate than place within primary_PJ dataframe.


# Define conversion coefficeints (multiply for conversion).
class Constant(Enum):
    k_TO_M = 1E-3
    TJ_TO_PJ = 1E-3
    EJ_TO_PJ = 1E3
    PJ_TO_EJ = 1 / EJ_TO_PJ
    GJ_TO_PJ = 1E-6
    GJ_TO_EJ = 1E-9
    TONNES_TO_GJ = 41.868 # EI Conversion Factors sheet.
    PRIMARY_ENERGY_CHANGE_START_YEAR = 1966
    ELEC_CHANGE_START_YEAR = 1995
    TFC_START_YEAR = 1990
    TFC_END_YEAR = 2021
    SUPTITLE_FONT_SIZE = "large"
    SUPTITLE_FONT_WEIGHT = "normal"
    SUPTITLE_ADDITION_FONT_SIZE = "x-large"
    SUPTITLE_ADDITION_FONT_WEIGHT = "demibold"
    TITLE_FONT_SIZE = "normal"
    TITLE_FONT_WEIGHT = "medium"
    FOOTER_TEXT_FONT_SIZE = "small"
    FOOTER_TEXT_FONT_WEIGHT = "normal"
    FIG_VSIZE_1x1 = 8.2
    FIG_HSIZE_1x1 = 8
    FIG_VSIZE_SUBPLOT_1X3 = 5.5
    FIG_HSIZE_SUBPLOT_1X3 = 15
    FIG_VSIZE_SUBPLOT_1X4 = 5
    FIG_HSIZE_SUBPLOT_1X4 = 18
    FIG_VSIZE_SUBPLOT_2X3 = 10
    FIG_HSIZE_SUBPLOT_2X3 = 15
    FIG_VSIZE_SUBPLOT_2X4 = 10
    FIG_HSIZE_SUBPLOT_2X4 = 15
    FIG_VSIZE_GROUPED_COLUMN_PLOT = 8.5
    FIG_HSIZE_GROUPED_COLUMN_PLOT = 18
    FIG_VSIZE_TREE_1X2 = 7
    FIG_HSIZE_TREE_1X2 = 12
    LINE_WIDTH_PLOT_1x1 = 4
    LINE_WIDTH_SUBPOLT = 2.5
    LINE_MARKER_SIZE = 5
    CHART_DPI = 100
    CHART_FONT = "Open Sans" #all: matplotlib.font_manager.get_font_names()
    CHART_STYLE = "bmh"     #"default", "seaborn-darkgrid"
# All prebuilt chart styles: https://python-charts.com/matplotlib/styles/#list
# Python chart gallery: https://python-graph-gallery.com/


# Define fuel colors for charts.
class Color(Enum):
    BOLD = '\033[1m'
    CO2 = "black"
    COAL = "black"
    OIL = "brown"
    GAS = "darkorange"
    NUCLEAR = "darkviolet"
    HYDRO = "dodgerblue"
    WIND = "blue"
    SOLAR = "crimson"
    BIOFUELS_AND_WASTE = "sienna"
    OTHER = "peru"
    HEAT = "darkmagenta"
    RENEWABLES = "limegreen"
    WIND_AND_SOLAR = "lime"
    ELECTRICITY = "teal"
    FOSSIL_FUELS = "dimgray"
# Color library: https://matplotlib.org/stable/gallery/color/named_colors.html


# Define dataset as global.
global ei_data_import
ei_data_import = []



