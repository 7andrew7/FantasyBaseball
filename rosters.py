#!/usr/bin/env python

import getpass
import gspread

keywords = {"HITTERS", "RESERVES", "PITCHERS"}
password = getpass.getpass()

gc = gspread.login('andrew.whitaker@mac.com', password)
sh = gc.open_by_key('0AlGIrGDLUd5OdHpDSm55Y1Utd0hrQUJDN1NRRVVUTlE')

others = ['Carter', 'Dugan', 'Duke', 'Kolman', 'Nelson', 'Owsen', 'Prowell', 'Stack',
          'Valla']
me = ['Whitaker']
_all = others + me


sheets = sh.worksheets()
rosters = {} # map from player name to set of players

for player in _all:
    ws = sh.worksheet(player)
    roster = set()
    rows = ws.get_all_values()
    for row in rows[4:]:
        if 'RELEASED' in row:
            break
        name = row[1]
        if name not in keywords:
            roster.add(name)

    rosters[player] = roster

print rosters
