import numpy as np

def rgb2hex(rgb):
    return '#' + ''.join(hex(c)[2:].zfill(2).upper() for c in rgb)

def hex2rgb(hex_color):
    hc = hex_color[1:]
    arr = [hc[i:i+2] for i in range(0, len(hc), 2)]
    color = np.array([int(c, 16) for c in arr])
    return color

def interpolate_gradient(c1, c2, n=10):
    return [rgb2hex((c1 + t*(c2-c1)).astype(int)) for t in np.linspace(0, 1, n)]

c1 = np.array([255, 0, 0])
c2 = np.array([0, 255, 0])
print(interpolate_gradient(c1, c2, n=100))

c1_hex = '#FF0000'
c2_hex = '#00FF00'
print(hex2rgb(c1_hex))
print(hex2rgb(c2_hex))
