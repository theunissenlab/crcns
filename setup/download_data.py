from download import download

# Url to data for the class
url = 'https://www.dropbox.com/s/hkrfyj2poizx9br/data.zip?dl=1'
# XXX another URL for course presentation material?

# Download and unzip the data for the course
download(url, '../data/', zipfile=True)
