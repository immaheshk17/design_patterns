from director import Director

if __name__ == "__main__":
    director = Director()
    computer = director.construct_gaming(cpu=16, gpu=4, ram=16, ssd=256)
    print(computer)