import yaml

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
