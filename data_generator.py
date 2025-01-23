import json
import random
import argparse

def generate_json_data(num_samples, output_file="data.json"):
    user_agents = ["Mozilla/5.0 (Windows)", "Mozilla/5.0 (Linux)", "Mozilla/5.0 (MacOS)"]
    tls_ja3_values = ["769,47-53-255,0-23-65281-10-11,29-23", "771,46-49-150,0-19-65280-11-13,28-21"]
    ttl_values = [128, 64, 255]
    is_anomaly_values = [0, 1]

    data = {
        "user_agent": [random.choice(user_agents) for _ in range(num_samples)],
        "tls_ja3": [random.choice(tls_ja3_values) for _ in range(num_samples)],
        "ttl": [random.choice(ttl_values) for _ in range(num_samples)],
        "is_anomaly": [random.choice(is_anomaly_values) for _ in range(num_samples)],
    }

    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Generated {num_samples} samples in {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_samples", type=int, required=True, help="Number of samples to generate")
    args = parser.parse_args()

    generate_json_data(args.num_samples)

