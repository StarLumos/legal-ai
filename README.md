# Legal AI
## A brief introduction
Legal AI is a program based on Python, JavaScript, and HTML that uses an API linking Open AI's ChatGPT. In short, the program takes an input (particularly a long, complicated legal document) and outputs the summary of the document, saving the user the time and effort of a futile attempt to read and understand the document. 

## Installation
Clone this repository 
```
git clone git@github.com:StarLumos/legal_ai.git
```
cd into the directory
```
cd legal_ai
```
Create a Python virtual environment
```
python -m venv venv
```
Activate the Python virtual environment

*For Windows*
```
.\venv\Scripts\activate
```
*For Unix*
```
source venv/bin/activate
```
Add your OpenAI API key to a `.env` file inside `src/backend/`
```
api=YOURAPIKEY
```
Install dependencies
```
pip install -r requirements.txt
```
Run the Python server
```
cd src/backend/
python main.py
```
Finally, spin up the client frontend with a web server of your choosing. (i.e. [live server VS Code extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer))
