import yaml
from sqlalchemy import create_engine, text
import pandas

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

    def __init__(self, db_dict):
        credentials_dict = db_dict

    def init_db_engine(self):
        """
        initalise a SQLAlchemy engine for connection to database
        """
        creds = self.credentials_dict
        engine = create_engine(f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}")

        return engine

    def extract_dbs_data(self, table):
        """
        return payments data from rds as a pandas dataframe
        """
        engine = self.init_db_engine()
        query = f"SELECT * FROM {table}"

        table_df = pandas.read_sql_query(sql=text(query), conn=engine)

        return table_df

        