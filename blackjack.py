from blackjack_art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_a_card():
    draw = random.choice(cards)
    return draw


def deal(u1, count):
    for count in range(0, count):
        u1.append(draw_a_card())
    # print(f"Drew = {u1}")
    return u1


def check_blackjack(u1):
    if 11 in u1 and 10 in u1 and len(u1) == 2:
        return True
    if u1[0] == 11 and u1[1] == 11:
        u1[1] = 1
    return False


def busted(u1):
    if sum(u1) > 21 and 11 in u1:
        u1.remove(11)
        u1.append(1)
    if sum(u1) > 21:
        return True
    else:
        return False


def who_won(u1, u2):
    if sum(u1) > sum(u2):
        print(f"   You: {u1} = {sum(u1)}. You WIN!")
        print(f"Dealer: {u2} = {sum(u2)}.")
    elif sum(u2) > sum(u1):
        print(f"   You: {u1} = {sum(u1)}.")
        print(f"Dealer: {u2} = {sum(u2)}. Dealer WINS!")
    else:
        print(f"   You: {u1} = {sum(u1)}. DRAW!")
        print(f"Dealer: {u2} = {sum(u2)}. DRAW!")


def main():
    user = []
    dealer = []
    print(logo)
    user = deal(user, 2)
    dealer = deal(dealer, 2)
    user_done_drawing_cards = False

    while not user_done_drawing_cards:
        user_sum = sum(user)
        dealer_sum = sum(dealer)
        print(f"   You: {user} = {user_sum}")
        print(f"Dealer: {dealer} = {dealer_sum}")
        if check_blackjack(dealer) and check_blackjack(user):
            print("Game is a DRAW!")
            return
        elif check_blackjack(dealer):
            print("Dealer has blackjack, you LOSE!")
            return
        elif check_blackjack(user):
            print("You have blackjack, you WIN!")
            return
        user_input = input("Do you want to draw another card? yes/no: ")
        if user_input.lower() == "yes":
            user = deal(user, 1)
            user_done_drawing_cards = False
        if user_input.lower() == "no":
            user_done_drawing_cards = True
        if busted(user):
            print(f"   You: {user} = {sum(user)}. You busted. You LOSE!")
            return

    while sum(dealer) < 17:
        dealer = deal(dealer, 1)
        if busted(dealer):
            print(f"Dealer: {dealer} = {sum(dealer)} Dealer busted. You WIN!")
            return
        else:
            print()

    who_won(user, dealer)


main()
