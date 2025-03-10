from observer_base import ObserverBase

class Phone(ObserverBase):
    def update(self, msg):
        print(f"Update in Phone: {msg}")