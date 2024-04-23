from collections import Counter

FILE_PATH = "Pink_Floyd_DB.txt"


def create_data_structure():
    """
    This function creats the data structure
    :return: the data structure
    :rtype: dict
    """
    # get contents of file
    file_input = open(FILE_PATH, "r")
    contents_file = file_input.read()
    # creating list of albums
    list_albums = contents_file.split('#')
    spllited_album = []
    organized_albums = {}
    songs_stuffs = []
    for album in list_albums:
        if album != '':
            # splliting name of album and its date from the songs
            spllited_album.append(album.split('*', 1))
            # spliiting the name and the date of the album
            name_and_date = spllited_album[0][0].split('::')
            songs_stuffs.append(name_and_date[1])
            # splitting the songs
            list_of_songs = spllited_album[0][1].split('*')
            # organizing each song
            for song in list_of_songs:
                parts_of_song = song.split("::")
                songs_stuffs.append(parts_of_song)
            organized_albums[name_and_date[0]] = songs_stuffs
            songs_stuffs = []
            spllited_album = []

    return organized_albums


def get_list_albums(dict_album):
    """
    This function creates a list of albums and then makes a string out of them
    :param dict_album: data structure in which all the information is stored
    :type dict_album: dict
    :return: the list of albums as string
    :rtype: str
    """
    album_list = []
    for album in dict_album.keys():
        album_list.append(album)
    album_str = ', '.join(album_list)
    return album_str


def get_list_songs(dict_album, name_album):
    """
    This function creates a list of all the songs in the chosen album and then
    makes a string out of the list
    :param dict_album: data structure in which all the information is stored
    :type dict_album: dict
    :param name_album: the name of the chosen album
    :return: the list of all songs as string
    :rtype: str
    """
    songs_in_album = []
    for album, songs in dict_album.items():
        if album == name_album:
            # in order to not include date
            for song in songs[1:]:
                songs_in_album.append(song[0])
    str_songs_in_album = ', '.join(songs_in_album)
    return str_songs_in_album


def get_len_song(dict_album, name_song):
    """
    This function finds the length of the chosen song
    :param dict_album: data structure in which all the information is stored
    :type dict_album: dict
    :param name_song: the name of the chosen song
    :type name_song: str
    :return: the length of the chosen song
    :rtype: str
    """
    length_song = 0
    for songs in dict_album.values():
        for song in songs[1:]:
            if song[0] == name_song:
                length_song = song[2]
    if length_song == 0:
        return "There is no such song"
    return str(length_song)


def get_words_song(dict_album, name_song):
    """
    This function gets the words of the chosen song
    :param dict_album: data structure in which all the information is stored
    :type dict_album: dict
    :param name_song: the name of the chosen song
    :type name_song: str
    :return: the words of the chosen song
    :rtype: str
    """
    words_song = ""
    for songs in dict_album.values():
        for song in songs[1:]:
            if song[0] == name_song:
                words_song = song[3]
    if words_song == "":
        return "There is no such song"
    return words_song


def get_album_of_song(dict_album, name_song):
    """
    This function finds the album of the chosen song
    :param dict_album: data structure in which all the information is stored
    :type dict_album: dict
    :param name_song: the name of the chosen song
    :type name_song: str
    :return: the album of the chosen song
    :rtype: str
    """
    album_of_song = ""
    for album, songs in dict_album.items():
        for song in songs[1:]:
            if song[0] == name_song:
                album_of_song = album
    if album_of_song == "":
        return "There is no such song"
    return album_of_song


def get_songs_by_word(dict_album, word):
    """
    This function finds all the songs that includes the chosen word
    and then makes a string out of the list
    :param dict_album: data structure in which all the information is stored
    :type dict_album: dict
    :param word: the chosen word
    :type word: str
    :return: a list of all the songs that includes the word as string
    :rtype: str
    """
    songs_with_word = []
    for songs in dict_album.values():
        for song in songs[1:]:
            """
            checking if the name of the song includes
            the word without connection to size
            """
            if word.lower() in song[0].lower():
                songs_with_word.append(song[0])
    if len(songs_with_word) == 0:
        return "There is no such word in any song name"
    str_songs_with_word = ', '.join(songs_with_word)
    return str_songs_with_word


