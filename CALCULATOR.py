import re
import math
from kivy.factory import Factory
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.properties import ObjectProperty
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.uix.colorpicker import ColorPicker
from kivy.properties import ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.uix.popup import Popup
Window.size = (500, 400)
Window.minimum_width, Window.minimum_height = Window.size
class mypopup(Popup):
    pass

class FirstWindow(Screen):
    def openpopup(self):
        pops=mypopup()
        pops.open()



    #def poptrigger(self):
      #  show_popup()


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    # Define a dynamic property for the button color
    button_color = ListProperty([1, 1, 1, 1])  # white

    def build(self):
        # Create a box layout widget
        layout = BoxLayout(orientation="vertical")
        # Create a color picker widget
        picker = ColorPicker()
        # Bind the function to change the button color on color selection
        picker.bind(color=self.change_color)
        # Create a button widget
        button = Button(text="Change Color",
                        background_color=self.button_color,
                        size_hint=(0.5, 0.2),
                        pos_hint={"center_x": 0.5, "center_y": 0.5})
        # Add the widgets to the layout
        layout.add_widget(picker)
        layout.add_widget(button)
        # Return the layout as the root widget
        return layout

    def change_color(self, instance, value):
        # Change the button color to the selected color
        self.button_color = value


class FourthWindow(Screen):
    pass


class FifthWindow(Screen):
    pass


class SixthWindow(Screen):
    pass


