#!/usr/bin/env bash

#set output 
xrandr --output DP-1 --primary

# reload colorschemes
wal -R

# Session manager
#lxsession &

# Remap caps lock to escape.
#isetxkbmap -option caps:escape &

 # Restore background.
nitrogen --restore &

# Network Manager applet
nm-applet &

# power manager
/usr/bin/xfce4-power-manager &

# Compositor
picom &

# Night light
redshift -l 12.87:74.84 &

