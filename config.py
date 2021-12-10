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
      Key([mod], "d", lazy.spawn("rofi -show drun -icons run"), desc="Launch Rofi in Window mode"),

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
      Key([mod], "s", lazy.group['scratchpad'].dropdown_toggle('term'), desc="Toggle Terminal Scratchpad"),

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
      Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

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
      Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
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

      # Multimedia Keybindings
      Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
      Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
      Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
      Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
      Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
      Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
      Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

  ]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

group_labels = [
    "  ",
    "  ",
    "  ",
    "  ",
    "  "
]
group_names = ["1", "2", "3", "4", "5"]

group_layouts = [
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "floating"
]

group_matches = [
    None,
    #[Match(wm_class=["kitty"])],
    None,
    [Match(wm_class=["firefox"])],
    [Match(wm_class=["thunar"])],
    [Match(wm_class=["Spotify"])],
]

group_exclusives = [
    False, False, False,
    False, False
]

group_persists = [
    True, True, True,
    True, True
]

group_inits = [
    True, True, True,
    True, True
]

groups = []

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            matches=group_matches[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
            exclusive=group_exclusives[i],
            init=group_inits[i],
            persist=group_persists[i]
        ))

for i in groups:     
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], i.name, lazy.window.togroup(i.name))) # Send window to another group

groups.append( ScratchPad("scratchpad", [
    DropDown("term", "kitty", opacity=0.8)
    ]))

layout_theme = {
        "border_width": 2,
        "margin": 10,
        "border_focus": "a94df9",
        "border_normal": "888888"
        }

floating_theme = {
        "border_width": 2,
        "border_focus": "c44332",
        "border_normal": "888888"
        }

treetab_theme = {
        "bg_color": "131313",
        "inactive_bg": "212121",
        "inactive_fg": "bdbdbd",
        "active_bg": "333333",
        "active_fg": "a94df9",
        "font": "System San Francisco Display 13",
        "fontsize": 12,
        "sections": ['Workspace'],
        "section_fontsize": 14,
        "panel_width": 210
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme,border_focus_stack='#d75f5f'),
    layout.TreeTab(**treetab_theme),
    layout.Floating(**floating_theme)
]

# colors for panel theming
colors = [["#131313", "#131313"], # panel background
    ["#333333", "#333333"], # background for current selected group
    ["#a94df9", "#a94df9"], # font color for selected group active 
    ["#9f9f9f", "#a94df9"], # border line color for current tab
    ["#333333", "#333333"], # border line color for 'other tabs' and color for 'odd widgets'
    ["#555555", "#555555"], # color for the 'even widgets'
    ["#a94df9", "#a94df9"], # window name and line color
    ["#bdbdbd", "#bdbdbd"]] # font color for non-selected groups

# Default Widget settings
widget_defaults = dict(
    font='System San Francisco Display 13',
    fontsize=16,
    padding=3,
    backround=colors[2]
)
extension_defaults = widget_defaults.copy()

# Widget Definitions and Settings
def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[2],
            background = colors[0]
            ),
        widget.GroupBox (
            font = "System San Francisco Display 13",
            fontsize = 16,
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 3,
            borderwidth = 2,
            active = colors[2],
            inactive = colors [7],
            rounded = False,
            highlight_color = colors [1],
            highlight_method = "line",
            this_current_screen_border = colors[6],
            this_screen_border = colors [4],
            foreground = colors[2],
            background = colors[0]
            ),
        widget.Sep(
            linewidth = 0,
            padding = 5,
            foreground = colors[2],
            background = colors[0]
            ),
        widget.Prompt(
            foreground = colors[6],
            background = colors[0],
            # prompt = "Run Command: "
            ),
        widget.WindowName(
            foreground = colors[6],
            background = colors[0],
            padding = 0
            ),
        widget.Sep (
            linewidth = 0,
            padding = 6,
            foreground = colors[0],
            background = colors[0]
            ),
        widget.Mpris2(
                    name='spotify',
                    foreground = colors[2],
                    background = colors[4],
                    objname="org.mpris.MediaPlayer2.spotify",
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_chars=None,
                    stop_pause_text='',
                    **widget_defaults
                ),
        #widget.TextBox (
         #   text= '',
          #  foreground = colors[0],
           # background = colors[4],
            #padding = 0,
           # fontsize = 26
            #),
        widget.Sep (
            linewidth = 0,
            padding = 6,
            foreground = colors[4],
            background = colors[0],
            ),
        widget.TextBox(
            text = '',
            foreground = colors[2],
            background = colors[0]
            ),
        widget.Volume (
            background = colors[0],
            foreground = colors[2],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')}
            ), 
        widget.Sep (
            linewidth = 0,
            padding = 6,
            foreground = colors[4],
            background = colors[0],
            ),
        widget.TextBox (
            text = "  ",
            foreground = colors[2],
            background = colors[0],
            padding = 0,
            fontsize = 14
            ),
        widget.Memory(
            foreground = colors[2],
            background = colors[0],
            #format = '{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}'
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('kitty htop')},
            padding = 5
            ),
        widget.Sep (
            linewidth = 0,
            padding = 6,
            foreground = colors[4],
            background = colors[0],
            ),
        widget.CPUGraph(
            foreground = colors[2],
            background = colors[0],
            ),
        widget.Sep (
            linewidth = 0,
            padding = 6,
            foreground = colors[4],
            background = colors[0],
            ),
        widget.ThermalSensor(
            foreground = colors[2],
            background = colors[0],
            ),
        #widget.NetGraph ( # requires python-psutil package
        #    interface = "wlp3s0",
        #    foreground = colors[4],
        #    #format = '{down} ﬕ {up} ',
        #    format = '{down}d,  {up}u ',
        #    background = colors[0],
        #    padding = 1,
        #    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('nm-connection-editor')}
        #    ),
        widget.Sep (
            linewidth = 0,
            padding = 6,
            foreground = colors[4],
            background = colors[0],
            ),
        widget.Clock (                                                   
            foreground = colors[2],
            background = colors[0],
            format = "%Y-%m-%d %H:%M"
            ),  
        widget.Sep (
            linewidth = 0,
            padding = 6,
            foreground = colors[4],
            background = colors[0],
            ),
        widget.Systray(
                background = colors[0],
                padding = 0
            ),
        widget.Sep (
            linewidth = 0,
            padding = 6,
            foreground = colors[4],
            background = colors[0],
            ),
        widget.BatteryIcon(
            foreground = colors[0],
            background = colors[0],
            ),
        widget.Sep (
            linewidth = 0,
            padding = 6,
            foreground = colors[4],
            background = colors[0],
            ),
        widget.CurrentLayoutIcon (
            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground = colors[4],
            background = colors[0],
            padding = 5
            ),
        widget.Sep (
            linewidth = 0,
            padding = 6,
            foreground = colors[4],
            background = colors[0],
            ),
        ]
    return widgets_list

# Initialize Screens and Widgets
screens = [
    Screen(
        top=bar.Bar(widgets=init_widgets_list(), opacity=1.0, size=20)
    )
]
