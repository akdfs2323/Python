def validate_isbn(isbn, length):
    # ตรวจความยาวก่อน
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    # ตรวจสอบอักขระผิด
    if length == 10:
        # ตัวสุดท้ายเป็น X ได้
        if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
            print('Invalid character was found.')
            return
    else:
        if not isbn.isdigit():
            print('Invalid character was found.')
            return

    # แยกตัวเลขหลักกับ check digit
    main_digits = isbn[:length-1]
    given_check_digit = isbn[length-1]

    main_digits_list = [int(digit) for digit in main_digits]

    # คำนวณ check digit ที่ถูกต้อง
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # เปรียบเทียบ
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    if result == 10:
        return '0'
    else:
        return str(result)


def main():
    user_input = input('Enter ISBN and length: ')

    # ต้องมี comma
    if ',' not in user_input:
        print('Enter comma-separated values.')
        return

    values = user_input.split(',')

    # ต้องมี 2 ค่า
    if len(values) != 2 or values[1] == '':
        print('Enter comma-separated values.')
        return

    isbn = values[0]

    # length ต้องเป็นตัวเลข
    try:
        length = int(values[1])
    except:
        print('Length must be a number.')
        return

    # ต้องเป็น 10 หรือ 13 เท่านั้น
    if length != 10 and length != 13:
        print('Length should be 10 or 13.')
        return

    validate_isbn(isbn, length)


# main()