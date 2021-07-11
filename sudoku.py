grid=[[-1]*9 for i in range(1,10)]
flag=1
n=int(input("Enter number of filled cells"))
for i in range(n):
    r=int(input("row="))
    c=int(input("col="))
    val=int(input("val="))
    grid[r][c]=val
for i in grid:
    for j in i:
        print(j,end=' ')
    print('')

def printgrid(grid):
    print('Grid=')
    for a in grid:
        for b in a:
            print(b,end=' ')
        print('')
def find_first_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==-1:
                return (i,j)
    return(8,8)
            
def find_invalid_set(grid,r,c):
    row=set(grid[r])
    col=set([grid[j][c] for j in range(0,9)])
    box=[]
    boxr=r-(r%3)
    boxc=c-(c%3)
    for j in range(boxr,boxr+3):
        for k in range(boxc,boxc+3):
            box.append(grid[j][k])
    box=set(box)
    s=row|col|box
    return s

def solver(grid):
    r,c=find_first_empty(grid)
    s=find_invalid_set(grid,r,c)
    for i in range(1,10):
        if i not in s:
            grid[r][c]=i
            if (r==8 and c==8 or solver(grid)):
                return 1
    grid[r][c]=-1
            

res=solver(grid)
print('Printing soln now')
printgrid(grid)

print('res=',res)
