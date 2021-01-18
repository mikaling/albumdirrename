# albumdirrename - Album Directory Renamer
# Renames album folders according to tags

import os, mutagen
from pathlib import Path

entries = Path('playground/')

for entry in entries.iterdir():
    if entry.is_dir():
        subdir = entries / entry.name # subdirectory name
        for file in subdir.iterdir(): # iterate through files until first audio file
            tags = mutagen.File(file) # returns an audio file type or None if not audio
            if tags is not None: # audio file found
                break
        
        year = str(tags['TDRC'][0])
        artist = tags['TPE1'][0]
        album = tags['TALB'][0]
        renamedPath = year + ' - ' + artist + ' - ' + album 
        print('original dir: ' + entry.name)
        print('renamed dir: ' + renamedPath)
        subdir.rename(entries / renamedPath)
