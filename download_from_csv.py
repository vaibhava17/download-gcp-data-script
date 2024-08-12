import csv
import os
import subprocess

csv_file = 'cv_list.csv'

download_dir = 'downloaded_files'

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

with open(csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row['url']
        if url: 
            gs_url = url.replace("https://storage.googleapis.com/", "gs://")
            
            filename = gs_url.split('/')[-1]
            
            print(f'Converted URL: {gs_url}')
            
            command = f'gsutil cp "{gs_url}" "{download_dir}/{filename}"'
            
            try:
                subprocess.run(command, shell=True, check=True)
                print(f'Downloaded: {filename}')
            except subprocess.CalledProcessError as e:
                print(f'Failed to download {filename}: {e}')
                continue

print('All files downloaded.')
