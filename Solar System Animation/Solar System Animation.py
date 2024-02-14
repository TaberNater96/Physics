"""

Vpython Solar Sytem Project 2.0
Computational Physics Term Project

Created By: Elijah Taber
Date: June 10, 2021

"""

from vpython import *
import numpy as np


print("""
Welcome to Elijah's solar system project 2.0!
Please restart the Kernal before running the simulation.
Press the play button when the simulation is ready and select the planet you wish to follow around the Sun!
Make sure and scroll in to see the inner planets.
      """)

#Radius of each planetary object in km
sunRadius = 69550
mercuryRadius = 2440
venusRadius = 6052
earthRadius = 6371
marsRadius = 3386
jupiterRadius = 69173
saturnRadius = 57316
saturnRingRadius = 120134
uranusRadius = 25362
neptuneRadius = 24622
plutoRadius = 1188.3

#Orbital radius of each planet around the Sun in km
sunOrbitRadius = 1.0
mercuryOrbitRadius = 69.27e6
venusOrbitRadius = 107.49e6
earthOrbitRadius = 151.78e6
marsOrbitRadius = 249.63e6
jupiterOrbitRadius = 755.36e6
saturnOrbitRadius = 1.4875e9
uranusOrbitRadius = 2.9543e9
neptuneOrbitRadius = 4.4754e9
plutoOrbitRadius = 5.9e9

#Creating the spherical objects for each planet and the Sun
#Note if the user wishes to remove the make trail, then simply set it to False
sun = sphere( radius = sunRadius, texture = "https://i.imgur.com/XdRTvzj.jpg", emissive = True )
mercury = sphere( radius = mercuryRadius, texture = "https://i.imgur.com/SLgVbwD.jpg", make_trail = True, trail_radius = mercuryRadius * 0.5 )
venus = sphere( radius = venusRadius, texture = "https://i.imgur.com/7VTEX2w.jpeg", make_trail = True, trail_color = color.green, trail_radius = venusRadius * 0.5 )
earth = sphere( radius = earthRadius, texture = textures.earth, make_trail = True, trail_color = color.blue, trail_radius = earthRadius * 0.5 )
mars = sphere( radius = marsRadius, texture = "https://i.imgur.com/Mwsa16j.jpg", make_trail = True, trail_color = color.red, trail_radius = marsRadius * 0.5 ) 
jupiter = sphere( radius = jupiterRadius, texture = "https://i.imgur.com/RMMtt0K.jpg", make_trail = True, trail_color = color.orange, trail_radius = jupiterRadius * 0.5 )
saturn = sphere( radius = saturnRadius, texture = "https://i.imgur.com/02Kt4gy.jpg", make_trail = True, trail_color = color.yellow, trail_radius = saturnRadius * 0.5 )
uranus = sphere( radius = uranusRadius, texture = "https://i.imgur.com/2kZNvFw.jpg", make_trail = True, trail_color = color.cyan, trail_radius = uranusRadius * 0.5 )
neptune = sphere( radius = neptuneRadius, texture = "https://i.imgur.com/lyLpoMk.jpg", make_trail = True, trail_color = color.blue, trail_radius = neptuneRadius * 0.5 )
pluto = sphere( radius = plutoRadius, texture = "https://i.imgur.com/ds7WOMu.jpg", make_trail = True, trail_color = vector(1,0.7,0.2), trail_radius = plutoRadius * 0.5 )

solar_system = {'Sun': sun, 'Mercury': mercury, 'Venus': venus, 'Earth': earth, 'Mars': mars,
                    'Jupiter': jupiter, 'Saturn': saturn, 'Uranus': uranus, 'Neptune': neptune, 'Pluto': pluto}

#Orbital Period, these values represent how many Earth days each planet orbits the Sun, therefore
#the orbital rate will be the inverse of these values as seen in the loop function
sunOrbitRate = 27.0 #rotates around its axis once per 27 Earth days
mercuryOrbitRate = 88.0
venusOrbitRate = 224.7
earthOrbitRate = 365.3
marsOrbitRate = 687.0
jupiterOrbitRate = 4331.6
saturnOrbitRate = 10759.2
uranusOrbitRate = 30660
neptuneOrbitRate = 60225
plutoOrbitRate = 90520

