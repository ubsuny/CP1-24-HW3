# EM Waves in Conductors

Maxwell's equations can be used to model the behavior of EM waves in conductors.

1. $$\nabla \cdot \mathbf{E} = \frac{1}{\epsilon} \rho_f$$

2. $$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

3. $$\nabla \cdot \mathbf{B} = 0$$

4. $$\nabla \times \mathbf{B} = \mu \sigma \mathbf{E} + \mu \epsilon \frac{\partial \mathbf{E}}{\partial t}$$

Using the continuity equation for free charge, Ohm's Law, and Gauss's Law, it can be shown that any initial free charge $\rho_f(0)$ dissipates in a **characteristic time** $\tau \equiv \epsilon / \sigma$. This is what we mean when we say that any excess charge deposited on a conductor resides on its surface. Of course, it takes a finite time for the excess charges to migrate to the surface. The shorter the characteristic time, the better the conductor.

Once any accumulated charges have disappeared, Maxwell's equations are simplified to:

1. $$\nabla \cdot \mathbf{E} = 0$$

2. $$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

3. $$\nabla \cdot \mathbf{B} = 0$$

4. $$\nabla \times \mathbf{B} = \mu \sigma \mathbf{E} + \mu \epsilon \frac{\partial \mathbf{E}}{\partial t}$$

Applying the curl to (2) and (4), we obtain the wave equations for $\vec{E}$ and $\vec{B}$:

$$\nabla^2 \mathbf{E}=\mu \epsilon \frac{\partial^2 \mathbf{E}}{\partial t^2}+\mu \sigma \frac{\partial \mathbf{E}}{\partial t},$$ $$\quad \nabla^2 \mathbf{B}=\mu \epsilon \frac{\partial^2 \mathbf{B}}{\partial t^2}+\mu \sigma \frac{\partial \mathbf{B}}{\partial t}$$

which admit plane wave solutions of the form

$$\tilde{\mathbf{E}}(z, t)=\tilde{\mathbf{E}}_0 e^{i(\tilde{k} z-\omega t)},$$

$$\tilde{\mathbf{B}}(z, t)=\tilde{\mathbf{B}}_0 e^{i(\tilde{k} z-\omega t)},$$

with a complex wavenumber 

$$\tilde{k}^2=\mu \epsilon \omega^2+i \mu \sigma \omega$$

Taking the square root, we can write:

$$\tilde{k}=k+i \kappa ,$$

where the **real wavenumber** $k$ is:

$$k \equiv \omega \sqrt{\frac{\epsilon \mu}{2}}\left[\sqrt{1+\left(\frac{\sigma}{\epsilon \omega}\right)^2}+1\right]^{1 / 2}$$

and the **attenuation constant** $\kappa$ is:

$$k \equiv \omega \sqrt{\frac{\epsilon \mu}{2}}\left[\sqrt{1+\left(\frac{\sigma}{\epsilon \omega}\right)^2}-1\right]^{1 / 2}$$

The imaginary part of $\tilde{k}$ leads to the attenuation of the wave inside the conductor:

$$\tilde{\mathbf{E}}(z, t)=\tilde{\mathbf{E}}_0 e^{-\kappa z} e^{i(k z-\omega t)},$$ 

$$\tilde{\mathbf{B}}(z, t)=\tilde{\mathbf{B}}_0 e^{-\kappa z} e^{i(k z-\omega t)},$$ 

The distance the wave travels before its amplitude gets reduced by a factor of $1/e$ is called the **skin depth** and is defined as:

$$d \equiv \frac{1}{\kappa}$$

Moreover, the $\vec{E}$ and $\vec{B}$ fields no longer remain in phase as the wave passes through a conductor, with 

$$\delta_B-\delta_E=\phi $$

where 

$$\phi \equiv \tan ^{-1}(\kappa / k)$$

is defined as the **phase shift**.



Reference: [1] Griffiths D.J, Introduction to Electrodynamics (4th Ed)

