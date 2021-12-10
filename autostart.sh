#!/usr/bin/env bash

# Session manager
#lxsession &

# Remap caps lock to escape.
#isetxkbmap -option caps:escape &

 # Restore background.
nitrogen --restore &

# Network Manager applet
nm-applet &

# Compositor
picom &

# Night light
#redshift -l 12.87:74.84 &
