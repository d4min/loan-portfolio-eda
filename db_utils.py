import yaml
from sqlalchemy import create_engine, text
import pandas as pd

def load_credentials(credentials_file):
    """
    Return dictionary of credentials for connection to database from yaml file. 
    """
    with open(credentials_file, 'r') as db_creds:
        db_dict = yaml.safe_load(db_creds)

    return db_dict

class RDSDatabaseConnector:
    """
    Class to handle database operations. 
    """

    def __init__(self, credentials_file):
        self.credentials_dict = load_credentials(credentials_file)

    def init_db_engine(self):
        """
        initalise a SQLAlchemy engine for connection to database
        """
        creds = self.credentials_dict
        engine = create_engine(f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}")

        return engine

    def extract_table_data(self, table):
        """
        return payments data from rds as a pandas dataframe
        """
        engine = self.init_db_engine()
        query = f"SELECT * FROM {table}"

        table_df = pd.read_sql_query(sql=text(query), conn=engine.connect())

        return table_df

    def save_to_csv(self, df):
        """
        save pandas df to a csv file for more efficient loading when performing eda
        """
        return df.to_csv('loan_payments.csv', index=False)
    

def main():

    db_connector = RDSDatabaseConnector('credentials.yaml')
    payments = db_connector.extract_table_data('loan_payments')

    print(payments.shape)

if __name__ == '__main__':
    main()

