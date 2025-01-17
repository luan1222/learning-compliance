from .sensor import Sensor
from b1_gym.utils.math_utils import quat_apply_yaw
from isaacgym.torch_utils import *

class EeGripperForceDirSensor(Sensor): # along z-axis
    def __init__(self, env, attached_robot_asset=None, delay=0):
        super().__init__(env)
        self.env = env

    def get_observation(self, env_ids = None):
        import torch
        
        # world to base frame (only yaw)
        # force_yaw_base = quat_apply_yaw(quat_conjugate(self.env.base_quat[:, :4]), 
        #                                 self.env.forces[:, self.env.gripper_stator_index, :3]).view(self.env.num_envs, 3)
        # return torch.atan2(force_yaw_base[:, 1], force_yaw_base[:, 0]).view(self.env.num_envs, 1)
    
        return torch.atan2(self.env.forces[:, self.env.gripper_stator_index, 1], self.env.forces[:, self.env.gripper_stator_index, 0]).view(self.env.num_envs, 1)
    
    def get_noise_vec(self):
        import torch
        return torch.zeros(1, device=self.env.device)
    
    def get_dim(self):
        return 1