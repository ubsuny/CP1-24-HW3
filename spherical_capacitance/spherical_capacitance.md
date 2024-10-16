# Capacitance from Spherical Capacitor
A spherical capacitor is created when two conducting spheres are cocentric with eachother. 
Their behavior is often learned in tandem with paralell plate capacitors, as the concepts certainly go hand in hand.

To calculate the capacitance of a spherical capacitor with dielectric medium between the spheres, you must
take into account the change in relative dielectric suseptability:

$\epsilon_r=\frac{\epsilon}{\epsilon_0}$

Where $\epsilon_r$ is the relative permittivity, $\epsilon$ is the dielectric's permittivity, 
and $\epsilon_0$ is the permittivity of free space.

## Formula for Capacitance Without Dielectric
$C = 4 \pi \epsilon_0 ~ \frac{a b}{b - a}$

Where C is the capacitance, a is the radius of the inner sphere, and b is the radius of the outer sphere.

With dielectrics present, the total capacitance depends on the properties of the dielectric materials between the spheres.

## Capacitance from Single Dielectric
When the gap between the spheres is filled with a dielectric medium with permittivity $\epsilon$, 
the electric field between the spheres change as:

$E=\frac{\epsilon_0}{\epsilon}E_0=\frac{1}{\epsilon_r}E_0$

Where $E_0$ is what the electric field would be in vacuum. This change in electric field inherently changes the capacitance, 
as the capacitance is inherently tied to the elctric field. This changes the capacitance as follows:

$C=\epsilon_r C = 4 \pi \epsilon_0 \epsilon_r ~ \frac{a b}{b - a}$

This is effective at getting the capacitance with one material between the spheres, however what if there was more than one?

# Total Capacitance from Multiple Dielectric
With multiple dielectric medium with varying permittivities, the total capacitance can be calculated by
combining the capacitance contributions of each layer as though they are in series. This is done as follows:

$\frac{1}{C_{net}}=\sum\limits_{i=1}^n ~ \frac{1}{C_i}$

For n different medium. Furthermore, taking the inverse gives the actual value of net capacitance, not just the inverse.

$C_{net}=\left( \sum\limits_{i=1}^n ~ \frac{1}{C_i} \right)^{-1}$

### Example Derivation
As an example, for 2 dielectric medium with permittivities $\epsilon_{r1}$ and $\epsilon_{r2}$ in a spherical capacitor: 
Assuming one medium ending a distance d away from the inner sphere's surface, and the other starting there,
the calculation is as follows...

$C_1 = 4 \pi \epsilon_0 \epsilon_{r1} ~ \frac{a d}{d - a}$

$C_2 = 4 \pi \epsilon_0 \epsilon_{r2} ~ \frac{d b}{b - d}$

$\frac{1}{C_{net}}=\frac{1}{C_1}+\frac{1}{C_2}$

$\frac{1}{C_{net}} = \frac{1}{4 \pi \epsilon_0 \epsilon_{r1}}~\frac{d - a}{a d}+\frac{1}{4 \pi \epsilon_0 \epsilon_{r2}} ~ \frac{b - d}{d b}$

$\frac{1}{C_{net}} = \frac{1}{4 \pi \epsilon_0} \left( \frac{d - a}{a d \epsilon_{r1}} +\frac{b - d}{d b \epsilon_{r2}} \right)$

$\boxed{\therefore C_{net}=4 \pi \epsilon_0 \left( \frac{d - a}{a d \epsilon_{r1}} +\frac{b - d}{d b \epsilon_{r2}} \right)^{-1}}$
