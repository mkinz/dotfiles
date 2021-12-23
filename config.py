# -*- coding: utf-8 -*-
# -*- mode: python; python-indent-offset: 4 -*-
# Imports for the config
import os
import re
import subprocess
from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, Rule, KeyChord
from libqtile.lazy import lazy

# starting defaults
mod = "mod4"
terminal = "kitty"
home_dir = "/home/xink/"


keys = [
      # Define the Basic Shortcuts
      Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
      Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
      Key([mod, "control"], "s", lazy.spawn(os.path.expanduser("~/.config/qtile/logoff.sh")), desc="Shutdown/Restart"),
      Key([mod, "control"], "x", lazy.spawn("xscreensaver-command -lock"), desc="Lock Screen w/ Xscreensaver"),
      Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
      Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
      Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Fullscreen focused window"),
      Key([mod, "shift"], "q", lazy.spawn("xkill"), desc="Spawn xkill mode"),
      Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Spawn a command using a prompt widget"),

      # Basic Rofi Command Shortcuts
      Key([mod], "p", lazy.spawn("rofi -show drun -show-icons"), desc="Launch Rofi in Window mode"),

      # "Extended" Command Shortcuts
      Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
      Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
      #Key([mod, "shift"], "d", lazy.spawncmd(), desc="Spawn a custom script which launches apps with a preset configuration"),
      Key([mod, "shift"], "e", lazy.spawn("thunar"), desc="Spawn the file manager"),

      # Quick Launch Applications
      KeyChord([mod], "a", [
          Key([], "b", lazy.spawn("firefox"), desc="Web Browser"),
          Key([], "e", lazy.spawn("thunar")),
          Key([], "s", lazy.spawn("spotify")),
          Key([], "h", lazy.spawn("kitty htop")),
      ]),

      # Toggle Scratchpad visibility
      Key([mod], "s", lazy.group['scratchpad'].dropdown_toggle('terminal'), desc="Toggle Terminal Scratchpad"),

      # Application / Utility / External Hot Keys
      Key([mod], "b", lazy.hide_show_bar()),
      Key([mod], "v", lazy.spawn("gscreenshot -c -s"), desc="Take a screenshot"),

      # Focus Movement
      Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
      Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
      Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
      Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
      Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
      Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
      Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
      Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
#      Key([mod], "space", lazy.layout.next(), desc="cycle focus"),

      # Window Movement
      Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
      Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
      Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
      Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
      Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
      Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
      Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
      Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

      # Change Window Sizing and Layout Functions
      Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
      Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
      Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
      Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
      Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
      Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
      Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
      Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
      Key([mod, "control"], "i", lazy.layout.shrink(), desc="Grow window up"),
      Key([mod, "control"], "o", lazy.layout.grow(), desc="Grow window up"),
      Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
      Key([mod, "control"], "b", lazy.layout.minimize(), desc="Reset all window sizes"),
      Key([mod, "control"], "m", lazy.layout.maximize(), desc="Maximize window"),
      #Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
      Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
      Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),

      # Window Movement / Functions related to TreeTab layout
      Key([mod, "mod1"], "j", lazy.layout.move_down()),
      Key([mod, "mod1"], "k", lazy.layout.move_up()),
      Key([mod, "mod1"], "h", lazy.layout.move_left()),
      Key([mod, "mod1"], "l", lazy.layout.move_right()),
      Key([mod, "mod1"], "o", lazy.layout.expand_branch()),
      Key([mod, "mod1"], "i", lazy.layout.collapse_branch()),
      Key([mod, "mod1", "shift"], "j", lazy.layout.section_down()),
      Key([mod, "mod1", "shift"], "k", lazy.layout.section_up()),


      # Move groups
#      Key([mod, ], "Right", lazy.screen.next_group()),
#      Key([mod, ], "Left", lazy.screen.prev_group()),
      Key([mod], "space", lazy.layout.screen.next_group(), desc="Cycle to next group"),
      Key([mod, "shift"], "space", lazy.layout.screen.prev_group(), desc="Cycle to previous group"),
      

      # Multimedia Keybindings
      Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
      Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
      Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
      Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
      Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
      Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
      Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

  ]

# custom workspace names and initialization
class Groupings:

    def init_group_names(self):
        return [("", {"layout": "monadtall"}),     # Terminals
                ("", {"layout": "monadtall"}),     # Web Browser
                ("", {"layout": "monadtall"}),     # File Manager
#                ("", {"layout": "monadtall"}),     # Text Editor
#                ("", {"layout": "monadtall"}),     # Media
                ("", {"layout": "monadtall"}),     # Music/Audio
#                ("漣", {"layout": "monadtall"})
]   

 # Settings

    def init_groups(self):
        return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = Groupings().init_group_names()
    groups = Groupings().init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 3,
                "margin": 5,
                "font": "Source Code Pro Medium",
                "font_size": 10,
                "border_focus": "#bd93f9",
                "border_normal": "#555555"
                }

