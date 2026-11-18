import random






def computer_choice():
    c_choice=random.randint(1,3)
    if c_choice==(1):
        c_choice=="Rock"
    elif c_choice==(2):
        c_choice=="Paper"
    else:
        c_choice=="Scissors"

def user_choice():
    u_choice=int(input("Choose 1 for Rock, 2 for Paper, 3 for Scissors"))
    if u_choice==(1):
        return "Rock"
    elif u_choice==(2):
        return "Paper"
    else:
        return "Scissors"

def winner(c,u):
    if c==u:
        print("Tie")
    elif (c=="Rock" and u =="Paper") or (c=="Paper" and u=="Scissors") or (c=="Scissors" and u=="Rock"):
        print("You win!")
    else:
        print("Computer Wins!")






    def main():
        c_choice=computer_choice()
        u_choice=user_choice()
        winner=determine_winner(c_choice,u_choice)
        results(winner)
main()