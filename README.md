# WaterReminder_Discord_Bot
## Environment
### Setup
- Python (3.10+)
- A Discord Bot (with a bot token)
- [Optional] Ruff

### Python Venv and Packages
1. Clone this repo and create venv.
2. Install required packages.

``` bash
pip install -r requirements.txt
```
### Create Your Own File from the Example

```bash
cp config.example.json config.json
cp token.example.env token.env
```

> Please use `copy` instead of `cp` if your computer is Windows.

> These 2 files are (and should remain) in `.gitignore`, so they won't be pushed to remote repo.

> After copying, open both files and fill in the required information.

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
5. Go to **UptimeRobot**: create an **HTTP / website monitoring** check and enter the bot's Render URL.


