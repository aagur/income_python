# Income

### Classification of the Adult dataset

The dataset was downloaded from https://archive.ics.uci.edu/ml/datasets/Adult.

The purpose of this project is to find the best model which will predict if some person will earn more or less than 50 thousand dollars per year.

The project includes preparing dataset into training (ex. dealing with missing values, transforming categorical variables into equivalent numerical values, standarization).
It has been compared 6 different classification models:
  * K-Nearest Neighbours
  * Decision Tree Classifier
  * Random Forest Classifier
  * Logistic Regression
  * Support Vector Machine (Linear and Radial)
  * XGBoost Classifier
  
and have been used GridSearchCV to find the best hyperparameters.
It has been analyzed different metrics (ex. AUC, accuracy, recall, precision)  to choose model with the best prediction power.

All plots included in the project was generated using libraries: plotly, matplotlib and seaborn.

### Software
The analysis and implementation has been done using Python 3.7.4 version.
