
# Mini Chat-Bot Application

## Introduction
The Mini Chat-Bot Application is a web-based tool built with **Streamlit** and **OpenAI's GPT API**. It allows users to easily summarize text from **PDF files** and **YouTube video transcripts**. With a user-friendly interface, this application makes it possible to extract key insights from lengthy documents and videos, saving time and effort.

## Objective
The main objective of this project is to provide users with an **efficient way to extract and understand key information** from long documents or video transcripts. By offering a fast summarization process, the application helps users grasp the essential content without having to go through all the details manually.

## Design
The project follows a modular design to ensure smooth interaction between the user and the summarization functionalities:
- **User Input**: Users can either upload a PDF file or enter a YouTube video link for summarization.
- **Processing**:
  - **PDF Handling**: Extracts text from uploaded PDF files using `PyMuPDF`.
  - **YouTube Transcript Handling**: Retrieves video transcripts using the `youtube-transcript-api`.
- **OpenAI API Integration**: The extracted text or transcripts are sent to the OpenAI GPT model for summarization.
- **Streamlit Interface**: Displays the summarized content back to the user through a simple and intuitive web interface.

## Implementation
To set up and run the project, follow these steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repository/mini-chatbot
   cd mini-chatbot
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install streamlit openai PyMuPDF youtube-transcript-api python-dotenv
   ```

4. **Configure API Key**:
   - Create a `.env` file in the project directory and add your OpenAI API key:
     ```
     OPENAI_API_KEY=sk-your-api-key
     ```
    - The code for the python is found in the chatbot.py

5. **Run the Application**:
   ```bash
   streamlit run chatbot.py
   ```

6. **Usage**:
   - Upload a PDF file or paste a YouTube link to summarize the content.
   - The summarized text will be displayed directly in the Streamlit interface.

## Testing
To ensure the functionality of the application, the following tests were conducted:
- **Functional Testing**: Verified that the application correctly processes PDFs and YouTube links, extracting and summarizing content.
- **Edge Case Testing**: Tested with large PDFs and videos with no transcripts to ensure appropriate error handling.
- **User Interface Testing**: Ensured the file upload and input fields work as expected and that the summarized output is displayed properly.
- **API Rate Limiting**: Checked that the application remains within OpenAI's API usage limits to prevent service interruptions.

## Future Enhancements
- Support for more file types, such as DOCX and TXT.
- Batch processing for multiple PDF files or YouTube videos.
- Options for different summarization lengths and customization based on user needs.

