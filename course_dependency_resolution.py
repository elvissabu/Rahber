from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        visited = {node: False for node in self.graph}
        stack = []

        for node in self.graph:
            if not visited[node]:
                self.topologicalSortUtil(node, visited, stack)

        return stack[::-1]

def resolvePrerequisites(courses):
    graph = Graph()

    # Add all courses to the graph
    for course in courses.keys():
        graph.addEdge(course, None)

    # Build the graph
    for course, prerequisites in courses.items():
        for prerequisite in prerequisites:
            graph.addEdge(prerequisite, course)

    # Check for circular dependency
    if hasCircularDependency(graph):
        print("Circular dependency detected. Please resolve manually.")
        return None
    else:
        sortedCourses = graph.topologicalSort()
        return sortedCourses

def hasCircularDependency(graph):
    visited = set()
    recStack = set()

    def isCyclicUtil(v):
        if v not in visited:
            visited.add(v)
            recStack.add(v)
            for neighbor in graph.graph.get(v, []):
                if neighbor not in visited and isCyclicUtil(neighbor):
                    return True
                elif neighbor in recStack:
                    return True
        recStack.remove(v)
        return False

    for node in graph.graph:
        if isCyclicUtil(node):
            return True
    return False

# Example usage
# courses = {
#     'C': ['A', 'B'],
#     'A': [],
#     'B': ['A']
# }

# sortedCourses = resolvePrerequisites(courses)
# if sortedCourses:
#     print("Course order:", sortedCourses)
