import doctest
from abc import ABC, abstractmethod


class Table(ABC):
    def __init__(self, material: str, length: float, width: float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал стола
        :param length: Длина стола
        :param width: Ширина стола

        Примеры:
        >>> table = ConcreteTable('wood', 1.5, 0.8)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.material = material
        self.length = length
        self.width = width

    @abstractmethod
    def assemble(self) -> None:
        """
        Собрать стол.

        Примеры:
        >>> table = ConcreteTable('wood', 1.5, 0.8)
        >>> table.assemble()
        """
        ...

    @abstractmethod
    def disassemble(self) -> None:
        """
        Разобрать стол.

        Примеры:
        >>> table = ConcreteTable('wood', 1.5, 0.8)
        >>> table.disassemble()
        """
        ...

    @abstractmethod
    def polish(self, polish_material: str) -> None:
        """
        Отполировать стол с использованием указанного материала.

        :param polish_material: Материал, используемый для полировки

        Примеры:
        >>> table = ConcreteTable('wood', 1.5, 0.8)
        >>> table.polish('воск')
        """
        if not isinstance(polish_material, str):
            raise TypeError("Материал для полировки должен быть строкой")
        ...


class ConcreteTable(Table):
    def assemble(self) -> None:
        pass

    def disassemble(self) -> None:
        pass

    def polish(self, polish_material: str) -> None:
        pass


class Tree(ABC):
    def __init__(self, species: str, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param height: Высота дерева
        :param age: Возраст дерева

        Примеры:
        >>> tree = ConcreteTree('oak', 5.0, 10)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть неотрицательным целым числом")
        self.species = species
        self.height = height
        self.age = age

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Заставить дерево расти в течение определенного количества лет.

        :param years: Количество лет для роста

        Примеры:
        >>> tree = ConcreteTree('oak', 5.0, 10)
        >>> tree.grow(5)
        """
        if not isinstance(years, int) or years <= 0:
            raise ValueError("Количество лет должно быть положительным целым числом")
        ...

    @abstractmethod
    def shed_leaves(self) -> None:
        """
        Заставить дерево сбросить листья.

        Примеры:
        >>> tree = ConcreteTree('oak', 5.0, 10)
        >>> tree.shed_leaves()
        """
        ...

    @abstractmethod
    def photosynthesize(self) -> None:
        """
        Заставить дерево проводить фотосинтез.

        Примеры:
        >>> tree = ConcreteTree('oak', 5.0, 10)
        >>> tree.photosynthesize()
        """
        ...


class ConcreteTree(Tree):
    def grow(self, years: int) -> None:
        pass

    def shed_leaves(self) -> None:
        pass

    def photosynthesize(self) -> None:
        pass


class Book(ABC):
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = ConcreteBook('1984', 'George Orwell', 328)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self.title = title
        self.author = author
        self.pages = pages

    @abstractmethod
    def read(self, page: int) -> str:
        """
        Прочитать определенную страницу книги.

        :param page: Номер страницы, которую нужно прочитать

        :return: Текст на странице

        Примеры:
        >>> book = ConcreteBook('1984', 'George Orwell', 328)
        >>> book.read(5)
        'Текст на странице 5'
        """
        if not isinstance(page, int) or page <= 0 or page > self.pages:
            raise ValueError(
                "Номер страницы должен быть положительным числом и не превышать количество страниц в книге")
        ...

    @abstractmethod
    def bookmark(self, page: int) -> None:
        """
        Добавить закладку на определенную страницу книги.

        :param page: Номер страницы для закладки

        Примеры:
        >>> book = ConcreteBook('1984', 'George Orwell', 328)
        >>> book.bookmark(100)
        """
        if not isinstance(page, int) or page <= 0 or page > self.pages:
            raise ValueError(
                "Номер страницы должен быть положительным числом и не превышать количество страниц в книге")
        ...

    @abstractmethod
    def get_summary(self) -> str:
        """
        Получить краткое содержание книги.

        :return: Краткое содержание книги

        Примеры:
        >>> book = ConcreteBook('1984', 'George Orwell', 328)
        >>> book.get_summary()
        'Краткое содержание книги'
        """
        ...


class ConcreteBook(Book):
    def read(self, page: int) -> str:
        return f"Текст на странице {page}"

    def bookmark(self, page: int) -> None:
        pass

    def get_summary(self) -> str:
        return "Краткое содержание книги"


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
