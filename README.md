# URL Dataset Crawling Project

This project includes a Python-based web crawler designed to extract data from a list of URLs and save the crawled content in various formats. The crawler is built using Scrapy, a fast high-level web crawling and web scraping framework.

## Prerequisites

- Python 3.6+
- pip (Python package installer)

## Installation

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/padas-lab-de/url-dataset-crawling.git
cd url-dataset-crawling
```

### 2. Set Up a Virtual Environment

Create a virtual environment to manage the project's dependencies separately from other Python projects:

```bash
# For Unix or MacOS
python3 -m venv env
source env/bin/activate

# For Windows
python -m venv env
.\env\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages specified in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

### Configuring the Crawler

1. **Input Data**: Place your list of URLs in a `.csv` or `.txt` file within the `data/inputs/` directory. Ensure the CSV file has a column named `url` containing the URLs.

2. **Output Format**: Decide on the format for the output data. Options include:
   - CSV file (`csv`): Appends crawled content to a CSV file.
   - JSON Lines file (`jsonl`): Stores each item in a separate line in JSON format.
   - HTML files (`html`): Saves complete HTML content to individual files and indexes them in a CSV file.

### Running the Crawler

Navigate to the project's root directory and run `main.py` using Python:

```bash
python main.py
```

You will be prompted to enter:
- The **input type** (`csv` or `txt`).
- The **output type** (`csv`, `jsonl`, or `html`).
- The **path to the input file** (relative to the project root).
- The **path to the output file or directory** (relative to the project root).

Example interaction:

```
Enter input type (csv/txt): csv
Enter output type (csv/jsonl/html): csv
Enter path to input file: data/inputs/OWS_URL_DS.csv
Enter path to output file/directory: data/outputs/output.csv
```

### Logs

Logs are saved in the `logs/` directory, which helps in troubleshooting and understanding the crawler's behavior.

## Troubleshooting

- **ModuleNotFoundError**: Ensure all scripts are being run from the project's root directory and the virtual environment is activated.
- **IOError or PermissionError**: Check the permissions of the directory where you are trying to write the output files. Ensure the directory exists and is writable.
