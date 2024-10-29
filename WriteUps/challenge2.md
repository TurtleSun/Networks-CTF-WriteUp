# Network Challenge 2: Weather forecast

The second challenge introduced us to a weather service on an SSH network that broadcasts weather updates hourly. According to the prompt, the flag was hidden within tomorrow's weather forecast broadcast.

From the challenge description, we learned that the weather service broadcasts from port 5455. While the broadcasts occur hourly, the exact minute of transmission wasn't specified. This uncertainty in timing required a methodical approach.

To solve this, I developed a script (`weather.sh`) that would connect to the port and listen for several minutes at a time, ensuring we wouldn't miss the broadcast regardless of its exact timing:

![Weather monitoring script](Scripts/weather.sh)

By running this script persistently, I was able to successfully capture the broadcast containing tomorrow's forecast and extract the flag:

![Captured flag from weather broadcast](Media/challenge2_flagFound.png)

## Key Insights
- Automated monitoring is crucial for time-sensitive network analysis
- Scripting eliminates human error in repetitive monitoring tasks
- Systematic approach is more reliable than manual monitoring attempts
- Timing uncertainties are best handled through automated solutions