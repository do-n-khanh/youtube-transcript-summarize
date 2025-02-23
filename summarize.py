import streamlit as st
import requests
import json
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Function to extract video ID from YouTube URL
def extract_video_id(url):
    """
    Extracts the video ID from a YouTube URL.
    Supports formats like: https://www.youtube.com/watch?v=VIDEO_ID or https://youtu.be/VIDEO_ID
    """
    if "youtube.com/watch?v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        raise ValueError("Invalid YouTube URL format")

# Function to get YouTube video transcript
def get_transcript(video_id, api_key):
    url = "https://www.searchapi.io/api/v1/search"
    params = {
        "engine": "youtube_transcripts",
        "video_id": video_id,
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    if "transcripts" not in data:
        raise ValueError("No transcripts found for this video")
    return " ".join([t["text"] for t in data["transcripts"]])  # Combine transcript segments

# Function to summarize transcript with real-time streaming
def summarize_transcript(transcript, output_placeholder):
    """
    Summarizes a transcript and streams the result in real-time to a Streamlit placeholder.
    
    Args:
        transcript (str): The text of the transcript to summarize.
        output_placeholder: Streamlit placeholder to display the streaming output.
    """
    llm = OllamaLLM(model="deepscaler", temperature=0.1)
    prompt_template = PromptTemplate(
        input_variables=["transcript"],
        template="""
        You are an expert summarizer. Provide a concise and accurate summary of the following transcript in your own words. Focus on the main points and key ideas, avoiding unnecessary details:
        
        Transcript: {transcript}
        
        Summary:
        """
    )
    chain = prompt_template | llm
    
    # Stream the output to the placeholder
    output_placeholder.write("Generating summary...")
    summary_text = ""
    for chunk in chain.stream({"transcript": transcript}):
        summary_text += chunk
        output_placeholder.write(summary_text)  # Update the placeholder with each chunk

# Streamlit app
def main():
    st.title("YouTube Video Transcript Summarizer")
    st.write("Enter a YouTube video URL to get a summary of its transcript.")

    # Input for YouTube URL
    youtube_url = st.text_input("YouTube Video URL", placeholder="e.g., https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    # Placeholder for API key (replace with your actual key or use an environment variable)
    api_key = st.text_input("SearchAPI.io API Key", type="password", placeholder="Enter your API key")

    # Button to trigger summarization
    if st.button("Summarize"):
        if not youtube_url or not api_key:
            st.error("Please provide both a YouTube URL and an API key.")
        else:
            try:
                # Extract video ID and get transcript
                video_id = extract_video_id(youtube_url)
                with st.spinner("Fetching transcript..."):
                    transcript = get_transcript(video_id, api_key)
                
                # Display transcript length for reference
                st.write(f"Transcript length: {len(transcript)} characters")
                
                # Placeholder for real-time summary output
                output_placeholder = st.empty()
                
                # Generate and stream the summary
                summarize_transcript(transcript, output_placeholder)
                
                st.success("Summary complete!")
            
            except ValueError as e:
                st.error(str(e))
            except requests.RequestException as e:
                st.error(f"Error fetching transcript: {str(e)}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
