# Neural Network Model to Predict Player Positions in PUBG
This is a research project that was originally conducted with the REU program in Cal Poly Pomona. The goal of this project is to train a neural network model to predict player positions using network packets.

This project has a few different components to it:

 - Parse replay files using the chicken-dinner library
 - Create tensors for player positions and network packets to train neural network model
 - Use tensors to train neural network model
 - PyGame that is currently under development to predict player positions in real-time.

This project uses the Chicken Dinner library from Python and is written entirely in Python.
Information on the chicken-dinner library can be found here:  [ReadTheDocs.io](https://chicken-dinner.readthedocs.io/en/latest/#) & [Github Source Code](https://github.com/crflynn/chicken-dinner/blob/master/docs/index.rst)

## Github File Structure
All important scripts are found in the REU_Project/REU Research/venv/[REU Research](https://github.com/Jorge626/REU_Project/tree/main/REU%20Research/venv/REU%20Research) directory.
- [main.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/main.py) is where the player position and network packets are turned into tensors to be used in training/evaluating the model (may need your own API key to run some code)
- [model.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/model.py) is the neural network model
- [packet_sniffer.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/packet_sniffer.py) is used in the PyGame tool to continuously sniff packets
- [preparedata.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/preparedata.py) is what is used to create tensors to train/evaluate model
- [pubg_csv.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/pubg_csv.py) is what is used to create CSV files for player positions
- [pubg_info.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/pubg_info.py) is only used for getting information from chicken-dinner library
- [pubg_plots.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/pubg_plots.py) plots the player positions on a line graph (used for visualization)
- [pubg_pygame_app.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/pubg_pygame_app.py) is the PyGame application currently in development to predict player positions using the neural network model
- [pubg_tensors.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/pubg_tensors.py) is used to create tensors from player position CSV files and JSON network packet files from WireShark
- [trainmodel.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/trainmodel.py)  is used to train, evaluate, and plot the model
## Parsing Replay Files
Replay files are parsed using the [main.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/main.py) file. 
- User can get information on latest match played by player using API key and [pubg_info.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/pubg_info.py) functions.
- Alternatively, users can use this website to get match id's of any match: [PUBG Lookup Website](https://pubglookup.com/) and inputting into this line of code: ```match_id = pubg.match('<InputMatchIdHere>') ```

Player positions are saved into a CSV file which are then used to create tensors to train/evaluate the model
## Network Packet Collection
Network packets used to train the model were captured using [WireShark](https://www.wireshark.org/).
 - Network packets are recorded during a game and then saved in JSON format.
 - [pubg_tensors.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/pubg_tensors.py) is then used in [main.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/main.py) to convert them into tensors used for training.
 - [packet_sniffer.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/packet_sniffer.py) is used in the PyGame application to sniff packets continuously. 
## Training Model
Once tensors have been created using the [main.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/main.py) file, the tensors can be used to either train or evaluate the model in [trainmodel.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/trainmodel.py)
 - The model can be saved if the evaluations are favorable
 - A plot is also created to visualize the predictions compared to the actual player positions
## PyGame
A simple PyGame application is currently under development in [pubg_pygame_app.py](https://github.com/Jorge626/REU_Project/blob/main/REU%20Research/venv/REU%20Research/pubg_pygame_app.py). Currently, the user can simply choose which map is being played and then that map is displayed as well as the predicted player positions as soon as a network packet is received.
