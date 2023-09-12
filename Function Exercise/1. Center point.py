def closest_to_center(x1, y1, x2, y2):
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        return f"({x1//1:.0f}, {y1//1:.0f})"
    return f"({x2//1:.0f}, {y2//1:.0f})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closest_to_center(x1, y1, x2, y2))