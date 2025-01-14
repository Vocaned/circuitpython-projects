#!/bin/bash

BOARD="CIRCUITPY"

# Check if board is mounted, mount if not
if [ ! -d "/run/media/$USER/$BOARD" ]; then
    if [ ! -e "/dev/disk/by-label/$BOARD" ]; then
        echo "Waiting for $BOARD to connect"
        while [ ! -e "/dev/disk/by-label/$BOARD" ]; do
            sleep 1
        done
    fi

    gio mount -d $(realpath "/dev/disk/by-label/$BOARD")
fi

cp "$1/main.py" "/run/media/$USER/$BOARD"
if [ -f "$1/settings.toml" ]; then
    cp "$1/settings.toml" "/run/media/$USER/$BOARD"
fi
