def sum_numbers(text: str) -> int:
    result = 0
    for i in text.split(" "):
        if i.isnumeric():
            result += int(i)
    return result

print(sum_numbers("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"))