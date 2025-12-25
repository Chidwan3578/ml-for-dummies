from pathlib import Path
import os


CONFIG_FILE_PATH = Path(__file__) 

#getting the project root 

PROJECT_ROOT = CONFIG_FILE_PATH.parent.absolute()

# creating directories

DATASET_DIR = PROJECT_ROOT / 'practiceDatasets'
NOTEBOOK_DIR = PROJECT_ROOT / 'practiceExercise'

#Defining dataset paths

MOBILE_CUSTOMERS_DATA = DATASET_DIR / 'mobile_customers.csv'