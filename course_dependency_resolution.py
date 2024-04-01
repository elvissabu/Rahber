from collections import defaultdict, deque

class Course:
    def __init__(self, name, completion_time=0):
        """
        Initialize a Course object.

        Parameters:
        - name: Name of the course.
        - completion_time: Time required to complete the course (default: 0).
        """
        self.name = name
        self.prerequisites = set()
        self.completion_time = completion_time

class CourseGraph:
    def __init__(self):
        """
        Initialize a CourseGraph object.
        """
        self.graph = defaultdict(lambda: Course(""))
        self.circular_dependencies = []

    def add_course(self, name, completion_time=0, prerequisites=None):
        """
        Add a course to the graph.

        Parameters:
        - name: Name of the course.
        - completion_time: Time required to complete the course (default: 0).
        - prerequisites: List of prerequisite courses (default: None).
        """
        if prerequisites is None:
            prerequisites = []
        course = self.graph[name]
        course.name = name
        course.completion_time = completion_time
        course.prerequisites.update(prerequisites)

    def add_prerequisite(self, course_name, prerequisite_name):
        """
        Add a prerequisite for a course.

        Parameters:
        - course_name: Name of the course.
        - prerequisite_name: Name of the prerequisite course.
        """
        self.graph[course_name].prerequisites.add(prerequisite_name)

    def detect_circular_dependencies(self):
        """
        Detect circular dependencies using depth-first search (DFS).
        """
        stack = set()
        visited = set()
        for course_name in self.graph:
            if course_name not in visited:
                if self._dfs(course_name, visited, stack):
                    return True
        return False

    def _dfs(self, course_name, visited, stack):
        """
        Depth-first search (DFS) to detect circular dependencies.
        """
        if course_name in stack:
            self.circular_dependencies = list(stack) + [course_name]
            return True

        if course_name in visited:
            return False

        visited.add(course_name)
        stack.add(course_name)

        for prerequisite in self.graph[course_name].prerequisites:
            if self._dfs(prerequisite, visited, stack):
                return True

        stack.remove(course_name)
        return False

    def merge_common_time(self):
        """
        Merge completion times of courses involved in circular dependencies.
        """
        if self.circular_dependencies:
            common_time = sum(self.graph[course_name].completion_time for course_name in self.circular_dependencies)
            for course_name in self.circular_dependencies:
                self.graph[course_name].completion_time = common_time

    def recalculate_completion_times(self):
        """
        Recalculate completion times after merging common time.
        """
        completion_times = defaultdict(int)
        for course_name, course in self.graph.items():
            completion_times[course_name] = course.completion_time
            for prerequisite in course.prerequisites:
                completion_times[course_name] += completion_times[prerequisite]
        return completion_times

    def topological_sort(self):
        """
        Perform topological sort to get the learning path and completion times.
        """
        if self.detect_circular_dependencies():
            self.merge_common_time()

        completion_times = self.recalculate_completion_times()

        in_degree = defaultdict(int)
        for course in self.graph.values():
            for prerequisite in course.prerequisites:
                in_degree[prerequisite] += 1

        queue = deque([course_name for course_name in self.graph if in_degree[course_name] == 0])
        order = []

        while queue:
            course_name = queue.popleft()
            order.append(course_name)
            for prerequisite in self.graph[course_name].prerequisites:
                in_degree[prerequisite] -= 1
                if in_degree[prerequisite] == 0:
                    queue.append(prerequisite)

        return order, completion_times

class CoursePlatform:
    def __init__(self):
        """
        Initialize a CoursePlatform object.
        """
        self.graph = CourseGraph()

    def add_course(self, name, completion_time=0, prerequisites=None):
        """
        Add a course to the platform.

        Parameters:
        - name: Name of the course.
        - completion_time: Time required to complete the course (default: 0).
        - prerequisites: List of prerequisite courses (default: None).
        """
        if prerequisites is None:
            prerequisites = []
        self.graph.add_course(name, completion_time, prerequisites)

    def add_prerequisite(self, course_name, prerequisite_name):
        """
        Add a prerequisite for a course.

        Parameters:
        - course_name: Name of the course.
        - prerequisite_name: Name of the prerequisite course.
        """
        self.graph.add_prerequisite(course_name, prerequisite_name)

    def get_learning_path(self, target_course):
        """
        Get the learning path and total completion time for a target course.

        Parameters:
        - target_course: Name of the target course.

        Returns:
        - Tuple containing the learning path (list of courses) and total completion time.
        """
        try:
            learning_path, completion_times = self.graph.topological_sort()
            target_index = learning_path.index(target_course)
            total_completion_time = completion_times[target_course]
            return learning_path[:target_index+1], total_completion_time
        except ValueError as e:
            print(e)

# demonstrating Usage
def main():
    # Simple learning path
    # platform = CoursePlatform()

    # # Adding courses and their dependencies
    # platform.add_course("Introduction to Python", 5)
    # platform.add_course("Data Structures and Algorithms", 8, ["Introduction to Python"])
    # platform.add_course("Machine Learning Fundamentals", 10, ["Introduction to Python"])
    # platform.add_course("Deep Learning", 12, ["Machine Learning Fundamentals"])
    # platform.add_course("Natural Language Processing", 15, ["Machine Learning Fundamentals"])
    # platform.add_course("Advanced Python", 6, ["Introduction to Python"])

    # # Getting learning path for Natural Language Processing
    # learning_path, total_completion_time = platform.get_learning_path("Natural Language Processing")
    # if learning_path is not None:
    #     print("Learning Path for Natural Language Processing:", learning_path)
    #     print("Total Completion Time:", total_completion_time)
    
    # Circular dependency learning path
    platform = CoursePlatform()

    # Adding courses and their dependencies with circular dependency
    platform.add_course("Introduction to Python", 5)
    platform.add_course("Data Structures and Algorithms", 8, ["Introduction to Python"])
    platform.add_course("Machine Learning Fundamentals", 10, ["Introduction to Python"])
    platform.add_course("Deep Learning", 12, ["Machine Learning Fundamentals", "Data Structures and Algorithms"])  # Circular dependency
    platform.add_course("Natural Language Processing", 15, ["Machine Learning Fundamentals"])
    platform.add_course("Advanced Python", 6, ["Introduction to Python"])

    # Getting learning path for Deep Learning (which has circular dependency)
    learning_path, total_completion_time = platform.get_learning_path("Natural Language Processing")
    if learning_path is not None:
        print("Total Completion Time:", total_completion_time)
    
    learning_path, total_completion_time = platform.get_learning_path("Deep Learning")
    if learning_path is not None:
        print("Total Completion Time:", total_completion_time)

if __name__ == "__main__":
    main()