#Ecliptic coordinates for axial tilt rotation, these values are correlated to
#their given rotational tilt (or epsilon) with respect to the 2D orbital plane 
#that revolves around the Sun, the numbers are converted from degrees to radians
sunEpsilon = radians(0.1265364)
mercuryEpslion = radians(0.0349066)
venusEpsilon = radians(0.0523599)
earthEpsilon = radians(0.4101524)
marsEpsilon = radians(0.43964844)
jupiterEpsilon = radians(0.0349066)
saturnEpsilon = radians(0.471239)
uranusEpsilon = radians(1.71042)
neptuneEpsilon = radians(0.488692)
plutoEpsilon = radians(0.994838)

#Initialize each planet's angle on a single 2D plane around the Sun
mercuryAngle = 0
venusAngle = 0
earthAngle = 0
marsAngle = 0
jupiterAngle = 0
saturnAngle = 0
uranusAngle = 0
neptuneAngle = 0
plutoAngle = 0

#The following variables define glowscripts graphing capabilities that plots the position of the planet's orbit around the 
#Sun in real time. If the user wishes to see the progression of the plotting for the planets faster, then set the rate to a
#higher number
tgraph = graph(title = "Position of Planets Orbiting the Sun", xtitle="Position in x-direction (km)", ytitle="Position in z-direction(km)", background = color.black)
rm = gcurve(color = color.white, label="Mercury")
rv = gcurve(color = color.green, label = "Venus")
re = gcurve(color = color.magenta, label = "Earth")
rM = gcurve(color = color.red, label = "Mars" )
rj = gcurve(color = color.orange, label = "Jupiter")
rs = gcurve(color = color.yellow, label = "Saturn")
ru = gcurve(color = color.cyan, label = "Uranus")
rn = gcurve(color = color.blue, label = "Neptune")
rp = gcurve(color = vector(1,0.7,0.2), label = "Pluto")

#Creates a subtle sunlight animation to give the full affect of the Sun on each planet
sunlight = local_light( pos = vec(0,0,0), color=color.white )

#Initializing a standard rate for how fast the program will animate
programSpeed = 1.0

#Pauses the animation at the beginning in order to allow the user to scroll in and find the planet they want to view
scene.pause() 

#This is the only consistent way I could figure out to make make a space background for the animation, but unfortunately
#vpython is very glitchy when inside of another sphere and only looks good when viewed from middle to outer planets. If the
#user wishes to implement the following code into the program, the stars will disappear around the orbit of Mars
"""
sphere(pos=vector(0,0,0),texture="https://i.imgur.com/1nVWbbd.jpg",radius=45e6,shininess=0)
"""

#This function allows the user to select a planetary object in order to have the camera follow it
def camera_menu(m):
    if m.selected in solar_system:
        scene.camera.follow(solar_system[m.selected])

#If the user wishes to roam freely around the solar system, then comment out the following line
menu(choices=list(solar_system.keys()), bind=camera_menu, pos=scene.title_anchor) 

