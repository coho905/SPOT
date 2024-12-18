from pocketsphinx import LiveSpeech
from openai import OpenAI
import platform
import os
import subprocess
from gtts import gTTS

# TODO check if env variable already exits + input yours here if not
api_key = os.getenv('OPENAI_API_KEY', None)
if api_key == None:
    os.environ['OPENAI_API_KEY'] = 'YOUR API KEY HERE'
client = OpenAI()
print('What is your command?')
command = ""
for phrase in LiveSpeech():
        print(phrase.__str__())
        command += phrase.__str__()
        command += ' '
        #print(command)
        if 'yes' in phrase.__str__():
            break
        elif 'redo' in phrase.__str__() or 'radio' in phrase.__str__():
            command = ""
        #print(command)
real_command = command.split("yes", 1)[0].strip()
#print(c`ommand)
#real_command = command.strip()
print(real_command)
#real_command= 'view everything in my current directory'

string = 'Do you want to execute this: ' + real_command
'''speechObj = gTTS(text=string, lang='en', slow=False)
speechObj.save("naturalLang.mp3")
tryObj = gTTS(text='Did not recognize, please try again', lang='en', slow=False)
tryObj.save('tryagain.mp3')
os.system("start naturalLang.mp3")
'''
print(string)
correct1 = 0
for phrase in LiveSpeech():
    strphrase = str(phrase)
    if strphrase == 'yes':
        correct1 = 1
        break
    elif strphrase == 'no':
        correct1 = 0
        break
    #os.system("start tryagain.mp3")
    print('Do not recognize, please try again')

if correct1 == 0:
    import sys
    sys.exit("aborted")
else:
    role = "I am going to tell you what I want to do, and you are going to convert it to instructions for a "+ platform.system()+ " terminal. Return ONLY the command as a plain text string, and nothing else."
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
            {"role": "system", "content": role},
            {
                "role": "user",
                "content": real_command
            }
        ]
    )
    
    #print('Command: ' + completion.choices[0].message.content)
    string2 = 'Do you want to execute this: ' + completion.choices[0].message.content
    print(string2)
    '''
    openAiObj = gTTS(text=string2, lang='en', slow=False)
    openAiObj.save("openAi.mp3")
    os.system("start openAi.mp3")
    '''
    user = 0
    for phrase in LiveSpeech():
        strphrase = str(phrase)
        if 'yes' in strphrase:
            user = 1
            break
        elif 'no' in strphrase:
            user = 0
            break
        #os.system("start tryagain.mp3")
        print('Do not recognize, please try again')
    if user == 1:
        result = subprocess.run(completion.choices[0].message.content.split(" "), capture_output=True, text=True, shell=True)
        print(result.stdout)
        # TODO write errors to error file?
    print('executed')

#print('done')
