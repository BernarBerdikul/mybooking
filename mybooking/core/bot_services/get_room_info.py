from ..models import Room


def get_room_with_schedule(room_name: str) -> Room:
    room = Room.objects.prefetch_related(
        'bookings'
    ).get(room_name=room_name)
    return room
