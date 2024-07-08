import re
from decimal import Decimal, getcontext

# 设置浮点数运算的精度
getcontext().prec = 28


def evaluate_expression(expression):
    def parse_expression(expr):
        # 将表达式中的空格去掉
        expr = re.sub(r'\s+', '', expr)

        # 处理括号中的表达式
        while '(' in expr:
            expr = re.sub(r'\([^()]*\)', lambda x: str(evaluate_simple_expression(x.group()[1:-1])), expr)

        return evaluate_simple_expression(expr)

    def evaluate_simple_expression(expr):
        # 替换表达式中的运算符，避免使用内置eval，改为Decimal运算
        expr = re.sub(r'([\d.]+)', r'Decimal("\1")', expr)
        expr = re.sub(r'([*/+-])', r' \1 ', expr)
        # 使用eval进行计算，但只允许Decimal和运算符
        result = eval(expr)
        return result

    def format_result(result):
        if result == result.to_integral_value():
            return int(result)
        return float(result)

    result = parse_expression(expression)
    return format_result(result)


def add_spaces(expression):
    # 在运算符前后添加空格
    expression = re.sub(r'(\d)\s*([*/+-])\s*(\d)', r'\1 \2 \3', expression)
    return expression


def number_to_words(num):
    number_words = {
        '0': '零', '1': '一', '2': '二', '3': '三', '4': '四',
        '5': '五', '6': '六', '7': '七', '8': '八', '9': '九',
        '.': '点'
    }
    return ''.join(number_words.get(digit, digit) for digit in str(num))


def expression_to_words(expression):
    words_operators = {
        '+': '加', '-': '减', '*': '乘', '/': '除', '(': '左括号', ')': '右括号'
    }
    for operator, words_operator in words_operators.items():
        expression = expression.replace(operator, words_operator)
    return expression

if __name__ == '__main__':
    # 示例使用
    expression = input("请输入一个四则运算表达式，例如 '3 + 5 * (2 - 8)': ")

    try:
        expression_with_spaces = add_spaces(expression)
        result = evaluate_expression(expression_with_spaces)
        result_str = str(result)
        print(f"{expression_with_spaces} = {result_str}")
    except Exception as e:
        print(f"解析表达式时出错: {e}")
