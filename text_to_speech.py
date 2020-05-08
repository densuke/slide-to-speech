from google.cloud import texttospeech


def convert(text, output_filename):
    print(f"tts: '{text}'")

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(ssml=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='ja-JP',
        name='ja-JP-Wavenet-B',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open(output_filename, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print(f'Audio content written to file {output_filename}')


# main
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="音声変換したい内容が入ったテキスト(SSML)")
    parser.add_argument("output", help="出力ファイル名(存在していたら上書きします)")
    args = parser.parse_args()

    with open(args.text, "r") as f:
        text = f.read()
        convert(text, args.output)
