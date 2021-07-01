import model
import torch


def train(m, x, y):
	opt = torch.optim.Adam(m.parameters(), lr=0.001)
	loss_fn = torch.nn.MSELoss()
	ls = []
	for i in range(100):
		y_pred = m(x)
		loss = loss_fn(y_pred, y)
		opt.zero_grad()
		loss.backward()
		opt.step()
		print(loss)
		ls.append(loss)


def evaluation(m, x, y):
	loss_fn = torch.nn.MSELoss()
	return loss_fn(m(x), y)


def main():
	train_x = torch.load('train_x.pt')
	train_y = torch.load('train_y.pt')
	m = model.load()
	train(m, train_x, train_y)

	val_x = torch.load('val_x.pt')
	val_y = torch.load('val_y.pt')
	loss = evaluation(m, val_x, val_y)
	print(loss)
	# if result is "good":
	model.save(m)


if __name__ == "__main__":
	main()
