# base class to build reusable utility actions. Actions are bits of code that perform some action usually against
# an API or some executable. The idea here is to make this as simple and abstract as possible

from abc import ABC


class AbstractAction(ABC):
    import abc

    @abc.abstractmethod
    def execute_template(self, template):
        """
         execute the action with the compiled template as an input
        :param template: compiled template
        :return: string
        """
        return

    @abc.abstractmethod
    def cleanup(self):
        """
        Perform any cleanup actions needed
        :return:
        """
        return




