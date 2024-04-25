import gymnasium as gym


env = gym.make("roundabout-v0", render_mode = "rgb_array")

# config for the environment
config = {
    "observation": {
        "type": "TimeToCollision"
    },
    "action": {
        "type": "DiscreteMetaAction"
    },
    "incoming_vehicle_destination": None,
    "duration": 11, # [s] If the environment runs for 11 seconds and still hasn't done(vehicle is crashed), it will be truncated. "Second" is expressed as the variable "time", equal to "the number of calls to the step method" / policy_frequency.
    "simulation_frequency": 15,  # [Hz]
    "policy_frequency": 1,  # [Hz]
    "other_vehicles_type": "highway_env.vehicle.behavior.IDMVehicle",
    "screen_width": 600,  # [px] width of the pygame window
    "screen_height": 600,  # [px] height of the pygame window
    "centering_position": [0.5, 0.6],  # The smaller the value, the more southeast the displayed area is. K key and M key can change centering_position[0].
    "scaling": 5.5,
    "show_trajectories": False,
    "render_agent": True,
    "offscreen_rendering": False
}