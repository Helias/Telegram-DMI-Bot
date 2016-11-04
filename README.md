# Telegram-DMI-Bot

**Telegram-DMI-Bot** is the platform that powers **@DMI_bot**, a Telegram bot aided at helping students find informations about professors, classes' schedules, administration's office hours and more.

###Setting up a local istance
If you want to test the bot by creating your personal istance, follow this steps:
* **Clone this repository** or download it as zip.
* **Copy config/token.conf.dist into "token.conf" and write your telegram bot token here.** (If you don't have a token, message Telegram's @BotFather to create a bot and get a token for it)
* **Send a message to your bot** on Telegram, even '/start' will do. If you don't, you could get an error.
* If your system supports bash shell scripting, **launch "restarter.sh"**. Alternatively, you can launch "telegrambot.py" with your Python interpreter, even if doing so will not restart the bot in the event of a crash.

For the bot istance to be executed, your system needs:

- Python 2
- python-pip
- python-bs4
- python-beautifulsoup

install with *pip*
- python-telegram-bot
- pydrive

###Using the live version
The bot is live on Telegram with the username [@DMI_Bot](https://telegram.me/DMI_Bot).
Send **'/start'** to start it, **'/help'** to see a list of commands.

Please note that the commands and their answers are in Italian.

###License
This open-source software is published under the GNU General Public License (GNU GPL) version 3. Please refer to the "LICENSE" file of this project for the full text.

###Credits
This project is made possible thanks to the contributions of [Stefano Borzì](https://github.com/Helias), [Adriano Ferraguto](https://github.com/adrianoferraguto),[Vincenzo Filetti](https://github.com/veeenz) and [Simone Di Mauro](https://github.com/simone989).
