from observer_base import ObserverBase

class Tablet(ObserverBase):
    def update(self, msg):
        print(f"Update in tablet: {msg}")