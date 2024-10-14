# Electrostatic Potential

Electric potential is a scalar valued field defined at every point by that points distance from all charges in space and those charges' magnitudes. 

It generally takes the form $$V = \sum_i\frac{1}{4\pi\epsilon_0}\frac{q_i}{r_i}$$ where $\epsilon_0$ is the so-called permitivity of free space, $q_i$ is the charge of the $i^{th}$ particle in the system and $r_i$ is the distance from charge $q_i$ to the observation point at which we are finding the potential. 

In general, we don't have discrete charge distributions, so the sum over $q$ becomes an integral over te charge density of the space, $\rho$. $$V(\vec r) = \frac{1}{4\pi\epsilon_0} \int_{\text{All Space}}\frac{\rho(\vec r)}{|\vec r|}d\vec r$$

## Not to be confused with voltage

The symbol for electric potential is V, the same symbol for voltage, which is often described in the language of "potential difference." Though these two quantities are often discussed in similar contexts, they are distinct quantities that must be treated independently.

## For use in finding dynamics

Scalar potential is often used to find the dynamics of a system in electrostatic. This is due to the fact that the potential is defined such that the electric field, $\vec E$ is can be given as $\vec E = -\vec\nabla V$. This is often easier to work with since the electric field itself is a vector field and more cumbersome to be dealt with/found analytically than the potential.