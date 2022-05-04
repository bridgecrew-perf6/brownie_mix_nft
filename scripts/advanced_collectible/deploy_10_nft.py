from scripts.advanced_collectible.create_collectible import create_collectible


def deploy10():
    toDeploy = 3
    for n in range(toDeploy):
        print(f"run number {(n + 1)}")
        create_collectible()
        if n > toDeploy:
            print("done, execute next")
        else:
            print("job finished")

def main():
    deploy10()
