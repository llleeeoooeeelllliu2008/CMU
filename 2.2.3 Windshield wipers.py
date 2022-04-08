from cmu_graphics import *


def onMouseMove(x, y):
    # Move the wipers to follow the mouse!
    # (HINT: The wipers are Lines, and we can move one end of a line by
    #          changing some of the .x1, .y1, .x2, and .y2 properties!)
    # Place Your Code Here #
    wiper1.x2 = x - 20
    wiper2.x2 = x + 20
    pass


def main():
    # This draws the top of the car.
    Oval(200, 250, 800, 650, fill='dimGrey')
    Oval(200, 250, 800, 450, fill='grey')

    # This draws the road.
    Rect(0, 130, 400, 270, fill='gray')
    Line(-25, 220, 220, 100, fill='darkGreen', lineWidth=85)
    Line(445, 175, 250, 80, fill='darkGreen', lineWidth=70)
    Line(0, 260, 245, 133, fill=gradient('gray', 'white', start='top'), lineWidth=4)
    Line(400, 200, 275, 133, fill=gradient('gray', 'white', start='top'), lineWidth=4)
    Line(140, 400, 260, 133, fill=gradient('gray', 'white', start='top'), lineWidth=4)

    # This draws the sky and hills.
    Oval(200, 90, 425, 90, fill=gradient('skyBlue', 'azure', start='top'))
    Oval(0, 130, 420, 80, fill='darkGreen', rotateAngle=3)
    Oval(600, 130, 600, 70, fill='darkGreen')

    # This draws the car.
    Oval(200, 400, 700, 150, fill='dimGrey')
    Circle(90, 380, 90, fill=None, border='black', borderWidth=20)
    Star(90, 380, 90, 4, roundness=10)
    Rect(120, 320, 160, 10)


if __name__ == '__main__':
    main()
    # wipers
    wiper1 = Line(140, 330, 120, 90, lineWidth=10)
    wiper2 = Line(260, 330, 240, 90, lineWidth=10)
    cmu_graphics.run()
