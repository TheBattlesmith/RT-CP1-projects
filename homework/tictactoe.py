# Roman Torres, period 1, Tic_Tac_Toe




game = True

while game == True:
    playing = True
    moves = ["\nTop Left: 1", "\nTop Center: 2", "\nTop Right: 3","\nMiddle Left: 4","\nMiddle Center: 5","\nMiddle Right: 6","\nBottom Left: 7","\nBottom Center: 8","\nBottom Right: 9"]
    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while playing == True:
        while True:
            try:
                print(*moves)
                player1 = int(input("Player 1, where would you like to move (please input a number)---\n\n "))
                
                if player1 not in available:
                    raise TypeError("---That is not an available move---")
            except:
                print("---Please answer with an integer---")
            else:
                available.remove(player1)
                break
        if player1 == 1:
            moves.remove("\nTop Left: 1")
        if player1 == 2:
            moves.remove("\nTop Center: 2")
        if player1 == 3:
            moves.remove("\nTop Right: 3")
        if player1 == 4:
            moves.remove("\nMiddle Left: 4")
        if player1 == 5:
            moves.remove("\nMiddle Center: 5")
        if player1 == 6:
            moves.remove("\nMiddle Right: 6")
        if player1 == 7:
            moves.remove("\nBottom Left: 7")
        if player1 == 8:
            moves.remove("\nBottom Center: 8")
        if player1 == 9:
            moves.remove("\nBottom Right: 9")
