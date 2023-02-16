#🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀#
#🚀              A RACE THROUGH SPACE              🚀#
#🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀#  

#IMPORTS AND SETUP
from tkinter import*
from random import*
from time import*
from math import*



root = Tk()
s = Canvas( root, width=600, height=600, background="black")
rocketImageFile = PhotoImage(file = "rocketTransparent4.png")

#Startup Screen with Game Instructions 
def startupScreen():
  
  s.create_text(300,300, fill = 'white', text = "   A RACE THROUGH SPACE \n\n          A 2-Player Game\n   Use WASD for the left ship\n and arrow keys for the right\n   ship to navigate your ship \n       to the top for a point!\nWhoever has the most points \n by the end of the 60 second\n               timer wins!", font = "Arial 20" )


#SETTING INITIAL VALUES
def setInitialValues():

  #GLOBALIZING VARIABLES

  #Basic Gameplay
  global quit, score1, score2, timer, startTime, clockDisplay
  #Asteroids
  global x, y, xSpeed, ySpeed, size, asteroids, numasteroids, xchoices
  #Rockets
  global rx1, ry1, rSpeedx1, rSpeedy1, rocket1, rx2, ry2, rSpeedx2, rSpeedy2, rocket2
  #Explosion
  global xe, ye, r, eSpeedx, eSpeedy, esize, ecolours, explosion, e

  #For quit function
  quit = False

  #Score
  score1 = 0
  score2 = 0

  #Timer
  startTime = time()
  timer = 60

  #Asteroids
  numasteroids = 50
  x = []
  y = []
  xSpeed = []
  ySpeed = []
  size = []
  asteroids = []
  xchoices = [randint(-50,5),randint(600,650)]

  #Rocket 1 (left)
  rx1 = 150
  ry1 = 450
  rSpeedx1 = 0
  rSpeedy1 = 0
  rocket1 = 0

  #Rocket 2 (right)
  rx2 = 450
  ry2 = 450
  rSpeedx2 = 0
  rSpeedy2 = 0
  rocket2 = 0

  #Explosion
  xe = []
  ye = []
  r = []
  eSpeedx = []
  eSpeedy = []
  esize = []
  ecolours = []
  explosion = []
  e = []

  #ADDING VALUES TO THE EMPTRY ARRAYS
  
  #Explosion
  for i in range(0, 1000): 
    #Starting points	
    xe.append(  400  )
    ye.append(  300  )
    #So that the debris is moving in different directions
    e.append(uniform(-2,2))
    #Part of the equation needed
    r.append(uniform(-2*pi,2*pi))
    #Speeds
    eSpeedx.append(sin(r[i])*e[i])
    eSpeedy.append(cos(r[i])*e[i])
    #Adding the sizes and colours for the explosion
    esize.append(uniform(2, 5)  )
    ecolours.append(  choice(["white",'grey','lightgrey','darkgrey','black']  ))
    explosion.append(0)

  #Asteroids
  for i in range( 5 ):
    for j in range( numasteroids):
      size.append( randint(5,7) )
      c = choice(xchoices)
      x.append( c )
      y.append( randint(0,400) )
      if c < 50:
        xSpeed.append( round(uniform(1.00, 3.00),2))
        ySpeed.append( randint(-4, 4) )
      else:
        xSpeed.append( round(uniform(-3.00,-1.00),2))
        ySpeed.append( randint(-4, 4) )

      asteroids.append ( 0 )  


#UPDATING THE OBJECTS
def updateObjects():
  global x,y,xSpeed,numasteroids
  global rx1, ry1, rSpeedx1, rSpeedy1, rx2, ry2, rSpeedx2, rSpeedy2, xc, yc, df1, df2
  global score1, score2, eSpeedx, eSpeedy, esize, ecolours, explosion

  for i in range( numasteroids ):
    x[i] = x[i] + xSpeed[i]
    #print(x[i])
    xc = x[i]
    yc = y[i]
    if x[i] > 650 or x[i] < -50:
      xSpeed[i] = -1*xSpeed[i]

    #Distance Formula Equations
    df1 = sqrt((rx1-xc)**2 + (ry1-yc)**2 )
    df2 = sqrt((rx2-xc)**2 + (ry2-yc)**2 )
    
    #If rocket 1 collides with an asteroid
    if df1 < 10:
      for i in range(0,1000):
        explosion[i] = s.create_oval( rx1, ry1, rx1 +esize[i], ry1 +esize[i], fill= ecolours[i], outline = '')
        rx1 += eSpeedx[i]  
        ry1 += eSpeedy[i]
      rx1 = 150
      ry1 = 450
      score1 = 0

    #If rocket 2 collides with an asteroid
    if df2 < 10:
      for i in range(0,1000):
        explosion[i] = s.create_oval( rx2, ry2, rx2 +esize[i], ry2 +esize[i], fill= ecolours[i], outline = '')
        rx2 += eSpeedx[i]  
        ry2 += eSpeedy[i]
      rx2 = 450
      ry2 = 450
      score2 = 0 
  
  #Rocket Movement
  rx1 += rSpeedx1  
  ry1 += rSpeedy1
  rx2 += rSpeedx2 
  ry2 += rSpeedy2

  
  #If Rocket 1 Gets to the top
  if ry1 < 1:
    rx1 = 150
    ry1 = 450
    score1 += 1
    
  #If Rocket 2 Gets to the top
  if ry2 < 1:
    rx2 = 450
    ry2 = 450
    score2 += 1

  #If Rocket 1 hits a wall
  if rx1 > 290 or rx1 < 10:
    rx1 = 100
    ry1 = 450

  #If Rocket 2 hits a wall
  if rx2 < 310 or rx2 > 590:
    rx2 = 450
    ry2 = 450


