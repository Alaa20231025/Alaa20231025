def subtract_a_square():
    # The rule of the game
    print("Welcome to subtract a square game\n")
    print("The Game consists of two players. The players should define the number of piles.") 
    print("The players should enter an integer non-zero square number like (1, 4, ....) less than the number of piles")
    print("Subtract the number the players enter from the number of piles. The last player to take a number and reminder=0 wins\n")
    try:
        number_of_piles = int(input("Please, enter an integer number of piles to start the game: "))
        print(f"The number of piles = {number_of_piles}")
        a = number_of_piles

        # Starting the game
        while a > 0:
            # Player 1
            number1 = int(input("Player1\nEnter your number: "))
            square1 = int(number1 ** 0.5)

            # Checking if the input of the user follows the rules of the game or not
            while number1 > a or number1 <= 0 or square1 ** 2 != number1:
                print(f"Please, enter an integer non-zero square number less than {a}")
                number1 = int(input("Player1\nEnter your number: "))
                square1 = int(number1 ** 0.5)

            a -= number1
            print(f"The reminder is: {a}")
            if a == 0:
                print("Congratulations. Player1 is the winner")
                break

            # Player 2
            number2 = int(input("Player2\nEnter your number: "))
            square2 = int(number2 ** 0.5)

            # Checking if the input of the user follows the rules of the game or not
            while number2 > a or number2 <= 0 or square2 ** 2 != number2:
                print(f"Please, enter an integer non-zero square number less than {a}")
                number2 = int(input("Player2\nEnter your number: "))
                square2 = int(number2 ** 0.5)

            a -= number2
            print(f"The reminder is: {a}")
            if a == 0:
                print("Congratulations. Player2 is the winner")
                break
    except ValueError:
            print("Invalid input Please enter a valid ")


# Ask the user if they want to play again or not
def playing_again():
    while True:
        try:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                subtract_a_square()
            elif play_again == "no":
                print("Thank you. I hope you enjoyed playing.")
                break
            else:
               print("Invalid input. Please enter 'yes' or 'no'.")
        except ValueError:
            print("Invalid input Please enter a valid input")


# Start the game
subtract_a_square()

# Ask if the user wants to play again
playing_again()
