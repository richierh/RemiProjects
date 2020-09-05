
from remi.gui import *

class Container( Container ):                                                                                                          #cheak:Maybe change class name to name of root container

    def __init__(self, AppInst=None, *args, **kwargs):
        super().__init__(*args, **kwargs)                                                                                                #cheak:remove Comments
        self.AppInst = AppInst                                                                                                           #cheak:remove Comments
        self.constructUI()                                                                                                               #cheak:instead we just call it
        self.userInit(args, kwargs)                                                                                                      #more. Register events. Add custom widgets. Add css classes etc.
                                                                                                                                         # pass kwargs to user init in case user needs it.

    def constructUI(self):
        self.attr_class = "Container"
        self.attr_editor_newclass = False
        self.css_align_content = "stretch"
        self.css_align_self = "auto"
        self.css_display = "flex"
        self.css_height = "250px"
        self.css_left = "20px"
        self.css_position = "static"
        self.css_top = "20px"
        self.css_width = "250px"
        self.variable_name = "container0"
        hbox0 = HBox()
        hbox0.attr_class = "HBox"
        hbox0.attr_editor_newclass = False
        hbox0.css_align_items = "center"
        hbox0.css_display = "flex"
        hbox0.css_flex_direction = "row"
        hbox0.css_height = "250px"
        hbox0.css_justify_content = "space-around"
        hbox0.css_left = "20px"
        hbox0.css_position = "static"
        hbox0.css_top = "20px"
        hbox0.css_width = "250px"
        hbox0.variable_name = "hbox0"
        vbox0 = VBox()
        vbox0.attr_class = "VBox"
        vbox0.attr_editor_newclass = False
        vbox0.css_align_items = "center"
        vbox0.css_background_color = "rgb(145,166,173)"
        vbox0.css_display = "flex"
        vbox0.css_flex_direction = "column"
        vbox0.css_height = "250px"
        vbox0.css_justify_content = "space-around"
        vbox0.css_order = "139949328420048"
        vbox0.css_position = "static"
        vbox0.css_top = "20px"
        vbox0.css_width = "250px"
        vbox0.variable_name = "vbox0"
        button0 = Button()
        button0.attr_class = "Button"
        button0.attr_editor_newclass = False
        button0.css_background_color = "rgb(122,69,180)"
        button0.css_border_color = "rgb(0,0,0)"
        button0.css_color = "rgb(255,255,255)"
        button0.css_font_size = "30px"
        button0.css_height = "50px"
        button0.css_order = "139949325360384"
        button0.css_position = "static"
        button0.css_top = "20px"
        button0.css_width = "70px"
        button0.text = "7"
        button0.variable_name = "button0"
        vbox0.append(button0,'button0')
        button1 = Button()
        button1.attr_class = "Button"
        button1.attr_editor_newclass = False
        button1.css_height = "30px"
        button1.css_order = "139949326830896"
        button1.css_position = "static"
        button1.css_top = "20px"
        button1.css_width = "100px"
        button1.text = "button"
        button1.variable_name = "button1"
        vbox0.append(button1,'button1')
        button2 = Button()
        button2.attr_class = "Button"
        button2.attr_editor_newclass = False
        button2.css_height = "30px"
        button2.css_order = "139949326839040"
        button2.css_position = "static"
        button2.css_top = "20px"
        button2.css_width = "100px"
        button2.text = "button"
        button2.variable_name = "button2"
        vbox0.append(button2,'button2')
        button3 = Button()
        button3.attr_class = "Button"
        button3.attr_editor_newclass = False
        button3.css_height = "30px"
        button3.css_order = "139949344362016"
        button3.css_position = "static"
        button3.css_top = "20px"
        button3.css_width = "100px"
        button3.text = "button"
        button3.variable_name = "button3"
        vbox0.append(button3,'button3')
        hbox0.append(vbox0,'vbox0')
        vbox1 = VBox()
        vbox1.attr_class = "VBox"
        vbox1.attr_editor_newclass = False
        vbox1.css_align_items = "center"
        vbox1.css_display = "flex"
        vbox1.css_flex_direction = "column"
        vbox1.css_height = "250px"
        vbox1.css_justify_content = "space-around"
        vbox1.css_order = "139949328041920"
        vbox1.css_position = "static"
        vbox1.css_top = "20px"
        vbox1.css_width = "250px"
        vbox1.variable_name = "vbox1"
        button4 = Button()
        button4.attr_class = "Button"
        button4.attr_editor_newclass = False
        button4.css_flex_direction = "row"
        button4.css_height = "30px"
        button4.css_order = "139949319292192"
        button4.css_position = "static"
        button4.css_top = "20px"
        button4.css_width = "100px"
        button4.text = "button"
        button4.variable_name = "button4"
        vbox1.append(button4,'button4')
        button5 = Button()
        button5.attr_class = "Button"
        button5.attr_editor_newclass = False
        button5.css_height = "30px"
        button5.css_order = "139949319063872"
        button5.css_position = "static"
        button5.css_top = "20px"
        button5.css_width = "100px"
        button5.text = "button"
        button5.variable_name = "button5"
        vbox1.append(button5,'button5')
        button6 = Button()
        button6.attr_class = "Button"
        button6.attr_editor_newclass = False
        button6.css_height = "30px"
        button6.css_order = "139949319249440"
        button6.css_position = "static"
        button6.css_top = "20px"
        button6.css_width = "100px"
        button6.text = "button"
        button6.variable_name = "button6"
        vbox1.append(button6,'button6')
        button7 = Button()
        button7.attr_class = "Button"
        button7.attr_editor_newclass = False
        button7.css_height = "30px"
        button7.css_order = "139949319249152"
        button7.css_position = "static"
        button7.css_top = "20px"
        button7.css_width = "100px"
        button7.text = "button"
        button7.variable_name = "button7"
        vbox1.append(button7,'button7')
        hbox0.append(vbox1,'vbox1')
        vbox2 = VBox()
        vbox2.attr_class = "VBox"
        vbox2.attr_editor_newclass = False
        vbox2.css_align_items = "center"
        vbox2.css_display = "flex"
        vbox2.css_flex_direction = "column"
        vbox2.css_height = "250px"
        vbox2.css_justify_content = "space-around"
        vbox2.css_order = "139949328158384"
        vbox2.css_position = "static"
        vbox2.css_top = "20px"
        vbox2.css_width = "250px"
        vbox2.variable_name = "vbox2"
        button8 = Button()
        button8.attr_class = "Button"
        button8.attr_editor_newclass = False
        button8.css_height = "30px"
        button8.css_order = "139949330661088"
        button8.css_position = "static"
        button8.css_top = "20px"
        button8.css_width = "100px"
        button8.text = "button"
        button8.variable_name = "button8"
        vbox2.append(button8,'button8')
        button9 = Button()
        button9.attr_class = "Button"
        button9.attr_editor_newclass = False
        button9.css_height = "30px"
        button9.css_order = "139949344341632"
        button9.css_position = "static"
        button9.css_top = "20px"
        button9.css_width = "100px"
        button9.text = "button"
        button9.variable_name = "button9"
        vbox2.append(button9,'button9')
        button10 = Button()
        button10.attr_class = "Button"
        button10.attr_editor_newclass = False
        button10.css_font_size = "-8px"
        button10.css_height = "30px"
        button10.css_order = "139949329278816"
        button10.css_position = "static"
        button10.css_top = "20px"
        button10.css_width = "100px"
        button10.text = "button"
        button10.variable_name = "button10"
        vbox2.append(button10,'button10')
        button11 = Button()
        button11.attr_class = "Button"
        button11.attr_editor_newclass = False
        button11.css_height = "30px"
        button11.css_order = "139949312654592"
        button11.css_position = "static"
        button11.css_top = "20px"
        button11.css_width = "100px"
        button11.text = "button"
        button11.variable_name = "button11"
        vbox2.append(button11,'button11')
        hbox0.append(vbox2,'vbox2')
        self.append(hbox0,'hbox0')
        
        pass

    def userInit(self, *args, **kwargs):
        self.shownInMenu = 'My Menu Name'
        self.menuTitle = 'My View Name'

    def updateView(self):
        # Here you can update the view if it needs updates
        pass
