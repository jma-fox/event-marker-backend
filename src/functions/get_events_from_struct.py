from functions.read_tdt_struct import read_tdt_struct
import pandas as pd


def get_events_from_struct(tdt_data_path):
    tdt_data = read_tdt_struct(tdt_data_path)
    events = tdt_data["epocs"]["eve_"]["data"][0]
    times = tdt_data["epocs"]["eve_"]["onset"][0]
    event_data = pd.DataFrame({"events": events, "times": times})

    return event_data
