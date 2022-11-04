# Line Bot

## Resources
- Line Developers
- Line Official Account Manager
- heroku


### Line Developers
- https://developers.line.biz/console/profile
- This is the console to manage the function of line developer tools.
- the channel to send messages or have a bot function can be created in this tool.
- this has a lot of documents about Line development, such as Messaging API


### Line Official Account manager
- Messaging API can be activated in this page.

### Heroku
- free server
- by using git hub student pack, I can use it by free.
- it have a function that can fire the event when I want to do.

## how to implement Line bot
1. create line channel by the line Developers
2. if it is needed, Messenger API should be valid.
3. add the channel to friend on Line.
4. coding
5. create Heroku account 
6. 


## about coding
- using module of "line-bot-sdk"
    - to understand the detail, refering to the documnt.
- broadcast method is used in this case.
    - this can send message to many people who added the channel to their friend list.
- on the other hand, there is a method that can send message ont to one.
- if I want to send message to each user, it needs userid. I couldn't get the userid thouch, because it requires the premium account of Line Developer.

## about heroku deploy
- to run the python script at heroku, these files should be created under the same location of app.
    - requirements.txt :libraries
    - runtime.txt :python version

    - ex. requirements.txt
        ```
        line-bot-sdk==2.3.0
        python-dotenv==0.21.0
        ```

    - runtime.txt
        ```
        python-3.10.7
        ```

- these steps should be made
    1. install heroku cli
    ```
    brew tap heroku/brew && brew install heroku
    ```

    2. login to heroku
    ```
    heroku login
    ```

    3. go folder where app is locted.
    4. create heroku app
    ```
    heroku create appname
    ```

    5. config line channel access token
    ```
    heroku config:add ACCESS_TOKEN=token
    ```
    6. deploy
    ```
    git push heroku main
    ```

    if the config time-shceduling is be set, you should
    ```
    heroku addons:add scheduler:standard
    ```

    and setting in the heroku page.