import streamlit as st
import openai
import fitz  # PyMuPDF
from urllib.parse import urlparse
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Mini Chat-Bot")
st.write("Upload a PDF file or enter a YouTube video link to summarize the content.")

# Upload PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
st.markdown("Or enter a YouTube video link below:")
raw_transcript = st.text_input("YouTube Video Link")

# Store messages in session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Process YouTube video transcript
if raw_transcript:
    parsed_url = urlparse(raw_transcript)
    video_id = parsed_url.query.split("=")[1]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([content["text"] for content in transcript])
        st.session_state.messages.append({"role": "system", "content": transcript_text})

        if st.button("Summarize Video"):
            summarized_video = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
                messages=[
                    {"role": "user", "content": f"Summarize the following video transcript: {transcript_text}"}
                ]
            )
            summary = summarized_video.choices[0].message["content"]
            st.write("Video Summary:")
            st.markdown(summary)

    except Exception as e:
        st.error(f"Error fetching transcript: {e}")

# Process PDF file
if uploaded_file:
    try:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        pdf_text = ""
        for page in doc:
            pdf_text += page.get_text()
        doc.close()

        st.session_state.messages.append({"role": "system", "content": pdf_text})

        if st.button("Summarize PDF"):
            summarized_text = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
                messages=[
                    {"role": "user", "content": f"Summarize the following PDF content: {pdf_text}"}
                ]
            )
            summary = summarized_text.choices[0].message["content"]
            st.write("PDF Summary:")
            st.markdown(summary)

    except Exception as e:
        st.error(f"Error processing PDF: {e}")

# Display chat history
for message in st.session_state.messages:
    if message["role"] != "system":
        st.markdown(f"**{message['role'].capitalize()}:** {message['content']}")

# Handle user input for chat
if prompt := st.chat_input("Enter message here"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[
                {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
            ]
        )
        answer = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.write("Assistant Response:")
        st.markdown(answer)
    except Exception as e:
        st.error(f"Error: {e}")
