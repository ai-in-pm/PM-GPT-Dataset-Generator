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
