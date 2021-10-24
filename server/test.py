import board
import actions
import elements
import player
import user
from actions import BuyType as BuyType

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

board = board.Board(players, 3)



while not board.gameOver:
    player = board.nexRound()
    endFlag = False
    name = player.user.nickname

    print(name, " rolled ", actions.diceRoll(board))


    while not endFlag:
        st = input(name +"'s turn: ")

        inst = st.split(" ")
        fun = inst[0]
        comp = inst[1]
        extra = inst[2]

        if fun == "BUY":
            if comp == "SETTLEMENT":
                try:
                    bType = BuyType.SETTLEMENT
                    c = extra.split(',')
                    print(c)
                    coord = elements.Vertex(int(c[0]), int(c[1]), int(c[2]))

                except:
                    print("Wrong input")
                    break


            elif comp == "CITY":
                try :
                    bType = BuyType.CITY
                    c = extra.split(',')
                    coord = elements.Vertex(int(c[0]), int(c[1]), int(c[2]))
                except:
                    print("Wrong input")
                    break


            elif comp == "ROAD":
                try:
                    bType = BuyType.ROAD
                    c = extra.split('/')
                    c0 = c[0].split(',')
                    c1 = c[1].split(',')
                    coord = [elements.Vertex(int(c0[0]), int(c0[1]), int(c0[2])), elements.Vertex(int(c1[0]), int(c1[1]), int(c1[2]))]


                except:
                    print("Wrong input")
                    break

            elif comp == "SPECIALCARD":
                bType = BuyType.SPECIALCARD
            else:
                print("UNRECOGNIZED COMP")

            #COMMON BUY
            succ = actions.buy(board, player, bType, coord)

            if succ:
                print("Successful bought a ", comp)

            else:
                print("Not enough funds")




        elif fun == "TRADE":
            pass

        elif fun == "SPECIAL":
            pass

        elif fun == "END":
            endFlag = True

        else:
            print("UNRECOGNIZED COMMAND")
