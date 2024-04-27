import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    def calculate():
        if user_total == 21 and len(user_cards) == 2:
            print('You win.')
            cont = False
        elif computer_total == 21 and len(computer_cards) == 2:
            print('Computer wins.')
            cont = False
        elif user_total and computer_total == 21:
            print('Draw.')
            cont = False
        elif user_total and computer_total != 21:
            if user_total > 21:
                if 11 in user_cards:
                    if (user_total-10) > 21:
                        print('You went over. You lose.')
                        cont = False
            elif computer_total > 21:
                print('Computer went over. You win.')
                cont = False
            else:
                if new_card == 'y':
                    pass
                    cont = True
                else:
                    if user_total > computer_total:
                        print('You win.')
                        cont = False
                    elif user_total < computer_total:
                        print('You lose.')
                        cont = False
                    else:
                        print('Draw.')
                        cont = False

    user_cards = []
    computer_cards = []

    for n in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        user_total = sum(user_cards)
        computer_total = sum(computer_cards)
    print(f'Your cards: {user_cards}, current score: {user_total}')
    print(f"Computer's first draw: {computer_cards[0]}")
    new_card = input("Type 'y' to get another card, type 'n' to pass. ").lower()
    if new_card == 'y':
        cont = True
        calculate()
    else:
        cont = False
        print(f'Your final hand: {user_cards}, final score: {user_total}')
        print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
        calculate()

    while cont:
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        user_total = sum(user_cards)
        computer_total = sum(computer_cards)
        print(f'Your cards: {user_cards}, current score: {user_total}')
        print(f"Computer's first draw: {computer_cards[0]}")
        new_card = input("Type 'y' to get another card, type 'n' to pass. ").lower()
        if new_card == 'y':
            cont = True
            calculate()
        else:
            cont = False
            print(f'Your final hand: {user_cards}, final score: {user_total}')
            print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
            calculate()
    play_again = input("Type 'y' to play another game, type 'n' to stop. ").lower()
    if play_again == 'y':
        blackjack()
    else:
        print('Goodbye.')

play_game = input('Do you want to play a game of blackjack? ')
if play_game == 'y':
    blackjack()
else:
    print('Goodbye.
