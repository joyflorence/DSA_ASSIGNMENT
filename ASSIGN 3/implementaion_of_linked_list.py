class Waypoint:
    def __init__(self, location, description):
        self.location = location  # Location identifier of the waypoint
        self.description = description  # Description of the waypoint
        self.next = None  # Pointer to the next waypoint
        self.previous = None  # Pointer to the previous waypoint (for BidirectionalRoute)

class Route:
    def __init__(self):
        self.head = None  # Head pointer of the linked list

    def add_waypoint(self, location, description):
        # Creating a new waypoint
        new_waypoint = Waypoint(location, description)
        if not self.head:
            # If the route is empty, set the new waypoint as the head
            self.head = new_waypoint
        else:
            # Traverse to the end of the route and append the new waypoint
            current = self.head
            while current.next:
                current = current.next
            current.next = new_waypoint

    def insert_waypoint_after(self, target_location, location, description):
        # Create a new waypoint
        new_waypoint = Waypoint(location, description)
        current = self.head
        while current:
            if current.location == target_location:
                # Insert the new waypoint after the target waypoint
                new_waypoint.next = current.next
                current.next = new_waypoint
                return
            current = current.next

    def remove_waypoint(self, location):
        current = self.head
        if current and current.location == location:
            # If the head is the waypoint to be removed, update head pointer
            self.head = current.next
            return
        while current:
            if current.next and current.next.location == location:
                # Remove the next waypoint by skipping/bypassing it
                current.next = current.next.next
                return
            current = current.next

    def next_waypoint(self):
        # Move to the next waypoint in the route after removing the previous waypoint and update the head pointer
        if self.head:
            self.head = self.head.next
            return self.head
        
class BidirectionalRoute(Route):
    def __init__(self):
        super().__init__()

    def insert_waypoint_after(self, target_location, location, description):
        new_waypoint = Waypoint(location, description)
        current = self.head
        while current:
            if current.location == target_location:
                # Insert the new waypoint after the target waypoint
                new_waypoint.next = current.next
                if current.next:
                    # Update the previous pointer of the waypoint after insertion
                    current.next.previous = new_waypoint
                current.next = new_waypoint
                new_waypoint.previous = current
                return
            current = current.next

    def remove_waypoint(self, location):
        current = self.head
        if current and current.location == location:
            # If the head is the waypoint to be removed, update head pointer
            self.head = current.next
            if self.head:
                # Update the previous pointer of the new head
                self.head.previous = None
            return
        while current:
            if current.location == location:
                # Remove the waypoint and update previous and next pointers
                if current.next:
                    current.next.previous = current.previous
                current.previous.next = current.next
                return
            current = current.next

    def previous_waypoint(self):
        # Move to the previous waypoint in the bidirectional route
        if self.head and self.head.previous:
            self.head = self.head.previous
            return self.head
            
# Testing Scenario
if __name__ == "__main__":
    # Create a Route
    route = Route()
    route.add_waypoint("A", "Description A")
    route.add_waypoint("B", "Description B")
    route.add_waypoint("C", "Description C")
    route.add_waypoint("D", "Description D")
    route.add_waypoint("E", "Description E")

    # Demonstrate adding, inserting, and removing waypoints
    route.insert_waypoint_after("C", "C.5", "Description C.5")
    route.remove_waypoint("D")

    # Show single direction traversal
    print("Single Direction Traversal:")
    current = route.head
    while current:
        print(current.location, current.description)
        current = current.next

    # Create a BidirectionalRoute
    bidirectional_route = BidirectionalRoute()
    bidirectional_route.add_waypoint("A", "Description A")
    bidirectional_route.add_waypoint("B", "Description B")
    bidirectional_route.add_waypoint("C", "Description C")
    bidirectional_route.add_waypoint("D", "Description D")
    bidirectional_route.add_waypoint("E", "Description E")

    # Demonstrate adding, inserting, and removing waypoints
    bidirectional_route.insert_waypoint_after("C", "C.5", "Description C.5")
    bidirectional_route.remove_waypoint("D")

    # Show bidirectional traversal
    print("\nBidirectional Traversal Forward:")
    current = bidirectional_route.head
    while current:
        print(current.location, current.description)
        current = current.next

    print("\nBidirectional Traversal Backward:")
    current = bidirectional_route.head
    while current.next:
        current = current.next
    while current:
        print(current.location, current.description)
        current = current.previous
