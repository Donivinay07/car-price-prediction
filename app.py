from flask import Flask, render_template,jsonify,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods =['GET','POST'])
def predict():
    if request.method=="POST":
        make=request.form.get("make")
        model=request.form.get("model")
        year = request.form.get("year")
        fuel_type = request.form.get("fuel_type")
        hp = request.form.get("hp")
        cylinders = request.form.get("cylinders")
        transmission = request.form.get("transmission")
        driven_wheels = request.form.get("driven_wheels")
        doors = request.form.get("doors")
        size = request.form.get("size")
        style = request.form.get("style ")
        highway_mpg = request.form.get("highway_mpg")
        city_mpg = request.form.get("city_mpg") 
        popularity = request.form.get("popularity")
        print(make,model,year,fuel_type,hp,cylinders,transmission,driven_wheels,doors,size,style,highway_mpg,city_mpg,popularity)
        return jsonify({"status":"data fetched sucessfully"})
    else:
        return render_template('predict.html')
        

        
if __name__=='__main__':
    app.run(host='0.0.0.0')