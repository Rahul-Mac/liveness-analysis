'''
Author: Rahul Mac

Code:
    a ← 0
L1 :b ← a + 1
    c ← c + b
    a ← b ∗ 2
    if a < N goto L1
    return c
'''
import copy

def equal(l1, l2):
        if len(l1)== len(l2) and len(l1) == sum([1 for i, j in zip(l1, l2) if i == j]):
                return(True)
        else:
                return(False)

def table(IN, OUT):
        print("\nID\tIN\t\tOUT")
        for x in range(len(IN)):
                print(str(x+1)+"\t"+str(IN[x])+"\t\t"+str(OUT[x]))
        
relation = {0:[1], 1:[2], 2:[3], 3:[4], 4:[1, 5], 5:[]}
DEF = [["a"], ["b"], ["c"], ["a"], [], []]
USE = [[], ["a"], ["b", "c"], ["b"], ["a"], ["c"]]
IN = [[], [], [], [], [], []]
OUT = [[], [], [], [], [], []]
PREV = [[], [], [], [], [], []] 
iteration = 0
change = True
while(change):
        if (iteration==0):
                PREV = copy.deepcopy(OUT)
                print("Iteration "+ str(iteration + 1))
                IN = copy.deepcopy(USE)
                for i in range(len(IN)):
                        r = relation[i]
                        if(len(r)>0):
                                if(len(r) > 1):
                                        for x in r:
                                                OUT[i].append("".join(IN[x]))
                                else:
                                        OUT[i] = IN[r[0]]
                table(IN, OUT)
        else:
                PREV = copy.deepcopy(OUT)
                print("\nIteration "+ str(iteration + 1))
                for i in range(len(IN)):
                        d = set(DEF[i])
                        o = set(OUT[i])
                        x = o.difference(d)
                        for y in x:
                                if y not in IN[i]:
                                        IN[i].append(y)
                for i in range(len(IN)):
                        r = relation[i]
                        if(len(r)>0):
                                if(len(r) > 1):
                                        for x in r:
                                                for q in IN[x]:
                                                        if q not in OUT[i]:
                                                                OUT[i].append(q)
                                else:
                                        OUT[i] = IN[r[0]]
                table(IN, OUT)
        if(equal(PREV, OUT)):
                change = False
        iteration += 1
'''
OUTPUT:
Iteration 1

ID	IN		OUT
1	[]		['a']
2	['a']		['b', 'c']
3	['b', 'c']		['b']
4	['b']		['a']
5	['a']		['a', 'c']
6	['c']		[]

Iteration 2

ID	IN		OUT
1	[]		['a', 'c']
2	['a', 'c']		['b', 'c']
3	['b', 'c']		['b']
4	['b']		['a', 'c']
5	['a', 'c']		['a', 'c']
6	['c']		[]

Iteration 3

ID	IN		OUT
1	['c']		['a', 'c']
2	['a', 'c']		['b', 'c']
3	['b', 'c']		['b', 'c']
4	['b', 'c']		['a', 'c']
5	['a', 'c']		['a', 'c']
6	['c']		[]

Iteration 4

ID	IN		OUT
1	['c']		['a', 'c']
2	['a', 'c']		['b', 'c']
3	['b', 'c']		['b', 'c']
4	['b', 'c']		['a', 'c']
5	['a', 'c']		['a', 'c']
6	['c']		[]
'''
