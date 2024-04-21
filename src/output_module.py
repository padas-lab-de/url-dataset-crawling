import pandas as pd
import json
import os
from datetime import datetime

def save_to_csv(data, file_path):
    """
    Append the provided data to a CSV file at the specified or a default file path.
    
    Args:
        data (list of dict): Data to be saved.
        file_path (str): Path to the CSV file where the data should be appended. If empty, a default path is used.
        
    Raises:
        Exception: If there is an IOError due to file writing.
    """
    if not file_path:
        file_path = os.path.join('default_output', f'default_output_file.csv')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        df = pd.DataFrame(data)
        df.to_csv(file_path, mode='a', index=False)
    except IOError as e:
        raise Exception(f"Failed to write to CSV file at {file_path}: {e}")

def save_to_jsonl(data, file_path):
    """
    Append the provided data to a JSONL file at the specified or a default file path.
    
    Args:
        data (list of dict): Data to be saved.
        file_path (str): Path to the JSONL file where the data should be appended. If empty, a default path is used.
        
    Raises:
        Exception: If there is an IOError due to file writing.
    """
    if not file_path:
        file_path = os.path.join('default_output', f'default_output_file.jsonl')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, 'a') as file:
            for item in data:
                file.write(json.dumps(item) + '\n')
    except IOError as e:
        raise Exception(f"Failed to write to JSONL file at {file_path}: {e}")

def save_html_content(data, html_dir, index_csv):
    """
    Save HTML content to individual files in a specified or default directory and index them in a CSV file.
    
    Args:
        data (list of dict): List containing URL, HTML content, and UID for each item.
        html_dir (str): Directory where HTML files will be saved. If empty, a default directory is used.
        index_csv (str): CSV file path to append index data of HTML files. If empty, a default path is used.
        
    Raises:
        Exception: If there are any issues creating directories or writing files.
    """
    if not html_dir:
        html_dir = os.path.join('default_output', 'html')
    if not index_csv:
        index_csv = os.path.join(html_dir, 'index.csv')
    try:
        os.makedirs(html_dir, exist_ok=True)
        index_data = []
        for item in data:
            file_path = os.path.join(html_dir, f"{item['uid']}.html")
            with open(file_path, 'w') as file:
                file.write(item['html'])
            index_data.append({'uid': item['uid'], 'url': item['url'], 'file_path': file_path})
        pd.DataFrame(index_data).to_csv(index_csv, mode='a', header=False, index=False)
    except IOError as e:
        raise Exception(f"Failed to write HTML content or update index CSV at {html_dir} or {index_csv}: {e}")
    except OSError as e:
        raise Exception(f"Failed to create directory {html_dir} or write files: {e}")
