#!/usr/bin/env python

from rosters import *
from rar import *

from operator import itemgetter

rosters  = fetch_rosters()
rars = fetch_rars()

taken = set()
for roster in rosters.itervalues():
    taken.update(roster)

avail = [(name, rar) for name, rar in rars.iteritems() if name not in taken]
print sorted(avail, key=itemgetter(1))
