import json
import os

import cyflann.flann_info

pth = os.path.join(os.path.dirname(cyflann.flann_info), 'flann_config.json')
with open(pth, 'w') as f:
    json.dump({'FLANN_DIR': os.environ['FLANN_DIR']}, f)
