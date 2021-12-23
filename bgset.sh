#!/bin/bash

echo "Choosing a random wallpaper..."
wall=$(find $HOME/Photos/wallpapers -type f | shuf -n 1)

echo "Setting up wallpaper..."
xwallpaper --zoom $wall

echo "Generating pywal color schemes..."
wal -i $wall >/dev/null
sed -i 'N;$!P;D' $HOME/.cache/wal/colors-wal-dwm.h
