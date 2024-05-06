<div align="center">
  <h2><b>Physics Projects<b></h2>
</div>

&nbsp;

<details>
  <summary><b>Click Here To Navigate To Each Repository<b></summary>
    
  - [Fourier and Lorentz Transformations](https://github.com/TaberNater96/Physics/blob/main/Fourier%20and%20Lorentz%20Transformations/Fourier%20and%20Lorentz%20Transformations.ipynb)
  - [Solar System Animation (Term Project)](https://github.com/TaberNater96/Physics/tree/main/Solar%20System%20Animation)
  - [Light and Orbital Mechanics](https://github.com/TaberNater96/Physics/blob/main/Light%20and%20Orbital%20Mechanics/Light%20and%20Orbital%20Mechanics.ipynb)
  - [Schrodinger Equations and Sunspot Distributions](https://github.com/TaberNater96/Physics/blob/main/Schrodinger%20Equations%20and%20Sunspot%20Distributions/Schrodinger%20Equations%20and%20Sunspot%20Distributions.ipynb)
</details>

&nbsp;

My first encounter with programming stemmed from a course I took during my Physics degree called "Computational Physics" where we needed to calculate and visualize complex physics problems using Python. This programming language became my tool of choice for the years to come, enabling me to dive deep into data analysis and calculations that push the boundaries of what we understand about physics, skills that have become invaluable throughout my entire academic career. This particular repository is a testament to this journey, showcasing projects where theory meets practice, from calculating complex calculus equations to producing insightful and visually unique images. These projects represent just the beginning of my academic achievements and the depth of knowledge I've gained in both my Physics and Data Science studies. 

Throughout a single 10-week term, I immersed myself in computational physics projects and assignments without any prior exposure to programming. This experience is a testament to my quick learning abilities and my capacity to tackle complex and unfamiliar challenges head-on. These projects marked the beginning of my journey to where I stand today, igniting my passion for data, science, and programming.

<div align="center">
  <h2>Quick Summaries (TLDR)</h2>
</div>

## Table of Contents
- [Pixel Focussing Using Fourier Transformations](#pixel-focussing-using-fourier-transformations)
- [Solar System Animation](#solar-system-animation)
- [Light Wavelength and Intensities](#light-and-orbital-mechanics)
- [Schrodinger Equations and Sunspot Distributions](#schrodinger-equations-and-sunspot-distributions)
- [Lorenz Equations and the Strange Attractor](#lorenz-equations-and-the-strange-attractor)

<div id="pixel-focussing-using-fourier-transformations" align="center">
  <h2>Pixel Focussing Using Fourier Transformations</h2>
</div>

This is probably my favorite transformation that I did in my computational physics class, where I took a blurred image in the form of a matrix and performed a complex inverse array transformation to unblur an image.

<div align="center">
<img src="https://github.com/TaberNater96/Physics/blob/main/Fourier%20and%20Lorentz%20Transformations/Images/Blur.png?raw=true" width="600" height="550">
</div>

<div align="center">
<img src="https://github.com/TaberNater96/Physics/blob/main/Fourier%20and%20Lorentz%20Transformations/Images/Grid%20Sample.png?raw=true" width="600" height="550">
</div>

<div align="center">
<img src="https://github.com/TaberNater96/Physics/blob/main/Fourier%20and%20Lorentz%20Transformations/Images/Focussed.png?raw=true" width="600" height="550">
</div>

<div id="solar-system-animation" align="center">
  <h2>Solar System Animation</h2>
</div>

For my term project in computational physics, I developed an animation that accurately depicts the solar system using, modeling the orbits of each planet. The code for this animation is built using VPython, otherwise known as GlowScript. This animation is a true-to-life representation, where the scale of the planets is proportional to the Sun, and each planet follows its real-life orbital path, velocity, rotation, and angle. The animation here is sped up to 10,000 times faster than in real life, but can be adjusted down to 1 if desired.

<div align="center">
<img src="https://github.com/TaberNater96/Physics/blob/main/Solar%20System%20Animation/Animations/Solar%20System%20Animation.gif?raw=true" width="800" height="400">
</div>

Although the dropdown button for planet selection is not visible during recordings, the actual program allows users to select any planet and observe its orbit around the Sun. Going beyond the basics, I integrated an animated graph that updates in real-time to track and plot the distances of the planets throughout the animation, showcasing the vast scale of our solar system.

<div align="center">
<img src="https://github.com/TaberNater96/Physics/blob/main/Solar%20System%20Animation/Animations/Graph%20Animation.gif?raw=true" width="600" height="400">
</div>

<div id="light-and-orbital-mechanics" align="center">
  <h2>Light Wavelength and Intensities</h2>
</div>

This assignment explores the diffraction limit of telescopes through an analysis of light diffraction patterns using Bessel functions. It demonstrates the application of Simpson's Rule to compute these functions, which are crucial for describing the intensity variations in the diffraction pattern as light passes through a telescope's circular aperture. The calculated Bessel functions illustrate the oscillatory nature typical of wave phenomena.

<div align="center">
<img src="https://github.com/TaberNater96/Physics/blob/main/Light%20and%20Orbital%20Mechanics/Images/Wave%20Diffraction.png?raw=true" width="600" height="400">
</div>

&nbsp;

Additionally, the code generates a detailed density plot of the circular diffraction pattern in the focal plane, showing how intensity varies with radial distance from the center. This visualization effectively highlights the central peak and surrounding concentric rings, illustrating the fundamental limits of resolution imposed by the physical properties of telescopes in astronomical observations.

<div align="center">
<img src="https://github.com/TaberNater96/Physics/blob/main/Light%20and%20Orbital%20Mechanics/Images/Lightwave%20Intensity.png?raw=true" width="600" height="550">
</div>

<div id="schrodinger-equations-and-sunspot-distributionss" align="center">
  <h2>Schrodinger Equations and Sunspot Distributions</h2>
</div>

This assignment mainly focussed on glycolysis models, Schrodinger Equations, electron levels, and sunspot distributions. The following plot shows how an electron in a well of *V = 20 eV* and *w = 1 nm*, given 3 different energies for 6 different energy levels of the particle.

<div align="center">
<img src="https://github.com/TaberNater96/Physics/blob/main/Schrodinger%20Equations%20and%20Sunspot%20Distributions/Images/Eelectron%20Energy%20Levels.png?raw=true" width="600" height="400">
</div>

After going through other quantum processes, the assignment turned to sunspot distributions. The objective here was to observe the fluctuations on a particular cycle given a distribution of sunspots. After a frequency was determined, a Fourier Transformation was applied to extract out a noticeable peak at a nonzero value *k*. This is a representation that there is one frequency in the Fourier Series that has a higher amplitude than the others around it, indicating a large sine-wave term with this frequency, which corresponds to the periodic wave seen in the original data.

<div align="center">
<img src="https://github.com/TaberNater96/Physics/blob/main/Schrodinger%20Equations%20and%20Sunspot%20Distributions/Images/Sunspot%20Data.png?raw=true" width="600" height="400">
</div>

&nbsp;

<div align="center">
<img src="https://github.com/TaberNater96/Physics/blob/main/Schrodinger%20Equations%20and%20Sunspot%20Distributions/Images/FT%20Sunspots.png?raw=true" width="600" height="400">
</div>

<div id="lorenz-equations-and-the-strange-attractor" align="center">
  <h2>Lorenz Equations and the Strange Attractor</h2>
</div>

One of the most celebrated sets of differential equations in physics is the Lorenz equations, which were first studied by Edward Lorenz in 1963, who derived them from a simplified model of weather patterns. The reason for their fame is that they were one of the first incontrovertible examples of *deterministic chaos*, the occurrence of apparently random motion even though there is no randomness built into the equations. Producing a plot of z vs x creates a butterfly shaped plot where the plot never repeats itself.

<div align="center">
<img src="https://github.com/TaberNater96/Physics/blob/main/Fourier%20and%20Lorentz%20Transformations/Images/Random.png?raw=true" width="600" height="400">
</div>

<div align="center">
<img src="https://github.com/TaberNater96/Physics/blob/main/Fourier%20and%20Lorentz%20Transformations/Images/The%20Strange%20Attractor.png?raw=true" width="600" height="400">
</div>










