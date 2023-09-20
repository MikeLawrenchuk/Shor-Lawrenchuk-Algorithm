# The Shor-Lawrenchuk-Algorithm

The "Shor-Lawrenchuk-Algorithm" is a Python-based tool designed to process large numbers. It performs primality tests, factorization, and outputs results to a timestamped CSV file.

## Description

This program is tailored to handle large numbers efficiently. It offers the following features:

- **Primality Testing**: The algorithm uses the Miller-Rabin test to determine if the last 'n' digits of a number are prime.
- **Factorization**: If the last 'n' digits aren't prime, the Pollard's rho algorithm is employed to factor them.
- **CSV Output**: The processed results, including the number of digits, the extracted digits, and their factors (or an indication of their primality), are saved to a CSV file.

## Usage

1. Import the necessary modules.
2. Define the number and the range of last digits to process.
3. Call the `save_factors_to_csv` function with the number and the range as arguments.

```python
# Example:
number = 412023436986659543855531365332575948179811699844327982845455626433876445565248426198098870423161841879261420247188869492560931776375033421130982397485150944909106910269861031862704114880866970564902903653658867433731720813104105190864254793282601391257624033946373269391
n_list = list(range(10, 51, 5))
save_factors_to_csv(number, n_list)
