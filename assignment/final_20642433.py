import random
FNAME = 'inputs/2.txt'
OUTFNAME = 'output.txt'


# Q1 - function to read data from the text file and save it in a data structure.
### Stage 1
def readData():
    global numDays, timeslots,rooms, students, supervisors, panels
    # read data
    inFile = open(FNAME,'r')

    numDays = int(inFile.readline().split(':')[-1])
    timeslots = int(inFile.readline().split(':')[-1])
    rooms = int(inFile.readline().split(':')[-1])

    # Gap
    inFile.readline()
    students = []
    supervisors = {}
    panels = {}
    while True:
        line = inFile.readline().strip()
        if line == '': break

        d = line.split(';')
        students.append(d[0])
        supervisors[d[0]] = d[1]
        panels[d[0]] = tuple(d[2].split(','))

        

    inFile.close()
    # print('numDays: ',numDays)
    # print('timeslots: ',timeslots)
    # print('rooms: ',rooms)

    # print("students: ", students)
    # print("supervisors: ", supervisors)
    # print("panels: ", panels)

# Q2 - function to generate the conflict matrix
### Stage 2
def generateConflictMatrix():
    global conflictMatrix, totalConflicts
    conflictMatrix, totalConflicts = {}, {}
    
    for i in supervisors:
        num = 0
        for j in panels:
    
            if i == j: conflictMatrix[(i,j)] = '0'
            else:
                s1 = supervisors[i]
                s2 = supervisors[j]
                p1 = panels[i]
                p2 = panels[j]
                if (s1 in p2 or s2 in p1 or s1 == s2) and bool(set(p1).intersection(p2)):
                    num += 1
                    conflictMatrix[(i,j)] = '1*'
                elif s1 in p2 or s2 in p1 or s1 == s2:
                    conflictMatrix[(i,j)] = '*'
                elif bool(set(p1) & set(p2)):
                    num += 1
                    conflictMatrix[(i,j)] = '1'
                else:
                    conflictMatrix[(i,j)] = '0'
            # print(i,j,conflictMatrix[(i,j)])
        totalConflicts[i] = num
    # print(conflictMatrix)
    # print(totalConflicts)



### Stage 3

# Creating an empty schedule
def generateEmptySchedule():   
    global schedule
    schedule = {}
    # numOfSlots = 0
    for i in range(numDays):
        # k1 = 'D'+str(i+1)
        k1 = i+1
        for j in range(timeslots):
            # k2 = 'slot'+ str(j+1)
            # numOfSlots +=1
            k2 = j+1
            sch={}

            for k in range(rooms):
                k3 = k+1
                sch[k3] = ''
            schedule[(k1,k2)]= sch 


# Q3 - function to generate the students ordered list
# Step 1
# Generate the students ordered list

def mySortFunc(e):
    # print (e,totalConflicts[e])
    return totalConflicts[e]


def generateOrderedList():
    #using random
    # random.shuffle(students)
    # plan = students.copy()

    #using penalty
    plan = sorted(totalConflicts,key=mySortFunc,reverse=True)

    # generate empty schedule
    generateEmptySchedule()

    #Step 2
    while len(plan) > 0:
        s = plan[0]
        # print(s,plan)
        status = generateSchedule(s)
        # if status: 
        plan.pop(0)
        # else:
        #     print('scheduled plan', plan, len(plan))
            # generateOrderedList()
            # break
    # print(schedule)



# Q4
#step 3
supervisorPenalty = 0
def generateSchedule(s):  
    global supervisorPenalty 

    pKey = 0
    for k in schedule:
        # print(k, schedule[k])
        for r in range(1, rooms+1):
            rm = schedule[k][r]

            if rm == '':
                if r == 1:
                    schedule[k][r] = s
                    return True
                else:
                    isConflict = False
                    for preR in range(1, r):
                        previousRoom = schedule[k][preR]
                        # print(previousRoom,s)
                        if previousRoom != '':

                            type = conflictMatrix[(previousRoom,s)]
                            # print('conflict type: ',type)
                        
                            if type == '1' or type == '1*' or previousRoom == s:
                                isConflict = True
                                break
                            elif type == '*':
                                isConflict = True
                                if pKey == 0: 
                                    pKey = (k,r)
                            
    
                    if not isConflict:
                        schedule[k][r] = s
                        return True
                    else:
                        break


        
        
    if pKey != 0:
        schedule[pKey[0]][pKey[1]] = s
        supervisorPenalty += 2
        return True
    else:
        print('No Schedule found for',s)
        return False
    
    # return False




