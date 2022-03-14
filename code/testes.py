objeto1 = [60, 50, 70, 50]
objeto2 = [140, 80, 70, 50]

collision = False

def axes_collision(point1, dist1, point2, dist2):
    if point1 < point2:
        if point2 < (point1 + dist1):
            return True
        return False

    elif objeto1[0] < (point2 + dist2):
        return True

if axes_collision(objeto1[0], objeto1[2], objeto2[0], objeto2[2]):
    collision = axes_collision(objeto1[1], objeto1[3], objeto2[1], objeto2[3])


print(collision)