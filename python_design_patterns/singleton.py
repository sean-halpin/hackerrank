class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print(Singleton, cls)
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.data = None
        return cls._instance

    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
def test_singleton():
    single1 = Singleton()
    assert single1.get_data()
    single1.set_data("my sample data")
    assert single1.get_data() == "my sample data", "Test Failed, singleton 1 did not set it's data correctly"
    single2 = Singleton()
    assert single2.get_data() == "my sample data", "Test Failed, singleton 2 did not have singleton1's data"
    assert single1 is single2, "Test Failed, Singleton1 is not the same instance as Singleton2"
    print(single1, single2)
    print("All Passed")
    
test_singleton()