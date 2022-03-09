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
    This function will drop payment_type_id', 'internet_service_type_id','contract_type_id', 
    convert all the columns that have yes/no to 0/1, 
    create dummy vars from 'gender', 'contract_type', 'internet_service_type', 'payment_type',
    change total_charges from object typeto a float type. 
    '''

    #clean data

    #drop duplicate rows, if present
    df = df.drop_duplicates()
    #drop most of id columns since it is not useful in analysis
    df = df.drop(columns = ['customer_id','internet_service_type_id','payment_type_id','contract_type_id'])

    #conver total_charges to float
    df['total_charges'] = df.total_charges.replace(' ', '0').astype(float)
    
    #create a dummy df
    col_list = df.select_dtypes('object').columns.to_list()

    #create a dummy df
    for col in col_list:
        dummy_df = pd.get_dummies(df[col],prefix=df[col].name,drop_first=True,dummy_na=False)
    # Concatenate the dummy_df dataframe above with the original df
        df = pd.concat([df, dummy_df], axis=1)
    # drop the columns that we already use to create dummy_df
        df.drop(columns=col, inplace=True)
    
    #drop duplicates columns again
    #df.drop(columns = ['payment_type_id', 'internet_service_type_id','contract_type_id'], inplace=True)
    
    # rename columns
    df = df.rename(columns={'gender_Male':'gender',
                            'dependents_Yes':'dependents',
                            'partner_Yes':'partner',
                            'phone_service_Yes':'one_line',
                            'multiple_lines_No phone service': 'no_phone_service',
                            'multiple_lines_Yes':'multiple_lines', 
                            'online_security_No internet service': 'online_security_with_no_internet service',
                            'online_security_Yes':'online_security',
                            'online_backup_No internet service':'online_backup_with_no_internet service',
                            'online_backup_Yes':'online_backup',
                            'device_protection_No internet service':'device_protection_with_no_internet service',
                            'device_protection_Yes':'device_protection',
                            'tech_support_No internet service':'tech_support_with_no_internet service',
                            'tech_support_Yes':'tech_support',
                            'streaming_tv_No internet service':'streaming_tv_with_no_internet service',
                            'streaming_tv_Yes':'streaming_tv',
                            'streaming_movies_No internet service':'streaming_movies_with_no_internet service',
                            'streaming_movies_Yes':'streaming_movies',
                            'paperless_billing_Yes':'paperless_billing',
                            'churn_Yes':'churn',
                            'contract_type_One year':'one_year',
                            'contract_type_Two year':'two_year',
                            'payment_type_Credit card (automatic)':'Auto_pay',
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
                                            stratify=df.churn)

    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.churn)
    return train, validate, test

def prepare (df):
    '''
    Cleaning and splitting the data using 2 function above
    '''
    clean_df =clean_data(df)
    train, validate, test = split_data(clean_df)

    return train, validate, test