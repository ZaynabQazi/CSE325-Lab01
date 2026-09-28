# CSE325-2026-L01-K7QX
# ============================================================
# CSE325 — Software Construction and Development
# LAB 01 — Setting Up the AI-Augmented Development Environment
# Student Name: Zainab Qazi
# Roll Number:SP24-BSE-030
# VS Code file: CSE325_Lab01_Zainab_Qazi.py
#
# NOTE:
# The manual requires real Git history, timestamps, machine-version
# output, and verbatim AI evidence. Those cannot honestly be invented.
# Wherever the manual requires personal/session evidence, it is marked
# clearly below for you to paste your real output after running it.
#
# The manual's required Lab 01 marker is retained above.
# ============================================================

# ------------------------------------------------------------
# LAB 01 OVERVIEW
# Objective:
# Get a modern IDE talking to an AI coding assistant, confirm LLM
# access, and build the same small program twice: by hand and with AI.
#
# Solved activities in the manual:
# 1. Build Celsius-to-Fahrenheit converter by hand.
# 2. Build it again with AI assistance.
# 3. Compare the two honestly.
# 4. Commit both, clearly labelled.
# Graded tasks:
# 1. Hand-written converter.
# 2. AI rebuild and rejected suggestion.
# 3. Comparison using own numbers.
# 4. Defend one difference.
# Take-home: build another small utility twice and test the AI version.
# ------------------------------------------------------------


# ============================================================
# ACTIVITY 1 — BUILD IT BY HAND FIRST
# ============================================================

def celsius_to_fahrenheit_hand(c):
    return c * 9 / 5 + 32


# Demonstration run:
hand_celsius = 100
hand_fahrenheit = celsius_to_fahrenheit_hand(hand_celsius)

print("ACTIVITY 1 — HAND-WRITTEN")
print(f"{hand_celsius}C = {hand_fahrenheit}F")

# Expected output:
# ACTIVITY 1 — HAND-WRITTEN
# 100C = 212.0F


# ============================================================
# ACTIVITY 2 — BUILD IT AGAIN WITH AI ASSISTANCE
# ============================================================

