import hashlib


def hash160(data) -> str:
    
    sha256_bytes = hashlib.sha256(str(data).encode('utf-8')).digest()
    try:
        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(sha256_bytes)
        return ripemd160.hexdigest()
    except ValueError:
        return hashlib.sha256(sha256_bytes).hexdigest()[:40]


def parse_input(raw_str: str) -> list:
    cleaned = raw_str.strip().strip("[]").replace(",", " ")
    return cleaned.split()


def run_script(tokens: list) -> bool:
    stack = []

    for token in tokens:
        t_str = str(token).strip("'\"")

        if t_str == "OP_ADD":
            if len(stack) < 2:
                return False
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a + b)

        elif t_str == "OP_EQUAL":
            if len(stack) < 2:
                return False
            b = stack.pop()
            a = stack.pop()
            stack.append(a == b)

        elif t_str == "OP_DUP":
            if len(stack) < 1:
                return False
            stack.append(stack[-1])

        elif t_str == "OP_HASH160":
            if len(stack) < 1:
                return False
            val = stack.pop()
            stack.append(hash160(val))

        elif t_str == "OP_EQUALVERIFY":
            if len(stack) < 2:
                return False
            b = stack.pop()
            a = stack.pop()
            return a == b

        else:
            if t_str.lstrip('-').isdigit():
                stack.append(int(t_str))
            else:
                stack.append(t_str)

    return len(stack) > 0 and stack[-1] is True


if __name__ == "__main__":
    raw_script = input("Nhập chuỗi lệnh script: ")
    tokens = parse_input(raw_script)
    print(run_script(tokens))