class CalWindow(Screen):
    def get_value(self, number):
        prenum = self.ids.cal_inp.text
        if 'Error' in prenum:
            prenum = ''
        if 'Math error' in prenum:
            prenum = ''
        if 'Undefined' in prenum:
            prenum = ''

        #if prenum == "0":
            #self.ids.cal_inp.text = " "
            #self.ids.cal_inp.text = f"{number}"
        else:
            self.ids.cal_inp.text = f"{prenum}{number}"

    def all_clr(self):
        prenum = self.ids.cal_inp.text
        self.ids.cal_inp.text = ''

    def back(self):
        prenum = self.ids.cal_inp.text
        nwnm = prenum[:-1]
        self.ids.cal_inp.text = nwnm

    def signs(self, operators):
        prenum = self.ids.cal_inp.text
        self.ids.cal_inp.text = f'{prenum}{operators}'

    def answer(self):
        try:
            prenum = self.ids.cal_inp.text

            ans = eval(prenum)
            self.ids.cal_inp.text = str(ans)
            if '^' in prenum   :
                ans1 = prenum.replace("^", "**")
                ans2 = ans1
                ans3 = eval(ans2)
                self.ids.cal_inp.text = str(float(ans3))
            if "0^0" in prenum:
                self.ids.cal.inp.text='nope'





        except:

            self.ids.cal_inp.text = 'Error'

    def posneg(self):
        prenum = self.ids.cal_inp.text
        if '-' in prenum:
            self.ids.cal_inp.text = f'{prenum.replace("-", "")}'
        else:
            self.ids.cal_inp.text = f'-{prenum}'

    def dot(self):
        prenum = self.ids.cal_inp.text
        num_list = re.split('\+|-|/|\*', prenum)
        if ('+' in prenum or '-' in prenum or '*' in prenum or '/' in prenum) and '.' not in num_list[-1]:
            prenum = f'{prenum}.'
            self.ids.cal_inp.text = prenum
        elif '.' in prenum:
            pass
        else:
            self.ids.cal_inp.text = f'{prenum}.'

    def percent(self):
        try:

            prenum = self.ids.cal_inp.text
            ans1 = f'{prenum}/100'
            ans2 = eval(ans1)
            self.ids.cal_inp.text = str(float(ans2))
        except:
            self.ids.cal_inp.text = 'Undefined'

    def one_over(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = f'1/{prenum}'
            ans1 = eval(ans)
            self.ids.cal_inp.text = str(float(ans1))
        except:
            self.ids.cal_inp.text = 'Undefined'

    def square(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = f'{prenum}*{prenum}'
            ans1 = eval(ans)
            self.ids.cal_inp.text = str(float(ans1))
        except:

            self.ids.cal_inp.text = 'Error'

    def cube(self):
        try:

            prenum = self.ids.cal_inp.text
            ans = f'{prenum}*{prenum}*{prenum}'
            ans1 = eval(ans)
            self.ids.cal_inp.text = str(float(ans1))
        except:

            self.ids.cal_inp.text = 'Error'

    def square_root(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = math.sqrt(float(prenum))
            self.ids.cal_inp.text = str(ans)
        except:
            self.ids.cal_inp.text = 'Error'

    def cube_root(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = f'{prenum}**(1/3)'
            ans1 = eval(ans)
            self.ids.cal_inp.text = str(ans1)
        except:
            self.ids.cal_inp.text = 'Error'

    def sine(self):
        try:

            prenum = self.ids.cal_inp.text
            ans = math.sin(math.radians(float(prenum)))

            self.ids.cal_inp.text = str(ans)
        except:
            self.ids.cal_inp.text = 'Error'

    def cosine(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = math.cos(math.radians(float(prenum)))

            self.ids.cal_inp.text = str(ans)
        except:
            self.ids.cal_inp.text = 'Error'

    def tangent(self):
        try:

            prenum = self.ids.cal_inp.text
            ans = math.tan(math.radians(float(prenum)))

            self.ids.cal_inp.text = str(ans)
        except:
            self.ids.cal_inp.text = 'Error'

    def tangent_inv(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = math.atan(float(prenum))
            ans2 = math.degrees(ans)

            self.ids.cal_inp.text = str(ans2)
        except:
            self.ids.cal_inp.text = 'Math error'

    def cosine_inv(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = math.acos(float(prenum))
            ans2 = math.degrees(ans)

            self.ids.cal_inp.text = str(ans2)
        except:
            self.ids.cal_inp.text = 'Math error'

    def sine_inv(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = math.asin(float(prenum))
            ans2 = math.degrees(ans)

            self.ids.cal_inp.text = str(ans2)
        except:
            self.ids.cal_inp.text = 'Math error'

    def log(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = math.log10(float(prenum))

            self.ids.cal_inp.text = str(ans)
        except:
            self.ids.cal_inp.text = 'Math error'

    def pi(self):
        try:
            prenum = self.ids.cal_inp.text
            self.ids.cal_inp.text = str(math.pi)
        except:
            self.ids.cal_inp.text = 'Error'

    def x_tenpow(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = f'{prenum}**10'
            ans2 = eval(ans)
            self.ids.cal_inp.text = str(ans2)
        except:
            self.ids.cal_inp.text = 'too much to render'

    def sinh(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = math.sinh(float(prenum))
            self.ids.cal_inp.text = str(ans)
        except:
            self.ids.cal_inp.text = 'Math error'

    def cosh(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = math.cosh(float(prenum))
            self.ids.cal_inp.text = str(ans)
        except:
            self.ids.cal_inp.text = 'Math error'

    def tanh(self):
        try:
            prenum = self.ids.cal_inp.text
            ans = math.tanh(float(prenum))
            self.ids.cal_inp.text = str(ans)
        except:
            self.ids.cal_inp.text = 'Math error'


class AreaWindow(Screen):
    #functions for triangle
    def get_value(self, num):
        prenum1 = self.ids.b.text

        prenum2 = self.ids.c.text

        if self.ids.chk.active == True:
            self.ids.chk1.active = False
            self.ids.chk2.active = False
            prenum = self.ids.a.text

            self.ids.a.text = f"{prenum}{num}"
        if self.ids.chk1.active == True:
            self.ids.chk.active = False
            self.ids.chk2.active = False
            prenum1 = self.ids.b.text
            self.ids.b.text = f"{prenum1}{num}"
        if self.ids.chk2.active == True:
            prenum2 = self.ids.c.text
            self.ids.c.text = f"{prenum2}{num}"

    def answers(self):
        try:
            inpa = float(self.ids.a.text)
            inpb = float(self.ids.b.text)
            inpc = float(self.ids.c.text)
            ans1 = (inpa + inpb + inpc) / 2
            an = (ans1 * (ans1 - inpa) * (ans1 - inpb) * (ans1 - inpc))
            ans2 = math.sqrt(an)
            ans3 = str(ans2)
            ans4 = round(ans2, 6)
            self.ids.ans.text = f"{ans4} m²"
        except:
            self.ids.ans.text = 'math domain error'

    def al_clr(self):
        self.ids.a.text = ''
        self.ids.b.text = ''
        self.ids.c.text = ''
        self.ids.ans.text = ''

    def point(self):
        prenum = self.ids.a.text
        prenum1 = self.ids.b.text
        prenum2 = self.ids.c.text
        if self.ids.chk.active == True and '.' not in prenum:
            self.ids.a.text = f'{prenum}.'
        elif '.' in prenum:
            pass

        if self.ids.chk1.active == True and '.' not in prenum1:
            self.ids.b.text = f'{prenum1}.'
        elif '.' in prenum1:
            pass

        if self.ids.chk2.active == True and '.' not in prenum2:
            self.ids.c.text = f'{prenum2}.'
        elif '.' in prenum2:
            pass

    def tri_back(self):
        prenum = self.ids.a.text
        prenum1 = self.ids.b.text
        prenum2 = self.ids.c.text
        if self.ids.chk.active == True:
            nwnm = prenum[:-1]
            self.ids.a.text = nwnm
        if self.ids.chk1.active == True:
            nwnm = prenum1[:-1]
            self.ids.b.text = nwnm
        if self.ids.chk2.active == True:
            nwnm = prenum2[:-1]
            self.ids.c.text = nwnm
    def t_change(self,value):
        self.ids.t_canvas.t_color=(1,1,1)
        if value:
            self.ids.t_canvas.t_color = (0, 1, 1)
            self.ids.for_t.text='s=([i][b][size=24][color=#04d3ff]a[/color][/size][/i][/b]+b+c)/2'
            self.ids.for_t1.text='A=√(s-[i][b][size=24][color=#04d3ff]a[/color][/size][/i][/b])(s-b)(s-c)'
        else:
            self.ids.for_t.text = 's=([size=20][color=#ffffff]a[/color][/size]+b+c)/2'
            self.ids.for_t1.text = 'A=√(s-[size=20][color=ffffff]a[/color][/size])(s-b)(s-c)'
    def t_change1(self, value):
        self.ids.t_canvas.t_color1 = (1, 1, 1)
        if value:
            self.ids.t_canvas.t_color1 = (0, 1, 1)
            self.ids.for_t.text='s=(a+[i][b][size=24][color=#04d3ff]b[/color][/size][/i][/b]+c)/2'
            self.ids.for_t1.text='A=√(s-a)(s-[i][b][size=24][color=#04d3ff]b[/color][/size][/i][/b])(s-c)'
        else:
            self.ids.for_t.text = 's=(a+[size=20][color=#ffffff]b[/color][/size]+c)/2'
            self.ids.for_t1.text = 'A=√(s-a)(s-[size=20][color=#ffffff]b[/color][/size])(s-c)'

    def t_change2(self, value):
        self.ids.t_canvas.t_color2 = (1, 1, 1)
        if value:
            self.ids.t_canvas.t_color2 = (0, 1, 1)
            self.ids.for_t.text="s=(a+b+[i][b][size=24][color=#04d3ff]c[/color][/size][/i][/b])/2"
            self.ids.for_t1.text="A=√(s-a)(s-b)(s-[i][b][size=24][color=#04d3ff]c[/color][/size][/i][/b])"
        else:
            self.ids.for_t.text = "s=(a+b+[size=20][color=#ffffff]c[/color][/size])/2"
            self.ids.for_t1.text = "A=√(s-a)(s-b)(s-[size=20][color=#ffffff]c[/color][/size])"

    # functions for area of rectangle
    def get_valuer(self, num1):
        prenum = self.ids.inpr.text
        prenum1 = self.ids.inpr1.text
        if self.ids.rchk.active == True:
            self.ids.inpr.text = f"{prenum}{num1}"
        if self.ids.rchk1.active == True:
            self.ids.inpr1.text = f"{prenum1}{num1}"

    def area_rec(self):
        try:
            prenum = self.ids.inpr.text
            prenum1 = self.ids.inpr1.text
            ans = float(prenum) * float(prenum1)
            ans1 = float(ans)
            ans2 = round(ans1, 8)
            self.ids.rans.text = f"{ans2}  m²"
        except:
            self.ids.rans.text = 'input error'

    def rec_dot(self):
        prenum = self.ids.inpr.text
        prenum1 = self.ids.inpr1.text
        if self.ids.rchk.active == True and '.' not in prenum:
            self.ids.inpr.text = f"{prenum}."
        elif '.' in prenum:
            pass
        if self.ids.rchk1.active == True and '.' not in prenum1:
            self.ids.inpr1.text = f"{prenum1}."
        elif '.' in prenum1:
            pass

    def rec_all_clr(self):
        self.ids.inpr.text = ''
        self.ids.inpr1.text = ''
        self.ids.rans.text = ''

    def rec_del(self):

        prenum1 = self.ids.inpr.text
        prenum2 = self.ids.inpr1.text

        if self.ids.rchk.active == True:
            nwnm = prenum1[:-1]
            self.ids.inpr.text = nwnm
        if self.ids.rchk1.active == True:
            nwnm = prenum2[:-1]
            self.ids.inpr1.text = nwnm

    def change1(self, value):
        self.ids.w_canvas.my_color = (1, 1, 1)
        self.ids.w_canvas.my_color2 = (1, 1, 1)
        if value:
            self.ids.w_canvas.my_color = (0, 1, 1)
            self.ids.for_rec.text = "A=[size=34][color=#04d3ff][i][b]L[/b][/i][/color][/size]XW"


        else:
            self.ids.w_canvas.my_color = (1, 1, 1)
            self.ids.for_rec.text = "A=[size=30][color=#ffffff]L[/color][/size]XW"

    def change2(self, value):
        self.ids.w_canvas.my_color = (1, 1, 1)
        self.ids.w_canvas.my_color2 = (1, 1, 1)
        if value:
            self.ids.w_canvas.my_color2 = (0, 1, 1)
            self.ids.for_rec.text = "A=LX[size=34][color=#04d3ff][i][b]W[/b][/i][/color][/size]"
        else:
            self.ids.w_canvas.my_color2 = (1, 1, 1)
            self.ids.for_rec.text = "A=[size=30][color=#ffffff]LX[size=30][color=#ffffff]W[/color][/size]"

    # functions for area of trapezium
    def tra_get_value(self, num2):
        prenum = self.ids.tra_inp.text
        prenum1 = self.ids.tra_inp1.text
        prenum2 = self.ids.tra_inp2.text
        if self.ids.tra_chk.active == True:
            self.ids.tra_inp.text = f'{prenum}{num2}'
        if self.ids.tra_chk1.active == True:
            self.ids.tra_inp1.text = f'{prenum1}{num2}'
        if self.ids.tra_chk2.active == True:
            self.ids.tra_inp2.text = f'{prenum2}{num2}'

    def tra_ans(self):
        try:
            prenum = self.ids.tra_inp.text
            prenum1 = self.ids.tra_inp1.text
            prenum2 = self.ids.tra_inp2.text
            ans = ((float(prenum) + float(prenum1)) / 2) * float(prenum2)
            self.ids.tra_ans.text = f"{ans} m²"

        except:
            self.ids.tra_ans.text = "input error"

    def tra_all_clr(self):
        self.ids.tra_inp.text = ''
        self.ids.tra_inp1.text = ''
        self.ids.tra_inp2.text = ''
        self.ids.tra_ans.text = ''

    def tra_back(self):
        prenum = self.ids.tra_inp.text
        prenum1 = self.ids.tra_inp1.text
        prenum2 = self.ids.tra_inp2.text
        if self.ids.tra_chk.active:
            nwnm = prenum[:-1]
            self.ids.tra_inp.text = nwnm
        if self.ids.tra_chk1.active:
            nwnm = prenum1[:-1]
            self.ids.tra_inp1.text = nwnm
        if self.ids.tra_chk2.active:
            nwnm = prenum2[:-1]
            self.ids.tra_inp2.text = nwnm

    def tra_dot(self):
        prenum = self.ids.tra_inp.text
        prenum1 = self.ids.tra_inp1.text
        prenum2 = self.ids.tra_inp2.text
        if self.ids.tra_chk.active == True and '.' not in prenum:
            self.ids.tra_inp.text = f"{prenum}."
        elif '.' in prenum:
            pass
        if self.ids.tra_chk1.active == True and '.' not in prenum1:
            self.ids.tra_inp1.text = f"{prenum1}."
        elif '.' in prenum1:
            pass
        if self.ids.tra_chk2.active == True and '.' not in prenum2:
            self.ids.tra_inp2.text = f"{prenum2}."
        elif '.' in prenum2:
            pass

    def tra_change(self, value):
        self.ids.w_canvas1.tra_color = (1, 1, 1)
        self.ids.w_canvas1.tra_color1 = (1, 1, 1)
        self.ids.w_canvas1.tra_color2 = (1, 1, 1)
        self.ids.w_canvas1.tra_color3 = (1, 1, 1)

        if value:
            self.ids.w_canvas1.tra_color = (0, 1, 1)
            self.ids.for_tra.text = 'A=1/2([size=34][color=#04d3ff][i][b]b[/i][/b][/color][/size][sub][color=#04d3ff][size=20][i][b]1[/b][/i][/size][/sub][/color]+b[sub][size=15]2[/size][/sub])h'
        else:
            self.ids.w_canvas1.tra_color = (1, 1, 1)
            self.ids.for_tra.text = "A=1/2([size=30][color=#ffffff]b[/size][/color][sub][size=15][color=ffffff]1[/size][/sub][/color]+b[sub][size=15]2[/size][/sub])h"

    def tra_change1(self, value):
        self.ids.w_canvas1.tra_color = (1, 1, 1)
        self.ids.w_canvas1.tra_color1 = (1, 1, 1)
        self.ids.w_canvas1.tra_color2 = (1, 1, 1)
        self.ids.w_canvas1.tra_color3 = (1, 1, 1)

        if value:
            self.ids.w_canvas1.tra_color2 = (0, 1, 1)
            self.ids.for_tra.text = "A=1/2(b[sub][size=15][color=#ffffff]1[/size][/sub][/color]+[size=34][color=#04d3ff][i][b]b[/b][/i][/size][/color][sub][color=#04d3ff][size=20][i][b]2[/i][/b][/size][/color][/sub])h"
        else:
            self.ids.w_canvas1.tra_color2 = (1, 1, 1)
            self.ids.for_tra.text = 'A=1/2(b[sub][size=15]1[/size][/sub]+b[sub][size=15]2[/size][/sub])h'

    def tra_change2(self, value):
        self.ids.w_canvas1.tra_color = (1, 1, 1)
        self.ids.w_canvas1.tra_color1 = (1, 1, 1)
        self.ids.w_canvas1.tra_color2 = (1, 1, 1)
        self.ids.w_canvas1.tra_color3 = (1, 1, 1)

        if value:
            self.ids.w_canvas1.tra_color1 = (0, 1, 1)
            self.ids.for_tra.text = 'A=1/2(b[sub][size=15]1[/size][/sub]+b[sub][size=15]2[/size][/sub])[size=34][color=#04d3ff][b][i]h[/i][/b][/size][/color]'
        else:
            self.ids.w_canvas1.tra_color1 = (1, 1, 1)
            self.ids.for_tra.text = 'A=1/2(b[sub][size=15]1[/size][/sub]+b[sub][size=15]2[/size][/sub])h'
    # functions for sphere
    def get_value_sp(self,num):
        if self.ids.sp_id.active==True:
            prenum=self.ids.sp_inp.text
            self.ids.sp_inp.text=f"{prenum}{num}"
        else:
            pass
    def sp_ans(self):
        prenum=float(self.ids.sp_inp.text)
        pie=math.pi
        ans=4*pie*prenum**2
        ans1=round(ans,6)
        self.ids.sp_ans.text=f'{ans1}m²'
    def sp_change(self,value):
        if value:
            self.ids.sp_cnvs.sp_rad_color=(0,1,1)
            self.ids.for_sp.text='A=4π[b][i][size=34][color=#04d3ff]r[/i][/b][/color][/size][sup][color=#04d3ff][size=20]2[/size][/color][/sup]'
        else:
            self.ids.for_sp.text='A=4π[size=30][color=#ffffff]r[/color][/size][sup][color=#ffffff][size=15]2[/size][/color][/sup]'
            self.ids.sp_cnvs.sp_rad_color = (1, 1, 1)
    def sp_all_clr(self):
        self.ids.sp_ans.text = ""
        self.ids.sp_inp.text = ""
    def sp_back(self):
        prenum=self.ids.sp_inp.text
        nwnm=prenum[:-1]
        self.ids.sp_inp.text=nwnm
    def sp_dot(self):
        prenum=self.ids.sp_inp.text
        if self.ids.sp_id.active==True and '.' not in prenum:
            self.ids.sp_inp.text=f"{prenum}."
        if '.' in prenum:
            pass
    #functions for cirle
    def cir_get_value(self,num):
        if self.ids.cir_id.active==True:
            prenum=self.ids.cir_inp.text
            self.ids.cir_inp.text=f"{prenum}{num}"
        else:
            pass
    def cir_ans(self):
        prenum=float(self.ids.cir_inp.text)
        pi=math.pi
        ans=pi*prenum**2
        ans2=round(ans,6)
        self.ids.cir_ans.text=f"{ans2}m²"
    def cir_change_color(self,value):
        if value:
            self.ids.cir_cnvs.cir_rad_color=(0,1,1)
            self.ids.for_cir.text='A=π[b][i][color=#04d3ff][size=34]r²[/b][/i][/color][/size]'
        else:
            self.ids.cir_cnvs.cir_rad_color = (1, 1, 1)
            self.ids.for_cir.text = 'A=π[color=#ffffff][size=30]r²[/color][/size]'
    def cir_alcr(self):
        self.ids.cir_inp.text=''
        self.ids.cir_ans.text=''
    def cir_dot(self):
        prenum=self.ids.cir_inp.text
        if self.ids.cir_id.active==True and '.' not in prenum:
            self.ids.cir_inp.text=f"{prenum}."
        if '.' in prenum:
            pass
    def cir_back(self):
        prenum=self.ids.cir_inp.text
        nwnm=prenum[:-1]
        self.ids.cir_inp.text=nwnm
    #fumctioms for paralellogram
    def para_get_value(self,num):
        if self.ids.par_id1.active==True:
            prenum1=self.ids.par_inp1.text
            self.ids.par_inp1.text=f"{prenum1}{num}"
        if self.ids.par_id2.active == True:
            prenum2 = self.ids.par_inp2.text
            self.ids.par_inp2.text = f"{prenum2}{num}"
    def para_dot(self):
        prenum1=self.ids.par_inp1.text
        prenum2 = self.ids.par_inp2.text
        if self.ids.par_id1.active==True and '.' not in prenum1:
            self.ids.par_inp1.text=f"{prenum1}."
        elif '.' in prenum1:
            pass
        if self.ids.par_id2.active==True and '.' not in prenum2:
            self.ids.par_inp2.text=f"{prenum2}."
        if '.' in prenum2:
            pass
    def para_allclr(self):
        self.ids.par_inp1.text=""
        self.ids.par_inp2.text = ""
        self.ids.para_ans.text = ""
    def para_delete(self):
        prenum= self.ids.par_inp1.text
        prenum2=self.ids.par_inp2.text
        if self.ids.par_id1.active== True:
            nwnm=prenum[:-1]
            self.ids.par_inp1.text=nwnm
        if self.ids.par_id2.active== True:
            nwnm=prenum2[:-1]
            self.ids.par_inp2.text=nwnm
    def para_change1(self,value):
        self.ids.par_id.len_color_par=(1, 1 , 1)
        self.ids.par_id.width_color_par = (1, 1, 1)
        self.ids.par_id.par_height=(1,1,1)
        if value:
            self.ids.par_id.len_color_par = (0, 1, 1)
            self.ids.for_par.text="A=[size=34][color=#04d3ff][i][b]b[/b][/i][/color][/size]h"
        else:
            self.ids.par_id.len_color_par = (1, 1, 1)
            self.ids.par_id.width_color_par = (1, 1, 1)
            self.ids.for_par.text="A=[size=30][color=#ffffff]b[size=30][color=#ffffff]h[/color][/size]"
    def para_change2(self,value):
        self.ids.par_id.len_color_par = (1, 1, 1)
        self.ids.par_id.width_color_par = (1, 1, 1)
        self.ids.par_id.par_height = (1, 1, 1)
        if value:
            self.ids.par_id.par_height=(0,1,1)
            self.ids.for_par.text="A=b[size=34][color=#04d3ff][i][b]h[/b][/i][/color][/size]"
        else:
            self.ids.par_id.par_height = (1, 1, 1)
            self.ids.par_id.width_color_par = (1, 1, 1)
            self.ids.for_par.text = "A=[size=30][color=#ffffff]b[size=30][color=#ffffff]h[/color][/size]"
    def para_area(self):
        try:
            prenum=float(self.ids.par_inp1.text)
            prenum2=float(self.ids.par_inp2.text)
            answer= prenum*prenum2
            self.ids.para_ans.text=f"{answer}m²"
        except:
            self.ids.para_ans.text="math domain error"

#functions for rhombus
    def get_value_rhombus(self,num):
        prenum=self.ids.rhom_inp1.text
        prenum2=self.ids.rhom_inp2.text
        if self.ids.rhom_chk_id1.active==True:
            self.ids.rhom_inp1.text=f"{prenum}{num}"
        if self.ids.rhom_chk_id2.active==True:
            self.ids.rhom_inp2.text=f"{prenum2}{num}"
    def rhom_dot(self):
        prenum = self.ids.rhom_inp1.text
        prenum2 = self.ids.rhom_inp2.text
        if self.ids.rhom_chk_id1.active==True and '.' not in prenum:
            self.ids.rhom_inp1.text=f"{prenum}."
        else:
            pass
        if self.ids.rhom_chk_id2.active==True and '.' not in prenum2:
            self.ids.rhom_inp2.text=f"{prenum2}."
        else:
            pass
    def rhom_back(self):
        prenum = self.ids.rhom_inp1.text
        prenum2 = self.ids.rhom_inp2.text
        if self.ids.rhom_chk_id1.active==True:
            nwnm=prenum[:-1]
            self.ids.rhom_inp1.text=nwnm
        if self.ids.rhom_chk_id2.active == True:
            nwnm = prenum2[:-1]
            self.ids.rhom_inp2.text = nwnm
    def rhom_allclr(self):
        self.ids.rhom_inp1.text=""
        self.ids.rhom_inp2.text = ""
        self.ids.rhom_ans.text = ""
    def rhom_change1(self,value):
        self.ids.rhom_cnvs.rhom_d1_color=(1,1,1)
        self.ids.rhom_cnvs.rhom_d2_color = (1, 1, 1)
        if value:
            self.ids.rhom_cnvs.rhom_d1_color = (0, 1, 1)
            self.ids.for_rhom.text="A=1/2([color=#04d3ff][size=34][i][b]d[sub][color=#04d3ff][size=20][b][i]1[/color][/b][/i][/size][/sub][/b][/i][/color][/size]d[sub][size=15]2[/sub][/size])"
        else:
            self.ids.rhom_cnvs.rhom_d1_color = (1, 1, 1)
            self.ids.rhom_cnvs.rhom_d2_color = (1, 1, 1)
            self.ids.for_rhom.text="A=1/2([color=#ffffff][size=30]d[/color][/size][color=#ffffff][sub][size=15]1[/size][/sub][/color]d[sub][size=15]2[/sub][/size])"

    def rhom_change2(self,value):
        self.ids.rhom_cnvs.rhom_d1_color = (1, 1, 1)
        self.ids.rhom_cnvs.rhom_d2_color = (1, 1, 1)
        if value:
            self.ids.rhom_cnvs.rhom_d2_color=(0,1,1)
            self.ids.for_rhom.text="A=1/2(d[sub][size=15]1[/sub][/size][b][i][size=34][color=#04d3ff]d[sub][color=#04d3ff][size=20][b][i]2[/sub][/color][/i][/b][/size][/sub][/color][/i][/b][/size])"
        else:
            self.ids.rhom_cnvs.rhom_d1_color = (1, 1, 1)
            self.ids.rhom_cnvs.rhom_d2_color = (1, 1, 1)
            self.ids.for_rhom.text="A=1/2(d[sub][size=15]1[/sub][/size][size=30][color=#ffffff]d[/color][/size][sub][size=15][color=#ffffff]2[/sub][/color][/size])"

    def rhom_answer(self):
        prenum=self.ids.rhom_inp1.text
        prenum2=self.ids.rhom_inp2.text
        answer=1/2*(float(prenum)*float(prenum2))

        self.ids.rhom_ans.text=f"{answer}m²"









class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('ourch.kv')


class mainApp(App):



    def build(self):
        Window.clearcolor=(0,0,0,.5)
        return kv
    def close_app(self):
        self.stop()




#def show_popup():
   # show= popwind()
    #popcontent=Popup(title="popup window",content=show,size_hint=(None,None),size=(400,400))
    #popcontent.open()

if __name__ == '__main__':
    mainApp().run()

