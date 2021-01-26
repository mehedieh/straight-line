import matplotlib.pyplot as plt
import numpy as np
import os
import time


def clear():
    _ = os.system('cls')



#Uses gradient and y intercept to calculate a y point for a given x point
def GetYPoint(xPoint, gradient, yIntercept):
    yPoint = (xPoint * gradient) + yIntercept
    return yPoint


class Line():


    #Class constructor
    def __init__(self, gradient, yIntercept):
        self.gradient = gradient
        self.yIntercept = yIntercept

    xPoints = []
    yPoints = []

    # Draw points from line
    def Draw(self, currentXPoint, xLimit):
        increment = 1
        xPoints = []
        yPoints = []


        #Create array of x points based on given range and increment
        for i in range(currentXPoint, xLimit + 1, +increment):
            xPoints.append(currentXPoint)
            currentXPoint += increment


        #Creates array of y points using array of x points
        for i in range(0, len(xPoints), +1):
            yPoints.append(GetYPoint(xPoints[i], self.gradient, self.yIntercept))

        #Draw points to axes

        fig, ax = plt.subplots()
        plt.title("y = " + str(gradient) + "x + " + str(yIntercept))
        ax.plot(xPoints, yPoints)
        plt.ylim(yPoints[0], yPoints[-1])
        plt.xlim(xPoints[0], xPoints[-1])
        plt.show()




print("Line equation: y = ", end="")
gradient = float(input())
clear()
print("Line equation: y = " + str(gradient) + "x + ", end="")
yIntercept = float(input())
clear()
print("Line equation: y = " + str(gradient) + "x + " + str(yIntercept))
time.sleep(1)
clear()

newLine = Line(gradient, yIntercept)

print("X Range: ", end="")
currentXPoint = input()
clear()
print(f"X Range: {currentXPoint} to  {end=}"")
xLimit = input()
clear()
print(f"X Range: {currentXPoint} to {xLimit}")    
time.sleep(1)
clear()


newLine.Draw(int(currentXPoint), int(xLimit))





