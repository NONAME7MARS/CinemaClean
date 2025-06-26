import os
import django
import random
from datetime import datetime, timedelta, time, date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinema_project.settings")
django.setup()

from cinema.models import Movie, Hall, Session

def create_halls():
    hall_types = ["Стандарт", "IMAX", "VIP"]
    for i in range(1, 4):
        Hall.objects.get_or_create(
            number=i,
            defaults={"capacity": 100, "type": random.choice(hall_types)}
        )

def get_available_slot(occupied_times, duration):
    start_hour = 10
    end_hour = 22

    for hour in range(start_hour, end_hour - duration // 60):
        start = time(hour, 0)
        end = (datetime.combine(date.today(), start) + timedelta(minutes=duration)).time()
        overlap = any(
            (start < s_end and end > s_start)
            for s_start, s_end in occupied_times
        )
        if not overlap:
            return start, end
    return None, None

def create_sessions():
    today = date.today()
    movies = Movie.objects.all()
    halls = Hall.objects.all()
    days = 5  # на 5 днів вперед

    for single_day in [today + timedelta(days=i) for i in range(days)]:
        for hall in halls:
            hall_schedule = []

            for movie in movies:
                duration = movie.duration
                start, end = get_available_slot(hall_schedule, duration)
                if not start:
                    continue

                hall_schedule.append((start, end))

                Session.objects.create(
                    movie=movie,
                    hall=hall,
                    date=single_day,
                    start_time=start,
                    end_time=end,
                )
                print(f"✔ Сеанс: {movie.title} в Зал {hall.number} на {single_day} о {start}")

if __name__ == "__main__":
    create_halls()
    create_sessions()
