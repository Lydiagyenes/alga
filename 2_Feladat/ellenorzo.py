import os
import subprocess

# A tesztfájlok mappáinak megadása
INPUT_DIR = "test_inputs"
OUTPUT_DIR = "test_outputs"
EXPECTED_DIR = "expected_outputs"
SCRIPT = "password_cracker.py"  # A jelszóellenőrző program neve

# Ellenőrzi a teszteseteket
def run_tests(num_tests):
    for i in range(1, num_tests + 1):
        input_file = f"{INPUT_DIR}/test{i}.txt"
        output_file = f"{OUTPUT_DIR}/output{i}.txt"
        expected_file = f"{EXPECTED_DIR}/expected{i}.txt"
        
        print(f"Teszteset {i} futtatása...")

        # Futtatja a Python szkriptet a bemeneti fájllal és menti az eredményt
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            subprocess.run(["python3", SCRIPT], stdin=infile, stdout=outfile)
        
        # Az eredmények ellenőrzése
        with open(output_file, 'r') as outfile, open(expected_file, 'r') as expfile:
            output = outfile.read().strip()
            expected = expfile.read().strip()

            if output == expected:
                print(f"Teszteset {i} sikeres!")
            else:
                print(f"Teszteset {i} sikertelen!")
                print(f"Kapott eredmény:\n{output}")
                print(f"Várt eredmény:\n{expected}")

# A fő függvény
if __name__ == "__main__":
    NUM_TESTS = 10  # A tesztesetek száma
    run_tests(NUM_TESTS)
