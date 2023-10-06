from typing import Tuple
import torch
import torch.nn as nn

from utils import get_device

device = get_device()

# https://github.com/pytorch/examples/blob/main/time_sequence_prediction/train.py

# https://blog.floydhub.com/long-short-term-memory-from-zero-to-hero-with-pytorch/
# https://medium.com/unit8-machine-learning-publication/transfer-learning-for-time-series-forecasting-87f39e375278
# https://towardsdatascience.com/pytorch-lstms-for-time-series-data-cd16190929d7
# https://medium.com/intel-student-ambassadors/implementing-attention-models-in-pytorch-f947034b3e66
# https://www.crosstab.io/articles/time-series-pytorch-lstm
# https://www.kaggle.com/code/omershect/learning-pytorch-lstm-deep-learning-with-m5-data/notebook

class LSTM(nn.Module):

    def __init__(self, num_classes: int, input_size: int, hidden_size: int, num_layers: int) -> None:
        super(LSTM, self).__init__()
        self.num_classes: int = num_classes
        self.input_size: int = input_size
        self.hidden_size: int = hidden_size
        self.num_layers: int = num_layers

        # long-short term memory layer
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=self.num_layers,
            batch_first=True,
        ).to(device)

        self.dropout = nn.Dropout(0.4)

        # first fully connected layer
        self.fc_1 = nn.Linear(hidden_size, 512).to(device)
        # second fully connected layer
        self.fc_2 = nn.Linear(512, 256).to(device)
        # thrid fully connected layer
        self.fc_3 = nn.Linear(256, num_classes).to(device)
        # activation function
        self.relu = nn.ReLU().to(device)

    def forward(self, input: torch.Tensor):
        # Propagate input through LSTM
        _, (hn, _) = self.lstm(input, self.get_hidden_internal_state(input))

        # Reshaping the data for the Dense layer
        out = hn.view(-1, self.hidden_size)
        # out = self.relu(hn[0])
        out = self.fc_1(out)
        # out = self.dropout(out)
        out = self.relu(out)

        out = self.fc_2(out)
        # out = self.dropout(out)
        out = self.relu(out)
        out = self.fc_3(out)

        return out

    def get_hidden_internal_state(self, input: torch.Tensor):
        hidden_state = torch.zeros(self.num_layers, input.size(0), self.hidden_size).requires_grad_().to(device)
        internal_state = torch.zeros(self.num_layers, input.size(0), self.hidden_size).requires_grad_().to(device)

        return (hidden_state, internal_state)


