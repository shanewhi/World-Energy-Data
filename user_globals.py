# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created on Wed Mar 20 14:19:37 2024
# @author: shanewhite

# Import Python modules
from enum import Enum

# Define conversion coefficeints (multiply for conversion)

class Constant(Enum):
    THOUSAND_TO_MILLION = 1 / 1000
    FIG_SIZE = 8
    FIG_HSIZE_SUBPLOT_1X3 = 15
    FIG_VSIZE_SUBPLOT_1X3 = 5
    FIG_HSIZE_SUBPLOT_2X3 = 15
    FIG_VSIZE_SUBPLOT_2X3 = 10
    FIG_HSIZE_PIE_1X2 = 12
    FIG_VSIZE_PIE_1X2 = 6
    FIG_HSIZE_TREE_1X2 = 14
    FIG_VSIZE_TREE_1X2 = 7
    LINE_WIDTH_SUBPOLT = 2.5
    LINE_MARKER_SIZE = 5
    CHART_FONT = 'Open Sans' #all: matplotlib.font_manager.get_font_names()
    CHART_STYLE = 'bmh'     #'default', 'seaborn-darkgrid'
# All prebuilt chart styles: https://python-charts.com/matplotlib/styles/#list


# Define fuel colors for charts
# https://matplotlib.org/stable/gallery/color/named_colors.html

class Color(Enum):
     COAL = 'black'
     OIL = 'brown'
     GAS = 'darkorange'
     NUCLEAR = 'darkmagenta'
     HYDRO = 'dodgerblue'
     WIND = 'blue'
     SOLAR = 'crimson'
     GEO_BIO_OTHER = 'sienna'
     OTHER = 'tan'
     FOSSIL_FUELS = 'dimgray'
     RENEW = 'forestgreen'
     WIND_SOLAR = 'limegreen'
     ELECTRICITY = 'teal'
#Python chart gallery: https://python-graph-gallery.com/

# Define custom class of a country specific energy system

class Energy_System:
    def __init__(
            self,
            name, #country name
            coalprod_Mt,
            oilprod_Mbpd,
            gasprod_bcm,
            primary_EJ,
            coal_primary_EJ,
            oil_primary_EJ,
            gas_primary_EJ,
            nuclear_primary_EJ,
            hydro_primary_EJ,
            wind_primary_EJ,
            solar_primary_EJ,
            geo_bio_other_primary_EJ):
        self.name = name
        self.coalprod_Mt = coalprod_Mt
        self.oilprod_Mbpd = oilprod_Mbpd
        self.gasprod_bcm = gasprod_bcm
        self.primary_EJ = primary_EJ
        self.coal_primary_EJ = coal_primary_EJ
        self.oil_primary_EJ = oil_primary_EJ
        self.gas_primary_EJ = gas_primary_EJ
        self.nuclear_primary_EJ = nuclear_primary_EJ
        self.hydro_primary_EJ = hydro_primary_EJ
        self.wind_primary_EJ = wind_primary_EJ
        self.solar_primary_EJ = solar_primary_EJ
        self.geo_bio_other_primary_EJ = geo_bio_other_primary_EJ
