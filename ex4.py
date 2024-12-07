import turtle

# Define the points
points = [(2, -1), (1, 3), (4, 0), (4, 3), (5, 2)]


# Function to calculate cross product to determine the turn direction
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


# Jarvis March Algorithm to find the convex hull
def jarvis_march(points):
    # Find the leftmost point (smallest x-coordinate)
    leftmost = min(points, key=lambda p: p[0])

    convex_hull = []
    point_on_hull = leftmost

    while True:
        convex_hull.append(point_on_hull)
        next_point = points[0]  # Start with any point as the next candidate
        for candidate in points:
            if candidate == point_on_hull:
                continue
            # Check counterclockwise turn using cross product
            if next_point == point_on_hull or cross(point_on_hull, next_point, candidate) > 0:
                next_point = candidate
        point_on_hull = next_point
        if point_on_hull == leftmost:
            break
    return convex_hull


# Visualization function using turtle
def visualize(points, convex_hull):
    # Set up the turtle window
    screen = turtle.Screen()
    screen.setworldcoordinates(-1, -3, 6, 4)  # Adjust for better view

    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()

    # Draw points and display their coordinates
    for x, y in points:
        pen.goto(x, y)
        pen.dot(10, "red")
        pen.goto(x, y + 0.2)
        pen.write(f"({x},{y})", align="center", font=("Arial", 8, "normal"))

    # Draw the convex hull
    pen.goto(convex_hull[0][0], convex_hull[0][1])
    pen.pendown()
    pen.pensize(2)
    pen.color("blue")

    for point in convex_hull[1:]:
        pen.goto(point[0], point[1])

    pen.goto(convex_hull[0][0], convex_hull[0][1])  # Close the hull

    pen.penup()
    pen.goto(0, -2)
    pen.write("Convex Hull", align="center", font=("Arial", 16, "normal"))

    turtle.done()


# Find the convex hull using Jarvis March
convex_hull = jarvis_march(points)

# Print the convex hull
print("Convex Hull:", convex_hull)

# Visualize using turtle
visualize(points, convex_hull)
