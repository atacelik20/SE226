totalSeconds=int(input("How many seconds are there?"))
hours=totalSeconds//3600
remains=totalSeconds%3600
minutes=remains//60
seconds=remains%60
print(f"{totalSeconds} Seconds is {hours} Hours, {minutes} Minutes, {seconds} Seconds.")
