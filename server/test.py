import board
import actions
import elements
import player
import user

##TEST CASE##

#INIT USERS
users = []
users.append(user.User("Miguel", "1234", "0", "0"))
users.append(user.User("Lucas", "1234", "0", "0"))
users.append(user.User("Carmona", "1234", "0", "0"))

#USERS JOIN PLAYER
players = []
for us in users:
    players.append(player.Player(us))


#SERVER INIT GAME
board = board.Board(3)

turn = 0
