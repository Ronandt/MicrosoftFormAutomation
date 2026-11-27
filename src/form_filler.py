import abc
import rpa
class BaseFormFiller(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def submit_form(self) -> None:
        return None

