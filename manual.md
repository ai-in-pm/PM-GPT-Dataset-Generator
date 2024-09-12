# Synthetic Project Management-GPT Dataset Generator User Manual

## Introduction
The Synthetic Project Management-GPT Dataset Generator is a web application developed using Streamlit. It allows users to generate synthetic project management datasets for training and testing natural language processing models, specifically GPT models.

## Installation
To use the Synthetic Project Management-GPT Dataset Generator, follow these steps:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone the repository containing the code for the Synthetic Project Management-GPT Dataset Generator.

3. Open a terminal or command prompt and navigate to the directory where the code is located.

4. Create a virtual environment (optional but recommended) by running the following command:
   ```
   python -m venv venv
   ```

5. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

6. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage
To use the Synthetic Project Management-GPT Dataset Generator, follow these steps:

1. Make sure you have completed the installation steps mentioned above.

2. Open a terminal or command prompt and navigate to the directory where the code is located.

3. Activate the virtual environment (if you created one) by running the appropriate command mentioned in the installation steps.

4. Run the following command to start the web application:
   ```
   streamlit run main.py
   ```

5. The web application will start running and you will see a browser window open with the application interface.

6. In the web application interface, you will see the following options:
   - Number of Projects: Enter the desired number of projects for the dataset.
   - Number of Tasks per Project: Enter the desired number of tasks per project for the dataset.
   - Include Task Descriptions: Check this option if you want to include task descriptions in the dataset.
   - Generate Dataset: Click this button to generate the dataset based on the provided inputs.

7. After clicking the "Generate Dataset" button, the generated dataset will be displayed in JSON format on the web application interface.

8. You can copy the generated dataset for further use or analysis.

## Conclusion
The Synthetic Project Management-GPT Dataset Generator is a powerful tool for generating synthetic project management datasets. By following the installation and usage instructions provided in this user manual, you can easily generate datasets for training and testing natural language processing models.