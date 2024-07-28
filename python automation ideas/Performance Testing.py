import subprocess

def run_performance_test(jmeter_path, test_plan, result_file):
    subprocess.run([jmeter_path, "-n", "-t", test_plan, "-l", result_file])
    print(f"Performance test completed, results saved to {result_file}")

def analyze_performance_results(result_file):
    with open(result_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            if "FAILED" in line:
                print(f"Test failure detected: {line}")

if __name__ == "__main__":
    run_performance_test("/path/to/jmeter", "test_plan.jmx", "results.jtl")
    analyze_performance_results("results.jtl")
