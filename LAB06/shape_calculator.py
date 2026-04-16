import geometry_utils

print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter (e.g., circle_area)")

operations = {
    "circle_area": geometry_utils.circle_area,
    "circle_perimeter": geometry_utils.circle_perimeter,
    "rectangle_area": geometry_utils.rectangle_area,
    "rectangle_perimeter": geometry_utils.rectangle_perimeter,
    "triangle_area": geometry_utils.triangle_area
}

operation = input("Enter the operation you want to perform: ").strip()

try:
    if operation not in operations:
        raise ValueError("Invalid operation.")

    if operation.startswith("circle"):
        radius = float(input("Enter radius: "))
        result = operations[operation](radius)

    elif operation.startswith("rectangle"):
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        result = operations[operation](width, height)

    elif operation.startswith("triangle"):
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        result = operations[operation](base, height)

    print(f"Result: {result:.2f}")

except ValueError as e:
    print(f"Input Error: {e}")
except Exception:
    print("Input Error: Please enter valid numeric values.")