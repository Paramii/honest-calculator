msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_list = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

operations_list = ["+", "-", "*", "/"]

memory = 0


def is_one_digit(n):
    if n > -10 and n < 10 and n.is_integer():
        return True
    else:
        return False


def check(n1, n2, op):
    msg = ""
    if is_one_digit(n1) and is_one_digit(n2):
        msg = msg + msg_6
    if (n1 == 1 or n2 == 1) and op == "*":
        msg = msg + msg_7
    if (n1 == 0 or n2 == 0) and not (op == "/"):
        msg = msg + msg_8
    if not (msg == ""):
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)
    calc = input()
    x, operation, y = calc.split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory
    else:
        try:
            x = float(x)
            y = float(y)
        except:
            print(msg_1)
            continue

    if operation not in operations_list:
        print(msg_2)
        continue
    else:
        check(x, y, operation)
        if operation == "+":
            result = x + y
        elif operation == "-":
            result = x - y
        elif operation == "*":
            result = x * y
        elif operation == "/" and not (y == 0):
            result = x / y
        else:
            print(msg_3)
            continue
        print(result)
        while True:
            store_result = input(msg_4)
            if store_result == "y":
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        recheck = input(msg_list[msg_index])
                        if recheck == "y":
                            if msg_index < 12:
                                msg_index += 1
                                continue
                            else:
                                memory = result
                                break
                        elif msg_index > 12 or recheck == "n":
                            break
                        else:
                            continue
                else:
                    memory = result
            elif not (store_result == "n"):
                continue
            while True:
                continue_cal = input(msg_5)
                if continue_cal == "n":
                    break
                elif continue_cal == "y":
                    break
                else:
                    continue
            break
    if continue_cal == "y":
        continue
    else:
        break
