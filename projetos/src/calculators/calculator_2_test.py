from calculators.calculator_2 import Calculator2
from typing import Dict
from pytest import raises

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest(body={"number": [2.12, 4.63, 1.32, 1.23]})
  calculator_2 = Calculator2()

  response = calculator_2.calculate(mock_request)

  assert "data" in response
  assert "Calculator" in response["data"]
  assert "result" in response["data"]

  assert response["data"]["result"] == 14.25
  assert response["data"]["Calculator"] == 1
