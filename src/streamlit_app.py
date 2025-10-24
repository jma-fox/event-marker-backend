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

        if 'trial_start_time' not in task_data.columns:
            task_data = mark_trial_start_times(task_data, event_data)

        st.write(task_data)

        event_names = event_data['events'].unique().tolist()
        selected_event = st.selectbox("Event to Mark:", options=event_names)

        st.write("")

        if st.button("Mark Task Events"):
            data = {
                "event_data": event_data,
                "task_data": task_data,
                "event": selected_event
            }

            task_data = mark_event_times(data)

            st.write("")

            st.write(task_data)

            experiment = task_data["Experiment"].iloc[0]
            file_name = f"{experiment}"

            st.download_button(
                label="Download Data",
                data=task_data.to_csv(index=False).encode('utf-8'),
                file_name=f'{file_name}.csv',
                mime='text/csv',
            )


if __name__ == '__main__':
    streamlit_app()
    