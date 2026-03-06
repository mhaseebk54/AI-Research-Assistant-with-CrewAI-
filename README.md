📌 AI Research Assistant with CrewAI

A multi-agent AI research assistant built with CrewAI, Streamlit, and Groq LLMs, designed to autonomously research topics, analyze data, and generate reports.

🔍 Features

🧠 Multi-Agent System using CrewAI:

Research Specialist: Gathers information from multiple sources.

Data Analyst: Processes and analyzes research findings.

Content Writer: Generates detailed reports.

📝 Automated Research Workflow: From topic input to final report.

🌐 Streamlit Frontend: Easy-to-use web interface for research tasks.

🔑 Environment-Based Configuration: Securely store API keys in a .env file.

📄 Exportable Reports: Download research, analysis, and final reports in Markdown.

🛠 Tech Stack

CrewAI – Multi-agent orchestration

LiteLLM / Groq – Language model backend

Streamlit – Web application frontend

Python 3.10+ – Programming language

dotenv – Environment variable management

🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/your-username/ai-research-assistant.git
cd ai-research-assistant
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Create .env file

Create a .env in the project root with your API keys:

SERPER_API_KEY=your_serper_api_key
GROQ_API_KEY=your_groq_api_key
WRITER_AGENT_LLM=llama-3.3-70b-versatile
4️⃣ Run the app
streamlit run app.py
📝 Usage

Enter a research topic in the Streamlit input box.

Click Start Research.

The agents will:

🔍 Gather research data

📊 Analyze results

✍️ Generate a final report

View and download the results from tabs for:

Research Findings

Analysis Report

Final Report

⚙️ Configuration

Ensure all API keys are valid and set in .env.

Agent models are defined in agents/ folder.

Tasks are defined in tasks/ folder.

