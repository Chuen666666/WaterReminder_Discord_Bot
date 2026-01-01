# WaterReminder_Discord_Bot
## Environment
### Setup
- Python (3.10+)
- A Discord Bot (with a bot token)
### Python Venv and Packages
1. Clone this repo and create venv.
2. Install required packages.
``` bash
pip install -r requirements.txt
```
### Change Files' Name
|Old Name|New Name|Content|
|:-:|:-:|:-:|
|`config_example.py`|`config.py`|Paste your information|
|`token_example.py`|`token.py`|Paste your bot token|
> These 2 files are (and should remain) in `.gitignore`, so they won't be pushed to remote repo.
### Run Bot
Run the bot in venv, using the following command (or run `main.py` in any other ways):

``` bash
python main.py

```

If the bot runs on the Render environment, it will automatically stay online. The setup for Render and UptimeRobot is as follows:

1. Create a **Web Service**.
2. Select the bot's GitHub repository (you can fork this repo first).
3. Fill in the following settings:

   - **Runtime**: `Python3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
   - **Environment Variables**: Add a variable named `TOKEN` and set its value to your Discord Bot Token.
   - **Advanced**

     - **Secret Files**: Set `Filename` to `config.json` and paste the contents of that JSON file into `File Contents`.
     - **Health Check Path**: `/` (default is `/healthz`)
4. Finally, click **Deploy Web Service**.
5. After deployment, go to **Settings &rarr; Health Checks &rarr; Health Check Path** and change it to `/` (the default should be `healthz`).
6. Go to **UptimeRobot**: create an **HTTP / website monitoring** check and enter the bot's Render URL.