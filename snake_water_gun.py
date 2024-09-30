import random

class SnakeWaterGunGame:
    def __init__(self):
        self.choices = ['Snake', 'Water', 'Gun']
        self.score_player = 0
        self.score_computer = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def get_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'Draw'
        elif (player_choice == 'Snake' and computer_choice == 'Water') or \
             (player_choice == 'Water' and computer_choice == 'Gun') or \
             (player_choice == 'Gun' and computer_choice == 'Snake'):
            self.score_player += 1
            return 'Player'
        else:
            self.score_computer += 1
            return 'Computer'

    def play_round(self):
        player_choice = input("Enter your choice (Snake/Water/Gun): ").capitalize()
        if player_choice not in self.choices:
            print("Invalid choice, please choose again.")
            return

        computer_choice = self.get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = self.get_winner(player_choice, computer_choice)
        if winner == 'Draw':
            print("It's a draw!")
        else:
            print(f"{winner} wins this round!")

    def display_score(self):
        print(f"\nCurrent Score:\nPlayer: {self.score_player}\nComputer: {self.score_computer}\n")

    def start_game(self):
        print("Welcome to Snake Water Gun Game!")
        rounds = int(input("Enter number of rounds to play: "))
        
        for _ in range(rounds):
            self.play_round()
            self.display_score()

        if self.score_player > self.score_computer:
            print("\nCongratulations! You won the game!")
        elif self.score_player < self.score_computer:
            print("\nComputer wins the game!")
        else:
            print("\nThe game ended in a draw.")

# Create a game instance and start
game = SnakeWaterGunGame()
game.start_game()
