
from crewai import Agent

class WriterAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Writer Agent",
            role="Writes content based on an outline",
            goal="Generate detailed content from a given outline",
            backstory="A skilled writer who can draft well-structured articles."
        )

    def write(self, outline):
        return f"Draft Article based on outline:\n{outline}\n\nIntroduction...\nBackground...\nKey Points...\nConclusion..."
