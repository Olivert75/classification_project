import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# plot distributions
def distribution (df):
    cols =df.columns.to_list()
    for col in cols:
        if df[col].dtype != 'object':
            plt.hist(df[col])
            plt.title(f'Distribution of {col}')
            plt.xlabel('values')
            plt.ylabel('Counts of customers')
            plt.show()


# plot distributions
def distribution_obj (df):
    cols =df.columns.to_list()
    for col in cols:
        if df[col].dtype == 'object':
            plt.hist(df[col])
            plt.title(f'Distribution of {col}')
            plt.xlabel('values')
            plt.ylabel('Counts of customers')
            plt.show()

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
        ax[i].axhline(churn_rate, ls='--', color='red')


def plot_tenure (df, tenure):
    '''
    Take in a df and tenure and plot tenure and churn
    '''
    plt.figure(figsize=(15,10))
    # Distribution of Tenure
    sns.histplot(df,
                 x=df[tenure],
                 hue='churn',
                 multiple='stack',
                 binwidth=1          
                 )

    plt.title("Distribution of Tenure")
    plt.xlabel('Tenure (in months)')
    plt.xlim(1, df[tenure].median())

def get_churn_heatmap(df):
    plt.figure(figsize=(8,12))
    churn_heatmap = sns.heatmap(df.corr()[['churn']].sort_values(by='churn', ascending=False), vmin=-.5, vmax=.5, annot=True)
    churn_heatmap.set_title('Feautures Correlating with Churn')
    
    return churn_heatmap


