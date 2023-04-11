import requests
import pandas as pd 
import os
from io import StringIO

conf = {
    'endpoint': 'https://archive.ics.uci.edu/ml/machine-learning-databases/image/',
    'files': ['segmentation.data','segmentation.test'],
    'local_datapath': '../local/',
    'datafile': 'data.csv',
    'seed': 11
}

class DataStore:

    def __init__(self,conf=conf):
        self._load_data(conf['endpoint'],conf['files'],conf['local_datapath'],conf['datafile'])
        self.seed = conf['seed']

    def _etl(self,endpoint,file):
        response = requests.get(endpoint + file)
        if response.ok:
            rows = str(response.content).split('\\n')
            header = [rows[3]]
            data = rows[5:-2]
            return "\n".join(header + data)
        else:
            raise Exception("TODO")

    def _load_data(self,endpoint,files,datapath,datafile):
        filepath = datapath + datafile
        if not os.path.exists(filepath):
            if not os.path.exists(datapath):
                os.makedirs(datapath)
            dataframes = [pd.read_csv(StringIO(self._etl(endpoint,file))) for file in files]
            self.data = pd.concat(dataframes)
            self.data.to_csv(filepath)
        else:
            self.data = pd.read_csv(filepath)

    def build_datasets(self):
        D1 = self.data.iloc[:,4:9]
        D2 = self.data.iloc[:,10:19]
        D3 = self.data.iloc[:,4:19]
        return [D1,D2,D3]





        
    