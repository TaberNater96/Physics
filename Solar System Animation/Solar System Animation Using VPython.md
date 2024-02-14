# Solar System Animation Using VPython

The "Vpython_Solar_System_Model" project utilizes the VPython 3D animation library to create a solar system animation. Planetary objects are modeled as spheres with customizable properties like position, radius, color, texture, and trail. The program starts by defining basic variables for each planet's radius and orbital radius, sourced from NASA's planetary data for accuracy.

Planets are positioned in a 3D vector space, using trigonometric functions to simulate orbital motion around a central sun located at vector (0,0,0). Each planet's movement is controlled through a loop, adjusting its position vector based on its radius and an incrementally changing angle value. This approach creates a circular orbital path.

Apart from orbiting the sun, planets also rotate around their axis (except Mercury), with VPython's rotation function enabling this. The axial rotation is based on each planet's ecliptic coordinates, converted into radians for VPython.

The model also takes into account the varied orbital rates of planets, inversely proportional to their Earth-day orbital periods. An additional feature is the VPython graphing function, which tracks real-time positions of planets, useful for understanding their distances and movements relative to each other.

The project aims to provide a scaled simulation of the solar system, demonstrating the vast distances and rates between planets. It highlights VPython's capabilities for basic 3D object animation, though acknowledging its limitations compared to more advanced graphics software. This model serves as a simple representation of more complex celestial animations and sets a foundation for future enhancements and more dynamic simulations within VPython's framework.
