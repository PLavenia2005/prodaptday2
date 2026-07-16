class VehicleError(Exception):
    """Base class for other exceptions"""
    pass

class OwnerAlreadySetError(VehicleError):
    """Raised when trying to set an owner for a vehicle that already has one"""
    def __init__(self, owner_name):
        message = f"Owner '{owner_name}' is already set for this vehicle."
        super().__init__(message)

class InvalidBatteryCapacityError(VehicleError):
    """Raised when the battery capacity is invalid"""
    def __init__(self, capacity):
        super().__init__("Invalid battery capacity. must be a positive number.")

        