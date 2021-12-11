# A class to make time series forecasts
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pmdarima as pm


class CGForecaster:
    """
    A class to make time series forecasts
    """
    def __init__(self, data:pd.DataFrame, target: str):
        """
        Initialize the CGForecaster object
        :type data: Pandas DataFrame
        """
        self.data = data
        self.target = target

    def preprocess(self, target: str, data: pd.DataFrame,
                   drop_cols: list = None,
                   drop_rows: list = None,
                   fill_na: str = 'ffill',
                   fill_val: float = 0.0):
        """
        Preprocess the data
        :type target: str
        :type data: Pandas DataFrame
        :type drop_cols: list
        :type drop_rows: list
        :type fill_na: str
        :type fill_val:
        """
        if drop_cols is not None:
            data.drop(drop_cols, axis=1, inplace=True)
        if drop_rows is not None:
            data.drop(drop_rows, axis=0, inplace=True)
        data.fillna(value=fill_val, inplace=True)
        self.data = data

    def train(self, target: str, data: pd.DataFrame,
              drop_cols: list = None,
              drop_rows: list = None,
              fill_na: str = 'ffill',
              fill_val: float = 0.0):
        """
        Train the model
        :type target: str
        :type data: Pandas DataFrame
        :type drop_cols: list
        :type drop_rows: list
        :type fill_na: str
        :type fill_val: float
        """
        self.preprocess(target, data, drop_cols, drop_rows, fill_na, fill_val)
        self.model = pm.auto_arima(self.target, start_p=1, start_q=1,
                                   test='adf', max_p=3, max_q=3, m=12,
                                   d=None, seasonal=False,
                                   start_P=0, D=0,
                                   trace=True, error_action='ignore',
                                   suppress_warnings=True,
                                   stepwise=True)

    def forecast(self, n_periods: int = 1):
        """
        Make a forecast
        :type n_periods: int
        """
        self.forecast = self.model.predict(n_periods=n_periods)


    def postprocess(self, target: str, data: pd.DataFrame,
                    drop_cols: list = None,
                    drop_rows: list = None,
                    fill_na: str = 'ffill',
                    fill_val: float = 0.0):
        """

        :param target:
        :param data:
        :param drop_cols:
        :param drop_rows:
        :param fill_na:
        :param fill_val:
        :return:
        """
        return None 


    def thingificate(self, stuff):
        """
        
        """
