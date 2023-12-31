import json
import re

class Track:
    def __init__(self):
        self.id = None
        self.songName = None
        self.artistName = None
        self.yearReleased = None
        self.countryReleased = None
        self.imageCoverLink = None
        self.youtubeLink = None
        self.serializedStyles = None
        self.serializedGenre = None

    def extractData(self, track):
        self.id = track.id
        songText = track.title
        artistName = track.artists[0].name
        match = re.search(r'\s*-\s*(.+)$', songText)
        if match:
            self.songName = match.group(1)
        else:
            self.songName = songText

        self.artistName = artistName
        self.yearReleased = track.year if track.year != 0 else 2000
        self.countryReleased = track.country
        self.imageCoverLink = track.data['cover_image']
        self.youtubeLink = self.getYouTubeLink(track)
        styles = track.data['style']
        genre = track.data['genre']
        self.serializedStyles = json.dumps(styles)
        self.serializedGenre = json.dumps(genre)

    def getYouTubeLink(self, track):
        for vid in track.videos:
            if self.songName in vid.data['title']:
                return vid.data['uri']
        return None

    def getData(self):
        return {
            'id' : self.id,
            'songName' : self.songName,
            'artist' : self.artistName,
            'genre' : self.serializedGenre,
            'year' : self.yearReleased,
            'styles' : self.serializedStyles,
            'country' : self.countryReleased,
            'albumCover' : self.imageCoverLink,
            'youtubeLink' : self.youtubeLink
        }