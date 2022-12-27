n=int(input("Enter number of rows : "))
for i in range (0,n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range (0,i+1):      
        print("*",end=" ")
    for j in range (0,i):         #if we use(0,i+1) again her  we get a peak less star 
        print("*",end=" ")
    print()

'''
Enter number of rows : 5
          *  ----> this is a peak                
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *


        * *
      * * * *      
    * * * * * *    ------> This is a peak less star 
  * * * * * * * *
* * * * * * * * * *

'''