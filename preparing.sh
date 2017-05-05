#!/bin/bash
# Bash script for preparation for work

# Created by Matz Chromatiq
# https://github.com/BORN2LOSE

# Project Hawk X
# See more https://github.com/Hawk-X


################## Check you'r chmod skill ######################

if [[ $EUID -ne 0 ]]; then
        echo -e "\e[1;31mYou don't have admin privilegies, execute the script as root.""\e[0m"""
        exit 1
fi

##################################### < CONFIGURATION  > #####################################

WORK_DIR=`pwd`
version=0.1
author="Matz Chromatiq"
gitlink="https://github.com/Hawk-X/"

#Colors
white="\033[1;37m"
grey="\033[0;37m"
green="\033[1;32m"
Fiuscha="\033[0;35m"

##################################### < END OF CONFIGURATION SECTION > #####################################




############################################## < START > ##############################################

echo ""
		   sleep 0.01 && echo -e "$grey "
           sleep 0.01 && echo -e "         ██╗  ██╗ █████╗ ██╗    ██╗██╗  ██╗██╗  ██╗    "
           sleep 0.01 && echo -e "         ██║  ██║██╔══██╗██║    ██║██║ ██╔╝╚██╗██╔╝    "
           sleep 0.01 && echo -e "         ███████║███████║██║ █╗ ██║█████╔╝  ╚███╔╝     "
           sleep 0.01 && echo -e "         ██╔══██║██╔══██║██║███╗██║██╔═██╗  ██╔██╗     "
           sleep 0.01 && echo -e "         ██║  ██║██║  ██║╚███╔███╔╝██║  ██╗██╔╝ ██╗    "
           sleep 0.01 && echo -e "         ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝ "

	echo""
	sleep 0.1
	echo -e $green"  	  Hawk X "$white"version "$version" "$yellow"by"$white" $author"
	sleep 0.1
	echo -e $green "	    Page:"$Fiuscha" $gitlink "$transparent
	sleep 0.1
	tput civis
	echo ""
	tput cnorm
	sleep 0.1


get_term() {
    # If function was run, stop here.
    ((term_run == 1)) && return

    # Workaround for macOS systems that
    # don't support the block below.
    case "$TERM_PROGRAM" in
        "iTerm.app") term="iTerm2" ;;
        "Terminal.app") term="Apple Terminal" ;;
        "Hyper") term="HyperTerm" ;;
        *) term="${TERM_PROGRAM/\.app}" ;;
    esac

    # Check $PPID for terminal emulator.
    while [[ -z "$term" ]]; do
        parent="$(get_ppid "$parent")"
        name="$(get_process_name "$parent")"

        case "${name// }" in
            "${SHELL/*\/}" | *"sh" | "tmux"* | "screen" | "su"*) ;;
            "login"* | *"Login"* | "init" | "(init)") term="$(tty)" ;;
            "ruby" | "1" | "systemd" | "sshd"* | "python"* | "USER"*"PID"*) break ;;
            "gnome-terminal-") term="gnome-terminal" ;;
            *) term="${name##*/}" ;;
        esac
    done

    # Log that the function was run.
    term_run=1
}

# Hollywood scenes
if [[ $WORK_DIR ]]; then
    chmod u+x remove.py
    python remove.py
    echo -e $white"Remove repositories..."
    sleep 0.3
    pip install -r requirements.txt
    echo -e $white"Installing..."
    exit 1
else
    echo -e $Fiuscha "Please, change the working directory to hawk"
    exit 0
fi
