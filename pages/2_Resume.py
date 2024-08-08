import streamlit as st
st.title("Resume Prep")
st.write("This will generate formatted resume based on your input and you can copy and paste to your word processor.")
st.divider()

st.subheader("Selection a layout")
layouts = st.columns(3)

st.subheader("Basic Info")
name = st.text_input("Applicant Name")
columns = st.columns(2)
with columns[0]:
    location = st.text_input("Location")
    linkedIn = st.text_input("LinkedIn")
with columns[1]:
    email = st.text_input("Email")
    portfolio = st.text_input("Portfolio")
st.divider()

st.subheader("Education")
num_edu = st.number_input("Number of items in the Education section", 1)
edu_list = list()
for i in range(num_edu):
    obj = dict()
    columns = st.columns(3)
    with columns[0]:
        obj["school"] = st.text_input(f"School Name {i+1}")
        obj["degree_type"] = st.text_input(f"Degree Type {i+1}")
        obj["gpa"] = st.text_input(f"GPA {i+1}")

    with columns[1]:
        obj["location"] = st.text_input(f"School Location {i+1}")
        obj["major"] = st.text_input(f"Major {i+1}")
        obj["coursework"] = st.text_input(f"Coursework {i+1}")
    with columns[2]:
        obj["grad_date"] = st.text_input(f"Graduation Date {i+1} (or Expected)")
        obj["minor"] = st.text_input(f"Minor {i+1}")
        obj["honors"] = st.text_input(f"Honors & Awards {i+1}")
    edu_list.append(obj)
    st.divider()

st.subheader("Professional Experience")
num_prof = st.number_input("Number of items in the Professional Experience section", 1)
prof_list = list()
for i in range(num_prof):
    pass

st.subheader("Projects")
num_prof = st.number_input("Number of items in the Projects section", 1)

st.subheader("Skills")
num_prof = st.number_input("Number of bullet points in the Skills section", 1)

st.button("Generate", type="primary")