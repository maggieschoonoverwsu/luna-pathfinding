import random

def generate_coordinates(num_points=10, x_range=(-180, 180), y_range=(-90, 90)):
    """
    Generates an array of coordinate pairs (x, y) with floating point values.
    :param num_points: Number of coordinate pairs to generate.
    :param x_range: Tuple representing the range (min, max) for x values.
    :param y_range: Tuple representing the range (min, max) for y values.
    :return: List of tuples containing (x, y) coordinates.
    """
    coordinates = [(random.uniform(*x_range), random.uniform(*y_range)) for _ in range(num_points)]
    return coordinates

if __name__ == "__main__":
    num_points = 10  # Change as needed
    coords = generate_coordinates(num_points)
    print("Generated Coordinates:")
    print(coords)