import os
import logging
from zipfile import ZipFile
import pandas as pd

data_dir = "data"

def unzip_file():
    if not os.path.exists(data_dir):
        logging.info("Data Directory doesn't exists, Creating one...")
        os.makedirs(data_dir)

        with ZipFile("equity-post-HCT-survival-predictions.zip") as zip_ref:
            zip_ref.extractall(data_dir)
            logging.info("Data extracted successfully..")

def display_data_information():
    # Lod in the dataframe file
    data_information = pd.read_csv("data/data_dictionary.csv")
    print(data_information)

if __name__ == "__main__":
    unzip_file()
    display_data_information()