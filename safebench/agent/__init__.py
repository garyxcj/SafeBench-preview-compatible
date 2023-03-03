'''
Author:
Email: 
Date: 2023-01-31 22:23:17
LastEditTime: 2023-03-01 19:57:19
Description: 
    Copyright (c) 2022-2023 Safebench Team

    This work is licensed under the terms of the MIT license.
    For a copy, see <https://opensource.org/licenses/MIT>
'''

from safebench.agent.dummy import DummyAgent
from safebench.agent.rl.sac import SAC

from safebench.agent.object_detection.yolov5 import YoloAgent
from safebench.agent.object_detection.faster_rcnn import FasterRCNNAgent

AGENT_POLICY_LIST = {
    'dummy': DummyAgent,
    'yolo': YoloAgent,
    'sac': SAC,
    'faster_rcnn': FasterRCNNAgent
}
