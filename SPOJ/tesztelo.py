import subprocess

def run_test(test_input, expected_output):
    # Futtatjuk a programot a teszt bemenettel
    process = subprocess.Popen(
        ["python3", "prime.py"],  # A fájl neve, amit tesztelni szeretnénk
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Bemenet átadása a programnak
    stdout, stderr = process.communicate(input=test_input.encode())

    # Eredmény összehasonlítása
    if stdout.decode().strip() == expected_output.strip():
        print("Test Passed")
    else:
        print("Test Failed")
        print("Expected Output:")
        print(expected_output)
        print("Actual Output:")
        print(stdout.decode().strip())

# Tesztesetek listája
tests = [
    {
        "input": "1\n1 10\n", 
        "expected_output": "2\n3\n5\n7\n"
    },
    {
        "input": "1\n3 5\n", 
        "expected_output": "3\n5\n"
    },
    {
        "input": "1\n10 20\n", 
        "expected_output": "11\n13\n17\n19\n"
    },
    {
        "input": "1\n1 100\n", 
        "expected_output": "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n31\n37\n41\n43\n47\n53\n59\n61\n67\n71\n73\n79\n83\n89\n97\n"
    },
    {
        "input": "1\n100 200\n", 
        "expected_output": "101\n103\n107\n109\n113\n127\n131\n137\n139\n149\n151\n157\n163\n167\n173\n179\n181\n191\n193\n197\n199\n"
    },
    {
        "input": "1\n500000000 500000010\n", 
        "expected_output": "500000003\n500000009\n"
    },
    {
        "input": "1\n999999990 1000000000\n", 
        "expected_output": "999999991\n"
    },
    {
        "input": "1\n1000000000 1000000010\n", 
        "expected_output": "1000000003\n1000000009\n"
    },
    {
        "input": "1\n500 1000\n", 
        "expected_output": "503\n509\n521\n523\n541\n547\n557\n563\n569\n571\n577\n587\n593\n599\n607\n613\n617\n619\n631\n641\n643\n"
    },
    {
        "input": "1\n1 100000\n", 
        "expected_output": "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n31\n37\n41\n43\n47\n53\n59\n61\n67\n71\n73\n79\n83\n89\n97\n"
    }
]

# Tesztek futtatása
for test in tests:
    print(f"Running test with input: {test['input']}")
    run_test(test["input"], test["expected_output"])
    print("\n---\n")
