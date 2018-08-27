
class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("This class is Singleton")
        else:
            Singleton._instance = self


def main():
    import pdb;pdb.set_trace()
    s = Singleton()
    print(s)

    s.getInstance()
    print(s)

    s = Singleton.getInstance()
    print(s)
if __name__ == "__main__":
    main()