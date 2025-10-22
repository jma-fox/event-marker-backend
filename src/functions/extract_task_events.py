from pathlib import Path

from functions.get_events_from_block import get_events_from_block
from functions.get_events_from_struct import get_events_from_struct
from event_code_dict import event_code_dict


def extract_task_events(tdt_path):
    tdt_path = Path(tdt_path)

    if tdt_path.is_dir():
        event_data = get_events_from_block(tdt_path)
    else:
        event_data = get_events_from_struct(tdt_path)

    event_data['events'] = event_data['events'].map(event_code_dict)

    return event_data
    