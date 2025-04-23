"create and activate a virtual on your mac terminal"
"python3 -m venv venv"
"source venv/bin/activate"



import  numpy as np
import  pandas as pd
import  seaborn as sns
import  matplotlib.pyplot as plt
from    sklearn.model_selection import train_test_split
from    sklearn.metrics import accuracy_score
from    sklearn.metrics import classification_report
import  string
import  re

df_fake = pd.read_csv("Fake.csv", on_bad_lines='skip')
df_true = pd.read_csv("True.csv", on_bad_lines='skip')

df_fake.head()

df_true.head(5)

df_fake["class"] = 0
df_true["class"] = 1

df_fake.shape, df_true.shape

df_fake_manual_testing = df_fake.tail(10)
for i in range(23480,23470,-1):
    df_fake.drop([i], axis = 0, inplace = True)


df_true_manual_testing = df_true.tail(10)
for i in range(21416,21406,-1):
    df_true.drop([i], axis = 0, inplace = True)

df_fake.shape, df_true.shape

df_fake_manual_testing = pd.read_csv('Fake.csv')
df_true_manual_testing = pd.read_csv('True.csv')

# Assign class labels (0 for fake, 1 for real)
df_fake_manual_testing["class"] = 0
df_true_manual_testing["class"] = 1



df_fake.shape, df_true.shape

df_fake_manual_testing = df_fake.tail(10)


df_fake = df_fake.iloc[:-10]  # Keep everything except the last 10 rows


df_true_manual_testing = df_true.tail(10)

df_true = df_true.iloc[:-10]  # Keep everything except the last 10 rows

df_fake.shape, df_true.shape

df_fake_manual_testing["class"] = 0
df_true_manual_testing["class"] = 1

df_fake_manual_testing.head(10)

df_true_manual_testing.head(10)

df_manual_testing = pd.concat([df_fake_manual_testing,df_true_manual_testing], axis = 0)
df_manual_testing.to_csv("manual_testing.csv")

df_merge = pd.concat([df_fake, df_true], axis =0 )
df_merge.head(10)

df_merge.columns

df = df_merge.drop(["title", "subject","date"], axis = 1)

df.isnull().sum()

df = df.sample(frac = 1)

df.head()

df.reset_index(inplace = True)
df.drop(["index"], axis = 1, inplace = True)

df.columns

df.head()

