
# -*- coding: utf-8 -*-

from editor.editor import *
from remi.gui import *
from remi import start, App


class untitled(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        container0 = Container()
        container0.attr_class = "Container"
        container0.attr_editor_newclass = False
        container0.css_height = "250px"
        container0.css_left = "20px"
        container0.css_position = "absolute"
        container0.css_top = "20px"
        container0.css_width = "250px"
        container0.variable_name = "container0"
        link0 = Link()
        link0.attr_class = "Link"
        link0.attr_editor_newclass = False
        link0.attr_href = ""
        link0.css_height = "30px"
        link0.css_left = "15.0px"
        link0.css_position = "absolute"
        link0.css_top = "15.0px"
        link0.css_width = "100px"
        link0.text = "link"
        link0.variable_name = "link0"
        container0.append(link0,'link0')
        hbox0 = HBox()
        hbox0.attr_class = "HBox"
        hbox0.attr_editor_newclass = False
        hbox0.css_align_items = "center"
        hbox0.css_display = "flex"
        hbox0.css_flex_direction = "row"
        hbox0.css_height = "250px"
        hbox0.css_justify_content = "space-around"
        hbox0.css_left = "20px"
        hbox0.css_position = "absolute"
        hbox0.css_top = "20px"
        hbox0.css_width = "250px"
        hbox0.variable_name = "hbox0"
        container0.append(hbox0,'hbox0')
        

        self.container0 = container0
        return self.container0
    


#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
