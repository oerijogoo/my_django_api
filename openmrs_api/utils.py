def luhn_check_digit(number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10

def generate_identifier(base_identifier):
    check_digit = luhn_check_digit(base_identifier)
    return f"{base_identifier}{check_digit}"
