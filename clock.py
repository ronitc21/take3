from apscheduler.schedulers.blocking import BlockingScheduler
from honey import send_message

sched = BlockingScheduler()

# Schedule send_message function to be called every few hours
sched.add_job(send_message, 'interval', seconds = 1)

sched.start()