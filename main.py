import requests
import npyscreen as nps
import socket
import json
link = "https://api.coingecko.com/api/v3/exchange_rates"
query = requests.get(url=link)
response1=query.json()

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class App(nps.NPSAppManaged):
  def onStart(self):
      #add forms to the application
      self.addForm('MAIN',FirstForm, name="Currency Converter")
      self.addForm('FORM2',SecondForm, name='Currency Converting')

class FirstForm(nps.ActionFormMinimal):
    def create(self):
      self.button = self.add(nps.Button, name="Press OK to start")

    def on_ok(self):
      self.parentApp.setNextForm('FORM2')

class SecondForm(nps.ActionForm, nps.FormWithMenus):
    def create(self):
      self.currencyExplain = self.add(nps.TitleFixedText, name ='Please delete btc and enter your desired currency')
      self.currencyAdd = self.add(nps.TitleText, name="Type currency", value = 'btc', editable=True)

    def on_ok(self):
      dkkValue = response1['rates']['dkk']['value']
      coinValue = response1['rates'][self.currencyAdd.value]['value']
      global newValue
      newValue = dkkValue/coinValue

      myJSON = json.dumps({ 'Currency': self.currencyAdd.value, 'Currency in DKK': newValue})

      myBytes = bytes( myJSON, 'utf-8' )

      sock.sendto(myBytes, (UDP_IP, UDP_PORT))

      nps.notify_confirm(str(newValue), title="OK Pressed", wrap=True, wide=True, editw=1)
      self.parentApp.setNextForm('MAIN')
      
app = App()
app.run()