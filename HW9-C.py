n = input().strip()
orig_n = n
pass_count = 1

while True:
    digit_sum = sum(int(d) for d in n)
    print(f"Pass {pass_count} : {digit_sum}")
    if digit_sum <= 9:
        break
    n = str(digit_sum)
    pass_count += 1

print(f"Digital Root of {orig_n} : {digit_sum}")
