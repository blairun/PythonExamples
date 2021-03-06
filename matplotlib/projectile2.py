''' projectile_motion.py
projectile motion equations:
height = y(t) = hs + (t * v * sin(a)) - (g * t*t)/2
distance = x(t) = v * cos(a) * t
where:
t is the time in seconds
v is the muzzle velocity of the projectile (meters/second)
a is the firing angle with repsect to ground (radians)
hs is starting height with respect to ground (meters)
g is the gravitational pull (meters/second_square)
tested with Python27/Python33  by  vegaseat  20mar2013
'''
import math
def projectile_xy(v, a, hs=0.0, g=9.8):
    '''
    calculate a list of (x, y) projectile motion data points
    where:
    x axis is distance (or range) in meters
    y axis is height in meters
    v is muzzle velocity of the projectile (meter/second)
    a is the firing angle with repsect to ground (radians)
    hs is starting height with respect to ground (meters)
    g is the gravitational pull (meters/second_square)
    '''
    data_xy = []
    t = 0.0
    while True:
        # now calculate the height y
        y = hs + (t * v * math.sin(a)) - (g * t * t)/2
        # projectile has hit ground level
        if y < 0:
            break
        # calculate the distance x
        x = v * math.cos(a) * t
        # append the (x, y) tuple to the list
        data_xy.append((x, y))
        # use the time in increments of 0.1 seconds
        t += 0.1
    return data_xy
# use a firing angle of 45 degrees
d = 45
a = math.radians(d)  # radians
# muzzle velocity of the projectile (meters/second)
v = 100
data_45 = projectile_xy(v, a)
# find maximum height ...
point_height_max = max(data_45, key = lambda q: q[1])
xm, ym = point_height_max
print('''
    Projectile Motion ...
Using a firing angle of {} degrees
and a muzzle velocity of {} meters/second
the maximum height is {:0.1f} meters
at a distance of {:0.1f} meters,'''.format(d, v, ym, xm))
# find maximum distance ...
x_max = max(data_45)[0]
print("the maximum distance is {:0.1f} meters.".format(x_max))
''' result ...
    Projectile Motion ...
Using a firing angle of 45 degrees
and a muzzle velocity of 100 meters/second
the maximum height is 255.1 meters
at a distance of 509.1 meters,
the maximum distance is 1018.2 meters.
'''