# Assignment Exam

### Description 

Write a TCP client-server application in Python in order to implement the game "Guess The Number".

Guess The Number is a game where the player must use your logic in order to guess a 4-digit secret number selected by the server application at the beginning of the game.

The number is formed with digits from 0 to 9; each digit appears once at most.

After connecting the client to the server, the player is asked to enter 4 digits and this number is sent to the server.

This number is guessed by the player via multiple attempts. An attempt consists of a proposed number, sent by the player trough the client application input line, and the server's reply. The server must tell the player, in his reply, how many digits has the player guessed on the same position, and how many digits has the player  guessed on a different position.

The player will be given maximum 10 attempts to guess the generated number, until he exits the application himself by typing "q" or "quit".

The randint(min,max) function from the random module can be used to generate random numbers.

Your solution can be copied in the text box below on this page or you can attach one file (if you write a joint client/server application in one file) or two separate files (client and server) as an attachment to the solution.