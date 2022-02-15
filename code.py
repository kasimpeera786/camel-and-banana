Aim: Implement a banana camel problem using Python, based on AI technique that satisfies
temporal constraints.
Procedure/Algorithm: There would be one or more than one checkpoint. We are breaking each section of the checkpoint in the sections of length one.
Here transportation is done in 1-mile steps. As in the example discussed above, camel walks with 1000 bananas for 1 mile left 998 bananas there and consume 2. In the last round, the camel will consume only one banana.
At each subsequent mile, we are subtracting the no. of bananas lost in travelling each mile from the total no. of bananas. To calculate the total bananas left after 1 mile we use another variable start.
Program: 
total=int(input('Enter no. of bananas at starting '))
distance=int(input('Enter distance you want to cover '))
load_capacity=int(input('Enter max load capacity of your camel '))
lose=0
start=total
for i in range(distance):
    while start>0:
        start=start-load_capacity

        if start==1:
            lose=lose-1
        lose=lose+2

    lose=lose-1
    start=total-lose
    if start==0:
        break
print(start)
Manual Output:    Let’s have 2 drop points in between the source and destination.

With 3000 bananas at the source. 2000 at a first intermediate point and 1000 at 2nd intermediate point.

Source————–IP1—————–IP2———————-Destination

3000       x km        2000     y km           1000          z km
3000 – 5x = 2000 so we get x = 200
2000-3y = 1000 so we get y = 333.33 but here the distance is also the number of bananas and it cannot be fraction so we take y =333 and at IP2 we have the number of bananas equal 1001, so its 2000-3y = 1001
So the remaining distance to the market is 1000 -x-y =z i.e  1000-200-333 => z =467.
Now, there are 1001 bananas at IP2.

So from IP2 to the destination point camel eats 467 bananas. The remaining bananas are 1001-468=533.
