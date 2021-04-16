import matplotlib.pyplot as plt

# Create grapgh
def create_graph_paper():
    global paper
    paper = plt.gca()
    plt.axis("scaled")

# Create Coordinate class
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def reflect(self, axis, inset=False):
        if axis == "x":
            temporary_y = self.y * -1

            if inset:
                self.y = temporary_y
            else:
                return (self.x, temporary_y)
        else:
            temporary_x = self.x * -1

            if inset:
                self.x = temporary_x
            else:
                return (temporary_x, self.y)

    def translate(self, move_x, move_y, inset=False):
        if inset:
            self.x += move_x
            self.y += move_y
        else:
            return (self.x + move_x, self.y + move_y)
    
    def rotate(self, degree, direction, inset=False):
        if inset:
            if degree == 180:
                self.x *= -1
                self.y *= -1
            elif (degree == 90 and direction == "CCW") or (degree == 270 and direction == "CW"):
                temporary_x = self.x
                temporary_y = self.y

                self.x = temporary_y * -1
                self.y = temporary_x
            else:
                temporary_x = self.x
                temporary_y = self.y

                self.x = temporary_y
                self.y = temporary_x * -1
        else:
            if degree == 180:
                return (self.x * -1, self.y * -1)
            elif (degree == 90 and direction == "CCW") or (degree == 270 and direction == "CW"):
                temporary_x = self.x
                temporary_y = self.y

                return (temporary_y * -1, temporary_x)
            else:
                temporary_x = self.x
                temporary_y = self.y

                return (temporary_y, temporary_x * -1)


    def together(self):
        return (self.x, self.y)

def reflect_points(coordinates, axis, inset=False):
    if inset:
        for i in coordinates:
            if axis == "x":
                i.y = i.y * -1
            else:
                i.x *= -1
    else:
        image_points = []
        for i in coordinates:
            if axis == "x":
                image_points.append((i.x, i.y * -1))
            else:
                image_points.append((i.x * -1, i.y))

        return image_points

def tranlate_points(coordinates, move_x, move_y, inset=False):
    if inset:
        for i in coordinates:
            i.x += move_x
            i.y += move_y
    else:
        image_points = []
        for i in coordinates:
            image_points.append((i.x + move_x, i.y + move_y))
        
        return image_points

def rotate_points(coordinates, degree, direction, inset=False):
    if inset:
        for i in coordinates:
            if degree == 180:
                i.x *= -1
                i.y *= -1
            elif (degree == 90 and direction == "CCW") or (degree == 270 and direction == "CW"):
                temporary_x = i.x
                temporary_y = i.y

                i.x = temporary_y * -1
                i.y = temporary_x
            else:
                temporary_x = i.x
                temporary_y = i.y

                i.x = temporary_y
                i.y = temporary_x * -1
    else:
        for i in coordinates:
            if degree == 180:
                return (i.x * -1, i.y * -1)
            elif (degree == 90 and direction == "CCW") or (degree == 270 and direction == "CW"):
                temporary_x = i.x
                temporary_y = i.y

                return (temporary_y * -1, temporary_x)
            else:
                temporary_x = i.x
                temporary_y = i.y

                return (temporary_y, temporary_x * -1)


class Polygon():
    def __init__(self, points, closed=None, fill=None, edgecolor=None):
        self.edgecolor = edgecolor
        self.points = [(i.x, i.y) for i in points]
        self.fill = fill
        self.closed = closed
    
    def draw_on_paper(self):
        global paper

        blah_blah_polygon_blaaaah = plt.Polygon(self.points, closed=self.closed, fill=self.fill, edgecolor=self.edgecolor)

        paper.add_patch(blah_blah_polygon_blaaaah)
    
    def present(self):
        plt.show()
