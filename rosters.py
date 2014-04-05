#!/usr/bin/env python

import getpass
import gspread

from normalize import *

KEYWORDS = {"HITTERS", "RESERVES", "PITCHERS"}
OTHERS = ['Carter', 'Dugan', 'Duke', 'Kolman', 'Nelson', 'Owsen', 'Prowell', 'Stack', 'Valla']
ME = ['Whitaker']
ALL = OTHERS + ME


def fetch_rosters(username='andrew.whitaker@mac.com', password=None):
    if not password:
        password = getpass.getpass()
    gc = gspread.login(username, password)
    sh = gc.open_by_key('0AlGIrGDLUd5OdHpDSm55Y1Utd0hrQUJDN1NRRVVUTlE')

    sheets = sh.worksheets()
    rosters = {} # map from player name to set of players

    for player in ALL:
        ws = sh.worksheet(player)
        roster = set()
        rows = ws.get_all_values()
        for row in rows[4:]:
            if 'RELEASED' in row:
                break
            name = row[1]
            if name not in KEYWORDS:
                roster.add(normalize(name))

        rosters[player] = roster

    return rosters

if __name__ == '__main__':
    rosters = fetch_rosters()
    print rosters['Whitaker']
