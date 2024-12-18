# SPOT
## SPeech tO Terminal (SPOT)
**Speak commands directly to your terminal**
<br />~~Remembering hundreds of terminal commands on various operating systems~~ -> Use natural language (and your voice) to execute command line instructions!

## How To Set Up
1. ```bash
   pip install -r requirements.txt```
2. Get an OpenAI API key (and plug it in): <=$5 for a years amount the last I checked
3. ```bash
   python[3] main.py
   ```
## Usage
1. After initial prompt, speak your command (the system will find an available microphone if it exists). Alternatively type it after update 1
2. Say 'yes' to confirm you are done speaking (stop word). Say 'radio' or 'redo' to reset the current command and restate it.
3. After that, you will be asked to confirm whether or not you want to send the request to the OpenAI api.
4. Then, the system display the received bash command asking if you would like it to be executed on your system (the result will be correct based on OS automatically - no need to specify)
5. Lastly, the results from the execution will be displayed

## Updates
1. Allow for text inputs instead of just voice
2. Customize reset and stop words
3. Look into huggingface API calls (free) instead of OpenAI (~$5 a year)
4. Allow for speaking instructions instead of typing
5. Enable forced execution
6. Make an option for an infinite loop (until final ending word)

### Motivation
Saw Jensen Huang say English is the future programming language, so I thought it would be cool to enable speaking directly to your machine as though it is a person. Additionally, this could help those who are unfamiliar and want to learn shell commands, those who have conditions rendering it difficult/impossible to type, and the visually impaired (see update 4). Would love any help on it

MIT License. Copyright - Colin Wolfe, 2024
