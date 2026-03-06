from crewai import Crew

def get_research_crew():
    from agents.research_specialist import research_specialist_agent
    from agents.data_analyst import data_analyst_agent
    from agents.content_writer import content_writer_agent
    from tasks.research_task import research_task
    from tasks.analysis_task import analysis_task
    from tasks.writing_task import writing_task

    return Crew(
        agents=[
            research_specialist_agent,
            data_analyst_agent,
            content_writer_agent,
        ],
        tasks=[
            research_task,
            analysis_task,
            writing_task,
        ],
        verbose=True
    )