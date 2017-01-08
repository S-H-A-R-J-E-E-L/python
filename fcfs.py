from array import *
wait_time = array('i', []);
for x in range(0, 100):
    wait_time.append(0);
burst_time = array('i', []);
turnaround_time = array('i', []);
for x in range(0, 100):
    turnaround_time.append(0);
process_no = array('i',[]);
process = 0;
avg_wait_time = 0;
avg_turn_time = 0;

process = input("Enter Total Process: ");

for i in range(0, process):
    x = input("Enter process Burst time: ");
    burst_time.append(int(x));
    
wait_time[0] = 0;

for j in range(1, process):
    wait_time[j] = 0;
    for k in range(0, j):
        wait_time[j] += burst_time[k];
        
print("\n process \t\t Burst Time \t Waiting Time\t Turnaround Time");

for k in range(0, process):
    turnaround_time[k] = burst_time[k] + wait_time[k];
    avg_wait_time += wait_time[k];
    avg_turn_time += turnaround_time[k];
    print(k+1, burst_time[k], wait_time[k], turnaround_time[k]);
    
print("Average Waiting Time: ", avg_wait_time);
print("Average Turnaround Time: ", avg_wait_time);
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    

    