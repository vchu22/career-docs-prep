import streamlit as st
from helper.cover_letter import CoverLetter, template_instructions

# declare variables
cl = CoverLetter()
# Start of page
st.title("Cover Letter Prep")
st.divider()

# Load Input Values
cl_settings_file = st.file_uploader("Choose a JSON file to load input values")
if cl_settings_file is not None:
    # File is read as bytes:
    bytes_data = cl_settings_file.getvalue()
    json_data = cl.import_from_file(bytes_data)

# Input fields
col1, col2 = st.columns(2)

with col1:
    cl.company_name = st.text_input("Company Name", value=cl.settings['company_name'])
    cl.job_title = st.text_input("Job Title", value=cl.settings['job_title'])

with col2:
    cl.referer = st.text_input("Referral Source", value=cl.settings['referer'])
    cl.applicant_name = st.text_input("Applicant Name", value=cl.settings['applicant_name'])

# Use custom tags
custom_tags = st.radio("Custom Template Tags", ["Yes", "No"], index=1) == "Yes"
if custom_tags:
    col1, col2 = st.columns(2)

    with col1:
        company_tag = st.text_input("Company Name Tag", value="[Company Name]")
        job_tag = st.text_input("Job Title Tag", value="[Job Title]")

    with col2:
        referer_tag = st.text_input("Referral Source Tag", value="[Referral Source]")
        applicant_tag = st.text_input("Applicant Name Tag", value="[Applicant Name]")

cl.template = st.text_area("Cover Letter Template", value=cl.settings['template'],
                               height=360, placeholder=template_instructions)

# Save Button
st.download_button("Save Input Values", data=cl.export_to_json(), file_name="cover_letter_settings.json", mime="application/json")

# Fill template button
fill_btn = st.button("Fill Cover Letter Template", type="primary")

if fill_btn:
    if custom_tags:
        res_text = cl.fill_template(company_tag, job_tag, referer_tag, applicant_tag)
    else:
        res_text = cl.fill_template()
    st.text_area("Cover Letter", value=res_text, height=360)