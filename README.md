# Prime Factorization in Python

A small, interactive Python program for beginners. Enter a whole number, and the
program tries to write it as the product of **exactly two prime numbers**.

For example, `15 = 3 x 5` and `49 = 7 x 7`.

Although this repository is named `qiskit-shor`, the current program uses a
classical search. It does not use Qiskit, quantum computing, or Shor's algorithm.

## 1. Install Python

You need **Python 3**. Download it from [python.org](https://www.python.org/downloads/)
and follow the installer instructions.

Open a terminal (PowerShell on Windows, Terminal on macOS, or your Linux terminal)
and check that Python is available:

**Windows:**

```powershell
py --version
```

**macOS / Linux:**

```bash
python3 --version
```

You should see a version beginning with `Python 3`.

No extra packages are needed. The program uses only built-in Python features, so
there is no `requirements.txt` and you do not need to run `pip install`.

## 2. Download the project

On [the repository page](https://github.com/zhangl64/qiskit-shor), select
**Code → Download ZIP**, then extract the ZIP file.

If you already have Git installed, you can instead run:

```bash
git clone https://github.com/zhangl64/qiskit-shor.git
```

In your terminal, use `cd` to enter the downloaded folder containing
`prime_factorization.py`. For example, if you extracted the ZIP into your
Downloads folder:

```bash
cd ~/Downloads/qiskit-shor-main
```

Replace that path with the actual location of your folder. If you used Git,
the folder is named `qiskit-shor` instead of `qiskit-shor-main`.

## 3. Run the program

**Windows:**

```powershell
py prime_factorization.py
```

**macOS / Linux:**

```bash
python3 prime_factorization.py
```

When the prompt appears, type a number such as `15` and press **Enter**:

```text
Enter an integer to factorize: 15
15 = 3 x 5
```

The program handles one number per run. Run the same command again to try another
number. Start with small numbers; the search can be slow for large inputs.

## More examples

| Input | Result | Explanation |
| --- | --- | --- |
| `21` | `21 = 3 x 7` | Both factors are prime. |
| `49` | `49 = 7 x 7` | The two prime factors can be equal. |
| `13` | `13 is a prime number and cannot be factorized.` | A prime has no pair of prime factors. |
| `12` | `12 cannot be factorized into two prime numbers.` | Its prime factorization is `2 x 2 x 3`, which has three factors. |
| `1`, `0`, or a negative number | Cannot be factorized into two prime numbers. | Try a positive integer greater than 1. |
| `hello` or `15.0` | `Please enter a valid integer.` | Enter a whole number, such as `15`. |

## How the code works

Open `prime_factorization.py` in a text editor to follow along:

1. `is_prime(n)` checks whether a number is prime by looking for divisors up to
   its square root.
2. `factorize(n)` searches for a prime divisor and checks whether the other
   factor is also prime.
3. The code at the bottom reads your input and prints the result.

## Troubleshooting

- **Python command not found:** Finish installing Python, then close and reopen
  your terminal. On Windows, try `python` if `py` is unavailable.
- **Cannot open the file / file not found:** Make sure your terminal is in the
  folder containing `prime_factorization.py`. Use `dir` on Windows or `ls` on
  macOS/Linux to list the files in your current folder.
- **You see `>>>`:** You are inside Python's interactive shell. Type `exit()` and
  press Enter, then run the command from step 3 in your terminal.
- **The program takes too long:** Press **Ctrl+C** to stop it, then try a smaller
  number.

## License

This project is licensed under the [Apache License 2.0](LICENSE).
