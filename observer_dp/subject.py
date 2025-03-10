from subject_base import SubjectBase

class Subject(SubjectBase):
    def __init__(self):
        self.version = 0
        self.observers = []


    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def change(self, update_msg):
        for obs in self.observers:
            if hasattr(obs, 'update'):
                obs.update(update_msg)

    def version_update(self, version):
        self.version = version
        print("+++++++++++++ Initializing Version Updates in Devices +++++++++++++++++++")
        self.change(self.version)
        print("+++++++++++++ Completed Version Updates in Devices ++++++++++++++++++++++\n")
