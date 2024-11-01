import streamlit as st
from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.tools import Tool
from langchain.tools import StructuredTool
from typing import Optional
import json
import requests
from datetime import datetime
import time

# load environment variables
load_dotenv()
if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = "your-api-key"
# initialize llm & serper
serper = "your-api-key"
llm = ChatGroq(
    model_name="groq/llama-3.1-70b-versatile"
)




def google_search(query: str) -> dict:
    if 'search_status' in st.session_state:
        st.session_state.search_status.markdown(f"🔎 Researching: {query}")

    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': serper,
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)

    # get search in ui
    if 'search_results' in st.session_state:
        with st.session_state.search_results.expander("📚 Search Results", expanded=False):
            st.json(response.json())

    return response.json()


# searching tool
search_tool = StructuredTool.from_function(
    func=google_search,
    name="Google Search",
    description="Searches Google for articles and information based on the provided query. Input should be a specific search query string."
)

# agent conf with prompts
planner = Agent(
    role="Strategic Content Planner",
    goal="Develop a comprehensive, data-driven content strategy that engages the target audience and provides unique insights on {topic}",
    backstory="""You are an expert content strategist with years of experience in digital content planning. 
    Your strength lies in identifying trending angles, understanding audience psychology, and structuring content 
    that drives engagement. You have a track record of planning viral content that both educates and entertains.""",
    llm=llm,
    tools=[search_tool],
    allow_delegation=False,
    verbose=True
)

