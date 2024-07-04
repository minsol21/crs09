# CRS09 Exercise

## Team Members
- **Minsol Kim**
- **Bhargav Solanki**


# Foraging Robot Simulation
This Python simulation involves a swarm of robots navigating an arena to collect objects and transport them to a designated home zone. As it was simulation to test robot collectivity, we thought implementing a home zone and a whole new sensors and logic to swarmy simulator will not be efficient. A
So we embodied at least but effective simulation for estimating swarm efficiency, including sensors and logic in assignment guide. 

## Features Implemented:

1. **Robot Initialization:**
   - Each robot starts at a random position within the arena and with a random orientation.
   - The home zone is located at the center of the arena and is sized as 25% of arena.

2. **Sensors:**
   - **Light Sensor:** Calculates the distance to the home zone and provides a value inversely proportional to the distance.
   - **Proximity Sensors:** Detects distances to the arena boundaries (left, bottom, right, top).
   - **Bumper Sensor:** Simulated to detect object collisions with a 10% chance of registering a collision when close to an object. For this sensor, placing all the objects in arena and detecting each of them would be too much volume so we decided to leave it as 10% chance, which is reasonable.


3. **Robot Behaviors:**
   - **Random Search:** Robots randomly move within the arena when not transporting objects.
   - **Move to Light:** Once a robot picks up an object, it moves towards the home zone using the light sensor feedback.
   - **Avoid Boundary:** If a robot gets too close to the arena boundary, it turns 90 degrees to avoid collisions.
   - **Object Pickup:** Robots pick up an object if they collide with it (simulated by the bumper sensor).


4. **Foraging Logic:**
   - Robots wander until they detect an object (using the bumper sensor).
   - Upon picking up an object, they navigate towards the home zone.
   - Upon reaching the home zone, robots drop off their objects and reset their position to continue foraging.


5. **Simulation:**
   - The simulation runs for a specified number of time steps (`simulation_time`) with varying swarm sizes (`swarm_size`).
   - Performance is measured by the number of objects collected and is plotted against the swarm size.

6. **Visualization:**
   - The collected data is plotted as a graph showing swarm performance (collected objects) against swarm size.


## Implementation Details:

- **Sensors and Values:** Sensor values such as proximity to boundaries and objects, as well as the likelihood of collision (bumper sensor), are simplified and based on randomized or threshold-based calculations.
- **Movement and Navigation:** Robot movements are simplified to directional changes and translations based on their current orientation and sensor readings.
- **Home Zone Interaction:** Robots drop off objects in the home zone based on a light sensor threshold.
- **Arena Boundary Handling:** Robots avoid boundaries by turning 90 degrees if they get too close.
- **Object Pickup Logic:** Robots pick up objects upon collision, and the number of objects picked up is counted.

## Limitations and Simplifications:

- **Sensor Accuracy:** Actual physical measurements like object weight, size, and precise forces exerted during collisions are not simulated.
- **Environmental Dynamics:** Factors such as object movement, dynamic obstacles, or complex terrain are not simulated.
- **Behavioral Complexity:** The robots' decision-making processes are simplified for the sake of clarity and implementation ease.
