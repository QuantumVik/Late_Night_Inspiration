from apscheduler.schedulers.background import BackgroundScheduler
from Late_Night_Inspiration.app.services.idea_service import IdeaService

scheduler = BackgroundScheduler()

def check_unsearched_ideas():
    service = IdeaService()
    unsearched = service.get_unsearched_ideas()
    for idea in unsearched:
        print(f"Reminder: You haven't searched for the idea with ID{idea['id']}." )


def scheduler_on():
    scheduler.add_job(check_unsearched_ideas,'interval',minutes = 10)
    scheduler.start()
