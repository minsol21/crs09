import random
import matplotlib.pyplot as plt
import numpy as np

class Robot:
    def __init__(self, arena_size):
        self.arena_size = arena_size
        self.position = np.array([random.uniform(0, arena_size), random.uniform(0, arena_size)])
        self.orientation = random.uniform(0, 2 * np.pi)  # in radians
        self.home_zone_center = np.array([arena_size / 2, arena_size / 2])
        self.is_transporting_object = False

    def read_sensors(self):
        # Calculate distance to home zone light (simplified)
        distance_to_home = np.linalg.norm(self.position - self.home_zone_center)
        light_sensor_value = 1 / (1 + distance_to_home)

        # Detecting the arena boundary (simplified)
        proximity_sensors = [
            self.position[0],  # distance to left boundary
            self.position[1],  # distance to bottom boundary
            self.arena_size - self.position[0],  # distance to right boundary
            self.arena_size - self.position[1]   # distance to top boundary
        ]
        proximity_sensor_value = min(proximity_sensors) / self.arena_size

        # Bumper sensor (simplified for object detection)
        bumper_sensor_value = random.random() if random.random() < 0.1 else 0  # 10% chance of hitting an object

        return {
            'light_sensor_value': light_sensor_value,
            'proximity_sensor_value': proximity_sensor_value,
            'bumper_sensor_value': bumper_sensor_value
        }

    def move_to_light(self, light_sensor_value):
        direction_to_home = self.home_zone_center - self.position
        angle_to_home = np.arctan2(direction_to_home[1], direction_to_home[0])
        
        if abs(angle_to_home - self.orientation) > 0.1:  # Turn towards the home zone
            self.orientation += 0.1 if angle_to_home > self.orientation else -0.1
        else:
            self.position += 0.5 * np.array([np.cos(self.orientation), np.sin(self.orientation)])

    def random_search(self):
        self.orientation += random.uniform(-0.1, 0.1)
        self.position += 0.5 * np.array([np.cos(self.orientation), np.sin(self.orientation)])
        self.position = np.clip(self.position, 0, self.arena_size)  # Ensure the robot stays within the arena

    def avoid_boundary(self, proximity_sensor_value):
        if proximity_sensor_value < 0.1:  # Too close to boundary
            self.orientation += np.pi / 2  # Turn 90 degrees

    def forage(self):
        sensors = self.read_sensors()
        light_sensor_value = sensors['light_sensor_value']
        proximity_sensor_value = sensors['proximity_sensor_value']
        bumper_sensor_value = sensors['bumper_sensor_value']

        error = 'unknown'
        collision = bumper_sensor_value > 0
        arena_boundary = proximity_sensor_value < 0.1
        transporting_object = self.is_transporting_object
        home_zone = light_sensor_value > 0.5  # Arbitrary threshold for being in the home zone

        if home_zone and self.is_transporting_object:
            self.is_transporting_object = False
        elif self.is_transporting_object:
            self.move_to_light(light_sensor_value)
        elif bumper_sensor_value > 0.5:
            self.is_transporting_object = True
        elif arena_boundary:
            self.avoid_boundary(proximity_sensor_value)
        else:
            self.random_search()

        return {
            'position': self.position,
            'orientation': self.orientation,
            'error': error,
            'collision': collision,
            'arena_boundary': arena_boundary,
            'transporting_object': transporting_object,
            'home_zone': home_zone
        }


def simulate_swarm(swarm_size, simulation_time, arena_size):
    swarm = [Robot(arena_size) for _ in range(swarm_size)]
    collected_objects = 0

    for t in range(simulation_time):
        for robot in swarm:
            status = robot.forage()
            if status['home_zone'] and not status['transporting_object']:
                collected_objects += 1

    return collected_objects


def main():
    swarm_sizes = range(1, 11)
    performance = []

    simulation_time = 1000  # number of simulation steps
    arena_size = 100  # size of the arena

    for swarm_size in swarm_sizes:
        collected_objects = simulate_swarm(swarm_size, simulation_time, arena_size)
        performance.append(collected_objects)

    # Plotting the results
    plt.plot(swarm_sizes, performance, marker='o')
    plt.title('Swarm Performance')
    plt.xlabel('Swarm Size')
    plt.ylabel('Collected Objects')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
