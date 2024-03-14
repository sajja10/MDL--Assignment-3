import numpy as np

numberofiterations = 0
Max_Change = 1

NextItrVal = np.zeros((4,3))
typeofcell = np.full((4,3), " ")
bonus = np.full((4,3), " ")
bonus[0][1]="Reward"
bonus[0][2]="Penalty"
bonus[2][1]="T"
typeofcell[0, 1] = "Reward" 
typeofcell[0, 2] = "Penalty"
typeofcell[2, 1] = "T"  
NextItrVal[0, 1] = 1.0
NextItrVal[0, 2] = -1.0

CurItrVal = NextItrVal.copy()


def ValueReturn(NewRow, NewCol, OldRow, OldCol):
    if (NewRow < 0 or NewRow >= 4 or NewCol < 0 or NewCol >= 3): # out of bounds
        return CurItrVal[OldRow][OldCol]
    if(typeofcell[NewRow][NewCol] == "W"): # hit a wall
        return CurItrVal[OldRow][OldCol]
    else:
        return CurItrVal[NewRow][NewCol]




Max_Change = 1
while 1:
    if (Max_Change <= 0.0001):
        break
    Max_Change = 0
    for i in range(4):
        for j in range(3):
            if typeofcell[i, j] == " ":
                # NSEW
                Val1 = (-0.04)+(0.95)*((0.7)*ValueReturn(i-1, j, i, j)+(0.15)*ValueReturn(i, j-1, i, j)+(0.15)*ValueReturn(i, j+1, i, j))
                Val2 = (-0.04)+(0.95) * ((0.7)*ValueReturn(i+1, j, i, j)+(0.15)*ValueReturn(i, j-1, i, j)+(0.15)*ValueReturn(i, j+1, i, j))
                Val3 = (-0.04)+(0.95) * ((0.7)*ValueReturn(i, j+1, i, j)+(0.15)*ValueReturn(i+1, j, i, j)+(0.15)*ValueReturn(i-1, j, i, j))
                Val4 = (-0.04)+(0.95) * ((0.7)*ValueReturn(i, j-1, i, j)+(0.15)*ValueReturn(i+1, j, i, j)+(0.15)*ValueReturn(i-1, j, i, j))
                maxval = max(Val1, Val2, Val3, Val4)
                if(maxval==Val1):
                    bonus[i][j]="N"
                if(maxval==Val2):
                    bonus[i][j]="S"
                if(maxval==Val3):
                    bonus[i][j]="E"
                if(maxval==Val4):
                    bonus[i][j]="W"
                Max_Change = max(abs(CurItrVal[i, j]-maxval),Max_Change)
                NextItrVal[i, j] = maxval
    CurItrVal = NextItrVal.copy()
    numberofiterations += 1
    print(CurItrVal)




print("Number of iterations = ", numberofiterations)

print("\n\n")

print(bonus)

print("\nKey - N=North, S=South, W=West, E=East, R=Reward, P=Penalty, T=Wall")