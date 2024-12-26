class MyClass:

  def method_1(self) -> None:
    print('method 1')
    self.__method_2()

  def __method_2(self) -> None:
    print('method 2')

  def __verify_registry(self) -> None:
    print('Verify registry')

obj = MyClass()
obj.method_1()