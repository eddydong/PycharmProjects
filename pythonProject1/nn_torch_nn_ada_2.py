import torch
import matplotlib.pyplot as plt
import numpy as np

# torch.manual_seed(1)
iterations = 1000

x = torch.tensor([[5.,4.],[4.,7.],[3.,8.],[7.,3.],[1.,8.],[2.,4.],[5.,3.],
                  [1.,4.],[4.,1.],[3.,1.],[1.,3.],[4.,8.],[7.,4.],[5.,6.]])
y = torch.tensor([[0.],[1.],[1.],[0.],[1.],[1.],[0.],
                  [1.],[0.],[0.],[1.],[1.],[0.],[1.]])

model = torch.nn.Sequential(
    torch.nn.Linear(2, 3),
    torch.nn.ELU(),
    torch.nn.Linear(3, 1),
    torch.nn.Sigmoid(),
)

res = []
loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
for t in range(iterations):
    optimizer.zero_grad()
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    if ((t+1) % round(iterations / 10) == 0):
        print(t+1, loss.item())
    res.append([t+1, loss.item()])
    loss.backward()
    optimizer.step()


x = torch.tensor([[9.,7.]])
print(model(x))

# res = np.array(res)
# plt.plot(res[:,0],res[:,1])
# plt.show()

