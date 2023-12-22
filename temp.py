DICT_WITH_SONG: dict = {
    "one_album": {
        "one_song": "la-la",
        "two_song": "uhu-uhu"
    }
}

album: dict = DICT_WITH_SONG["one_album"]

for song in album.values():
    
    
    print(song)

