import pandas as pd

class DataTransformer:
    """
    A class to perform data transformations on a DataFrame.
    """

    def __init__(self, df):
        """
        Initialise the DataTransformer with a DataFrame.

        Args:
            df: The DataFrame to be transformed. 
        """
        self.df = df

    def convert_to_category(self, column_name):
        """
        Convert a column to the 'category' dtype for memory efficiency.

        Args:
            column_name: The name of the column to convert.

        Returns:
            self.df: The DataFrame with the specified column converted to 'category'.
        """
        self.df[column_name] = self.df[column_name].astype('category')
        return self.df

    def convert_to_datetime(self, column_name):
        """
        Convert a column with date strings to datetime objects.

        Args:
            column_name: The name of the column to convert. Dates should be in the format 'Mon-YYYY'.

        Returns:
            self.df: The DataFrame with the specified column converted to datetime. 
        """
        self.df[column_name] = pd.to_datetime(self.df[column_name], format='%b-%Y')
        return self.df
    

    
