"""
A huge phone book containing pairs of the form {phone number, person's name} was
stored as a vector sorted by name in alphabetical order. Write a program that finds the
phone number of a given person in this list, bearing in mind that the list is very large and that
users need the search results to be as fast as possible.
"""

from random import choice, randint
from typing import TypedDict


class Contact(TypedDict):
    name: str
    phone: int


def populate_and_sorted_list(contacts_list_len: int) -> list[Contact]:
    phone_list = []
    first_names = ('John', 'Andy', 'Joe')
    last_names = ('Johnson', 'Smith', 'Williams')
    for _ in range(contacts_list_len + 1):
        phone_list.append(Contact(name=f'{choice(first_names)} {choice(last_names)}',
                                  phone=randint(90000000, 99999999)))
    sorted_contacts = sorted(phone_list, key=lambda x: x['name'])
    return sorted_contacts


def search_contact(phone_list: list[Contact], contact_name: str) -> Contact | str:
    copy_list = phone_list.copy()
    while len(copy_list) > 1:
        len_list = len(copy_list)
        mid = len_list // 2
        if copy_list[mid].get("name") == contact_name:
            return copy_list[mid]
        else:
            if copy_list[mid].get("name")[:1] > contact_name[:1]:
                copy_list = copy_list[:mid]
            else:
                copy_list = copy_list[mid:]
    return f"no contact found with name: {contact_name}"


if __name__ == "__main__":
    contact_list = populate_and_sorted_list(100)
    print(search_contact(contact_list, "Joe Smith"))
