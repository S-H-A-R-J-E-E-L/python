from array import *
arival_time = array('i', []);
burst_time =array('i', []);
r_time = array('i', []);
r_process = 0;
count = 0;
time = 0;
flag = 0;
wait_time =0;
turnaround_time = 0;

process = input("Enter Total Process: ");
r_process = process;
quantam_time = input("Enter Quantam Time: ");

for i in range(0, process):
    x = raw_input("Enter Arival Time: ");
    y = raw_input("Enter Burst Time: ");
    arival_time.append(int(x));
    burst_time.append(int(y));
    r_time.append(int(y));
    
print("\n\nProcess | Turnaround Time | Waiting Time\n\n\n");

while(r_process != 0):
    
    if(r_time[count] <= quantam_time and r_time[count] > 0):
        time += r_time[count];
        r_time[count] = 0;
        flag = 1;
        
    elif(r_time[count] > 0):
        r_time[count] = r_time[count] - quantam_time;
        time += quantam_time;
        
    if(r_time[count] == 0 and flag == 1):
        r_process -= 1;
        print(count+1, time-arival_time[count], time - arival_time[count]- burst_time[count]);
        wait_time += time - arival_time[count] - burst_time[count];
        turnaround_time += time - arival_time[count];
        flag = 0;
        
    if(count == (process-1)):
        count = 0;
    elif(arival_time[count+1] <= time):
        count += 1;
    else:
        count = 0;   
        
print("Average waiting Time: ", (wait_time*1.0)/process);
print("Average Turnaround Time: ", (turnaround_time*1.0)/process);
    


    

    