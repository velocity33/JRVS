import speech_recognition as sr 
from TTS import TTS


class STT: 

    
    r = sr.Recognizer()    # Set up the recognizer and microphone
    mic = sr.Microphone()

    

    def recognize_speech(a):
        x = a
        while(x):
            with STT.mic as source:
                STT.r.adjust_for_ambient_noise(source)
                # STT.r.dynamic_energy_threshold = False
                # STT.r.energy_threshold = 400
                print("Scanning Voice")
                audio = STT.r.listen(source)
                text = ""
                try: 
                        # Adjust the ambient noise threshold dynamically
                        
                
                        # Listen for speech and convert it to text
                        
                        text = STT.r.recognize_google(audio)
                        print("Machine Interpretation: " + str(text))
                except sr.UnknownValueError:
                        TTS.tts("Could not understand audio")
                        continue
            return text.lower()
            
        
   