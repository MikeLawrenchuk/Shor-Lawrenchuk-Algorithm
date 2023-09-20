import csv
import datetime
import random
import math

def miller_rabin_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n) 
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def pollards_rho(n, max_iterations=10000):
    if n % 2 == 0:
        return 2
    x = random.randint(1, n-1)
    y = x
    c = random.randint(1, n-1)
    g = 1
    iterations = 0

    while g == 1 and iterations < max_iterations:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        g = math.gcd(abs(x - y), n)
        iterations += 1
        
    return g if g != 1 else n

def factorize(n):
    factors = []
    while n > 1:
        f = pollards_rho(n)
        while n % f == 0:
            factors.append(f)
            n //= f
    return factors
def save_factors_to_csv(number, n_list):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"factored_results_{timestamp}.csv"
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header
        writer.writerow(["Number of Digits", "Last N Digits", "Factors (or 'Prime')"])
        
        for n in n_list:
            last_n_digits = int(str(number)[-n:])
            if miller_rabin_test(last_n_digits):
                writer.writerow([n, last_n_digits, "Prime"])
            else:
                factors = factorize(last_n_digits)
                writer.writerow([n, last_n_digits, ', '.join(map(str, factors))])
    
    print(f"File saved as {filename}")
    return filename


# Number and n_list
number = 412023436986659543855531365332575948179811699844327982845455626433876445565248426198098870423161841879261420247188869492560931776375033421130982397485150944909106910269861031862704114880866970564902903653658867433731720813104105190864254793282601391257624033946373269391
n_list = list(range(10, 51, 5))

# Save the factored results to a CSV file
save_factors_to_csv(number, n_list)
