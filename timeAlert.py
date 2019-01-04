import os
import time

timeDuration = 30 # in minutes

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def nextTime(past):
	return past + timeDuration * 60

def main():
	start_time = time.time()
	prev = start_time

	next_time = nextTime(prev)

	while True:
		time_now = time.time()

		if time_now >= next_time:
			# comp has been running for half hour more
			duration = str((time_now - start_time) / 60)
			title = "High Computer Usage"
			message = "The Computer has been on for Another " + str(timeDuration) + " mins.\n"
			message += "It has been " + duration + " mins " 
			message += "Since the Start of the Computer."

			# Notification
			notify(title, message)

			# updating prev and next time
			prev = time_now
			next_time = nextTime(prev)

if __name__ == '__main__':
	main()
