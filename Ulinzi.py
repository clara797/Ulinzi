import streamlit as st
import csv
import os
import uuid
import pandas as pd
from datetime import datetime


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = None

if "roles" not in st.session_state:
    st.session_state.roles = []


USERS = {
    "cnasimiyu": {"password": "safaricom123", "roles": ["Technical", "Management","Security"]},
    "rmoenga":{"password":"safaricom123", "roles":["Technical", "Management","Security"] },

}

submit = False

def show_login():
    st.title("🔐 Ulinzi Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.roles = USERS[username]["roles"]
            st.success(
                f"Logged in as {username} "
                f"({', '.join(st.session_state.roles)})"
            )
            st.rerun()
        else:
            st.error("Invalid username or password")

if not st.session_state.logged_in:
    show_login()
    st.stop()


st.set_page_config(page_title="Ulinzibora", layout="centered")

st.title("🛡️ Ulinzibora")
st.caption("Vandalism incidents and technical audit tool")

st.sidebar.success(f"User: {st.session_state.username}")
st.sidebar.info(
    f"Roles: {', '.join(st.session_state.roles)}"
)



DATA_DIR="data"
DATA_FILE=os.path.join(DATA_DIR,"ulinzi_records.csv")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

Headers=[
     "incident_id",
     "site_name",
     "region",
     "territory",
     "incident_datetime",
     "vandalism_type",
     "mitigation_applied",
     "security_status",
     "engineer_name",
     "audit_date",
     "equipment category",
     "equipment_description",
     "service_impact",
     "downtime_hours",
     "permanent_fix"
]

if not os.path.exists(DATA_FILE):
    with open (DATA_FILE, mode="w" ,newline="") as file:
     writer = csv.writer(file)
     writer.writerow(Headers)

if any(r in st.session_state.roles for r in ["Security", "Technical"]):

    with st.form("incident_form"):
        st.subheader("🛡️ Security Incident + Technical Audit")

        site_name = st.text_input("Site Name")
        region = st.selectbox(
            "Region",
            ["Greater Western", "Rift", "Nairobi_West","Nairobi_East" "Coast"]
        )
        territory = st.text_input("Territory")
        incident_datetime = st.date_input("Incident Date")

        vandalism_type = st.selectbox(
            "Nature of Vandalism",
            ["Fence cut", "Fuel drained", "Other"]
        )

        mitigation_applied = st.text_input("Immediate Mitigation Applied")
        security_status = st.selectbox(
            "Security Status", ["Open", "Contained", "Closed"]
        )

        st.divider()
        st.subheader("🛠️ Technical Audit")

        engineer_name = st.text_input("Engineer Name")
        company_name = st.selectbox (
          "Company Name",  
          ["Safaricom", "Huawei","Nextgen","Tetranet", "Adrian" "Kinde" "other"]
        
        )
        ticket_number = st.text_input("Ticket number")
        audit_date = st.date_input("Audit Date")

        equipment_category = st.selectbox(
            "Equipment Category",
            ["RF power cable", "RF fiber cable","Transmission Fiber cable", "Starter Battery", "Other"]
        )

        equipment_description = st.text_area("Equipment Description")

        service_impact = st.selectbox(
            "Service Impact",
            ["No Outage", "Partial Outage", "Full Outage"]
        )

        downtime_hours = st.number_input(
            "Downtime (Hours)", min_value=0.0
        )

        permanent_fix = st.selectbox(
            "Permanent Fix Applied?", ["Yes", "No"]
        )

    submit = st.form_submit_button("Submit Incident")


    if submit:
        if not all([
            site_name,
            region,
            territory,
            engineer_name,
            equipment_description
        ]):
            st.error("Please fill all mandatory fields.")
        else:
            incident_id = f"ULINZI-{uuid.uuid4().hex[:8].upper()}"

            with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    incident_id,
                    site_name,
                    region,
                    territory,
                    incident_datetime,
                    vandalism_type,
                    mitigation_applied,
                    security_status,
                    engineer_name,
                    audit_date,
                    equipment_category,
                    equipment_description,
                    service_impact,
                    downtime_hours,
                    permanent_fix
                ])

            st.success(
                f"Incident {incident_id} recorded successfully."
            )


if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame()


if "Management" in st.session_state.roles:
    st.divider()
    st.header("📊 Management Dashboard")

    df = pd.read_csv(DATA_FILE)

    st.subheader("Top Vandalized Sites")
    st.bar_chart(df["site_name"].value_counts())

    st.subheader("Incidents by Region")
    st.bar_chart(df["region"].value_counts())

    total_downtime = df["downtime_hours"].sum()
    st.metric("Total Downtime (Hours)", total_downtime)



st.markdown("---")
st.subheader("⬇️ Export Audit Report")

if not df.empty:
    st.download_button(
        label="Download CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="ulinzi_audit_report.csv",
        mime="text/csv"
    )
else:
    st.info("No data available to download yet.")
















