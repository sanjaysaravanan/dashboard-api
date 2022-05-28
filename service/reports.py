""" Graph Generation Service """
import pandas as pd
import uuid

from service.base import Base
from util.utils import words_to_snake_case
from util.db_util import DBUtil


class Reports(Base):
    """ Reports Service """

    def get_all(self):
        """ Get all the Reports """
        reports = list(self.collection.find({}, {"_id": 0}))
        return reports
    
    def delete_one(self, report_id):
        """ Delete one Report """
        try:

            report_data = self.collection.find_one({"id": report_id}, {"_id": 0})

            if report_data:
                collection_name = words_to_snake_case(report_data["name"])
                DBUtil().get_collection(collection_name).drop()

            self.collection.delete_one({ "id": report_id })

            return {
                "message": "Report Deleted Successfully"
            }
        except Exception as ex:
            print(ex)
            return {
                "errorMsg": "Something went wrong, please try after some time"
            }

    def file_to_dataframe(self, file, data):
        """ Convert the uploaded file to dataframe """

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

        collection_name = words_to_snake_case(data["name"])
        collection_data = df.to_dict(orient="records")

        data_collection = DBUtil().get_collection(collection_name)
        data_collection.insert_many(
            collection_data
        )

        try:
            write_obj = {
                **data,
                "fields": list(df.columns),
                "collectionName": collection_name,
                "objectFields": object_fields,
                "dataFields": data_fields,
                "id": str(uuid.uuid4())
            }

            self.collection.insert_one(write_obj)
            write_obj.pop('_id')

            updated_reports = list(self.collection.find({}, {"_id": 0}))

            return {
                'message': 'Report created',
                "reports": updated_reports
            }
        except Exception as ex:
            print(ex)
            return {
                "errorMsg": "Something went wrong, please try after some time"
            }
