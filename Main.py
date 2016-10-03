import random
ARRIVAL_TIME = 1
JOB_NUM = 0
JOB_LEN = 2
test_job = [[1, 4, 9], [2,15,2], [3, 18, 16], [4,20,3],[5, 26, 29], [6,29,198],[7, 35, 7], [8,45,170],[9, 57, 180], \
            [10,83,178],[11, 88, 73], [12,95,8] ]

class Round_Robin():
    def __init__(self, jobs):
        self.jobs = jobs
        self.proc_jobs = self.prep_processor(4)

    def prep_processor(self, num_proc):
        n_jobs = []
        for i in range(0, num_proc):
            n_jobs.append([])

        for job in self.jobs:
            n_jobs[job[0] % num_proc].append(job)

        return n_jobs

    def apply_processor(self, proc):

        time = 0
        counter = 0
        while (True):

            if (proc[counter][ARRIVAL_TIME] < time):
                if (proc[counter][JOB_LEN] > 0):
                    proc[counter][JOB_LEN] -= 1
                    time += 1
                elif (counter == len(proc) - 1):
                    return time
                else:
                    counter += 1
                    time += 1

            else:
                time += 1


    def run(self):

        result_0 = self.apply_processor(self.proc_jobs[0])
        result_1 = self.apply_processor(self.proc_jobs[1])
        result_2 = self.apply_processor(self.proc_jobs[2])
        result_3 = self.apply_processor(self.proc_jobs[3])
        return max(result_0, result_1, result_2, result_3)


class SRT():
    def __init__(self, jobs):
        self.jobs = jobs




def make_jobs():
    jobs = []

    for i in range(0,1000):
        jobs.append([i, i, random.randint(1, 1000)])
    return jobs



#randomly create jobs
x = make_jobs()
#add jobs to processor7
y = Round_Robin(x)
print (y.run())


#apply processor to each queue






