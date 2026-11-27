
from typing import Callable
from functools import wraps

def update_state(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.state.next_question()
        return result
    return wrapper

class FormState:
    def __init__(self, current_question: int = 1):
        self._current_question = current_question
        self._default_state = current_question

    @property
    def current_question(self):
        return self._current_question
    
    def previous_question(self, back_number = 1):
        self._current_question -= back_number

    def next_question(self, forward_number = 1):
        self._current_question += forward_number
    
    def clear(self):
        self._current_question = self._default_state

class Form:
    def __init__(self, question_identifier, next_page, submit, form_state = FormState()):
        self.form_state = form_state
        self.question_identifier = question_identifier
        self.next_page = next_page
        self.submit = submit
    