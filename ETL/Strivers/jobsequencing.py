class job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit




class Solution:
    def jobScheduling(self, jobs):
        jobs.sort(key=lambda x: x.profit, reverse=True) #sort the jobs on the basis of profit in descending order
        maxi = jobs[0].deadline
        for i in range(1, len(jobs)):
            maxi = max(maxi, jobs[i].deadline)#calculate the maximum deadline of the job


        slot = [-1] * (maxi + 1)#initialise arry [-1 with size maxdeadeline
        countJobs = 0
        jobProfit = 0


        for i in range(len(jobs)): #put the jobs in the longest ossible day if free 
            for j in range(jobs[i].deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    countJobs += 1
                    jobProfit += jobs[i].profit
                    break


        return countJobs, jobProfit




if __name__ == "__main__":
    jobs = [job(1, 4, 20), job(2, 1, 10), job(3, 2, 40), job(4, 2, 30)]
    count, profit = Solution().jobScheduling(jobs)
    print(count, profit)
