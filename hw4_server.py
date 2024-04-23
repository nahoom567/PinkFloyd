import socket
import select
import data

RECO_DICT = {"#albo_sear_**:": 1,
             "#song_find_**:": 2,
             "#leng_song_**:": 3,
             "#word_song_**:": 4,
             "#find_albo_**:": 5,
             "#song_name_**:": 6,
             "#song_lyri_**:": 7,
             "#e_x_i_t_by**:": "#answe_8_is**",
             "#comm_words**:": 9,
             "#album_leng**:": 10}

PORT = 28
IP = "0.0.0.0"


def handle_choice(choice, par=''):
    """
    This function handles the choice of the user and extra parameter if exist
    :param choice: the choice
    :type choice: int
    :param par: the extra parameter that doesnt always exist
    :return: the response according to the user choice
    """
    dict_album = data.create_data_structure()
    if choice == 1:
        album_list = data.get_list_albums(dict_album)
        return album_list
    elif choice == 2:
        songs_in_album = data.get_list_songs(dict_album, par)
        return songs_in_album
    elif choice == 3:
        length_song = data.get_len_song(dict_album, par)
        return length_song
    elif choice == 4:
        words_song = data.get_words_song(dict_album, par)
        return words_song
    elif choice == 5:
        album_of_song = data.get_album_of_song(dict_album, par)
        return album_of_song
    elif choice == 6:
        songs_with_word = data.get_songs_by_word(dict_album, par)
        return songs_with_word
    elif choice == 7:
        lyrics_with_word = data.get_songs_by_lyrics(dict_album, par)
        return lyrics_with_word
    elif choice == 9:
        top_50 = data.get_most_common_lyrics(dict_album)
        return top_50
    else:
        sorted_albums = data.get_albums_in_order(dict_album)
        return sorted_albums


def create_server():
    """
    This function creates the server
    :return: none
    """
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_sock:
        listen_sock.bind((IP, PORT))
        # Listen for incoming connections
        listen_sock.listen()
        print("Server is up and running")
        client_sockets = []
        # in order to create multi user server
        while True:
            ready_to_read, ready_to_write, in_error = select\
                .select([listen_sock] + client_sockets, [], [])
            for current_socket in ready_to_read:
                if current_socket is listen_sock:
                    client_socket, client_address = listen_sock.accept()
                    print("New client joined!", client_address)
                    client_sockets.append(client_socket)
                    # sending welcome message to the user
                    client_socket.send("Welcome".encode())
                else:
                    try:
                        data = current_socket.recv(1024).decode()
                        print("Client sent: " + data)
                        if data != "#e_x_i_t_by**:":
                            """
                            splitting between the choice of the user and
                            the extra parameter if exist
                            """
                            data_list = data.split(',')
                            """
                            sending a message to the client according to the
                            received data
                            """
                            # taking care of the choice of the user
                            for req in RECO_DICT.keys():
                                if req == data_list[0]:
                                    choice = RECO_DICT[req]
                                    """
                                    the second to seventh requests
                                    have an extra parameter
                                    """
                                    if choice > 1 and choice < 8:
                                        res = \
                                            handle_choice(choice, data_list[1])
                                    else:
                                        res = handle_choice(choice)
                                    print("The server sent to client:", res)
                                    current_socket.send(res.encode())
                        else:
                            client_sockets.remove(current_socket)
                            current_socket.close()
                    except ConnectionResetError as e:
                        client_sockets.remove(current_socket)
                        current_socket.close()
                        print("Error: ", e)
            """
            when there are no clients left, the server asks the user
             if he/she would like the server to keep operating
            """
            if not client_sockets:
                operate = input("if you want the server to keep operating"
                                " type yes and if not type anything else: ")
                if operate != "yes":
                    break


def main():
    create_server()


if __name__ == "__main__":
    main()
