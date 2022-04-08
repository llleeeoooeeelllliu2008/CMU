from cmu_graphics import *


def onMousePress(mouseX, mouseY):
    # Change your code so that the circles are drawn where you press your mouse!
    # (HINT: Be sure to read the comment at the top of the editor!)
    # Fix Your Code Here #
    Circle(mouseX, mouseY, 15, fill='steelBlue')


def main():
    # Below the editor are Test Cases. When you check your code, we compare your code
    # with the solution for each test case. You can add/remove the test case from your
    # code by clicking on the + or - sign that appears when you hover over it!
    app.background = 'moccasin'

    cmu_graphics.run()


if __name__ == '__main__':
    main()
