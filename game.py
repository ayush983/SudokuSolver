import pygame


class Solver:
    def __init__(self,width):
        self.width=width
        self.cell_height=self.cell_width=width/9
    def find_first_empty(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    return (i,j)
        return (8,8)
                
    def find_invalid_set(self,grid,r,c):
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

    def solve_grid(self,grid):
        r,c=self.find_first_empty(grid)
        s=self.find_invalid_set(grid,r,c)
        for i in range(1,10):
            if i not in s:
                grid[r][c]=i
                self.drawNum(r,c,i)
                if (r==8 and c==8 or self.solve_grid(grid)):
                    return 1
                self.clearNum(r,c,i)
        grid[r][c]=0
        
    def drawNum(self,i,j,num):
        xcor=j*self.cell_width+10
        ycor=i*self.cell_width+10
        pos=(xcor,ycor)
        num_text=font.render(str(num),True,pygame.Color(255,226,222))
        back_rect=pygame.Rect(pos[0],pos[1],60,60)
        pygame.draw.rect(screen,(39,51,75),back_rect)
        screen.blit(num_text,(pos[0]+5,pos[1]+5))
        pygame.display.update()
        pygame.time.wait(100)
        pygame.draw.rect(screen,(71,71,71),back_rect)
        screen.blit(num_text,(pos[0]+5,pos[1]+5))
        pygame.display.update()
        pygame.event.pump()
        
    def clearNum(self,i,j,num):
        xcor=j*self.cell_width+10
        ycor=i*self.cell_width+10
        pos=(xcor,ycor)
        back_rect=pygame.Rect(pos[0],pos[1],59,59)
        num_text=font.render(str(num),True,pygame.Color(255,226,222))
        pygame.draw.rect(screen,(236,102,82),back_rect)
        screen.blit(num_text,(pos[0]+5,pos[1]+5))
        pygame.display.update()
        pygame.time.wait(100)
        pygame.draw.rect(screen,(71,71,71),back_rect)
        pygame.display.update()
        pygame.event.pump()

class Grid:
    def __init__(self,width,height):
        self.width=width
        self.grid=[[0]*9 for i in range(1,10)]
        self.cell_width=width/9
    def get_grid(self):
        return self.grid
        
    def background(self):
        pygame.draw.rect(screen,pygame.Color(183,174,193),pygame.Rect(5,5,self.width,self.width),4)
        i=1
        while(i*70<self.width):
            width=1
            if i%3==0:width=4
            pygame.draw.line(screen,pygame.Color(183,174,193),(i*70+5,5),(i*70+5,635),width)#vertical lines
            pygame.draw.line(screen,pygame.Color(183,174,193),(5,i*70+5),(635,i*70+5),width)#horizontal lines
            i+=1
        pygame.display.update()
        
    def select_cell(self,screen,pos,select):
        row,col=pos[0],pos[1]
        if row!=-1 and not self.grid[row][col]:
            xcor=col*self.cell_width+10
            ycor=row*self.cell_width+10
            back_rect=pygame.Rect(xcor,ycor,60,60)
            color=(71,71,71)
            if select:color=(39,51,75)
            pygame.display.update(pygame.draw.rect(screen,color,back_rect))
            
    def draw_num(self,screen,pos,num,setnum):
        row,col=pos[0],pos[1]
        if row!=-1 and not self.grid[row][col]:
            xcor=col*self.cell_width+10
            ycor=row*self.cell_width+10
            num_text=font.render(num,True,pygame.Color(255,226,222))
            pygame.display.update(screen.blit(num_text,(xcor+5,ycor+5)))
            if setnum:
                self.grid[int(row)][int(col)]=int(num)
                
    def get_rowcol(self,event_pos):
        cell_width=self.width/9
        cell_height=self.width/9
        if event_pos[1]>0 and event_pos[1]<=self.width and event_pos[0]>=0 and event_pos[0]<=self.width:
            row=event_pos[1]//(cell_height+2.5)
            col=event_pos[0]//(cell_width+2.5)
            return int(row),int(col)
        return -1,-1
    
def printLine(line_text,ypos):
    line_font=pygame.font.SysFont(None,30)
    i=0
    for letter in line_text:
        text=line_font.render(letter,True,pygame.Color(255,220,200))
        pygame.display.update(screen.blit(text,(65+18*i,ypos)))
        i+=1
        pygame.time.wait(150)
        pygame.event.pump()
def blinkCursor(pos,reps):
    line_font=pygame.font.SysFont(None,30)
    cursor=line_font.render("__",True,pygame.Color("white"))
    clear_rect=pygame.Rect(pos[0],pos[1],25,25)
    for i in range(reps):
        pygame.display.update(screen.blit(cursor,pos))
        pygame.time.wait(200)
        pygame.display.update(pygame.draw.rect(screen,(71,71,71),clear_rect))
        pygame.time.wait(200)
        pygame.event.pump()
    
def welcomeScreen():
    welcome_font=pygame.font.SysFont(None,30)
    ypos=150
    printLine("Hi,Welcome to Sudoku Solver",ypos)
    blinkCursor((540,ypos),5)
    printLine("Select any box",ypos+100)
    blinkCursor((310,ypos+100),5)
    printLine("Press ENTER to fix your number",ypos+120)
    blinkCursor((595,ypos+120),5)
    printLine("Press SPACE to solve the grid",ypos+200)
    blinkCursor((580,ypos+200),10)
    screen.fill(pygame.Color(71,71,71))
    pygame.event.clear()



pygame.init()
screen = pygame.display.set_mode((640,640))
font=pygame.font.SysFont(None,70)
pygame.display.set_caption("Sudoku Solver")
screen.fill(pygame.Color(71,71,71))
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.update()
running=True
#welcomeScreen()
grid=Grid(630,630)
grid.background()
solver=Solver(630)
solved=0
select=0
pos=-1,-1
num=""
setnum=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if not solved:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if select:
                    grid.select_cell(screen,pos,0)
                pos=grid.get_rowcol(event.pos)
                grid.select_cell(screen,pos,1)
                select=1

            if select and event.type==pygame.KEYDOWN:
                if num and event.key==pygame.K_RETURN:
                    setnum=1
                    grid.select_cell(screen,pos,0)
                    grid.draw_num(screen,pos,num,setnum)
                if num and event.key==pygame.K_BACKSPACE:
                    grid.select_cell(screen,pos,1)
                else:
                    num=event.unicode
                    setnum=0
                    grid.draw_num(screen,pos,num,setnum)
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                grid1=grid.get_grid()
                print(grid1)
                solved=solver.solve_grid(grid1)


