import random
import function_lib as function_lib
import superbowllistbobby as funny
time_out = 1
line_of_scrim = 50
distance = line_of_scrim - line_of_scrim
clock = 120
qb_random = random.randint(0, 4)
funny_random = random.randint(0, 2)
random_num_pass = random.randint(0, 5)
random_num_run = random.randint(8, 10)
current_down = 1
total_yards = 0
double_pass = 0
double_run = 0
double_run_fumble = 0
random_num_kick = random.randint(0, 1)
qb_calls =  ["Quarterback audibles at the the line: 'blue 80 on three, blue 80… blue 80… hut hut hut.'", "Quarterback barks: 'Red 80! Red 80! Hut! Hut! Hut!'", "Quarterback: 'Green 18...Green 18….. set-hut!'", "Quarterback: play call '319…319… hut!'", "Quarterback: Ready…..  set hut!"]
nfl_teams = ["Falcons", "Bills", "Packers", "Chiefs",
             "Steelers", "Saints", "Giants", "Eagles", "49ers"]

function_lib.blank_line()
print("WELCOME TO THE NFL SUPERBOWL TERMINAL GAME")
function_lib.blank_line()
function_lib.star_line()
your_team = (input(f"Pick a team from the list {nfl_teams} : ")).title()
function_lib.star_line()
print(f"""
Over the past twenty years the New England Patriots have dominated the NFL 
landscape by participating in 9 Super Bowls and winning six. Every new season 
teams try to emulate them by getting players to take less money while building 
a talented roster to have a chance at winning the Super Bowl. This year the {your_team} 
have succeeded at making the Super Bowl and is 2:00 minutes away from dethroning the mighty 
New England Patriots and winning a Super Bowl. Down by two points the odds 
are currently stacked against the {your_team} with the ball at the 50 yard line. 
You have to drive the ball down field and score to win the game. Should you succeed the {your_team} 
will become Super Bowl Champions.
""")
function_lib.star_line()
function_lib.blank_line()
function_lib.rules()
print("If you reach the 0 yard line,", your_team, "wins the game, else the", your_team, "lose.")
function_lib.blank_line()
function_lib.star_line()
function_lib.blank_line()
print(your_team, "are at the", line_of_scrim, "Yard Line")

#******(BELOW) WHILE LOOP TO RUN THE GAME (BELOW)******#
while line_of_scrim > 0:
    function_lib.blank_line()
    move_clock = 0
    function_lib.star_line()
#******(ABOVE) WHILE LOOP TO RUN THE GAME (ABOVE)******#

#******(BELOW) USER INPUT FOR PLAY CALL (BELOW)******#
#TIMEOUT AND KICK OPTION
    if current_down == 4 and clock < 10 and line_of_scrim <= 25 and time_out == 1: 
        user_input = int(input("Choose a play coach! 1.Pass 2.Run 3.Kick 4.Timeout: "))
        function_lib.star_line() 
#TIMEOUT OPTION IF USER IS ON 4TH DOWN OR CLOCK IS UNDER 10 SECONDS
    elif current_down == 4 and time_out == 1: 
        user_input = int(input("Choose a play coach! 1.Pass 2.Run 4.Timeout: "))
        function_lib.star_line() 
    elif line_of_scrim > 25:
        user_input = int(input("Choose a play coach! 1.Pass 2.Run: "))
        function_lib.star_line()        
#KICK OPTION APPEARS IF LINE OF SCRIMMAGE IS LESS THAT THE 25 YARD LINE
    elif line_of_scrim <= 25 and current_down < 3: 
        user_input = int(input("Choose a play coach! 1.Pass 2.Run 3.Kick: "))
        function_lib.star_line()
#******(ABOVE) USER INPUT FOR PLAY CALL (ABOVE)******#

#******(BELOW) CODING THE PLAY IN ACTION (BELOW)******#

#PASS PLAY
    if user_input == 1:
        line_of_scrim -= random_num_pass
        move_clock = abs(random_num_pass) + 10
        function_lib.blank_line()
        print(qb_calls[qb_random])
        function_lib.blank_line() 
        print("Quarter Back passed the football")
        if random_num_pass > 0:
            print("Pass complete: for", random_num_pass, "yard(s) at the", line_of_scrim, "yard Line.")
        if random_num_pass == 0:
            print("Incomplete pass.")
        if random_num_pass < 0:
            print("Quarter Back was sacked")
            print("and loss", abs(random_num_pass), "yards.")
            print(funny.qb_sack[funny_random])
#PASS PLAY

#RUN PLAY
    if user_input == 2:
        line_of_scrim -= random_num_run
        move_clock = random_num_run + 4
        function_lib.blank_line()
        print(qb_calls[qb_random])
        function_lib.blank_line()
        print("Running back ran the football")
        if random_num_run > 0:
            print("and ran for", random_num_run, "yards to the", line_of_scrim, "yard Line.")
        if random_num_run == 0:
            print("No gain.")
        if random_num_run < 0:
            print("and was tackled behind the line")
            print("and loss", abs(random_num_run), "yards.")
#RUN PLAY

