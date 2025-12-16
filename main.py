import gymnasium as gym
import highway_env
from stable_baselines3 import PPO
import config
from utils import make_highway_env

def train():
   
    env = make_highway_env(config.ENV_NAME)

    model = PPO("MlpPolicy", 
                env, 
                verbose=1, 
                learning_rate=config.LEARNING_RATE, 
                tensorboard_log=config.LOG_DIR)

    print(f"Starting training for {config.TOTAL_TIMESTEPS} timesteps...")
    model.learn(total_timesteps=config.TOTAL_TIMESTEPS)

    model.save(f"{config.MODEL_DIR}/highway_ppo_model")
    print("Model successfully saved in: 'models/'")

if __name__ == "__main__":
    train()