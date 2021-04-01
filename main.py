"""
Developed by - 
Shubh Pathak (MSM19B018)
"""

from flask import Flask,render_template,jsonify,request
import random

app = Flask(__name__)

# Data Storing in List
sno = []
temperature = []
pressure = []
light = []
humidity = []

# Generating Random Values
def generate_data():
   for i in range(1,6):
      sno.append(i)
      temperature.append(random.randint(10,100))
      pressure.append(random.randint(1,50))
      light.append(random.randint(10,20))
      humidity.append(random.randint(20,50))


@app.route('/')
def index():

   data = zip(sno,temperature,pressure,light,humidity)

   return render_template('index.html',data=data) 

"""
REST API Implementations
"""

# Returns the Data
@app.route('/api/data',methods=['GET',])
def return_all_data():
   data = {
      "temperature":temperature,
      "pressure":pressure,
      "light":light,
      "humidity":humidity
   }
   return jsonify(data)


# Appends the New Values of Data to the List
@app.route('/api/add',methods=['POST',])
def add_new_data():
   data = request.get_json()

   try:
      temperature_ = data['temperature']
   except:
      temperature_ = 0
   
   try:
      pressure_ = data['pressure']
   except:
      pressure_ = 0
   
   try:
      light_ = data['light']
   except:
      light_ = 0
   
   try:
      humidity_ = data['humidity']
   except:
      humidity_ = 0

   sno.append(len(sno)+1)
   temperature.append(temperature_)
   pressure.append(pressure_)
   light.append(light_)
   humidity.append(humidity_)
      
   return jsonify({"Values Added":"Check Index Page!"})

# Changes the New Values of Data in the List at Given Index of Array
@app.route('/api/change',methods=['PUT',])
def modify_data():
   data = request.get_json()

   try:
      sno = data['sno']
   except:
      return jsonify({"Unable To Modify Data!":"Invalid Index"})

   try:
      temperature_ = data['temperature']
   except:
      temperature_ = 0
   
   try:
      pressure_ = data['pressure']
   except:
      pressure_ = 0
   
   try:
      light_ = data['light']
   except:
      light_ = 0
   
   try:
      humidity_ = data['humidity']
   except:
      humidity_ = 0

   temperature[sno] = temperature_
   pressure[sno] = pressure_
   light[sno] = light_
   humidity[sno] = humidity_
      
   return jsonify({"Values Changed":"Check Index Page!"})


# Resets All Values in List to 0
@app.route('/api/delete',methods=['DELETE',])
def delete_all_data():
   for i in range(0,len(temperature)):
      temperature[i] = 0
      pressure[i] = 0
      humidity[i] = 0
      light[i] = 0

   return jsonify({"All Values Set To 0":"Restart Flask Server to Get New Random Values!"})

if __name__ == '__main__':
   generate_data()
   app.debug = True
   app.run(host="127.0.0.1",port=5000)