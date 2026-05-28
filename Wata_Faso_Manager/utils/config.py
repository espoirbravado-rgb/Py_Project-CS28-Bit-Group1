#  CONFIG.PY

"""Global configuration module for the WattaFaso-Manager application.

"""



import os

# Automatic creation of the folder if it does not exist
DATA_FOLDER = "data"
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# Updated paths to the subfolder

STOCK_PATH = os.path.join(DATA_FOLDER, "subscribed.txt")
HISTORY_PATH = os.path.join(DATA_FOLDER, "history.txt")

SOCIAL_RATE = 250
COMMERCIAL_RATE = 450
MAINTENANCE_TAX = 1000

MAX_CONSUMPTION_LIMIT = 500

FUEL_STOCK_LITERS  = 150
CRITICAL_FUEL_THRESHOLD  = 30

# END OF CONFIG.PY CODE
