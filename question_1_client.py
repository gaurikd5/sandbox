import socket
import pickle
import pandas as pd
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))

max_message_received = 0

data_repository_base_location ='C:\\Users\\wsxbvus\\Drive\\Learning\\Python\\Sensor_Data\\{}'

def save_sensor_data_to_file(data_dict):
    file_name =str(time.time()).split(".")[0] + ".csv"
    file_location = data_repository_base_location.format(file_name)
    pd_df= pd.DataFrame([data_dict])
    print("After")
    print(f"Saving Data To : {file_location}\n")
    pd_df.to_csv(file_location,index=False)


while True:
    msg = pickle.loads(s.recv(1024))
    print(f"Message Received .. {msg}")
    print(type(msg))
    save_sensor_data_to_file(msg)


    #max_message_received = max_message_received + 1
    # if max_message_received==5:
    #     print("Max message received")
    #     break

