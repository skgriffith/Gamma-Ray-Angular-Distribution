# Gamma-Ray-Angular-Distribution

gammappdata.db provides the FLUKA data for double-differential gamma-ray yields from proton-proton collisions at various energies ($E_{CR}$) between the pion production threshold, 1.2 GeV, and 100 GeV for an energetic proton on a static proton target. The yields are given as $d^2 N / dx d \Omega$, where $N$ is the number of gamma-rays, $\Omega$ is the solid angle, and $x = E_\gamma / E_{CR}$. For a given proton energy, a table is provided which has the $x$-value of the bin on the left side and the angular bin (in increments of $5^\circ$) along the top. The bin at the intersection then gives the yield.

The accompanying python module, gammappyield.py, provides a simple use case for the data. This function takes the primary energy and observation angle as arguments and returns a list of pairs, where the first entry is the $x$-value of the bin and the second entry is the yield. There is no interpolation between bins, the primary energy is rounded to the nearest available value. This is intended as an example from which to build on as appropriate for a given simulation. 

Any use of these results should also cite the FLUKA collaboration, [https://fluka.cern/](https://fluka.cern/), specifically the following publications:

["New Capabilities of the FLUKA Multi-Purpose Code"](https://inspirehep.net/literature/2034530) <br />
C. Ahdida et al, <br />
Frontiers in Physics 9, 788253 (2022)

["Overview of the FLUKA code"](https://inspirehep.net/literature/1421238) <br />
G. Battistoni et al, <br />
Annals of Nuclear Energy 82, 10-18 (2015).

["The FLUKA Code: Developments and Challenges for High Energy and Medical Applications"](https://inspirehep.net/literature/1619967) <br />
T.T. Böhlen, F. Cerutti, M.P.W. Chin, A. Fassò, A. Ferrari, P.G. Ortega, A. Mairani, P.R. Sala, G. Smirnov and V. Vlachoudis, <br />
Nuclear Data Sheets 120, 211-214 (2014)

["FLUKA: a multi-particle transport code"](https://inspirehep.net/literature/701721) <br />
A. Ferrari, P.R. Sala, A. Fasso`, and J. Ranft, <br />
CERN-2005-10 (2005), INFN/TC_05/11, SLAC-R-773 
