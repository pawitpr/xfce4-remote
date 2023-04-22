import requests
import os
from tqdm import tqdm

file_urls = [
    'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb ',
    'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ',

]  # Replace with a list of URLs of the files you want to download
blocks = input("Enter your block size for download file example: 4097")
for url in file_urls:
    filename = os.path.basename(url)

    response = requests.get(url, stream=True)

    total_size = int(response.headers.get('content-length', 0))
    block_size = blocks
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True, desc=filename)

    with open(filename, 'wb') as f:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)

    progress_bar.close()

    if total_size != 0 and progress_bar.n != total_size:
        print(f'Error: Download of {filename} failed.')
    else:
        print(f'Download of {filename} completed.')

os.system("ls")
os.system("sudo apt install ./chrome-remote-desktop_current_amd64.deb -y")
print("Installing Google chrome ")
os.system("sudo apt install ./google-chrome-stable_current_amd64.deb -y")
print("Installing XFCE4 ENV")
os.system("sudo DEBIAN_FRONTEND=noninteractive \
    apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver")

print("Done")
exit(0)