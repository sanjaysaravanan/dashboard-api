""" Charts Service """
import pandas as pd
import uuid

from service.base import Base
from util.utils import ERROR_MSG
from util.db_util import DBUtil


class Charts(Base):
    """ Charts Service """

    def get_all(self):
        """ Get all the Charts """
        try:
            reports = list(self.collection.find({}, {"_id": 0}))
            return reports
        except Exception as ex:
            print(ex)
            return {
                "errorMsg": ERROR_MSG
            }

    def delete_one(self, chart_id):
        """ Delete one Chart """
        try:
            self.collection.delete_one({"id": chart_id})
            return {
              "message": "Chart Deleted Successfully"
            }
        except Exception as ex:
            print(ex)
            return {
                "errorMsg": ERROR_MSG
            }

    def save_line_chart(self, data):
        """ Store a Line Chart """
        try:

            report_data = DBUtil().get_collection('reports').find_one({ "id": data['reportId'] })

            write_obj = {
              **data,
              "id": str(uuid.uuid4()),
              "collectionName": report_data["collectionName"]
            }

            self.collection.insert_one(write_obj)

            updated_charts = list(self.collection.find({}, {"_id": 0}))

            return {
              "message": "Chart Created Successfully",
              "charts": updated_charts
            }
        except Exception as ex:
            print(ex)
            return {
                "errorMsg": ERROR_MSG
            }

    
    def data_line_chart(self, chart_data):
        """ Return line Chart data """
        try:
            query = { '_id': 0, chart_data['xaxis']: 1 }

            for line in chart_data['lines']:
                query[line['dataField']] = 1
            
            df_data = pd.DataFrame(list(DBUtil().get_collection(
                chart_data['collectionName']).find({}, query)))

            return {
                **chart_data,
                'chartData': df_data.to_dict(orient="records")
            }
        except Exception as ex:
            print(ex)
            return { "errorMsg": ERROR_MSG }
