#!/bin/bash

if [ ! -f .env.installed ]; then
    cp .env.example .env.installed
fi

cp ./lib/systemd/system/dht22-python.service /lib/systemd/system/
chmod 644 /lib/systemd/system/dht22-python.service

systemctl daemon-reload
systemctl disable dht22-python.service
systemctl enable dht22-python.service
