#!/bin/bash

echo "Starting Arch Linux cleanup..."

# Clear pacman cache (keep only installed versions)
echo "Cleaning pacman cache..."
sudo paccache -rk0

# Vacuum journal logs older than 2 weeks
echo "Cleaning systemd journal logs..."
sudo journalctl --vacuum-time=2weeks

# Clear user cache
echo "Clearing user cache (~/.cache)..."
rm -rf ~/.cache/*

# Remove orphan packages
echo "Removing orphan packages..."
orphans=$(pacman -Qdtq)
if [ -n "$orphans" ]; then
  sudo pacman -Rns $orphans
else
  echo "No orphan packages found."
fi

echo "Cleanup complete!"
