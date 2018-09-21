
import kivy
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
import firebase_admin
from  kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import sys
import time
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import ast
from kivy.properties import ListProperty
import random
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.utils import get_color_from_hex
from sklearn import neighbors, datasets, linear_model
from firebase import firebase
import datetime
from kivy.properties import ObjectProperty
from kivy.properties import ObjectProperty
import call_SIA_API

LabelBase.register(name="Lato", fn_regular="Lato-Regular.ttf" ,fn_bold="Lato-Bold.ttf")

# Create the screen manager
class SIAUIRoot(BoxLayout):
    accord_1 = ObjectProperty(None)
    accord_2 = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(SIAUIRoot, self).__init__(**kwargs)
        self.screen_list = []
        self.quantityInWarehouse,self.quantityInFlight= call_SIA_API.callSIAAPI()
        Clock.schedule_interval(self.change_colour, 2)
        for ac in [self.ids.start_screen.accord_1, self.ids.start_screen.accord_2]:
            print(ac.title)

    def change_screen(self, next_screen, transition=SlideTransition()):
        if self.ids.screen_manager.current not in self.screen_list:
            self.screen_list.append(self.ids.screen_manager.current)
        self.ids.screen_manager.transition = transition
        self.ids.screen_manager.current = next_screen

    def onbackbtn(self):
        # Check if there are any screens to go back to
        if self.screen_list:
            # if there are screens we can go back to, the just do it
            self.ids.screen_manager.current = self.screen_list.pop()
            # Saw we don't want to close
            return True
        # No more screens to go back to
        return False

    def change_colour(self,dt):
        #Retrieve data from firebase
        batt_state = [1,1,1]
        #use of Firebase package has been removed as Publishing credentials as public would result in firebase being suspended
        used= 0
        for bar in batt_state:
            if bar == 0:
               used=used+10
        if batt_state[0] == 0:
            self.ids.start_screen.ids.green1.green_batt = (0.5,0.5,0.5) #TopMostGreen
        else:
            self.ids.start_screen.ids.green1.green_batt = (0.49,1,0) #TopMostGreen
        if batt_state[1] == 0:
            self.ids.start_screen.ids.green2.green_batt2 = (0.5,0.5,0.5) #TopMostGreen
        else:
            self.ids.start_screen.ids.green2.green_batt2 = (0.49,1,0) #TopMostGreen
        if batt_state[1] == 0:
            self.ids.start_screen.ids.green3.green_batt3 = (0.5,0.5,0.5) #TopMostGreen
        else:
            self.ids.start_screen.ids.green3.green_batt3 = (0.49,1,0) #TopMostGreen
        self.ids.start_screen.ids.wareHouseLargePlates.text = "Large Plates: \n" + str(self.quantityInWarehouse)
        self.ids.start_screen.ids.left_plate.text = "Left: " + str(self.quantityInFlight-used)

        self.ids.start_screen.ids.refill_plate.text = "Refill: " + str(used)


class StartScreen(Screen):
    pass

class SavingsScreen(Screen):
    pass

class SIAUIApp(App):
    def __init__(self, **kwargs):
        super(SIAUIApp, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.onbackbtn)
    def build(self):
        return SIAUIRoot()

    def onbackbtn(self, window, key, *args):
        # user presses back button
        if key == 27:
            return self.root.onbackbtn()


if __name__ == '__main__':
    SIAUIApp().run()
