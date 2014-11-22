import turtle
import tkinter

class Card:
    def __init__(self, canvas, val, backimg, frontimg):
        self.val = val
        self.canvas = canvas
        self.backimg = backimg
        self.frontimg = frontimg
        self.faceDown = True
        
        
    def isFaceDown(self):
        return self.faceDown
    
    def getBlackjackRank(self):
        # fix this, not self.val 
        return self.val
    
    def setFaceDown(self):
        # part of it, not the whole thing
        self.faceDown = True
        
    def setFaceUp(self):
        # part of it, not the whole thing
        self.faceDown = False
    
def main():
    # CALLING THE Tk constructor
    root = tkinter.Tk()
    
    # Calling the Canvas constructor
    cv = tkinter.Canvas(root)
    
    #mutator method call
    cv.pack()
    
    # Calling the RawTurtle constructor
    t = turtle.RawTurtle(cv)
    
    # Called two accessor methods
    print(t.xcor(), t.ycor())
    
    screen = t.getscreen()
    
    screen.addshape("cards/back.gif")
    
    for i in range(1,53):
        screen.addshape("cards/"+str(i)+".gif")
    
    t.shape("cards/1.gif")
    
    t.goto(100,100)
    #c = Card(0, cv, "cards/back.gif","cards/1.gif")
    tkinter.mainloop()
    
if __name__ == "__main__":
    main()
    
    