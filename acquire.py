import pandas as pd
import os
from env import user_name, password, host

pd.set_option('display.max_columns',None) #pd.set_option('display.max_rows',None)

import warnings
warnings.filterwarnings("ignore")

# *************************************  connection url **********************************************

# Create helper function to get the necessary connection url.
def get_connection(db_name):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user_name}:{password}@{host}/{db_name}'

#Create query to get necessary data
def telco_data():
    '''
    This function reads in the telcoco data from the Codeup db
    and returns a pandas DataFrame with all columns and it was joined with other tables.
    '''
    sql_query = '''
    Select * from customers
    join contract_types on contract_types.contract_type_id = customers.contract_type_id
    join payment_types on payment_types.payment_type_id = customers.payment_type_id
    join internet_service_types on internet_service_types.internet_service_type_id = customers.internet_service_type_id
    '''
    return pd.read_sql(sql_query,get_connection('telco_churn'))

#Convert the function above into a csv file
def get_telco_data():
    '''
    This function reads in telco data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('telco_churn.csv'):
        df = pd.read_csv('telco_churn.csv', index_col=0)
    else:
        df = telco_data()
        df.to_csv('telco_churn.csv')
    return df