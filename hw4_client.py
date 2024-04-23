import socket

PROT_DICT = {"#albo_sear_**:": 1, "#song_find_**:": 2, "#leng_song_**:": 3,
             "#word_song_**:": 4, "#find_albo_**:": 5, "#song_name_**:": 6,
             "#song_lyri_**:": 7, "#e_x_i_t_by**:": 8, "#comm_words**:": 9,
             "#album_leng**:": 10}
SERVER_IP = "127.0.0.1"
PORT = 28


def get_choice():
    """
    This function gets the choice from the user and returns the request with
    an extra paremeter if needed
    according to customer choice
    :return: request according to customer choice and extra paremeter if needed
    :rtype: str
    """
    # getting the choice from the user
    choice = 0
    while not 1 <= choice <= 10:
        try:
            choice = int(input(("Choose option:\n1 - get list of albums\n"
                                "2 - get list of songs in album\n"
                                "3 - get length of song\n"
                                "4 - get lyrics of song\n"
                                "5 - get album of song\n"
                                "6 - get song by name\n"
                                "7 - get song by lyrics\n8 - exit\n"
                                "9 - get 50 most common words\n"
                                "10 - get list of albums by length\n")))
            if not 1 <= choice <= 10:
                print("try again")
        except ValueError as e:
            print("You didn't enter a number", e)
            print("try again")

    # getting the message to the server according to the choice
    for req, choose in PROT_DICT.items():
        if choice == choose:
            right_request = req
    # getting from the user another parament if needed
    if choice == 2:
        name_album = input("Enter name of album: ")
        return right_request + ',' + name_album
    elif choice == 3 or choice == 4 or choice == 5:
        name_song = input("enter name of song: ")
        return right_request + ',' + name_song
    elif choice == 6 or choice == 7:
        word = input("Enter word: ")
        return right_request + ',' + word
    else:
        return right_request


def create_client():
    """
    This function creates the client
    :return: none
    """
    req = ""
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
        my_socket.connect((SERVER_IP, PORT))
        try:
            while req != "#e_x_i_t_by**:":
                data = my_socket.recv(1024).decode()
                print("The server sent " + data)
                if req != "#e_x_i_t_by**:":
                    # sending the message to the server according to the choice
                    req = get_choice()
                    print("request is", req)
                    my_socket.send(req.encode())
        except ConnectionResetError as e:
            print("Error: ", e)


def main():
    create_client()


if __name__ == "__main__":
    main()
