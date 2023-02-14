
import torch
from lstm_models import UtilizationLSTM


def load_model_parameters(dir_path: str = 'models/small-epochs-100') -> dict:
    if torch.has_cuda:
        return torch.load(dir_path)
    else:
        return torch.load(dir_path, map_location=torch.device('cpu'))
    
def get_lstm_model(dir_path: str, for_evaluation: bool = True) -> UtilizationLSTM:
    model_parameters = load_model_parameters(dir_path)

    lstm_model = UtilizationLSTM(
        model_parameters['num_classes'],
        model_parameters['input_size'],
        model_parameters['hidden_size'],
         model_parameters['num_layers']
    )
    lstm_model.load_state_dict(model_parameters['model_state_dict'])
    if for_evaluation:
        lstm_model.eval()
    return lstm_model

