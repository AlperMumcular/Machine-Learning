# Alper Mumcular
# CS464 - HW1

import pandas as pd
import numpy as np

np.seterr(divide = 'ignore')

x_train = pd.read_csv("x_train.csv")
x_test = pd.read_csv("x_test.csv")
y_train = pd.read_csv("y_train.csv")
y_test = pd.read_csv("y_test.csv")


# Question 3.1 Question 1
y_train_size = y_train.size
count = 0
for i in y_train["Prediction"]:
    if i == 1:
        count = count + 1

percentage = count * 1.0 / y_train_size
print("Answer of Question 3.1-1: " + str(percentage))

# Question 3.2 (x == 0) - 3.3 (x == 1) - 3.4 (x == 2)
for x in range(0,3):
    train = pd.concat([x_train.iloc[:, 0:3000], y_train["Prediction"]], axis=1)

    if x == 2:
        train[train != 0] = 1
        x_train[x_train != 0] = 1
        x_test[x_test != 0] = 1

    a = 0
    if x == 1:
        a = 5 #1, 2, 4, 10, 50, 100 test values

    if x != 2:
        spam_estimator = (train[train["Prediction"] == 1].sum().drop(['Prediction']) + a) * 1.0 / (train[train["Prediction"] == 1].sum().drop(['Prediction']).sum() + a * len(x_train.columns))
        normal_estimator = (train[train["Prediction"] == 0].sum().drop(['Prediction']) + a) * 1.0 / (train[train["Prediction"] == 0].sum().drop(['Prediction']).sum() + a * len(x_train.columns))
    else:
        spam_estimator = x_train[y_train["Prediction"] == 1].sum() / x_train[y_train["Prediction"] == 1].shape[0]
        normal_estimator = x_train[y_train["Prediction"] == 0].sum() / x_train[y_train["Prediction"] == 0].shape[0]

    pi_estimator_normal = y_train[y_train["Prediction"] == 0].size * 1.0 / y_train_size

    log_n = np.log(normal_estimator)
    log_n[ log_n == float('-inf') ] = - (10 ** 12)

    log_s = np.log(spam_estimator)
    log_s[ log_s == float('-inf') ] = - (10 ** 12)

    non_spam = []
    spam = []
    for i in range(0, x_test.shape[0]):
        if x != 2:
            non_spam.append( np.log(1-percentage) + np.sum( log_n * x_test.iloc[i] ) )
            spam.append( np.log(percentage) + np.sum( log_s * x_test.iloc[i] ) )
        else:
            tmp1 = np.sum(np.log( normal_estimator * x_test.iloc[i] + (1-x_test.iloc[i]) * (1-normal_estimator) ))
            if tmp1 == float('-inf'):
                tmp1 = - (10 ** 12)

            tmp2 = np.sum(np.log( spam_estimator * x_test.iloc[i] + (1-x_test.iloc[i]) * (1-spam_estimator) ))
            if tmp2 == float('-inf'):
                tmp2 = - (10 ** 12)

            non_spam.append(np.log(1-percentage) + tmp1)
            spam.append(np.log(percentage) + tmp2)

    y = np.maximum(non_spam,spam)
    guesses = []
    for i in range(0, x_test.shape[0]):
        if y[i] == non_spam[i]:
            guesses.append(0)
        else:
            guesses.append(1)

    matrix = pd.crosstab(y_test["Prediction"], guesses, colnames=['    Predicted'], rownames=['Actual'])

    tp = matrix.iloc[1][1]
    fp = matrix.iloc[0][1]
    fn = matrix.iloc[1][0]
    tn = matrix.iloc[0][0]

    accuracy = (tp + tn) * 1.0 / (tp+fp+fn+tn)
    precision = tp * 1.0 / (tp + fp)
    recall = tp * 1.0 / (tp + fn)
    specificity = tn * 1.0 / (fp + tn)
    f = 2 * precision * recall / (precision + recall)

    if x == 0:
        print("\n---------------Multinomial Naive Bayes Model-----------------")
    elif x == 1:
        print("\n---------------Multinomial Naive Bayes Model - Dirichlet Prior-----------------")
    else:
        print("\n---------------Bernoulli Naive Bayes Model-----------------")

    print("TP: " + str(tp) + "\tFP: " + str(fp))
    print("FN: " + str(fn) + "\tTN: " + str(tn))
    print("\nAccuracy: " + str(accuracy))
    print("Precision: " + str(precision))
    print("Recall: " + str(recall))
    print("Specificity: " + str(specificity))
    print("F-Measure: " + str(f))
    print("Wrong predictions: " + str(fn + fp) )

