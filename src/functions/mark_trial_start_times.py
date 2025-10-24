import pandas as pd


def mark_trial_start_times(task_data, event_data):
    all_trial_starts = list(event_data[event_data['events'] == 'trial_start']['times'])
    task_trial_starts = all_trial_starts[-len(task_data):]
    task_data['trial_start_time'] = task_trial_starts

    return task_data
