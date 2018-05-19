# encoding=utf8
# Read File
from copy import deepcopy
f = open("input1.txt","r")
myList = []
for line in f:
    myList.append(line)
#    print line
player = myList[0].strip('\n')
algorithm = myList[1].strip('\n')
depthLimit = int(myList[2])

passC=0
passS=0
w, h = 8, 8;
current_board= [[0 for x in range(w)] for y in range(h)]
myList[3] = myList[3].strip('\n')
current_board[0] = myList[3].split(',')
myList[4] = myList[4].strip('\n')
current_board[1] = myList[4].split(',')
myList[5] = myList[5].strip('\n')
current_board[2] = myList[5].split(',')
myList[6] = myList[6].strip('\n')
current_board[3] = myList[6].split(',')
myList[7] = myList[7].strip('\n')
current_board[4] = myList[7].split(',')
myList[8] = myList[8].strip('\n')
current_board[5] = myList[8].split(',')
myList[9] = myList[9].strip('\n')
current_board[6] = myList[9].split(',')
myList[10] = myList[10].strip('\n')
current_board[7] = myList[10].split(',')

rowValues_circle = map(int, myList[11].split(','))

rowValues_star = [0 for x in range(w)]
for i in range(0,8,1):
    rowValues_star[7-i] = rowValues_circle[i]

circles=0
stars=0

w, h = 8, 8;
count_circle = [[0 for x in range(w)] for y in range(h)]
count_star = [[0 for x in range(w)] for y in range(h)]

for i in range(0,8,1):
    for j in range(0,8,1):
        count_star[i][j] = 0
        count_circle[i][j] = 0


def ccs(board):
    w, h = 8, 8;
    csa = [[0 for x in range(w)] for y in range(h)]

    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            if board[i][j].startswith("S"):
                sc = board[i][j]
                sc = int(sc[1:])
                csa[i][j]+=sc
    return csa
def ccsq(board):
    w, h = 8, 8;
    csa = 0

    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            if board[i][j].startswith("S"):
                sc = board[i][j]
                sc = int(sc[1:])
                csa+=sc
    return csa
def ccsqq(board):
    w, h = 8, 8;
    csa =0

    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            if board[i][j].startswith("C"):
                sc = board[i][j]
                sc = int(sc[1:])
                csa+=sc
    return csa

def ccs2(board):
    w, h = 8, 8;
    csb = [[0 for x in range(w)] for y in range(h)]

    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            if board[i][j].startswith("C"):
                sc = board[i][j]
                sc = int(sc[1:])
                csb[i][j]+=sc
    return csb

for i in range(0,8,1):
    for j in range(0,8,1):
        if current_board[i][j].startswith("S"):
            sc=current_board[i][j]
            sc=int(sc[1:])
            count_star[i][j] = count_star[i][j] + sc
        elif current_board[i][j].startswith("C"):
            cc = current_board[i][j]
            cc = int(cc[1:])
            count_circle[i][j] = count_circle[i][j] + cc

if player =="Star":
    current_player = "Star"
    opponent = "Circle"
else:
    current_player = "Circle"
    opponent = "Star"

initial_row = 0
initial_column = 0
final_row = 0
final_column = 0

w, h = 8, 8;
update_board = [[0 for x in range(w)] for y in range(h)]

best = []
for i in range(0, 5, 1):
    best.append(0)
if player != opponent:
    best[0] = float('-inf')
if player == opponent:
    best[0] = float('+inf')

nodes=1

f.close()

class BestUtility:
    def __init__(self,q,w,e,r,t):
        self.best_value=q
        self.best_initial_row=w
        self.best_initial_column=e
        self.best_final_row=r
        self.best_final_column=t

# Valid Moves for Star or Circle
def valid_move(player,board):
    if player == "Circle":
#        print(board)
        for i in range(0,8,1):
            for j in range(0,8,1):
                if board[i][j].startswith("C"):
                    # print("svdv")
                    #print(current_board[i][j])
                    if i+1<=7 and j+1<=7:
                        if board[i + 1][j + 1] == "0":
                            return 1
                    if i+1<=7 and j-1>=0:
                        if board[i + 1][j - 1] == "0":
                            return 1
                    if j + 2 <= 7 and i + 2 <= 7:
                        if board[i + 1][j + 1] == "S1" and board[i + 2][j + 2] == "0":
                            return 1
                    if j-2>=0 and i+2<=7:
                        if board[i + 1][j - 1] == "S1" and board[i + 2][j - 2] == "0":
                            return 1
                    if i==5 and j-2>=0 and j+2<=7:
                        if board[i + 1][j - 1] == "S1" and board[i + 2][j - 2].startswith("C"):
                            return 1
                        if board[i + 1][j + 1] == "S1" and board[i + 2][j + 2].startswith("C"):
                            return 1
                    if i==6:
                        if i+1<=7 and j+1<=7 and board[i + 1][j + 1] == "0":
                            return 1
                        if i+1<=7 and j-1>=0 and board[i + 1][j - 1] == "0":
                            return 1
                        if i+1<=7 and j+1<=7 and board[i + 1][j + 1].startswith("C"):
                            return 1
                        if i+1<=7 and j-1>=0 and board[i + 1][j - 1].startswith("C"):
                            return 1
        return 0

    if player == "Star":
        #print("lll")
        for i in range(0,8,1):
            for j in range(0,8,1):
                if board[i][j].startswith("S"):
                    # print("lll")
                    # print(i)
                    # print(j)
                    if i-1>=0 and j+1<=7:
                        if board[i - 1][j + 1] == "0":
                            return 1
                    if i-1>=0 and j-1>=0:
                        if board[i - 1][j - 1] == "0":
                            return 1
                    if i-2>=0 and j+2<=7:
                        if board[i - 1][j + 1] == "C1" and board[i - 2][j + 2] == "0":
                            return 1
                    if i-2>=0 and j-2>=0:
                        if board[i - 1][j - 1] == "C1" and board[i - 2][j - 2] == "0":
                            return 1
                    if i==2 and j+2<=7 and j-2>=0:
                        if board[i - 1][j - 1] == "C1" and board[i - 2][j - 2].startswith("S"):
                            return 1
                        if board[i - 1][j + 1] == "C1" and board[i - 2][j + 2].startswith("S"):
                            return 1
                    if i==1 :
                        if i-1>=0 and j+1<=7 and board[i - 1][j + 1] == "0":
                            return 1
                        if i-1>=0 and j-1>=0 and board[i - 1][j - 1] == "0" :
                            return 1
                        if i-1>=0 and j+1<=7 and board[i - 1][j + 1].startswith("S") :
                            return 1
                        if i-1>=0 and j-1>=0 and board[i - 1][j - 1].startswith("S"):
                            return 1
        return 0
    return 0

# Are any moves left in the board?
def moves_left(player,board):
    if valid_move(player,board) ==0:
        return 0
    else:
        return 1

# Is pass true or false?
def is_pass():
    if moves_left(player) == 1:
        return 0
    if moves_left(player) == 0:
        return 1


# Evaluate function
def evaluate(current_board):
    evaluated_value = 0;
    csa=ccs(current_board)
    csb=ccs2(current_board)
    #print(csa)
    #print(csb)
    if current_player == "Star":
        for i in range(0,8,1):
            for j in range(0,8,1):
                if current_board[i][j].startswith("S"):
                    evaluated_value += csa[i][j] * rowValues_star[i]
                #print(evaluated_value)
        for i in range(0, 8, 1):
            for j in range(0, 8, 1):
                if current_board[i][j].startswith("C"):
                     evaluated_value -= csb[i][j] * rowValues_circle[i]
            # print(evaluated_value)
    if current_player=="Circle":
        for i in range(0, 8, 1):
            for j in range(0, 8, 1):
                if current_board[i][j].startswith("C"):
                    evaluated_value += csb[i][j]*rowValues_circle[i]

        for i in range(0, 8, 1):
            for j in range(0, 8, 1):
                if current_board[i][j].startswith("S"):
                    evaluated_value  -=csa[i][j]*rowValues_star[i]


    return evaluated_value



