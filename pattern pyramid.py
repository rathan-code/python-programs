num=int(input("Enter the number of rows: "))
for i in range (0,num):         #for rows
    for j in range (0,num-i-1): #for spaces 
        print(end=" ")          
    for j in range (0,i+1):     #for printing *
        print("*",end=" ")
    print()
    

    '''
    Out put
    *
   * *
  * * *  
 * * * *   
    '''