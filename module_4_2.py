def test_function():
    def inner_function():
        print('Я в области видимости test function')
    inner_function()
inner_function()

