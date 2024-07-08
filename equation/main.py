import re
import math
import time

def type_like_output(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def parse_and_standardize_equation(equation):
    type_like_output("开始解析方程...")
    # 去掉空格
    equation = equation.replace(" ", "")
    type_like_output(f"去掉空格后的方程：{equation}")

    # 查找等号位置
    if '=' in equation:
        left_side, right_side = equation.split('=')
    else:
        raise ValueError("方程格式不正确")

    type_like_output(f"左边：{left_side}, 右边：{right_side}")

    # 将右侧移到左侧
    right_side = right_side.replace("-", "+-")
    left_side = left_side + "+-" + right_side
    type_like_output(f"移项后方程：{left_side} = 0")

    # 提取所有项
    terms = re.findall(r'[+-]?\d*\.?\d*x\^2|[+-]?\d*\.?\d*x|[+-]?\d*\.?\d+', left_side)
    type_like_output(f"解析出方程项：{terms}")

    a, b, c = 0, 0, 0
    for term in terms:
        if 'x^2' in term:
            coeff = term.replace('x^2', '')
            a += float(coeff) if coeff not in ('', '+', '-') else 1.0 if coeff in ('', '+') else -1.0
        elif 'x' in term:
            coeff = term.replace('x', '')
            b += float(coeff) if coeff not in ('', '+', '-') else 1.0 if coeff in ('', '+') else -1.0
        else:
            c += float(term)

    type_like_output(f"系数 a = {a}, b = {b}, c = {c}")
    return a, b, c

def solve_quadratic(a, b, c):
    type_like_output("这是一个一元二次方程。")
    type_like_output("二次方程的一般形式为：ax^2 + bx + c = 0")
    type_like_output(f"其中 a = {a}, b = {b}, c = {c}")

    # 列出求解公式
    type_like_output("求根公式为：\nx = (-b ± √(b² - 4ac))\n——————————————————————\n         2a")

    # 计算判别式
    discriminant = b ** 2 - 4 * a * c
    type_like_output(f"计算判别式：Δ = b² - 4ac = {b}² - 4 * {a} * {c} = {discriminant}")

    # 根据判别式的值判断方程的根的情况
    if discriminant > 0:
        type_like_output("因为 Δ > 0，所以方程有两个实数根。")
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        type_like_output(f"第一个根：x1 = (-{b} + √{discriminant}) / (2 * {a}) = {root1}")
        type_like_output(f"第二个根：x2 = (-{b} - √{discriminant}) / (2 * {a}) = {root2}")
        return root1, root2
    elif discriminant == 0:
        type_like_output("因为 Δ = 0，所以方程有一个实数根。")
        root = -b / (2 * a)
        type_like_output(f"唯一的根：x = -{b} / (2 * {a}) = {root}")
        return root,
    else:
        type_like_output("因为 Δ < 0，所以方程无实数根。")
        return None

def solve_linear(b, c):
    type_like_output("这是一个一元一次方程。")
    if b != 0:
        root = -c / b
        type_like_output(f"方程有一个实根：x = -{c} / {b} = {root}")
        return root
    elif c == 0:
        type_like_output("方程有无穷多个解。")
        return "无穷多个解"
    else:
        type_like_output("方程无解。")
        return "无解"

def solve_sqrt(c):
    if c >= 0:
        root = math.sqrt(c)
        type_like_output(f"方程有一个实根：x = √{c} = {root}")
        return root
    else:
        type_like_output("方程无解。")
        return "无解"

def main(equation):
    try:
        a, b, c = parse_and_standardize_equation(equation)

        if a == 0 and b == 0 and c != 0:
            # 处理 sqrt(x) 形式的方程
            result = solve_sqrt(-c)
            return f"方程有一个实根: {result}"
        elif a == 0:
            # 一元一次方程
            result = solve_linear(b, c)
            if isinstance(result, str):
                return f"方程有{result}"
            else:
                return f"方程有一个实根: {result}"
        else:
            # 一元二次方程
            roots = solve_quadratic(a, b, c)
            if roots:
                if len(roots) == 1:
                    return f"方程有一个实根: {roots[0]}"
                else:
                    return f"方程有两个实根: {roots[0]} 和 {roots[1]}"
            else:
                return "方程无实数根"
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    equation = input("请输入方程：")
    result = main(equation)
    print(result)
