#
# atoms left/right equilibrium
#

from pylab import *

N = 210         # Number of particles
nstep = 4000    # Number of steps
n = zeros(nstep)
n[0] = 210      # Initial number on left hand side
for i in range(1, nstep):
    r = rand(1)
    if(r < n[i-1]/N):
        n[i] = n[i - 1] - 1     # Move atom from left to right side
    else:
        n[i] = n[i - 1] + 1     # Move atom from right to left side
plot(range(0, nstep), n/N)
xlabel('t'), ylabel('n/N')
show()