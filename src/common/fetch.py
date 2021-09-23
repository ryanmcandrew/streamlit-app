import zipfile as zp
import sys, os
import json
from kaggle.api.kaggle_api_extended import KaggleApi

#load json config

api = KaggleApi()
api.authenticate()

k_data_sources = json.load(open(os.getcwd() + '/src/config/kaggle_data_links.json','r'))

it = 0
for i in k_data_sources['kl_data']:
    file = api.dataset_download_file(i['url_path'],
                          file_name=i['filename'],
                          path=os.getcwd() +i['storage_path'])
    
    if zp.is_zipfile(os.getcwd() +i['storage_path'] + i['filename'] + ".zip"):
        with zp.ZipFile(os.getcwd() +i['storage_path'] + i['filename'] + ".zip", 'r') as zipref:
            zipref.extractall(os.getcwd() +i['storage_path'])
            os.remove(os.getcwd() +i['storage_path'] + i['filename'] + ".zip")
