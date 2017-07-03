import os

os.system("curl -L https://source.unsplash.com/1920x1080/?nature > /home/user/Pictures/wallpaper.jpg")
os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/user/Pictures/wallpaper.jpg")
