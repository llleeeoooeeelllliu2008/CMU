from cmu_graphics import *


def onMousePress(x, y):
    # Move the fish across the screen. We've named each part of the fish above.
    # (HINT: To figure out how far to move each piece, click the first test
    #          below and use the inspector to see how far the fish moves!)
    # Place Your Code Here #
    fishBody.centerX += 10
    fishTail.centerX += 10
    fishEye.centerX += 10
    pass


def main():
    app.background = 'azure'

    # This draws the ocean.
    Rect(0, 120, 400, 325, fill='steelBlue')

    # This draws the shark.
    Oval(200, 400, 200, 400, fill='grey')
    Oval(200, 420, 150, 300, fill='white')
    Circle(135, 250, 3)
    Circle(265, 250, 3)
    Oval(200, 360, 100, 150, fill='crimson')
    Oval(200, 370, 110, 120, fill='white')


if __name__ == '__main__':
    main()
    # This draws and names each part of the fish.
    fishBody = Oval(250, 160, 40, 22, fill='orangeRed')
    fishTail = Star(230, 160, 15, 4, fill='orangeRed', rotateAngle=45)
    fishEye = Circle(260, 160, 2, fill='black', border='white', borderWidth=1)
    cmu_graphics.run()
