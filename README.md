# Naive-Discrete-Fourier-Transform
A fun little hand-coded implementation of a Fourier Transform. A low-frequency toy signal is defined a priori over the interval [0,1], and a much higher sampling rate is used. The goal was to turn math on paper into a code implementation that could reliably recover the frequencies present in the signal. 

With the famous inner product that defines the geometry of the Hilbert Space with the trigonometric functions as basis vectors, we can project our signal into this space by multiplying it by a complex exponential probe at a frequency n and finding its integral (scaled appropriately ofc).

At any frequency n, we have two sinusoidal basis vectors, cos(nx) and sin(nx). In essence, at frequency n, we take a 2-D slice of the infinite-dimensional space and ask whether our signal has any components in that space and, if so, where they are. The complex exponential just neatly packages the cos and sin such that we can get both coordinates at the same time (which also makes our job of computing magnitudes much easier).

The coordinates are complex numbers, and their magnitudes provide the information on "how much" of a particular frequency is present in the signal. This is just the beginning.
