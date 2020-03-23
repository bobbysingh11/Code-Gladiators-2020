''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
    num_test_cases=int(input())

    for i in range(num_test_cases):
        num_team_members=int(input())

        text_input_Players=input()
        text_input_Opponent=input()

        Players=[]
        Opponents=[]

        for item in text_input_Players.split():
            Players.append(int(item))

        for item in text_input_Opponent.split():
            Opponents.append(int(item))

        win_count=0


    # To fight in an optimal manner, player power should be
    # strictly higher to win the fight, but the difference with
    # the opponent power should be minimum to avoid wastage
    # as that battle power could be used elsewhere. 

    # So we basically use a greedy algorithm, and match the 
    # smallest possible value greater than the opponents value.
    # We use a flag 0 to see if that value is available

        Opponents.sort()
        Players.sort()


        for item in Opponents:
            minimum_number=0
            for idx in range(len(Players)):

            # first check if player can defeat opponent
                if Players[idx]>item:

                # check if minimum_number is initialized
                    if minimum_number==0:
                        minimum_number=Players[idx]

                # Then check if we find smaller minimum_number
                    elif Players[idx]<minimum_number:
                        minimum_number=Players[idx]
                else:
                    pass

            if(minimum_number!=0):
                Players.remove(minimum_number)
                win_count+=1

        print(win_count)

           
main()