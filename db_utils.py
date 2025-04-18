import yaml
from sqlalchemy import create_engine, text
import pandas as pd

def load_credentials(credentials_file):
    """
    Load database credentials from a YAML file. 

    Args:
        credentials_file: Path to the YAML file containing database credentials.

    Returns:
        credentials_dict: A dictionary containing the database credentials.
    """
    with open(credentials_file, 'r') as db_creds:
        credentials_dict = yaml.safe_load(db_creds)

    return credentials_dict

class RDSDatabaseConnector:
    """
    A class to manage connections and operations with an RDS database.
    """

    def __init__(self, credentials_file):
        """
        Initialise the RDSDatabaseConnector with database credentials.

        Args:
            credentials_file: Path to the YAML file containing database credentials. 
        """
        self.credentials_dict = load_credentials(credentials_file)

    def init_db_engine(self):
        """
        Initalise a SQLAlchemy engine for connecting to the database.

        Returns:
            engine: A SQLAlchemy engine instance for database connections
        """
        creds = self.credentials_dict
        engine = create_engine(f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}")

        return engine

    def extract_table_data(self, table):
        """
        Extract data from a specified table in the RDS database.

        Args:
            table: The name of the table to extract data from. 

        Returns:
            table_df: A DataFrame containing the table data.
        """
        engine = self.init_db_engine()
        query = f"SELECT * FROM {table}"

        table_df = pd.read_sql_query(sql=text(query), conn=engine.connect())

        return table_df

    def save_to_csv(self, df):
        """
        Save a DataFrame to a CSV file. 

        Args:
            df: The DataFrame to be saved to a CSV file. 
        """
        df.to_csv('loan_payments.csv', index=False)

    def read_from_csv(self, file):
        """
        Read a CSV file into a DataFrame.

        Args:  
            file: The path to the CSV file to be read.

        Returns:
            df: A DataFrame containing the data from the CSV file. 
        """
        with open(file, 'r') as file:
            df = pd.read_csv(file)

            return df
    
def main():
    db_connector = RDSDatabaseConnector('credentials.yaml')
    payments_df = db_connector.read_from_csv('loan_payments.csv')
    print(payments_df.info())

if __name__ == '__main__':
    main()


