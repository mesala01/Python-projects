

# The imports include turtle graphics and tkinter modules.
# The colorchooser and filedialog modules let the user
# pick a color and a filename.
import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
import random

class Tile(turtle.RawTurtle):
    def __init__(self,canvas,screen,rowIndex,colIndex,matrix,gameApp):
        super().__init__(canvas)
        
        self.gameApp = gameApp
        self.rowIndex = rowIndex
        self.colIndex = colIndex
        self.matrix = matrix
        self.penup()
        #screen.tracer(0)
        
        self.shape("tile36.gif")
        self.screen = screen
        
        self.goto(100+colIndex*200+rowIndex*200)
        
        def leftClickHandler(x,y):
            self.whenLeftClicked()
            
        self.onclick(leftClickHandler)
        
        def rightClickHandler(x,y):
            self.whenRightClicked()
            
        self.onclick(rightClickHandler,btn=3)        
        
    def whenLeftClicked(self):
        if self.isvisible():
            for row in range(3):
                for col in range(3):
                    if self[row][col].eval() != 0:
                        self[row][col].st()
                        self[row][col].goto(col*100+50,row*100+50)
           
            self.screen.update() 
            
            
    class Dummy:
        def __init__(self):
            pass
    
        def eval(self):
            return 0
    
        def goto(self,x,y):
            pass            
    
            
            
       
        
  
    ##def gameOver(self):
        #if self.bomb:
            #self.shape("bomb36.gif")
        #self.onclick(None)
        #self.onclick(None,btn=3)


class TicTacToeApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.matrix = []
        self.buildWindow()
        self.paused = False
        self.stop = False
        self.running = False
        self.turn = Player1
        self.turn = Player2
        self.locked = False        
        
    def decTileNum(self):
        self.tileNum = self.tileNum - 1
        self.tileLabel.config(text="Tiles = " + str(self.tileNum))
        if self.tileNum == 40:
            self.gameOver()
            tkinter.messagebox.showinfo(message="Cat's game!!",title="Nobody  Won!!!!")

    def gameOver(self):
        for row in self.matrix:
            for tile in row:
                tile.gameOver()
        self.screen.update()

    def buildWindow(self):

        self.master.title("TicTacToe")

        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)

        def newGame():
            screen = theTurtle.getscreen()
            screen.setworldcoordinates(0,600,600,0)  
            screen.clear()
            screen.tracer(0)
            self.screen = screen
            
            screen.register_shape("bomb36.gif")
            screen.register_shape("tile36.gif")
            screen.register_shape("flag36.gif")
            
            for row in self.matrix:
                for tile in row:
                    tile.goto(-1000,-1000)            
            
            randomNumbers = []
            
            for i in range(40):
                r = random.randrange(256)
                while r in randomNumbers:
                    r = random.randrange(256)
                randomNumbers.append(r)
    
            
            self.matrix = []
            self.tileNum = 256
            count = 0
            
            for rowIndex in range(16):
                row = []
                
                for colIndex in range(16):
                    bomb = (count in randomNumbers)

                        
                    aTile = Tile(canvas,screen,rowIndex,colIndex,self.matrix,bomb,self)
                    count = count + 1                
                    row.append(aTile)
                    
                self.matrix.append(row)
                
            self.screen.update()
                    

        fileMenu.add_command(label="New Game",command=newGame)
     
        fileMenu.add_command(label="Exit",command=self.master.quit)

        bar.add_cascade(label="File",menu=fileMenu)

        self.master.config(menu=bar)

        canvas = tkinter.Canvas(self,width=600,height=600)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.ht()

        newGame()          

        sideBar = tkinter.Frame(self,padx=5,pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        bombLabel = tkinter.Label(sideBar,text="Bombs = 40")
        bombLabel.pack()
        
        self.tileLabel = tkinter.Label(sideBar,text="Tiles = 256")
        self.tileLabel.pack()        


def main():
    root = tkinter.Tk()
    TictactoeApp = TicTacToeApplication(root)

    TictacToeApp.mainloop()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()