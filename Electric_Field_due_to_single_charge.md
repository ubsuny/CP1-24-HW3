# Classical Electrodynamics Exxample - Electric Field 

## 1. Introduction

The electric field \( \mathbf{E} \) is a fundamental concept in electromagnetism, representing the force per unit charge exerted on a test charge placed at a point in space. 
Classical Electrodynamics uses a field theory approach in order to explain the physics of interactions which is different from the newtonian way of approaching the natural phenomena ( describing the force between the masses directly). Maxwell's equations explain the charecteristics of Electriv Field in great detail and how it generates from time varying magnetic field.

Here I will document the theory of Electriv Fields at a graduate level, although explain the functioning of the code using the example of Coulomb's law due to a single charge.

## 2. Electric Field from Coulomb’s Law

For static (electrostatic) cases, the electric field due to a point charge at a position is given by Coulomb's law in its vector form:

$$
\mathbf{E}(\mathbf{r}) = \frac{1}{4 \pi \varepsilon_0} \frac{q (\mathbf{r} - \mathbf{r}_0)}{|\mathbf{r} - \mathbf{r}_0|^3}
$$

Where:

$r$ is the position vector where the electric field is being measured.

$r_0$ is the position vector of the point charge.

$q$ is the magnitude of the charge.

$\varepsilon_0 = 8.85 \times 10^{-12} \, \text{C}^2/\text{Nm}^2$ is the permittivity of free space.

This expression shows that the electric field due to a point charge decreases with the square of the distance and is directed radially outward from the charge for positive $q$ (inward for negative $q$).

## 4. Electric Fields in Time-Varying Situations

In time-varying fields, the concept of an electric field becomes more dynamic, governed by **Maxwell’s equations**. The electric field is no longer purely a function of the charge distribution but is influenced by changing magnetic fields as well.

Maxwell's equations provide a complete description of the electric field. In differential form, these are:

1. **Gauss’s law for electricity**:
   
$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}
$$

3. **Faraday’s law of induction**:

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$

4. **Gauss’s law for magnetism** (stating no magnetic monopoles exist):

$$
\nabla \cdot \mathbf{B} = 0
$$

5. **Ampère’s law (with Maxwell’s correction)**:

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
$$

These equations show that, in time-varying situations, electric fields can be induced by changing magnetic fields (via Faraday’s law), and the interaction between electric and magnetic fields is tightly coupled. Things become more interesting when we study Quantum Electrodynamics and extend the discussion to a quantum scale where we add quantization and many more intesresting things.

## Coulomb's Law (single charge)

If I make $r_0$ as zero, I get a more simplified expression as described below. Coulomb’s law gives the magnitude of the electric field $E$ produced by a point charge $q$ at a distance $r$ as:

$$
E = \frac{k \cdot q}{r^2}
$$

Where:
- $E$ is the electric field (measured in Newtons per Coulomb, $N/C$),
- $q$ is the charge in Coulombs (C),
- $r$ is the distance from the charge in meters (m),
- $k$ is Coulomb's constant, $k = 8.99 \times 10^9 \, \text{Nm}^2/\text{C}^2$.

The electric field is a vector, meaning it has both magnitude and direction. The direction of the field is along the line joining the charge and the point where the field is being measured, directed outward for positive charges and inward for negative charges.

## Superposition Principle

If multiple charges are present, the net electric field at any point is the vector sum of the fields due to each charge. This is the **superposition principle**. Mathematically, for $n$ point charges, the net electric field at a given point is:

$$
E_{\text{net}} = \sum_{i=1}^{n} E_i
$$

Where $E_i$ is the electric field due to charge $i$.

## Conclusion

Electromahgmnetism is the heart of explaining real world natural phenomena and Electric Field is one of the fundamental concepts. I have chosen Coulomb's law for the sake of simplicity, but the complete behaviour of Electric Fields are governed by the Maxwell's equations where Electric Field is just one entity that aids in explaioning the physics. It is intertwined with magnetic fields which create such time invariant systems and makes things more interesting.

## References

1. Jackson, J.D. (1998). Classical Electrodynamics (3rd ed.). Wiley
2. Griffiths, D.J. (2017). Introduction to Electrodynamics (4th ed.). Pearson


