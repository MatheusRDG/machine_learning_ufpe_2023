import requests
import pandas as pd
import os
from io import StringIO
from .utils import set_seed

set_seed()

conf = {
    "endpoint": "https://archive.ics.uci.edu/ml/machine-learning-databases/image/",
    "files": ["segmentation.data", "segmentation.test"],
    "local_datapath": "./local/",
    "datafile": "data.csv",
}


class DataStore:
    def __init__(self, conf=conf):
        self._load_data(
            conf["endpoint"], conf["files"], conf["local_datapath"], conf["datafile"]
        )

    def _etl(self, endpoint, file):
        response = requests.get(endpoint + file)
        if response.ok:
            rows = str(response.content).split("\\n")
            header = [rows[3]]
            data = rows[5:-2]
            return "\n".join(header + data)
        else:
            raise Exception("TODO")

    def _load_data(self, endpoint, files, datapath, datafile):
        filepath = datapath + datafile
        if not os.path.exists(filepath):
            if not os.path.exists(datapath):
                os.makedirs(datapath)
            dataframes = [
                pd.read_csv(StringIO(self._etl(endpoint, file))) for file in files
            ]
            self.data = pd.concat(dataframes)
            self.data["label"] = self.data.index

            self.data.reset_index()

            self.data.to_csv(filepath)
        else:
            self.data = pd.read_csv(filepath)

    def build_datasets(self):
        """Builds the datasets for the experiments."""
        partition_1 = self.data.iloc[:, 4:9]
        partition_1["label"] = self.data["label"]

        partition_2 = self.data.iloc[:, 10:19]
        partition_2["label"] = self.data["label"]

        partition_3 = self.data.iloc[:, 4:19]
        partition_3["label"] = self.data["label"]

        return partition_1, partition_2, partition_3
