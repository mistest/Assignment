# Requirements
Design a command line tool that will allow the user to query the merriam-webster dictionary and receive a formatted response with the word definition.
https://dictionaryapi.com/products/api-collegiate-dictionary

# Command Line Tool
This is a simple python CLI tool that will return some information from a public API service.

### HOW TO USE THIS TOOL
PreRequistes:
```bash
 Python 3.11
 Windows or Unix Machine
 API to be used once you register in https://dictionaryapi.com
```
Usage:
```bash
git clone https://github.com/mistest/Assignment.git
set API_KEY=XXXX-XXXX-XXXX-XXXX  (Use export in Linux Instead and value should used as Secret/Masked if needs to be used in Pipelines)
pip install -r requirements.txt
python app.py <Word to be Queried>
eg:
    python app.py exercise
    Argument List: exercise
    INFO:root:Connecting to Merriam-Webster Dictionary
    INFO:root:Connection successful to MW
    Result of exercise in Merriam-Webster Dictionary is:  the act of putting into use, action, or practice
```