import math
from typing import List, Union

import time
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import mean_absolute_error, mean_squared_error

import nvidia_smi

def get_df(file: str, header=None, sample: bool = False, sample_number: int = 1000):
    if sample:
        df = pd.read_csv(file, header=None).sample(sample_number)
    else:
        df = pd.read_csv(file, header=None)

    df.columns = pd.read_csv("{}.header".format(
        file.split('.csv')[0])).columns if header is None else header
    return df

def transform_column_to_one_hot_encoding(
    df: pd.DataFrame, 
    df_column: Union[str, int]
    ) -> pd.DataFrame:
    if type(df_column) == int:
        df_column = df.columns[df_column] # type: ignore   
                
    one_hot_columns = pd.get_dummies(df[df_column])
    
    return pd.concat([df.drop(axis=1, labels=[df_column]), one_hot_columns], axis=1)

def merge_one_hot_columns(
    df: pd.DataFrame, 
    columns: List[Union[str, int]], 
    column_name: str, 
    drop_merged: bool = True
    ) -> pd.DataFrame:
    if type(columns[0]) == int:
        columns = df.columns[columns]

    merged_series: pd.Series = df[columns].agg('sum', axis=1)
    merged_series.index.name
    if drop_merged:
        df = df.drop(columns=columns)
    
    df[column_name] = merged_series
    
    return df

def get_device() -> torch.device:
    device_as_string = get_device_as_string()
    return torch.device(device_as_string)


def get_device_as_string() -> str:
    if torch.cuda.is_available():
        return 'cuda'
        # cuda_devices = get_available_cuda_devices()
        # # if more than one gpu are available, use all of them
        # if len(cuda_devices) > 1:
        #     if len(cuda_devices) == len(get_available_cuda_devices()):
        #         return 'cuda'
        #     else:
        #         # return 'cuda:1'
        #         cuda_devices = get_available_cuda_devices()
        #         # return cuda_devices[0]
        # elif len(cuda_devices) == 1:
        # # if only one gpu is available, return the cuda id (cuda:0) of it
        #     return cuda_devices[0]
        
    # if no gpu available, use cpu instead
    return 'cpu'


def get_rmse(actual_values, predicted_values) -> float:
    '''returns the root mean squared error'''
    return math.sqrt(mean_squared_error(actual_values, predicted_values))


def get_mape(actual_values, predicted_values):
    '''returns the mean absolute percentage error'''
    return np.mean(np.abs(actual_values - predicted_values) / np.abs(actual_values) * 100)


def get_mae(actual_values, predicted_values) -> float:
    '''returns the mean absolute error'''
    return mean_absolute_error(actual_values, predicted_values)


def get_available_cuda_devices(free_mem_threshold: float = 0.90) -> List[str]:
    available_gpus: List[str] = []
    if torch.cuda.is_available() == False:
        print('No CUDA device available')
    
    elif torch.cuda.is_available():
        nvidia_smi.nvmlInit()
        time.sleep(1)
        device_count = nvidia_smi.nvmlDeviceGetCount()
        
        for idx in range(device_count):
            handle = nvidia_smi.nvmlDeviceGetHandleByIndex(idx)
            info = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
            
            free_memory: float = info.free / info.total
            
            if free_memory >= free_mem_threshold:
                available_gpus.append(f'cuda:{idx}')
                
        nvidia_smi.nvmlShutdown()
    return available_gpus

def plot_column(actual_values: pd.DataFrame, predicted_values: pd.DataFrame, column_number: int = 0, rmse_threshold: float = 0.30, is_training: bool = True):

    label_columns = actual_values.columns

    if len(label_columns) <= column_number:
        print('Out of Prediction Bounds')
        return

    plt.figure(figsize=(25, 15))  # plotting
    plt.rcParams.update({'font.size': 22})

    column = label_columns[column_number]
    pred_column = f"pred_{column}_{'training' if is_training else 'test'}"

    rmse = get_rmse(actual_values[column], predicted_values[column])
    mae = mean_absolute_error(actual_values[column], predicted_values[column])

    predicted_color = 'green' if rmse < rmse_threshold else 'orange'

    plt.plot(actual_values[column], label=column, color='black')  # actual plot
    plt.plot(predicted_values[column], label=pred_column, color=predicted_color)  # predicted plot

    plt.title('Time-Series Prediction')
    plt.plot([], [], ' ', label=f'RMSE: {rmse}')
    plt.plot([], [], ' ', label=f'MAE: {mae}')
    plt.legend()
    plt.ylabel('timeline', fontsize=25)
    
    # if INCLUDE_WANDB:
    #     wandb.log({pred_column: wandb.Image(plt)})
    #     wandb.summary[f'Root Mean Squared Error ({column})'] = rmse
    #     wandb.summary[f'Mean Absolute Error ({column})'] = mae
        
    plt.show()

                
                
if '__main__' == __name__:
    print(get_available_cuda_devices())
    print(get_device_as_string())
    print(get_device())