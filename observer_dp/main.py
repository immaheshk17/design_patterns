from phone import Phone
from tablet import Tablet
from tv import TV
from subject import Subject

if __name__ == "__main__":
    sub = Subject()

    phone = Phone()
    tab = Tablet()
    tv = TV()

    sub.attach(phone)
    sub.attach(tab)
    sub.attach(tv)

    sub.change("coming new version - 2.0")

    sub.detach(tv)

    sub.change("coming new version - 3.0")