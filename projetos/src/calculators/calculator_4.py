from typing import Dict, List
from flask import request as FlaskRequest, jsonify

class Calculator4:
  
  def calculate(self, request: FlaskRequest) -> Dict:
    body = request.json
    numbers = self.__validate_body(body)

    if numbers is None:
      return jsonify({"error": "Body mal formatado! A chave 'numbers' é obrigatória."}), 400

    average = self.__calculate_average(numbers)
    response = self.__format_response(average)
    return response

  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise ValueError("Body mal formatado! A chave 'numbers' é obrigatória.")
    return body["numbers"]

  def __calculate_average(self, numbers: List[float]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0

  def __format_response(self, calc_result: float) -> Dict:
    return {
      "data": {
        "Calculator": 4,
        "result": round(calc_result, 2)
      }
    }