writer = Agent(
    role="Expert Content Creator",
    goal="Create an engaging, well-researched, and authoritative article that provides unique insights and actionable value on {topic}",
    backstory="""You are a skilled content creator with expertise in crafting compelling narratives. 
    Your writing style combines deep research with storytelling elements, making complex topics accessible 
    and engaging. You excel at creating content that resonates with readers and drives discussion.""",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

editor = Agent(
    role="Senior Content Editor",
    goal="Refine and polish the content to ensure it meets the highest standards of quality, readability, and impact",
    backstory="""You are a meticulous editor with an eye for detail and a deep understanding of what makes 
    content compelling. You excel at improving clarity, flow, and engagement while maintaining the author's 
    voice. Your edits consistently elevate content to its highest potential.""",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

# task with details
plan = Task(
    description="""
    Develop a comprehensive content strategy by:
    1. Conducting thorough research on {topic} to identify:
       - Latest trends and developments
       - Key industry insights and statistics
       - Unique angles and perspectives
       - Gaps in existing content

    2. Create a detailed audience analysis:
       - Primary demographic and psychographic profiles
       - Key pain points and interests
       - Information needs and content preferences
       - Level of expertise on the topic

    3. Develop a strategic content outline including:
       - Hook and unique value proposition
       - Key arguments and insights
       - Supporting data points and examples
       - Logical flow of information

    4. Identify optimization opportunities:
       - Primary and secondary keywords
       - Relevant sources and citations
       - Content hooks for different platforms
       - Engagement triggers and discussion points

    Use the Google Search tool to validate trends and gather supporting evidence.
    """,
    expected_output="""A detailed content strategy document including:
    1. Research findings and key insights
    2. Audience analysis
    3. Structured content outline
    4. SEO and engagement strategy""",
    agent=planner,
)

write = Task(
    description="""
    Create an exceptional piece of content following these guidelines:
    1. Craft a compelling narrative that:
       - Opens with a powerful hook
       - Presents unique insights and perspectives
       - Maintains reader engagement throughout
       - Supports claims with credible data

    2. Structure the content effectively:
       - Use clear, engaging headlines and subheadings
       - Maintain logical flow between sections
       - Include relevant examples and case studies
       - Create smooth transitions

    3. Optimize for engagement:
       - Incorporate narrative elements and storytelling
       - Use active voice and conversational tone
       - Include thought-provoking questions
       - Add relevant analogies and metaphors

    4. Ensure content meets these criteria:
       - Matches specified length of {length} words
       - Naturally incorporates {keywords}
       - Addresses points from {bullet_points}
       - Provides actionable takeaways

    5. Focus on reader value:
       - Offer practical insights
       - Include expert perspectives
       - Address potential questions
       - Provide clear conclusions
    """,
    expected_output="A polished, engaging article that educates, entertains, and provides genuine value to readers.",
    agent=writer,
)

edit = Task(
    description="""
    Enhance the content through careful editing:
    1. Structural Analysis:
       - Verify logical flow and progression
       - Ensure strong opening and conclusion
       - Check section transitions
       - Validate argument coherence

    2. Content Quality:
       - Verify factual accuracy
       - Check data and statistics
       - Ensure balanced perspective
       - Validate source credibility

    3. Language Enhancement:
       - Improve sentence variety
       - Eliminate redundancy
       - Enhance clarity and impact
       - Maintain consistent tone

    4. Technical Review:
       - Fix grammar and punctuation
       - Check formatting consistency
       - Verify keyword usage
       - Optimize headings and subheadings

    5. Final Polish:
       - Enhance readability
       - Strengthen calls-to-action
       - Improve engagement elements
       - Ensure professional presentation
    """,
    expected_output="A thoroughly polished, professional article ready for publication.",
    agent=editor
)

# create crew
crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=True
)

# st frontend
def main():
    st.title("Professional Blog Generator")
    st.markdown("""
    This AI-powered tool will generate a professional blog post based on your inputs.
    Watch the creative process unfold in real-time! 🚀
    """)

    # initialize session for storing blog post
    if 'blog_content' not in st.session_state:
        st.session_state.blog_content = None
    if 'process_status' not in st.session_state:
        st.session_state.process_status = st.empty()
    if 'search_status' not in st.session_state:
        st.session_state.search_status = st.empty()
    if 'search_results' not in st.session_state:
        st.session_state.search_results = st.empty()
    if 'agent_outputs' not in st.session_state:
        st.session_state.agent_outputs = st.empty()

    # input form
    with st.form("blog_form"):
        col1, col2 = st.columns(2)
        with col1:
            topic = st.text_input(
                "Topic",
                help="Enter the main topic of your blog post"
            )
            keywords = st.text_input(
                "Keywords (comma-separated)",
                help="Enter relevant keywords separated by commas"
            )

        with col2:
            length = st.number_input(
                "Word Count",
                min_value=300,
                max_value=5000,
                value=800,
                help="Specify the desired length of your blog post"
            )

        bullet_points = st.text_area(
            "Key Points",
            help="Enter key points to be covered in the blog post"
        )

        submitted = st.form_submit_button("Generate Blog Post ✨")

    # gen content
    if submitted:
        if not topic or not keywords or not bullet_points:
            st.error("Please fill in all the required fields!")
            return

        # tabs output and progress
        progress_tab, output_tab = st.tabs(["Generation Progress", "Final Output"])

        with progress_tab:
            # progress track
            st.subheader("🔄 Real-time Progress")
            process_container = st.container()
            research_container = st.container()
            agent_container = st.container()

            with process_container:
                status_placeholder = st.empty()
                progress_bar = st.progress(0)

            with research_container:
                st.subheader("🔍 Research Progress")
                st.session_state.search_status = st.empty()
                st.session_state.search_results = st.container()

            with agent_container:
                st.subheader("🤖 Agent Activities")
                planner_output = st.expander("Content Planner", expanded=True)
                writer_output = st.expander("Content Writer", expanded=True)
                editor_output = st.expander("Content Editor", expanded=True)

            # init input
            inputs = {
                "topic": topic,
                "keywords": [k.strip() for k in keywords.split(",")],
                "bullet_points": [p.strip() for p in bullet_points.split("\n") if p.strip()],
                "length": length
            }

            try:
                # progress bar update
                status_placeholder.markdown("### 🎯 Starting Content Generation")
                progress_bar.progress(10)

                # exec planner
                status_placeholder.markdown("### 📋 Planning Content Strategy")
                result = crew.kickoff(inputs=inputs)

                # update planner output
                planner_output.markdown("""
                #### Content Strategy
                """)
                planner_output.markdown(str(plan.output))
                progress_bar.progress(40)

                # update writer output
                status_placeholder.markdown("### ✍️ Writing Content")
                writer_output.markdown("""
                #### Initial Draft
                """)
                writer_output.markdown(str(write.output))
                progress_bar.progress(70)

                # update editor output
                status_placeholder.markdown("### 📝 Editing and Polishing")
                editor_output.markdown("""
                #### Final Edited Version
                """)
                editor_output.markdown(str(edit.output))
                progress_bar.progress(100)

                status_placeholder.markdown("### ✅ Content Generation Complete!")

                # store content in session
                st.session_state.blog_content = str(edit.output)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                return

        with output_tab:
            st.subheader("📚 Final Blog Post")

            if st.session_state.blog_content:
                try:
                    # string conv check
                    content_str = str(st.session_state.blog_content)

                    # download button
                    st.download_button(
                        label="Download Blog Post",
                        data=content_str,
                        file_name=f"blog_post_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                        mime="text/markdown"
                    )

                    # display the final blog post
                    st.markdown(content_str, unsafe_allow_html=True)

                    # display metadata
                    with st.expander("📊 Content Metadata"):
                        st.json({
                            "Topic": topic,
                            "Keywords": keywords.split(","),
                            "Word Count": length,
                            "Generation Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "Number of Key Points": len(bullet_points.split("\n")),
                            "Content Length": len(content_str)
                        })
                except Exception as e:
                    st.error(f"Error handling content: {str(e)}")


if __name__ == "__main__":
    main()