sudo apt install python3 -y
pip install requests
pip install tqdm
python3 start.py

sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session'
sudo systemctl disable lightdm.service
echo "Go to https://remotedesktop.google.com/headless and click on next then authorize and copy the debian code and paste here"

read -p "code" code

$code