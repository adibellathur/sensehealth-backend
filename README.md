# Sense Health Backend
### Backend for Company 3's HackForHope Project

**Authors:** Ankur Karwal, Gavin Bains, Andrew Ki, Willhelm Willie, Connor Chyung, Janeline Wong, Zach Sullens, Glory Kanes, Adithya Bellathur

## Installation Instructions
1. Create VirtualEnv for python. Detailed Instructions found here: https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/. Simple instructions for OSX are as follows:
```
pip3 install virtualenv # install virtualenv
virtualenv -p python3 ~/venv/sensehealth_env  # create virtualenv of python3 in your ~/venv directory
source ~/venv/sensehealth_env/bin/activate  # activate your virtualenv
```
2. clone repo to computer
3. once inside the repo, activate your virtualenv as shown above (just the last line).
4. run `pip install -r requirements.txt`. This will pip install the necessary packages to your virtualenv

## Run the server locally for development
run `python app.py`, and go to `http://127.0.0.1:5000/` to see the changes.

## Setting Up Heroku
1. install heroku. instructions can be found here: https://devcenter.heroku.com/articles/heroku-cli
2. use `heroku login` to log into your heroku account on the cmd line
3. run `heroku git:remote -a sensehealth-backend` to add heroku as a remote repository you can push to. This will let you push to the heroku once you have made changes. You need access so contact Adithya to give that to you.
4. Once you have successfully made changes and pushed to master, you run `git push heroku master` to have those changes reflected on the heroku server. All changes should show on `https://sensehealth-backend.herokuapp.com/`
