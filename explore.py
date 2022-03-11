import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def churn_bar(df):
    #This function create a bar plot for churn rate
    #Plot churn rate base on number of customers
    
    df = df.churn_Yes.value_counts()
    plt.figure(figsize=(6,8))
    df.plot.bar(rot = 0)
    plt.title(f"Overall churn rate: {churn_rate:.2%}")
    plt.xlabel('Churn')
    plt.ylabel('Customers')

    plt.show()

#Create a heatmap show to the positve and negative related to churn
def get_churn_heatmap(df):
    plt.figure(figsize=(8,12))
    churn_heatmap = sns.heatmap(df.corr()[['churn_Yes']].sort_values(by='churn_Yes', ascending=False), vmin=-.5, vmax=.5, annot=True)
    churn_heatmap.set_title('Feautures Correlating with Churn')
    
    return churn_heatmap

def plot_tenure (df, tenure):
    '''
    Take in a df and tenure and plot tenure and churn
    '''
    plt.figure(figsize=(15,10))
    # Distribution of Tenure
   
    sns.histplot(train, x=train.tenure,
             hue='churn_Yes',
             multiple='stack',
             legend=False
             )

    plt.title("Distribution of Tenure")
    plt.xlabel('Tenure (in months)')
    plt.legend(title = 'churn', loc='upper right',labels=[0,1])
    plt.xlim(1, df[tenure].median())

def bar_plot (features, df):
    '''
    Take in a features (max 4) to plot  and churn_rate.
    '''
    churn_rate = df['churn'].mean()
    lc = len(features)
    _, ax = plt.subplots(nrows=1, ncols=lc, figsize=(16, 6), sharey=True)
    for i, feature in enumerate(features):
        sns.barplot(feature, 'churn', data=df, ax=ax[i], alpha=0.5, saturation=1)
        ax[i].set_xlabel('Churn')
        ax[i].set_ylabel(f'Churn Rate ={churn_rate:.2%}')
        ax[i].set_title(feature)
        ax[i].axhline(churn_rate, ls='--', color='black')

def report_tenure (train, tenure):
    '''
    This function create a report based on a specified tenure. Calculate total customers, churn customers, churn rate,
    % of phone service , % only internet,  % of type of contracts, and electronic cheks and paperless billing for
    the first months of the specified tenure, 
    train: dataframe
    tenure : number of the first month of tenure.
    Example:
    report_tenure (df, tenure)
    
    '''
    #Set the tensure at 12
    tenure = 12
    #cols has all the columns that I want to check
    cols = ['monthly_charges',
            'tenure', 'churn_Yes','one_year','two_year',
            'paperless_billing_Yes','credit_card',
            'mailed_check','electronic_check',
            'phone_service_Yes','multiple_lines_Yes',
            'fiber_optic','no_internet_service']
    
    #create a df with the fist months of tenure specified in the function
    df_t1 =train[cols][train['tenure'] <= tenure ]
    #total of customers that have the specified tenure
    ct1 = train.tenure_months[train['tenure_months'] < tenure].count()
    #total customer with specified tenure and churn =1
    can = df_t1.churn[ df_t1['churn'] == 1].count()
    #create a df and churn =1
    churndf = df_t1[(df_t1['churn']== 1)]
    #df of customers who have service phone
    cols_m = ['multiple_lines_Yes','monthly_charges','fiber_optic', 'electronic_check', 'paperless_billing_Yes','one_year','two_year']
    ml_df = churndf[cols_m].groupby('multiple_lines_Yes').sum()
    #calculate the total of phone service
    phone = ml_df.iloc[1:3, 5:].sum().sum()
    #calculate tonly internet service
    only_int = (ml_df.iloc[0, 1:3].sum()).astype(int)
    #create report of  churn = 1 and tenure < tenure
    cols_1v = ['monthly_charges','electronic_check','paperless_billing_Yes','month_to_month', 'one_year','two_year','churn']
    res_df= pd.DataFrame((churndf[cols_1v].sum()),columns=['churn_counts']) 
    #calculate nmontlhy charges
    m_char = res_df.iloc[0, 0]
    # let's see the churn rate
    churn_rate = train['churn'].mean()
    #customers with month_to month contracts and have canceled
    m2m =(res_df.loc['month_to_month'][0]).astype(int)
    #customers with mone year contract and churn
    oyc =(res_df.loc['one_year'][0]).astype(int)
    #customers with two year contract and churn
    tyc =(res_df.loc['two_year'][0]).astype(int)
    #customers with electronic_check and have canceled
    ec=(res_df.loc['electronic_check'][0]).astype(int)
    #customers with paperless billing and have canceled
    ppl=(res_df.loc['paperless_billing'][0]).astype(int)
    print(f'                      *** THE FIRST {tenure -1}  MONTH(S) OF TENURE *** ')
    print("")
    print(f'Total customers :     {ct1} ')
    print(f'Total cancellations : {can} ')
    print(f"Churn rate in the first {tenure -1 } month(s) of Tenure: {(can/ct1):.2%}")
    print("")
    print (f"****Overall churn rate: {churn_rate:.2%}******")
    print("")
    print("________________________________________________________________________________")
    print("")
    print(f'                    ** FIRST {tenure-1} MONTH(S) OF TENURE AND CHURN** ')
    print("")
    print(f'Customers with phone service:         {(phone/can):.2%} ')
    print(f'Customers with only internet service: {(only_int/can):.2%} ')
    print(f'Monlthy charges: $ {str(round(m_char, 3))} ')
    print("")

    print("")
    print(f'Month_to_month contracts: {(m2m/can):.2%} ')
    print(f'One year contract:        {(oyc/can):.2%} ')
    print(f'Two year contract:        {(tyc/can):.2%} ')
    print(f"Paperless_billing:        {(ppl/can):.2%}")
    print(f'Electronic_check payment type : {(ec/can):.2%} ')
