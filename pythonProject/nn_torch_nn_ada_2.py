import torch
import matplotlib.pyplot as plt
import numpy as np

torch.manual_seed(2)
iterations = 1000

x = torch.tensor([[0., 0., 1.],
                  [1., 0., 1.],
                  [0., 0., 0.],
                  [1., 1., 1.],
                  [0., 1., 0.],
                  [1., 1., 0.]])
y = torch.tensor([[0.],
                  [1.],
                  [0.],
                  [1.],
                  [0.],
                  [1.]])

model = torch.nn.Sequential(
    torch.nn.Linear(3, 6),
    torch.nn.Sigmoid(),
    torch.nn.Linear(6, 4),
    torch.nn.Sigmoid(),
    torch.nn.Linear(4, 1)
)

res = []

loss_fn = torch.nn.MSELoss(reduction="mean")
optimizer = torch.optim.SGD(model.parameters(), lr=0.1, momentum=0.7)
for t in range(iterations):
    optimizer.zero_grad()
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    if ((t+1) % round(iterations / 10) == 0):
        print(t+1, loss.item())
    res.append([t+1, loss.item()])
    loss.backward()
    optimizer.step()

res = np.array(res)
plt.plot(res[:,0],res[:,1])
# plt.show()

print(model(torch.tensor([0., 1., 1.])))
