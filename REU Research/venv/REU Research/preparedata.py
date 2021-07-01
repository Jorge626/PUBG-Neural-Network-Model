import torch


# Prepares the data into random permutations to be used in testing model
def prepare_data(x, y):
    idx = torch.randperm(x.size()[0])
    split = int(x.size()[0] * 0.80)
    train_x = x[idx[:split], :]
    val_x = x[idx[split:], :]
    train_y = y[idx[:split], :]
    val_y = y[idx[split:], :]

    torch.save(train_x, 'train_x.pt')
    torch.save(train_y, 'train_y.pt')
    torch.save(val_x, 'val_x.pt')
    torch.save(val_y, 'val_y.pt')
