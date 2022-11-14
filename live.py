from datetime import datetime
import time

access_time_map = {
}


def event(user_name, access_time):
    access_time = time.mktime(datetime.strptime(access_time, "%Y/%m/%d %H:%M").timetuple())
    # access_time = time.time(access_time, "%Y/%m/%d %H:%M")
    last_access = access_time_map.get(user_name)
    if last_access:
        if access_time > last_access + 300:
            access_time_map[user_name] = access_time
            return True
        else:
            return False
    else:
        access_time_map[user_name] = access_time
        return True


assert event('Bod', '2022/08/04 12:00') is True
assert event('Bod', '2022/08/04 12:03') is False
assert event('Bod', '2022/08/04 12:06') is True
assert event('Bod', '2022/08/05 12:00') is True
assert event('Mary', '2022/08/04 12:07') is True
