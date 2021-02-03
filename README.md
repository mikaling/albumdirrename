# albumdirrename - Album Directory Renamer

A Python script that renames a music album folder based on the metadata of the music files within it.

## Installation
Download or clone this repo  
> `git clone https://github.com/mikaling/albumdirrename.git`

Install the required dependencies  
> `pip install -r requirements.txt`

## Usage

Place the `albumdirrename.py` file at the root of the directory containing the folders to be renamed and run it with  
> `python3 albumdirrename.py`

Example folder structure: 
``` 
.
├── albumdirrename.py
├── badly-named-folder1
│   ├── song.mp3
│   └── cover.jpg
├── badly-named-folder2
│   ├── newfile4.txt
│   └── song.flac
├── badly-named-folder3
│   ├── newfile3.txt
│   └── song.mp3
└── newfile2.txt

```

Folders will be renamed to the format `[Year] - [Artist] - [Album Title]`

## Dependencies
mutagen >= 1.45.1

## Planned Features
* User can set folder format using regular expressions