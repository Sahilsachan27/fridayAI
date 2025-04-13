# FridayAI: Functional Responsive Intelligent Digital Assistant for You
FridayAI is a personal AI assistant designed to provide a seamless user experience. Built with Python, Eel, and the DeepSeek R1 Distill Llama 70B model, FridayAI can handle both local commands and interact with users via a chatbot interface. It features a futuristic web UI, speech recognition, text-to-speech, and more.

## Features

- **Voice Recognition**: Capture and execute voice commands.
- **Text-to-Speech**: Get voice responses from the assistant.
- **Local Commands**: Open applications like Notepad, search the web, and check the time.
- **Chatbot Integration**: Powered by the DeepSeek R1 Distill Llama 70B model for intelligent text responses.
- **Web Interface**: A futuristic interface with animations built using Eel, HTML, CSS, and JavaScript.
- **Siri-Style Wave Animations**: Adds an interactive experience with smooth animations.

## Installation

### Prerequisites

Make sure you have the following installed on your system:

- **Python 3.x**
- **Git** (optional for cloning the repo)

### Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/Sahilsachan27/fridayAI.git
   cd fridayAI
   
2. Install dependencies:
pip install -r requirements.txt

If requirements.txt is not available, install these manually:

pip install eel pyttsx3 speech_recognition playsound

3. Run the assistant:

python friday.py
This will open the web interface in your default browser.

# How it Works
# Backend: FridayAI is powered by Python and uses eel for frontend-backend integration. It listens for voice commands using the speech_recognition library and responds using the pyttsx3 text-to-speech engine.

# Frontend: The assistant's web interface is styled with HTML5, CSS, and JavaScript, featuring smooth animations using SiriWave.js and other libraries.

# Chatbot: The assistant uses the DeepSeek R1 Distill Llama 70B model for intelligent text-based chatbot interactions.

# Contributing
Feel free to fork the repository and create a pull request if you'd like to contribute. Any help is appreciated!

# License
This project is open-source and available under the MIT License.
