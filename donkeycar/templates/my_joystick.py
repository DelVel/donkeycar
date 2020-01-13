
from donkeycar.parts.controller import Joystick, JoystickController


class MyJoystick(Joystick):
    #An interface to a physical joystick available at /dev/input/js0
    def __init__(self, *args, **kwargs):
        super(MyJoystick, self).__init__(*args, **kwargs)


        self.button_names = {
            0x136 : 'LB',
            0x137 : 'RB',
            0x134 : 'Y',
            0x131 : 'B',
            0x130 : 'A',
            0x133 : 'X',
            0x13a : 'BACK',
            0x13b : 'START',
            0x13c : 'HOME',
            0x13d : 'LSB',
            0x13e : 'RSB',
        }


        self.axis_names = {
            0x1 : 'LVERT',
            0x0 : 'LHORIZ',
            0x4 : 'RVERT',
            0x3 : 'RHORIZ',
            0x2 : 'LT',
            0x5 : 'RT',
            0x10 : 'CROSSHORIZ',
            0x11 : 'CROSSVERT',
        }



class MyJoystickController(JoystickController):
    #A Controller object that maps inputs to actions
    def __init__(self, *args, **kwargs):
        super(MyJoystickController, self).__init__(*args, **kwargs)


    def init_js(self):
        #attempt to init joystick
        try:
            self.js = MyJoystick(self.dev_fn)
            self.js.init()
        except FileNotFoundError:
            print(self.dev_fn, "not found.")
            self.js = None
        return self.js is not None


    def init_trigger_maps(self):
        #init set of mapping from buttons to function calls

        self.button_down_trigger_map = {
            'A' : self.erase_last_N_records,
            'B' : self.emergency_stop,
            'LB' : self.toggle_mode,
        }


        self.axis_trigger_map = {
            'RHORIZ' : self.set_steering,
            'LVERT' : self.set_throttle,
        }


