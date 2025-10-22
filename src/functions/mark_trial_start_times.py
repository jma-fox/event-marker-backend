import pandas as pd


def mark_trial_start_times(data):
    task_data = data["task_data"]
    event_data = data["event_data"]
    bumper_index = data["bumper_index"]

    all_trial_starts = list(event_data[event_data['events'] == 'trial_start']['times'])
    task_trial_starts = all_trial_starts[-len(task_data):]

    if bumper_index is not None:
        if bumper_index == -1:
            task_trial_starts = [0.0] + task_trial_starts
            task_trial_starts = task_trial_starts[:len(task_data)]
        else:
            task_trial_starts.insert(bumper_index + 1, pd.NA)
            task_trial_starts = task_trial_starts[-len(task_data):]

    task_data['trial_start_time'] = task_trial_starts

    return task_data
