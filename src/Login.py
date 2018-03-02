'''
Created on 1 mar. 2018

@author: JorInt
'''

import wx


class LoginFrame(wx.Frame):
    def __init__(self, parent, titulo):
        wx.Frame.__init__(self, parent, title=titulo, size=(300,400))
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.WHITE)
        self.usuarioBox()
        self.passwordBox()
        self.loginButton()
        self.Show(True)
     
       
    def usuarioBox(self):
        self.texto_usuario = wx.StaticText(self.panel, label='Usuario', size=(150, 30), pos=(100,20))
        self.usuario_box = wx.TextCtrl(self.panel, size=(150, 30), pos=(100, 50))
        
    def passwordBox(self):
        self.texto_password = wx.StaticText(self.panel, label='Clave', size=(150, 30), pos=(100,100))
        self.password_box = wx.TextCtrl(self.panel, size=(150, 30), pos=(100, 130))
    
    def loginButton(self):
        self.boton_login = wx.Button(self.panel, label= 'Ingresar', size=(70, 30), pos=(150, 170), style=wx.BORDER_NONE)
        self.boton_login.SetForegroundColour(wx.WHITE)
        self.boton_login.SetBackgroundColour(wx.BLUE)
        
    
    def cerrar_frame(self):
        self.Destroy()





debug = True
if debug == True:
    app = wx.App(False)
    frame = LoginFrame(None, "Hello")
    frame.Show(True)
    app.MainLoop()