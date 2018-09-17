class Flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration


a = Flight("Delhi", 'Mumbai', 576)
#print(a.origin)
#print(a.destination)
#print(a.duration)

def main():
    b = Flight(origin='Paris', destination='Tokyo', duration=200)
    b.duration+=10
    print(b.duration)
main()