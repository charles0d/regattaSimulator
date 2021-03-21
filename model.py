import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from pathlib import Path


class LinearQNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear3 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        return self.linear3(x)

    def save(self, file_name='model.pth'):
        model_folder_path = Path('./model')
        if not model_folder_path.exists():
            model_folder_path.mkdir()
        file_path = model_folder_path / file_name
        torch.save(self.state_dict(), file_path)


class QTrainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr= self.lr)
        self.criterion = nn.MSELoss()

    def train_step(self, state, action, reward, next_state, done):
        state = torch.tensor(state, dtype=float)
        next_state = torch.tensor(next_state, dtype=float)
        action = torch.tensor(action, dtype=float)
        reward = torch.tensor(reward, dtype=float)

        if len(state.shape) == 1:
            state = torch.unsqueeze(state)
            next_state = torch.unsqueeze(next_state)
            action = torch.unsqueeze(action)
            reward = torch.unsqueeze(reward)
            done = (done, )

        # 1. predicted Q values with current state
        prediction = self.model(state)

        # 2. Q_new = r + gamma * max(next predicted Q value) -> only do if not done
        target = prediction.clone()
        for idx in range(len(done)):
            Q_new = reward[idx]
            if not done[idx]:
                Q_new += self.gamma * torch.max(self.model(next_state))
            target[idx][torch.argmax(action).item()] = Q_new

        self.optimizer.zero_grad()
        loss = self.criterion(target, prediction)
        loss.backward()

        self.optimizer.step()