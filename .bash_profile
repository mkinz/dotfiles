#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
  exec startx
fi

PATH="$PATH:/$HOME/.local/bin"	
PATH="$PATH:/$HOME/.local/bin/i3cmds"
PATH="$PATH:/$HOME/.local/bin/statusbar"
