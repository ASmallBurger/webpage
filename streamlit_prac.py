import streamlit as st

st.title("File Upload Webpage")


uploaded_files = st.file_uploader(
    "Select Files",
    accept_multiple_files=True,
    type='csv'  #file types
)


if uploaded_files:
    st.write(f"{len(uploaded_files)} file(s) selected:")
    for file in uploaded_files:
        st.write(f"- {file.name}")
else:
    st.info("No files selected.")


with st.form("upload_form", clear_on_submit=True):
    submit = st.form_submit_button("Confirm Upload")
    if submit:
        if uploaded_files:
            st.success("Files uploaded successfully!")

        else:
            st.warning("Please select file(s) before confirming upload.")


st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)
