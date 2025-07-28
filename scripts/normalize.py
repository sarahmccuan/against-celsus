import glob
import sys
from greek_normalisation.utils import convert_to_2019, nfc
from text_validator.main import validate
from pathlib import Path 

def normalize_file(filename):
    try: 
        with open(filename, 'r+', encoding='utf-8') as f:
            file_contents = f.read()
            f.seek(0)
            f.write(nfc(convert_to_2019(file_contents)))
            f.truncate()
    except:
        print('Error: ' + str(sys.exc_info()[0]))

files_list = ['book7.md']

for file in files_list:
    normalize_file(file)