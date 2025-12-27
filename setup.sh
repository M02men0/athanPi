#!/bin/bash
set -e

echo "=== Complete Athan Setup ==="

# Step 1: Create project structure
mkdir -p /home/$USER/athan/{audio,logs}
echo "Project directories created"

# Step 2: Make script executable (assuming files exist)
chmod +x /home/user1/athan/script.py
echo "Script made executable"[file:1]

# Step 3: Install packages
sudo apt update
sudo apt install -y mpg123
echo "Packages installed"

# Step 4: Create service file
sudo tee /etc/systemd/system/athan.service > /dev/null <<EOF
[Unit]
Description=Athan Scheduler
After=network-online.target sound.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/user1/athan/script.py
WorkingDirectory=/home/user1/athan
User=user1
Restart=always
RestartSec=5
StandardOutput=append:/home/user1/athan/logs/athan.log
StandardError=append:/home/user1/athan/logs/athan.log

[Install]
WantedBy=multi-user.target
EOF

# Step 5: Enable service
sudo systemctl daemon-reload
sudo systemctl enable athan
echo "Service created and enabled"
sudo systemctl start athan
echo "Service started"


echo "Setup complete! ✅"
echo "Enjoy!"
