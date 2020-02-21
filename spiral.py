#course:cmps3500
#lab3
#date:2/18/20
#username:mmercado
#name:Ma Mikaela Mercado
#description: PART B: Spiral Path
import numpy as np 
def spiraly(row,column,m):
    startrow=0;startcolumn=0
    print("\nOne dimensional list spiraling clockwise:")
    while(startrow < row and startcolumn < column):
        for i in range(startcolumn,column):
            print m[startrow][i], 
        
        startrow+=1
        for i in range(startrow,row):
            print m[i][column-1],
        
        column-=1
        if(startrow<row):
            for i in range((column-1),(startcolumn-1),-1):
                print m[row-1][i],
        
        row-=1
        if(startcolumn<column):
            for i in range((row-1),(startrow-1),-1):
                print m[i][startcolumn],
        startcolumn+=1
        
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
   
m = [] 
print("Type in each number followed by the enter key to fill in matrix:") 
for i in range(R):           
        a =[] 
        for j in range(C):       
            a.append(int(input())) 
        m.append(a) 
                                    
                                    
print("\nOriginal Matrix:")
print(np.matrix(m))
spiraly(R,C,m)

