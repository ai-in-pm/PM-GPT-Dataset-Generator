'''
This file contains the main code for the Synthetic Project Management-GPT Dataset Generator web application using Streamlit.
'''
import streamlit as st
from dataset_generator import DatasetGenerator
def main():
    st.title("Synthetic Project Management-GPT Dataset Generator")
    generator = DatasetGenerator()
    num_projects = st.number_input("Number of Projects", min_value=1, step=1)
    num_tasks = st.number_input("Number of Tasks per Project", min_value=1, step=1)
    include_description = st.checkbox("Include Task Descriptions")
    if st.button("Generate Dataset"):
        dataset = generator.generate_dataset(num_projects, num_tasks, include_description)
        st.json(dataset)
if __name__ == "__main__":
    main()