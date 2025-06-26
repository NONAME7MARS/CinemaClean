from datetime import date, timedelta, datetime, time
from cinema.models import Movie, Session, Hall

titles = [
    "Барбі",
    "Оппенгеймер",
    "Дюна: Частина друга",
    "Вартові Галактики 3",
    "Людина-павук: Крізь всесвіт"
]

movies = Movie.objects.filter(title__in=titles)
halls = list(Hall.objects.all())
base_times = [time(12, 0), time(14, 15), time(16, 30), time(18, 45), time(21, 0)]
start_date = date(2025, 6, 15)
end_date = date(2025, 6, 22)
days_range = (end_date - start_date).days + 1

Session.objects.filter(
    movie__in=movies,
    date__range=(start_date, end_date)
).delete()

for movie in movies:
    for i in range(days_range):
        current_date = start_date + timedelta(days=i)
        used_halls = set()
        for j in range(3):  # по 3 сеанси на день
            available_halls = [h for h in halls if h.id not in used_halls]
            if not available_halls:
                break
            hall = available_halls[j % len(available_halls)]
            used_halls.add(hall.id)

            start = base_times[j % len(base_times)]
            end = (datetime.combine(date.today(), start) + timedelta(hours=2)).time()

            Session.objects.create(
                movie=movie,
                hall=hall,
                date=current_date,
                start_time=start,
                end_time=end
            )
print("Сеанси оновлено!")
