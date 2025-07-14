
from crewai import Agent

class PlannerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Planner Agent",
            role="Breaks down the topic into an outline",
            goal="Create a structured outline for an article",
            backstory="An experienced editor that outlines content before writing begins."
        )

    def plan(self, topic):
        return f"Outline for article on '{topic}':\n1. Introduction\n2. Background\n3. Key Points\n4. Conclusion"
