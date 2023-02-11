from .atri import Atri
from fastapi import Request, Response
from atri_utils import *
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def set_data(at: Atri, data):
    for i in range(1, 6):
        instance: at.Flex13.__class__ = getattr(at, f'Flex13{i}')
        instance.styles.display = 'none'
    for i in range(1, int(data['rating']) + 1):
        instance: at.Flex13.__class__ = getattr(at, f'Flex13{i}')
        instance.styles.display = 'flex'
   


def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    pass


def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """


def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """