
import torch.nn as nn
from torch import cat, relu

class GNet(nn.Module):
    def __init__(self):
        super(GNet, self).__init__()
        #1
        self.conv1 = nn.Conv2d(in_channels=2, out_channels=8, kernel_size=3, padding=1)
        #2
        self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, padding=1)
        #3
        self.conv3_1 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)
        #4
        self.conv4 = nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, padding=1)
        #5
        self.conv5 = nn.Conv2d(in_channels=32, out_channels=1, kernel_size=3, padding=1)
        self.final_activation = nn.Sigmoid()




    def forward(self, x,y):
        t=cat([x,y],dim=1)
        t1=self.conv1(t)
        t2 = self.conv2(relu(t1))
        t3_1 = self.conv3_1(relu(t2))
        t4 = self.conv4(relu(t3_1))
        t5 = self.conv5(relu(t4))
        t5=self.final_activation(t5)
        return t5