#CREATING THE OBJECTS
def createObjects():

  global score1, score2, numasteroids, asteroids, x, y, size, rx1, ry1, rx2, ry2, rocket1, rocket2, clockText, timer
  
  #Creating the clock display
  c = ""
  clockText = str(round(timer,2))
  clockDisplay = s.create_text( 300, 45, text = clockText,
  font="Arial 55", fill="white", anchor=CENTER)

  #Creating the score display
  s1 = s.create_text(200,450, fill = 'white', text=score1, font="Arial 75")
  s2 = s.create_text(400,450, fill = 'white', text=score2, font="Arial 75")

  #Creating the asteroids
  for i in range( numasteroids ):
    asteroids[i] = s.create_oval( x[i], y[i], x[i]+size[i], y[i]+size[i], fill="white", outline="")

  #Creating the rockets
  rocket1 = s.create_image(rx1, ry1, anchor=CENTER, image= rocketImageFile)
  rocket2 = s.create_image(rx2, ry2, anchor=CENTER, image= rocketImageFile)

  #Creating the dividing line
  midline = s.create_line(300,80, 300,600, fill = 'white', width = 5)

#USING KEYS TO MOVE ROCKET
def keyDownHandler( event ):
  global rSpeedx1, rSpeedx2, rSpeedy1, rSpeedy2, quite
  
  if event.keysym == "Left":    
    rSpeedx2 = -5  
      
  if event.keysym == "Right":  
    rSpeedx2 = 5  

  if event.keysym == "Up":     
    rSpeedy2 = -5

  if event.keysym == "Down": 
    rSpeedy2 = 5

  if event.keysym == "a":    
    rSpeedx1 = -5  
      
  if event.keysym == "d":  
    rSpeedx1 = 5  

  if event.keysym == "w":     
    rSpeedy1 = -5

  if event.keysym == "s": 
    rSpeedy1 = 5

  elif event.keysym == "q" or event.keysym == "Q": 
    quit = True


def keyUpHandler( event ):

  global rSpeedx1, rSpeedy1, rSpeedx2, rSpeedy2

  if event.keysym in ["a","d"]:
    rSpeedx1 = 0
  elif event.keysym in ["Left","Right"]:
    rSpeedx2 = 0
  elif event.keysym in ["w","s"]:
    rSpeedy1 = 0
  elif event.keysym in ["Up","Down"]:
    rSpeedy2 = 0
  
  #if event.keysym in ["Left", "Right", "a", "d"]:
    #rSpeedx1 = 0
    #rSpeedx2 = 0

  #elif event.keysym in ["Up", "Down", "w", "s"]:
    #rSpeedy1 = 0
    #rSpeedy2 = 0


#FOR WHEN GAME HAS ENDED
def stopGame():
  s.delete("all")

  s.create_text( 300, 300, text="Thanks for playing...good bye", anchor=CENTER, font="Times 30")
  s.update()
  sleep(10)
  root.destroy()

#FUNCTION TO RUN GAME
def runGame():
  global startTime, clockDisplay, timer, quit
  
  #Allowing the startup screen to be shown for a bit
  startupScreen()
  s.update()
  sleep(10)

  #Calling main function for values
  setInitialValues()
  c = 0
  
  
  frameNum = 0
  
  while quit == False:
    #Setting up more timer parts
    elapsedTime = time() - startTime
    if elapsedTime >= 1: 
      timer = timer - 1
      startTime = time() 
    
    #If the timer hits 0
    if timer == 0:
      s.delete("all")

      #Deciding the winner
      if score1 > score2:
        winner = "The Winner Is Rocket 1"
      elif score2 > score1:
        winner = "The Winner Is Rocket 2"
      else:
        winner = "Tie"

      #Letting users know who the winner is
      endText = s.create_text(300,300, fill = 'white', text = winner, font = "Arial 20" )
      s.update()
      sleep(5)
      s.delete(endText)
      #Ending the game
      quit = True

    #Calling rest of the functions
    else:
      createObjects()
      
      s.update()
      sleep(0.03)
      s.delete("all")

      updateObjects()

      #print("Just finished frame #", frameNum)
      frameNum = frameNum + 1
    
      

  stopGame()


#FINAL SETUP CODE
root.after(0, runGame)

s.bind( "<Key>", keyDownHandler)
s.bind( "<KeyRelease>", keyUpHandler)


s.pack()
s.focus_set()
root.mainloop()