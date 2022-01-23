# GP Collection

This python script auto-collects the daily rewards from GP. While this does not give players an unfair advantage in any games on the service, interpretations of the GP terms of use may vary and I make no guarantees as to your their policies. (In other words, use at your own risk!)

## Installation and Configuration
To run, you will need the following python packages:
- webdriver_manager
- selenium

Bash script gp_job.sh runs the python script with the usernames and passwords stored in environment variables $GP_EMAIL and $GP_PASS. Bear in mind that writing these manually into your scripts or environment set up may compromise your account security! 

Feel free to use the provided .plist with launchd (on Apple systems) in order to configure daily runs. If you are using a different operating system, you may wish to use cron or similar. 
