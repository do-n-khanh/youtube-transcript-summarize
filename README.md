# YouTube Transcript Summarizer

A Python web application built with [Streamlit](https://streamlit.io/), [LangChain](https://python.langchain.com/), and [Ollama](https://ollama.com/) to summarize YouTube video transcripts in real-time. Users can input a YouTube video URL, and the app fetches the transcript using [SearchAPI.io](https://www.searchapi.io/), then generates a concise summary using the Deepscaler model, streaming the output as it’s created.

## Features
- **Interactive UI**: Enter a YouTube URL and API key via a simple Streamlit interface.
- **Real-Time Summarization**: Watch the summary generate token-by-token as the LLM processes the transcript.
- **Error Handling**: User-friendly messages for invalid URLs, missing transcripts, or API issues.
- **Powered by AI**: Uses LangChain and the Deepscaler model (via Ollama) for efficient summarization.

## Demo
*(Add a GIF or screenshot here if you deploy the app and capture its output!)*

## Prerequisites
- **Python 3.8+**
- **Ollama**: Installed and running locally with the Deepscaler model.
- **SearchAPI.io API Key**: Required to fetch YouTube transcripts.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/youtube-transcript-summarizer.git
   cd youtube-transcript-summarizer
