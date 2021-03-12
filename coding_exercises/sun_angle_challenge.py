def sun_angle(time: str):
    """Get the angle of the sun based on what time it is"""
    times = time.split(':')
    hours = int(times[0])
    minutes = int(times[1])
    if hours < 6:
        return "I don't see the sun!"
    if hours >= 18 and minutes > 0:
        return "I don't see the sun!"
    if hours == 6 and minutes == 0:
        return 0
    if hours >= 6:
        hours_degrees = (hours - 6) * 15
        minutes_degrees = minutes * .25
        return hours_degrees + minutes_degrees


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"