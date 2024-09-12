# PM-GPT-Dataset-Generator

## Overview

The **PM-GPT-Dataset-Generator** is a tool designed to create synthetic project management datasets that can be used to train Large Language Models (LLMs) for project management tasks. This generator aims to produce high-quality, diverse, and realistic datasets for use in AI models tailored for project management applications, such as task planning, resource allocation, risk management, and schedule optimization.

## Features

- **Synthetic Dataset Generation**: Automatically generates synthetic datasets for various project management domains, including Agile, Waterfall, and Hybrid methodologies.
- **Customizable Parameters**: Users can customize project types, size, complexity, deadlines, and risks.
- **Streamlit UI**: A simple and intuitive web-based interface built using Streamlit for easy dataset generation without manual configuration file editing.
- **Multilingual Support**: Generate project management datasets in different languages to train global models.
- **Scalable Output**: Create datasets of various sizes to meet training needs, from small samples to large datasets.
- **Flexible Formats**: Export datasets in multiple formats, including CSV, JSON, and Excel.

## Usage

### Prerequisites

Before using the **PM-GPT-Dataset-Generator**, ensure that you have the following installed:

- Python 3.7+
- **Streamlit** for running the web interface
- Required dependencies (listed in `requirements.txt`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/PM-GPT-Dataset-Generator.git
    cd PM-GPT-Dataset-Generator
    ```

2. Install dependencies, including Streamlit:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Web Interface

You can use **Streamlit** to interactively generate datasets through a web-based interface. To launch the interface, run:

```bash
streamlit run app.py

This will launch a web application that lets you configure the dataset parameters, such as project types, task complexity, resources, and risks, through an easy-to-use UI.

Dataset Generation (CLI)
For users preferring a command-line interface, datasets can also be generated via:

Configure the dataset parameters in config.json. Set the number of projects, types of tasks, milestones, resource allocation strategies, risks, etc.

Run the generator script:
python generate_dataset.py --config config.json

This will generate a dataset based on the parameters set in the config.json file.

Example Configuration (config.json)

{
  "project_count": 100,
  "methodologies": ["Agile", "Waterfall", "Hybrid"],
  "task_types": ["Development", "Testing", "Deployment", "Documentation"],
  "resources": {
    "developers": 10,
    "testers": 5,
    "project_managers": 3
  },
  "risk_levels": ["low", "medium", "high"],
  "output_format": "csv"
}

Output Example
After running the generator, you will find the output dataset in the output/ directory (or your specified directory). The dataset will contain information like:

Project Names
Task Lists
Start and End Dates
Resource Allocations
Risk Analysis
Command-Line Options
The script supports the following command-line options:

--config: Path to the configuration file (default: config.json)
--output_dir: Directory to store the generated dataset (default: output/)

python generate_dataset.py --config config.json --output_dir /my/output/dir

Customization
Adding Custom Project Management Scenarios
You can add more scenarios to the dataset generation by modifying the scenarios.py file. This allows you to introduce new types of tasks, risks, or methodologies specific to your use case.

Extending Dataset Formats
If you need the dataset in a specific format that is not yet supported (e.g., XML or SQL), you can extend the export logic by editing the exporter.py file.

Contributing
Contributions are welcome! To contribute:

Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/your-feature)
Create a new Pull Request
