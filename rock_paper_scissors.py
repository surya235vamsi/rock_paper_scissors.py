import random
def play():
    user=input("'r for rock','s for scissors','p for paper'\n")
    computer=random.choice(['r','s','p'])
    if user==computer:
        return "tie"
    if winning_status(user,computer):
        return "you won !"
    return "you lost !"
def winning_status(player,k):
    if  ((player=='r' and k=='s') or (player=='s' and k=='p') or (player=='p' and k=='r')) and (player=='r' or 's' or 'p'):
        return True
print(play())
