EXPERIMENT_CONFIG = {
    'pre_2007': {
        'expid': 'e5303_m21c_jan98',
        'strm': 'm21c_ens_strm1'
    },
    '2007_to_2016': {
        'expid': 'e5303_m21c_jan08',
        'strm': 'm21c_ens_strm2'
    },
    '2017_onward': {
        'expid': 'e5303_m21c_jan18',
        'strm': 'm21c_ens_strm3'
    }
}

# TODO: change the import name m21c
# PLOT_FILENAME_TEMPLATE = "M21C_EnsSpread_hovm_{var}_{year}.png"

DEFAULT_VAR3D = ['tv', 'u', 'v', 'sphu', 'ozone']
DEFAULT_VAR2D = ['ps']

BASE_INPUT_PATH = "../data"
BASE_OUTPUT_PLOT_PATH = "../plots"