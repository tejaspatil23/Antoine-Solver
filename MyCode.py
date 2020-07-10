import numpy as np

n = int(input("How many components are in your system? "))

entering_array = []
rows_in = int(input("How many streams are entering your system? "))
for w in range(rows_in):
    stream_in = []
    for i in range(n):
        flow_rate = input('In entering stream ' + str(w+1) + ', enter the flowrate of component ' + str((i+1)) + ' :')
        stream_in.append(flow_rate)
    stream_in = np.asarray(stream_in)
    entering_array.append(stream_in)

entering_array = np.asarray(entering_array)
entering_array = np.transpose(entering_array)
print(entering_array)
print(entering_array.ndim)

exiting_array = []
rows_out = int(input("How many streams are exiting your system? "))
for w in range(rows_out):
    stream_out = []
    for i in range(n):
        flow_rate = input('In exiting stream ' + str(w+1) + ', enter the flowrate of component ' + str((i+1)) + ' :')
        stream_out.append(flow_rate)
    stream_out = np.asarray(stream_out)
    exiting_array.append(stream_out)

exiting_array = np.asarray(exiting_array)
exiting_array = np.transpose(exiting_array)
print(exiting_array)
print(exiting_array.ndim)