class UtilizationLSTM(nn.Module):

    def __init__(self, num_classes: int, input_size: int, hidden_size: int, num_layers: int = 1, generalization: str = 'batch', lstm_mode: str = 'full') -> None:
        super(UtilizationLSTM, self).__init__()
        self.num_classes: int = num_classes
        self.input_size: int = input_size
        self.hidden_size: int = hidden_size
        self.num_layers = num_layers
        self.lstm_mode = lstm_mode
        self.device = device
        
        # if dataset is split, remove two columns not used in the lstm model
        split_decrement: int = 2 if lstm_mode == 'split' else 0

        # long-short term memory layer to predict cpu usage
        self.cpu_lstm = nn.LSTM(
            input_size=input_size - split_decrement,
            hidden_size=hidden_size,
            num_layers=self.num_layers, 
            batch_first=True,
        ).to(device)

        # long-short term memory layer to predict memory usage
        self.mem_lstm = nn.LSTM(
            input_size=input_size - split_decrement,
            hidden_size=hidden_size,
            num_layers=self.num_layers,
            batch_first=True,
        ).to(device)

        if generalization == 'dropout':
            self.cpu_lstm_seq = self.init_sequential_layer_dropout(hidden_size)
            self.mem_lstm_seq = self.init_sequential_layer_dropout(hidden_size)
            
        elif generalization == 'batch':
            self.cpu_lstm_seq = self.init_sequential_layer_batchnorm(hidden_size)
            self.mem_lstm_seq = self.init_sequential_layer_batchnorm(hidden_size)

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        if self.lstm_mode == 'full':
            cpu_input, mem_input = input, input
        elif self.lstm_mode == 'split':
            cpu_input, mem_input = self.split_input(input)

        # Propagate input through LSTM
        _, (cpu_ht, _) = self.cpu_lstm(cpu_input,
                                       self.get_hidden_internal_state(input))
        _, (mem_ht, _) = self.mem_lstm(mem_input,
                                       self.get_hidden_internal_state(input))
               
        # Reshaping the data for the Dense layer
        cpu_ht = cpu_ht.view(-1, self.hidden_size)
        mem_ht = mem_ht.view(-1, self.hidden_size)

        cpu_out: torch.Tensor = self.cpu_lstm_seq(cpu_ht)
        mem_out: torch.Tensor = self.mem_lstm_seq(mem_ht)

        # Concat the two tensors column-wise
        output = torch.cat([cpu_out, mem_out], dim=1)
        
        # Only use the last stacked lstm layer as output
        output = output[(self.num_layers - 1) * input.size(0):]

        # don't allow negative values
        output = torch.abs(output)
        
        return output
        # return torch.abs(output)
        
    def get_hidden_internal_state(self, input: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        hidden_state = torch.zeros(self.num_layers, input.size(0), self.hidden_size).requires_grad_().to(device)
        internal_state = torch.zeros(self.num_layers, input.size(0), self.hidden_size).requires_grad_().to(device)

        return (hidden_state, internal_state)

    def split_input(self, input: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Splits the Input Tensor into two Tensors.
            - CPU Tensor:
                - Indices: [0, 1] + (if more than 4 columns) [3, ...]
                - Shape: Same as input tensor but without the memory columns [2, 3]
            - MEM Tensor: 
                - Indices: [2, 3] + (if more than 4 columns) [3, ...]
                - Shape: Same as input tensor but without the cpu columns [0, 1]

        Args:
            input (torch.Tensor): The input tensor consisting of at least 4 columns `['plan_cpu', 'cap_cpu', 'plan_mem', 'cap_mem']`
                                  The tensor can also include additional information about each task, that can be appended starting at column 3.

        Returns:
            Tuple[torch.Tensor, torch.Tensor]: Returns the two tensors (CPU_input, MEM_input)
        """
        if input.size(dim=2) < 4:
            return torch.empty(1), torch.empty(1)
        
        cpu_columns, mem_columns = [0, 1], [2, 3]
        
        if input.size(dim=2) > 4:
            cpu_columns = cpu_columns + [x for x in range(4, input.size(dim=2))]
            mem_columns = mem_columns + [x for x in range(4, input.size(dim=2))]

        cpu_input, mem_input = input[:, :, cpu_columns], input[:, :, mem_columns]
        
        return (cpu_input, mem_input)

    def init_sequential_layer_batchnorm(self, hidden_size: int) -> nn.Sequential:
        return nn.Sequential(
            nn.ReLU(),
            nn.BatchNorm1d(hidden_size),
            nn.Linear(hidden_size, 512),
            
            nn.ReLU(),
            nn.BatchNorm1d(512),
            nn.Linear(512, 128),
            
            nn.ReLU(),
            nn.BatchNorm1d(128),
            nn.Linear(128, 1),
        ).to(device)


    def init_sequential_layer_dropout(self, hidden_size: int) -> nn.Sequential:
        return nn.Sequential(
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(hidden_size, 512),
            
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(512, 128),
            
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(128, 1),
        ).to(device)

if __name__ == '__main__':

    test_tensor = torch.ones([300, 1, 5], dtype=torch.float32).to(device)
    # test_tensor = torch.ones([1000, 1, 8], dtype=torch.float32).to(device)
    
    for i in range(test_tensor.size(2)):
        test_tensor[:, :, i] *= test_tensor[:, :, i] * (i)

    # number of features
    input_size: int = test_tensor.shape[2]
    # number of features in hidden state
    hidden_size: int = test_tensor.shape[2] * 2**8
    # number of stacked lstm layers
    num_layers: int = 3
    # number of output classes
    num_classes: int = 1

    # lstm = LSTM(num_classes, input_size, hidden_size, num_layers, test_tensor.shape[1], bidirectional=True)

    # lstm.forward(test_tensor)

    lstm = UtilizationLSTM(num_classes, input_size, hidden_size, num_layers=1, generalization='dropout')
    lstm.forward(test_tensor)
    
    output = lstm.split_input(test_tensor)
    print(output[0].shape, output[1].shape)
