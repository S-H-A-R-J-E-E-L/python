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
total = 0;
temp = 0;
p = 0;
t = 0;
avg_wait_time = 0;
avg_turn_time = 0;

process = input("Enter Total Process: ");

for i in range(0, process):
    x = raw_input("Enter Burst Time: ");
    burst_time.append(int(x));
    process_no.append(int(i+1));
    

for j in range (0, process):
    p = i;
    t = t+i;
    for k in range(t, process):
        if(burst_time[k] < burst_time[p]):
            p = k;
            
    temp = burst_time[j];
    burst_time[j] = burst_time[p];
    burst_time[p] = temp;
    
    temp = process_no[j];
    process_no[j] = process_no[p];
    process_no[p] = temp;
    
    

for m in range(1, process):
    wait_time[m] = 0;
    for j in range(0, i):
        wait_time[m] += burst_time[j];
        
    total += wait_time[m];
    
avg_wait_time = total/process;
total = 0;

print("\nProcess\t Burst Time   \tWaiting Time\t   Turnaround Time");

for l in range(0, process):
    turnaround_time[l] = burst_time[l] + wait_time[l];   
    total += turnaround_time[l];
    print(process_no[l], burst_time[l], wait_time[l], turnaround_time[l] );
    
avg_turn_time = total/process;

print("Average Waiting Time", avg_wait_time);
print("Average Turnaround Time", avg_turn_time);

    

    