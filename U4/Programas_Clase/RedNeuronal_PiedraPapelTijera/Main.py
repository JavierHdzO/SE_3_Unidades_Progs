#pip install scikit-learn

# El presente proyecto es una modificación al código fuente extraído de: 
# https://dev.to/marisbotero/juguemos-piedra-papel-y-tijera-con-redes-neuronales-2pm4
# Consulta realizada en Abril de 2022
#

################################################################################################################

from random import choice
from sklearn.neural_network import MLPClassifier #MultiLayer Perceptron << Type of ANN 
clf = MLPClassifier(verbose=False, warm_start=True)

options = ["R", "S", "P"] #R = rock    P = Paper  S = Scissors

################################################################################################################

def search_winner(p1, p2):
    if p1 == p2:
        return 0
    elif (p1 == "R" and p2 == "S") or (p1 == "S" and p2 == "P") or (p1 == "P" and p2 == "R"):
        return 1
    else:  #p1 == "R" and p2 == "P" #     p1 == "S" and p2 == "R" #      p1 == "P" and p2 == "S"
        return 2     

################################################################################################################

def str_to_list(option): #clase -> vector de salidas
    if option=="R":
        res = [1,0,0]
    elif option=="S":
        res = [0,1,0]
    else:
        res = [0,0,1]
    return res

################################################################################################################

def play_and_learn(tot_games):
    score = {"win": 0, "loose": 0}

    data_X = [] #input
    data_y = [] #output

    for i in range(tot_games):
        player1 = choice(options) #random input
        predict = list(model.predict_proba([str_to_list(player1)])[0]) #[0] = outputs  ##calculate an output

        ########################################################
        index = predict.index(max(predict))  #decision making
        if predict[index] >= 0.95: 
            player2 = options[index]        
        else:
            player2 = choice(options)
        ########################################################

        winner = search_winner(player1, player2)

        if winner==2: #save the winning case
            if str_to_list(player1) not in data_X: ## better or worse?
                data_X.append(str_to_list(player1))
                data_y.append(str_to_list(player2))

            score["win"]+=1
        else:
            score["loose"]+=1

    return score, data_X, data_y

################################################################################################################

data_X = str_to_list("R")
data_y = str_to_list("P")

model = clf.fit([data_X], [data_y]) #training

i = 0
iterations_without_change = 0
max_iterations_without_change = 10
best_precision = -1
while iterations_without_change < max_iterations_without_change:    
    i+=1
    score, data_X, data_y = play_and_learn(1000)
    precision = (score["win"]*100/(score["win"]+score["loose"]))    
    print("Iter: %s - score: %s %s %%" % (i, score, precision))

    if len(data_X):
        model = model.partial_fit(data_X, data_y) #Incremental learning

    if best_precision != precision:
        best_precision = precision
        iterations_without_change = 0
    
    iterations_without_change += 1

################################################################################################################
##
print("Testing: ")

op = "RS-G-11" #valor por defecto
while op!="X":
    op = input("Player Decision: ")
    if op!="X":
        predict = list(model.predict_proba([str_to_list(op)])[0])
        index = predict.index(max(predict))  #decision making    
        player2 = options[index]   
        winner = search_winner(op, player2)
        print("Player 1: ", op, " Player 2: ", player2, " Winner: ",  winner) #Player 2 will always win
    