panelState = {}
penaltyPerPanel = 0
def updatePanelState(panel,sup, k):
    # print(sup, panel,k)
    global penaltyPerPanel

    for p in panel:
        if p in panelState:
            previousState = panelState[p]
            # print("Check Penalty for ",p,previousState,"Current State",k)
            
            slot = k - previousState
            
            if slot > 1:
                penaltyPerPanel += (slot-1)
            # if previousState[1]
        
        panelState[p] = k
    
    panelState[sup] = k
    
    

# Q5 - function to calculate the quality of the final schedule
def calculateQuality():
    global totalPenalty
    #Create a panel state with the start
    for p in students:
        pan = list(panels[p])
        pan.append(supervisors[p])
        for tech in pan:
            if tech not in panelState:
                panelState[tech] = 0
    # print('Empty',panelState)

    

    ## TODO: Create a new schedule using slot values
    index = 0
    for k in schedule:
        index+=1
        for r in range(1,rooms+1):
            
            rm = schedule[k][r]
            if rm == '': 
                continue
            else:
                updatePanelState(list(panels[rm]),supervisors[rm],index)

        
        # print(day,slot,room,student)
    #Total Penalty
    totalPenalty = supervisorPenalty + penaltyPerPanel
    # print("Total Penalty", totalPenalty)
    



# Q6 - display the schedule 
def getSchedule(s,r):
    student = schedule[s][r]
    if student == '': return '-- '
    elif len(student) <3: return student + ' '
    else: return student

def displaySchedule():
    print('=' *90,end='\n\n')
     
    print('|\t\t\t|',end='')
    for s in range(1,timeslots+1):
        print(f"\tSlot {s}",end="\t")
    print(end='\n')
    print('|','=' *90,)
    
    for d in range(1,numDays+1):
        print(f'|  Day {d}\t|',"-"*70)
        for r in range(1,rooms+1):
            
            print(f'|\t\t| R{r}\t|',end = '      ')
            for slot in range(1,timeslots+1):
                
                student = schedule[(d,slot)][r]
                
                # print((d,slot,num),end= "   ")
                print(student if student != '' else '--',end= "\t\t")
            print(end='\n')
        
    
    print('|','=' *90)


    print('Supervisor penalty:',supervisorPenalty)
    print("Panel Penalty",penaltyPerPanel)
    print("Total Penalty: ",totalPenalty)


# displaySchedule()



#Q7 - function to save the schedule in a text file.
# Save data
def saveSchedule():
    string = ""
    outFile = open(OUTFNAME,'w')

    for key in schedule:
        
        day = key[0]
        slot = key[1]
        for r in range(1, rooms + 1):
            string += f'D{day},Slot{slot},R{r};{schedule[key][r]}\n'
        
    # Save the schedule in following format for reusability
    # Day,Slot,Room;Student
    # Day slot and room seperated by ',' and assigned student seperated by ';'   

    
    string += f'\nSupervisor penalty:{supervisorPenalty}\n'
    string += f"Panel Penalty:{penaltyPerPanel}\n"
    string += f"Total Penalty:{totalPenalty}\n"

    outFile.write(string)
    outFile.close()

# Q4 - function to schedule student presentations.
def mainMethod():
    
    # Q1
    readData()
    
    # Q2
    generateConflictMatrix()
    
    # Q3 generate student ordered list
    generateOrderedList()

    # Q5
    calculateQuality()

    # # Q6
    displaySchedule()

    # # Q7
    saveSchedule()

    # print("schedule", schedule)


# Function calls
mainMethod()