import streamlit as st
import csv
import os
import uuid
from datetime import datetime

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "ulinzi_records.csv")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "incident_id",
            "site_name",
            "region",
            "territory",
            "incident_date",
            "vandalism_type",
            "mitigation_applied",
            "security_status",
            "engineer_name",
            "audit_date",
            "equipment_category",
            "equipment_description",
            "service_impact",
            "downtime_hours",
            "permanent_fix"
        ])

if "incident_id" not in st.session_state:
    st.session_state.incident_id = None

st.set_page_config(page_title ="Ulinzibora" ,layout ="centered")
st.title("Ulinzi")
st.subheader("Vandalism incidents and technical audit tool")

DATA_DIR="data"
DATA_FILE=os.path.join(DATA_DIR,"ulinzi_records.csv")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

Headers=[
     "incident_id",
     "site name",
     "region",
     "incident_datetime",
     "vandalism_type",
     "mitigation_applied",
     "security_status",
     "engineer_name",
     "audit_date",
     "equipment_description",
     "service_impact",
     "downtime_hours",
     "permanent_fix"
]

if not os.path.exists(DATA_FILE):
    with open (DATA_FILE, mode="w" ,newline="") as file:
     writer = csv.writer(file)
     writer.writerow(Headers)

with st.form("ulinzi_form"):

    st.subheader("🛡️ Security Incident Details")
    site_name = st.text_input("Site Name")
    region = st.selectbox(
        "Region",
        [
           "Greater Western",
           "Rift",
           "Nairobi_West",
           "Nairobi_East",
           "Mount Kenya",
           "Coast",
        ]
    )

    territory = st.text_input("Territory")
    incident_datetime = st.date_input("Incident Date")

    vandalism_type = st.selectbox(
        "Nature of Vandalism",
        [
            "Fence cut",
            "Fuel drained",
            "Other"
        ]
    )

    mitigation_applied = st.text_input("Immediate Mitigation Applied")

    security_status = st.selectbox(
        "Security Status",
        ["Open", "Contained", "Closed"]
    )

    st.divider()

    st.subheader("🛠️ Technical Audit")
    engineer_name = st.text_input("Engineer Name")
    audit_date = st.date_input("Audit Date")

    equipment_category = st.selectbox(
        "Equipment Category",
        [
            "RF power cable",
            "RF fiber cable",
            "Electric strands",
            "Starter battery",
            "Grounding",
            "Fiber cable",
            "Other"
        ]
    )

    equipment_description = st.text_area("Equipment Description")

    service_impact = st.selectbox(
        "Service Impact",
        ["No Outage", "Partial Outage", "Full Outage"]
    )

    downtime_hours = st.number_input(
        "Downtime (Hours)",
        min_value=0.0
    )

    permanent_fix = st.selectbox(
        "Temporary Fix Applied?",
        ["Yes", "No"]
    )

    submit = st.form_submit_button("Submit Incident")


if submit:
    incident_id = f"ULINZI-{uuid.uuid4().hex[:8].upper()}"

    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
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

    st.success(f"Incident {incident_id} recorded successfully.")
if not all([site_name, region, engineer_name, equipment_description]):
    st.error("All mandatory fields must be filled.")
if submit:
    if not all([...]):
        st.error(...)
else:
        # write CSV here








