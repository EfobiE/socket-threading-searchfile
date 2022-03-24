# Socket Communication and Multithreading with Search File Script

## Files

The files under the root directory of the projects are the following.

```
searchfile.py	The script file which searches wordlist.txt for the message accounting for the wildcard, an asterisk(*).

wordlist.txt    An alphabetically sorted list of words.

README.md	This file.

mt-server.py    Receives messages from the client, and uses searchfile.py to search wordlist.txt for the messages. The server’s thread then sends the reply to the client and closes.

mt-client.py    Gets a message from the user and starts a thread that connects to the server over the socket and sends message.
```
## Running the Program

First, run `mt-server.py` in command line. Then, run `mt-client.py` in seperate command line. Multiple instances of `mt-client.py` can be run adjacently in seperate command lines. `mt-client.py` prompts the user to enter a wildcard search query. Inputing 'quit' as the search query closes the connection to the server and terminates the `mt-client.py` program.