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


    # Line Chart
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
            df_grouped = pd.DataFrame()
            group_by_obj = df_data.groupby(by=[chart_data['xaxis']], as_index=False)
            if chart_data['accumulator'] == 'avg':
                df_grouped = group_by_obj.mean().round(2)
            elif chart_data['accumulator'] == 'sum':
                df_grouped = group_by_obj.sum()
            return {
                **chart_data,
                'chartData': df_grouped.to_dict(orient="records")
            }
        except Exception as ex:
            print(ex)
            return { "errorMsg": ERROR_MSG }


    # Pie Chart
    def save_pie_chart(self, data):
        """ Saves the details of the Pie Chart """
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
                "message": "Chart created successfully",
                "charts": updated_charts
            }
        except Exception as ex:
            print(ex)
            return { "errorMsg": ERROR_MSG }


    def data_pie_chart(self, chart_data):
        """ Return Pie Chart data """
        try:
            query = { '_id': 0, chart_data['showBy']: 1, chart_data['dataField']: 1  }

            df_data = pd.DataFrame(list(DBUtil().get_collection(
                chart_data['collectionName']).find({}, query)))
            
            df_grouped = pd.DataFrame()
            group_by_obj = df_data.groupby(by=[chart_data['showBy']], as_index=False)
            if chart_data['accumulator'] == 'avg':
                df_grouped = group_by_obj.mean().round(2)
            elif chart_data['accumulator'] == 'sum':
                df_grouped = group_by_obj.sum()
            return {
                **chart_data,
                'chartData': df_grouped.to_dict(orient="records")
            }
        except Exception as ex:
            print(ex)
            return { "errorMsg": ERROR_MSG }


    # Bar Chart
    def data_bar_chart(self, chart_data):
        """ Return line Chart data """
        try:
            query = { '_id': 0, chart_data['xaxis']: 1 }

            for line in chart_data['bars']:
                query[line['dataField']] = 1
            
            df_data = pd.DataFrame(list(DBUtil().get_collection(
                chart_data['collectionName']).find({}, query)))
            df_grouped = pd.DataFrame()
            group_by_obj = df_data.groupby(by=[chart_data['xaxis']], as_index=False)
            if chart_data['accumulator'] == 'avg':
                df_grouped = group_by_obj.mean().round(2)
            elif chart_data['accumulator'] == 'sum':
                df_grouped = group_by_obj.sum()
            return {
                **chart_data,
                'chartData': df_grouped.to_dict(orient="records")
            }
        except Exception as ex:
            print(ex)
            return { "errorMsg": ERROR_MSG }
    

    # Get Chart Data
    def get_chart_data(self, chart_id):
        """ Get Chart Data """

        try:
            chart_obj = self.collection.find_one({ 'id': chart_id }, { '_id': 0 })

            response = None
            chart_type = chart_obj['type']

            if chart_type == 'line':
                response = self.data_line_chart(chart_obj)
            elif chart_type == 'pie':
                response = self.data_pie_chart(chart_obj)
            elif chart_type == 'bar':
                response = self.data_bar_chart(chart_obj)
            
            return response
        except Exception as ex:
            print(ex)
            return { "errorMsg": ERROR_MSG }
