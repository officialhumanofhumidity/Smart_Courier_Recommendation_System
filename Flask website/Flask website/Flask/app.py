
from flask import Flask, render_template,request
from bluedart_rate_and_transit import bluedart_rate_transit
from picker_rate_transit import picker_get_price
from delhivery import delhivery_rate_transit
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('user-input.html')

@app.route('/', methods=['GET','POST'])
def getvalue():
    if request.method == 'POST':
        fromz = request.form.get('from')
        to1 = request.form.get('to')
        weight = (request.form.get('weight'))
        lenghth = request.form.get('lenghth')
        width = request.form.get('width')
        height = request.form.get('height')
        value = request.form.get('value')
        bluedart = bluedart_rate_transit(to1,weight)
        picker = picker_get_price(fromz,to1,weight)
        print("pickker price is ",picker)
        delhivery_data=delhivery_rate_transit(str(fromz),str(to1),str(weight),str(width),str(lenghth),str(height))
        delhivery_price=delhivery_data["Delhivery"]
        dtdc_price=delhivery_data["DTDC 500GMS"]
        kerry_price = delhivery_data["Kerry Indev Express"]
        pricelist=[bluedart["price"],delhivery_price,dtdc_price,kerry_price,picker]
        return render_template('Smart-output.html', value= pricelist)


@app.route('/output')
def output():
    return render_template('Smart-output.html')


app.run()