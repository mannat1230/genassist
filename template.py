import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

list_of_files = [
    'requirements.txt',
    'Dockerfile',
    '.github/workflows/ci.yml',
    'app/main.py',
    'app/summarizer.py',
    'ui/gradio-app.py'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the file: {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty file: {filepath}')
                         
    
    else:
        logging.info(f'{filename} already exists.')