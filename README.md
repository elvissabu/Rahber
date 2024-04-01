# Rahber

This repository contains files related to the development of a comprehensive educational platform designed to facilitate seamless learning experiences for users. Below is an overview of the main components included in this repository:

## Course Dependency Resolution

**File:** `course_dependency_resolution.py`

This Python script implements an algorithm to efficiently resolve course prerequisites on our video course platform. It optimizes course completion time, accommodates parallel course enrollment, and intelligently manages circular dependencies.

In the provided example:

- We initialize a new instance of the `CoursePlatform` class, creating a platform to manage courses and their dependencies.
- We add several courses to the platform using the `add_course` method. Each course is added with its name, and some courses also include completion times and prerequisites. Here's the breakdown of the courses added:
  - "Introduction to Python": A foundational course with a completion time of 5 units.
  - "Data Structures and Algorithms": Builds upon "Introduction to Python" with a completion time of 8 units.
  - "Machine Learning Fundamentals": Also builds upon "Introduction to Python" with a completion time of 10 units.
  - "Deep Learning": Requires completing "Machine Learning Fundamentals" with a completion time of 12 units.
  - "Natural Language Processing": Also requires "Machine Learning Fundamentals" with a completion time of 15 units.
  - "Advanced Python": Builds upon "Introduction to Python" with a completion time of 6 units.
- We use the `get_learning_path` method of the platform instance to retrieve the learning path and total completion time for the course "Natural Language Processing". This method calculates the sequence of courses needed to be completed before reaching the target course and returns the total completion time required.
- Finally, we print out the learning path for "Natural Language Processing" and its total completion time to the console.

## Scalable Video Streaming

**File:** `scalable_video_platform_architecture.pdf`

This document proposes a system architecture for scalable video streaming, ensuring low latency, high availability, and adaptive streaming quality for a diverse global audience. It covers various components such as content ingestion, CDN utilization, load balancing, and security measures.

## Personalized Learning Path Generation

**File:** `learning_path_generator.py`

This Python script generates personalized learning paths for users based on their interests, past course engagements, and performance data. It filters courses matching user interests and ensures they have not already completed them, providing a tailored learning experience.

**Example provided within code as below**

Suppose we have users with different interests, completed courses, and performance metrics:

- User 1: Interests in Python and programming, completed course "Python Programming" with a score of 90.
- User 2: Interests in machine learning and Python, completed course "Machine Learning Basics" with a score of 85.
- User 3: Interests in web development and Python (no completed courses or performance data).
- User 4: Interests in data science and Python, completed course "Data Science Fundamentals" with a score of 88.

The script will generate personalized learning paths for each user, recommending relevant courses based on their interests and past engagements.
