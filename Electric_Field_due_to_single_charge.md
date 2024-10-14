# Classical Electrodynamics Exxample - Electric Field 

## 1. Introduction

The electric field \( \mathbf{E} \) is a fundamental concept in electromagnetism, representing the force per unit charge exerted on a test charge placed at a point in space. 
Classical Electrodynamics uses a field theory approach in order to explain the physics of interactions which is different from the newtonian way of approaching the natural phenomena ( describing the force between the masses directly). Maxwell's equations explain the charecteristics of Electriv Field in great detail and how it generates from time varying magnetic field.

Here I will document the theory of Electriv Fields at a graduate level, although explain the functioning of the code using the example of Coulomb's law.

## 2. Electric Field from Coulomb’s Law

For static (electrostatic) cases, the electric field due to a point charge at a position is given by Coulomb's law in its vector form:

$$
\mathbf{E}(\mathbf{r}) = \frac{1}{4 \pi \varepsilon_0} \frac{q (\mathbf{r} - \mathbf{r}_0)}{|\mathbf{r} - \mathbf{r}_0|^3}
$$

Where:

\\( \mathbf{r} \\) is the position vector where the electric field is being measured.

\\( \mathbf{r}_0 \\) is the position vector of the point charge.

\\( q \\) is the magnitude of the charge.

\\( \varepsilon_0 = 8.85 \times 10^{-12} \, \text{C}^2/\text{Nm}^2 \\) is the permittivity of free space.

This expression shows that the electric field due to a point charge decreases with the square of the distance and is directed radially outward from the charge for positive \( q \) (inward for negative \( q \)).
