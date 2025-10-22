from tdt import read_block
import pandas as pd


def get_events_from_block(tdt_path):
    tdt_data = read_block(tdt_path, evtype=["epocs"])
    events = tdt_data["epocs"]["eve_"]["data"]
    times = tdt_data["epocs"]["eve_"]["onset"]
    event_data = pd.DataFrame({"events": events, "times": times})

    return event_data
