import requests
import pandas as pd 
from io import StringIO

ENDPOINT = 'https://archive.ics.uci.edu/ml/machine-learning-databases/image/'
TRAIN_FILE = 'segmentation.data'
TEST_FILE = 'segmentation.test'

class DataStore:

    def __init__(self,endpoint=ENDPOINT,files=[TRAIN_FILE,TEST_FILE]):
        self._load_data(endpoint,files)

    def _etl(self,endpoint,file):
        response = requests.get(endpoint + file)
        if response.ok:
            rows = str(response.content).split('\\n')
            header = [rows[3]]
            data = rows[5:-2]
            return "\n".join(header + data)
        else:
            raise Exception("TODO")

    def _load_data(self,endpoint,files):
        dataframes = [pd.read_csv(StringIO(self._etl(endpoint,file))) for file in files]
        self.data = pd.concat(dataframes)

    def build_datasets(self):
        D1 = self.data.iloc[:,4:9]
        D2 = self.data.iloc[:,10:19]
        D3 = self.data.iloc[:,4:19]
        return [D1,D2,D3]





        
    