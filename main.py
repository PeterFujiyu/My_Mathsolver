import re
from arithmetic.main import evaluate_expression, add_spaces
from equation.main import main as solve_equation

def main():
    expression = input("请输入一个四则运算表达式或方程，例如 '3 + 5 * (2 - 8)' 或 '30x^2 + 15x - 560 = 0': ")

    if '=' in expression:
        # 处理方程
        try:
            result = solve_equation(expression)
            print(f"方程的结果是: {result}")
        except Exception as e:
            print(f"解析方程时出错: {e}")
    else:
        # 处理四则运算表达式
        try:
            expression_with_spaces = add_spaces(expression)
            result = evaluate_expression(expression_with_spaces)
            result_str = str(result)
            print(f"{expression_with_spaces} 等于 {result_str}")
        except Exception as e:
            print(f"解析表达式时出错: {e}")

if __name__ == "__main__" or __name__ == "init":
    main()
