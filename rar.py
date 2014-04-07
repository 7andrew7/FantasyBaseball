from normalize import *

import json
import subprocess
import sys

def fetch_rars():
    out = subprocess.check_output(['scrapy', 'crawl', 'fangraphs', '-o' , '-'], cwd='fangraphs')
    rars = {}

    for line in out.splitlines():
        player = json.loads(line)
        name = normalize(player['name'])
        rars[name] = player['rar']

    return rars
