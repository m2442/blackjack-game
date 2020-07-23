import tkinter
import random


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("dealer wins")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("player wins")
    elif dealer_score > player_score:
        result_text.set("dealer wins")
    else:
        result_text.set("draw")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins")


#     global player_score
#     global player_ace
#     card_value = deal_card(player_card_frame)[0]
#     if card_value == 1 and not player_ace:
#         player_ace = True
#         card_value == 11
#     player_score += card_value
# #  if we would bust, check it there is an ace and subtract
#     if player_score > 21 and player_ace:
#         player_ace = False
#         player_score -= 10
#     player_score_label.set(player_score)
#     if player_score > 21:
#         result_text.set("dealer wins")
#     # print(locals())


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['king', 'queen', 'jack']
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

#     for each suit,retrieve the images for the card
    for suit in suits:
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
    if score > 21 and ace:
        score -= 10
        ace = False
    return score


def restart():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky="nw")
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, rowspan=2, sticky="ew")
    result_text.set("")
    dealer_hand = []
    player_hand = []
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def shuffle():
    random.shuffle(deck)


def play():
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
    mainWindow.mainloop()




mainWindow = tkinter.Tk()

mainWindow.title("blackjack_game")
mainWindow.geometry("640x480")
mainWindow.config(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)
card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky="nw")

player_score_label = tkinter.IntVar()
# player_score = 0
# player_ace = False
tkinter.Label(card_frame, text="player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, rowspan=2, sticky="ew")

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")
player_button = tkinter.Button(button_frame, text="player", command=deal_player)
player_button.grid(row=0, column=1)
dealer_button = tkinter.Button(button_frame, text="dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)
restart_button = tkinter.Button(button_frame, text='restart', command=restart)
restart_button.grid(row=0, column=2)
shuffle_button = tkinter.Button(button_frame, text='shuffle', command=shuffle)
shuffle_button.grid(row=0, column=3)
# load cards
cards = []
load_images(cards)
print(cards)
# create a new deck of cards and shuffle them
deck = list(cards) + list(cards)
shuffle()
# random.shuffle(deck)
# create the list to store the dealer's and players's hands
dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()
# deal_player()
# dealer_hand.append(deal_card(dealer_card_frame))
# dealer_score_label.set(score_hand(dealer_hand))
# deal_player()
# mainWindow.mainloop()
