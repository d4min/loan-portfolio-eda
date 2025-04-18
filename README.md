# Loan Portfolio EDA

## Project Overview

This project performs exploratory data analysis on loan portfolio data to enhance loan approval decisions and risk management at a financial institution. 

## Environment Setup 

The foundation of the loan portfolio analysis was established by:

- Initisaling Git repository with appropriate `.gitignore` configuration
- Creating project structure and documentation files
- Establishing secure credential management approach

```
loan-portfolio-eda/
├── .gitignore            # Excludes credentials and unnecessary files
├── README.md             # Project documentation
├── credentials.yaml      # Database connection credentials (gitignored)
├── db_utils.py           # Database connection utilities
├── transformations.py    # Data transformation utilities
└── loan_data_dict.md     # Data dictionary for loan dataset
```

## Database Connection 

Implemented utilities in `db_utils.py` to handle all database operations. Key components include:

```python
# Database engine intialisation
def init_db_engine(self):
    creds = self.credentials_dict
    engine = create_engine(f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}")
    return engine 
```

```python
# Data extraction from database
def extract_table_data(self, table):
    engine = self.init_db_engine()
    query = f"SELECT * FROM {table}"
    table_df = pd.read_sql_query(sql=text(query), conn=engine.connect())
    return table_df
```

### Usage Example:

```python
# Extract data and save to CSV
db_connector = RDSDatabaseConnector('credentials.yaml')
loan_data = db_connector.extract_table_data('loan_payments')
db_connector.save_to_csv(loan_data)

# Load data from CSV for analysis
loan_data = db_connector.read_from_csv('loan_payments.csv')
```

## Data Schema Documentation 

Created a copmrehensive data dictionary that includes definitions for all 36 columns in the loan dataset. Key categories include:

- **Loan identifiers:** `id`, `member_id`
- **Loan amounts:** `loan_amount`, `funded_amount`, `funded_amount_inv`
- **Loan terms:** `term`, `int_rate`, `instalment`, `grade`, `sub_grade`
- **Borrower information:** `employment_length`, `home_ownership`, `annual_inc`
- **Payment status:** `loan_status`, `payment_plan`, `total_payment`
- **Credit indicators:** `dti`, `deling_2yr`, `open_accounts`, `total_accounts`

## Data Transformation 

Implemented transformation utilities in `transformations.py` to prepare data for analysis:

```python
# Convert columns to category type for efficiency
def convert_to_category(self, column_name):
    return self.df[column_name].astype('category')

# Convert string dates to datetime objects
def convert_to_datetime(self, column_name):
    self.df[column_name] = pd.to_datetime(self.df[column_name], format='mixed')
    self.df[column_name] = self.df[column_name].astype('datetime64[ns]')
    return self.df[column_name].dt.strftime()
```

### Usage Example:
```python
# Transform categorical and date columns
transformer = DataTransformer(loan_data)

# Convert categorical columns
loan_data['grade'] = transformer.convert_to_category('grade')
loan_data['home_ownership'] = transformer.convert_to_category('home_ownership')

# Convert date columns
loan_data['issue_date'] = transformer.convert_to_datetime('issue_date')
loan_data['last_payment_date'] = transformer.convert_to_datetime('last_payment_date')
```

This approach provides:
- Proper typing of categorical variables for memory efficiency and analysis
- Standardised datetime formatting for temporal analysis
- Foundation for further data cleaning and preprocessing
