from gym.envs.registration import register

register(
    id='Chopper-v0',
    entry_point='gym_Chopper.envs:ChopperEnv',
)
