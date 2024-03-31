# -*- coding: utf-8 -*-
"""Loan_Approval_Predictor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XkDTo-mRXtprYDtndEaktrvVAhTuxjD7

**Automatic Loan Approval Predictor.**

>This dataset consists of more than 9,500 loans with information on the loan structure, the borrower, and whether the loan was pain back in full. This data was extracted from LendingClub.com, which is a company that connects borrowers with investors.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

df=pd.read_csv('loan_data.csv')
df

"""**Variable	Explanation**


1.  **credit_policy**	1 if the customer meets the credit underwriting criteria; 0 otherwise.
2. **purpose**	The purpose of the loan.
3. **int_rate**	The interest rate of the loan (more risky borrowers are assigned higher interest rates).
4.	**installment**	The monthly installments owed by the borrower if the loan is funded.
5.	**log_annual_inc**	The natural log of the self-reported annual income of the borrower.
6.	**dti**	The debt-to-income ratio of the borrower (amount of debt divided by annual income).
7.	**fico**	The FICO credit score of the borrower.
8.	**days_with_cr_line**	The number of days the borrower has had a credit line.
9.	**revol_bal**	The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle).
10.	**revol_util**	The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available).
11.	**inq_last_6mths**	The borrower's number of inquiries by creditors in the last 6 months.
12.	**delinq_2yrs**	The number of times the borrower had been 30+ days past due on a payment in the past 2 years.
13.	**pub_rec**	The borrower's number of derogatory public records.
14.	**not_fully_paid**	1 if the loan is not fully paid; 0 otherwise.
"""

pip install sweetviz

df.head(20) #top 20 rows of the data

df.tail(20) #last 10 rows of the data

"""**General Description **"""

df.info()

df.columns #columns of the data

df.describe(include=['object']) #description of the data type object

df.describe().T # statistical summary of the data

df['credit.policy']=df['credit.policy'].astype(int)
df['credit.policy']

df.groupby(['not.fully.paid','purpose']).nunique()

df['credit.policy'].value_counts()

df['int.rate'].describe()

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x='not.fully.paid', y='int.rate', data=df, color='skyblue')
plt.xlabel('Not Fully Paid',fontweight='bold')
plt.ylabel('Interest Rate',fontweight='bold')
plt.title('Boxplot of Interest Rate by Loan Status',fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
xtick = [0,1]
xlab = ["paid", "not_paid"]

plt.xticks(xtick, xlab)

plt.show()

sns.boxplot(x='credit.policy', y='int.rate', data=df, color='skyblue')
plt.xlabel('credit Policy',fontweight='bold')
plt.ylabel('Interest Rate',fontweight='bold')
plt.title('Boxplot of Interest Rate by credit Policy',fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
xtick = [0,1]
xlab = ["meet_criteria", "not_meet_criteria"]

plt.xticks(xtick, xlab)

plt.show()

df.groupby('credit.policy')['int.rate'].describe()

plt.bar(df['credit.policy'].unique(), df['credit.policy'].value_counts())
plt.title('credit policy',fontweight='bold')
plt.xlabel('credit policy',fontweight='bold')
plt.ylabel('frequency',fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.show()

df['credit.policy'].value_counts()

df['credit.policy'].unique()

df.nunique() #unique values of the data

df.shape #shape of the data

df.size #size of the data

print(df['purpose'].unique()) #unique category of the data
print(df['purpose'].value_counts()) #unique values of the data
print(df['purpose'].value_counts(normalize=True)) #unique values in %.

print(df['credit.policy'].unique()) #unique values in the credit policy column
print(df['credit.policy'].value_counts()) # frequency of the categories
print(df['credit.policy'].value_counts(normalize=True)) #% of the categories

df.isnull().sum() #null values in data

"""**Distribution of the variables**"""

import matplotlib.pyplot as plt
import seaborn as sns

# Plotting distributions of various features
fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(20, 20))

columns = df.columns
index = 0

for i in range(5):
    for j in range(3):
        if index < len(columns):
            sns.histplot(df[columns[index]], kde=True, ax=axes[i, j])
            axes[i, j].set_title(columns[index], fontweight='bold')
            axes[i, j].set_xlabel('Values', fontweight='bold')
            axes[i, j].set_ylabel('Frequency', fontweight='bold')
            for label in axes[i, j].get_xticklabels() + axes[i, j].get_yticklabels():
                label.set_fontweight('bold')
            index += 1
        else:
            # If there are more subplots than features, hide the empty subplot
            axes[i, j].axis('off')

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="viridis")  # Set cmap to "Blues" for bluish color

# Accessing the current axes
ax = plt.gca()

# Bold axis labels with black color
ax.set_xticklabels(ax.get_xticklabels(), fontweight='bold', color='black')
ax.set_yticklabels(ax.get_yticklabels(), fontweight='bold', color='black')

plt.show()

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

# Scatter plot with color-coded points based on the 'credit.policy' column
scatter = plt.scatter(df['int.rate'], df['installment'], c=df['col'])

# Calculate the coefficients for the line of best fit (linear regression)
#coefficients = np.polyfit(df['int.rate'], df['installment'], 1)
#line = np.poly1d(coefficients)

# Plot the line of best fit
#plt.plot(df['int.rate'], line(df['int.rate']), color='red', linestyle='--')

# Add colorbar
#plt.colorbar(scatter, label='Credit Policy')

# Set labels and title
plt.xlabel('Interest Rate', fontweight='bold')
plt.ylabel('Installments', fontweight='bold')
plt.title('Interest Rate vs Installments with Line of Best Fit', fontweight='bold')

# Set fontweight for ticks
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

# Show plot
plt.show()

import matplotlib.pyplot as plt

# Define unique colors for the legend
colors = ['blue', 'red']

# Create scatter plot with color-coded points based on the 'not.fully.paid' column
scatter = plt.scatter(df['int.rate'], df['installment'], c=df['not.fully.paid'], cmap='coolwarm')

# Create custom legend with unique colors
legend_labels = ['Fully Paid', 'Not Fully Paid']
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for color, label in zip(colors, legend_labels)]
plt.legend(handles=legend_handles, loc='best')

# Add colorbar
plt.colorbar(scatter, label='Not Fully Paid')

# Set labels and title
plt.xlabel('Interest Rate', fontweight='bold')
plt.ylabel('Installments', fontweight='bold')
plt.title('Interest Rate vs Installments', fontweight='bold')

# Set fontweight for ticks
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

# Show plot
plt.show()

plt.scatter(df['int.rate'], df['log.annual.inc'], c=df['col'])
plt.colorbar(scatter, label='Not Fully Paid')  # Add a colorbar with label

plt.xlabel('intrest rate',fontweight='bold')
plt.ylabel('annual income',fontweight='bold')
plt.title ('int rate vs Income',fontweight='bold')

plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

plt.show()

plt.scatter(df['int.rate'], df['days.with.cr.line'], c=df['col'])
plt.xlabel('intrest rate',fontweight='bold')
plt.ylabel('credit line days',fontweight='bold')
plt.title ('int rate vs credit line days',fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

plt.show()

plt.scatter( df['log.annual.inc'],df['installment'], c=df['col'])
#plt.plot(df['log.annual.inc'],df['installment'])
plt.xlabel('income',fontweight='bold')
plt.ylabel('installment',fontweight='bold')
plt.title ('income by installments',fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

plt.show()

plt.scatter(df['int.rate'], df['inq.last.6mths'], c=df['col'])
plt.xlabel('intrest rate',fontweight='bold')
plt.ylabel('inquired in last 6 months',fontweight='bold')
plt.title ('int rate vs inquired in last 6 months',fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

plt.show()

plt.scatter(df['int.rate'], df['delinq.2yrs'], c=df['col'])
plt.xlabel('intrest rate',fontweight='bold')
plt.ylabel('30+ d. pmt due in last 2yrs',fontweight='bold')
plt.title ('int rate vs 30+ days past due pmt last 2y',fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

plt.show()

import matplotlib.pyplot as plt

plt.scatter(df['int.rate'], df['delinq.2yrs'], c=df['col'])
plt.xlabel('Interest Rate', fontweight='bold')
plt.ylabel('30+ Days Past Due Payment in Last 2 Years', fontweight='bold')
plt.title('Interest Rate vs 30+ Days Past Due Payment Last 2 Years', fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

# Adding a legend based on the 'col' column
plt.legend(labels=df['col'].unique(), loc='upper right')

plt.show()

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# Define custom colors (mixture of blue and green)
#custom_colors = [(0, 0.5, 1), (0, 1, 0.5)]  # RGB tuples for blue and green mixture

plt.figure(figsize=(15, 6))
plt.bar(df['purpose'].unique(), df['purpose'].value_counts(), color='#0074D9')
plt.xlabel('Purpose', fontweight='bold')
plt.ylabel('Count', fontweight='bold')
plt.title('Purpose for Credit', fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

plt.show()

import seaborn as sns

# Create the logistic regression plot
sns.lmplot(x='int.rate', y='not.fully.paid', data=df, logistic=True, y_jitter=0.03)

# Set labels and title
plt.xlabel('Interest Rate')
plt.ylabel('prob of not fully paid')
plt.title(' Interest Rate by Not Fully Paid')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate colors using the viridis colormap
num_categories = len(df['purpose'].unique())
colors = plt.cm.viridis(np.linspace(0, 1, num_categories))

plt.figure(figsize=(15, 6))
plt.bar(df['purpose'].unique(), df['purpose'].value_counts(), color=colors)
plt.xlabel('Purpose', fontweight='bold')
plt.ylabel('Count', fontweight='bold')
plt.title('Purpose for Credit', fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Generate colors using the viridis colormap
num_categories = len(df['purpose'].unique())
colors = plt.cm.viridis(np.linspace(0, 1, num_categories))

plt.figure(figsize=(8, 10))  # Adjust figure size for vertical display
plt.barh(df['purpose'].unique(), df['purpose'].value_counts(), color=colors)  # Use barh for horizontal bars
plt.ylabel('Purpose', fontweight='bold')  # Change ylabel to 'Purpose'
plt.xlabel('Count', fontweight='bold')  # Change xlabel to 'Count'
plt.title('Purpose for Credit', fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
#xtick = ['educational','major_purchase']
#xlab = ["educational", "major_purcahse"]

#plt.xticks(xtick, xlab)

plt.show()

df['purpose'].value_counts(normalize=True)

for column in df.columns:
    # Skip non-numeric data
    if df[column].dtype == 'object':
        continue

    # Create a box plot for the column
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df, x=column)
    plt.title(f'Box Plot of {column}',fontweight='bold')
    plt.ylabel('Value',fontweight='bold')
    plt.xticks(fontweight='bold')
    plt.yticks(fontweight='bold')

    plt.show()

plt.figure(figsize=(15, 6))
df.boxplot(column=['log.annual.inc', 'dti'])
plt.title('Boxplot of ',fontweight='bold')
plt.xlabel('old and new balances',fontweight='bold')
plt.ylabel('amount',fontweight='bold')
plt.show()
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

plt.subplots_adjust(wspace=1.5)

import matplotlib.pyplot as plt
import seaborn as sns

figsize = (12, 1.2 * len(df['purpose'].unique()))
plt.figure(figsize=figsize)
ax = sns.boxplot(data=df, x='installment', y='purpose', palette='Dark2')

# Bold axis labels
ax.set_xlabel('Installment', fontweight='bold')
ax.set_ylabel('Purpose', fontweight='bold')

# Bold axis ticks
ax.set_xticklabels(ax.get_xticklabels(), fontweight='bold')
ax.set_yticklabels(ax.get_yticklabels(), fontweight='bold')

sns.despine(top=True, right=True, bottom=True, left=True)
plt.show()



df

# @title int.rate

from matplotlib import pyplot as plt
df['int.rate'].plot(kind='line', figsize=(8, 4), title='int.rate')
plt.gca().spines[['top', 'right']].set_visible(False)

# @title Interest rate vs FICO score

import matplotlib.pyplot as plt

# Scatter plot
plt.scatter(df['int.rate'], df['fico'], c=df['col'])

# Bold labels
plt.xlabel('Interest Rate', fontweight='bold')
plt.ylabel('FICO Score', fontweight='bold')
plt.title('Interest Rate vs FICO Score', fontweight='bold')

# Bold axis ticks
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

plt.show()

import matplotlib.pyplot as plt

# Scatter plot
plt.scatter(df['int.rate'], df['not.fully.paid'], c=df['not.fully.paid'])

# Bold labels
plt.xlabel('Interest Rate', fontweight='bold')
plt.ylabel('FICO Score', fontweight='bold')
plt.title('Interest Rate vs FICO Score', fontweight='bold')

# Bold axis ticks
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

plt.show()

plt.scatter(df['log.annual.inc'], df['fico'], c=df['fico'])
plt.xlabel('Annual Income',fontweight='bold')
plt.ylabel('FICO Score', fontweight='bold')
_ = plt.title('Income vs FICO Score',fontweight='bold')
# Bold axis ticks
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')

import matplotlib.pyplot as plt

# Calculate the value counts normalized
value_counts_normalized = df['not.fully.paid'].value_counts(normalize=True)

# Define labels for the pie chart
labels = ['Fully Paid', 'Not Fully Paid']

# Plotting the pie chart
plt.pie(value_counts_normalized, labels=labels)

# Adding a legend
plt.legend()

# Adding a title
plt.title('Proportion of Fully Paid vs. Not Fully Paid Loans')

# Displaying the plot
plt.show()

df['not.fully.paid'].value_counts(normalize=True)

a = df.drop(columns=['purpose', 'col'], axis=1)
a

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# List of columns to scale
columns_to_scale = ['int.rate', 'installment', 'log.annual.inc', 'dti', 'fico','days.with.cr.line','revol.bal','revol.util']

# Applying StandardScaler only to the specified columns
df_scaled = a.copy()
df_scaled[columns_to_scale] = scaler.fit_transform(a[columns_to_scale])

# Display the first few rows of the scaled dataframe
df_scaled.head()

"""**Train Test Split**"""

from sklearn.model_selection import train_test_split
X=a.drop('not.fully.paid', axis=1)
y1=df['not.fully.paid']
X_train, X_test, y_train, y_test = train_test_split( X, y1, test_size=0.2, random_state=4)
print ('Train set:', X_train.shape,  y_train.shape)
print ('Test set:', X_test.shape,  y_test.shape)
print(type(X_train)); print(type(y_train))

from sklearn.model_selection import train_test_split
Xs=df_scaled.drop('not.fully.paid', axis=1)
ys=df_scaled['not.fully.paid']
Xs_train, Xs_test, ys_train, ys_test = train_test_split( Xs, ys, test_size=0.2, random_state=4)
print ('Train set:', Xs_train.shape,  ys_train.shape)
print ('Test set:', Xs_test.shape,  ys_test.shape)
print(type(Xs_train)); print(type(ys_train))

"""**Logistic Regression**"""

from sklearn.linear_model import LogisticRegression

LR1 = LogisticRegression(penalty=None).fit(X_train,y_train)
print(LR1)
LR2 = LogisticRegression(penalty=None).fit(Xs_train,ys_train)
LR2

yhat1 = LR1.predict(X_test)
print(yhat1)
yhat2 = LR2.predict(Xs_test)
yhat2

yhat1_prob_temp = LR1.predict_proba(X_test)
yhat1_prob_temp
yhat2_prob_temp = LR2.predict_proba(Xs_test)
yhat2_prob_temp

yhat1_prob = LR1.predict_proba(X_test)[:,1]
yhat1_prob
yhat2_prob = LR2.predict_proba(Xs_test)[:,1]
yhat2_prob

from sklearn.metrics import accuracy_score
accuracy_score(y_test, yhat1)

import statsmodels.api as sm
logit_model=sm.Logit(y1,X)
result=logit_model.fit()
print(result.summary2())

X = sm.add_constant(X)

# Fit logistic regression model
model = sm.Logit(y1, X).fit()

# Print model summary
coefficients = model.params

# Calculate odds ratios
odds_ratios = np.exp(coefficients)

# Print odds ratios
for feature, odds_ratio in zip(X.columns, odds_ratios):
    print(f'{feature}: {odds_ratio}')

model = sm.Logit(y1, X).fit()

# Print model summary
summary = model.summary()
results_table = summary.tables[1]
coef_data = results_table.data[1:]

# Create a dictionary to store coefficient estimates, standard errors, and confidence intervals
coef_info = {}
for row in coef_data:
    coef_name = row[0]
    coef_value = float(row[1])
    std_error = float(row[2])
    ci_lower = float(row[4])
    ci_upper = float(row[5])

    # Calculate odds ratio
    odds_ratio = np.exp(coef_value)

    # Calculate confidence intervals for odds ratio
    ci_lower_odds_ratio = np.exp(ci_lower)
    ci_upper_odds_ratio = np.exp(ci_upper)

    coef_info[coef_name] = {
        'Coefficient': coef_value,
        'Standard Error': std_error,
        'Odds Ratio': odds_ratio,
        'CI Lower': ci_lower_odds_ratio,
        'CI Upper': ci_upper_odds_ratio
    }

# Print coefficient information
for coef_name, info in coef_info.items():
    print(f'{coef_name}:')
    print(f'  Coefficient: {info["Coefficient"]}')
    print(f'  Standard Error: {info["Standard Error"]}')
    print(f'  Odds Ratio: {info["Odds Ratio"]}')
    print(f'  95% CI Lower: {info["CI Lower"]}')
    print(f'  95% CI Upper: {info["CI Upper"]}')
    print()

from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report, confusion_matrix

classificatio_report

cm = confusion_matrix(y_test, yhat1)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()

cms = confusion_matrix(ys_test, yhat2)

disp = ConfusionMatrixDisplay(confusion_matrix=cms)
disp.plot()

print(type(yhat1_prob))

print(type(yhat2_prob))

prob_df = pd.DataFrame(yhat1_prob)

prob_df.describe()

tn, fp, fn, tp = cm.ravel()

print(tn, fp, fn, tp)

tn, fp, fn, tp = cms.ravel()

print(tn, fp, fn, tp)

sensitivity = tp / (tp + fn)

specificity = tn / (tn + fp)
print("Sensitivity: ", sensitivity)
print("Specificity: ", specificity)

sensitivity = tp / (tp + fn)

specificity = tn / (tn + fp)
print("Sensitivity: ", sensitivity)
print("Specificity: ", specificity)

import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score, roc_curve

# Calculate the ROC Curve and AUC
fpr, tpr, thresholds = roc_curve(y_test, yhat1_prob)
roc_auc = roc_auc_score(y_test, yhat1_prob)

# Plotting the ROC Curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2)
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')

plt.show()

roc_auc

fpr, tpr, thresholds = roc_curve(ys_test, yhat2_prob)
roc_auc = roc_auc_score(ys_test, yhat2_prob)

# Plotting the ROC Curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2)
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')

plt.show()

roc_auc

print(fpr); print(tpr); print(thresholds)

roc_auc



"""**K_Nearest_Neighbors**"""

from sklearn.neighbors import KNeighborsClassifier
k = 8
#Train Model and Predict
neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
neigh

yhat = neigh.predict(X_test)
yhat[0:5]

from sklearn import metrics
print("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))

Ks = 10
mean_acc = np.zeros((Ks-1))
std_acc = np.zeros((Ks-1))

print(mean_acc); print(std_acc)

for n in range(1,Ks):

    #Train Model and Predict
    neigh = KNeighborsClassifier(n_neighbors = n).fit(X_train,y_train)
    yhat=neigh.predict(X_test)
    mean_acc[n-1] = metrics.accuracy_score(y_test, yhat)


    std_acc[n-1]=np.std(yhat==y_test)/np.sqrt(yhat.shape[0])

mean_acc

plt.plot(range(1,Ks),mean_acc,'g')  #g specifies color - green
plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)
plt.fill_between(range(1,Ks),mean_acc - 3 * std_acc,mean_acc + 3 * std_acc, alpha=0.10,color="green")
plt.legend(('Accuracy ', '+/- 1xstd','+/- 3xstd'))
plt.ylabel('Accuracy ')
plt.xlabel('Number of Neighbors (K)')
plt.tight_layout()
plt.show()

print( "The best accuracy was with", mean_acc.max(), "with k=", mean_acc.argmax()+1)

"""**Decision Tree**"""

from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score, roc_curve

# Initializing and training the Decision Tree Classifier with Gini impurity
dt_gini = DecisionTreeClassifier(criterion='gini', random_state=42)
dt_gini.fit(X_train, y_train)

# Initializing and training the Decision Tree Classifier with Information Gain (Entropy)
dt_entropy = DecisionTreeClassifier(criterion='entropy', random_state=42)
dt_entropy.fit(X_train, y_train)

# Making predictions and evaluating the models
y_pred_gini = dt_gini.predict(X_test)
y_pred_entropy = dt_entropy.predict(X_test)

accuracy_gini = accuracy_score(y_test, y_pred_gini)
accuracy_entropy = accuracy_score(y_test, y_pred_entropy)

accuracy_gini, accuracy_entropy

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Assuming dt_gini and dt_entropy are the trained Decision Tree models

# Visualizing the Decision Tree using Gini impurity
plt.figure(figsize=(20,10))
plot_tree(dt_gini, filled=True, feature_names=X.columns, class_names=['No Disease', 'Disease'], rounded=True)
plt.title("Decision Tree using Gini Impurity")
plt.show()
plt.close()

# Visualizing the Decision Tree using Information Gain (Entropy)
plt.figure(figsize=(20,10))
plot_tree(dt_entropy, filled=True, feature_names=X.columns, class_names=['No Disease', 'Disease'], rounded=True)
plt.title("Decision Tree using Information Gain (Entropy)")
plt.show()
plt.close()

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score, roc_curve

# Assuming y_test, y_pred_gini, and y_pred_entropy are already defined from your model predictions

# Evaluation metrics for Gini model
confusion_gini = confusion_matrix(y_test, y_pred_gini)
precision_gini = precision_score(y_test, y_pred_gini)
recall_gini = recall_score(y_test, y_pred_gini)
f1_score_gini = f1_score(y_test, y_pred_gini)
roc_auc_gini = roc_auc_score(y_test, y_pred_gini)

# Evaluation metrics for Entropy model
confusion_entropy = confusion_matrix(y_test, y_pred_entropy)
precision_entropy = precision_score(y_test, y_pred_entropy)
recall_entropy = recall_score(y_test, y_pred_entropy)
f1_score_entropy = f1_score(y_test, y_pred_entropy)
roc_auc_entropy = roc_auc_score(y_test, y_pred_entropy)

# Printing the evaluation metrics
print("Gini Model Evaluation Metrics:")
print("Confusion Matrix:\n", confusion_gini)
print("Precision: {:.2f}".format(precision_gini))
print("Recall: {:.2f}".format(recall_gini))
print("F1 Score: {:.2f}".format(f1_score_gini))
print("ROC AUC: {:.2f}".format(roc_auc_gini))

print("\nEntropy Model Evaluation Metrics:")
print("Confusion Matrix:\n", confusion_entropy)
print("Precision: {:.2f}".format(precision_entropy))
print("Recall: {:.2f}".format(recall_entropy))
print("F1 Score: {:.2f}".format(f1_score_entropy))
print("ROC AUC: {:.2f}".format(roc_auc_entropy))

# ROC curve calculations
fpr_gini, tpr_gini, _ = roc_curve(y_test, y_pred_gini)
fpr_entropy, tpr_entropy, _ = roc_curve(y_test, y_pred_entropy)

# Plotting ROC curves
plt.figure(figsize=(10, 6))
plt.plot(fpr_gini, tpr_gini, label='Gini - AUC: {:.2f}'.format(roc_auc_gini))
plt.plot(fpr_entropy, tpr_entropy, label='Entropy - AUC: {:.2f}'.format(roc_auc_entropy))
plt.plot([0, 1], [0, 1], 'k--') # Dashed diagonal line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.show()

pip install -U imbalanced-learn scikit-learn

!pip uninstall imbalanced-learn

from imblearn.over_sampling import SMOTE

smote = SMOTE()
X_sm, y_sm = smote.fit_resample(X_train, y_train)

from sklearn.linear_model import LogisticRegression

LR1 = LogisticRegression(penalty=None).fit(X_sm,y_sm)
print(LR1)

yhat1 = LR1.predict(X_test)
yhat1

yhat1_prob_temp = LR1.predict_proba(X_test)
yhat1_prob_temp

from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report, confusion_matrix

cm = confusion_matrix(y_test, yhat1)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()

tn, fp, fn, tp = cm.ravel()

print(tn, fp, fn, tp)

sensitivity = tp / (tp + fn)

specificity = tn / (tn + fp)
print("Sensitivity: ", sensitivity)
print("Specificity: ", specificity)

import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score, roc_curve

# Calculate the ROC Curve and AUC
fpr, tpr, thresholds = roc_curve(y_test, yhat1_prob)
roc_auc = roc_auc_score(y_test, yhat1_prob)

# Plotting the ROC Curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2)
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')

plt.show()

roc_auc