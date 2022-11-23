from walker import RandomWalker
        

if __name__ == "__main__":
    path = []
    zombie = RandomWalker()
    for _ in range(10):
        zombie.walk1s()  
        path.append(zombie.position)
    print(path)
