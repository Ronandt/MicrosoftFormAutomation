import abc
from form_filler import BaseFormFiller
import rpa
class AbstractMicrosoftFormFiller(BaseFormFiller):
    @abc.abstractmethod
    def fill_radio(self) -> None:
        return None
    
    @abc.abstractmethod
    def fill_input(self,  input: str) -> None:
        return None
    
    @abc.abstractmethod
    def fill_rating(self) -> None:
        return None
    
    @abc.abstractmethod
    def next_page(self) -> None:
        return None
    
    

