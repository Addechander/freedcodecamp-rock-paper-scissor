# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
num_of_games = 0
def player(prev_play, opponent_history=[], prev_guess = []):
    global num_of_games
    if prev_play != "":
        opponent_history.append(prev_play)


    def player_v_quincy(opponent_history):
        counter_list = ["P", "S", "S", "R", "P"] 
        return counter_list[len(opponent_history) % len(counter_list)]
                 
    def player_v_kris(prev_play):
        if prev_play == "R":
            return "P"
        if prev_play == "P":
            return "S"
        if prev_play == "S":
             return "R"

    def player_v_mrugesh(opponent_history):
        pattern = opponent_history[-10:]
        most_frequent = min(set(pattern), key=pattern.count)
        if most_frequent == "R":
            return "P"
        if most_frequent == "P":
            return "S"
        if most_frequent == "S":
            return"R"

    def player_v_abbey(opponent_history):

        '''play_order={}

        last_two = "".join(opponent_history[-2:])
        if last_two in play_order.keys():
            play_order[last_two] += 1 
        else:
            play_order[last_two] = 1 
          

        potential_plays = [
            prev_play + "R",
            prev_play + "P",
            prev_play + "S",
        ]

        for i in potential_plays:
            if not i in play_order.keys():
                play_order[i] = 0

        predict = max(potential_plays, key=lambda key: play_order[key])'''

        counters = ['R', 'P', 'S']
        probabilities = {
            'R' : [0.44444444, 0.33333333, 0.33333333],
            'P': [0.33333333, 0.44444444, 0.33333333],
            'S' : [0.33333333, 0.33333333, 0.4444444]
        }

        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
      
        selected_item = random.choices(counters, probabilities[ideal_response[opponent_history[-1]]])[0]
  
        return selected_item
      
        '''# Transition probabilities
        transitions = {
        'R': {'R': 0.33, 'P': 0.33, 'S': 0.34},
        'P': {'R': 0.34, 'P': 0.33, 'S': 0.33},
        'S': {'R': 0.33, 'P': 0.34, 'S': 0.33}
        }
        

        next_state_probs = transitions[opponent_history[-1]]
        next_state = max(next_state_probs, key=lambda k: next_state_probs[k])
        
        return next_state'''


    guess = "R" 
    prev_guess.append(guess)
    num_of_games += 1

    def guess(opponent_history):
      global num_of_games
      if len(opponent_history) > 5:  
        if opponent_history[0:5] == ["R", "P", "P", "S", "R"]:
          num_of_games += 1
          return player_v_quincy(opponent_history)
        
        if [x == y for x, y in zip(opponent_history[0:5], prev_guess[0:5])] == [False for _ in range(5)]:
          prev_guess.append(guess)
          num_of_games += 1
          return player_v_kris(prev_play)
    
        if len(opponent_history) > 10 and prev_play == max(set(opponent_history[-10:]), key=opponent_history[-10:].count):
          num_of_games += 1
          return player_v_mrugesh(opponent_history)
    
        else:
          num_of_games += 1
          return player_v_abbey(opponent_history)
          


    move = guess(opponent_history)
    if num_of_games == 1000:
      opponent_history.clear()
      prev_guess.clear()
      num_of_games = 0
    
    return move
    







