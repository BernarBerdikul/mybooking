from ..models import Booking


def create_booking_object_db(
        start_time: str,
        end_time: str, username: str,
        booking_date: str,
        room_id: int
) -> Booking:
    new_booking_object = Booking.objects.create(
        room_id=room_id,
        username=username,
        day=booking_date,
        start_time=start_time,
        end_time=end_time
    )
    return new_booking_object
