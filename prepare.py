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
    
    #Conver total_charges to float
    df['total_charges'] = df.total_charges.replace(' ', '0').astype(float)
    #total_charges had 11 null values and filled nulls with the mean of all total charges.
    df.total_charges = df.total_charges.fillna(value=df.total_charges.mean()).astype(float)
    
    #Replacing no internet service and no phone service with a no so it alittle easier to encoding
    df.replace('No internet service', 'No', inplace=True)
    df.replace('No phone service', 'No', inplace = True)
    
    #Convert yes and no to 1 and 0 respectively 
    #Changing the type of some columns that are object to int but not all
    #Do the same for other columns except contract type, payment type and internet service
    #These columns has 3 values in them. 
    #For example, it harder to understand one year = 0 and two year = 0, they are the same as month to month 
    df["is_male"] = df.gender == "Male"
    df['is_male'] = df['is_male'].astype(int)

    df["partner"] = df.partner == "Yes"
    df['partner'] = (df['partner']).astype(int)

    df["dependents"] = df.dependents == "Yes"
    df['dependents'] = (df['dependents']).astype(int)

    df["phone_service"] = df.phone_service == "Yes"
    df['phone_service'] = (df['phone_service']).astype(int)

    df["streaming_tv"] = df.streaming_tv == "Yes"
    df['streaming_tv'] = (df['streaming_tv']).astype(int)

    df["streaming_movies"] = df.streaming_movies == "Yes"
    df['streaming_movies'] = (df['streaming_movies']).astype(int)

    df["paperless_billing"] = df.paperless_billing == "Yes"
    df['paperless_billing'] = (df['paperless_billing']).astype(int)

    df["multiple_lines"] = df.multiple_lines == "Yes"
    df['multiple_lines'] = (df['multiple_lines']).astype(int)

    df["online_security"] = df.online_security == "Yes"
    df['online_security'] = (df['online_security']).astype(int)

    df["online_backup"] = df.online_backup == "Yes"
    df['online_backup'] = (df['online_backup']).astype(int)

    df["device_protection"] = df.device_protection == "Yes"
    df['device_protection'] = (df['device_protection']).astype(int)

    df["tech_support"] = df.tech_support == "Yes"
    df['tech_support'] = (df['tech_support']).astype(int)

    #Drop most of id columns since it is not useful in analysis
    #Keep the customer id column because need it to make prediction.csv 
    df = df.drop(columns = ['gender','internet_service_type_id','payment_type_id','contract_type_id',
                            'internet_service_type_id.1','payment_type_id.1','contract_type_id.1'])

    #Select every columns that is object type except the customer_id 
    col_list = list(df.select_dtypes('object').columns)[1:]

    #Create a dummy df and then 
    #create a loop to make it look through the list above
    #then drop some drops that is repeatedly
    dummy_df = pd.get_dummies(df[col_list],dummy_na=False, drop_first=False)
    dummy_df = dummy_df.drop(columns = ['churn_No'])
        
    #Concatenate the dummy_df dataframe above with the original df
    df = pd.concat([df, dummy_df], axis=1)
    
    #Drop the columns that we already use to create dummy_df
    df.drop(columns=col_list, inplace=True)
    
    #Rename columns so more its meaningful 
    df = df.rename(columns={'contract_type_Month-to-month':'month_to_month',
                            'payment_type_Credit card (automatic)':'credit_card',
                            'payment_type_Bank transfer (automatic)':'bank_transfer',
                            'payment_type_Electronic check':'electronic_check',
                            'payment_type_Mailed check':'mailed_check',
                            'internet_service_type_DSL':'dsl',
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