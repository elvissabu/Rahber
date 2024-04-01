import random

class User:
    def __init__(self, user_id, interests, completed_courses=None, performance=None):
        """
        Initialize a User object.

        Parameters:
        - user_id: User identifier.
        - interests: List of user interests or tags.
        - completed_courses: Set of completed course IDs (default: None).
        - performance: Dictionary mapping course IDs to performance scores (default: None).
        """
        self.user_id = user_id
        self.interests = interests
        self.completed_courses = completed_courses if completed_courses else set()
        self.performance = performance if performance else {}

    def update_performance(self, course_id, score):
        """
        Update user's performance for a course.

        Parameters:
        - course_id: ID of the course.
        - score: Performance score for the course.
        """
        self.performance[course_id] = score
        # Additional logic for updating user performance metrics can be included here.

class Course:
    def __init__(self, course_id, title, tags):
        """
        Initialize a Course object.

        Parameters:
        - course_id: Course identifier.
        - title: Title of the course.
        - tags: List of tags or topics related to the course.
        """
        self.course_id = course_id
        self.title = title
        self.tags = tags

class LearningPathGenerator:
    def __init__(self, courses):
        """
        Initialize a LearningPathGenerator object.

        Parameters:
        - courses: List of Course objects.
        """
        self.courses = courses

    def generate_learning_path(self, user):
        """
        Generate a learning path for a given user based on their interests and completed courses.

        Parameters:
        - user: User object.

        Returns:
        - List of recommended Course objects for the user.
        """
        recommended_courses = self._filter_courses(user)
        return recommended_courses

    def _filter_courses(self, user):
        """
        Filter courses based on user interests and completed courses.

        Parameters:
        - user: User object.

        Returns:
        - List of Course objects recommended for the user.
        """
        recommended_courses = []
        for course in self.courses:
            if any(tag in course.tags for tag in user.interests) and course.course_id not in user.completed_courses:
                recommended_courses.append(course)
        return recommended_courses

# Example usage
def main():
    # Dummy data for courses
    courses = [
        Course(1, "Python Programming", ["programming", "python"]),
        Course(2, "Machine Learning Basics", ["machine learning", "python"]),
        Course(3, "Web Development with Django", ["web development", "python"]),
        Course(4, "Data Science Fundamentals", ["data science", "python"]),
    ]
    
    # Dummy data for users
    users = [
        User(1, ["python", "programming"], completed_courses={1}, performance={1: 90}),
        User(2, ["machine learning", "python"], completed_courses={2}, performance={2: 85}),
        User(3, ["web development", "python"]),
        User(4, ["data science", "python"], completed_courses={4}, performance={4: 88}),
    ]

    # Learning path generation for each user
    path_generator = LearningPathGenerator(courses)
    for user in users:
        learning_path = path_generator.generate_learning_path(user)
        print(f"Learning path for User {user.user_id}:")
        for course in learning_path:
            print(f"{course.course_id}: {course.title}")

if __name__ == "__main__":
    main()
