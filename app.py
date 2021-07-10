import numpy as np
from flask import Flask, request, jsonify, render_template,abort
from joblib import load
import requests
from training import prediction
from sendemail import sendmail
import smtplib


model= load('smartagriculture.save')


app = Flask(__name__)
@app.route('/')
def homepagea():
    return render_template('homepage.html')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')



@app.route('/cropprediction')
def cropprediction():
    return render_template('cropprediction.html')



@app.route('/y_predictt',methods=['POST'])
def y_predictt():
   
    if request.method == 'POST' :
        location= request.form['location']
        pressure = request.form['pressure']
        ne= request.form['ne']
        nw = request.form['nw']
        se= request.form['se']
        sw= request.form['sw']
        swe= request.form['swe']
        if swe=="Loamy Soil":
            swe=int(1)
        elif swe=="Clay Soil":
            swe=int(2)
        else:
            swe=int(3)
            
        
        
       
        xx_test= [[location,pressure,ne,nw,se,sw,swe]]
        
        prediction = model.predict(xx_test) 
        print(prediction)
        output=prediction[0] 
        if output <0.7 :
            print(output)
            output="Carrot Crop is Suitable for this region"
        elif output >0.7 and output <1.8 :
            print(output)
            output="Coconut Crop is Suitable for this region"
        elif output >1.8 and output <2.8 :
            print(output)
            output="Cotton is Suitable for this region"
        elif output >2.8 and output <1.8 :
            print(output)
            output="Ground nut Crop is Suitable for this region"
        elif output >3.8 and output <1.8 :
            print(output)
            output="Melon is Suitable for this region"
        elif output >4.8 and output <1.8 :
            print(output)
            output="Millet is Suitable for this region"
        elif output >5.8 and output <1.8 :
            print(output)
            output="Potatoes is Suitable for this region"
        elif output >6.8 and output <1.8 :
            print(output)
            output="Rice is Suitable for this region"
        elif output >7.8 and output <1.8 :
            print(output)
            output="Vegetables/fruits is Suitable for this region"
        
        else :
            print(output)
            output="Wheat is Suitable for this region"
        print(output)
        
        
        #Flask code 
        
        return render_template('cropprediction.html', prediction_text='{}'.format(output))




@app.route('/contactus', methods =['GET', 'POST'])
def contactus():
    global userid
    msg = 'Contact Sucessfully , We will try to connect soon as possible early' 
   
  
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        message = request.form['message']
        tt=message
        TEXT = "Hello "+username + ",\n\n"+ """Thanks for contacting us for prediction of Natural Disaster Prediction, as soon possible early we will contact you """ 
        message  = 'Subject: {}\n\n{}'.format("Disaster Prediction", TEXT)
        xy="Disaster Prediction"
        sendmail(TEXT,email,xy,tt)
    return render_template('contactus.html', msg = msg)  
        




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True,port = 5000)
