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
alias cf='vim ~/.config/qtile/config.py'
alias cleaner='sudo pacman -Rsn $(pacman -Qdtq)'
alias mirror='sudo reflector --latest 5 --sort rate --country US --age 12 --protocol https --save /etc/pacman.d/mirrorlist'
alias itb='cd /home/xink/.local/share/IntoTheBreach/profile_mooncheese'
alias gl='git log --graph --oneline --decorate --all'
alias gll="git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)    <%an>%Creset%n' --abbrev-commit --date=relative --branches"



# network connections
alias network='nmcli connection show'

# configs
aw='cd ~/.config/awesome/'
awbk='cp ~/.config/awesome/rc.lui ~/.config/awesome/rc.lui.bk'

#colorscheme
(cat ~/.cache/wal/sequences &)

