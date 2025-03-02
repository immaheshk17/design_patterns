from zombies import Zombie, Sword

if __name__ == "__main__":
    z = Zombie(health=100, sword=Sword(100))

    arr = []
    for i in range(100):
        arr.append(z.clone())


    print(arr[0])
    print(arr[1])

    print(arr[0].sword)
    print(arr[1].sword)
