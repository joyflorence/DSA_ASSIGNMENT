# Waypoint Node
class Waypoint:
    def __init__(self, location, description):
        # Initialize a Waypoint object with location and description
        self.location = location #the location of the waypoint.
        self.description = description #the description of the waypoint
        
        # Pointers to the next and previous waypoints
        self.next = None #the next waypoint in the squence
        self.prev = None #the pervious waypoint in the squence

# Route (Singly linked list)
class Route:
    # Initialize a Route object with head and current pointers
    def __init__(self):
        self.head = None 
        self.current = None

    def add_waypoint(self, location, description):
        new_waypoint = Waypoint(location, description)
        if not self.head:
            # If the route is empty, set the new waypoint as the head
            self.head = new_waypoint
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_waypoint

    def insert_waypoint_after(self, target, location, description):
        if not self.head:
            raise Exception("Route is empty")
        new_waypoint = Waypoint(location, description)
        if self.head == target:
            new_waypoint.next = self.head
            self.head = new_waypoint
            return
        current = self.head
        while current and current != target:
            current = current.next
        if not current:
            raise Exception("Target waypoint not found")
        new_waypoint.next = current.next
        current.next = new_waypoint

    def remove_waypoint(self, location):
        if not self.head:
            raise Exception("Route is empty")
        if self.head.location == location:
            self.head = self.head.next
            return
        current = self.head
        while current and current.next and current.next.location != location:
            current = current.next
        if not current or not current.next:
            raise Exception("Waypoint not found")
        current.next = current.next.next

    def next_waypoint(self):
        current = self.head
        if not current:
            raise Exception("Route is empty")
        while current.next:
            current = current.next
        return current

# BidirectionalRoute (Doubly linked list)
class BidirectionalRoute(Route):
    def __init__(self):
        super().__init__()
        self.tail = None

    def add_waypoint(self, location, description):
        new_waypoint = Waypoint(location, description)
        if not self.head:
            self.head = new_waypoint
            self.tail = new_waypoint
        else:
            self.tail.next = new_waypoint
            new_waypoint.prev = self.tail
            self.tail = new_waypoint

    def insert_waypoint_after(self, target, location, description):
        if not self.head:
            raise Exception("Route is empty")
        new_waypoint = Waypoint(location, description)
        if self.head == target:
            self.head.prev = new_waypoint
            new_waypoint.next = self.head
            self.head = new_waypoint
            return
        current = self.head
        while current and current != target:
            current = current.next
        if not current:
            raise Exception("Target waypoint not found")
        new_waypoint.next = current.next
        new_waypoint.prev = current
        if current.next:
            current.next.prev = new_waypoint
        else:
            self.tail = new_waypoint
        current.next = new_waypoint

    def remove_waypoint(self, location):
        if not self.head:
            raise Exception("Route is empty")
        if self.head.location == location:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
        current = self.head
        while current and current.next and current.next.location != location:
            current = current.next
        if not current or not current.next:
            raise Exception("Waypoint not found")
        if current.next.next:
            current.next.next.prev = current
        else:
            self.tail = current
        current.next = current.next.next

    def previous_waypoint(self):
        current = self.tail
        if not current:
            raise Exception("Route is empty")
        while current.prev:
            current = current.prev
        return current


route = Route()
route.add_waypoint("New York", "The Big Apple")
route.add_waypoint("Chicago", "The Windy City")
route.add_waypoint("Denver", "Mile High City")

print("Adding waypoint to Route:")
route.insert_waypoint_after(route.head, "Seattle", "Emerald City")
current = route.head
while current:
    print(f"Location: {current.location}, Description: {current.description}")
    current = current.next

print("Removing waypoint from Route:")
route.remove_waypoint("Seattle")
current = route.head
while current:
    print(f"Location: {current.location}, Description: {current.description}")
    current = current.next

bidirectional_route = BidirectionalRoute()
bidirectional_route.add_waypoint("Los Angeles", "City of Angels")
bidirectional_route.add_waypoint("Austin", "Live Music Capital")
bidirectional_route.add_waypoint("Boston", "Beantown")

print("Adding waypoint to BidirectionalRoute:")
bidirectional_route.insert_waypoint_after(
    bidirectional_route.head.next.next, "San Francisco", "Fog City")
current = bidirectional_route.head
while current:
    print(f"Location: {current.location}, Description: {current.description}")
    current = current.next

print("Bidirectional traversal:")
current = bidirectional_route.head
while current:
    print(f"Location: {current.location}, Description: {current.description}")
    current = current.next
current = bidirectional_route.previous_waypoint()
while current:
    print(f"Location: {current.location}, Description: {current.description}")
    current = current.prev
