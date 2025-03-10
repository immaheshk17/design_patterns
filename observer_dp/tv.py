from observer_base import ObserverBase

class TV(ObserverBase):
    def update(self, msg):
        print(f"Update in tv: {msg}")