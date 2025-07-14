
from crewai import Agent

class ReviewerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Reviewer Agent",
            role="Reviews and improves the written content",
            goal="Polish the draft and correct issues",
            backstory="A professional editor that ensures the article is publication-ready."
        )

    def review(self, draft):
        return f"Final Reviewed Article:\n{draft}\n\n[Edited for clarity and grammar]"
