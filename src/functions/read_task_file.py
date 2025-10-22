import pandas as pd


def read_task_file(file_path):
    task_data = pd.read_csv(file_path)

    return task_data
