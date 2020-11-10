"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
must be rounded to the closest valid value.
Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
The following are examples of expected output values:
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


def rgb_filter(chunk):
    result = ''
    if 9 < chunk <= 255:
        result = str(hex(chunk))[2::].upper()
    elif chunk < 0:
        result = '00'
    elif chunk > 255:
        result = 'FF'
    elif chunk <= 9:
        result = '0' + str(hex(chunk))[2::].upper()

    return result


def rgb(r, g, b):
    return '{0}{1}{2}'.format(
        rgb_filter(r),
        rgb_filter(g),
        rgb_filter(b),
    )


print(rgb(255, 255, 255))
print(rgb(148, 0, 300))
print(rgb(-20, 275, 125))
