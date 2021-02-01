import logging
from plyer.utils import platform
from plyer import notification
from win10toast import ToastNotifier 

from .tools import logAndExit

logger = logging.getLogger('cricNotifier')

def sendNotification(header, message):

    if platform == 'win':
        toastNotifier = ToastNotifier()
        try:
            toastNotifier.show_toast(
                title=header, 
                msg = message, 
                duration = 20,
                icon_path ='static/icon/cricNotifier.ico', 
                threaded=True
            )
        except Exception as e:
            logAndExit()
    else:
        try:
            notification.notify(
                title=header,
                message=message,
                app_name="cricNotifier",
                timeout=20,
                toast=False,
                app_icon='static/icon/cricNotifier.png'
            )
        except Exception as e:
            logAndExit()