import random
import string


# ------------------------------------
# booking id generate function
# ------------------------------------
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_booking_id_generator(instance):
    new_booking_id = random_string_generator().upper()

    klass = instance.__class__
    qs_exists = klass.objects.filter(booking_id=new_booking_id).exists()
    if qs_exists:
        return unique_booking_id_generator(instance)
    return new_booking_id
# end of booking id gerating function

