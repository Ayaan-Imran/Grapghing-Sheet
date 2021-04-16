import GrapghSheet as gs

# Create platform
gs.create_graph_paper()

# Create pre-image points
A = gs.Coordinate(1, 1)
B = gs.Coordinate(3, 3)
C = gs.Coordinate(5, 1)

# Create image points
image_points = gs.tranlate_points([A, B, C], 3, -4)

# Create Polygon
my_triangle = gs.Polygon([A, B, C], fill="Green", edgecolor="Orange")
my_triangle.draw_on_paper()
my_triangle.present()