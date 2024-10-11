# Reactance in an RLC Circuit
The opposition to a flow of alternating current in a circuit that arises due to
the presence of inductors and capacitors. Though it only occurs in AC circuits,
it is analogous to resistance in DC circuits.

Reactance causes the voltage and current of the circuit to be out of phase with
each other. The type and magnitude of reactance determines whether current
leads or lags behind the voltage.

### Formula for Total Reactance
X = X_L - X_C , where X_L is the inductive reactance and X_C is the capacitive reactance.

A positive X value indicates that the circuit's inductive reactance dominates
the capacitive reactance and so the current will lag behind the voltage.

A negative X value indicates that the circuits capacitive reactance dominates
the inductive reactance and so the current leads the voltage.


## Inductive Reactance
Inductive reactance is the opposition to an alternating current caused by an
inductor.

Inductors resist changes in current by creating a magnetic which stores energy
and opposes the flow of current via induction. In a purely inductive circuit
the current lags behind the voltage by 90 degrees.

### Inductive Reactance: X_L
X_L = (2)(pi)(*f*)(L) , where X_L is measured in ohms, *f* is the frequency
measured in Hz, and L is the inductance of the inductor measured in H.


## Capacitive Reactance
Capacitive Reactance is a resistive phenomenon that occurs when an alternating current is passed through a capacitor, or in certain cases wires that exhibit capacitance.

### Capacitive Reactance: X_C
X_C = 1 / [(2*pi)(f)(C)] where f is the frequency of the alternating current (in Hz) and C is the capacitance (in Farads).

Since capacitors store and release energy in an electric field, this results in
the voltage lagging behind the current in a circuit. In a purely capacitive
circuit, the current leads voltage by 90 degrees.

Single wires do not typically exhibit capacitance, however [...] and so in certain high frequency applications parasitic capacitance can occur between segments of a single wire as well as between a wire and circuit components or
other conductive components.


### How to Determine X_C:
- Start by estimating the parasitic capacitance C using knowledge of the system, its geometry, and its surroundings.
- Determine the operating frequency *f*
- Use [Eqn 2] to compute X_C for the segment/component.

### Parasitic Reactance:
Parasitic (or unintended) reactance occurs as a side-effect that can arise
between different parts of an electrical component, circuit, or system due to
the specific physical characteristics of that object. These characteristics may
include geometric configuration of a circuit, proximity between components, and material properties.

Parasitic reactance can be inductive or capacitive depending on the system and
its configuration. An interesting detail is that while normal (intentional)
capacitive reactance is typically limited to capacitors, parasitic capacitance
can arise nearly anywhere in a circuit if the conditions allow for it.

# Impedance
Based on the total impedance and resistance, the phase relationship can be
inferred. If the impedance is much greater than the resistance, the circuit is dominated by reactance. If the resistance dominates, the circuit behaves more
like a resistor (with less phase shift between voltage and current).

Z = [R^2 + (X_L + X_L_wire - (X_C + X_C_wire))^2 ]^(1/2)

##
