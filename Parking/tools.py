import cv2
import gym
from pathlib import Path
import numpy as np
from IPython.display import HTML
from base64 import b64encode

class RecordVideos(gym.Wrapper):
    def __init__(self, env, save_dir="videos", fps=20):
        super().__init__(env)
        self.frames = []
        self.save_dir = Path(save_dir)
        self.fps = fps
        self.save_dir.mkdir(parents=True, exist_ok=True)
        self.video_path = None

    def reset(self, **kwargs):
        self.frames = []
        return super().reset(**kwargs)

    def step(self, action):
        observation, reward, done, truncated, info = super().step(action)
        self.frames.append(self.env.render())
        return observation, reward, done, truncated, info

    def close(self):
        if self.frames:
            self.save_video()
        super().close()

    def save_video(self):
        video_id = len(list(self.save_dir.glob("*.avi"))) + 1
        self.video_path = self.save_dir / f"episode_{video_id}.avi"
        frame_size = (self.frames[0].shape[1], self.frames[0].shape[0])
        out = cv2.VideoWriter(str(self.video_path), cv2.VideoWriter_fourcc(*'DIVX'), self.fps, frame_size)
        for frame in self.frames:
            out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        out.release()

def record_videos(env):
    return RecordVideos(env)
