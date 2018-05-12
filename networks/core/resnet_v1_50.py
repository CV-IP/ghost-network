import os

import tensorflow.contrib.slim.nets as nets

from config import config as FLAGS
from networks.lib.lib_resnet_v1_50 import resnet_v1_50

_CHECKPOINT_NAME = 'resnet_v1_50.ckpt'
checkpoint_path = os.path.join(
    FLAGS.checkpoint_path,
    _CHECKPOINT_NAME
)

arg_scope = nets.resnet_v1.resnet_arg_scope(weight_decay=0.0)
func = resnet_v1_50
