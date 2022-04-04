from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def data_preprocess(df, categorical_cols, float_cols):

    df[categorical_cols] = df[categorical_cols].astype('category')
    df[float_cols] = df[float_cols].astype('float')

    return df