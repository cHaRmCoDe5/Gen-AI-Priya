import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Leave Management")

st.title("Employee Leave Management")

role = st.sidebar.selectbox(
    "Select Dashboard",
    ["Employee Dashboard", "Manager Dashboard"]
)

# -----------------------------------
# Employee Dashboard
# -----------------------------------
if role == "Employee Dashboard":

    st.header("Apply Leave")

    emp_id = st.text_input("Employee ID")
    emp_name = st.text_input("Employee Name")

    start_date = st.date_input("Leave Start Date")
    end_date = st.date_input("Leave End Date")

    if st.button("Submit Leave"):

        response = requests.post(
            f"{API_URL}/apply_leave",
            params={
                "employee_id": emp_id,
                "employee_name": emp_name,
                "start_date": start_date,
                "end_date": end_date
            }
        )

        st.success(response.json()["message"])

    st.divider()

    st.subheader("View Leave Status")

    history_id = st.text_input(
        "Employee ID to View Status"
    )

    if st.button("Get Leave History"):

        response = requests.get(
            f"{API_URL}/leave_history/{history_id}"
        )

        data = response.json()

        if data:
            st.dataframe(pd.DataFrame(data))
        else:
            st.info("No records found")


# -----------------------------------
# Manager Dashboard
# -----------------------------------
if role == "Manager Dashboard":

    st.header("Manager Approval Dashboard")

    response = requests.get(
        f"{API_URL}/leave_requests"
    )

    data = response.json()

    df = pd.DataFrame(data)

    st.dataframe(df)

    leave_id = st.number_input(
        "Leave ID",
        min_value=1
    )

    action = st.radio(
        "Action",
        ["Approve", "Reject"]
    )

    if st.button("Submit Decision"):

        if action == "Approve":

            response = requests.put(
                f"{API_URL}/approve_leave/{leave_id}"
            )

        else:

            response = requests.put(
                f"{API_URL}/reject_leave/{leave_id}"
            )

        st.success(response.json()["message"])

        st.rerun()