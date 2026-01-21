import streamlit as st
import csv
import os
import uuid
from datetime import datetime

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
    "site_id",
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
    "temporary_fix"
]

if not os.path.exists(DATA_FILE):
    with open (DATA_FILE, mode="w" ,newline="") as file:
     writer = csv.writer(file)
     writer.writerow(Headers)

with st.form("ulinzi_form"):
    st.markdown("Security Incident Details")
    site_id = st.text_input("Site ID")
    region = st.text_input("Region")
    territory = st.text_input("territory")
    incident_datetime = st.date_input("Incident Date")
    submitted = st.form_submit_button("Submit Incident")
    
    if submitted:
      st.success("Incident recorded successfully!")

    vandalism_type = st.selectbox(
        "Type of Vandalism",
        ["Starter battery Theft", "RF power cable cut", "Fence cut","RF fiber cable cut" "Other"]
    )

    mitigation_applied = st.text_input("Immediate Mitigation Applied")
    security_status = st.selectbox(
        "Security Status",
        ["Open", "Contained", "Closed"]
    )

    st.markdown("---")
    st.markdown("Technical Audit")

    engineer_name = st.text_input("Engineer Name")
    audit_date = st.date_input("Audit Date")

    equipment_category = st.selectbox(
        "Equipment Category",
        [
            "RF power cable",
            "RF fiber cable",
            "Electric strands",
            "Starter battery",
            "grounding",
            "Fiber cable"
            "Other"
        ]
    )

equipment_description = st.text_area("Equipment Description")

with st.form("incident_form"):
 service_impact = st.selectbox(
        "Service Impact",
        ["No Outage", "Partial Outage", "Full Outage"]
    )
 downtime_hours = st.number_input(
     "Downtime (Hours)", 
     min_value=0.0
     )
 temporary_fix = st.selectbox(
     "Temporary Fix Applied?", 
     ["Yes", "No"]
     )
 submit = st.form_submit_button("Submit Incident")
    
if "incident_id" in st.session_state:
    st.success(
        f"Incident {st.session_state.incident_id} recorded successfully."



   

with open(DATA_FILE, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([ 
                      "incident_id",
                      "site name",
                      "site_id",
                      "region",
                      "incident_datetime",
                      "vandalism_type",
                      "mitigation_applied",
                      "security_status",
                      "engineer_name",
                      "audit_date",
                      "equipment description",
                      "sercice_impact",
                      "downtime_hours",
                      "temporary_fix",
                    
                    
 ])


st.success(
  f"Incident {st.session_state.incident_id} recorded successfully."
)






    


    

   


















