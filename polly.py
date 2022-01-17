from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

def speak(phrase, voice):
    # Create a client using the credentials and region defined in the [adminuser]
    # section of the AWS credentials file (~/.aws/credentials).
    session = Session(profile_name="pollyuser")
    polly = session.client("polly")

    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Text=phrase, 
                                            OutputFormat="mp3",
                                            VoiceId=voice)
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    # Access the audio stream from the response
    if "AudioStream" in response:
        # Note: Closing the stream is important because the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
        with closing(response["AudioStream"]) as stream:
            output = os.path.join(gettempdir(), "speech.mp3")

            try:
                # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)

    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

    # Play the audio using the platform's default player
    if sys.platform == "win32":
        os.startfile(output)
    else:
        #os.system("nvlc {}".format(output))
        # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, output])

if __name__ == "__main__":
    #  [Nicole, Kevin, Enrique, Tatyana, Russell, Olivia, Lotte, Geraint, Carmen, Ayanda, Mads, Penelope, Mia, Joanna, Matthew, Brian, Seoyeon, Ruben, Ricardo, Maxim, Lea, Giorgio, Carla, Aria, Naja, Maja, Astrid, Ivy, Kimberly, Chantal, Amy, Vicki, Marlene, Ewa, Conchita, Camila, Karl, Zeina, Miguel, Mathieu, Justin, Lucia, Jacek, Bianca, Takumi, Ines, Gwyneth, Cristiano, Mizuki, Celine, Zhiyu, Jan, Liv, Joey, Raveena, Filiz, Dora, Salli, Aditi, Vitoria, Emma, Lupe, Hans, Kendra, Gabrielle]
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    speak("Hello, the current time is {}".format(current_time),"Joanna")