from turtle import *
import tkinter
import random

screenMaxX = 300
screenMaxY = 300
screenMinX = -300
screenMinY = -300
    
# This is a example of a class that uses inheritance. 
# The Ball class inherits from the RawTurtle class. 
# This is indicated to Python by writing
# class Ball(RawTurtle):
# That says, class Ball inherits from RawTurtle, which 
# means that a Ball is also a RawTurtle, but it is a 
# little more than just a RawTurtle. The Ball class also 
# maintains a dx and dy value that is the amount
# to move as it is animated. 
#a ball is turtle
class Ball(RawTurtle):
      # The __init__ is the CONSTRUCTOR. Its purpose is to 
      # initialize the object by storing data in the object. Anytime
      # self.variable = value is written a value is being stored in 
      # the object referred to by self. self always points to the 
      # current object.
      #we must have a definite in our class
      def __init__(self,cv,dx,dy):
            # Because the Ball class inherits from the RawTurtle class
            # the Ball class constructor must call the RawTurtle class
            # constructor to initialize the RawTurtle part of the object.
            # The RawTurtle class is called the BASE class. The Ball class 
            # is called the DERIVED class. The call to initialize the 
            # base class part of the object is always the first thing
            # you do in the derived class's constructor.
            #RawTurtle.__init__(self,cv)
            #call the turtle constructor
            super().__init__(cv)
            
            # Then the rest of the object can be initialized.
            #To remove the line of the turtle
            self.penup()
            #create the shape
            self.shape("soccerball.gif")
            #current position and add dx to it
            self.dx = dx
            #current position add dy to it
            self.dy = dy

      # The move method is a mutator method. It changes the data
      # of the object by adding something to the Ball's x and y 
      # position. 
      def move(self):
            newx = self.xcor() + self.dx
            newy = self.ycor() + self.dy

            # The if statements below make the ball
            # bounce off the walls.
            if newx < screenMinX:
                  newx = 2 * screenMinX - newx
                  self.dx = -self.dx
            if newy < screenMinY:
                  newy = 2 * screenMinY - newy
                  self.dy = - self.dy
            if newx > screenMaxX:
                  newx = 2 * screenMaxX - newx
                  self.dx = - self.dx
            if newy > screenMaxY:
                  newy = 2 * screenMaxY - newy
                  self.dy = -self.dy
            
            # Then we call a method on the RawTurtle 
            # to move to the new x and y position.
            self.goto(newx,newy)
class GravityBall(Ball):
      def __init__(self,cv,dx,dy):
            Ball.__init__(self,cv,dx,dy)
      def move(self):
            if abs(self.dy)<0.2 and self.ycor()<5:
                  self.dy=0
            else:
                  self.dy=self.dy-0.195
            if abs(self.dx) <0.2:
                  self.dx=0
            else:
                  self.dx=0.999*self.dx
            Ball.move(self)


# Once the classes and functions have been defined we'll put our
# main function at the bottom of the file. Main isn't necessarily
# written last. It's simply put at the bottom of the file. Main
# is not a method. It is a plain function because it is not 
# defined inside any class. 
def main():

      # Start by creating a RawTurtle object for the window. 
      root = tkinter.Tk()
      root.title("Bouncing Balls!")
      cv = ScrolledCanvas(root,600,600,600,600)
      cv.pack(side = tkinter.LEFT)
      t = RawTurtle(cv)
      fram = tkinter.Frame(root)
      fram.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)

      screen = t.getscreen()
      screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
      t.ht()
      screen.tracer(20)
      screen.register_shape("soccerball.gif")

      # The ballList is a list of all the ball objects. This 
      # list is needed so the balls can be animated by the 
      # program. 
      ballList = []

      # Here is the animation handler. It is called at
      # every timer event.
      def animate():
            # Tell all the balls to move
            for ball in ballList:
                  ball.move()

            # Set the timer to go off again
            screen.ontimer(animate)

      # This code creates 10 balls heading
      # in random directions
      
            
      #for k in range(10):
            #dx = random.random() * 3 + 1
            #dy = random.random() * 3 + 1
            ## Here is how a ball object is created. We 
            ## write ball = Ball(5,4)
            ## to create an instance of the Ball class
            ## and point the ball reference at that object.
            ## That way we can refer to the object by writing
            ## ball. 
            #ball = Ball(cv,dx,dy)
            ## Each new ball is added to the Ball list so 
            ## it can be accessed by the animation handler.
            #ballList.append(ball)

      # This is the code for the quit Button handling. This
      # function will be passed to the quitButton so it can
      # be called by the quitButton when it wasPressed.
      def quitHandler():
            # close the window and quit
            print("Good Bye")
            root.destroy()
            root.quit() 
            quitButton = tkinter.Button(fram, text = "Quit", command=quitHandler)
            quitButton.pack()            
            
      
      def addballHandler():
            dx = random.random() * 3 + 1
            dy = random.random() * 3 + 1 
            ball = Ball(cv,dx,dy)
            ballList.append(ball)
            
            
            # close the window and quit
            #print("Good Bye")
            #root.destroy()
            #root.quit()
            print(done)
      # Here is where the quitButton is created. To create
      # an object we write
      # objectReference = Class(<Parameters to Constructor>)
      addButton = tkinter.Button(fram, text = "Addball", command=addballHandler)
      addButton.pack()

      # This is another example of a method call. We've been doing 
      # this all semester. It is an ontimer method call to the 
      # TurtleScreen object referred to by screen.
      screen.ontimer(animate)

      tkinter.mainloop()

if __name__ == "__main__":
      main()

      
    