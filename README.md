# 📝 `Blog Writer` Crew AI Agents - Streamlit App 🖋️
Blog Writer Crew AI Agents to Get `Blog` based on a specific `Topic`.

## 📝 Work Flow
- Streamlit Ai Crew - 3 Agents :
- `CrewAi` : Framework for Agents, Tasks and Tools (2x2 Agents/Tasks)
- `Callbacks` : To render the Agents processing and final outputs
- `DuckSearchTools` : Get the informations from DuckDuckGo Search Class
- `Groq API` : for Inference
- `llama3` : as LLM


## BLOG WRITER : DuckDuckGo Search & CREW AI
- Blog Writer assitant to help generate a LLM powered Blog posts based on your topic.

![CrewAi App WorkFlow](TravelPlanner_screenshot.png)

## CREW AI AGENT :
- An advanced research assistant by leveraging LangChain-powered tools into a CrewAI-powered multi-agent setup.
- LangChain is a framework enabling developers to easily build LLM-powered applications over their data; it contains production modules for indexing, retrieval, and prompt/agent orchestration.
- A core use case is building a generalized QA interface enabling knowledge synthesis over complex questions.
- Plugging a LangChain RAG pipeline as a tool into a CrewAI agent setup enables even more sophisticated/advanced research flows

## ✈️ Run the App
- Fork or Clone the Repo
- Get and Put your `GROQ_API` in `.streamlit/secrets.toml`
- Run : `streamlit run blog_app.py`
