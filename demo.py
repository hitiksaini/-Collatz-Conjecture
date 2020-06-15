#the 3n+1 problem that even the smaller number had more no. of steps but a large number has less iteration to get 
#infinte that is -> 4,2,1.....->


# if the number is even divide it by 2  if odd- 3n+1 

def checksum(num):
    iterations=1
    while(num!=1):
        if(num%2==0):
            num=int(num/2)
            iterations+=1
        else:
            num= 3*num+1
            iterations+=1
    print(num, iterations)

checksum(256)  #this will check that after how many iterations it becomes 1 .


##output: 1 9
