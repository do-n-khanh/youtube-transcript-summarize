# YouTube Transcript Summarizer

A Python web application built with [Streamlit](https://streamlit.io/), [LangChain](https://python.langchain.com/), and [Ollama](https://ollama.com/) to summarize YouTube video transcripts in real-time. Users can input a YouTube video URL, and the app fetches the transcript using [SearchAPI.io](https://www.searchapi.io/), then generates a concise summary using the Deepscaler model, streaming the output as it’s created.

## Features
- **Interactive UI**: Enter a YouTube URL and API key via a simple Streamlit interface.
- **Real-Time Summarization**: Watch the summary generate token-by-token as the LLM processes the transcript.
- **Error Handling**: User-friendly messages for invalid URLs, missing transcripts, or API issues.
- **Powered by AI**: Uses LangChain and the Deepscaler model (via Ollama) for efficient summarization.

## Demo
![image](https://github.com/user-attachments/assets/7cf9bfe0-b3e1-411d-aab6-b37deec974ac)


## Prerequisites
- **Python 3.8+**
- **Ollama**: Installed and running locally with the Deepscaler model.
- **SearchAPI.io API Key**: Required to fetch YouTube transcripts.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/youtube-transcript-summarizer.git
   cd youtube-transcript-summarizer

2. **Install Dependencies**:
```bash

pip install -r requirements.txt

3. **Set Up Ollama**:

    Install Ollama: Follow instructions at ollama.com.
    Start the Ollama server:
    bash

ollama serve

Pull the Deepscaler model:
bash

        ollama pull deepscaler

    Get a SearchAPI.io API Key:
        Sign up at searchapi.io.
        Copy your API key for use in the app.

4. **Usage**

    Run the App:
    bash

streamlit run app.py

This opens the app in your browser at http://localhost:8501.
Interact with the App:

    YouTube Video URL: Enter a valid URL (e.g., https://www.youtube.com/watch?v=dQw4w9WgXcQ).
    SearchAPI.io API Key: Paste your API key.
    Click Summarize to fetch the transcript and see the summary stream in real-time.

Example:

    Input: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    Output: A summary of the video’s lyrics or spoken content (if transcripts are available).
