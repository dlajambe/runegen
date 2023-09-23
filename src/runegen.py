import torch
from torch import nn
import torch.nn.functional as F

class RuneGen(nn.Module):
    def __init__(self):
        super().__init__()

if torch.cuda.is_available():
    print('Cuda available')
else:
    print ('Cuda unavailable')