#KICK FIELD GOAL (ONLY AVAILABLE IF USER REACHES 25 YARD LINE)
#IF USER IS LESS THAN 15 YARD LINE, KICK WILL ALWAYS BE SUCCESSFUL)
    if line_of_scrim < 15:
        random_num_kick = 1  

#ELSE KICK SUCESS WILL BE RANDOMIZED 
    elif line_of_scrim > 15:
        random_num_kick = random.randint(0, 1)
    if user_input == 3:
        function_lib.blank_line()
        print("Kicker kicked the football")
        if random_num_kick == 0:
            print("and scored,", your_team, "win!")
            function_lib.status(1)
            break 
        if random_num_kick == 1:
            print("and missed,", your_team, "lose.")
            function_lib.status(2)
            break

#KICK FIELD GOAL (ONLY AVAILABLE IF USER REACHES 25 YARD LINE)
#******(ABOVE) CODING THE PLAY IN ACTION (ABOVE)******#
    qb_random = random.randint(0, 4)
    clock -= move_clock

    if user_input == 1:
        total_yards = total_yards + random_num_pass
        double_pass += 1
    elif user_input == 2:
        total_yards = total_yards + random_num_run

#Game getting more difficult as user gets closer to the goal line
#PASS GETS HARDER
    if line_of_scrim > 40:
        random_num_pass = random.randint(8, 15)
    elif line_of_scrim > 30 and line_of_scrim < 40:
        random_num_pass = random.randint(1, 10)
    elif line_of_scrim > 25 and line_of_scrim < 30:
        random_num_pass = random.randint(-5, 7)
    elif line_of_scrim > 20 and line_of_scrim < 25:
        random_num_pass = random.randint(-7, 5)
    elif line_of_scrim > 16 and line_of_scrim < 20:
        random_num_pass = random.randint(-10, 1)

#RUN GETS HARDER   
    elif line_of_scrim > 40:
        random_num_run = random.randint(4, 8)
    elif line_of_scrim > 30 and line_of_scrim < 40:
        random_num_run = random.randint(1, 5)
    elif line_of_scrim > 25 and line_of_scrim < 30:
        random_num_run = random.randint(-3, 3)
    elif line_of_scrim > 20 and line_of_scrim < 25:
        random_num_run = random.randint(-7, 2)
    elif line_of_scrim > 16 and line_of_scrim < 20:
        random_num_run = random.randint(-1, 5)

#Game getting more difficult as user gets closer to the goal line
    if double_pass == 3:
        # random.randint(-5, 1)
        random_num_pass = random.randint(-5, 1)
        double_pass = 0
    # if double_pass == 4:
    #     print("Interception, game over.", your_team, "lose.")
    #     function_lib.status(2)
    #     break
   
    if user_input == 2:
        double_run_fumble += 1
        double_run += 1
 
    if user_input == 2 and double_run_fumble == 4:
        print("Fumble, game over.", your_team, "lose.")
        function_lib.status(2)
        break

    if line_of_scrim > 20 and double_run == 3:
        random_num_run = random.randint(-3, 0)
        double_run = 0

    else:
        # random.randint(-2, 10)
        random_num_run = random.randint(-4, 10) 
    
    current_down += 1
    if total_yards >= 10:
        current_down = 1

#TIMEOUT RESTORES A DOWN OR ADDS 10 SECONDS TO THE CLOCK
    if user_input == 4 and current_down > 3 and time_out > 0 and clock > 5:
        current_down -= 2
        time_out -= 1
    elif user_input == 4 and clock < 5 and time_out > 0 and current_down < 4:
        clock += 10
        time_out -= 1

#TIMEOUT RESTORES A DOWN OR ADDS 10 SECONDS TO THE CLOCK
    if line_of_scrim >= 0 and clock > 0 and current_down < 5:   
        function_lib.simple_line()
        function_lib.blank_line()
        if total_yards >= 10:
            print(funny.first_down[funny_random])
        elif current_down == 2:
            print(funny.second_down[funny_random])
        elif current_down == 3:
            print(funny.third_down[funny_random])
        elif current_down == 4:
            print(funny.fourth_down[funny_random])
        print(your_team,"are at the", line_of_scrim, "Yard Line")
        # print("Current Down:", current_down) 
        print("Game Clock:", clock, "Seconds")

    if total_yards >= 10:
        total_yards = 0    

    if total_yards > 0 and clock >= 0 and current_down < 5 and line_of_scrim > 0:
        print(your_team, "need", 10 - total_yards, "yards for a first down")

    if total_yards <= 0 and clock >= 0 and current_down < 5 and line_of_scrim > 0:
        print(your_team, "need", 10 + abs(total_yards), "yards for a first down")
 
 #******(BELOW) GAME RESULTS (BELOW)******#   
    function_lib.simple_line()  
    if line_of_scrim <= 0:
        function_lib.blank_line()
        print("Touchdown,", your_team, "win!")
        import winningstars as win
        function_lib.status(1)
        break

    if clock <= 0:
        function_lib.blank_line()
        print("Time Expired.", your_team, "lose.")
        function_lib.status(2)
        break

    if current_down > 4:
        function_lib.blank_line()
        print("No more downs", your_team, "lose.")
        function_lib.status(2)
        break    
#******(ABOVE) GAME RESULTS (ABOVE)******#