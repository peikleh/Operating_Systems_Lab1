"""
Author: Nevin Leh

Description:This file contains two classes that apply two different processor scheduling algorithms.
The first is round robin as described in the problem statement. The second is shortest remaining time. This
algorith adds each successive job to the processor with the shortest queue in terms of time remaining.
Both algorithms just simulate the resulting run times. They do not accurately depict how this would be done in
real time.

Instructions: run in terminal with <python leh_1.py>
              Written in Python 3.5
              output in leh_1.output

Note: For 100 samples this program can take a while to run. Give it a couple minutes.

"""
import random
import copy
import math
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

        result_0 = apply_processor(self.proc_jobs[0])
        result_1 = apply_processor(self.proc_jobs[1])
        result_2 = apply_processor(self.proc_jobs[2])
        result_3 = apply_processor(self.proc_jobs[3])
        return max(result_0, result_1, result_2, result_3)


class SRT():
    """This class takes in a list of jobs and assignes them to processors in a shortest remaining time scheme.
    This implementation simply precomputes what the shortest processor queue is and adds the next job to that queue. This
    is before the processors are even simulated.
    """
    def __init__(self, jobs):
        self.jobs = jobs
        self.proc_jobs = [[],[],[],[]]


    def shortest(self, procs):
        """Given a list of  processor queues, return the index of the processor with the shortest queue"""
        min = 0
        for i in range(0, len(procs)):
            if (self.time_left(procs[i]) < self.time_left(procs[min])):
                min = i
        return min

    def time_left(self, proc):
        """Calculates and returns the time left on a processor"""
        total = 0
        for i in proc:
            total += i[2]
        return total

    def make_proc_queues(self):
        """Loops through jobs, assigning them to the processor with the shortest queue"""
        for job in self.jobs:
            shortest = self.shortest(self.proc_jobs)
            self.proc_jobs[shortest].append(job)

    def run(self):
        """Makes processor queues and runs each queue on a processor. Then returns """
        self.make_proc_queues()
        result_0 = apply_processor(self.proc_jobs[0])
        result_1 = apply_processor(self.proc_jobs[1])
        result_2 = apply_processor(self.proc_jobs[2])
        result_3 = apply_processor(self.proc_jobs[3])
        return max(result_0, result_1, result_2, result_3)



def apply_processor( proc):
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

def make_jobs():
    jobs = []
    for i in range(0,1000):
        jobs.append([i, i, random.randint(1, 1000)])
    return jobs

def std_dev(test_info):
    """Finds standard deviation of a list"""
    mean = sum(test_info)/float(len(test_info))
    sums = 0
    for info in test_info:
        sums += (info - mean)**2
    sums = sums/float(len(test_info))
    sums = math.sqrt(sums)
    return sums


def main():
    rr = 0
    srt =0

    #test test_set on round robin
    rr_test_set = copy.deepcopy(test_job)
    rr_o = Round_Robin(rr_test_set)
    rr = rr_o.run()

    #test test_set on Shortest Remaining time
    srt_o = SRT(test_job)
    srt = srt_o.run()

    #data for random tests
    rr_test_info = []
    srt_test_info = []

    #do test 100 times
    for i in range (0, 100):
        print ("Running test: " + str(i+1))

        #make random set and a copy
        random_set = make_jobs()
        rr_set = copy.deepcopy(random_set)

        #apply round robin to set
        x = Round_Robin(rr_set)
        rr_test_info.append(x.run())

        #apply SRT to set
        y = SRT(random_set)
        srt_test_info.append(y.run())

    output = open("output.out", 'w')
    output.write("Given data set results:\n    RoundRobin: " + str(rr) + "\n    SRT: " + str(srt))

    output.write("\n\n100 Random sets of 1000 results:\n\n")

    output.write("    RoundRobin:\n")
    output.write("               Minimum: " + str(min(rr_test_info)))
    output.write("\n               Maximum: " + str(max(rr_test_info)))
    output.write("\n                  Mean: " + str(sum(rr_test_info)/float(len(rr_test_info))))
    output.write("\n               Std Dev: " + str(std_dev(rr_test_info)))

    output.write("\n\n           SRT:\n")
    output.write("               Minimum: " + str(min(srt_test_info)))
    output.write("\n               Maximum: " + str(max(srt_test_info)))
    output.write("\n                  Mean: " + str(sum(srt_test_info) / float(len(srt_test_info))))
    output.write("\n               Std Dev: " + str(std_dev(srt_test_info)))
    print("Test done. Check leh_1.output for stats.")

if __name__ == "__main__":
    main()







