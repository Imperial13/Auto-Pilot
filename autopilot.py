class Autopilot:
    def __init__(self):
        self.flying = False
        self.base_location = None

    def take_off(self):
        self.flying = True
        print("Taking off...")

    def land(self):
        self.flying = False
        print("Landing...")

    def detect_base(self, current_location):
        # Simulate base detection logic
        if current_location == self.base_location:
            print("Base detected.")
            return True
        return False

    def drop_bomb(self):
        if self.flying:
            print("Dropping bomb...")
        else:
            print("Cannot drop bomb while not flying.")

    def set_base_location(self, location):
        self.base_location = location
        print(f"Base location set to {location}.")