# AddressingHomesFlaskRewrite
## Clone Repo with

```
git clone https://github.com/nishchaysinha/AddressingHomesFlaskRewrite.git
```
## Start the flask server

```
pip3 install -r requirements.txt
cd AddressingHomesFlaskRewrite
python3 app.py
```

## Ensure you have Firefox or Chrome is installed if using Linux or MacOS
### Ensure [Geckodriver](https://github.com/mozilla/geckodriver/releases "Geckodriver") is installed if Tor or Firefox is being used

### If using chrome(on windows or linux), please install the [Chromedriver](https://chromedriver.chromium.org/downloads "Chromedriver")

## Place All Drivers in the drivers folder

# Working

```
-The python scripts for the reverse geocoder have been kept as separate modules which can be imported into any project
-The python scripts contain a single function which require only two parameters(Latitude and Longitude)

I've currently used a flask backend for this demo to make it easier for me to setup
But I researched various ways in which this could be used along with Angular
One way is to leave this as a backend service on another port and make it completely server sided
```
