############
#
# Code Review
#
# Please do a code review for the following snippet.
# Add your review suggestions inline as python comments
#

############
import enum


def get_value(data, key, default, lookup=None, mapper=None):
    """
    Finds the value from data associated with key, or default if the
    key isn't present.
    If a lookup enum is provided, this value is then transformed to its
    enum value.
    If a mapper function is provided, this value is then transformed
    by applying mapper to it.
    """
    return_value = data.get(key, default)
    #return_value = data[key]
    # if return_value is None or return_value == "": # you must consider using data.get(key, default=default) instead of this condition
    #     return_value = default
    if lookup:
        return_value = lookup(return_value) # you have to call enum using parenthesis
    if mapper:
        return_value = mapper(return_value) # you have to pass return_value as list mapper([return_value])
    return return_value


def ftp_file_prefix(namespace):
    """
    Given a namespace string with dot-separated tokens, returns the
    string with
    the final token replaced by 'ftp'.
    Example: a.b.c => a.b.ftp
    """
    return ".".join(namespace.split(".")[:-1]) + '.ftp'


def string_to_bool(string):
    """
    Returns True if the given string is 'true' case-insensitive,
    False if it is
     'false' case-insensitive.
    Raises ValueError for any other input.
    """

    if string.lower() == 'true':
        return True
    if string.lower() == 'false':
        return False
    raise ValueError(f'String {string} is neither true nor false')


def config_from_dict(dict):
    """
    Given a dict representing a row from a namespaces csv file,
    returns a DAG configuration as a pair whose first element is the
    DAG name
    and whose second element is a dict describing the DAG's properties
    """
    #namespace = dict['Namespace'] # you must be use dict get to pass default value for namespace or raise fail just in case
    namespace = dict.get("namespace", "default")

    return (dict['Airflow DAG'], #dict['Airflow DAG'], # you must be setdefault title if you want to put Airflow DAG on dict or get by key, if you pass this value
            {"earliest_available_delta_days": 0,
             "lif_encoding": 'json',
             "earliest_available_time":
                 get_value(dict, 'Available Start Time', '07:00'),
             "latest_available_time":
                 get_value(dict, 'Available End Time', '08:00'),
             "require_schema_match":
                 get_value(dict, 'Requires Schema Match', 'True',
                           mapper=string_to_bool),
             "schedule_interval":
                 get_value(dict, 'Schedule', '1 7 * * * '),
             "delta_days":
                 get_value(dict, 'DAY_BEFORE', 'Delta Days',
                           lookup=DeltaDays), # Delta Day not imported or implemented
             "ftp_file_wildcard":
                 get_value(dict, 'File Naming Pattern', None),
             "ftp_file_prefix":
                 get_value(dict, 'FTP File Prefix',
                           ftp_file_prefix(namespace)),
             "namespace": namespace
             }
            )


'''
You have to import or create DetalDays enum
'''
class DeltaDays(enum.Enum):
     DAY_BEFORE = 'Delta Days'


#config_from_dict(dict)
dict = dict()
dict['Airflow DAG'] = 'Airflow DAG'
print(config_from_dict(dict)) # you have to instance a dict object