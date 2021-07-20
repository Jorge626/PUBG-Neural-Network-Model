import torch
import torch.nn as nn
import os


class NN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(756, 500)
        self.fc2 = nn.Linear(500, 315)

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        return self.fc2(x)


def load():
    if os.path.exists('prediction_model.pt'):
        return torch.load('prediction_model.pt')
    return NN()


def save(model):
    torch.save(model, 'prediction_model.pt')
