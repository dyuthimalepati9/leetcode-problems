import heapq
class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        nbCourses = 0
        heap = []
        for dur, lastD in courses:
            nbCourses += dur
            heapq.heappush(heap, -dur)
            if nbCourses > lastD:
                nbCourses += heapq.heappop(heap)
        return len(heap)   