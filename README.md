# Agentic-Blog-Generator
Agentic based Blog generator made using CREWAI, Serper and Groq Api

# Agentic Blog Generator 🤖✍️

An intelligent, multi-agent blog generation system that leverages CrewAI, Groq LLM, and Streamlit to create well-researched, SEO-optimized content with real-time progress tracking.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.x-red)
![CrewAI](https://img.shields.io/badge/crewai-latest-orange)
![License](https://img.shields.io/badge/license-MIT-green)

## 🎯 Overview

Agentic Blog Generator is a sophisticated content creation tool that combines the power of multiple AI agents to research, write, and edit high-quality blog posts. Watch in real-time as the system plans, researches, writes, and polishes your content.

## 🌟 Features

### Core Functionality
- **Interactive Web Interface**: Streamlit-based UI with real-time progress tracking
- **Multi-Agent System**: Specialized agents for planning, writing, and editing
- **AI-Powered Content**: Utilizing Groq's LLaMA 3.1 70B model
- **Research Integration**: Automated Google search via Serper API

### Content Quality
- **SEO Optimization**: Keyword integration and optimization
- **Research-Backed**: Real-time web research integration
- **Quality Control**: Multi-stage content refinement
- **Structured Output**: Professional formatting and organization

### User Experience
- **Real-Time Progress**: Watch the content creation process unfold
- **Customizable Output**: Adjustable word count and content focus
- **Interactive Display**: Expandable sections for detailed progress
- **Content Download**: Easy export in Markdown format

## 📋 Prerequisites

- Python 3.8 or higher
- Active Groq API account
- Active Serper API account
- Stable internet connection

## 🛠️ Installation

1. **Clone the Repository**
```bash
git clone https://github.com/abdullah-w-21/Agentic-Blog-Generator.git
cd Agentic-Blog-Generator
```

2. **Set Up Virtual Environment (Recommended)**
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API Keys**

Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## 📦 Dependencies

```text
streamlit==1.32.0
crewai==0.11.0
python-dotenv==1.0.0
langchain-groq==0.0.3
requests==2.31.0
```

## 🚀 Usage

1. **Start the Application**
```bash
streamlit run app.py
```

2. **Access the Interface**
- Open your browser
- Navigate to `http://localhost:8501`

3. **Generate Content**
   - Enter your topic
   - Add relevant keywords
   - Specify key points
   - Set desired word count
   - Click "Generate Blog Post ✨"

4. **Monitor Progress**
   - Watch real-time research updates
   - View agent activities
   - Track content development
   - Download the final result

## 🔧 System Architecture

### Agent System
1. **Strategic Content Planner**
   - Researches topic
   - Analyzes audience
   - Creates content strategy
   - Identifies key angles

2. **Expert Content Creator**
   - Develops narrative
   - Incorporates research
   - Maintains engagement
   - Ensures topic coverage

3. **Senior Content Editor**
   - Refines structure
   - Enhances clarity
   - Optimizes SEO
   - Polishes final output

## 📊 Progress Tracking

The system provides real-time updates on:
- Research progress
- Content planning
- Writing status
- Editing process
- Final refinements


## 🐛 Troubleshooting

Common issues and solutions:
1. **API Key Errors**
   - Verify API keys in `.env`
   - Check environment variables
   - Confirm API account status

2. **Generation Issues**
   - Check internet connection
   - Verify input parameters
   - Review API quotas

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Important Notes

- Monitor API usage and credits
- Review generated content before publishing
- Keep API keys secure
- Regular updates recommended

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the multi-agent framework
- [Groq](https://groq.com/) for the LLM capabilities
- [Serper](https://serper.dev/) for Google search API
- [Streamlit](https://streamlit.io/) for the web interface

## 📧 Contact

Abdullah Wasim - [LinkedIn](https://pk.linkedin.com/in/abdullah-wasim-436a39253)

Project Link: [Agentic Blog Generator](https://github.com/abdullah-w-21/Agentic-Blog-Generator)

## 🚨 Disclaimer

This tool uses AI to generate content. While it strives for accuracy and quality:
- Always review and edit generated content
- Verify facts and sources
- Consider your audience and context
- Monitor for potential biases or inaccuracies

---
Made with ❤️ by Abdullah Wasim
