# Facebook Comment Bot 🤖
![Architecture Diagram](architecture/architecture.png)

## Installation
### 1. Clone github repo
```
https://github.com/lintosunny/facebook-comment-bot.git
```

### 2. Set up virtual environment
```
python<vesrion> -m venv <virtual-env-name>
```

### 3. Activate virtual environment
```
.\<virtual-env-name>\Scripts\Activate
```

### 4. Install dependencies
```
pip install -r requirements.txt
```

### 5. Set up environment variables
Create ```.env``` file in the root folder and add your facebook and gemini api credentials:
```
FACEBOOK_ACCESS_TOKEN = <your-facebook-access-token>
GEMINI_API_KEY = <your-gemini-api-key>
PAGE_ID = <your-facebook-page-id>
```

### 6. Update artifacts
Update the date in ```./artifacts/last_updated.json```. If you want to reply comments posted from yesterday, change date to yesterday's.
After a successful run, the system will automatically update the date to the current timestamp. Ensure the datetime format remains as ```YYYY-MM-DDTHH:MM:SS+0000```
```
{"last_updated_str": "<your-desired-datetime>"}
```

### 7. Update prompt
Update the prompt in ```./src/config/prompt.yaml``` as per your use case.
```
prompt_template: |
 <your-prompt>
```

### 8. Run locally
Run the script on your command prompt
```
python main.py
```