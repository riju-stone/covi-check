import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle


def data_split(data, ratio):
    np.random.seed(35)
    shuffled_data = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled_data[:test_set_size]
    train_indices = shuffled_data[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


if __name__ == "__main__":
    # reading dataset
    df = pd.read_csv('covid-dataset.csv')
    # training set test set splitting
    train_data, test_data = data_split(df, 0.3)

    output_var = ['COVID-19']
    # feature columns and prediction column splitting
    x_train = train_data.iloc[:, :20].to_numpy()
    y_train = train_data[output_var].to_numpy().ravel()
    x_test = test_data.iloc[:, :20].to_numpy()
    y_test = test_data[output_var].to_numpy().ravel()

    # model initialising and training set fitting
    regressor = LogisticRegression(solver='lbfgs', multi_class='multinomial')
    regressor.fit(x_train, y_train)

    # open a file, where you ant to store the data
    file = open('model.pkl', 'wb')

    # dump information to that file
    pickle.dump(regressor, file)

    # close the file
    file.close()
