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

    def create_datasets(self):
        '''
        D1 = 
        D2 = 
        D3 = 
        return [D1,D2,D3]
        '''
        pass
        
import pandas as pd
D1
data.drop(["REGION-CENTROID-ROW","REGION-PIXEL-COUNT","SHORT-LINE-DENSITY-5","RAWRED-MEAN","RAWBLUE-MEAN","RAWGREEN-MEAN","EXRED-MEAN","EXBLUE-MEAN","EXGREEN-MEAN","VALUE-MEAN","SATURATION-MEAN","HUE-MEAN",""], axis=1, inplace=True)
print(Data)

D2
data.drop(["REGION-CENTROID-ROW","REGION-PIXEL-COUNT","SHORT-LINE-DENSITY-5","SHORT-LINE-DENSITY-2","VEDGE-MEAN","VEDGE-SD","HEDGE-MEAN","HEDGE-SD","INTENSITY-MEAN"], axis=1, inplace=True)
print(Data)

D3
data.drop(["REGION-CENTROID-ROW","REGION-PIXEL-COUNT","SHORT-LINE-DENSITY-5"], axis=1, inplace=True)
print(data)





        
    