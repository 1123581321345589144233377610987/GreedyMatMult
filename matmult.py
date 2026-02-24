def calc(d):
    table=[]
    length=len(d)
    for i in range(length):
        table.append([])
        for j in range(length):
            table[i].append(-42)
    
    #base cases:
    for i in range(1,length):
        table[i][i]=0
    
    row=1
    col=2
    mastercol=2
    while table[1][length-1]==-42:
        possibilities=[]
        for k in range(row,col):
            possibilities.append(table[k+1][col]+table[row][k]+(d[row-1]*d[k]*d[col]))
        table[row][col]=min(possibilities)
        row+=1
        col+=1
        if col>(length-1):
            mastercol+=1
            col=mastercol
            row=1
    #testing
    #for i in table:
     #   print(i)
    return(table[1][length-1])
'''
    for i in range(1,length):
        for j in range(1,length):
            if(j>i):
                possibilities=[]
                for k in range (i,j):
                    if(table[k+1][j]!=-42 and table[i][k]!=-42):
                        possibilities.append(table[k+1][j]+table[i][k]+(d[i-1]*d[k]*d[j]))
                table[i][j]=min(possibilities)
'''
class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.sortby=-1
    def calcSortby(self):
        self.sortby=abs((self.value/self.right.value)-(self.value/self.left.value))

def greedy(d):
    nodes=[]
    length=len(d)
    for i in range(length):
        nodes.append(node(d[i]))
        if(i>0):
            nodes[i].left=nodes[i-1]
    for i in range(length-1):
        nodes[i].right=nodes[i+1]
    
    middles=nodes[1:length-1]
    for i in middles:
        i.calcSortby()
    middles.sort(key=lambda x: x.sortby, reverse=True)

    cost=0
    while(len(middles)>0):
        #testing
        #print(cost)
        #print([x.value for x in nodes])
        #print([x.value for x in middles])
        cost+=middles[0].value*middles[0].right.value*middles[0].left.value
        middles[0].left.right=middles[0].right
        middles[0].right.left=middles[0].left
        if(middles[0].left.left!=None):
            middles[0].left.calcSortby()
        '''
        else:
            middles[0].left.right.left=None
            del nodes[0]
        '''
        if(middles[0].right.right!=None):
            middles[0].right.calcSortby()
        '''
        else:
            middles[0].right.left.right=None
            del nodes[-1]
        '''
        del middles[0]
        middles.sort(key=lambda x: x.sortby, reverse=True)
    return cost

#works
#d=[1,7,100,8,9,1]
#d=[1,6,2,3,3]
#d=[1,2,3,4,5]
#d=[1,2,3,4,5,6]
#d=[6,5,4,3,2,1]
#d=[1,3,5,4,2]
#d=[1,3,7,54]
#d=[1,3,7,67]
#d=[1,3,7,54,67,1]
#d=[7,54,67,1]
#d=[7,54,67]
#d=[100,100,100,1,1]
#d=[100,200,300,1,1]
#d=[100,200,300,2,2]

#problems
#d=[3,7,54,67]
#d=[3,7,80,67]
#d=[3,7,50,67]
#d=[1,2,100,100]
#d=[1,2,100,100,300]
#d=[100,100,2,1]
#d=[100,100,100,2,1]
#d=[100,200,300,2,1]

d=[100,200,300,2,2]
print(calc(d))
print(greedy(d))
