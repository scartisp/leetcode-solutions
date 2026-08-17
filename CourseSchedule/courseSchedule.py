class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        status = [0]*numCourses

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        def checkDependencies(course) -> bool:
            if status[course] == 1:
                return False
            if status[course] == 2:
                return True
            if status[course] == 0:
                status[course] = 1
            
            for prereq in graph[course]:
                if not checkDependencies(prereq):
                    return False
            
            status[course] = 2
            return True
        
        for course in graph:
            if not checkDependencies(course):
                return False

        return True
