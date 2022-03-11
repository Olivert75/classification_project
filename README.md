#### PROJECT DESCRIPTION

- Predict customer churn at Telco, a telecommunications company, using a machine learning classification model.
<br>

## Project Objectives

-Document code, process (data acquistion, preparation, exploratory data analysis, statistical testing, modeling(model evaluation), findings, and key takeaways in a Jupyter Notebook report.

-Create modules (acquire.py, prepare.py, explore.py) that make your process repeateable.

-Construct a model to predict customer churn using classification techniques.

-Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.

-Answer panel questions about your code, process, findings and key takeaways, and model.
<br>

#### GOALS 

- Find drivers for customer churn at Telco.

- Construct a ML classification model that accurately predicts customer churn.

- Document your process well enough to be presented or read like a report.
<br>

#### DATA DICTIONARY
---
| Attribute | Definition | Values|
| ----- | ----- | ----- |
senior_citizen|Indicates if the customer is 65 or older | 0(no), 1(yes)1 |
tenure|The length of a customers  with Telco  in months | numbers(in months) |
monthly_charges|The amount a customer pays each month for services with Telco | numbers(US Dollars) |
total_charges|The total amount a customer has paid for Telco™ services| numbers(US Dollars) |
gender_male |Indicates sex of a customer |  | 0(female), 1(male) |
partner_Yes|If a customer is married | 0(no), 1(yes) |
dependents_Yes|Indicates if a customer lives with dependents | 0(no), 1(yes) |
phone_service_Yes|If a customer has phone service | 0(no), 1(yes) |
multiple_lines_Yes|If a customer has multiple phone lines | 0(no), 1(yes) |
online_security_Yes|Indicates if a customer has online security add-on | 0(no), 1(yes) |
online_backup_Yes|Indicates if a customer has online backups add-on | 0(no), 1(yes) |
device_protection_Yes|Indicates if a customer has a protection plan for Telco devices  | 0(no), 1(yes) |
tech_support_Yes|Indicates whether a customer has technical support add-on | 0(no), 1(yes) |
streaming_tv_Yes|Indicates if a customer uses internet to stream tv | 0(no), 1(yes) |
streaming_movies_Yes|Indicates if a customer uses internet to stream movies | 0(no), 1(yes) |
paperless_billing_Yes|Indicates if a customer is enrolled in auto payment | 0(no), 1(yes) |
churn_Yes | Indicates whether a customer has left service | 0(Still using the service), 1(Canceled the service) |
one_year |Customers have a one year contract | 0(no), 1(yes) |
two_year |Customers have a two year contract | 0(no), 1(yes) |
credit_card|Customers use creit card as a type of payment | 0(no), 1(yes) |
electronic_check|Customers use electronic check as a type of payment | 0(no), 1(yes) |
mailed_check|Customers mailed a check as a type of payment | 0(no), 1(yes) |
fiber_optic|Indicates the type of internet service as fiber optic | 0(no), 1(yes) |
no_internet_service|Indicates if a customer has internet | 0(no), 1(yes) |

<br>

#### PROJECT PLANNIG

- Acquire data from the Codeup Database using my own function to automate this process. this function is saved in acquire.py file to import into the Final Report Notebook.
- Clean and prepare data for preparation step. Create a function to automate the process. The function is saved in a prepare.py module. Use the function in Final Report Notebook.
- Define two hypotheses, set an alpha, run the statistical tests needed,document findings and takeaways.
- Establish a baseline accuracy and document well.
- Train three different classification models.
- Evaluate models on train and validate datasets.
- Choose the model that performs the best.
- Evaluate the best model (only one) on the test dataset
- Create csv file with customer_id, probability of churn, and prediction of churn
<br>

#### AUDIENCE

Your target audience for your notebook walkthrough is your direct manager and their manager. This should guide your language and level of explanations in your walkthrough.
<br>

#### INSTRUCTIONS FOR RECREATING PROJECT

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

Read this README.md Clone the aquire.py, prepare.py, explore.py, and telco_churn_final.ipynb files into your working directory Add your own env file to your directory. (user, password, host) Run the telco_churn_final.ipynb notebook
<br>

#### DELIVER:
- A Jupyter Notebook Report showing process and analysis with goal of finding drivers for customer churn.
- A README.md file containing project description with goals, a data dictionary, project planning (lay out your process through the data science pipeline), instructions or an explanation of how someone else can recreate your project and findings (What would someone need to be able to recreate your project on their own?), and key findings and takeaways from your project.
- A CSV file with customer_id, probability of churn, and prediction of churn. 
- Individual modules, .py files, that hold your functions to acquire and prepare your data.
- A notebook walkthrough presentation with a high-level overview of your project (5 minutes m