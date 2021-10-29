from abc import abstractmethod



class Adapter:

    @abstractmethod
    def get_fiction_title(self):
        pass

    @abstractmethod
    def get_fiction_chapter_list(self):
        pass

    @abstractmethod
    def get_fiction_chapter_content(self):
        pass

