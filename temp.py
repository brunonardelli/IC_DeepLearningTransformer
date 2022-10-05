import pandas as pd

if __name__ == '__main__':
    df_train = pd.read_csv('Data\\train_dataset.csv')
    df_test = pd.read_csv('Data\\test_dataset.csv')

    print(df_test.info())