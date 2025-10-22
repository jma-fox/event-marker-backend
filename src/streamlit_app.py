import streamlit as st

from functions.extract_task_events import extract_task_events
from functions.read_task_file import read_task_file
from functions.mark_trial_start_times import mark_trial_start_times
from functions.mark_event_times import mark_event_times


def streamlit_app():
    st.set_page_config(page_title="Event Marker")
    st.title("Event Marker")

    task_file_path = st.text_input("Task File Path:")
    tdt_data_path = st.text_input("TDT Data Path:")

    st.write("")

    if task_file_path and tdt_data_path:
        event_data = extract_task_events(tdt_data_path)
        task_data = read_task_file(task_file_path)

        event_names = event_data['events'].unique().tolist()
        selected_event = st.selectbox("Event to Mark:", options=event_names, index=0)

        bumper_index = st.text_input("Bumper Index:", value="")
        try:
            bumper_index = int(bumper_index)
        except ValueError:
            bumper_index = None

        if st.button("Mark Task Events"):
            data = {
                "event_data": event_data,
                "task_data": task_data,
                "bumper_index": bumper_index,
                "selected_event": selected_event
            }

            st.write("")

            task_data = mark_trial_start_times(data)
            task_data = mark_event_times(data)

            st.write(task_data)

            date = task_data["Date"].iloc[0]
            experiment = task_data["Experiment"].iloc[0]
            file_name = f"{date}_{experiment}"

            st.download_button(
                label="Download Data",
                data=task_data.to_csv(index=False).encode('utf-8'),
                file_name=f'{file_name}.csv',
                mime='text/csv',
            )


if __name__ == '__main__':
    streamlit_app()
    