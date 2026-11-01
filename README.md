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

## Classroom challenge: whose laptop finishes first?

During the lecture, everyone will factorize the **same number using the same
program** and compare completion times. The fastest correct result wins!

Run the commands below from the folder containing `prime_factorization.py`.
They supply the input automatically, so the timer does not include the time you
spend typing a number at the prompt. Enter numbers **without commas**.

### macOS / Linux

```bash
echo 50000167000051 | /usr/bin/time -p python3 prime_factorization.py
```

The output will include the factors followed by timing information, for example:

```text
Enter an integer to factorize: 50000167000051 = 1000003 x 50000017
real 4.25
user 4.18
sys 0.02
```

These times are illustrative; yours will differ. Record **`real`**, the elapsed
time in seconds. `user` and `sys` measure CPU time and are not the competition
score. The `-p` option gives the same timing labels on macOS and Linux.

### Windows PowerShell (recommended on Windows)

Open **PowerShell** or a PowerShell tab in Windows Terminal, then run:

```powershell
Measure-Command { "50000167000051" | py prime_factorization.py | Out-Default } | Select-Object TotalSeconds
```

The factors appear first, followed by **`TotalSeconds`**, the elapsed time in
seconds. `Out-Default` makes the program's output visible while it is being timed.
If you normally use `python` instead of `py`, replace `py` in this command.

### Windows Command Prompt (cmd.exe)

You can invoke the same PowerShell timer from Command Prompt:

```bat
powershell -NoProfile -Command "Measure-Command { '50000167000051' | py prime_factorization.py | Out-Default } | Select-Object TotalSeconds"
```

Record **`TotalSeconds`**. The Command Prompt command `time /t` only displays the
current clock time; use the timer above to get elapsed seconds automatically.

### Challenge rounds

Replace `50000167000051` in your command with the number for the current round:

| Round | Input (copy without commas) | Expected prime factors |
| --- | --- | --- |
| Warm-up | `15` | `3 x 5` |
| 1 | `50000167000051` | `1000003 x 50000017` |
| 2 | `167700407018119` | `3354007 x 50000017` |
| Take-home challenge | `6763011116220131` | `68778473 x 98330347` |

The take-home challenge may run for a long time. Press **Ctrl+C** to stop a run
if needed; an interrupted run does not count as a completed result.

For a more consistent comparison:

1. Use the same input and unmodified script for each round.
2. Plug in your laptop and close other busy applications.
3. Run each round three times and report the middle time (the median), along with
   your laptop model, operating system, and Python version (`py --version` on
   Windows or `python3 --version` on macOS/Linux).
4. Confirm that your output contains the expected factors before submitting a time.

These commands time the whole Python run, including startup. Results reflect the
laptop, Python version, and system load. The warm-up mostly measures startup;
the larger rounds make the factorization work more noticeable.

Timing command references: [GNU Time](https://www.gnu.org/software/time/manual/)
and [PowerShell Measure-Command](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/measure-command).

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
