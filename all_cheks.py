#!/usr/bin/env python 3
import os

def check_reboot():
    """ Returns True if the computer has a pending reboot."""
    return os.path.exists("run/reboot-required")

def main():
    pass

main()