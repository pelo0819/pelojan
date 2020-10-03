# -*- coding: utf-8 -*-

import os

def run(**args):
    print("[*] In dirlister mudule.")
    files = os.listdir(".")
    return str(files)
