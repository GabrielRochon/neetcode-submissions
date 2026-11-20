class Solution:
    import math

    def evalRPN(self, tokens: list[str]) -> int:
        
        # On commence à peupler un stack avec les nombres. Lorsqu'un symbole est lu et qu'il y a deux nombres, on effectue l'opération sur ces nombres, et le résultat est remis dans le stack. À faire jusqu'à ce que tous les caractères soient lus
        
        operators_list = [ '+', '-', '*', '/' ]
        operators = set(operators_list)             # Pour regarder l'existence en O(1)

        operation_pile = []

        for token in tokens:

            if token not in operators:
                operation_pile.append(int(token))

            elif token in operators and len(operation_pile) >= 2:
                second_number = operation_pile.pop()
                first_number = operation_pile.pop()

                if token == '+':
                    operation_pile.append(first_number + second_number)

                elif token == '-':
                    operation_pile.append(first_number - second_number)

                elif token == '*':
                    operation_pile.append(first_number * second_number)

                elif token == '/':
                    float_result = first_number / second_number
                    if float_result < 0:
                        float_result = math.ceil(float_result)
                    elif float_result > 0:
                        float_result = math.floor(float_result)
                    operation_pile.append(int(float_result))
        
                else:
                    print("Invalid number: not expected.")
        
        return operation_pile.pop()
