from url import Url
import rpa
from typing import Callable
from form_state import update_state, FormState
from abstract_microsoft_form_filler import AbstractMicrosoftFormFiller


class MicrosoftFormFiller(AbstractMicrosoftFormFiller):
    SUBMIT = '//*[@data-automation-id="submitButton"]'
    NEXT = '//*[@data-automation-id="nextButton"]'

    def __init__(self, url: Url, turbo_mode: bool = True, chrome_browser: bool = True, headless=False, state = FormState()) -> None:

        if type(url) is not Url:
            raise TypeError("url argument is not a URL")
        elif type(turbo_mode) is not bool:
            raise TypeError("turbo_mode argument is not a bool")
        elif type(chrome_browser) is not bool:
            raise TypeError("chrome_browser argument is not a bool")
        elif(url.metadata.hostname.lower() != "forms.office.com"):
            raise ValueError("This is an invalid Microsoft Forms link")

        self.state = state 
        self.url = url.get_url
        rpa.init(turbo_mode=turbo_mode, chrome_browser=chrome_browser,
                 headless_mode=headless)
        rpa.url(self.url)

    @update_state
    def fill_radio(self, selection: int = 1) -> "MicrosoftFormFiller":
        if type(selection) is not int:
            raise TypeError("selection argument is not an integer")
        rpa.click(f'({self.__XPATH_INPUT_ID()})[{selection}]')
        return self

    @update_state
    def fill_input(self,  input: str) -> "MicrosoftFormFiller":
        if type(input) is not str:
            raise TypeError("input argument is not a str")
        rpa.type(self.__XPATH_INPUT_ID(), input)
        return self

    def skip(self, skipping_number: int = 1) -> "MicrosoftFormFiller":
        self.state.next_question(skipping_number)
        return self

    def submit_form(self) -> None:
        rpa.click(self.SUBMIT)
        rpa.wait(1)
        rpa.close()
        print("\033[94m" + "Form Submitted" + "\033[0m")

    def next_page(self) -> "MicrosoftFormFiller":
        rpa.click(self.NEXT)
        self.state.clear()

        return self

    def __XPATH_INPUT_ID(self) -> str:
        return f'//*[@id="question-list"]/div[{self.state.current_question}]//input'


# get form manager to manage state or form to represnt form position with pages etc