#Continuously change the position of each planet around the Sun in the x and z plane
while (True):
    #To simulate the real orbital speeds of our solar system, set rate to the painfully slow speed of 1 
    rate(10000) 
    #Note that the orbital radius of each planet is scaled down by 1/150th so that the user can see and compare the distances 
    #of each planet. If the user wishes to view the full scale of our solar system, each planet will be incredibly far away
    #from one another (especially past Jupiter) and will not be able to see other planets since our solar system is so big
    #and glowscript does not handle distant onjects very well
    mercury.pos = vec( mercuryOrbitRadius/150 * cos(radians(mercuryAngle)), 0, mercuryOrbitRadius/150 * sin(radians(mercuryAngle)) ) 
    venus.pos = vec( venusOrbitRadius/150 * cos(radians(venusAngle)), 0, venusOrbitRadius/150 * sin(radians(venusAngle)) ) 
    earth.pos = vec( earthOrbitRadius/150 * cos(radians(earthAngle)), 0, earthOrbitRadius/150 * sin(radians(earthAngle)) )
    mars.pos = vec( marsOrbitRadius/150 * cos(radians(marsAngle)), 0, marsOrbitRadius/150 * sin(radians(marsAngle)) ) 
    jupiter.pos = vec( jupiterOrbitRadius/150 * cos(radians(jupiterAngle)), 0, jupiterOrbitRadius/150 * sin(radians(jupiterAngle)) ) 
    saturn.pos = vec( saturnOrbitRadius/150 * cos(radians(saturnAngle)), 0, saturnOrbitRadius/150 * sin(radians(saturnAngle)) ) 
    uranus.pos = vec( uranusOrbitRadius/150 * cos(radians(uranusAngle)), 0, uranusOrbitRadius/150 * sin(radians(uranusAngle)) )
    neptune.pos = vec( neptuneOrbitRadius/150 * cos(radians(neptuneAngle)), 0, neptuneOrbitRadius/150 * sin(radians(neptuneAngle)) )
    pluto.pos = vec( plutoOrbitRadius/150 * cos(radians(plutoAngle)), 0, plutoOrbitRadius/150 * sin(radians(plutoAngle)) )
    
    #Creating the orbital speed ratio for each planet, the closer the planet is to the Sun, the faster the rate will be
    mercuryAngle -= 1/mercuryOrbitRate * programSpeed
    venusAngle -= 1/venusOrbitRate * programSpeed
    earthAngle -= 1/earthOrbitRate * programSpeed
    marsAngle -= 1/marsOrbitRate * programSpeed
    jupiterAngle -= 1/jupiterOrbitRate * programSpeed
    saturnAngle -= 1/saturnOrbitRate * programSpeed
    uranusAngle -= 1/uranusOrbitRate * programSpeed
    neptuneAngle -= 1/neptuneOrbitRate * programSpeed
    plutoAngle -= 1/plutoOrbitRate * programSpeed
    
    #Rotating each celestial body about its respective axis, each planetary object aside from Mercury has both a rotation
    #and a tilt with respect to the solar systems 2D orbital plane. The axial tilt values that was converted into radians
    #earlier are now vectorized using eccliptic vector formulas for a 3D objecct that is angled in the x-y plane
    sun.rotate (angle = sunEpsilon, axis = vector(np.sin(sunEpsilon), np.cos(sunEpsilon), 0))
    #Mercury is tidally locked to the Sun and does not rotate on its axis, but does have a slight tilt
    mercury.rotate (angle = 0, axis = vector(np.sin(mercuryEpslion), np.cos(mercuryEpslion), 0))
    venus.rotate (angle = venusEpsilon, axis = vector(np.sin(venusEpsilon), np.cos(venusEpsilon), 0))
    earth.rotate (angle = earthEpsilon, axis = vector(np.sin(earthEpsilon), np.cos(earthEpsilon), 0))
    mars.rotate (angle = marsEpsilon, axis = vector(np.sin(marsEpsilon), np.cos(marsEpsilon), 0))
    jupiter.rotate (angle = jupiterEpsilon, axis = vector(np.sin(jupiterEpsilon), np.cos(jupiterEpsilon), 0))
    saturn.rotate (angle = saturnEpsilon, axis = vector(np.sin(saturnEpsilon), np.cos(saturnEpsilon), 0))
    uranus.rotate (angle = uranusEpsilon, axis = vector(np.sin(uranusEpsilon), np.cos(uranusEpsilon), 0))
    neptune.rotate (angle = neptuneEpsilon, axis = vector(np.sin(neptuneEpsilon), np.cos(neptuneEpsilon), 0))
    pluto.rotate (angle = plutoEpsilon, axis = vector(np.sin(plutoEpsilon), np.cos(plutoEpsilon), 0))
    
    #Plotting the real time positions of each planet around the Sun
    rm.plot(mercury.pos.x, mercury.pos.z)
    rv.plot(venus.pos.x, venus.pos.z)
    re.plot(earth.pos.x, earth.pos.z)
    rM.plot(mars.pos.x, mars.pos.z)
    rj.plot(jupiter.pos.x, jupiter.pos.z)
    rs.plot(saturn.pos.x, saturn.pos.z)
    ru.plot(uranus.pos.x, uranus.pos.z)
    rn.plot(neptune.pos.x, neptune.pos.z)
    rp.plot(pluto.pos.x, pluto.pos.z)
    
