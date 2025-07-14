
from agents.planner_agent import PlannerAgent
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent

def main():
    topic = "The Rise of AI in Everyday Life"

    planner = PlannerAgent()
    outline = planner.plan(topic)

    writer = WriterAgent()
    draft = writer.write(outline)

    reviewer = ReviewerAgent()
    final_article = reviewer.review(draft)

    print("=== Final Article ===")
    print(final_article)

if __name__ == "__main__":
    main()
