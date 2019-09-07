# pyedgeon-service
pyedgeon-service is designed to use twilio + [pyedgeon](https://github.com/abehmiel/pyedgeon) + imgur api to, in order:

1. text a twilio number some short (6-20 character) string
2. receive a sms message with twilio that routes the request to an http endpoint (in this case serving a localhost port using ngrok)
3. parse the body and metadata from that text message into a python dict using flask
4. validate the input text
5. send the input text through pyedgeon and create an optical illusion in the filesystem
6. upload the optical illusion to imgur and receive the link
7. formulate a messaging rsponse that includes a body response text and the media url
8. send the response back through the twilio webhook and route to the originating phone number
9. message appears as an optical illusion to the originating phone number

You must set up imgur API keys and a twilio account and configure their webhooks. I have this service set up with ngrok but many other options are available, 
including bypassing ngrok and imgur altogether and configuring your own web server that exposes content to the wider web (which is required for twilio MMS).

required python packages:

`pip3 install pyedgon`

`pip3 install flask`

`pip3 install imgur-python`

`pip3 install twilio`

After cloning the repository, you must set the following imgur environment variables in your system after creating an application:

`export IMGUR_ID="XXXXXXXXXXXXXXXXXXXXXXXXXXX"`

`export IMGUR_SECRET="XXXXXXXXXXXXXXXXXXXXXXXXXXX"`

[ngrok](https://dashboard.ngrok.com/get-started)

Run ngrok first and use the website it gives you as the twilio "a message comes in" webhook and connect it to the flask endpoint, like

`http://x1x2x3x4x5.ngrok.io/sms`

[imgur API](https://apidocs.imgur.com/?version=latest)

Note: you can use the anonymous API with imgur, it's a little easier in that it doesn't need refresh tokens, but you lose
the ability to post as a particular user.

[twilio](https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account)

This is essential. You can use the free tier (which only supports 1 number to receive texts from).

