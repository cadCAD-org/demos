# Tutorials and demos
This repo contains tutorials and demos for learning how to use cadCAD. 

## cadCAD System in "Plain English" 
In the cadCAD simulation [methodology](https://community.cadcad.org/t/differential-specification-syntax-key/31), we operate on four layers: **Policies, Mechanisms, States**, and **Metrics**. Information flows do not have an explicit feedback loop unless noted. **Policies** determine the inputs into the system dynamic, and can come from user input, observations from the exogenous environment, or algorithms. **Mechanisms** are functions that take the policy decisions and update the States to reflect the policy level changes. **States** are variables that represent the system quantities at the given point in time, and **Metrics** are computed from state variables to assess the health of the system. Metrics can often be thought of as KPIs, or Key Performance Indicators. 

At a more granular level, to set up a model, there are system conventions and configurations that must be [followed.](https://community.cadcad.org/t/introduction-to-simulation-configurations/34)

The way to think of cadCAD modeling is analogous to machine learning pipelines which normally consist of multiple steps when training and running a deployed model. There is preprocessing, which includes segregating features between continuous and categorical, transforming or imputing data, and then instantiating, training, and running a machine learning model with specified hyperparameters. cadCAD modeling can be thought of in the same way as states, roughly translating into features, are fed into pipelines that have built-in logic to direct traffic between different mechanisms, such as scaling and imputation. Accuracy scores, ROC, etc are analogous to the metrics that can be configured on a cadCAD model, specifying how well a given model is doing in meeting its objectives. The parameter sweeping capability of cadCAD can be thought of as a grid search, or a way to find the optimal hyperparameters for a system by running through alternative scenarios. A/B style testing that cadCAD enables is used in the same way machine learning models are A/B tested, except out of the box, in providing a side-by-side comparison of multiple different models to compare and contract performance. Utilizing the field of Systems Identification, dynamical systems models can be used to "online learn" by providing a feedback loop to generative system mechanisms. 

The flexibility of cadCAD also enables the embedding of machine learning models into behavior policies or mechanisms for complex systems with a machine learning prediction component. 

In this repository are a series of demos and tutorials for how to use cadCAD. Tutorials example how to use cadCAD while demos show examples of cadCAD in use. 

## Tutorials

**Robot and Marbles Tutorial Series**

In this series, we introduce basic concepts of cadCAD and system modeling, in general, using a simple toy model.  
[Part 1](tutorials/robots_and_marbles/robot-marbles-part-1/robot-marbles-part-1.ipynb) - States and State Update Functions  
[Part 2](tutorials/robots_and_marbles/robot-marbles-part-2/robot-marbles-part-2.ipynb) - Actions and State-Dependent Policies  
[Part 3](tutorials/robots_and_marbles/robot-marbles-part-3/robot-marbles-part-3.ipynb) - From Synchronous to Asynchronous Time  
[Part 4](tutorials/robots_and_marbles/robot-marbles-part-4/robot-marbles-part-4.ipynb) - Uncertainty and Stochastic Processes  
[Part 5](tutorials/robots_and_marbles/robot-marbles-part-5/robot-marbles-part-5.ipynb) - Using class objects as state variables  
[Part 6](tutorials/robots_and_marbles/robot-marbles-part-6/robot-marbles-part-6.ipynb) - A/B testing  
[Part 7](tutorials/robots_and_marbles/robot-marbles-part-7/robot-marbles-part-7.ipynb) - Parameter Sweeping  

Check out the [videos](tutorials/robots_and_marbles/videos) folder for detailed walkthroughs of each one of the tutorials.


**Numerical Computation Series**

In this series, we introduce mathematical concepts and how to use cadCAD for numerical computation.

* [Numerical Integration 1: Trapezoid Rule](tutorials/numerical_computation/numerical_integration_1.ipynb)
* Numerical Integration 2: [Simpson's Rule](https://en.wikipedia.org/wiki/Simpson's_rule)
* Numerical Differential 1: [Point Differences](https://en.wikipedia.org/wiki/Numerical_differentiation)
* Numerical Differential 2: [Gradients](https://en.wikipedia.org/wiki/Numerical_differentiation)
* Optimization 1: [Gradient Descent](https://en.wikipedia.org/wiki/Gradient_descent)
* Optimization 2: [Stochastic Gradient Descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)
* Optimization 3: [Newton's Method (to solve least squares)](https://en.wikipedia.org/wiki/Newton%27s_method)
* Dynamical Systems 1: [Euler's Method](https://en.wikipedia.org/wiki/Euler_method)
* Dynamical Systems 2: [RK4](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods)
* Control Systems 1: [Proportional Control](https://en.wikipedia.org/wiki/Proportional_control)
* Control Systems 2: [PID Control](https://en.wikipedia.org/wiki/PID_controller)
* Machine Learning: [Perceptron](https://en.wikipedia.org/wiki/Perceptron)

### Extra credit:
* [Zero-Order and First-Order Optimization Algorithms](http://web.stanford.edu/class/msande311/lecture10.pdf)

## Demos

We will look at demos that use different types of modeling, to give the reader an understanding of the various tools available to modelers.

1. System Dynamics Modelling
2. Agent-Based Modelling
3. Networked Modelling
4. Multiscale Modelling

### 1. System Dynamics (SD)

System Dynamics is a modeling paradigm used to model the nonlinear behavior of complex systems using flows, stocks, and feedback loops. Systems Dynamics modeling is very useful in modeling population flows, financial statements, etc but has a limited ability to represent complex agent and system interactions.

#### Predator-Prey model formulation
An example model for understanding a dynamical system is the commonly used Lotka–Volterra Prey-Predator model, which is a pair of first-order non-linear differential equations that are used to describe the dynamics of two species interacting, one which is a predator the other which is the prey. We can model the population changes over time.

It is based on the following[1,2]

<img src="https://latex.codecogs.com/gif.latex?\frac&space;{dx}{dt}=\alpha&space;x-\beta&space;xy" title="\frac {dx}{dt}=\alpha x-\beta xy" /></a>

<img src="https://latex.codecogs.com/gif.latex?\frac&space;{dy}{dt}=\delta&space;xy-\gamma&space;y" title="\frac {dy}{dt}=\delta xy-\gamma y" /></a>

Where:
* <img src="https://latex.codecogs.com/gif.latex?x" title="x" /></a> is the number of prey 
* <img src="https://latex.codecogs.com/gif.latex?y" title="y" /></a> is the number of some predator 
* <img src="https://latex.codecogs.com/gif.latex?\frac{dx}{dt}" title="\frac{dx}{dt}" /></a> and  <img src="https://latex.codecogs.com/gif.latex?\frac{dy}{dt}" title="\frac{dy}{dt}" /></a> represent the instantaneous growth rates of
* <img src="https://latex.codecogs.com/gif.latex?t" title="t" /></a> represents time
* <img src="https://latex.codecogs.com/gif.latex?\alpha,\beta,\gamma,\delta," title="\alpha,\beta,\gamma,\delta," /></a>are positive real parameters describing the interaction of the two species.

The most prominent feature of it is the existence, depending on the choice of parameters, of a repeatable cycle around a fixed point which creates a dynamical equilibrium between the number of prey and predators on a system.

```
partial_state_update_block = [
    {
        'policies': {
            'reproduce_prey': reproduce_prey,
            'reproduce_predators': reproduce_predators,
            'eliminate_prey': eliminate_prey,
            'eliminate_predators': p_eliminate_predators
        },
        'variables': {
            'prey_population': prey_population,
            'predator_population': predator_population            
        }
    }

]
```

![](https://i.imgur.com/caK3SWK.png)

*Demo:* See the [model here.](demos/System_Dynamics/prey_predator_sd/Predator_Prey_SD_model.ipynb)

#### Compartment Models
To create a mathematical representation of infectious diseases, we will use compartmental models.

The simplest compartmental model is SIR, which consists of three compartments:

* Susceptible: The number of individuals at risk of contracting the disease;
* Infectious: The number of individuals who have been infected and are capable of infecting susceptible individuals;
* Recovered: The number of individuals who have been infected and have recovered from the disease.
As SIR is a very simple model, it considers that the disease's death rate is negligible.

The SIR model can give us a decent analysis of the behavior of infectious diseases, but its simplicity limits it. Many infections have a significant incubation period during which individuals have been infected but neither show symptoms nor are capable of infecting other individuals. Because of that, the SEIR model can represent them in a better way.

As we know, some diseases also have a significant death rate, such as measles, Ebola and SARS. Because of that, SIR and SEIR models can be considerably inaccurate when representing them. Therefore, the SEIRD model can better do it, as it includes individuals who died because of the disease in compartment D.

*Demo:* To see all three models, [click here.](demos/System_Dynamics/Compartment_Models/lab_notebook.ipynb)

##### System Dynamics paradigm (macroscopic view) advantages

* Fast-performing, allowing a very large number of timesteps and simulations
* Easy to prototype and to add/modify mechanisms
* Easy to insert a multitude of complex factors
* The output is usually easy to visualize

### 2. Agent-Based Modeling (ABM)
Agent-based modeling is a modeling paradigm to simulate the interaction of autonomous agents and their results on the underlying system. An example of Agent-Based Modeling is modeling secondary market behavior of individual actors, such as traders, long-term investors, and liquidity providers. 

*Demo:* Using the same Predator-Prey model defined above in the Systems Dynamics Example, we'll adopt a [model](demos/Agent_Based_Modeling/prey_predator_abm/Predator_Prey_ABM_model.ipynb) based on a grid world, on which preys and predators take the following actions at each timestep of their lives:

* Food is grown on every site.
* All agents digest some of the food on their stomachs and get older.
* All agents move (if possible) to an available random neighboring location.
* The agents reproduce themselves if there is an available partner nearby
* The prey agents feed on the available food
* The predator agents hunt the nearby preys
* All old enough agents die

There is an inherent stochastic nature to this model, and every time that you run it, we'll have a completely different result for the same parameters. But we can see that there is sort of a random equilibrium that converges to the dynamical equilibrium which we presented on the dynamical simulation.

```
partial_state_update_block = [
    {
        # environment.py
        'policies': {
            'grow_food': grow_food
        },
        'variables': {
            'sites': update_food
        }
    },
    {
        # agents.py
        'policies': {
            'increase_agent_age': digest_and_olden
        },
        'variables': {
            'agents': agent_food_age

        }
    },
    {
        # agents.py
        'policies': {
            'move_agent': move_agents
        },
        'variables': {
            'agents': agent_location

        }
    },
    {
        # agents.py
        'policies': {
            'reproduce_agents': reproduce_agents

        },
        'variables': {
            'agents': agent_create

        }
    },
    {
        # agents.py
        'policies': {
            'feed_prey': feed_prey
        },
        'variables': {
            'agents': agent_food,
            'sites': site_food
        }
    },
    {
        # agents.py
        'policies': {
            'hunt_prey': hunt_prey
        },
        'variables': {
            'agents': agent_food
        }
    },
    {
        # agents.py
        'policies': {
            'natural_death': natural_death
        },
        'variables': {
            'agents': agent_remove
        }
    }
]


```
![](https://i.imgur.com/v2nLJw8.png)



#### Agent-based modeling paradigm (microscopic view) advantages

* Are conceptually closer to experience, making it easier to explain to someone with no previous background
* Easier to generate complex behavior with simple rules
* Generates more granular and detailed information

##### Conclusion on Predator-Prey demo

We explored here two different paradigms for modeling: the dynamic system one, which captures a macroscopical view of the system, and the agent-based one, which can give us a microscopic view of the system. Depending on the targets and considerations, both can be equivalent or completely distinct, but can also be complementary. cadCAD allows you to mix them at will, so you can have hybrid models where agent behavior and environment are shaped by complex dynamical systems. There is a whole multiverse of mixed simulations that you can do (challenges on the next block for you to try!).

Both paradigms have some characteristics, which in a general manner we can express as being:

##### Dynamical system (macroscopic view) advantages

* Fast-performing, allowing a very large number of timesteps and simulations
* Easier to prototype and to add/modify mechanisms
* Easier to insert a multitude of complex factors
* The output is usually easy to visualize
* Inner workings are more transparent

##### Agent-based modelling (microscopic view) advantages

* Are conceptually closer to experience, making it easier to explain to someone with no previous background
<!---* There is more allowance on stochastic mechanisms and logic--->
* Easier to generate complex behavior with simple rules
* Generates more granular and detailed information
* Inner workings have more depth


#### Proposed challenges

##### Find the equivalent models

Use cadCAD's support for Monte Carlo simulations and parameter sweeping to find a set of parameters that, in expectation, results in nearly equivalent results for the populations of prey and predators over time in both models. You'll need to run multiple Monte Carlo runs of the ABM model and aggregate the results.

##### Sazonability of food growth

A quick way to mix the ABM and SD paradigms is the following: what if the food growth depends on a dynamical system?

You can model that by modifying the food growth policy, such as by inserting a seasonability that depends on the timestep for example. Or you could go even further and try to express it as depending on an irradiance-based dynamical system that models the Sun position according to Earth's movements (rotation, translation, recession, and mutation). How much do you think that those layers of additional complexity will add to the knowledge behind the physical system which we are modeling?

##### Stochasticity of the agent's decisions

In the current model, all randomness is derived from the agents' position on the grid relative to other agents. What if there was also some probability $p_i$ associated with each one of the actions (moving, eating, reproducing)? And what if the decision also depended on the state of the system near the agent, such as the presence of a predator and food availability?

##### Agent death by exponential probability

All agents die when the maximum lifespan arrives. Can you modify the ABM for having an associated spontaneous death probability according to exponential distribution? Something which makes almost all young agents live, but most old ones to die? What if this probability is also a function of an indicator of the agent's health, such as the amount of food in their stomach?

##### Prey evolution & adaptation

This is the master challenge. What if the preys had a varying attribute that gave them some competitive advantage over others? For example, several lives, like in a videogame, or speed, reproduction rate, or different lifespans? What if those attributes were passed on to their offspring with some mutation probability? Could we see an initial random population of prey evolve into a stronger set? Additionally, below are two open-source projects that Block Science was contracted for that provide some insight on how to apply cadCAD for real-world problems while introducing new paradigms for modeling.

### 3. Networked Models
*Demo:*  [Grassroots Economics](https://www.grassrootseconomics.org/) has created a Community Currency to help alleviate the liquidity crisis of rural Kenya. BlockScience created a [graph based dynamical system model in order to provide a scaffold for Grassroot's economy planning](https://github.com/BlockScience/Community_Inclusion_Currencies), a subset of which is discussed below as an illustration of networked model types. 

For networked, graph models evolving, assuming we have a directed graph <img src="https://latex.codecogs.com/gif.latex?\mathcal{G}(\mathcal{V},\mathcal{E})" title="\mathcal{G}(\mathcal{V},\mathcal{E})" /></a> with subpopulations as vertices or nodes <img src="https://latex.codecogs.com/gif.latex?\mathcal{V}&space;=&space;\{1...\mathcal{V}\}" title="\mathcal{V} = \{1...\mathcal{V}\}" /></a>and edges as <img src="https://latex.codecogs.com/gif.latex?\mathcal{E}&space;\subseteq&space;\mathcal{V}&space;\times&space;\mathcal{V}" title="\mathcal{E} \subseteq \mathcal{V} \times \mathcal{V}" /></a>. Demand, utility, and spend are edges connecting the subpopulations, with spend used to denote desired flow between agents, as <img src="https://latex.codecogs.com/gif.latex?i,j&space;\in&space;\mathcal{E}" title="i,j \in \mathcal{E}" /></a>. Technically, the graph is a weighted, directed multigraph with more than on edge, <img src="https://latex.codecogs.com/gif.latex?i&space;\longrightarrow&space;j" title="i \longrightarrow j" /></a> for any pair of vertices <img src="https://latex.codecogs.com/gif.latex?i,j&space;\in&space;\mathcal{V}" title="i,j \in \mathcal{V}" /></a> with <img src="https://latex.codecogs.com/gif.latex?w_{i,j}" title="w_{i,j}" /></a>. In this example, we have a state update block, as shown below, with two partial state update blocks, *choose_agents* and, *spend_allocation*. 

```
partial_state_update_block = [
    'Behaviors': {
        'policies': {
            'action': choose_agents
        },
        'variables': {
        'network': update_agent_activity,
        'outboundAgents': update_outboundAgents,
        'inboundAgents':update_inboundAgents
        }
    },
    'Spend allocation': {
        'policies': {
            'action': spend_allocation
        },
        'variables': {
        'network': update_node_spend
        }
    }
]
```
In this example, during the *spend_allocation*, we calculate, based on the desired interacting agentss' demand, utility, and liquidity constraints, we iterate through the desired demand and allocate based on a stack ranking of utility <img src="https://latex.codecogs.com/gif.latex?v_{i,j}" title="v_{i,j}" /></a> over demand <img src="https://latex.codecogs.com/gif.latex?\frac{v_{i,j}}{d_{i,j}}" title="\frac{v_{i,j}}{d_{i,j}}" /></a> until all demand for each agent is met or the agent <img src="https://latex.codecogs.com/gif.latex?i" title="i" /></a> runs out of funds. There are several assertions we may want to test, such as:
* Agent <img src="https://latex.codecogs.com/gif.latex?i" title="i" /></a> does not go negative in their funds.
* All edges that an agent <img src="https://latex.codecogs.com/gif.latex?i" title="i" /></a> is connected to have been stacked ranked by utility and demand.

![](https://i.imgur.com/4OGhCVL.png)

#### Networked Models Advantages
* Represent complex relationships containing interaction data between multiple agents
* Networked models are an object type, ad a result, they can be used in conjunction with ABM and multiscale modeling approaches for modeling detailed interactions efficiently.


### 4. Multiscale Modeling
Multiscale Modeling is a type of modeling over multiple scales of time or space to describe a system or spatiotemporal scales. An example of a multiscale model is Conviction Voting[Conviction Voting]((https://medium.com/giveth/conviction-voting-a-novel-continuous-decision-making-alternative-to-governance-aa746cfb9475)), aa novel decision-making process where voters express their preference for which proposals they would like to see approved in a continuous rather than discrete way. The longer the community keeps a preference on an individual proposal, the “stronger” the proposal conviction becomes. In the conviction voting [model](https://github.com/BlockScience/Aragon_Conviction_Voting), a graph structure is used to record the introduction and removal of participants, candidates, proposals, and their outcomes. The complexity and different scales represented that cadCAD can model.

#### Aragon Conviction Voting

*Demo:* This cadCAD model and notebook series is a collaboration between [Aragon Project](https://aragon.org), [1Hive](https://1hive.org), [BlockScience](https://block.science), and [the Commons Stack](https://commonsstack.org). A brief table of contents follows to explain the file structure of the various documents produced in this collaboration.
* https://github.com/BlockScience/Aragon_Conviction_Voting

#### Uniswap
*Demo:* Uniswap is an automated market maker for exchanging ERC20 tokens. Anyone can become a liquidity provider, and invest in the liquidity pool of an ERC20 token. This allows other users to trade that token for other tokens at an exchange rate based on their relative availability. When a token trade is executed, a small fee is paid to the liquidity providers that enabled the transaction. https://uniswap.io/

In our [cadCAD model](demos/Multiscale/uniswap/Uniswap_Model.ipynb), we have illustrated how to create a cadCAD model that takes in real data and replicates the mechanics of a real-world smart contract extremely accurately by translating the smart contract code into python code. We enforce best practices for cadCAD modeling and analyze our simulation data against the real data.

#### Adoption Funnel
*Demo*. This [cadCAD model](demos/Multiscale/adoption_funnel/adoption_funnel_model.ipynb). is a [Markov](https://en.wikipedia.org/wiki/Markov_chain) mixing process to exhibit the dynamics of an adoption process as a [finite state machine](https://en.wikipedia.org/wiki/Finite-state_machine). The purpose of this notebook explores the adoption funnel using a Finite State Machine model. Targeted members are treated as sub-population pools as they move through states of adoption, using a developed Adoption_pool class object. 

#### Bonding Curve
*Demo*. In this [notebook](demos/Multiscale/bonding_curve/Bonding_Curve.ipynb), we have shared the experimental code used by Dr. Zargham's [Economic Games as Estimators](https://epub.wu.ac.at/7433/) paper. We have illustrated how to use different driving processes for running numerical simulations.

#### Bonding Curve
*Demo*. In this [notebook](demos/Multiscale/bonding_curve/Bonding_Curve.ipynb), we have shared the experimental code used by Dr. Zargham's [Economic Games as Estimators](https://epub.wu.ac.at/7433/) paper. We have illustrated how to use different driving processes for running numerical simulations.

#### Three Sided Model
*Demo*. In this [notebook](demos/Multiscale/ThreeSided/ThreeSidedMarket.ipynb), we propose the ‘Three-Sided Market’ archetype for platform business where the product being produced enables transactions between a service provider and service consumer. The reference example for this case is a ride-sharing app such as Uber. In this case, drivers would-be providers, and riders would-be consumers. The corporation Uber is the producer, and in our three-sided market, that role will be spread to a decentralized community collectively providing all of the functions required for users (providers and consumers) to have an equivalent user experience.

#### Basic Three Sided Model
*Demo*. This [notebook](demos/Multiscale/ThreeSidedBasic/BasicThreeSidedMarketModel.ipynb) is a scaled-down, basic version of the Three Sided Market Model illustrated previously.

#### Multiscale Modeling Advantages
* Ability on multiple spatio-temporal scales.
* Nonlinear dynamics and feedback effects with emergent properties
* Realistic system complexity in engineering, control systems, and economics models. 

    
#### References
* [1] Lotka, A. J. 1925. Elements of physical biology. Baltimore: Williams & Wilkins Co.
* [2] Volterra, V. 1926. Variazioni e fluttuazioni del numero d'individui in specie animali conviventi. Mem. R. Accad. Naz. dei Lincei. Ser. VI, vol. 2.
