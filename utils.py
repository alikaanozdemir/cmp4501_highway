import gymnasium as gym

def make_highway_env(env_name: str, render_mode: str = "rgb_array"):
    """Highway ortamını oluşturur."""
    return gym.make(env_name, render_mode=render_mode)