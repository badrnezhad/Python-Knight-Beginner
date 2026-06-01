def turn_off_devices():
    pass


def read_from_temperature_device() -> int:
    pass


is_above_30_degree = None

if read_from_temperature_device() > 30:
    is_above_30_degree = False

if is_above_30_degree:
    turn_off_devices()
