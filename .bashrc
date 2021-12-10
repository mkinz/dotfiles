#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

alias v='/usr/bin/nvim'
alias vi='/usr/bin/nvim'
alias ll='ls -lrth'
alias kd='ls -larth'
alias grep='grep -i'
alias rfind='find . -print |grep'
alias ud='sudo pacman -Syyu'
alias mx='alsamixer'
alias cf='vim ~/.config/i3/config'
alias cleanup='pacman -Rsn $(pacman -Qdtq)'

# network connections
alias network='nmcli connection show'
