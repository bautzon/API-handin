""""
Fun w. API 
Requirements
1. Make it possible to save results, setting or other through JSON files.
Parse inquiries and return answers

import requests
import npyscreen
#import socket
import json
link = "https://api.coingecko.com/api/v3/exchange_rates"

query = requests.get(url=link)
response1=query.json()

class App(npyscreen.NPSAppManaged):
  def onStart(self):
      #add forms to the application
      self.addForm('MAIN',FirstForm, name="Currency Converter")
      self.addForm('FORM2',SecondForm, name='Currency Converting')

class FirstForm(npyscreen.ActionFormMinimal):
    def create(self):
      self.button = self.add(npyscreen.Button, name="Press OK to start")

      #self.name = self.add(npyscreen.TitleText, name="Username:"
    def on_ok(self):
      self.parentApp.setNextForm('FORM2')
    

class SecondForm(npyscreen.ActionForm, npyscreen.SplitForm, npyscreen.FormWithMenus):
    def create(self):
      self.currencyAdd = self.add( npyscreen.TitleText, name="Type currency2", value= ' ')

    def calc():
      dkkValue = response1['rates']['dkk']['value']
      coinValue = response1['rates'][self.currencyAdd.value]['value']
      newValue= dkkValue/coinValue


    def on_ok(self):
      npyscreen.notify_confirm(print(ToString(calc.newValue)), title="OK Presed", wrap=True, wide=True, editw=1)
      self.parentApp.setNextForm('MAIN')



app = App()
app.run()
"""
class TestApp(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "Welcome to Npyscreen",)
        t  = F.add(npyscreen.TitleText, name = "Text:",)
        fn = F.add(npyscreen.TitleFilename, name = "Filename:")
        fn2 = F.add(npyscreen.TitleFilenameCombo, name="Filename2:")
        dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        s  = F.add(npyscreen.TitleSlider, out_of=12, name = "Slider")
        ml = F.add(npyscreen.MultiLineEdit,
               value = 
               try typing here!\nMutiline text, press ^R to reformat.\n,
               
               max_height=5, rely=9)
        ms = F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One",
                values = ["Option1","Option2","Option3"], scroll_exit=True)
        ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, value = [1,], name="Pick Several",
                values = ["Option1","Option2","Option3"], scroll_exit=True)

        # This lets the user interact with the Form.
        F.edit()

        print(ms.get_selected_objects())

if __name__ == "__main__":
    App = TestApp()
    App.run()"""
    


"""
if ur in response1['rates']:
  print('Noice')
"""
""""
tag navn fra et input
finde værdien respone1(['rates'['currency'['value'])
gic currency et navn 
value traverse 
eth= 2 x btc

dkkPris for 1 bitcoin / ethPris for 1 bitcoin == pris på 1 eth i dkk

dkkValue = response1['rates']['dkk']['value']
        currency = input()
        coinValue=response1['rates'][currency]['value']

        print(dkkValue / coinValue)
"""


