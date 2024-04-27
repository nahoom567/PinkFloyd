# PinkFloyd
Pink Floyd was a British rock band that operated from the late 1960s to the mid-1990s. It is considered one of the most influential and successful bands in the history of popular music, and one of the only ones from the progressive rock genre that has gained popularity among the general public as well.

This is a relatively small and old project that does not showcase my current skills and knowledge in python, however it is pretty simple to understand and use.
The problem with uploading most of my other python projects is that they are individualy small projects that focuses on different part of cyber, including cryptography, reversing, scripting, expoits, web and so much more.

This project includes a server and client:

### Description of the server side - server.py

The purpose of the server is to provide information about the band Pink Floyd. The information includes all the albums, the songs, the length of each song, and the lyrics of all the songs.
The server works against a database saved in the file Pink_Floyd_DB.txt
After connecting to it, the server will send a short Welcome message to the client and wait for the client's choice of command.
The server will respond to the client according to his request and then wait for another command, until a disconnection message is sent by the client.

### Description of the client side - client.py

The client will connect to the server based on an address and port that will be kept constant in the code.
After a successful login, the client will present the user with a menu of all available commands.
After selecting the command and entering the information, the client will create the appropriate message and send to the server.
After the server responds, the client will display the response returned from the server to the user.
It will then display the command menu again and wait for another command from the user.


# Features
| Command                    | Description                                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------- |
| List of albums             | The user receives the list of albums.                                                        |
| List of songs on the album | The user taps the name of an album and gets a list of all the songs in that album.             |
| Getting the length of a song | The user taps a song name and gets its length.                                              |
| Getting lyrics to a song   | The user taps a song name and gets all the lyrics.                                             |
| What album is the song on? | The user taps a song name and gets its album.                                                  |
| Search song by name        | The user types a word and gets the names of all the songs that include that word.               |
| Search a song by lyrics in a song | The user types a word and gets the names of all the songs that include that word in the lyrics. |

another important feature is that multiple users can connect at the same time