def minimax(current_board, depthLimit, player, lo):#initial_row, initial_column, final_row, final_column):
    global nodes
    global best
    global passC
    global passS
    global circles
    global stars
    # print(nodes)
    # print("====================="+str(depthLimit))
    # print(current_board)
    # print(player)
    # print(moves_left(player,current_board))
    # print("=====================")

    if current_player==player:
        best[0]=float('-inf')

        ll = []
        ll.append(evaluate(current_board))

        # ll.append(initial_row)
        # ll.append(initial_column)
        # ll.append(final_row)
        # ll.append(final_column)
        ll.append(nodes)
        ll.append(lo)
        if depthLimit==0:
            # print("here")
            return ll
        if ccsq(current_board)==0 or ccsqq(current_board)==0:
            # print("QQQQQQQQQ")
            return ll

        # for c1 in range(0,8,1):
        #     for c2 in range(0,8,1):
        #         circles+=count_circle[c1][c2]
        #         stars+=count_star[c1][c2]
        #
        # if circles == 0 or stars==0:
        #     return ll

        if moves_left(player,current_board)==0 :
            if passC>0 and passS>0:
                #nodes+=1
                return ll
            if player=="Circle":
                nodes+=1
                passC+=1
                lm=deepcopy(lo)
                lm.append([-1, -1, -1, -1])
                # print (lm)
                # print("-----")
                return minimax(current_board,depthLimit-1,"Star",lm)
            else:
                nodes+=1
                passS+=1
                lm = deepcopy(lo)
                # print(lm)
                # print("-----")
                return minimax(current_board, depthLimit - 1, "Circle", lm)


        best_utility_array = []

        if depthLimit > 0:
            # print("here---")

            if player == "Circle" and moves_left(player,current_board)==1:
                # print("here---")
                for i in range(0, 8, 1):
                    for j in range(0, 8, 1):
                        if current_board[i][j].startswith("C"):
                            # print(current_board[i][j])
                            # print("here---")
                            if i == 6:
                                # print("here---")

                                #1-1
                                if j-1>=0 and current_board[i + 1][j - 1].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j - 1] = "C"+str(count_circle[i+1][j-1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    #move_value = evaluate(update_board,"Circle")
                                    print("10")
                                    lk = []
                                    lk=[i,j,i+1,j-1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("j-1>=0 and current_board[i + 1][j - 1].startswith(C)")
                                    utility=minimax(update_board, depthLimit - 1, "Star",lm)# i, j, i+1, j-1)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j - 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                        # for i9 in range(0,5,1):
                                        #     best[i9] = utility[i9]
                                    # print(str(best[1])+"??????????????????"+str(best[2]))
                                    best_utility_array.append(deepcopy(utility))

                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                #1-2
                                if j-1>=0 and current_board[i + 1][j - 1] == "0":
                                    nodes+=1
                                    update_board = deepcopy(current_board)
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j - 1] = "C1"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("8")
                                    lk = []
                                    lk=[i,j,i+1,j-1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j-1>=0 and current_board[i + 1][j - 1] == 0")
                                    utility=minimax(update_board, depthLimit - 1, "Star", lm) #i, j, i+1, j-1)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j - 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                        # for i7 in range(0,5,1):
                                        #     best[i7] = utility[i7]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))

                                        # print(str(best[1]) + "??????????????????1")
                                    best_utility_array.append(deepcopy(utility))
                                       # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                #1-3
                                if j+1<=7 and current_board[i + 1][j + 1].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j + 1] = "C"+str(count_circle[i+1][j+1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    move_value = evaluate(update_board,"Circle")
                                    # print("9")
                                    lk=[]
                                    lk=[i,j,i+1,j+1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+1<=7 and current_board[i + 1][j + 1].startswith(C)")
                                    utility=minimax(update_board, depthLimit - 1, "Star", lm)# i, j, i+1, j+1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j + 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                        # for i8 in range(0,5,1):
                                        #     best[i8] = utility[i8]
                                        # #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                    best_utility_array.append(deepcopy(utility))

                                 #   best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))



                                #1-4
                                if j+1<=7 and current_board[i + 1][j + 1] == "0":
                                    nodes+=1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j + 1] = "C1"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("7")
                                    lk=[i,j,i+1,j+1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+1<=7 and current_board[i + 1][j + 1] == 0:")
                                    utility=minimax(update_board, depthLimit - 1, "Star", lm)# i, j, i+1, j+1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j + 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                        # for i6 in range(0,5,1):
                                        #     best[i6] = utility[i6]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                    best_utility_array.append(deepcopy(utility))

                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i == 5:
                                # print("here---")
                                # 1
                                if j-2>=0 and current_board[i + 1][j - 1]=="S1" and current_board[i + 2][j - 2].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j - 1] -= 1
                                    count_circle[i + 2][j - 2] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j - 1] = "0"
                                    update_board[i + 2][j - 2] = "C"+str(count_circle[i+2][j-2])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("5")
                                    lk=[i,j,i+2,j-2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j-2>=0 and current_board[i + 1][j - 1]==S1 and current_board[i + 2][j - 2].startswith(C)")
                                    utility = minimax(update_board, depthLimit - 1, "Star", lm)#i, j, i + 2, j - 2)
                                    # print(str(utility)+"{{{{}{}{}}{")
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j - 1] += 1
                                    count_circle[i + 2][j - 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                        # for i4 in range(0, 5, 1):
                                        #     best[i4] = utility[i4]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                    best_utility_array.append(deepcopy(utility))

                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                # 2
                                if j+2<=7 and current_board[i + 1][j + 1]=="S1" and current_board[i + 2][j + 2].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j + 1] -= 1
                                    count_circle[i + 2][j + 2] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j + 1] = "0"
                                    update_board[i + 2][j + 2] = "C"+str(count_circle[i+2][j+2])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("6")
                                    lk=[i,j,i+2,j+2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+2<=7 and current_board[i + 1][j + 1]==S1 and current_board[i + 2][j + 2].startswith(C)")
                                    utility = minimax(update_board, depthLimit - 1, "Star", lm)#i, j, i + 2, j + 2)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j + 1] += 1
                                    count_circle[i + 2][j + 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                        # for i5 in range(0, 5, 1):
                                        #     best[i5] = utility[i5]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                    best_utility_array.append(deepcopy(utility))

                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            #2-1
                            if i + 1 <= 7 and j - 1 >= 0 and i!=6:
                                # print("here---!!!!!!!!!!!!!!!!!!!!!"+str(i)+str(j))
                                # print(current_board)
                                if current_board[i + 1][j - 1] == "0":
                                    nodes+=1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board=deepcopy(current_board)
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    # print(count_circle[i][j])
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j - 1] += 1
                                    if count_circle[i][j]==0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C"+str(count_circle[i][j])
                                    update_board[i + 1][j - 1] = "C"+str(count_circle[i+1][j-1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("2")
                                    lk=[i,j,i+1,j-1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i + 1 <= 7 and j - 1 >= 0 and i!=6:")
                                    utility=minimax(update_board, depthLimit - 1, "Star", lm)# i, j, i+1, j-1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j - 1] -= 1
                                    #print(move_value)
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                        # for i31 in range(0,5,1):
                                        #     best[i31] = utility[i31]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    #print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                   # best_utility_array.append(BestUtility(utility[0],utility[1],utility[2],utility[3],utility[4]))

                            #2-2
                            if i + 1 <= 7 and j + 1 <= 7 and i!=6:
                                # print("here---!!!!!!!!!!!!!!!!!!!!!" + str(i) + str(j))
                                # print("here---")
                                if current_board[i + 1][j + 1] == "0":
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board = deepcopy(current_board)
                                    # print("here---")
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j + 1] += 1
                                    if count_circle[i][j]==0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C"+str(count_circle[i][j])
                                    update_board[i + 1][j + 1] = "C"+str(count_circle[i+1][j+1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("1")
                                    lk=[i,j,i+1,j+1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i + 1 <= 7 and j + 1 <= 7 and i!=6:")
                                    utility=minimax(update_board, depthLimit - 1, "Star", lm)#i, j, i+1, j+1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j + 1] -= 1
                                    # print move_value
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                        # for iw in range(0,5,1):
                                        #     best[iw] = utility[iw]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    #print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            #2-3
                            if j - 2 >= 0 and i + 2 <= 7:
                                # print("here---")
                                if current_board[i + 1][j - 1] == "S1" and current_board[i + 2][j - 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j - 1] -= 1
                                    count_circle[i + 2][j - 2] += 1
                                    if count_circle[i][j]==0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C"+str(count_circle[i][j])
                                    update_board[i + 2][j - 2] = "C1"
                                    update_board[i + 1][j - 1] = "0"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("4")
                                    lk=[i,j,i+2,j-2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j - 2 >= 0 and i + 2 <= 7:")
                                    utility=minimax(update_board, depthLimit - 1, "Star", lm)# i, j, i+2, j-2)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j - 1] += 1
                                    count_circle[i + 2][j - 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)

                                    best_utility_array.append(deepcopy(utility))

                                        # for i3 in range(0,5,1):
                                        #     best[i3] = utility[i3]
                                       # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            #2-4
                            if j + 2 <= 7 and i + 2 <= 7:
                                # print("here---")
                                if current_board[i + 1][j + 1] == "S1" and current_board[i + 2][j + 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j + 1] -= 1
                                    count_circle[i + 2][j + 2] += 1

                                    if count_circle[i][j]==0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C"+str(count_circle[i][j])
                                    update_board[i + 2][j + 2] = "C1"
                                    update_board[i+1][j+1] = "0"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("3")
                                    lk=[i,j,i+2,j+2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j + 2 <= 7 and i + 2 <= 7:")
                                    utility=minimax(update_board, depthLimit - 1, "Star", lm)#i, j, i+2, j+2)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j + 1] += 1
                                    count_circle[i + 2][j + 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                        # for i2 in range(0,5,1):
                                        #     best[i2] = utility[i2]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3])+"{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                  #  best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))



                # print("here---")
                # print(str(len(best_utility_array))+"---------------------------------------")
                max1 = float('-inf')
                for kk in best_utility_array:
                    if kk[0] > max1:
                        max1 = kk[0]
                ft = []
                for kk in best_utility_array:
                    if (kk[0] == max1):
                        ft.append(kk)
                minx = float('inf')
                for kk in ft:
                    if kk[2][0][2] < minx:
                        minx = kk[2][0][2]
                ad = []
                for kk in ft:
                    if kk[2][0][2] == minx:
                        ad.append(kk)
                miny = float('inf')
                for kk in ad:
                    if kk[2][0][3] < miny:
                        miny = kk[2][0][3]
                ad2 = []
                for kk in ad:
                    if kk[2][0][3] == miny:
                        ad2.append(kk)
                        # print(miny)
                        # print("+++++++++++++++++++++++++++")
                best = deepcopy(ad2[0])
                # for f in best_utility_array:
                #     print("abcd")
                #     print(f.best_value)
                #     print(f.best_final_row)
                #     print(f.best_final_column)
                return best

            elif player=="Circle" and moves_left(player,current_board)==0:
                ll = []
                ll.append(evaluate(current_board, player))

                ll.append(nodes)
                ll.append(lo)
                return ll


            if player == "Star" and moves_left(player,current_board)==1:
                # print("===========")
                # print(best[0])
                for i in range(0, 8, 1):
                    for j in range(0, 8, 1):
                        if current_board[i][j].startswith("S"):
                            # print(current_board)
                            # print("||||||||||||||")
                                        #1-1
                            if i==1:
                                if i-1>=0 and j-1>=0 and current_board[i - 1][j - 1].startswith("S"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j - 1] += 1
                                    update_board[i][j]="0"
                                    update_board[i - 1][j - 1]="S"+str(count_star[i-1][j-1])
                                    # print("===========!!!!!!!!!!****")
                                    # print(update_board)
                                    #print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("10")
                                    lk=[i,j,i-1,j-1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j-1>=0 and current_board[i - 1][j - 1].startswith(S):")
                                    utility=minimax(update_board, depthLimit - 1, "Circle", lm)# i, j, i-1, j-1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j - 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                        # for i21 in range(0,5,1):
                                        #     best[i21] = utility[i21]
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                #1-2
                                if i-1>=0 and j-1>=0 and current_board[i - 1][j - 1] == "0":
                                    # print(current_board)
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j - 1]="S1"
                                    # print("===========!!!!!!!!!!***")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("8")
                                    lk=[i,j,i-1,j-1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j-1>=0 and current_board[i - 1][j - 1] == 0:")
                                    utility=minimax(update_board, depthLimit - 1, "Circle", lm)# i, j, i-1, j-1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j - 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                #1-3
                                if i-1>=0 and j+1<=7 and current_board[i - 1][j + 1].startswith("S"):
                                    # print("aaaaaaaa")
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board=deepcopy(current_board)
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j + 1]="S"+str(count_star[i-1][j+1])
                                    # print("===========!!!!!!!!!!**")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("9")
                                    lk=[i,j,i-1,j+1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j+1<=7 and current_board[i - 1][j + 1].startswith(S):")
                                    utility=minimax(update_board, depthLimit - 1, "Circle", lm)# i, j, i-1, j+1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j + 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                        # for i19 in range(0,5,1):
                                        #     best[i19] = utility[i19]
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                #1-4
                                if i-1>=0 and j+1<=7 and current_board[i - 1][j + 1] == "0":
                                    # print(current_board)
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i-1][j+1]="S1"

                                    # print("===========!!!!!!!!!!*"+str(i)+" "+str(j))
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("7")
                                    lk=[i,j,i-1,j+1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j+1<=7 and current_board[i - 1][j + 1] == 0")
                                    utility=minimax(update_board, depthLimit - 1, "Circle", lm)# i, j, i-1, j+1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j + 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                        # for i17 in range(0,5,1):
                                        #     best[i17] = utility[i17]
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i == 2:
                                if j-2>=0 and current_board[i - 1][j - 1] == "C1" and current_board[i - 2][j - 2].startswith("S"):
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board=deepcopy(current_board)
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j - 1] -= 1
                                    count_star[i - 2][j - 2] += 1
                                    update_board[i][j]="0"
                                    update_board[i-1][j-1]="0"
                                    update_board[i - 2][j - 2]="S"+str(count_star[i-2][j-2])
                                    # print("===========!!!!!!!!!!---------")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("5")
                                    lk=[i,j,i-2,j-2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j-2>=0 and current_board[i - 1][j - 1] == C1 and current_board[i - 2][j - 2].startswith(S):")
                                    utility=minimax(update_board, depthLimit - 1, "Circle", lm)#i, j, i-2, j-2)
                                    # print(str(utility[0])+"|}|}|}|}|")
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j - 1] += 1
                                    count_star[i - 2][j - 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                        # for i15 in range(0,5,1):
                                        #     best[i15] = utility[i15]
                                    #best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                if j+2<=7 and current_board[i - 1][j + 1] == "C1" and current_board[i - 2][j + 2].startswith("S"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j + 1] -= 1
                                    count_star[i - 2][j + 2] += 1
                                    update_board[i][j]="0"
                                    update_board[i-1][j+1]="0"
                                    update_board[i - 2][j + 2]="S"+str(count_star[i-2][j+2])
                                    # print("===========!!!!!!!!!!----------")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("6")
                                    lk=[i,j,i-2,j+2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+2<=7 and current_board[i - 1][j + 1] == C1 and current_board[i - 2][j + 2].startswith(S):")
                                    utility=minimax(update_board, depthLimit - 1, "Circle", lm)#i, j, i-2, j+2)
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j + 1] += 1
                                    count_star[i - 2][j + 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                        # for i16 in range(0,5,1):
                                        #     best[i16] = utility[i16]
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 2 >= 0 and j - 2 >= 0 and i!=1:
                                if current_board[i - 1][j - 1] == "C1" and current_board[i - 2][j - 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j - 1] -= 1
                                    count_star[i - 2][j - 2] += 1
                                    if count_star[i][j]==0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S"+str(count_star[i][j])

                                    update_board[i][j]="0"
                                    update_board[i-1][j-1]="0"
                                    update_board[i - 2][j - 2]="S1"
                                    # print("===========!!!!!!!!!!@")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("4")
                                    lk=[i,j,i-2,j-2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 2 >= 0 and j - 2 >= 0 and i!=1:")
                                    utility=deepcopy(minimax(update_board, depthLimit - 1, "Circle", lm)) # i, j, i-2, j-2))
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j - 1] += 1
                                    count_star[i - 2][j - 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                        # for i14 in range(0,5,1):
                                        #     best[i14] = utility[i14]
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 2 >= 0 and j + 2 <= 7 and i!=1:
                                if current_board[i - 1][j + 1] == "C1" and current_board[i - 2][j + 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j + 1] -= 1
                                    count_star[i - 2][j + 2] += 1
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])
                                    update_board[i-1][j+1]="0"
                                    update_board[i - 2][j + 2]="S1"
                                    # print("===========!!!!!!!!!!#")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("3")
                                    lk=[i,j,i-2,j+2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 2 >= 0 and j + 2 <= 7 and i!=1:")
                                    utility=minimax(update_board, depthLimit - 1, "Circle", lm)#i, j, i-2, j+2)
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j + 1] += 1
                                    count_star[i - 2][j + 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                        # for i13 in range(0,5,1):
                                        #     best[i13] = utility[i13]
                                    # print(str(best[0]) + "{{{{{{{{{{{{")
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 1 >= 0 and j - 1 >= 0 and i!=1:
                                if current_board[i - 1][j - 1] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j - 1] += 1
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])
                                    update_board[i - 1][j - 1]="S1"
                                    # print("===========!!!!!!!!!!$")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("2")
                                    lk=[i,j,i-1,j-1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 1 >= 0 and j - 1 >= 0 and i!=1:")
                                    utility=minimax(update_board, depthLimit - 1, "Circle", lm)# i, j, i-1, j-1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j - 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                        # for i12 in range(0,5,1):
                                        #     best[i12] = utility[i12]
                                    # print(str(best[0]) + "{{{{{{{{{{{{")
                                    # print(best[i])
                                    #best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 1 >= 0 and j + 1 <= 7 and i!=1:
                                if current_board[i - 1][j + 1] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # print(str(i) + " " + str(j))
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j + 1] += 1
                                    # print(update_board)
                                    # print(str(i-1)+" "+str(j+1))
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])
                                    update_board[i-1][j+1]="S1"

                                    # print(update_board)
                                    # print(current_board)
                                    lk=[i,j,i-1,j+1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 1 >= 0 and j + 1 <= 7 and i!=1:")
                                    utility=minimax(update_board, depthLimit - 1, "Circle", lm)#i, j, i-1, j+1)
                                    # print("===========!!!!!!!!!!^" + str(utility))
                                    count_star[i][j] += 1
                                    count_star[i - 1][j + 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                        # for i11 in range(0,5,1):
                                        #     best[i11] = utility[i11]
                                    # print(str(best[0])+"{{{{{{{{{{{{")
                                    #best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                # print("abcd--1111")
                # for f in best_utility_array:
                #     print("abcd--1111")
                #     print(f.best_value)
                max1=float('-inf')
                for kk in best_utility_array:
                    if kk[0]>max1:
                        max1=kk[0]
                ft=[]
                for kk in best_utility_array:
                    if(kk[0]==max1):
                        ft.append(kk)
                minx=float('inf')
                for kk in ft:
                    if kk[2][0][2]<minx:
                        minx=kk[2][0][2]
                ad=[]
                for kk in ft:
                    if kk[2][0][2] == minx:
                        ad.append(kk)
                miny = float('inf')
                for kk in ad:
                    if kk[2][0][3] < miny:
                        miny = kk[2][0][3]
                ad2 = []
                for kk in ad:
                    if kk[2][0][3] == miny:
                        ad2.append(kk)
                        # print(miny)
                        # print("+++++++++++++++++++++++++++")
                best=deepcopy(ad2[0])


            elif player == "Star" and moves_left(player,current_board) == 0:
                ll = []
                ll.append(evaluate(current_board))

                # ll.append(initial_row)
                # ll.append(initial_column)
                # ll.append(final_row)
                # ll.append(final_column)
                ll.append(nodes)
                ll.append(lo)
                return ll



        # print(str(len(best_utility_array)) + "---------------------------------------)))))"+str(best[1])+str(best[2]))
        return best

    else:
        best[0]=float('inf')
        ll = []
        ll.append(evaluate(current_board))

        # ll.append(initial_row)
        # ll.append(initial_column)
        # ll.append(final_row)
        # ll.append(final_column)
        ll.append(nodes)
        ll.append(lo)
        if depthLimit == 0:
            # print("here")
            return ll
        if ccsq(current_board) == 0 or ccsqq(current_board) == 0:
            # print("QQQQQQQQQ")
            return ll

        # for c1 in range(0,8,1):
        #     for c2 in range(0,8,1):
        #         circles+=count_circle[c1][c2]
        #         stars+=count_star[c1][c2]
        #
        # if circles == 0 or stars==0:
        #     return ll

        if moves_left(player, current_board) == 0:
            if passC > 0 and passS > 0:
                # nodes+=1
                return ll
            if player == "Circle":
                nodes += 1
                passC += 1
                lm = deepcopy(lo)
                # print (lm)
                # print("-----")
                return minimax(current_board, depthLimit - 1, "Star", lm)
            else:
                nodes += 1
                passS += 1
                lm = deepcopy(lo)
                # print(lm)
                # print("-----")
                return minimax(current_board, depthLimit - 1, "Circle", lm)

        best_utility_array = []

        if depthLimit > 0:
            # print("here---")

            if player == "Circle" and moves_left(player, current_board) == 1:
                # print("here---")
                for i in range(0, 8, 1):
                    for j in range(0, 8, 1):
                        if current_board[i][j].startswith("C"):
                            # print(current_board[i][j])
                            # print("here---")
                            if i == 6:
                                # print("here---")

                                # 1-1
                                if j - 1 >= 0 and current_board[i + 1][j - 1].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j - 1] = "C" + str(count_circle[i + 1][j - 1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("10")
                                    lk = []
                                    lk = [i, j, i + 1, j - 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("j-1>=0 and current_board[i + 1][j - 1].startswith(C)")
                                    utility = minimax(update_board, depthLimit - 1, "Star", lm)  # i, j, i+1, j-1)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j - 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                        # for i9 in range(0,5,1):
                                        #     best[i9] = utility[i9]
                                    # print(str(best[1]) + "??????????????????" + str(best[2]))
                                    best_utility_array.append(deepcopy(utility))

                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                # 1-2
                                if j - 1 >= 0 and current_board[i + 1][j - 1] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j - 1] = "C1"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("8")
                                    lk = []
                                    lk = [i, j, i + 1, j - 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j-1>=0 and current_board[i + 1][j - 1] == 0")
                                    utility = minimax(update_board, depthLimit - 1, "Star", lm)  # i, j, i+1, j-1)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j - 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                        # for i7 in range(0,5,1):
                                        #     best[i7] = utility[i7]
                                        # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))

                                        # print(str(best[1]) + "??????????????????1")
                                    best_utility_array.append(deepcopy(utility))
                                    # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                # 1-3
                                if j + 1 <= 7 and current_board[i + 1][j + 1].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j + 1] = "C" + str(count_circle[i + 1][j + 1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("9")
                                    lk = []
                                    lk = [i, j, i + 1, j + 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+1<=7 and current_board[i + 1][j + 1].startswith(C)")
                                    utility = minimax(update_board, depthLimit - 1, "Star", lm)  # i, j, i+1, j+1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j + 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                        # for i8 in range(0,5,1):
                                        #     best[i8] = utility[i8]
                                        # #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}" + str(best[4]))
                                    best_utility_array.append(deepcopy(utility))

                                #   best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                # 1-4
                                if j + 1 <= 7 and current_board[i + 1][j + 1] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j + 1] = "C1"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("7")
                                    lk = [i, j, i + 1, j + 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+1<=7 and current_board[i + 1][j + 1] == 0:")
                                    utility = minimax(update_board, depthLimit - 1, "Star", lm)  # i, j, i+1, j+1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j + 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                        # for i6 in range(0,5,1):
                                        #     best[i6] = utility[i6]
                                        # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}" + str(best[4]))
                                    best_utility_array.append(deepcopy(utility))

                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i == 5:
                                # print("here---")
                                # 1
                                if j - 2 >= 0 and current_board[i + 1][j - 1] == "S1" and current_board[i + 2][
                                    j - 2].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j - 1] -= 1
                                    count_circle[i + 2][j - 2] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j - 1] = "0"
                                    update_board[i + 2][j - 2] = "C" + str(count_circle[i + 2][j - 2])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("5")
                                    lk = [i, j, i + 2, j - 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j-2>=0 and current_board[i + 1][j - 1]==S1 and current_board[i + 2][j - 2].startswith(C)")
                                    utility = minimax(update_board, depthLimit - 1, "Star", lm)  # i, j, i + 2, j - 2)
                                    # print(str(utility) + "{{{{}{}{}}{")
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j - 1] += 1
                                    count_circle[i + 2][j - 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                        # for i4 in range(0, 5, 1):
                                        #     best[i4] = utility[i4]
                                        # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}" + str(best[4]))
                                    best_utility_array.append(deepcopy(utility))

                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                # 2
                                if j + 2 <= 7 and current_board[i + 1][j + 1] == "S1" and current_board[i + 2][
                                    j + 2].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j + 1] -= 1
                                    count_circle[i + 2][j + 2] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j + 1] = "0"
                                    update_board[i + 2][j + 2] = "C" + str(count_circle[i + 2][j + 2])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("6")
                                    lk = [i, j, i + 2, j + 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+2<=7 and current_board[i + 1][j + 1]==S1 and current_board[i + 2][j + 2].startswith(C)")
                                    utility = minimax(update_board, depthLimit - 1, "Star", lm)  # i, j, i + 2, j + 2)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j + 1] += 1
                                    count_circle[i + 2][j + 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                        # for i5 in range(0, 5, 1):
                                        #     best[i5] = utility[i5]
                                        # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}" + str(best[4]))
                                    best_utility_array.append(deepcopy(utility))

                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            # 2-1
                            if i + 1 <= 7 and j - 1 >= 0 and i != 6:
                                # print("here---!!!!!!!!!!!!!!!!!!!!!" + str(i) + str(j))
                                # print(current_board)
                                if current_board[i + 1][j - 1] == "0":
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board = deepcopy(current_board)
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    # print(count_circle[i][j])
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j - 1] += 1
                                    if count_circle[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C" + str(count_circle[i][j])
                                    update_board[i + 1][j - 1] = "C" + str(count_circle[i + 1][j - 1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("2")
                                    lk = [i, j, i + 1, j - 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i + 1 <= 7 and j - 1 >= 0 and i!=6:")
                                    utility = minimax(update_board, depthLimit - 1, "Star", lm)  # i, j, i+1, j-1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j - 1] -= 1
                                    # print(move_value)
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                    # for i31 in range(0,5,1):
                                    #     best[i31] = utility[i31]
                                    # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                # best_utility_array.append(BestUtility(utility[0],utility[1],utility[2],utility[3],utility[4]))

                            # 2-2
                            if i + 1 <= 7 and j + 1 <= 7 and i != 6:
                                # print("here---!!!!!!!!!!!!!!!!!!!!!" + str(i) + str(j))
                                # print("here---")
                                if current_board[i + 1][j + 1] == "0":
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board = deepcopy(current_board)
                                    # print("here---")
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j + 1] += 1
                                    if count_circle[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C" + str(count_circle[i][j])
                                    update_board[i + 1][j + 1] = "C" + str(count_circle[i + 1][j + 1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("1")
                                    lk = [i, j, i + 1, j + 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i + 1 <= 7 and j + 1 <= 7 and i!=6:")
                                    utility = minimax(update_board, depthLimit - 1, "Star", lm)  # i, j, i+1, j+1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j + 1] -= 1
                                    # print move_value
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                    # for iw in range(0,5,1):
                                    #     best[iw] = utility[iw]
                                    # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            # 2-3
                            if j - 2 >= 0 and i + 2 <= 7:
                                # print("here---")
                                if current_board[i + 1][j - 1] == "S1" and current_board[i + 2][j - 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j - 1] -= 1
                                    count_circle[i + 2][j - 2] += 1
                                    if count_circle[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C" + str(count_circle[i][j])
                                    update_board[i + 2][j - 2] = "C1"
                                    update_board[i + 1][j - 1] = "0"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("4")
                                    lk = [i, j, i + 2, j - 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j - 2 >= 0 and i + 2 <= 7:")
                                    utility = minimax(update_board, depthLimit - 1, "Star", lm)  # i, j, i+2, j-2)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j - 1] += 1
                                    count_circle[i + 2][j - 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)

                                    best_utility_array.append(deepcopy(utility))

                                    # for i3 in range(0,5,1):
                                    #     best[i3] = utility[i3]
                                    # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}" + str(best[4]))
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            # 2-4
                            if j + 2 <= 7 and i + 2 <= 7:
                                # print("here---")
                                if current_board[i + 1][j + 1] == "S1" and current_board[i + 2][j + 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j + 1] -= 1
                                    count_circle[i + 2][j + 2] += 1

                                    if count_circle[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C" + str(count_circle[i][j])
                                    update_board[i + 2][j + 2] = "C1"
                                    update_board[i + 1][j + 1] = "0"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("3")
                                    lk = [i, j, i + 2, j + 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j + 2 <= 7 and i + 2 <= 7:")
                                    utility = minimax(update_board, depthLimit - 1, "Star", lm)  # i, j, i+2, j+2)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j + 1] += 1
                                    count_circle[i + 2][j + 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    # for i2 in range(0,5,1):
                                    #     best[i2] = utility[i2]
                                    # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}" + str(best[4]))
                                #  best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                # print("here---")
                # print(str(len(best_utility_array)) + "---------------------------------------")
                max1 = float('-inf')
                for kk in best_utility_array:
                    if kk[0] > max1:
                        max1 = kk[0]
                ft = []
                for kk in best_utility_array:
                    if (kk[0] == max1):
                        ft.append(kk)
                minx = float('inf')
                for kk in ft:
                    if kk[2][0][2] < minx:
                        minx = kk[2][0][2]
                ad = []
                for kk in ft:
                    if kk[2][0][2] == minx:
                        ad.append(kk)
                miny = float('inf')
                for kk in ad:
                    if kk[2][0][3] < miny:
                        miny = kk[2][0][3]
                ad2 = []
                for kk in ad:
                    if kk[2][0][3] == miny:
                        ad2.append(kk)
                        # print(miny)
                        # print("+++++++++++++++++++++++++++")
                best = deepcopy(ad2[0])
                # for f in best_utility_array:
                #     print("abcd")
                #     print(f.best_value)
                #     print(f.best_final_row)
                #     print(f.best_final_column)
                return best

            elif player == "Circle" and moves_left(player, current_board) == 0:
                ll = []
                ll.append(evaluate(current_board, player))

                ll.append(nodes)
                ll.append(lo)
                return ll

            if player == "Star" and moves_left(player, current_board) == 1:
                # print("===========")
                # print(best[0])
                for i in range(0, 8, 1):
                    for j in range(0, 8, 1):
                        if current_board[i][j].startswith("S"):
                            # print(current_board)
                            # print("||||||||||||||")
                            # 1-1
                            if i == 1:
                                if i - 1 >= 0 and j - 1 >= 0 and current_board[i - 1][j - 1].startswith("S"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j - 1] = "S" + str(count_star[i - 1][j - 1])
                                    # print("===========!!!!!!!!!!****")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("10")
                                    lk = [i, j, i - 1, j - 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j-1>=0 and current_board[i - 1][j - 1].startswith(S):")
                                    utility = minimax(update_board, depthLimit - 1, "Circle", lm)  # i, j, i-1, j-1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j - 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                    # for i21 in range(0,5,1):
                                    #     best[i21] = utility[i21]
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                # 1-2
                                if i - 1 >= 0 and j - 1 >= 0 and current_board[i - 1][j - 1] == "0":
                                    # print(current_board)
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j - 1] = "S1"
                                    # print("===========!!!!!!!!!!***")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("8")
                                    lk = [i, j, i - 1, j - 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j-1>=0 and current_board[i - 1][j - 1] == 0:")
                                    utility = minimax(update_board, depthLimit - 1, "Circle", lm)  # i, j, i-1, j-1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j - 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                # 1-3
                                if i - 1 >= 0 and j + 1 <= 7 and current_board[i - 1][j + 1].startswith("S"):
                                    # print("aaaaaaaa")
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board = deepcopy(current_board)
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j + 1] = "S" + str(count_star[i - 1][j + 1])
                                    # print("===========!!!!!!!!!!**")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("9")
                                    lk = [i, j, i - 1, j + 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j+1<=7 and current_board[i - 1][j + 1].startswith(S):")
                                    utility = minimax(update_board, depthLimit - 1, "Circle", lm)  # i, j, i-1, j+1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j + 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                    # for i19 in range(0,5,1):
                                    #     best[i19] = utility[i19]
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                # 1-4
                                if i - 1 >= 0 and j + 1 <= 7 and current_board[i - 1][j + 1] == "0":
                                    # print(current_board)
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j + 1] = "S1"

                                    # print("===========!!!!!!!!!!*" + str(i) + " " + str(j))
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("7")
                                    lk = [i, j, i - 1, j + 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j+1<=7 and current_board[i - 1][j + 1] == 0")
                                    utility = minimax(update_board, depthLimit - 1, "Circle", lm)  # i, j, i-1, j+1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j + 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                    # for i17 in range(0,5,1):
                                    #     best[i17] = utility[i17]
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i == 2:
                                if j - 2 >= 0 and current_board[i - 1][j - 1] == "C1" and current_board[i - 2][j - 2].startswith("S"):
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board = deepcopy(current_board)
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j - 1] -= 1
                                    count_star[i - 2][j - 2] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j - 1] = "0"
                                    update_board[i - 2][j - 2] = "S" + str(count_star[i - 2][j - 2])
                                    # print("===========!!!!!!!!!!---------")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("5")
                                    lk = [i, j, i - 2, j - 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print(
                                    #     "if j-2>=0 and current_board[i - 1][j - 1] == C1 and current_board[i - 2][j - 2].startswith(S):")
                                    utility = minimax(update_board, depthLimit - 1, "Circle", lm)  # i, j, i-2, j-2)
                                    # print(str(utility[0]) + "|}|}|}|}|")
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j - 1] += 1
                                    count_star[i - 2][j - 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    # for i15 in range(0,5,1):
                                    #     best[i15] = utility[i15]
                                    # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                if j + 2 <= 7 and current_board[i - 1][j + 1] == "C1" and current_board[i - 2][
                                    j + 2].startswith("S"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j + 1] -= 1
                                    count_star[i - 2][j + 2] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j + 1] = "0"
                                    update_board[i - 2][j + 2] = "S" + str(count_star[i - 2][j + 2])
                                    # print("===========!!!!!!!!!!----------")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("6")
                                    lk = [i, j, i - 2, j + 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print(
                                    #     "if j+2<=7 and current_board[i - 1][j + 1] == C1 and current_board[i - 2][j + 2].startswith(S):")
                                    utility = minimax(update_board, depthLimit - 1, "Circle", lm)  # i, j, i-2, j+2)
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j + 1] += 1
                                    count_star[i - 2][j + 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                    # for i16 in range(0,5,1):
                                    #     best[i16] = utility[i16]
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 2 >= 0 and j - 2 >= 0 and i != 1:
                                if current_board[i - 1][j - 1] == "C1" and current_board[i - 2][j - 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j - 1] -= 1
                                    count_star[i - 2][j - 2] += 1
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])

                                    update_board[i][j] = "0"
                                    update_board[i - 1][j - 1] = "0"
                                    update_board[i - 2][j - 2] = "S1"
                                    # print("===========!!!!!!!!!!@")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("4")
                                    lk = [i, j, i - 2, j - 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 2 >= 0 and j - 2 >= 0 and i!=1:")
                                    utility = deepcopy(
                                        minimax(update_board, depthLimit - 1, "Circle", lm))  # i, j, i-2, j-2))
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j - 1] += 1
                                    count_star[i - 2][j - 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                    # for i14 in range(0,5,1):
                                    #     best[i14] = utility[i14]
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 2 >= 0 and j + 2 <= 7 and i != 1:
                                if current_board[i - 1][j + 1] == "C1" and current_board[i - 2][j + 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j + 1] -= 1
                                    count_star[i - 2][j + 2] += 1
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])
                                    update_board[i - 1][j + 1] = "0"
                                    update_board[i - 2][j + 2] = "S1"
                                    # print("===========!!!!!!!!!!#")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("3")
                                    lk = [i, j, i - 2, j + 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 2 >= 0 and j + 2 <= 7 and i!=1:")
                                    utility = minimax(update_board, depthLimit - 1, "Circle", lm)  # i, j, i-2, j+2)
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j + 1] += 1
                                    count_star[i - 2][j + 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                    # for i13 in range(0,5,1):
                                    #     best[i13] = utility[i13]
                                    # print(str(best[0]) + "{{{{{{{{{{{{")
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 1 >= 0 and j - 1 >= 0 and i != 1:
                                if current_board[i - 1][j - 1] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j - 1] += 1
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])
                                    update_board[i - 1][j - 1] = "S1"
                                    # print("===========!!!!!!!!!!$")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("2")
                                    lk = [i, j, i - 1, j - 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 1 >= 0 and j - 1 >= 0 and i!=1:")
                                    utility = minimax(update_board, depthLimit - 1, "Circle", lm)  # i, j, i-1, j-1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j - 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                    # for i12 in range(0,5,1):
                                    #     best[i12] = utility[i12]
                                    # print(str(best[0]) + "{{{{{{{{{{{{")
                                    # print(best[i])
                                    # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 1 >= 0 and j + 1 <= 7 and i != 1:
                                if current_board[i - 1][j + 1] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # print(str(i) + " " + str(j))
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j + 1] += 1
                                    # print(update_board)
                                    # print(str(i - 1) + " " + str(j + 1))
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])
                                    update_board[i - 1][j + 1] = "S1"

                                    # print(update_board)
                                    # print(current_board)
                                    lk = [i, j, i - 1, j + 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 1 >= 0 and j + 1 <= 7 and i!=1:")
                                    utility = minimax(update_board, depthLimit - 1, "Circle", lm)  # i, j, i-1, j+1)
                                    # print("===========!!!!!!!!!!^" + str(utility))
                                    count_star[i][j] += 1
                                    count_star[i - 1][j + 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))

                                    # for i11 in range(0,5,1):
                                    #     best[i11] = utility[i11]
                                    # print(str(best[0]) + "{{{{{{{{{{{{")
                                    # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                # print("abcd--1111")
                # for f in best_utility_array:
                #     print("abcd--1111")
                #     print(f.best_value)
                max1 = float('-inf')
                for kk in best_utility_array:
                    if kk[0] > max1:
                        max1 = kk[0]
                ft = []
                for kk in best_utility_array:
                    if (kk[0] == max1):
                        ft.append(kk)
                minx = float('inf')
                for kk in ft:
                    if kk[2][0][2] < minx:
                        minx = kk[2][0][2]
                ad = []
                for kk in ft:
                    if kk[2][0][2] == minx:
                        ad.append(kk)
                miny = float('inf')
                for kk in ad:
                    if kk[2][0][3] < miny:
                        miny = kk[2][0][3]
                ad2 = []
                for kk in ad:
                    if kk[2][0][3] == miny:
                        ad2.append(kk)
                        # print(miny)
                        # print("+++++++++++++++++++++++++++")
                best = deepcopy(ad2[0])


            elif player == "Star" and moves_left(player, current_board) == 0:
                ll = []
                ll.append(evaluate(current_board))

                # ll.append(initial_row)
                # ll.append(initial_column)
                # ll.append(final_row)
                # ll.append(final_column)
                ll.append(nodes)
                ll.append(lo)
                return ll

        # print(str(len(best_utility_array)) + "---------------------------------------)))))" + str(best[1]) + str(
        #     best[2]))
        return best





def alphabeta(current_board, depthLimit, player, lo, alpha, beta):#initial_row, initial_column, final_row, final_column):
    # print(alpha)
    # print(beta)
    global nodes
    global best
    global passC
    global passS
    global circles
    global stars
    # print(nodes)
    # print("====================="+str(depthLimit))
    # print(current_board)
    # print(player)
    # print(moves_left(player,current_board))
    # print("=====================")

    if current_player==player:
        best[0]=float('-inf')

        ll = []
        ll.append(evaluate(current_board))

        # ll.append(initial_row)
        # ll.append(initial_column)
        # ll.append(final_row)
        # ll.append(final_column)
        ll.append(nodes)
        ll.append(lo)
        if depthLimit==0:
            # print("here")
            return ll
        if ccsq(current_board)==0 or ccsqq(current_board)==0:
            # print("QQQQQQQQQ")
            return ll

        # for c1 in range(0,8,1):
        #     for c2 in range(0,8,1):
        #         circles+=count_circle[c1][c2]
        #         stars+=count_star[c1][c2]
        #
        # if circles == 0 or stars==0:
        #     return ll

        if moves_left(player,current_board)==0 :
            if passC>0 and passS>0:
                #nodes+=1
                return ll
            if player=="Circle":
                nodes+=1
                passC+=1
                lm=deepcopy(lo)
                lm.append([-1,-1,-1,-1])
                # print (lm)
                # print("-----")
                return alphabeta(current_board,depthLimit-1,"Star",lm,alpha, beta)
            else:
                nodes+=1
                passS+=1
                lm = deepcopy(lo)
                # print(lm)
                # print("-----")
                return alphabeta(current_board, depthLimit - 1, "Circle", lm, alpha, beta)


        best_utility_array = []

        if depthLimit > 0:
            # print("here---")

            if player == "Circle" and moves_left(player,current_board)==1:
                # print("here---")
                for i in range(0, 8, 1):
                    for j in range(0, 8, 1):
                        if current_board[i][j].startswith("C"):
                            # print(current_board[i][j])
                            # print("here---")
                            if i == 6:
                                # print("here---")

                                #1-1
                                if j-1>=0 and current_board[i + 1][j - 1].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j - 1] = "C"+str(count_circle[i+1][j-1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("10")
                                    lk = []
                                    lk=[i,j,i+1,j-1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("j-1>=0 and current_board[i + 1][j - 1].startswith(C)")
                                    # print(str(alpha)+"111111111"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Star",lm, alpha, beta)# i, j, i+1, j-1)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j - 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                        # for i9 in range(0,5,1):
                                        #     best[i9] = utility[i9]
                                    # print(str(best[1])+"??????????????????"+str(best[2]))
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])

                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                #1-2
                                if j-1>=0 and current_board[i + 1][j - 1] == "0":
                                    nodes+=1
                                    update_board = deepcopy(current_board)
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j - 1] = "C1"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("8")
                                    lk = []
                                    lk=[i,j,i+1,j-1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j-1>=0 and current_board[i + 1][j - 1] == 0")
                                    # print(str(alpha)+"222222222"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta) #i, j, i+1, j-1)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j - 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                        # for i7 in range(0,5,1):
                                        #     best[i7] = utility[i7]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))

                                        # print(str(best[1]) + "??????????????????1")
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])

                                       # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                #1-3
                                if j+1<=7 and current_board[i + 1][j + 1].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j + 1] = "C"+str(count_circle[i+1][j+1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("9")
                                    lk=[]
                                    lk=[i,j,i+1,j+1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+1<=7 and current_board[i + 1][j + 1].startswith(C)")
                                    # print(str(alpha)+"33333333333"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)# i, j, i+1, j+1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j + 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                        # for i8 in range(0,5,1):
                                        #     best[i8] = utility[i8]
                                        # #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                 #   best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))



                                #1-4
                                if j+1<=7 and current_board[i + 1][j + 1] == "0":
                                    nodes+=1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j + 1] = "C1"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("7")
                                    lk=[i,j,i+1,j+1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+1<=7 and current_board[i + 1][j + 1] == 0:")
                                    # print(str(alpha)+"444444444444"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)# i, j, i+1, j+1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j + 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                        # for i6 in range(0,5,1):
                                        #     best[i6] = utility[i6]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i == 5:
                                # print("here---")
                                # 1
                                if j-2>=0 and current_board[i + 1][j - 1]=="S1" and current_board[i + 2][j - 2].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j - 1] -= 1
                                    count_circle[i + 2][j - 2] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j - 1] = "0"
                                    update_board[i + 2][j - 2] = "C"+str(count_circle[i+2][j-2])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("5")
                                    lk=[i,j,i+2,j-2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j-2>=0 and current_board[i + 1][j - 1]==S1 and current_board[i + 2][j - 2].startswith(C)")
                                    # print(str(alpha)+"55555555555555"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)#i, j, i + 2, j - 2)
                                    # print(str(utility)+"{{{{}{}{}}{")
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j - 1] += 1
                                    count_circle[i + 2][j - 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                        # for i4 in range(0, 5, 1):
                                        #     best[i4] = utility[i4]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                # 2
                                if j+2<=7 and current_board[i + 1][j + 1]=="S1" and current_board[i + 2][j + 2].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j + 1] -= 1
                                    count_circle[i + 2][j + 2] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j + 1] = "0"
                                    update_board[i + 2][j + 2] = "C"+str(count_circle[i+2][j+2])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("6")
                                    lk=[i,j,i+2,j+2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+2<=7 and current_board[i + 1][j + 1]==S1 and current_board[i + 2][j + 2].startswith(C)")
                                    # print(str(alpha)+"6666666666"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)#i, j, i + 2, j + 2)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j + 1] += 1
                                    count_circle[i + 2][j + 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                        # for i5 in range(0, 5, 1):
                                        #     best[i5] = utility[i5]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            #2-1
                            if i + 1 <= 7 and j - 1 >= 0 and i!=6:
                                # print("here---!!!!!!!!!!!!!!!!!!!!!"+str(i)+str(j))
                                # print(current_board)
                                if current_board[i + 1][j - 1] == "0":
                                    nodes+=1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board=deepcopy(current_board)
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    # print(count_circle[i][j])
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j - 1] += 1
                                    if count_circle[i][j]==0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C"+str(count_circle[i][j])
                                    update_board[i + 1][j - 1] = "C"+str(count_circle[i+1][j-1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("2")
                                    lk=[i,j,i+1,j-1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i + 1 <= 7 and j - 1 >= 0 and i!=6:")
                                    # print(str(alpha)+"77777777777"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)# i, j, i+1, j-1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j - 1] -= 1
                                    #print(move_value)
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                        # for i31 in range(0,5,1):
                                        #     best[i31] = utility[i31]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    #print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                   # best_utility_array.append(BestUtility(utility[0],utility[1],utility[2],utility[3],utility[4]))

                            #2-2
                            if i + 1 <= 7 and j + 1 <= 7 and i!=6:
                                # print("here---!!!!!!!!!!!!!!!!!!!!!" + str(i) + str(j))
                                # print("here---")
                                if current_board[i + 1][j + 1] == "0":
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board = deepcopy(current_board)
                                    # print("here---")
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j + 1] += 1
                                    if count_circle[i][j]==0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C"+str(count_circle[i][j])
                                    update_board[i + 1][j + 1] = "C"+str(count_circle[i+1][j+1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("1")
                                    lk=[i,j,i+1,j+1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i + 1 <= 7 and j + 1 <= 7 and i!=6:")
                                    # print(str(alpha)+"8888888888"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)#i, j, i+1, j+1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j + 1] -= 1
                                    # print move_value
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                        # for iw in range(0,5,1):
                                        #     best[iw] = utility[iw]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    #print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            #2-3
                            if j - 2 >= 0 and i + 2 <= 7:
                                # print("here---")
                                if current_board[i + 1][j - 1] == "S1" and current_board[i + 2][j - 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j - 1] -= 1
                                    count_circle[i + 2][j - 2] += 1
                                    if count_circle[i][j]==0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C"+str(count_circle[i][j])
                                    update_board[i + 2][j - 2] = "C1"
                                    update_board[i + 1][j - 1] = "0"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("4")
                                    lk=[i,j,i+2,j-2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j - 2 >= 0 and i + 2 <= 7:")
                                    # print(str(alpha)+"9999999999"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)# i, j, i+2, j-2)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j - 1] += 1
                                    count_circle[i + 2][j - 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)

                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                        # for i3 in range(0,5,1):
                                        #     best[i3] = utility[i3]
                                       # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            #2-4
                            if j + 2 <= 7 and i + 2 <= 7:
                                # print("here---")
                                if current_board[i + 1][j + 1] == "S1" and current_board[i + 2][j + 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j + 1] -= 1
                                    count_circle[i + 2][j + 2] += 1

                                    if count_circle[i][j]==0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C"+str(count_circle[i][j])
                                    update_board[i + 2][j + 2] = "C1"
                                    update_board[i+1][j+1] = "0"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    #move_value = evaluate(update_board,"Circle")
                                    # print("3")
                                    lk=[i,j,i+2,j+2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j + 2 <= 7 and i + 2 <= 7:")
                                    # print(str(alpha)+"10101010101010"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)#i, j, i+2, j+2)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j + 1] += 1
                                    count_circle[i + 2][j + 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])

                                        # for i2 in range(0,5,1):
                                        #     best[i2] = utility[i2]
                                        #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3])+"{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                  #  best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))



                # print("here---")
                # print(str(len(best_utility_array))+"---------------------------------------")
                max1 = float('-inf')
                for kk in best_utility_array:
                    if kk[0] > max1:
                        max1 = kk[0]
                ft = []
                for kk in best_utility_array:
                    if (kk[0] == max1):
                        ft.append(kk)
                minx = float('inf')
                for kk in ft:
                    if kk[2][0][2] < minx:
                        minx = kk[2][0][2]
                ad = []
                for kk in ft:
                    if kk[2][0][2] == minx:
                        ad.append(kk)
                miny = float('inf')
                for kk in ad:
                    if kk[2][0][3] < miny:
                        miny = kk[2][0][3]
                ad2 = []
                for kk in ad:
                    if kk[2][0][3] == miny:
                        ad2.append(kk)
                        # print(miny)
                        # print("+++++++++++++++++++++++++++")
                best = deepcopy(ad2[0])
                # for f in best_utility_array:
                #     print("abcd")
                #     print(f.best_value)
                #     print(f.best_final_row)
                #     print(f.best_final_column)
                return best

            elif player=="Circle" and moves_left(player,current_board)==0:
                ll = []
                ll.append(evaluate(current_board, player))

                ll.append(nodes)
                ll.append(lo)
                return ll


            if player == "Star" and moves_left(player,current_board)==1:
                # print("===========")
                # print(best[0])
                for i in range(0, 8, 1):
                    for j in range(0, 8, 1):
                        if current_board[i][j].startswith("S"):
                            # print(current_board)
                            # print("||||||||||||||")
                                        #1-1
                            if i==1:
                                if i-1>=0 and j-1>=0 and current_board[i - 1][j - 1].startswith("S"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j - 1] += 1
                                    update_board[i][j]="0"
                                    update_board[i - 1][j - 1]="S"+str(count_star[i-1][j-1])
                                    # print("===========!!!!!!!!!!****")
                                    # print(update_board)
                                    #print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("10")
                                    lk=[i,j,i-1,j-1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j-1>=0 and current_board[i - 1][j - 1].startswith(S):")
                                    # print(str(alpha)+"121211212112122112"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)# i, j, i-1, j-1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j - 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                        # for i21 in range(0,5,1):
                                        #     best[i21] = utility[i21]
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                #1-2
                                if i-1>=0 and j-1>=0 and current_board[i - 1][j - 1] == "0":
                                    # print(current_board)
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j - 1]="S1"
                                    # print("===========!!!!!!!!!!***")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("8")
                                    lk=[i,j,i-1,j-1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j-1>=0 and current_board[i - 1][j - 1] == 0:")
                                    # print(str(alpha)+"1313131131311313113"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)# i, j, i-1, j-1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j - 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                #1-3
                                if i-1>=0 and j+1<=7 and current_board[i - 1][j + 1].startswith("S"):
                                    # print("aaaaaaaa")
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board=deepcopy(current_board)
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j + 1]="S"+str(count_star[i-1][j+1])
                                    # print("===========!!!!!!!!!!**")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("9")
                                    lk=[i,j,i-1,j+1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j+1<=7 and current_board[i - 1][j + 1].startswith(S):")
                                    # print(str(alpha)+"141414141"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)# i, j, i-1, j+1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j + 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                        # for i19 in range(0,5,1):
                                        #     best[i19] = utility[i19]
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                #1-4
                                if i-1>=0 and j+1<=7 and current_board[i - 1][j + 1] == "0":
                                    # print(current_board)
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i-1][j+1]="S1"

                                    # print("===========!!!!!!!!!!*"+str(i)+" "+str(j))
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("7")
                                    lk=[i,j,i-1,j+1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j+1<=7 and current_board[i - 1][j + 1] == 0")
                                    # print(str(alpha)+"1515151"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)# i, j, i-1, j+1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j + 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                        # for i17 in range(0,5,1):
                                        #     best[i17] = utility[i17]
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i == 2:
                                if j-2>=0 and current_board[i - 1][j - 1] == "C1" and current_board[i - 2][j - 2].startswith("S"):
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board=deepcopy(current_board)
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j - 1] -= 1
                                    count_star[i - 2][j - 2] += 1
                                    update_board[i][j]="0"
                                    update_board[i-1][j-1]="0"
                                    update_board[i - 2][j - 2]="S"+str(count_star[i-2][j-2])
                                    # print("===========!!!!!!!!!!---------")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("5")
                                    lk=[i,j,i-2,j-2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j-2>=0 and current_board[i - 1][j - 1] == C1 and current_board[i - 2][j - 2].startswith(S):")
                                    # print(str(alpha)+"161616116"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)#i, j, i-2, j-2)
                                    # print(str(utility[0])+"|}|}|}|}|")
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j - 1] += 1
                                    count_star[i - 2][j - 2] -= 1
                                    # print(utility[0])
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        # print(":::::::::")
                                        # print(utility[0])
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])

                                        # for i15 in range(0,5,1):
                                        #     best[i15] = utility[i15]
                                    #best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                if j+2<=7 and current_board[i - 1][j + 1] == "C1" and current_board[i - 2][j + 2].startswith("S"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j + 1] -= 1
                                    count_star[i - 2][j + 2] += 1
                                    update_board[i][j]="0"
                                    update_board[i-1][j+1]="0"
                                    update_board[i - 2][j + 2]="S"+str(count_star[i-2][j+2])
                                    # print("===========!!!!!!!!!!----------")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("6")
                                    lk=[i,j,i-2,j+2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+2<=7 and current_board[i - 1][j + 1] == C1 and current_board[i - 2][j + 2].startswith(S):")
                                    # print(str(alpha)+"17171717171"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)#i, j, i-2, j+2)
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j + 1] += 1
                                    count_star[i - 2][j + 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                        # for i16 in range(0,5,1):
                                        #     best[i16] = utility[i16]
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 2 >= 0 and j - 2 >= 0 and i!=1:
                                if current_board[i - 1][j - 1] == "C1" and current_board[i - 2][j - 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j - 1] -= 1
                                    count_star[i - 2][j - 2] += 1
                                    if count_star[i][j]==0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S"+str(count_star[i][j])

                                    update_board[i][j]="0"
                                    update_board[i-1][j-1]="0"
                                    update_board[i - 2][j - 2]="S1"
                                    # print("===========!!!!!!!!!!@")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("4")
                                    lk=[i,j,i-2,j-2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 2 >= 0 and j - 2 >= 0 and i!=1:")
                                    # print(str(alpha)+"18181811818"+str(beta))
                                    utility=deepcopy(alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)) # i, j, i-2, j-2))
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j - 1] += 1
                                    count_star[i - 2][j - 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                        # for i14 in range(0,5,1):
                                        #     best[i14] = utility[i14]
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 2 >= 0 and j + 2 <= 7 and i!=1:
                                if current_board[i - 1][j + 1] == "C1" and current_board[i - 2][j + 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j + 1] -= 1
                                    count_star[i - 2][j + 2] += 1
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])
                                    update_board[i-1][j+1]="0"
                                    update_board[i - 2][j + 2]="S1"
                                    # print("===========!!!!!!!!!!#")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("3")
                                    lk=[i,j,i-2,j+2]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 2 >= 0 and j + 2 <= 7 and i!=1:")
                                    # print(str(alpha)+"191919191919"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)#i, j, i-2, j+2)
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j + 1] += 1
                                    count_star[i - 2][j + 2] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                        # for i13 in range(0,5,1):
                                        #     best[i13] = utility[i13]
                                    # print(str(best[0]) + "{{{{{{{{{{{{")
                                   # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 1 >= 0 and j - 1 >= 0 and i!=1:
                                if current_board[i - 1][j - 1] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j - 1] += 1
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])
                                    update_board[i - 1][j - 1]="S1"
                                    # print("===========!!!!!!!!!!$")
                                    # print(update_board)
                                    # print(current_board)
                                    #move_value = evaluate(update_board,"Star")
                                    # print("2")
                                    lk=[i,j,i-1,j-1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 1 >= 0 and j - 1 >= 0 and i!=1:")
                                    # print(str(alpha)+"20202020"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)# i, j, i-1, j-1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j - 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                        # for i12 in range(0,5,1):
                                        #     best[i12] = utility[i12]
                                    # print(str(best[0]) + "{{{{{{{{{{{{")
                                    # print(best[i])
                                    #best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 1 >= 0 and j + 1 <= 7 and i!=1:
                                if current_board[i - 1][j + 1] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # print(str(i) + " " + str(j))
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j + 1] += 1
                                    # print(update_board)
                                    # print(str(i-1)+" "+str(j+1))
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])
                                    update_board[i-1][j+1]="S1"

                                    # print(update_board)
                                    # print(current_board)
                                    lk=[i,j,i-1,j+1]
                                    lm=deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 1 >= 0 and j + 1 <= 7 and i!=1:")
                                    # print(str(alpha)+"2121"+str(beta))
                                    utility=alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)#i, j, i-1, j+1)
                                    # print("===========!!!!!!!!!!^" + str(utility))
                                    count_star[i][j] += 1
                                    count_star[i - 1][j + 1] -= 1
                                    if utility[0] > best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]>=beta:
                                        return utility
                                    if alpha < utility[0]:
                                        alpha=deepcopy(utility[0])


                                        # for i11 in range(0,5,1):
                                        #     best[i11] = utility[i11]
                                    # print(str(best[0])+"{{{{{{{{{{{{")
                                    #best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                # print("abcd--1111")
                # for f in best_utility_array:
                #     print("abcd--1111")
                #     print(f.best_value)
                max1=float('-inf')
                for kk in best_utility_array:
                    if kk[0]>max1:
                        max1=kk[0]
                ft=[]
                for kk in best_utility_array:
                    if(kk[0]==max1):
                        ft.append(kk)
                minx=float('inf')
                for kk in ft:
                    if kk[2][0][2]<minx:
                        minx=kk[2][0][2]
                ad=[]
                for kk in ft:
                    if kk[2][0][2] == minx:
                        ad.append(kk)
                miny = float('inf')
                for kk in ad:
                    if kk[2][0][3] < miny:
                        miny = kk[2][0][3]
                ad2 = []
                for kk in ad:
                    if kk[2][0][3] == miny:
                        ad2.append(kk)
                        # print(miny)
                        # print("+++++++++++++++++++++++++++")
                best=deepcopy(ad2[0])


            elif player == "Star" and moves_left(player,current_board) == 0:
                ll = []
                ll.append(evaluate(current_board))

                # ll.append(initial_row)
                # ll.append(initial_column)
                # ll.append(final_row)
                # ll.append(final_column)
                ll.append(nodes)
                ll.append(lo)
                return ll



        # print(str(len(best_utility_array)) + "---------------------------------------)))))"+str(best[1])+str(best[2]))
        return best

    else:
        best[0]=float('inf')
        ll = []
        ll.append(evaluate(current_board))

        # ll.append(initial_row)
        # ll.append(initial_column)
        # ll.append(final_row)
        # ll.append(final_column)
        ll.append(nodes)
        ll.append(lo)
        if depthLimit == 0:
            # print("here")
            return ll
        if ccsq(current_board) == 0 or ccsqq(current_board) == 0:
            # print("QQQQQQQQQ")
            return ll

        # for c1 in range(0,8,1):
        #     for c2 in range(0,8,1):
        #         circles+=count_circle[c1][c2]
        #         stars+=count_star[c1][c2]
        #
        # if circles == 0 or stars==0:
        #     return ll

        if moves_left(player, current_board) == 0:
            if passC > 0 and passS > 0:
                # nodes+=1
                return ll
            if player == "Circle":
                nodes += 1
                passC += 1
                lm = deepcopy(lo)
                lm.append([-1,-1,-1,-1])
                # print (lm)
                # print("-----")
                return alphabeta(current_board, depthLimit - 1, "Star", lm, alpha, beta)
            else:
                nodes += 1
                passS += 1
                lm = deepcopy(lo)
                # print(lm)
                # print("-----")
                return alphabeta(current_board, depthLimit - 1, "Circle", lm, alpha, beta)

        best_utility_array = []

        if depthLimit > 0:
            # print("here---")

            if player == "Circle" and moves_left(player, current_board) == 1:
                # print("here---")
                for i in range(0, 8, 1):
                    for j in range(0, 8, 1):
                        if current_board[i][j].startswith("C"):
                            # print(current_board[i][j])
                            # print("here---")
                            if i == 6:
                                # print("here---")

                                # 1-1
                                if j - 1 >= 0 and current_board[i + 1][j - 1].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j - 1] = "C" + str(count_circle[i + 1][j - 1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("10")
                                    lk = []
                                    lk = [i, j, i + 1, j - 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("j-1>=0 and current_board[i + 1][j - 1].startswith(C)")
                                    # print(str(alpha)+"22"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)  # i, j, i+1, j-1)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j - 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                        # for i9 in range(0,5,1):
                                        #     best[i9] = utility[i9]
                                    # print(str(best[1]) + "??????????????????" + str(best[2]))
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                # 1-2
                                if j - 1 >= 0 and current_board[i + 1][j - 1] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j - 1] = "C1"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("8")
                                    lk = []
                                    lk = [i, j, i + 1, j - 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j-1>=0 and current_board[i + 1][j - 1] == 0")
                                    # print(str(alpha)+"23"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)  # i, j, i+1, j-1)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j - 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                        # for i7 in range(0,5,1):
                                        #     best[i7] = utility[i7]
                                        # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))

                                        # print(str(best[1]) + "??????????????????1")
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])

                                    # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                # 1-3
                                if j + 1 <= 7 and current_board[i + 1][j + 1].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j + 1] = "C" + str(count_circle[i + 1][j + 1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("9")
                                    lk = []
                                    lk = [i, j, i + 1, j + 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+1<=7 and current_board[i + 1][j + 1].startswith(C)")
                                    # print(str(alpha)+"24"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)  # i, j, i+1, j+1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j + 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                        # for i8 in range(0,5,1):
                                        #     best[i8] = utility[i8]
                                        # #best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}" + str(best[4]))
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > best[0]:
                                        beta=deepcopy(utility[0])


                                #   best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                # 1-4
                                if j + 1 <= 7 and current_board[i + 1][j + 1] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j + 1] = "C1"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("7")
                                    lk = [i, j, i + 1, j + 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j+1<=7 and current_board[i + 1][j + 1] == 0:")
                                    # print(str(alpha)+"25"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)  # i, j, i+1, j+1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j + 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                        # for i6 in range(0,5,1):
                                        #     best[i6] = utility[i6]
                                        # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}" + str(best[4]))
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i == 5:
                                # print("here---")
                                # 1
                                if j - 2 >= 0 and current_board[i + 1][j - 1] == "S1" and current_board[i + 2][
                                    j - 2].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j - 1] -= 1
                                    count_circle[i + 2][j - 2] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j - 1] = "0"
                                    update_board[i + 2][j - 2] = "C" + str(count_circle[i + 2][j - 2])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("5")
                                    lk = [i, j, i + 2, j - 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print(
                                    #     "if j-2>=0 and current_board[i + 1][j - 1]==S1 and current_board[i + 2][j - 2].startswith(C)")
                                    # print(str(alpha)+"26"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)  # i, j, i + 2, j - 2)
                                    # print(str(utility) + "{{{{}{}{}}{")
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j - 1] += 1
                                    count_circle[i + 2][j - 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                        # for i4 in range(0, 5, 1):
                                        #     best[i4] = utility[i4]
                                        # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}" + str(best[4]))
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                # 2
                                if j + 2 <= 7 and current_board[i + 1][j + 1] == "S1" and current_board[i + 2][
                                    j + 2].startswith("C"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j + 1] -= 1
                                    count_circle[i + 2][j + 2] += 1
                                    update_board[i][j] = "0"
                                    update_board[i + 1][j + 1] = "0"
                                    update_board[i + 2][j + 2] = "C" + str(count_circle[i + 2][j + 2])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("6")
                                    lk = [i, j, i + 2, j + 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print(
                                    #     "if j+2<=7 and current_board[i + 1][j + 1]==S1 and current_board[i + 2][j + 2].startswith(C)")
                                    # print(str(alpha)+"27"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)  # i, j, i + 2, j + 2)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j + 1] += 1
                                    count_circle[i + 2][j + 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                        # for i5 in range(0, 5, 1):
                                        #     best[i5] = utility[i5]
                                        # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}" + str(best[4]))
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > best[0]:
                                        beta=deepcopy(utility[0])


                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            # 2-1
                            if i + 1 <= 7 and j - 1 >= 0 and i != 6:
                                # print("here---!!!!!!!!!!!!!!!!!!!!!" + str(i) + str(j))
                                # print(current_board)
                                if current_board[i + 1][j - 1] == "0":
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board = deepcopy(current_board)
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    # print(count_circle[i][j])
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j - 1] += 1
                                    if count_circle[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C" + str(count_circle[i][j])
                                    update_board[i + 1][j - 1] = "C" + str(count_circle[i + 1][j - 1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("2")
                                    lk = [i, j, i + 1, j - 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i + 1 <= 7 and j - 1 >= 0 and i!=6:")
                                    # print(str(alpha)+"28"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)  # i, j, i+1, j-1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j - 1] -= 1
                                    # print(move_value)
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                    # for i31 in range(0,5,1):
                                    #     best[i31] = utility[i31]
                                    # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                # best_utility_array.append(BestUtility(utility[0],utility[1],utility[2],utility[3],utility[4]))

                            # 2-2
                            if i + 1 <= 7 and j + 1 <= 7 and i != 6:
                                # print("here---!!!!!!!!!!!!!!!!!!!!!" + str(i) + str(j))
                                # print("here---")
                                if current_board[i + 1][j + 1] == "0":
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board = deepcopy(current_board)
                                    # print("here---")
                                    count_circle[i][j] -= 1
                                    count_circle[i + 1][j + 1] += 1
                                    if count_circle[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C" + str(count_circle[i][j])
                                    update_board[i + 1][j + 1] = "C" + str(count_circle[i + 1][j + 1])
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("1")
                                    lk = [i, j, i + 1, j + 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i + 1 <= 7 and j + 1 <= 7 and i!=6:")
                                    # print(str(alpha)+"29"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)  # i, j, i+1, j+1)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_circle[i + 1][j + 1] -= 1
                                    # print move_value
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                    # for iw in range(0,5,1):
                                    #     best[iw] = utility[iw]
                                    # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}"+str(best[4]))
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            # 2-3
                            if j - 2 >= 0 and i + 2 <= 7:
                                # print("here---")
                                if current_board[i + 1][j - 1] == "S1" and current_board[i + 2][j - 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j - 1] -= 1
                                    count_circle[i + 2][j - 2] += 1
                                    if count_circle[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C" + str(count_circle[i][j])
                                    update_board[i + 2][j - 2] = "C1"
                                    update_board[i + 1][j - 1] = "0"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("4")
                                    lk = [i, j, i + 2, j - 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j - 2 >= 0 and i + 2 <= 7:")
                                    # print(str(alpha)+"30"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)  # i, j, i+2, j-2)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j - 1] += 1
                                    count_circle[i + 2][j - 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)

                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                    # for i3 in range(0,5,1):
                                    #     best[i3] = utility[i3]
                                    # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}" + str(best[4]))
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            # 2-4
                            if j + 2 <= 7 and i + 2 <= 7:
                                # print("here---")
                                if current_board[i + 1][j + 1] == "S1" and current_board[i + 2][j + 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_circle[i][j] -= 1
                                    count_star[i + 1][j + 1] -= 1
                                    count_circle[i + 2][j + 2] += 1

                                    if count_circle[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "C" + str(count_circle[i][j])
                                    update_board[i + 2][j + 2] = "C1"
                                    update_board[i + 1][j + 1] = "0"
                                    # print("---------UPDATED BOARD----------")
                                    # print(update_board)
                                    # move_value = evaluate(update_board,"Circle")
                                    # print("3")
                                    lk = [i, j, i + 2, j + 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if j + 2 <= 7 and i + 2 <= 7:")
                                    # print(str(alpha)+"31"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Star", lm, alpha, beta)  # i, j, i+2, j+2)
                                    # print(utility)
                                    count_circle[i][j] += 1
                                    count_star[i + 1][j + 1] += 1
                                    count_circle[i + 2][j + 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])

                                    # for i2 in range(0,5,1):
                                    #     best[i2] = utility[i2]
                                    # best_utility_array.append(BestUtility(best[0], best[1], best[2], best[3], best[4]))
                                    # print(str(best[3]) + "{{{{{{{{{{}}}}}}}}" + str(best[4]))
                                #  best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                # print("here---")
                # print(str(len(best_utility_array)) + "---------------------------------------")
                max1 = float('-inf')
                for kk in best_utility_array:
                    if kk[0] > max1:
                        max1 = kk[0]
                ft = []
                for kk in best_utility_array:
                    if (kk[0] == max1):
                        ft.append(kk)
                minx = float('inf')
                for kk in ft:
                    if kk[2][0][2] < minx:
                        minx = kk[2][0][2]
                ad = []
                for kk in ft:
                    if kk[2][0][2] == minx:
                        ad.append(kk)
                miny = float('inf')
                for kk in ad:
                    if kk[2][0][3] < miny:
                        miny = kk[2][0][3]
                ad2 = []
                for kk in ad:
                    if kk[2][0][3] == miny:
                        ad2.append(kk)
                        # print(miny)
                        # print("+++++++++++++++++++++++++++")
                best = deepcopy(ad2[0])
                # for f in best_utility_array:
                #     print("abcd")
                #     print(f.best_value)
                #     print(f.best_final_row)
                #     print(f.best_final_column)
                return best

            elif player == "Circle" and moves_left(player, current_board) == 0:
                ll = []
                ll.append(evaluate(current_board, player))

                ll.append(nodes)
                ll.append(lo)
                return ll

            if player == "Star" and moves_left(player, current_board) == 1:
                # print("===========")
                # print(best[0])
                for i in range(0, 8, 1):
                    for j in range(0, 8, 1):
                        if current_board[i][j].startswith("S"):
                            # print(current_board)
                            # print("||||||||||||||")
                            # 1-1
                            if i == 1:
                                if i - 1 >= 0 and j - 1 >= 0 and current_board[i - 1][j - 1].startswith("S"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j - 1] = "S" + str(count_star[i - 1][j - 1])
                                    # print("===========!!!!!!!!!!****")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("10")
                                    lk = [i, j, i - 1, j - 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j-1>=0 and current_board[i - 1][j - 1].startswith(S):")
                                    # print(str(alpha)+"32"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)  # i, j, i-1, j-1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j - 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                    # for i21 in range(0,5,1):
                                    #     best[i21] = utility[i21]
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                # 1-2
                                if i - 1 >= 0 and j - 1 >= 0 and current_board[i - 1][j - 1] == "0":
                                    # print(current_board)
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j - 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j - 1] = "S1"
                                    # print("===========!!!!!!!!!!***")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("8")
                                    lk = [i, j, i - 1, j - 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j-1>=0 and current_board[i - 1][j - 1] == 0:")
                                    # print(str(alpha)+"33"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)  # i, j, i-1, j-1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j - 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                # 1-3
                                if i - 1 >= 0 and j + 1 <= 7 and current_board[i - 1][j + 1].startswith("S"):
                                    # print("aaaaaaaa")
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board = deepcopy(current_board)
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j + 1] = "S" + str(count_star[i - 1][j + 1])
                                    # print("===========!!!!!!!!!!**")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("9")
                                    lk = [i, j, i - 1, j + 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j+1<=7 and current_board[i - 1][j + 1].startswith(S):")
                                    # print(str(alpha)+"34"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)  # i, j, i-1, j+1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j + 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                    # for i19 in range(0,5,1):
                                    #     best[i19] = utility[i19]
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                                # 1-4
                                if i - 1 >= 0 and j + 1 <= 7 and current_board[i - 1][j + 1] == "0":
                                    # print(current_board)
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j + 1] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j + 1] = "S1"

                                    # print("===========!!!!!!!!!!*" + str(i) + " " + str(j))
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("7")
                                    lk = [i, j, i - 1, j + 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i-1>=0 and j+1<=7 and current_board[i - 1][j + 1] == 0")
                                    # print(str(alpha)+"35"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)  # i, j, i-1, j+1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j + 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                    # for i17 in range(0,5,1):
                                    #     best[i17] = utility[i17]
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i == 2:
                                if j - 2 >= 0 and current_board[i - 1][j - 1] == "C1" and current_board[i - 2][j - 2].startswith("S"):
                                    nodes += 1
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    update_board = deepcopy(current_board)
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j - 1] -= 1
                                    count_star[i - 2][j - 2] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j - 1] = "0"
                                    update_board[i - 2][j - 2] = "S" + str(count_star[i - 2][j - 2])
                                    # print("===========!!!!!!!!!!---------")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("5")
                                    lk = [i, j, i - 2, j - 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print(
                                    #     "if j-2>=0 and current_board[i - 1][j - 1] == C1 and current_board[i - 2][j - 2].startswith(S):")
                                    # print(str(alpha)+"36"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)  # i, j, i-2, j-2)
                                    # print(str(utility[0]) + "|}|}|}|}|")
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j - 1] += 1
                                    count_star[i - 2][j - 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        # print("_)_)_)")
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])

                                    # for i15 in range(0,5,1):
                                    #     best[i15] = utility[i15]
                                    # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                                if j + 2 <= 7 and current_board[i - 1][j + 1] == "C1" and current_board[i - 2][
                                    j + 2].startswith("S"):
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j + 1] -= 1
                                    count_star[i - 2][j + 2] += 1
                                    update_board[i][j] = "0"
                                    update_board[i - 1][j + 1] = "0"
                                    update_board[i - 2][j + 2] = "S" + str(count_star[i - 2][j + 2])
                                    # print("===========!!!!!!!!!!----------")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("6")
                                    lk = [i, j, i - 2, j + 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print(
                                    #     "if j+2<=7 and current_board[i - 1][j + 1] == C1 and current_board[i - 2][j + 2].startswith(S):")
                                    # print(str(alpha)+"37"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)  # i, j, i-2, j+2)
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j + 1] += 1
                                    count_star[i - 2][j + 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                    # for i16 in range(0,5,1):
                                    #     best[i16] = utility[i16]
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 2 >= 0 and j - 2 >= 0 and i != 1:
                                if current_board[i - 1][j - 1] == "C1" and current_board[i - 2][j - 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j - 1] -= 1
                                    count_star[i - 2][j - 2] += 1
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])

                                    update_board[i][j] = "0"
                                    update_board[i - 1][j - 1] = "0"
                                    update_board[i - 2][j - 2] = "S1"
                                    # print("===========!!!!!!!!!!@")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("4")
                                    lk = [i, j, i - 2, j - 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 2 >= 0 and j - 2 >= 0 and i!=1:")
                                    # print(str(alpha)+"38"+str(beta))
                                    utility = deepcopy(
                                        alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta))  # i, j, i-2, j-2))
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j - 1] += 1
                                    count_star[i - 2][j - 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                    # for i14 in range(0,5,1):
                                    #     best[i14] = utility[i14]
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 2 >= 0 and j + 2 <= 7 and i != 1:
                                if current_board[i - 1][j + 1] == "C1" and current_board[i - 2][j + 2] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_circle[i - 1][j + 1] -= 1
                                    count_star[i - 2][j + 2] += 1
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])
                                    update_board[i - 1][j + 1] = "0"
                                    update_board[i - 2][j + 2] = "S1"
                                    # print("===========!!!!!!!!!!#")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("3")
                                    lk = [i, j, i - 2, j + 2]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 2 >= 0 and j + 2 <= 7 and i!=1:")
                                    # print(str(alpha)+"39"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)  # i, j, i-2, j+2)
                                    count_star[i][j] += 1
                                    count_circle[i - 1][j + 1] += 1
                                    count_star[i - 2][j + 2] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                    # for i13 in range(0,5,1):
                                    #     best[i13] = utility[i13]
                                    # print(str(best[0]) + "{{{{{{{{{{{{")
                                # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 1 >= 0 and j - 1 >= 0 and i != 1:
                                if current_board[i - 1][j - 1] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j - 1] += 1
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])
                                    update_board[i - 1][j - 1] = "S1"
                                    # print("===========!!!!!!!!!!$")
                                    # print(update_board)
                                    # print(current_board)
                                    # move_value = evaluate(update_board,"Star")
                                    # print("2")
                                    lk = [i, j, i - 1, j - 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 1 >= 0 and j - 1 >= 0 and i!=1:")
                                    # print(str(alpha)+"40"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)  # i, j, i-1, j-1)
                                    count_star[i][j] += 1
                                    count_star[i - 1][j - 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                    # for i12 in range(0,5,1):
                                    #     best[i12] = utility[i12]
                                    # print(str(best[0]) + "{{{{{{{{{{{{")
                                    # print(best[i])
                                    # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))

                            if i - 1 >= 0 and j + 1 <= 7 and i != 1:
                                if current_board[i - 1][j + 1] == "0":
                                    nodes += 1
                                    update_board = deepcopy(current_board)
                                    # print(str(i) + " " + str(j))
                                    # for i1 in range(0, 8, 1):
                                    #     for j1 in range(0, 8, 1):
                                    #         update_board[i1][j1] = current_board[i1][j1]
                                    count_star[i][j] -= 1
                                    count_star[i - 1][j + 1] += 1
                                    # print(update_board)
                                    # print(str(i - 1) + " " + str(j + 1))
                                    if count_star[i][j] == 0:
                                        update_board[i][j] = "0"
                                    else:
                                        update_board[i][j] = "S" + str(count_star[i][j])
                                    update_board[i - 1][j + 1] = "S1"

                                    # print(update_board)
                                    # print(current_board)
                                    lk = [i, j, i - 1, j + 1]
                                    lm = deepcopy(lo)
                                    lm.append(lk)
                                    # print(lm)
                                    # print("if i - 1 >= 0 and j + 1 <= 7 and i!=1:")
                                    # print(str(alpha)+"41"+str(beta))
                                    utility = alphabeta(update_board, depthLimit - 1, "Circle", lm, alpha, beta)  # i, j, i-1, j+1)
                                    # print("===========!!!!!!!!!!^" + str(utility))
                                    count_star[i][j] += 1
                                    count_star[i - 1][j + 1] -= 1
                                    if utility[0] < best[0]:
                                        best = deepcopy(utility)
                                    best_utility_array.append(deepcopy(utility))
                                    if utility[0]<=alpha:
                                        return utility
                                    if beta > utility[0]:
                                        beta=deepcopy(utility[0])


                                    # for i11 in range(0,5,1):
                                    #     best[i11] = utility[i11]
                                    # print(str(best[0]) + "{{{{{{{{{{{{")
                                    # best_utility_array.append(BestUtility(utility[0], utility[1], utility[2], utility[3], utility[4]))
                # print("abcd--1111")
                # for f in best_utility_array:
                #     print("abcd--1111")
                #     print(f.best_value)
                max1 = float('-inf')
                for kk in best_utility_array:
                    if kk[0] > max1:
                        max1 = kk[0]
                ft = []
                for kk in best_utility_array:
                    if (kk[0] == max1):
                        ft.append(kk)
                minx = float('inf')
                for kk in ft:
                    if kk[2][0][2] < minx:
                        minx = kk[2][0][2]
                ad = []
                for kk in ft:
                    if kk[2][0][2] == minx:
                        ad.append(kk)
                miny = float('inf')
                for kk in ad:
                    if kk[2][0][3] < miny:
                        miny = kk[2][0][3]
                ad2 = []
                for kk in ad:
                    if kk[2][0][3] == miny:
                        ad2.append(kk)
                        # print(miny)
                        # print("+++++++++++++++++++++++++++")
                best = deepcopy(ad2[0])


            elif player == "Star" and moves_left(player, current_board) == 0:
                ll = []
                ll.append(evaluate(current_board))

                # ll.append(initial_row)
                # ll.append(initial_column)
                # ll.append(final_row)
                # ll.append(final_column)
                ll.append(nodes)
                ll.append(lo)
                return ll

        # print(str(len(best_utility_array)) + "---------------------------------------)))))" + str(best[1]) + str(
        #     best[2]))
        return best








# ALPHABETA
if algorithm == "ALPHABETA":
    yt=[]
    farsighted_utility = alphabeta(current_board, depthLimit, player, yt, float('-inf'), float('inf'))
    # print("farsighted utility")
    # print(farsighted_utility)
    # print(current_board)
    # print(evaluate(current_board))
    # print("------------")
    w, h = 8, 8;
    myopic_board = [[0 for x in range(w)] for y in range(h)]
    for i in range(0,8,1):
        for j in range(0,8,1):
            myopic_board[i][j] = current_board[i][j]
    # print(myopic_board)



    yy=farsighted_utility[2][0];
    # print(yy)
    if player=="Star":
        count_star=ccs(current_board)
        count_circle = ccs2(current_board)
        count_star[yy[0]][yy[1]] -= 1
        count_star[yy[2]][yy[3]] += 1

        if yy[0]-yy[2] == 2:
            if yy[1]-yy[3] == 2:
                count_circle[yy[0]-1][yy[1]-1]-=1
                myopic_board[yy[0]-1][yy[1]-1]="0"
            if yy[1]-yy[3] == -2:
                count_circle[yy[0]-1][yy[1]+1]-=1
                myopic_board[yy[0]-1][yy[1]+1]="0"

        if count_star[yy[0]][yy[1]] == 0:
            myopic_board[yy[0]][yy[1]] = "0"

        if count_star[yy[0]][yy[1]] != 0:
            # print(",,,,,,,,,,")
            myopic_board[yy[0]][yy[1]] = "S"+str(count_star[yy[0]][yy[1]])

        myopic_board[yy[2]][yy[3]] = "S"+str(count_star[yy[2]][yy[3]])


    if player=="Circle":
        count_star = ccs(current_board)
        count_circle = ccs2(current_board)
        count_circle[yy[0]][yy[1]] -= 1
        count_circle[yy[2]][yy[3]] += 1

        if yy[0]-yy[2] == -2:
            if yy[1]-yy[3] == 2:
                count_star[yy[0]+1][yy[1]-1]-=1
                myopic_board[yy[0]+1][yy[1]-1]="0"
            if yy[1]-yy[3] == -2:
                count_star[yy[0]+1][yy[1]+1]-=1
                myopic_board[yy[0]+1][yy[1]+1]="0"


        if count_circle[yy[0]][yy[1]] == 0:
            myopic_board[yy[0]][yy[1]] = "0"
        if count_circle[yy[0]][yy[1]] != 0:
            myopic_board[yy[0]][yy[1]] = "C" + str(count_circle[yy[0]][yy[1]])
        myopic_board[yy[2]][yy[3]] = "C"+str(count_circle[yy[2]][yy[3]])


    if yy[0] == -1 and yy[1] == -1 and yy[2] == -1 and yy[3] == -1:
        myopic_board = deepcopy(current_board)
    # if passS>0 or passC>0:
    #     myopic_board = deepcopy(current_board)
    # print("Myopic Board")
    # print(myopic_board)
    myopic_value = evaluate(myopic_board)
    # print("Myopic Value")
    # print(myopic_value)



    if yy[0] == 0:
        yy[0] = "H"
    if yy[0] == 1:
        yy[0] = "G"
    if yy[0] == 2:
        yy[0] = "F"
    if yy[0] == 3:
        yy[0] = "E"
    if yy[0] == 4:
        yy[0] = "D"
    if yy[0] == 5:
        yy[0] = "C"
    if yy[0] == 6:
        yy[0] = "B"
    if yy[0] == 7:
        yy[0] = "A"

    if yy[2] == 0:
        yy[2] = "H"
    if yy[2] == 1:
        yy[2] = "G"
    if yy[2] == 2:
        yy[2] = "F"
    if yy[2] == 3:
        yy[2] = "E"
    if yy[2] == 4:
        yy[2] = "D"
    if yy[2] == 5:
        yy[2] = "C"
    if yy[2] == 6:
        yy[2] = "B"
    if yy[2] == 7:
        yy[2] = "A"

    yy[1]+=1
    yy[3]+=1

    # print(yy)
    # print(nodes)
    # print(farsighted_utility)
    # print("-----------------------------------------")
    # print(evaluate(current_board))
    with open('output.txt', 'w') as the_file:
        if yy[0]== -1 or yy[1] == -1 or yy[2] == -1 or yy[3] == -1:
            the_file.write("pass")
        else:
            the_file.write(yy[0])
            the_file.write(str(yy[1]))
            the_file.write("-")
            the_file.write(yy[2])
            the_file.write(str(yy[3]))
        the_file.write('\n')
        the_file.write(str(myopic_value))
        the_file.write('\n')
        the_file.write(str(farsighted_utility[0]))
        the_file.write('\n')
        the_file.write(str(nodes))
    the_file.close()



# MINIMAX
if algorithm == "MINIMAX":
    yt=[]
    farsighted_utility = minimax(current_board, depthLimit, player, yt)
    # print("farsighted utility")
    # print(farsighted_utility)
    # print(current_board)
    # print(evaluate(current_board))
    # print("------------")
    w, h = 8, 8;
    myopic_board = [[0 for x in range(w)] for y in range(h)]
    for i in range(0,8,1):
        for j in range(0,8,1):
            myopic_board[i][j] = current_board[i][j]
    #    print(myopic_board)
    yy=farsighted_utility[2][0];
    #    print(yy)
    # if player=="Star":
    #     count_star[yy[0]][yy[1]] -= 1
    #     count_star[yy[2]][yy[3]] += 1
    #
    #     if yy[0]-yy[2] == 2:
    #         if yy[1]-yy[3] == 2:
    #             count_circle[yy[0]-1][yy[1]-1]-=1
    #             myopic_board[yy[0]-1][yy[1]-1]="0"
    #         if yy[1]-yy[3] == -2:
    #             count_circle[yy[0]-1][yy[1]+1]-=1
    #             myopic_board[yy[0]-1][yy[1]+1]="0"
    #
    #     if count_star[yy[0]][yy[1]] == 0:
    #         myopic_board[yy[0]][yy[1]] = "0"
    #
    #     if count_star[yy[0]][yy[1]] != 0:
    #         #           print(",,,,,,,,,,")
    #         myopic_board[yy[0]][yy[1]] = "S"+str(count_star[yy[0]][yy[1]])
    #
    #     myopic_board[yy[2]][yy[3]] = "S"+str(count_star[yy[2]][yy[3]])
    #
    #
    # if player=="Circle":
    #     count_circle[yy[0]][yy[1]] -= 1
    #     count_circle[yy[2]][yy[3]] += 1
    #
    #     if yy[0]-yy[2] == -2:
    #         if yy[1]-yy[3] == 2:
    #             count_star[yy[0]+1][yy[1]-1]-=1
    #             myopic_board[yy[0]+1][yy[1]-1]="0"
    #         if yy[1]-yy[3] == -2:
    #             count_star[yy[0]+1][yy[1]+1]-=1
    #             myopic_board[yy[0]+1][yy[1]+1]="0"
    #
    #
    #     if count_circle[yy[0]][yy[1]] == 0:
    #         myopic_board[yy[0]][yy[1]] = "0"
    #     if count_circle[yy[0]][yy[1]] != 0:
    #         myopic_board[yy[0]][yy[1]] = "C" + str(count_circle[yy[0]][yy[1]])
    #     myopic_board[yy[2]][yy[3]] = "C"+str(count_circle[yy[2]][yy[3]])
    #
    # # print("Myopic Board")
    # # print(myopic_board)
    # myopic_value = evaluate(myopic_board)
    # # print("Myopic Value")
    # # print(myopic_value)
    #
    #
    #
    # if yy[0] == 0:
    #     yy[0] = "H"
    # if yy[0] == 1:
    #     yy[0] = "G"
    # if yy[0] == 2:
    #     yy[0] = "F"
    # if yy[0] == 3:
    #     yy[0] = "E"
    # if yy[0] == 4:
    #     yy[0] = "D"
    # if yy[0] == 5:
    #     yy[0] = "C"
    # if yy[0] == 6:
    #     yy[0] = "B"
    # if yy[0] == 7:
    #     yy[0] = "A"
    #
    # if yy[2] == 0:
    #     yy[2] = "H"
    # if yy[2] == 1:
    #     yy[2] = "G"
    # if yy[2] == 2:
    #     yy[2] = "F"
    # if yy[2] == 3:
    #     yy[2] = "E"
    # if yy[2] == 4:
    #     yy[2] = "D"
    # if yy[2] == 5:
    #     yy[2] = "C"
    # if yy[2] == 6:
    #     yy[2] = "B"
    # if yy[2] == 7:
    #     yy[2] = "A"
    #
    # yy[1]+=1
    # yy[3]+=1
    #
    # # print(yy)
    # # print(nodes)
    #
    # # print("-----------------------------------------")
    # # print(evaluate(current_board))
    # with open('output.txt', 'w') as the_file:
    #     if yy[0]== -1 and yy[1] == -1 and yy[2] == -1 and yy[3] == -1:
    #         the_file.write("pass")
    #     else:
    #         the_file.write(yy[0])
    #         the_file.write(str(yy[1]))
    #         the_file.write("-")
    #         the_file.write(yy[2])
    #         the_file.write(str(yy[3]))
    #     the_file.write('\n')
    #     the_file.write(str(myopic_value))
    #     the_file.write('\n')
    #     the_file.write(str(farsighted_utility[0]))
    #     the_file.write('\n')
    #     the_file.write(str(nodes))

    if player=="Star":
        count_star=ccs(current_board)
        count_circle = ccs2(current_board)
        count_star[yy[0]][yy[1]] -= 1
        count_star[yy[2]][yy[3]] += 1

        if yy[0]-yy[2] == 2:
            if yy[1]-yy[3] == 2:
                count_circle[yy[0]-1][yy[1]-1]-=1
                myopic_board[yy[0]-1][yy[1]-1]="0"
            if yy[1]-yy[3] == -2:
                count_circle[yy[0]-1][yy[1]+1]-=1
                myopic_board[yy[0]-1][yy[1]+1]="0"

        if count_star[yy[0]][yy[1]] == 0:
            myopic_board[yy[0]][yy[1]] = "0"

        if count_star[yy[0]][yy[1]] != 0:
            # print(",,,,,,,,,,")
            myopic_board[yy[0]][yy[1]] = "S"+str(count_star[yy[0]][yy[1]])

        myopic_board[yy[2]][yy[3]] = "S"+str(count_star[yy[2]][yy[3]])


    if player=="Circle":
        count_star = ccs(current_board)
        count_circle = ccs2(current_board)
        count_circle[yy[0]][yy[1]] -= 1
        count_circle[yy[2]][yy[3]] += 1

        if yy[0]-yy[2] == -2:
            if yy[1]-yy[3] == 2:
                count_star[yy[0]+1][yy[1]-1]-=1
                myopic_board[yy[0]+1][yy[1]-1]="0"
            if yy[1]-yy[3] == -2:
                count_star[yy[0]+1][yy[1]+1]-=1
                myopic_board[yy[0]+1][yy[1]+1]="0"


        if count_circle[yy[0]][yy[1]] == 0:
            myopic_board[yy[0]][yy[1]] = "0"
        if count_circle[yy[0]][yy[1]] != 0:
            myopic_board[yy[0]][yy[1]] = "C" + str(count_circle[yy[0]][yy[1]])
        myopic_board[yy[2]][yy[3]] = "C"+str(count_circle[yy[2]][yy[3]])


    if yy[0] == -1 and yy[1] == -1 and yy[2] == -1 and yy[3] == -1:
        myopic_board = deepcopy(current_board)
    # if passS>0 or passC>0:
    #     myopic_board = deepcopy(current_board)
    # print("Myopic Board")
    # print(myopic_board)
    myopic_value = evaluate(myopic_board)
    # print("Myopic Value")
    # print(myopic_value)



    if yy[0] == 0:
        yy[0] = "H"
    if yy[0] == 1:
        yy[0] = "G"
    if yy[0] == 2:
        yy[0] = "F"
    if yy[0] == 3:
        yy[0] = "E"
    if yy[0] == 4:
        yy[0] = "D"
    if yy[0] == 5:
        yy[0] = "C"
    if yy[0] == 6:
        yy[0] = "B"
    if yy[0] == 7:
        yy[0] = "A"

    if yy[2] == 0:
        yy[2] = "H"
    if yy[2] == 1:
        yy[2] = "G"
    if yy[2] == 2:
        yy[2] = "F"
    if yy[2] == 3:
        yy[2] = "E"
    if yy[2] == 4:
        yy[2] = "D"
    if yy[2] == 5:
        yy[2] = "C"
    if yy[2] == 6:
        yy[2] = "B"
    if yy[2] == 7:
        yy[2] = "A"

    yy[1]+=1
    yy[3]+=1

    # print(yy)
    # print(nodes)

    # print("-----------------------------------------")
    # print(evaluate(current_board))
    with open('output.txt', 'w') as the_file:
        if yy[0]== -1 or yy[1] == -1 or yy[2] == -1 or yy[3] == -1:
            the_file.write("pass")
        else:
            the_file.write(yy[0])
            the_file.write(str(yy[1]))
            the_file.write("-")
            the_file.write(yy[2])
            the_file.write(str(yy[3]))
        the_file.write('\n')
        the_file.write(str(myopic_value))
        the_file.write('\n')
        the_file.write(str(farsighted_utility[0]))
        the_file.write('\n')
        the_file.write(str(nodes))
    the_file.close()
