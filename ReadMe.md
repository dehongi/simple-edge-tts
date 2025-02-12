# Simple Edge TTS

A Python example for Microsoft Edge's Text-to-Speech service using `edge-tts`. This project provides an easy-to-use interface for converting text to speech with support for multiple languages and voices.

## Features

- Convert text to speech using Microsoft Edge's TTS engine
- Support for multiple languages and voices
- List all available voices and languages
- Asynchronous and synchronous interfaces
- Simple and straightforward API

## Installation

1. Ensure you have Python 3.7 or later installed
2. Install the required package:


## Usage

### Basic Text-to-Speech Conversion


## Available Functions

- `convert_text_to_speech(text, output_file="output.mp3", voice="en-US-ChristopherNeural")`: 
  Convert text to speech with specified parameters
- `get_voices()`: 
  Get a list of all available voices
- `print_available_voices()`: 
  Display all available voices grouped by language

## Voice Selection

The default voice is "en-US-ChristopherNeural", but you can choose from many other voices. Use `print_available_voices()` to see all available options.

Example voices:
- en-US-ChristopherNeural (Male, US English)
- en-GB-SoniaNeural (Female, British English)
- es-ES-AlvaroNeural (Male, Spanish)
- fr-FR-DeniseNeural (Female, French)

## Requirements

- Python 3.7+
- edge-tts

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## Acknowledgments

This project uses the `edge-tts` package to interact with Microsoft Edge's Text-to-Speech service.