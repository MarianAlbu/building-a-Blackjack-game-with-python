import random
Cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
should_continue= True
while should_continue:
    Your_final_cards=[]
    Comp_final_cards=[]
    def mixedcards():
        card1=random.choice(Cards)
        card2=random.choice(Cards)
        Your_final_cards.append(card1)
        Your_final_cards.append(card2)
        print(f'Your cards:[{card1},{card2}]')
    def comp_first_hand():
        card1=random.choice(Cards)
        Comp_final_cards.append(card1)
        print(f"Computer's first card: [{card1}]")
    mixedcards()
    comp_first_hand()
    if input(f"type 'y' to get another card, type 'n' to pass: ") =='y':
        Your_final_cards.append(random.choice(Cards))
        Comp_final_cards.append(random.choice(Cards))
        print(f'Your final hand: {Your_final_cards}')
        print(f'Comp final hand: {Comp_final_cards}')
    else:
        Comp_final_cards.append(random.choice(Cards))
        print(f'Your final hand: {Your_final_cards}')
        print(f'Comp final hand: {Comp_final_cards}')
    if sum(Your_final_cards)==21:
        print('blackjack :).You Win')
    if sum(Your_final_cards)<21:
        if sum(Your_final_cards)>sum(Comp_final_cards):
            print('You Win')
        else:
            print('You Lose')
    elif sum(Your_final_cards)>21:  #Ace handling
        if '11' in Your_final_cards:    
            score=sum(Your_final_cards)-10
            if score>sum(Comp_final_cards):
                print('You Win')
            else:  
                print('You Lose')
        else:
            print('You Lose')
    else:
        print('You Lose')
    if input("Type 'y' for a new game or 'n' to stop: ")=='n':
        should_continue= False
        print('see you later')