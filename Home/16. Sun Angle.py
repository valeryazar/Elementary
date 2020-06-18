# 16 Task. Sun Angle
def sun_angle(time):
    hour, minute = list(map(int, time.split(':')))
    angle = 15 * hour + minute / 4 - 90
    return angle if 0 <= angle <= 180 else "I don't see the sun!"


if __name__ == '__main__':
    print("Result =", sun_angle("10:00"))