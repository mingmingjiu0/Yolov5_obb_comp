import torch
from thop import profile
from thop import clever_format
from models.common import DetectMultiBackend
import sys, os
from pathlib import Path
from utils.torch_utils import select_device

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

weights = ROOT / 'runs/train/exp93/weights/best.pt'
device = select_device('cpu')
model = DetectMultiBackend(weights, device=device, dnn=False)
input_data = (torch.randn(1, 3, 640,640),) # 输入数据的shape为[batch_size, channel_num, height, width]
# 计算FLOPs和参数数量，并输出结果
flops, params = profile(model, input_data)
flops, params = clever_format([flops, params], "%.3f")
print("模型计算量（FLOPs）为：", flops)
print("模型参数数量为：", params)
