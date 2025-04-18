import pandas as pd
from db_utils import RDSDatabaseConnector

class DataTransformer:
    """
    Methods to handle data transformations.
    """

    def __init__(self, df):
        self.df = df

    def convert_to_category(self, column_name):
        """
        convert a column to dtype category
        """
        self.df[column_name] = self.df[column_name].astype('category')
        return self.df

    def convert_to_datetime(self, column_name):
        """
        convert a column to datetime
        """
        self.df[column_name] = pd.to_datetime(self.df[column_name], format='%b-%Y')
        return self.df
    

    
