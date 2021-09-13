from ..models import Room


def get_room_with_schedule(room_name: str) -> Room:
    return Room.objects.prefetch_related(
        'bookings', 'bookings__user'
    ).get(room_name=room_name)
