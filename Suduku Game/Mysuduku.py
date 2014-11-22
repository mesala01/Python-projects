


def reduce(matrix):
    change = True
    groups = getGroups(matrix)

    while change:
        change = reduceGroups(groups)

def reduceGroups(groups):
    change = False
    for group in groups:
        if reduceGroup(group):
            change = True
    return change


def reduceGroup(group):
    change = False
    for item in group:
        
        count = 0 
        for i in group:
            if i== item:
                count = count + 1

        if len(item)==count: 
            for a in group:
                if a!=item:
                    val = len(a)
                    a.difference_update(item)
                    if val != len(a):
                        change = True  
                     
                
         
    for i in range(9):
        if len(group[i])>1:
            
            value = group[i]
            valueCopy=value.copy()
            for j in range(9):
                if j != i:
                    valueCopy.difference_update(group[j])
            if len(valueCopy)==1:
                value.clear()
                value.update(valueCopy)
                change = True 
                        
                
    return change  
def getGroups(matrix):
    groups =[]
    for row in range(0,9,1):
        group= []
        for col in range(0,9,1):
            group.append(matrix[row][col])
        groups.append(group)
        
        
    for col in range(0,9,1):
        group = []
        for row in range(0,9,1):
            group.append(matrix[row][col])
        groups.append(group)

            
    for row in range(0,9,3):
        for col in range(0,9,3):
            group=[]
            for y in range(row,row+3):
                for x in range(col,col+3):
                    group.append(matrix[y][x])
            groups.append(group)
            
    return groups 
  


def printMatrix(matrix):
    result=""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(matrix[i][j])>1:
                s = "x "
            else:
                for x in matrix[i][j]:
                    s = str(x) + " "
            result = result + str(s)
        result = result + "\n"  
    print(result)
    
    

def main():
   
    file = open("sudoku.txt","r")
    matrix = []
    for t in range(9):
        line = file.readline()
        lst = line.split()
        row=[]
        for x in range(9):
            if lst[x] == "x":
                s = set(range(1,10))
            else:
              
                s = set([int(lst[x])])
            row.append(s)
        matrix.append(row)
    printMatrix(matrix)
   
    reduce(matrix)
    printMatrix(matrix)
    
    
    
    
    
    
    
if __name__=="__main__":
    main()