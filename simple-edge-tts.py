# A simple Python module for converting Text to Speech using edge-tts

import asyncio
import edge_tts


async def text_to_speech(
    text, output_file="output.mp3", voice="en-US-ChristopherNeural"
):
    """
    Convert text to speech using Microsoft Edge TTS

    Args:
        text (str): The text to convert to speech
        output_file (str): The output audio file path (default: output.mp3)
        voice (str): The voice to use (default: en-US-ChristopherNeural)
    """
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)


def convert_text_to_speech(
    text, output_file="output.mp3", voice="en-US-ChristopherNeural"
):
    """
    Synchronous wrapper for text_to_speech function
    """
    asyncio.run(text_to_speech(text, output_file, voice))


async def list_voices():
    """
    Get a list of all available voices from Edge TTS

    Returns:
        list: List of dictionaries containing voice information
    """
    voices = await edge_tts.VoicesManager.create()
    return voices.voices


def get_voices():
    """
    Synchronous wrapper for list_voices function

    Returns:
        list: List of dictionaries containing voice information
    """
    return asyncio.run(list_voices())


def print_available_voices():
    """
    Print all available voices grouped by language
    """
    voices = get_voices()
    languages = {}

    # Group voices by language
    for voice in voices:
        lang = voice["Locale"]
        if lang not in languages:
            languages[lang] = []
        languages[lang].append(voice["ShortName"])

    # Print voices grouped by language
    for lang, voice_list in sorted(languages.items()):
        print(f"\n{lang}:")
        for voice in sorted(voice_list):
            print(f"  - {voice}")


if __name__ == "__main__":
    # Example usage
    print("Available voices:")
    print_available_voices()

    # Original example
    sample_text = "Hello! This is a test of the text to speech conversion."
    convert_text_to_speech(sample_text)
