#*******************************************************************
#   PoBC, SS17
#
#   Template script for Exercise 2
#
#   The model consists of two populations, an input population of input 
#   neurons and a population of IAF neurons. The populations are
#   are connected with fixed indegree via dynamic synapses. The input neurons
#   produce Poisson spike trains with rate Ri, starting from Tstart.
#    
#
#       Robert Legenstein, March 2017
#
#*******************************************************************
# At the beginning we import the necessary Python packages
#from pypcsimplus import * # the pcsim package with extras
import nest
from numpy import *       # for numerical operations
from pylab import *       # for plotting (matplotlib)
import nest.raster_plot
import nest.voltage_trace
	
def avg_firing_rate(spikes, dt, binsize, Tsim, Nneurons):
    """
      Calculates the average firing rate of a set of spike trains.
      spikes...all spike times of the population in units of [s]
      dt - A value of the firing rate is calculated at each time step dt [s]
      binsize - the size of the bin in multiples of dt. Used to calculate the
      firing rate at a particular moment.
                The rate is <num of spikes in [t-binsize*dt,t]> / (binsize*dt*Nneurons).
      Tsim - The length (in [s]) of the spike trains.
    """
    spi = array(floor(spikes/dt),dtype=int)
    Nbins = int(ceil(Tsim/dt))
    rate = zeros(Nbins+binsize-1)
    for sp in spi:
       rate[sp:sp+binsize]+=1
    rate /= (dt*binsize*Nneurons)
    rate = rate[:Nbins]
    return rate

def construct_input_population(Nin, Rin, Tstart):
    # This is a hack.
    # Because in Nest, one cannot connect Poisson generators with other
    # neurons via dynamic synapses, we need to first connect them to a
    # pool of iaf_psc_exp neurons which are then serving as the input pool
    # The pool will produce approximately Poissonian spike trains with rate Rin 
    # Nin...number of input neurons
    # Rin...firing rate of each input neuron in [Hz]
    # Tstart...time when input neurons start to fire [sec]
    # Returns:
    # noise_neurons...the Poisson generators' GIDs
    # input_neurons...the input neurons' GIDs
    
    noise = nest.Create('poisson_generator',Nin,{'rate':Rin, 'start':Tstart})
    input_neurons = nest.Create("iaf_psc_delta",Nin)
    # Choose threshold very close to resting potential so that each spike in a Poisson generator
    # elicits one spike in the corresponding input neuron
    Vresting = -60.0
    nrn_params =     {"V_m": Vresting,     # Membrane potential in mV
                      "E_L": Vresting,     # Resting membrane potential in mV
                      "C_m": 1.0e4/40,           # Capacity of the membrane in pF
                      "tau_m": 0.5,      # Membrane time constant in ms
                      "V_th": -59.9999,     # Spike threshold in mV
                      "V_reset": Vresting, # Reset potential of the membrane in mV
		      "t_ref": .2   # refractory time in ms
                      }
    nest.SetStatus(input_neurons,nrn_params)
    # Connect Poisson generators to input neurons "one-to-one"
    nest.Connect(noise,input_neurons,{'rule':'one_to_one'},syn_spec={'weight':0.1})
    return noise, input_neurons
    
    
def perform_simulation(Nnrn,Nin,Rin,U,D,F,Tsim):
    """
        Use this one for task b)
	perform a simulation with one input pool of Nin spiking neurons
	connected to a pool of Nnrn IAF neurons with dynamic synapses
	Each IAF neuron has gets 50 inputs from the input (randomly drawn)
	Rin...rate of each input neuron in [Hz]
	U.....utilization parameter of dynamic synapses [-]
	D.....recovery time constant of dynamic synapses in [s]
	F.....facilitation time constant if dynamic synapses in [s]
        Tsim..The duration of the simulation
	Returns: 
	spikes....array containing all spike times (in [s]) in the network 
    """
        
    # use the following parameters for the dynamic synapses
    W = 1e6/Rin           # define the weight of dynamics synapses
    syn_param = {"tau_psc": 3.0,
		 "tau_fac": F*1000,  # facilitation time constant in ms
		 "tau_rec": D*1000,  # recovery time constant in ms
		 "U": U,             # utilization
		 "delay": 0.1,       # transmission delay
		 "weight": W,
		 "u": 0.0,
		 "x": 1.0}
    
    # construct IAF neuron population and recorders
    # use the construct_input_population function to construct the input population
    noise,input_neurons = construct_input_population(...)
    # connect input population to IAF population
    # connect recorders
    
    # Perform the simulation for Tsim seconds.
    
    # extract spike times and convert to [s]

    #return spikes and other stuff

def perform_simulation_d(Nnrn,Nin,U,D,F,Tsim):
    """
        Use this one for task d)
	perform a simulation with one input pool of Nin spiking neurons
	connected to a pool of Nnrn IAF neurons with dynamic synapses
	Each IAF neuron has gets 50 inputs from the input (randomly drawn)
	Rin...rate of each input neuron in [Hz]
	U.....utilization parameter of dynamic synapses [-]
	D.....recovery time constant of dynamic synapses in [s]
	F.....facilitation time constant if dynamic synapses in [s]
        Tsim..The duration of the simulation
	Returns: 
	spikes....array containing all spike times (in [s]) in the network 
    """
        
    # use the following parameters for the dynamic synapses
    W = 1e6/32.0           # USE THESE WEIGHT VALUES FOR TASK d)
    syn_param = {"tau_psc": 3.0,
		 "tau_fac": F*1000,  # facilitation time constant in ms
		 "tau_rec": D*1000,  # recovery time constant in ms
		 "U": U,             # utilization
		 "delay": 0.1,       # transmission delay
		 "weight": W,
		 "u": 0.0,
		 "x": 1.0}
    
    # construct IAF neuron population and recorders
    # use the construct_input_population function to construct the input population
    noise,input_neurons = construct_input_population(...)
    # connect input population to IAF population
    # connect recorders
    
    # Perform the simulation for Tsim seconds.
    
    # extract spike times and convert to [s]

    #return spikes and other stuff


#*******************************************************
# Main script code should be here.
# Several simulations with the model have to be performed
# with different Ri,U,D,F and the population rate should be 
# plotted. Use avg_firing_rate to calculate the population rate.
#*******************************************************


show() # don't forget to call show() in the end 
       # such that figures are displayed on the screen
