from sys import platform
if platform == "win32":
    from os import environ
    environ["KIVY_GL_BACKEND"] = "angle_sdl2"
from kivy.core.window import Window
import os
from time import sleep
from kivy.factory import Factory  # NOQA
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.config import Config
from multiprocessing.dummy import Process


kv = '''
Button:
    text: 'push me!'
'''


class ServiceApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def on_start(self):
        from kivy import platform
        if platform == "android":
            self.start_service()

    @staticmethod
    def start_service():
        from jnius import autoclass
        service = autoclass("org.mindset.codered.ServiceCodered")
        mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
        service.start(mActivity, "")
        return service


if __name__ == '__main__':
    ServiceApp().run()
