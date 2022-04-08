from cmu_graphics import *


def main():
    # This draws the first layer of the cave.
    Circle(200, 200, 300, fill='sienna')
    Circle(200, 200, 300, opacity=30)

    # This draws the second layer of the cave.
    Oval(210, 220, 500, 400, fill='sienna')
    Oval(210, 220, 500, 400, opacity=60)

    # Draw the two inner layers of the cave using 4 ovals.
    # Place Your Code Here #
    Oval(220, 240, 400, 300, fill='sienna')
    Oval(220, 240, 400, 300, opacity=80)

    Oval(230, 260, 300, 200, fill='sienna')
    Oval(230, 260, 300, 200, opacity=90)

    cmu_graphics.run()


if __name__ == '__main__':
    main()
