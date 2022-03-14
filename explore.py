import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def churn_bar(df):
    #This function create a bar plot for churn rate
    #Plot churn rate base on number of customers
    churn_rate = df['churn_Yes'].mean()
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
    # Distribution of Tenure
    sns.displot(df, x=df.tenure,
             hue='churn_Yes',
             multiple='stack',
             legend=False
             )

    plt.title("Distribution of Tenure")
    plt.xlabel('Tenure (in months)')
    plt.legend(title = 'churn', loc='upper right',labels=[0,1])

def bar_plot (features, df):
    '''
    Take in a length of features to plot and churn_rate.
    '''
    churn_rate = df['churn_Yes'].mean()
    _, ax = plt.subplots(nrows=1, ncols=len(features), figsize=(16, 6), sharey=True)
    for i, feature in enumerate(features):
        sns.barplot(feature, 'churn_Yes', data=df, ax=ax[i], alpha=0.5, saturation=1)
        ax[i].set_xlabel('Churn')
        ax[i].set_ylabel(f'Churn Rate')
        ax[i].set_title(feature)
        ax[i].axhline(churn_rate, ls='--', color='black')


def report_tenure (train, tenure):
    '''
    This function create a report based on a specified tenure. Calculate total customers, churn customers, churn rate,
    % of fiber optic ,  % of type of contracts, and % electronic cheks and $ paperless billing for
    the first months of the specified tenure, 
    train: dataframe
    tenure : number of the first month of tenure.
    Example:
    report_tenure (df, tenure)
    
    '''
    #Set the specified tenure (tenure = 1)
    tenure = 2
    #cols has all the columns that I want to check
    cols = ['dsl','fiber_optic','multiple_lines','phone_service',
        'bank_transfer','paperless_billing','electronic_check','mailed_check','credit_card','no_internet_service',
        'month_to_month','contract_type_One year','contract_type_Two year',
        'tenure','churn_Yes','total_charges','monthly_charges']
    
    #create a df with the fist months of tenure specified in the function
    df_month1 = train[cols][train['tenure'] < tenure ]
    #total of customers that have the specified tenure
    total_customer = train.tenure[train['tenure'] < tenure].count()
    #total customer with specified tenure and churn = 1
    #create a df and churn = 1
    cust_churned = df_month1.churn_Yes[df_month1['churn_Yes']== 1].count()
    churned_df = df_month1[(df_month1['churn_Yes']==1)] 
    #create report of  churn = 1 and tenure < tenure
    cols_1v = ['monthly_charges','electronic_check','paperless_billing',
           'fiber_optic',
           'month_to_month','contract_type_One year','contract_type_Two year','churn_Yes']
    res_df= pd.DataFrame((churned_df[cols_1v].sum()),columns=['churn_counts'])
    # let's see the churn rate
    churn_rate = train['churn_Yes'].mean()
    #customers with electronic_check and have canceled
    ec=(res_df.loc['electronic_check'][0]).astype(int)
    #customers with paperless billing and have canceled
    ppl=(res_df.loc['paperless_billing'][0]).astype(int)
    #customers with fiber_optic and have canceled
    fo=(res_df.loc['fiber_optic'][0]).astype(int)

    #print statment to total number customer in the first month and customer that churned and churn rate
    #print statement to show % customers with paperless billing, fiber optic, electronic_check
    print("")
    print(f'** FIRST {tenure - 1} MONTHS OF TENURE AND CHURN** ')
    print("")
    print(f"Total customer in the first month: {total_customer}")
    print(f"Total customer cancellations in the first month: {cust_churned}")
    print("")
    print(f"Churn rate in the first month of Tenure: {(cust_churned/total_customer):.2%}")
    print(f"Paperless_billing:                       {(ppl/cust_churned):.2%}")
    print(f'Electronic_check payment type :          {(ec/cust_churned):.2%} ')
    print(f"Fiber_optic:                             {(fo/cust_churned):.2%}")
    print("")
    print(f'Overall Churn Rate: {churn_rate:.2%}')
