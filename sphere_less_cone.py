# Volume Sphere Minus Cone (geometric/trigonometric approach)

from numpy import pi, sin, cos


def ball_less_cone(radius, angle=pi/4, deg=False):

    """
    Radians are default unit of angle. If no angle is given, pi/4 radians is assumed.
    For degrees, type 'True' into argument 3.
    """
    
    if deg is True:
        angle = angle * pi / 180
    else:
        pass
    
    # Volume Sphere
    volume_sphere = 4/3 * pi * radius**3

    # Determine Volume of cone
    r_cone = radius * cos(angle)  # Determine radius of cone using trig
    h_cone = radius * sin(angle)  # Determine radius of cone using trig
    volume_cone = 1/3 * pi * r_cone**2 * h_cone  # Calculate volume

    # Volume of spherical cap
    h_cap = radius - h_cone # height of cap is difference of radius and height of cone
    r_cap = radius # radius is simply radius given
    volume_cap = pi * h_cap**2 / 3 * (3*r_cap - h_cap) # Calculate volume

    # Calculate volume final
    volume = volume_sphere - (volume_cone + volume_cap)
    return volume
