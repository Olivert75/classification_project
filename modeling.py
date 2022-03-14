from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pandas as pd

def get_metrics_binary(X_train, y_train, y_pred,clf):
    '''
    This function takes in a confusion matrix (cnf) for a binary classifier and prints out metrics based on
    values in variables named X_train, y_train, and y_pred.
    return: a classification report as a transposed DataFrame
    '''
    accuracy = clf.score(X_train, y_train)
    class_report = pd.DataFrame(classification_report(y_train, y_pred, output_dict=True)).T
    conf = confusion_matrix(y_train, y_pred)
    tpr = conf[1][1] / conf[1].sum()
    fpr = conf[0][1] / conf[0].sum()
    tnr = conf[0][0] / conf[0].sum()
    fnr = conf[1][0] / conf[1].sum()
    print(f'''
    The accuracy for our model is {accuracy:.3%}
    The True Positive Rate is {tpr:.3%}, The False Positive Rate is {fpr:.3%},
    The True Negative Rate is {tnr:.3%}, and the False Negative Rate is {fnr:.3%}
    ''')
    return class_report