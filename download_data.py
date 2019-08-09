import os
import wget
import zipfile
import shutil
from input_parameter import get_args

def download_unzip(url):
    filename = wget.download(url)
    shutil.move(filename, './data')
    filename = os.path.join('./data', filename)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall('./data')
        os.remove(filename)
args = get_args()
if not os.path.isdir(args.DATADIR):
    os.mkdir(args.DATADIR)

DSD100_url = 'http://liutkus.net/DSD100.zip'
DSD100subset_url = 'https://www.loria.fr/~aliutkus/DSD100subset.zip'

DSD100_dir = os.path.join('./data', 'DSD100')
DSD100subset = os.path.join('./data', 'DSD100subset')

if not os.path.isdir(DSD100_dir):
    download_unzip(DSD100_url)
if not os.path.isdir(DSD100subset):
    download_unzip(DSD100subset_url)
