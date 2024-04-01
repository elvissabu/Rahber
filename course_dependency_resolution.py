from collections import defaultdict, deque

class Course:
    def __init__(self, name, completion_time=0):
        self.name = name
        self.prerequisites = set()
        self.completion_time = completion_time

class CourseGraph:
    def __init__(self):
        self.graph = defaultdict(lambda: Course(""))

    def add_course(self, name, completion_time=0, prerequisites=None):
        if prerequisites is None:
            prerequisites = []
        course = self.graph[name]
        course.name = name
        course.completion_time = completion_time
        course.prerequisites.update(prerequisites)

    def add_prerequisite(self, course_name, prerequisite_name):
        self.graph[course_name].prerequisites.add(prerequisite_name)

    def get_prerequisites(self, course_name):
        return self.graph[course_name].prerequisites

    def topological_sort(self):
        in_degree = defaultdict(int)
        completion_times = defaultdict(int)
        for course in self.graph.values():
            completion_times[course.name] = course.completion_time
            for prerequisite in course.prerequisites:
                in_degree[prerequisite] += 1

        queue = deque([course_name for course_name in self.graph if in_degree[course_name] == 0])
        order = []

        while queue:
            course_name = queue.popleft()
            order.append(course_name)
            for prerequisite in self.graph[course_name].prerequisites:
                in_degree[prerequisite] -= 1
                completion_times[course_name] += completion_times[prerequisite]
                if in_degree[prerequisite] == 0:
                    queue.append(prerequisite)

        if len(order) == len(self.graph):
            return order, completion_times
        else:
            raise ValueError("Circular dependencies exist")

class CoursePlatform:
    def __init__(self):
        self.graph = CourseGraph()

    def add_course(self, name, completion_time=0, prerequisites=None):
        if prerequisites is None:
            prerequisites = []
        self.graph.add_course(name, completion_time, prerequisites)

    def add_prerequisite(self, course_name, prerequisite_name):
        self.graph.add_prerequisite(course_name, prerequisite_name)

    def get_learning_path(self, target_course):
        try:
            learning_path, completion_times = self.graph.topological_sort()
            target_index = learning_path.index(target_course)
            total_completion_time = completion_times[target_course]
            return learning_path[:target_index+1], total_completion_time
        except ValueError as e:
            print(e)

def main():
    platform = CoursePlatform()

    platform.add_course("Introduction to Python", 5)
    platform.add_course("Data Structures and Algorithms", 8, ["Introduction to Python"])
    platform.add_course("Machine Learning Fundamentals", 10, ["Introduction to Python"])
    platform.add_course("Deep Learning", 12, ["Machine Learning Fundamentals"])
    platform.add_course("Natural Language Processing", 15, ["Machine Learning Fundamentals"])
    platform.add_course("Advanced Python", 6, ["Introduction to Python"])

    learning_path, total_completion_time = platform.get_learning_path("Natural Language Processing")
    print("Learning Path for Natural Language Processing:", learning_path)
    print("Total Completion Time:", total_completion_time)

if __name__ == "__main__":
    main()
