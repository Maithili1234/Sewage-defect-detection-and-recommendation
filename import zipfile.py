import zipfile

with zipfile.ZipFile('D:\\New folder\\first sewer dataset.v1i.yolov8.zip', 'r') as zip_ref:



    zip_ref.extractall('unzipped_dataset')

