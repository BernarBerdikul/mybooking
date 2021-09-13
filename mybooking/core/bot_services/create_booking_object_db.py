from ..models import Booking, Room
from datetime import datetime


def create_booking_object_db(
        start_time: str,
        end_time: str,
        booking_date: str,
        room_name: str
) -> Booking:
    new_booking_object = Booking.objects.create(
        room_id=Room.objects.get(room_name=room_name).id,
        day=datetime.strptime(booking_date, "%d-%m-%Y").strftime("%Y-%m-%d"),
        start_time=start_time,
        end_time=end_time
    )
    return new_booking_object


def update_booking_object(
        booking_id: int, user_id: int
) -> None:
    Booking.objects.filter(id=booking_id).update(user_id=user_id)
    return None
