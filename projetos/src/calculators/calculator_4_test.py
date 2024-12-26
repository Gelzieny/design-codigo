from flask import Flask
from typing import Dict
from pytest import raises

from calculators.calculator_4 import Calculator4

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest(body={"numbers": [10, 20, 2, 40]})
  calculator_4 = Calculator4()

  response = calculator_4.calculate(mock_request)

  assert "data" in response

  expected_result = (10 + 20 + 2 + 40) / 4 
  assert response['data']['result'] == expected_result

  assert response['data']['Calculator'] == 4

def test_calculate_with_body_error_calculator_4():
  mock_request = MockRequest(body={"something": 1})
  calculator_4 = Calculator4()

  with raises(ValueError) as excinfo:
    calculator_4.calculate(mock_request)

  assert str(excinfo.value) == "Body mal formatado! A chave 'numbers' é obrigatória."