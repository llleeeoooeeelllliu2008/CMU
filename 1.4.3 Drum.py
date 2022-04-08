from cmu_graphics import *


def main():
    app.background = gradient('lightBlue', 'blue')

    # This draws the drum.
    Oval(200, 300, 200, 100, fill='red', border='black')
    Rect(100, 150, 200, 150, fill='red')
    Line(125, 185, 125, 330, fill='white', lineWidth=5)
    Line(170, 200, 170, 350, fill='white', lineWidth=5)
    Line(230, 200, 230, 350, fill='white', lineWidth=5)
    Line(277, 185, 277, 330, fill='white', lineWidth=5)

    # Draw the top of the drum.
    # Place Your Code Here #
    Oval(200, 150, 200, 100, fill=gradient("white", "wheat"), border="black")
    # Draw the drum sticks.
    # Place Your Code Here #
    Line(80, 50, 155, 135, lineWidth=5, fill="sienna")
    Line(315, 50, 240, 135, lineWidth=5, fill="sienna")
    Oval(155, 135, 40, 30, fill="tan", rotateAngle=45)
    Oval(240, 135, 40, 30, fill="tan", rotateAngle=-45)

    # Draw the label.
    # Place Your Code Here #
    Label("Little Drummer", 200, 20, fill="white", font="arial", size=30)
    cmu_graphics.run()


if __name__ == '__main__':
    main()