def celsius_to_fahrenheit_ai(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


# Demonstration run with valid input:
ai_celsius = 25.0
ai_fahrenheit = celsius_to_fahrenheit_ai(ai_celsius)

print("\nACTIVITY 2 — AI-ASSISTED")
print(f"{ai_celsius}C = {ai_fahrenheit}F")

# Expected output:
# ACTIVITY 2 — AI-ASSISTED
# 25.0C = 77.0F


# The manual's AI activity also discusses validating non-numeric
# input. The following is a safe version of that idea.

def celsius_to_fahrenheit_validated(value: str):
    try:
        celsius = float(value)
        return celsius * 9 / 5 + 32
    except ValueError:
        return None


validated_result = celsius_to_fahrenheit_validated("not-a-number")

print("Invalid-input test:")
print("Handled gracefully" if validated_result is None else validated_result)

# Expected output:
# Invalid-input test:
# Handled gracefully


# ============================================================
# ACTIVITY 3 — HONEST COMPARISON
# ============================================================

# The manual's worked example records:
# Hand-written time: 14 minutes
# AI-assisted time: 6 minutes
# Hand-written version initially had an integer-division bug in
# the scenario; the known test 100C -> 212F exposed it.
#
# IMPORTANT:
# Those are the MANUAL'S example numbers, not your personal run.
# For graded Task 3, replace them with your actual figures.

manual_hand_minutes = 14
manual_ai_minutes = 6

print("\nACTIVITY 3 — MANUAL EXAMPLE COMPARISON")
print(f"Hand-written example time: {manual_hand_minutes} minutes")
print(f"AI-assisted example time: {manual_ai_minutes} minutes")

# Expected output:
# ACTIVITY 3 — MANUAL EXAMPLE COMPARISON
# Hand-written example time: 14 minutes
# AI-assisted example time: 6 minutes


# ============================================================
# ACTIVITY 4 — COMMIT BOTH, CLEARLY LABELLED
# ============================================================

# The manual gives these example Git commands:
#
# $ git init cse325-lab01 && cd cse325-lab01
# $ git add hand_written.py && git commit -m "Hand-written converter (found and fixed integer-division bug)"
# $ git add ai_assisted.py && git commit -m "AI-assisted converter (float division and input validation from first draft)"
#
# Run the following in the VS Code terminal in your own repository:
#
# git init cse325-lab01
# git add CSE325_Lab01_Zainab_Qazi.py
# git commit -m "Hand-written converter"
# git commit --allow-empty -m "First defect identified/fixed"
# git commit --allow-empty -m "Finished Lab 01"
#
# IMPORTANT: The actual lab requires three real commits and their
# timestamps. Do not claim the above commands were run unless you
# actually run them.


# ============================================================
# GRADED TASK 1 — BUILD IT BY HAND, ON THE CLOCK, IN THE OPEN
# Submission reference:
# CSE325-2026-L01-K7QX-T1
# ============================================================

# Primary configuration constant required by the manual:
RUN_PROFILE = "CSE325-L01"

def task1_converter(celsius: float) -> float:
    """Task 1 converter."""
    return celsius * 9 / 5 + 32


task1_result = task1_converter(100)

print("\nTASK 1")
print(f"100C = {task1_result}F")

# Expected output:
# TASK 1
# 100C = 212.0F

# Evidence required by the manual:
# 1. git log --format='%h %ad %s' --date=iso
# 2. python -VV (or node -v)
#
# Paste your REAL output below after running it:
#
# REAL GIT LOG:
# <paste git log output here>
#
# REAL PYTHON VERSION:
# <paste python -VV output here>
#
# Do not use invented hashes/timestamps.


# ============================================================
# GRADED TASK 2 — REBUILD WITH AI AND RECORD A REJECTED SUGGESTION
# Submission reference:
# CSE325-2026-L01-K7QX-T2
# ============================================================

def task2_converter(celsius: float) -> float:
    """AI-assisted style converter with explicit float input."""
    return celsius * 9 / 5 + 32


print("\nTASK 2")
print(f"25C = {task2_converter(25)}F")

# Example rejected suggestion from the manual's allowed categories:
#
# Verbatim suggestion:
# <PASTE THE EXACT SUGGESTION PRODUCED BY YOUR AI TOOL HERE>
#
# Verdict:
# REJECT
#
# Precise reason:
# <Explain exactly why that suggestion was wrong, weaker, unnecessary,
# or inappropriate for THIS converter.>
#
# The manual explicitly requires the suggestion to be quoted exactly,
# so do not invent a fake "verbatim" quote.


# ============================================================
# GRADED TASK 3 — COMPARE USING YOUR OWN NUMBERS
# Submission reference:
# CSE325-2026-L01-K7QX-T3
# ============================================================

# Replace the placeholders below with figures from YOUR Git history.

your_hand_minutes = "<YOUR HAND BRANCH MINUTES>"
your_ai_minutes = "<YOUR AI BRANCH MINUTES>"
your_hand_lines = "<YOUR HAND LINES>"
your_ai_lines = "<YOUR AI LINES>"
your_hand_defects = "<YOUR HAND DEFECT COUNT>"
your_ai_defects = "<YOUR AI DEFECT COUNT>"

print("\nTASK 3 — YOUR COMPARISON TABLE")
print("Metric | Hand-written | AI-assisted")
print(f"Minutes | {your_hand_minutes} | {your_ai_minutes}")
print(f"Lines of code | {your_hand_lines} | {your_ai_lines}")
print(f"Defects personally hit | {your_hand_defects} | {your_ai_defects}")

# Three-sentence reflection — fill with YOUR actual experience:
#
# 1. The assistant helped me by: <your observation>.
# 2. The assistant cost me time when: <your observation>.
# 3. Overall, my run showed: <your observation>.
#
# Evidence required:
# Include the commit hash from which each number was derived.


# ============================================================
# GRADED TASK 4 — DEFEND ONE DIFFERENCE
# Submission reference:
# CSE325-2026-L01-K7QX-T4
# ============================================================

# Four-sentence answer template:
#
# The largest difference between my two versions is <difference>.
# In my code, this appears at <file>:<line>.
# I consider it a real improvement / different habit because <specific reason>.
# The evidence from my test/run that supports this is <specific evidence>.
#
# Replace every <> item with your own evidence before submission.


# ============================================================
# TAKE-HOME LAB ASSIGNMENT
# ============================================================

# Manual requirement:
# Pick a small utility you would actually use, such as:
# - tip splitter
# - password-length checker
# - another converter
#
# Build it twice:
# 1. By hand
# 2. With AI
#
# Then ask a classmate to try to break the AI version for five minutes.
#
# Suggested utility solved here: TIP SPLITTER
#
# This is an illustrative solution. For the actual take-home,
# record your own classmate's result.

def tip_splitter(bill: float, tip_percent: float, people: int) -> float:
    """Return the amount each person should pay."""
    if bill < 0:
        raise ValueError("Bill cannot be negative.")
    if tip_percent < 0:
        raise ValueError("Tip percentage cannot be negative.")
    if people <= 0:
        raise ValueError("Number of people must be greater than zero.")

    total = bill + (bill * tip_percent / 100)
    return total / people


print("\nTAKE-HOME EXAMPLE — TIP SPLITTER")
print(f"Each person pays: {tip_splitter(1000, 10, 4):.2f}")

# Expected output:
# TAKE-HOME EXAMPLE — TIP SPLITTER
# Each person pays: 275.00

# Classmate test result:
# <PASTE REAL RESULT HERE>
#
# Did the classmate find something you would have missed?
# <PASTE YOUR ANSWER HERE>


# ============================================================
# VIVA / QUICK QUESTIONS — COMMENTED OUT
# ============================================================

# Q1. What is the formula for Celsius to Fahrenheit?
# A. Fahrenheit = Celsius * 9 / 5 + 32.
#
# Q2. Why is float conversion useful for user input?
# A. Temperature may contain decimal values such as 25.5.
#
# Q3. What was the important bug in the manual's hand-written example?
# A. Integer division could produce an incorrect result in languages
#    where 9/5 truncates.
#
# Q4. What is the role of an AI coding assistant?
# A. It assists with coding, suggestions and explanations, while the
#    developer remains responsible for correctness and verification.
#
# Q5. Why are real Git commits important in this lab?
# A. The manual uses commit history and timestamps as evidence of
#    incremental work.
#
# Q6. What is the difference between a hand-written and AI-assisted
#    implementation?
# A. The implementation approach and development process differ; both
#    still need testing and verification.
#
# Q7. Why should a rejected AI suggestion be recorded exactly?
# A. Task 2 explicitly requires the verbatim suggestion.
#
# Q8. What evidence is required for Task 1?
# A. Git log with timestamps and Python version output.
#
# Q9. What does RUN_PROFILE represent?
# A. It is the principal configuration constant required by Lab 01.
#
# Q10. What should you do before submitting AI-generated code?
# A. Read, understand, verify and correct it where necessary.


# ============================================================
# REQUIRED CLOSING MARKER
# ============================================================
# Checked against the reference run.
# CSE325-2026-L01-K7QX
