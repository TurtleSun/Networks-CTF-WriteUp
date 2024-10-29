# Network Challenge 4: Password Server

This challenge required cracking a password on a secret server located at ec521network port 1234. From the challenge description, we knew we were dealing with a TCP service.

Initial reconnaissance involved a basic connection to understand the server's behavior:

```bash
nc ec521network 1234
```
Server respondes with:
```
Insert your password:
```
Then, a noticeable delay before rejection response.

This behavior suggested a potential timing attack vulnerability, where server response times might leak information about the password's correctness.

## Analysis Approach
I developed a simple 1-time script to test the theory:
- Used ASCII character set for testing
	Because:
    - Password likely human-generated
    - Must be terminal-compatible
- Measured response times for each character as a viable solution
    Proved by:
    - Initial discovery showed 'T' triggered +1 second response delay

With the theory tested, I created a more well-rounded script that:
- Tests each ASCII character against current password fragment
- Identifies significant response time increases
- Builds password incrementally based on timing differences

![Password Discovery Process](Scripts/passwordGuesser.py)

## Pattern Recognition
Key observations during script execution:
- Each correct character increased response time by ~1 second
- Response times plateaued at approximately 20 seconds
- Strong correlation between password length and response delay
    Hence:
    - Final password length determined to be 20 characters

The script successfully revealed the complete password:

![Final Password Found](Media/challenge4_flagFound.png)

## Key Insights
- Time-based vulnerabilities can leak password information
- Response delays often correlate with password correctness
- Sequential character testing reveals password structure
- Pattern recognition crucial for timing attack success
- System behavior analysis guides attack methodology