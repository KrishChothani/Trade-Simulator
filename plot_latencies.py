import os
import sys
import matplotlib.pyplot as plt

def find_file(filename):
    """Search for the CSV file in common locations."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        filename,                                      # Current working directory
        os.path.join(script_dir, filename),            # Script directory
        os.path.join(script_dir, "build", filename),   # build directory relative to script
        os.path.join(os.getcwd(), "build", filename)   # build directory relative to CWD
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return None

def main():
    add_csv_path = find_file("add_latencies.csv")
    match_csv_path = find_file("match_latencies.csv")

    if not add_csv_path or not match_csv_path:
        print("Error: Could not locate 'add_latencies.csv' and/or 'match_latencies.csv'.")
        print("Please run the simulator first to generate latency logs, or check your directory.")
        sys.exit(1)

    print(f"Loading add latencies from: {add_csv_path}")
    print(f"Loading match latencies from: {match_csv_path}")

    # Load latencies from CSV
    with open(add_csv_path, 'r') as f:
        add_latencies = [float(line.strip()) for line in f if line.strip()]

    with open(match_csv_path, 'r') as f:
        match_latencies = [float(line.strip()) for line in f if line.strip()]

    # Plot series
    plt.figure(figsize=(10, 6))
    plt.plot(add_latencies, label='Add Latency (us)', color='blue', alpha=0.8)
    plt.plot(match_latencies, label='Match Latency (us)', color='green', alpha=0.8)
    plt.xlabel('Operation Index')
    plt.ylabel('Latency (microseconds)')
    plt.title('Order Book Operation Latencies Over Time')
    plt.legend()
    plt.grid(True)
    
    output_path = os.path.join(os.path.dirname(add_csv_path), "latencies.png")
    plt.savefig(output_path)
    print(f"Plot saved successfully to: {output_path}")

    # Display interactively if supported
    try:
        plt.show()
    except Exception:
        pass

if __name__ == "__main__":
    main()
