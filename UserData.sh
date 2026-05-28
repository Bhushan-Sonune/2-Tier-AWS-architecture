#!/bin/bash

dnf update -y
dnf install nginx python3-pip -y

systemctl enable nginx
systemctl start nginx

pip3 install boto3

echo "<h1>Production Web App</h1>" > /usr/share/nginx/html/index.html