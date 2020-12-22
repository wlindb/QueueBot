# QUEUE BOT
Bot to automate the process of queueing at [KTH lab queue](https://queue.csc.kth.se)

## How to Install the bot 
- Install the [chrome driver](https://chromedriver.chromium.org/downloads) for your version of chrome 
- Create the file secrets.py 
    ```python
    username = '<KTH_username_here>'
    pw = '<KTH_password_here>'
    ```
- Run 
    ```
    $ pip install selenium
    ```
## How to run the bot
- Run
    ```
    $ python main.py <course_id> <your_location> <comment> <1 if you want to prensent 0 otherwise>
    ```
Note that the course id is case sensitive and has to match the actual name of the course on https://queue.csc.kth.se/Queue/<course_id>.