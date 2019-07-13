# Assist-Home
controlling home appliances using google assistant

## What we need
  - Node Mcu x 1
  - 2 channel relay board x 1
  - Blynk app for mobile
  - IFTTT app for mobile
  - Arduino IDE
  
## Library
  ESP8266WiFi.h
  
## How does It Work
So in this project we have 4 parts:
  - Hardware
  - Blynk App
  - IFTTT
  - Google Assistant

For Hardware side we have the configuration as below

<img src="https://github.com/udaysolanki4/Assist-Home/blob/master/assisthome.JPG" height="400" align="left" /> 

So as shown above we are connecting relay 1 to pin D0 and relay 2 to pin D1. On the other side I'm connecting it with battery and source.
You can assume the battery as the ac source with 2 wires phase and neutral. And red led as the bulb of your room and blue led represent the fan of the room. So we are connecting the source with the led in series and then connecting them to Common(com) and Normally closed(NO) of the relay board.

Moving ahed we gonna use the assist home.ino code paste it in the arduino Ide and then go and download the blynk app. Blynk is a cloud platform which provide the ease of use to the user. We doesn't need to code for any thing all controlling is taken care by app where we can configure our operation. So now we go to app as easy sign up we used to go for new project. Select the name of the project then add the device You are using. Then choose your connectivity i choose for wifi. Moving ahead and create project. At first it will send the authentication to your email id copy that and past it to your ino code file. Then go for upload the code do not forget to change your network configuration change ssid and pass according to your hotspot. Moving ahead we need to add some widget box to our dashboard of blynk app. As shown below-

<img src="https://github.com/udaysolanki4/Assist-Home/blob/master/assist/Screenshot3.png" height="400" align="left" />
<img src="https://github.com/udaysolanki4/Assist-Home/blob/master/assist/Screenshot39.png" height="400" align="centre" />
<img src="https://github.com/udaysolanki4/Assist-Home/blob/master/assist/Screenshot1.png" height="400" align="centre" />

Now download the IFTTT app signin withe the same id what you are using in your mobile device. Now create applet in IFTTT with google assistant and webhook. Add the necessary config and add url in webhook http://cloud.blynk.cc:8080/XXXX your TOKEN XXXX/pin/ZZZ and replace XXXX your TOKEN XXXX with your actual token and ZZZ with the PIN number , for Digital PIN use DX like D1, D5 etc. and for Virtual PIN use VX like V1 ,V5 etc. As shown Below

<img src="https://github.com/udaysolanki4/Assist-Home/blob/master/assist/Screenshot05.png" height="400" align="left" />
<img src="https://github.com/udaysolanki4/Assist-Home/blob/master/assist/Screenshot7.png" height="400" align="centre" />
<img src="https://github.com/udaysolanki4/Assist-Home/blob/master/assist/Screenshot09.png" height="400" align="centre" />

Thank You. Go Ahead and Keep Experimenting.
