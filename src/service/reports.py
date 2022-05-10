""" Graph Generation Service """
import json
from attr import fields

import pandas as pd

from service.base import Base


class Reports(Base):
    """ Todos Service """

    def file_to_dataframe(self, file, data):
        """ Convert the uploaded file to dataframe """

        print(data)

        # JSON File
        # data = json.loads(file.read())
        # df = pd.json_normalize(data)

        # CSV File
        # df = pd.read_csv(file)

        # Xls
        df = pd.read_excel(file)
        object_fields = list(df.select_dtypes(include=["object"]).columns)
        data_fields = list(df.select_dtypes(
            include=["float64", "int64"]).columns)
        for t in df.select_dtypes(include=["datetime64"]).columns:
            df[t] = df[t].dt.strftime("%Y-%m-%d")

        try:

            write_obj = {
                **data,
                "fields": list(df.columns),
                # "data": df.to_dict(orient="records"),
                "objectFields": object_fields,
                "data_fields": data_fields,
            }

            self.collection.insert_one(write_obj)
            write_obj.pop('_id')

            return {
                'message': 'Report created',
                'item': write_obj
            }, 201
        except Exception as ex:
            print(ex)
            return {
                "errorMsg": "Something went wrong, please try after some time"
            }, 500