# window layouts
layouts = [
    layout.MonadTall(**layout_theme),
    # layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
    # layout.Stack(num_stacks=2, **layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Tile(**layout_theme),

    # Try more layouts by unleashing below layouts.
    layout.Columns(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]


# colors for the bar/widgets/panel
def init_colors():
    return [["#282a36", "#282a36"], # color 0 | bg
            ["#282a36", "#282a36"], # color 1 | bg
            ["#f8f8f2", "#f8f8f2"], # color 2 | fg
            ["#ff5555", "#ff5555"], # color 3 | red
            ["#50fa7b", "#50fa7b"], # color 4 | green
            ["#f1fa8c", "#f1fa8c"], # color 5 | yellow
            ["#bd93f9", "#bd93f9"], # color 6 | blue
            ["#ff79c6", "#ff79c6"], # color 7 | magenta
            ["#8be9fd", "#8be9fd"], # color 8 | cyan
            ["#bbbbbb", "#bbbbbb"]] # color 9 | white

def init_separator():
    return widget.Sep(
                size_percent = 60,
                margin = 1,
                linewidth = 2,
                background = colors[1],
                foreground = "#555555")

def nerd_icon(nerdfont_icon, fg_color):
    return widget.TextBox(
                font = "Iosevka Nerd Font",
                fontsize = 15,
                text = nerdfont_icon,
                foreground = fg_color,
                background = colors[1])

def init_edge_spacer():
    return widget.Spacer(
                length = 5,
                background = colors[1])


colors = init_colors()
sep = init_separator()
space = init_edge_spacer()

widget_defaults = dict(
    font='Source Code Pro Medium',
    fontsize=12,
    padding=5,
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
            ######################
            # Left Side of the bar
            ######################
            space,
            #widget.Image(
            #    filename = "/usr/share/pixmaps/archlinux-logo.png",
            #    background = colors[1],
            #    margin = 3
            #),
            widget.Image(
                filename = "~/.config/qtile/python.png",
                background = colors[1],
                margin = 3,
                mouse_callbacks = {
                    'Button3': lambda : qtile.cmd_spawn(
                        f'{terminal} -e vim {home_dir}/.config/qtile/config.py'
                    )
                }
            ),
            widget.GroupBox(
                font = "Iosevka Nerd Font",
                fontsize = 15,
                foreground = colors[2],
                background = colors[1],
                borderwidth = 4,
                highlight_method = "text",
                this_current_screen_border = colors[6],
                active = colors[4],
                inactive = colors[2]
            ),
            sep, 
            nerd_icon(
                "",
                colors[7]
            ),
            widget.CurrentLayout(
                foreground = colors[2],
                background = colors[1]
            ),
            sep,
            nerd_icon(
                "墳",
                colors[3]
            ),
            widget.Volume(
                foreground = colors[2],
                background = colors[1]
            ),
            widget.Mpris2(    
               name='spotify',    
               foreground = colors[2],    
                background = colors[1],    
               objname="org.mpris.MediaPlayer2.spotify",    
               display_metadata=['xesam:title', 'xesam:artist'],    
               scroll_chars=None,    
               stop_pause_text='',    
               **widget_defaults    
               ),
            widget.Spacer(
                length = bar.STRETCH,
                background = colors[1]
            ),
            ############
            # Center bar
            ############
            nerd_icon(
                "﬙",
                colors[3]
            ),
            widget.CPU(
                format = "{load_percent}%",
                foreground = colors[2],
                background = colors[1],
                update_interval = 2,
                mouse_callbacks = {
                    'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e htop")
                }
            ),
            nerd_icon(
                "",
                colors[4]
            ),
            widget.Memory(
                format = "{MemUsed:.0f}{mm}",
                foreground = colors[2],
                background = colors[1],
                update_interval = 2,
                mouse_callbacks = {
                    'Button1': lambda : qtile.cmd_spawn(f"{terminal} -e htop")
                }
            ),
            #######################
            # Right Side of the bar
            #######################

            widget.Spacer(
                length = bar.STRETCH,
                background = colors[1]
            ),
            nerd_icon(
                "",
                colors[4]
            ),
            widget.Net(
                format = "{down} ↓↑ {up}",
                foreground = colors[2],
                background = colors[1],
                update_interval = 2,
                mouse_callbacks = {
                    'Button1': lambda : qtile.cmd_spawn("def-nmdmenu")
                }
            ),
            sep,
            nerd_icon(
                "",
                colors[7]
            ),
            widget.Clock(
                format = '%b %d-%Y',
                foreground = colors[2],
                background = colors[1]
            ),
            nerd_icon(
                "",
                colors[8]
            ),
            widget.Clock(
                format = '%I:%M %p',
                foreground = colors[2],
                background = colors[1]
            ),
            sep,
            nerd_icon(
                "  ",
                colors[6]
            ),
            widget.Battery(
                foreground = colors[2],
                background = colors[1],
                format = "{percent:2.0%}"
            ),
            widget.Systray(
                background = colors[1]
            ),
            space
        ]
    return widgets_list


# screens/bar
def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_list(), size=35, opacity=0.9, margin=[5,10,0,10]))]

screens = init_screens()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#
# assign apps to groups/workspace
#
@hook.subscribe.client_new
def assign_app_group(client):
    d = {}

    # assign deez apps
#    d[group_names[0][0]] = ['kitty']
    d[group_names[1][0]] = ['firefox']
    d[group_names[2][0]] = ['thunar' 'nautilus']
    d[group_names[3][0]] = ['code', 'geany']
    d[group_names[4][0]] = ['vlc', 'obs', 'mpv', 'mplayer', 'lxmusic', 'gimp']
    d[group_names[5][0]] = ['spotify']
    d[group_names[6][0]] = ['lxappearance', 'gpartedbin', 'lxtask', 'lxrandr', 'arandr', 'pavucontrol', 'xfce4-settings-manager']

    wm_class = client.window.get_wm_class()[0]
    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)


main = None
@hook.subscribe.startup
def start_once():
    start_script = os.path.expanduser("~/scripts/autostart.sh")
    subprocess.call([start_script])

@hook.subscribe.startup_once
def start_always():
    # fixes the cursor
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='Viewnior'),  # Photos/Viewnior 
    Match(wm_class='Alafloat'),  # Floating Alacritty Terminal 
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], **layout_theme)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
