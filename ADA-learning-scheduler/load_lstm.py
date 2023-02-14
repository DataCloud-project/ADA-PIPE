
import torch
from lstm_models import UtilizationLSTM

model_parameters = torch.load('models/small-epochs-100', map_location=torch.device('cpu'))


model_parameters.keys()


num_classes = model_parameters['num_classes']
input_size = model_parameters['input_size']
hidden_size = model_parameters['hidden_size']
num_layers = model_parameters['num_layers']


lstm_model = UtilizationLSTM(num_classes, input_size, hidden_size, num_layers)


lstm_model.load_state_dict(model_parameters['model_state_dict'])


lstm_model.eval()