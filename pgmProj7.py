from turtlegraphics import Turtle
class Shape:

    def __init__(self, turtle, name = ""):
        self._turtle = turtle
        self._name = name
        
    def getName(self):
        """ """
        return self._name


class LineSegment(Shape):
    """ Represents a line segment."""

    def __init__(self, turtle, start=(0,0), end=(0,0), name = ""):
        """Constructor creates a segment with the given
        start and end points."""
        Shape.__init__(self, turtle, name)
        self._start = start
        self._end = end

    def getStart(self):
        """Resets the starting point to the given ordered pair."""
        return self._start

    def getEnd(self):
        """Resets the end point to the given ordered pair."""
        return self._end

    def draw(self):
        self._turtle.up()
        x, y = self._start
        self._turtle.move(x, y)
        self._turtle.down()
        x, y = self._end
        self._turtle.move(x, y)
        return 5

    def __str__(self):
        """Returns the string representation of the line segment."""

           

class Circle(Shape):
    """Represents a circle."""
    
    def __init__(self, turtle, center=(0,0), radius=1, name = ""):
        """Constructor creates a circle with the
        given center point and radius."""
        Shape.__init__(self, turtle, name)
        self._center = center
        self._radius = radius

    def getCenter(self):
        """Resets the center point to the given ordered pair."""
        return self._center

    def getRadius(self):
        """Sets the radius of the circle to the given length."""
        return self._radius

    def draw(self):                #I know this part of drawing the Circle needs work
        self._turtle.up()
        x, y = self._center
        self._turtle.move(x, y) 
        self._turtle.down()
        z = self._radius
        self._turtle.circle(z)
        
        return


class Rectangle(Shape):
    """Represents a rectangle."""
    def __init__(self, turtle, upLeft=(0,0), lowRight=(0,0), name = ""):
        """Constructor creates a rectangle with the
        given upper left and lower right points."""
        Shape.__init__(self, turtle, name)
        self._upLeft = upLeft
        self._lowRight = lowRight

    def getUpLeft(self):
        """Resets the upper left corner of the rectangle."""
        return self._upLeft

    def getLowRight(self):
        """Resets the lower right corner of the rectangle."""
        return self._lowRight

    def draw(self):
        self._turtle.up()
        x, y = self._upLeft
        self._turtle.move(x, y)
        self._turtle.down()
        a, b = self._lowRight
        self._turtle.move(a, y)
        self._turtle.move(a, b)
        self._turtle.move(x, b)
        return
