# Import libraries
import streamlit as st  # Streamlit library for creating web apps
from gtts import gTTS  # Google Text-to-Speech library for converting text to speech
import os  # Operating system interface for file operations

# Function to convert text to speech using Google Text-to-Speech
def text_to_speech(text, language='en'):
    # Create a gTTS (Google Text-to-Speech) object with the given text and language
    tts = gTTS(text=text, lang=language, slow=False)
    return tts  # Return the gTTS object

# Main function for the Streamlit web app
def main():
    # Set the title of the web app
    st.title("Text-to-Speech with Streamlit")

    # Create a text area for user input
    text_input = st.text_area("Enter text for speech synthesis")

    # Create a dropdown menu for selecting the language
    language = st.selectbox("Select language", ["en", "es", "fr", "de"])

    # Create a button for converting text to speech
    if st.button("Convert to Speech"):
        if text_input:
            # Convert the user input text to speech using the specified language
            tts = text_to_speech(text_input, language)

            # Save the speech as an audio file (output.mp3)
            audio_file_path = "output.mp3"
            tts.save(audio_file_path)

            # Play the generated audio file in the web app
            st.audio(audio_file_path, format="audio/mp3", start_time=0)

            # Remove the audio file after displaying the download link
            os.remove(audio_file_path)
        else:
            # Display a warning if no text is entered before attempting conversion
            st.warning("Please enter text before converting to speech.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
