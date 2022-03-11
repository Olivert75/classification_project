import pandas as pd
import os
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns',None) 
pd.set_option('display.max_rows',None)

# ignore warnings
import warnings
warnings.filterwarnings("ignore")



#Prep telco_churn

def clean_data(df):
    '''
    This function will drop uneccessary columns or duplicates that is not useful for analysis.  
    change total_charges from object type to a float type. 
    create dummy variables for telco data that have the object type columns and then join with it original telco dataframe. 
    after joining, drop the columns that used to create dummy dataframe.
    and then return original telco dataframe.
    '''

    #Clean data

    #Drop duplicate rows, if present
    df = df.drop_duplicates()
    #Drop most of id columns since it is not useful in analysis
    #Keep the customer id column because need it to make prediction.csv 
    df = df.drop(columns = ['internet_service_type_id','payment_type_id','contract_type_id'])

    #Conver total_charges to float
    df['total_charges'] = df.total_charges.replace(' ', '0').astype(float)
    
    #Select every columns that is object type except the customer_id 
    col_list = list(df.select_dtypes('object').columns)[1:]

    #Create a dummy df and then 
    #create a loop to make it look through the list above
    #then drop some drops that is repeatedly
    for col in col_list:
        dummy_df = pd.get_dummies(df[col_list],dummy_na=False, drop_first=True)
        dummy_df = dummy_df.drop(columns = ['multiple_lines_No phone service',
                                    'online_backup_No internet service',
                                    'online_security_No internet service',
                                    'device_protection_No internet service',
                                    'tech_support_No internet service',
                                    'streaming_tv_No internet service',
                                    'streaming_movies_No internet service'])
        
    #Concatenate the dummy_df dataframe above with the original df
        df = pd.concat([df, dummy_df], axis=1)
    
    #Drop the columns that we already use to create dummy_df
        df.drop(columns=col, inplace=True)
    
    #Rename columns so more its meaningful 
        df = df.rename(columns={'contract_type_One year':'one_year',
                            'contract_type_Two year':'two_year',
                            'payment_type_Credit card (automatic)':'credit_card',
                            'payment_type_Electronic check':'electronic_check',
                            'payment_type_Mailed check':'mailed_check',
                            'internet_service_type_Fiber optic':'fiber_optic',
                            'internet_service_type_None':'no_internet_service'})
    
    return df

def split_data(df):
    '''
    This function takes in a dataframe and split the data into 3: train, validate and test
    Establish train+validate set 80% of original data and then repeat the process 
    Split train+validate  into train, validate separately 
    '''
    train_validate, test = train_test_split(df, 
                                            test_size=.2, 
                                            random_state=123, 
                                            stratify=df.churn_Yes)

    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.churn_Yes)
    return train, validate, test

def prepare (df):
    '''
    Cleaning and splitting the data using 2 function above
    '''
    clean_df =clean_data(df)
    train, validate, test = split_data(clean_df)

    return train, validate, test