def get_songs_by_lyrics(dict_album, word):
    """
    This function finds the songs that includes the word in their lyrics
    :param dict_album: data structure in which all the information is stored
    :type dict_album: dict
    :param word: the chosen word
    :type word: str
    :return: list of all the songs that include the word in their lyrics as str
    :rtype: str
    """
    lyrics_with_word = []
    for songs in dict_album.values():
        for song in songs[1:]:
            if word.lower() in song[3].lower():
                lyrics_with_word.append(song[0])
    if len(lyrics_with_word) == 0:
        return "There is no such word in any song lyrics"
    str_lyrics_with_word = ', '.join(lyrics_with_word)
    return str_lyrics_with_word


def get_most_common_lyrics(dict_album):
    """
    This function gets the 50 most common words in the songs of pink floyed
    :param dict_album: data structure in which all the information is stored
    :type dict_album: dict
    :return: the 50 most common words in the songs of pink floyed
    """
    all_words = []
    for songs in dict_album.values():
        for song in songs[1:]:
            lyrics_list = song[3].split()
            all_words.extend(lyrics_list)
    # Pass the split_it list to instance of Counter class.
    counter = Counter(all_words)
    # most_common() produces k frequently encountered
    # input values and their respective counts.
    most_occur = counter.most_common(50)
    top_50 = "most common words are: "
    for word in most_occur:
        top_50 += word[0] + " and the amount of times: " + str(word[1]) + ", "
    # removing the , from the last common word
    top_50 = top_50[:-2]
    return top_50


def get_albums_in_order(dict_album):
    """
    This function creates a list of albums by length of the songs in them and
    then make a string out of the list
    :param dict_album: data structure in which all the information is stored
    :type dict_album: dict
    :return: list of albums by length as string
    :rtype: str
    """
    albums_length = []
    # the time format is %H:%M
    album_len = "00:00"
    for album, songs in dict_album.items():
        for song in songs[1:]:
            # checking if the hours are 2 digits and if not add 0
            if len(song[2]) < 5:
                song[2] = '0' + song[2]
            album_len = get_time(album_len + '-' + song[2])
        """
        making sure that the time format will change
        from %H:%M to %H.%M in order to sort
        """
        len_list = album_len.split(':')
        album_len = float(len_list[0] + '.' + len_list[1])
        albums_length.append((album, album_len))
        album_len = "00:00"
    # sorting by length which is the second element and from big to small
    albums_length.sort(reverse=True, key=lambda x: x[1])
    sorted_albums = "list of albums by length: "
    for album in albums_length:
        sorted_albums += album[0] + " and its length is " + \
                         str(album[1])[:2] + ':' + str(album[1])[3:] + ", "
    sorted_albums = sorted_albums[:-2]
    return sorted_albums


def get_time(time):
    """
    This function the sum of two times in format %H:%M-%H-%M
    :param time: the time that the user entered
    :return: the sum of the two times
    :rtype: str
    """
    # calculating the sum of times in hours and minutes between the two times
    fir_hours = int(time[6:8])
    sec_hours = int(time[0:2])
    fir_minutes = int(time[-2:])
    sec_minutes = int(time[3:5])
    hours = fir_hours + sec_hours
    minutes = fir_minutes + sec_minutes
    # if minutes are above 60 add to hour one and remove 60 from minutes
    if minutes > 60:
        hours = int(hours) + 1
        minutes -= 60
    # if hours or minutes do not have 2 digits add 0 at start
    if hours < 10:
        hours = '0' + str(hours)
    if minutes < 10:
        minutes = '0' + str(minutes)
    return str(hours) + ':' + str(minutes)
