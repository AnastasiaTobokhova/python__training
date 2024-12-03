def introspection_info(obj):
    """
    Проводит интроспекцию объекта и возвращает информацию о нем.

    :param obj: Объект для анализа
    :return: Словарь с информацией об объекте
    """
    # Определяем тип объекта
    obj_type = type(obj).__name__

    # Список всех атрибутов объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Список всех методов объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Модуль, к которому принадлежит объект
    module = getattr(obj, "__module__", "built-in")

    # Дополнительные свойства
    doc = getattr(obj, "__doc__", "No documentation available")

    return {
        "type": obj_type,
        "attributes": attributes,
        "methods": methods,
        "module": module,
        "doc": doc
    }



number_info = introspection_info(42)
print(number_info)


class MyClass:
    """Пример пользовательского класса"""

    def __init__(self, value):
        self.value = value

    def my_method(self):
        """Пример метода"""
        return f"Value is {self.value}"


# Пример с экземпляром пользовательского класса
my_object = MyClass(10)
class_info = introspection_info(my_object)
print(class_info)
