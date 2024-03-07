#!/usr/bin/python3
"""generates a .tgz file from the contens of web_static using FABRIC"""
from fabric.api import *
import datetime
import os.path
import re

