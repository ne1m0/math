#
# atoms left/right equilibrium (more)
#

from pylab import *

N = array([16, 32, 64, 96])         # Number of particles
nstep = 4000                        # Number of steps
for j in range(0, size(N)):
    NN = N[j]
    n = zeros(nstep)
    n[0] = NN                       # Initial number on left hand side
    for i in range(1, nstep):
        r = rand(1)
        if(r < n[i-1] / NN):
            n[i] = n[i - 1] - 1     # Move atom from left to right
        else:
            n[i] = n[i - 1] + 1     # Move atom from right to left
    plot(range(0, nstep), n)
show()