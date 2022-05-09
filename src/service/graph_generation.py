""" Graph Generation Service """
import json

import pandas as pd


class GraphGeneration():
    """ Todos Service """

    def file_to_dataframe(self, file, data):
        """ Convert the uploaded file to dataframe """

        # JSON File
        # data = json.loads(file.read())
        # df = pd.json_normalize(data)

        # CSV File
        # df = pd.read_csv(file)

        # Xls
        df = pd.read_excel(file)
        print(data)
        object_fields = list(df.select_dtypes(include=["object"]).columns)
        data_fields = list(df.select_dtypes(
            include=["float64", "int64"]).columns)
        for t in df.select_dtypes(include=["datetime64"]).columns:
            df[t] = df[t].dt.strftime("%Y-%m-%d")
        return {
            "fields": list(df.columns),
            "data": df.to_dict(orient="records"),
            "objectFields": object_fields,
            "data_fields": data_fields
        }
