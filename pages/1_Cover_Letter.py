import streamlit as st
from helper.cover_letter import CoverLetter

cl = CoverLetter()
template_instruction = """ Please use these template tags when writing your cover letter templete:
            Company Name: [Company Name], 
            Job Title: [Job Title],
            Referral/Where did you find this job: [Referral Source],
            Applicant/Your Name: [Applicant Name]"""

st.title("Cover Letter Prep")
st.divider()

# cl_settings_file = st.file_uploader("Choose a file")
# if cl_settings_file is not None:
#     # File is read as bytes:
#     bytes_data = cl_settings_file.getvalue()
#     json_data = cl.import_from_file(bytes_data)

# Input fields
col1, col2 = st.columns(2)

with col1:
    company_name = st.text_input("Company Name")
    cl.company_name = company_name
    print(cl.company_name)
    job_title = st.text_input("Job Title")
    cl.job_title = job_title

with col2:
    referer = st.text_input("Referral Source")
    cl.referer = referer
    applicant_name = st.text_input("Applicant Name")
    cl.applicant_name = applicant_name

cover_letter_templete = st.text_area("Cover Letter Template", height=360,
                                     placeholder=template_instruction)
cl.template = cover_letter_templete

# Save Button
st.download_button("Save Input Values", data=cl.export_to_json(), file_name="cover_letter_settings.json", mime="application/json")

# Fill template button
fill_btn = st.button("Fill Cover Letter Template")
if fill_btn:
    st.text(cl.fill_template())