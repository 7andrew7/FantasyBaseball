#!/usr/bin/env python

import operator

def normalize(s):
    s = s.replace('.', '')
    s = s.replace('-', '')
    s = s.replace("'", '')
    s = s.lower()
    return s.strip()
