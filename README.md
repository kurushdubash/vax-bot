# vax-bot
A simple vax bot that texts you with a link to sign up when CVS, MyTurn, or Walgreens has an appointment available

Needs the following environment variables to work:

```
export EMAIL_ADDRESS="###" # Your Gmail 

export GMAIL_APP_PASS="###" # Gmail App Specific Password https://support.google.com/accounts/answer/185833?hl=en


export GMAPS_KEY="###" # Google Maps API Key https://developers.google.com/maps/documentation/javascript/get-api-key
```

To run bot on server, do:

```
nohup python3 -u server.py > app.log &
```

which will save output to app.log.

