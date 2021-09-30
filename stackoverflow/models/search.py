from abc import ABC, abstractmethod


class SearchStrategy(ABC):
    @abstractmethod
    def search_question(self):
        pass

# implement class based on text string text