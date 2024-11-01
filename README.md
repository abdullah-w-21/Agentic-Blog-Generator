# Agentic-Blog-Generator
Agentic based Blog generator made using CREWAI, Serper and Groq Api

# AI-Powered Blog Generator with Streamlit 📝

A sophisticated blog post generator that combines CrewAI, Groq LLM, and Streamlit to create well-researched, SEO-optimized blog content with a user-friendly interface.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.x-red)
![License](https://img.shields.io/badge/license-MIT-green)

## 🌟 Features

- **Interactive Web Interface**: Built with Streamlit for easy content generation
- **AI-Powered Content Creation**: Utilizing Groq's LLaMA 3.1 70B model
- **Multi-Agent System**: Uses CrewAI with specialized agents for planning, writing, and editing
- **Web Research Integration**: Automated Google search via Serper API
- **SEO Optimization**: Keyword-focused content generation
- **Medium.com Style**: Content aligned with Medium's writing standards
- **Customizable Output**: Adjustable word count and content structure

## 📋 Prerequisites

- Python 3.8+
- Groq API key
- Serper API key
- Required Python packages

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/abdullah-w-21/Agentic-Blog-Generator.git
cd Agentic-Blog-Generator
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your API keys:
```env
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

## 📦 Dependencies

Create a `requirements.txt` file with the following:

```text
streamlit
crewai
python-dotenv
langchain-groq
requests
```

## 🚀 Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Access the web interface at `http://localhost:8501`

3. Fill in the form with:
   - Topic
   - Keywords (comma-separated)
   - Bullet points for context
   - Desired word count

4. Click "Generate Blog Post" and wait for the magic to happen!

## 🔧 Configuration

The application uses three main agents:

1. **Content Planner**: Researches and outlines the content
2. **Content Writer**: Creates the initial draft
3. **Editor**: Polishes and finalizes the content

Each agent can be configured by modifying their parameters in the code:
- `role`: Agent's specific role
- `goal`: Primary objective
- `backstory`: Context for decision-making
- `verbose`: Debugging output


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Important Notes

- The quality of generated content depends on the input parameters
- Always review and edit the generated content before publishing
- The app uses significant API credits - monitor your usage

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- CrewAI for the multi-agent framework
- Groq for the LLM capabilities
- Serper for Google search API
- Streamlit for the web interface

## 📧 Contact

Abdullah Wasim - (https://pk.linkedin.com/in/abdullah-wasim-436a39253)

Project Link: (https://github.com/abdullah-w-21/Agentic-Blog-Generator)

## ⚠️ Disclaimer

This tool uses AI to generate content. Always review and edit the generated content before publishing. The quality and accuracy of the output depend on the input parameters and available research data.
