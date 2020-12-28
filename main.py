from kivy.app import App
from kivy.graphics import *
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
import random
i=0
x=[]
class Papp(App):
    def chg(self,nesne):
        global i,x
        a=random.random()
        q=round(a,1)
        y=str(q)
        a1=random.random()
        q1=round(a1,1)
        y1=str(q1)
        a2=random.random()
        q2=round(a2,1)
        y2=str(q2)
        a3=random.random()
        q3=round(a3,1)
        y3=str(q3)
        x.append([q,q1,q2,q3])
        n=len(x)
        i +=1
        Window.clearcolor=(q,q1,q2,q3)
        if n >= 0:
            self.label2.text=str(i)+". Tercihiniz:"+str(x[n-1])
        else:
            self.label2.text=str(i)+". Tercihiniz:"+str(x[0])
        if n >= 2:                                            
            self.label3.text=str(i-1)+". Terchiniz:"+str(x[n-2])
        else:
            self.label3.text="Tercihler"
        if n >= 3:
            self.label4.text=str(i-2)+". Tercihiniz:"+str(x[n-3])
        else:
            self.label4.text="Tercihler"
        if n >=4 :
            self.label5.text=str(i-3)+". Tercihiniz:"+str(x[n-4])
        else:
            self.label5.text="Tercihler"
        if n >=5:
            self.label6.text=str(i-4)+". Tercihiniz:"+str(x[n-5])
        else:
            self.label6.text="Tercihler"
        
        self.label.text=("[color=ff0000]RGBCode:"+"("+y+" ,"+y1+" ,"+y2+" ,"+y3+")""[/color]")
    def build(self):
        root=Widget()
        self.label2=Label(text="Tercihler",size=(250,30),pos=(250,510))
        with self.label2.canvas.before:
            Color(0,0,0,1)
            Rectangle(pos=self.label2.pos,size=self.label2.size)
        self.label=Label(text="[color=ff0000]RgbCode:(0,0,0,0)[/color]",size=(250,30),pos=(250,540),markup=True)
        with self.label.canvas.before:
            Color(1,1,1,1)
            Rectangle(pos=self.label.pos , size=self.label.size)
        self.label3=Label(text="Tercihler",size=(250,30),pos=(250,480))
        with self.label3.canvas.before:
            Color(0,0,0,1)
            Rectangle(pos=self.label3.pos,size=self.label3.size)
        self.label4=Label(text="Tercihler",size=(250,30),pos=(250,450))
        with self.label4.canvas.before:
            Color(0,0,0,1)
            Rectangle(size=self.label4.size,pos=self.label4.pos)
        self.label5=Label(text="Tercihler",size=(250,30),pos=(250,420))
        with self.label5.canvas.before:
            Color(0,0,0,1)
            Rectangle(size=self.label5.size,pos=self.label5.pos)
            
        self.label6=Label(text="Tercihler",size=(250,30),pos=(250,390))
        with self.label6.canvas.before:
            Color(0,0,0,1)
            Rectangle(size=self.label6.size,pos=self.label6.pos)
        self.button=Button(text="Random",size=(100,100),pos=(330,250))        
        self.button.bind(on_press=self.chg)
        root.add_widget(self.label6)
        root.add_widget(self.label5)
        root.add_widget(self.label4)
        root.add_widget(self.label3)
        root.add_widget(self.label2)
        root.add_widget(self.button)
        root.add_widget(self.label)
        return root

Papp().run()