def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)  # Use r before the string
    text = re.sub(r'\\W', ' ', text)  # Double check this pattern; it may need r'\W'
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Use r for raw string
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(rf'[{re.escape(string.punctuation)}]', '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)  # Use raw string here
    return text


df["text"] = df["text"].fillna("")  # Replace NaN with empty string
df["text"] = df["text"].apply(wordopt)

x = df["text"]
y = df["class"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load your dataset
x_train, x_test, y_train, y_test = train_test_split(df['text'], df['class'], test_size=0.25, random_state=42)

# Bigram TF-IDF
vectorizer_bigram = TfidfVectorizer(ngram_range=(1, 2))  # Unigrams and Bigrams
xv_train_bigram = vectorizer_bigram.fit_transform(x_train)
xv_test_bigram = vectorizer_bigram.transform(x_test)

# Logistic Regression on Bigram TF-IDF
model_bigram = LogisticRegression(max_iter=1000)
model_bigram.fit(xv_train_bigram, y_train)

# Predict and evaluate the model
pred_bigram = model_bigram.predict(xv_test_bigram)
print("Performance with Bigrams:")
print(classification_report(y_test, pred_bigram))

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import classification_report

# Logistic Regression with Cross-Validation
cv_scores_lr = cross_val_score(LogisticRegression(max_iter=1000), xv_train_bigram, y_train, cv=5, scoring='accuracy')
print("Logistic Regression Cross-Validation Scores:", cv_scores_lr)
print("Mean CV Accuracy (Logistic Regression):", cv_scores_lr.mean())

# Hyperparameter Tuning for Logistic Regression
param_grid_lr = {'C': [0.01, 0.1, 1, 10], 'solver': ['liblinear', 'lbfgs']}
grid_search_lr = GridSearchCV(LogisticRegression(max_iter=1000), param_grid_lr, cv=5, scoring='accuracy')
grid_search_lr.fit(xv_train_bigram, y_train)
print("Best Parameters for Logistic Regression:", grid_search_lr.best_params_)

# Final Logistic Regression Model
best_lr = grid_search_lr.best_estimator_
pred_lr = best_lr.predict(xv_test_bigram)
print("Logistic Regression Report:")
print(classification_report(y_test, pred_lr))

best_lr.score(xv_test_bigram, y_test)

from sklearn.tree import DecisionTreeClassifier

# Decision Tree with Cross-Validation
cv_scores_dt = cross_val_score(DecisionTreeClassifier(), xv_train_bigram, y_train, cv=5, scoring='accuracy')
print("Decision Tree Cross-Validation Scores:", cv_scores_dt)
print("Mean CV Accuracy (Decision Tree):", cv_scores_dt.mean())

# Hyperparameter Tuning for Decision Tree
param_grid_dt = {'max_depth': [5, 10, 20, None], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 2, 4]}
grid_search_dt = GridSearchCV(DecisionTreeClassifier(), param_grid_dt, cv=5, scoring='accuracy')
grid_search_dt.fit(xv_train_bigram, y_train)
print("Best Parameters for Decision Tree:", grid_search_dt.best_params_)

# Final Decision Tree Model
best_dt = grid_search_dt.best_estimator_
pred_dt = best_dt.predict(xv_test_bigram)
print("Decision Tree Report:")
print(classification_report(y_test, pred_dt))

best_dt.score(xv_test_bigram, y_test)

from sklearn.ensemble import GradientBoostingClassifier

# Gradient Boosting with Cross-Validation
cv_scores_gbc = cross_val_score(GradientBoostingClassifier(random_state=0), xv_train_bigram, y_train, cv=5, scoring='accuracy')
print("Gradient Boosting Cross-Validation Scores:", cv_scores_gbc)
print("Mean CV Accuracy (Gradient Boosting):", cv_scores_gbc.mean())

# Hyperparameter Tuning for Gradient Boosting
param_grid_gbc = {'n_estimators': [100, 200, 300], 'learning_rate': [0.01, 0.1, 0.2], 'max_depth': [3, 5, 7]}
grid_search_gbc = GridSearchCV(GradientBoostingClassifier(random_state=0), param_grid_gbc, cv=5, scoring='accuracy')
grid_search_gbc.fit(xv_train_bigram, y_train)
print("Best Parameters for Gradient Boosting:", grid_search_gbc.best_params_)

# Final Gradient Boosting Model
best_gbc = grid_search_gbc.best_estimator_
pred_gbc = best_gbc.predict(xv_test_bigram)
print("Gradient Boosting Report:")
print(classification_report(y_test, pred_gbc))

best_gbc.score(xv_test_bigram, y_test)

from sklearn.ensemble import RandomForestClassifier

# Random Forest with Cross-Validation
cv_scores_rfc = cross_val_score(RandomForestClassifier(random_state=0), xv_train_bigram, y_train, cv=5, scoring='accuracy')
print("Random Forest Cross-Validation Scores:", cv_scores_rfc)
print("Mean CV Accuracy (Random Forest):", cv_scores_rfc.mean())

# Hyperparameter Tuning for Random Forest
param_grid_rfc = {'n_estimators': [100, 200, 300], 'max_depth': [10, 20, None], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 2, 4]}
grid_search_rfc = GridSearchCV(RandomForestClassifier(random_state=0), param_grid_rfc, cv=5, scoring='accuracy')
grid_search_rfc.fit(xv_train_bigram, y_train)
print("Best Parameters for Random Forest:", grid_search_rfc.best_params_)

# Final Random Forest Model
best_rfc = grid_search_rfc.best_estimator_
pred_rfc = best_rfc.predict(xv_test_bigram)
print("Random Forest Report:")
print(classification_report(y_test, pred_rfc))

best_rfc.score(xv_test_bigram, y_test)

def output_lable(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"

def manual_testing(news):
    testing_news = {"text": [news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt)
    new_xv_test = vectorizer_bigram.transform(new_def_test["text"])  # Use same vectorizer

    pred_LR = best_lr.predict(new_xv_test)
    pred_DT = best_dt.predict(new_xv_test)
    pred_GBC = best_gbc.predict(new_xv_test)
    pred_RFC = best_rfc.predict(new_xv_test)

    print("\n\nLR Prediction: {} \nDT Prediction: {} \nGBC Prediction: {} \nRFC Prediction: {}".format(
        output_lable(pred_LR[0]),
        output_lable(pred_DT[0]),
        output_lable(pred_GBC[0]),
        output_lable(pred_RFC[0])
    ))

news = str(input())
manual_testing(news)

import pickle

# Save vectorizer and models
# Save the tuned models
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer_bigram, f)

with open("logistic_model.pkl", "wb") as f:
    pickle.dump(best_lr, f)

with open("decision_tree.pkl", "wb") as f:
    pickle.dump(best_dt, f)

with open("gradient_boost.pkl", "wb") as f:
    pickle.dump(best_gbc, f)

with open("random_forest.pkl", "wb") as f:
    pickle.dump(best_rfc, f)