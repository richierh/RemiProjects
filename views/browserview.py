import remi.gui as gui
from remi import start,App


class MyApp(App):


    def __init__(self,*args):
        super().__init__(*args)

    def main(self):
        verticalContainer = gui.Container(width=540, margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})

        horizontalContainer = gui.Container(width='100%', layout_orientation=gui.Container.LAYOUT_HORIZONTAL, margin='0px', style={'display': 'block', 'overflow': 'auto'})
        


        menu = gui.Menu(width='100%', height='30px')
        m1 = gui.MenuItem('Rezky', width=100, height=30)
        m2 = gui.MenuItem('View', width=100, height=30)
        # m2.onclick.do(self.menu_view_clicked)
        m11 = gui.MenuItem('Save', width=100, height=30)
        m12 = gui.MenuItem('Open', width=100, height=30)
        # m12.onclick.do(self.menu_open_clicked)
        m111 = gui.MenuItem('Save', width=100, height=30)
        # m111.onclick.do(self.menu_save_clicked)
        m112 = gui.MenuItem('Save as', width=100, height=30)
        # m112.onclick.do(self.menu_saveas_clicked)
        m3 = gui.MenuItem('Dialog', width=100, height=30)
        # m3.onclick.do(self.menu_dialog_clicked)

        menu.append([m1, m2, m3])
        m1.append([m11, m12])
        m11.append([m111, m112])

        menubar = gui.MenuBar(width='100%', height='30px')
        menubar.append(menu)
        verticalContainer.append([menubar, horizontalContainer])


        return verticalContainer



if __name__=="__main__":
    start(MyApp, debug=True, address='0.0.0.0', port=8081, start_browser=True, multiple_instance=True)