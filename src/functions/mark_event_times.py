

def mark_event_times(data):
    task_data = data["task_data"]
    event_data = data["event_data"]
    event = data["event"]
    trial_starts = list(task_data['trial_start_time'])
    event_times = []

    for i in range(len(trial_starts)):
        trial_start = trial_starts[i]

        if i + 1 < len(trial_starts):
            trial_stop = trial_starts[i + 1]
        else:
            trial_stop = float('inf')

        filter_1 = (event_data['times'] >= trial_start)
        filter_2 = (event_data['times'] < trial_stop)
        filter_3 = (event_data['events'] == event)
        event_time = event_data[filter_1 & filter_2 & filter_3]['times']

        if not event_time.empty:
            event_time = event_time.iloc[0]
            event_times.append(event_time)
        else:
            event_times.append(None)

    task_data[f"{event}_time"] = event_times

    return task_data
