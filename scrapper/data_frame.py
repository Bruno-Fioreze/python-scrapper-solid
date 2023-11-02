import pandas as pd
from io import StringIO

class DataFrameReader:
    def __init__(self, tables):
        self.tables = tables

    def read_dataframes(self):
        dataframes = [pd.read_html(StringIO(str(table)))[0] for table in self.tables]
        return dataframes

class DataFrameColumnRemove:
    def remove_columns(self, df, columns):
        return df.drop(columns, axis=1)

class DataFrameSlicer:
    def slice_column(self, df, column, stop):
        df[column] = df[column].str.slice(stop=stop)
        return df

class DataFrameConcatenator:
    def concat_dataframes(self, dataframes, axis=1):
        return pd.concat(dataframes, axis=axis)