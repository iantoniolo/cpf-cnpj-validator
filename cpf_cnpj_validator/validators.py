import re

def calculate_digit(cpf, weights):
    total = sum(cpf[i] * weights[i] for i in range(len(weights)))
    remainder = total % 11
    return 0 if remainder < 2 else 11 - remainder

def validate_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    cpf_digits = [int(digit) for digit in cpf[:9]]
    digit_1 = calculate_digit(cpf_digits, list(range(10, 1, -1)))

    if cpf_digits.append(digit_1) and cpf[:10] == ''.join(map(str, cpf_digits)):
        cpf_digits = [int(digit) for digit in cpf]
        digit_2 = calculate_digit(cpf_digits[:10], list(range(11, 1, -1)))
        return cpf_digits.append(digit_2) and cpf == ''.join(map(str, cpf_digits))

    return False

def validate_cnpj(cnpj):
    cnpj = re.sub(r'[^0-9]', '', cnpj)

    if len(cnpj) != 14 or len(set(cnpj)) == 1:
        return False

    cnpj_digits = [int(digit) for digit in cnpj[:12]]
    digit_1 = calculate_digit(cnpj_digits, list(range(5, 1, -1)) + list(range(9, 1, -1)))

    if cnpj_digits.append(digit_1) and cnpj[:13] == ''.join(map(str, cnpj_digits)):
        cnpj_digits = [int(digit) for digit in cnpj]
        digit_2 = calculate_digit(cnpj_digits[:13], list(range(6, 1, -1)) + list(range(9, 1, -1)))
        return cnpj_digits.append(digit_2) and cnpj == ''.join(map(str, cnpj_digits))

    return False
