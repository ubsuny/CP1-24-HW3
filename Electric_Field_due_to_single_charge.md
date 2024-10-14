# Classical Electrodynamics Exxample - Electric Field 

## 1. Introduction

The electric field \( \mathbf{E} \) is a fundamental concept in electromagnetism, representing the force per unit charge exerted on a test charge placed at a point in space. 
Classical Electrodynamics uses a field theory approach in order to explain the physics of interactions which is different from the newtonian way of approaching the natural phenomena ( describing the force between the masses directly). Maxwell's equations explain the charecteristics of Electriv Field in great detail and how it generates from time varying magnetic field.

Here I will document the theory of Electriv Fields at a graduate level, although explain the functioning of the code using the example of Coulomb's law.

## 2. Electric Field from Coulomb’s Law

For static (electrostatic) cases, the electric field \( \mathbf{E} \) due to a point charge \( q \) at a position \( \mathbf{r}_0 \) is given by Coulomb's law in its vector form:

$$
\mathbf{E}(\mathbf{r}) = \frac{1}{4 \pi \varepsilon_0} \frac{q (\mathbf{r} - \mathbf{r}_0)}{|\mathbf{r} - \mathbf{r}_0|^3}
$$
