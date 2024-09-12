import random


class DatasetGenerator:
    def __init__(self):
        self.projects = ["Project A", "Project B",
                         "Project C", "Project D", "Project E"]
        self.tasks = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5"]

        # Translated Task Descriptions
        self.task_descriptions = [
            "Develop the project plan and finalize project scope with stakeholders.",
            "Identify and mitigate risks that may impact the project timeline or budget.",
            "Perform a detailed analysis of project requirements to ensure all objectives are met.",
            "Manage project resources and ensure all team members are aligned with the project goals.",
            "Conduct a post-implementation review to evaluate project success and identify improvement areas."
        ]

        # EVM metrics used in project performance tracking
        self.status_metrics = ['Planned Value (PV)', 'Earned Value (EV)', 'Actual Cost (AC)',
                               'Budget at Completion (BAC)', 'Cost Performance Index (CPI)',
                               'Schedule Performance Index (SPI)', 'Estimate at Completion (EAC)',
                               'Variance at Completion (VAC)']

    def generate_dataset(self, num_projects, num_tasks, include_description):
        dataset = []
        # Calculate the total number of tasks across all projects
        total_num_tasks = num_projects * num_tasks

        for _ in range(num_projects):
            project = random.choice(self.projects)
            tasks = random.choices(self.tasks, k=num_tasks)

            # Generate project-level performance metrics
            project_data = {
                "project": project,
                "tasks": [],
                "performance_metrics": {
                    "Budget at Completion (BAC)": random.randint(100000, 500000),
                    "Planned Value (PV)": round(random.uniform(50000, 300000), 2),
                    "Earned Value (EV)": round(random.uniform(50000, 300000), 2),
                    "Actual Cost (AC)": round(random.uniform(50000, 300000), 2),
                    "Cost Performance Index (CPI)": round(random.uniform(0.8, 1.2), 2),
                    "Schedule Performance Index (SPI)": round(random.uniform(0.8, 1.2), 2),
                    "Estimate at Completion (EAC)": random.randint(100000, 500000),
                    "Variance at Completion (VAC)": round(random.uniform(-50000, 50000), 2)
                }
            }

            # Generate task-level data with optional description
            for task in tasks:
                task_data = {
                    "task": task,
                    "Cost Variance (CV)": round(random.uniform(-50000, 50000), 2),
                    "Schedule Variance (SV)": round(random.uniform(-50000, 50000), 2)
                }

                # Add task description if required
                if include_description:
                    task_data["description"] = random.choice(
                        self.task_descriptions)

                project_data["tasks"].append(task_data)

            dataset.append(project_data)

        return dataset
