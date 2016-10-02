import random
ARRIVAL_TIME = 1
JOB_NUM = 0
JOB_LEN = 2

def make_jobs():
    jobs = []
    total = 0
    for i in range(0,1000):
        jobs.append([i, i, random.randint(1, 1000)])
        total += jobs[i][JOB_LEN]
    print(total)
    return jobs

def prep_processor(jobs, num_proc):
    n_jobs = []
    for i in range(0, num_proc):
        n_jobs.append([])

    for job in jobs:
        n_jobs[job[0]%num_proc].append(job)

    return n_jobs


def apply_processor(proc):
    time = 0
    counter = 0
    while (True):


        if (proc[counter][ARRIVAL_TIME] < time):
            if (proc[counter][JOB_LEN] > 0):
                proc[counter][JOB_LEN] -= 1
                time += 1
            elif (counter == len(proc) -1 ):
                return time
            else:
                counter += 1
                time +=1

        else:
            time += 1

#randomly create jobs
x = make_jobs()
#add jobs to each processors queue
y = prep_processor(x, 4)
#apply processor to each queue
result_0 = apply_processor(y[0])
result_1 = apply_processor(y[1])
result_2 = apply_processor(y[2])
result_3 = apply_processor(y[3])


print(result_0)
print(result_1)
print(result_2)
print(result_3)

print(result_0 + result_1 + result_2 + result_3)




