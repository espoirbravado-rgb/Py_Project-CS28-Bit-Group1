#  MODELS.PY 

"""Subscriber profile modeling module for the WattaFaso-Manager network."""

from utils  import config


class Subscriber:
    """ class representing a network subscriber."""

    def __init__(self, code, name, previous_index, current_index, initial_balance=0):
        """Initializes a new subscriber with indexes and unpaid balance.
        """
        self._code = code
        self._name = name
        self._previous_index = previous_index
        self._current_index = current_index
        self._unpaid_balance = initial_balance

    def get_code(self):
        """Returns the subscriber unique code.

        Return:
            str: Identification code.
        """
        return self._code

    def get_name(self):
        """Returns the subscriber full name.
        """
        return self._name

    def get_previous_index(self):
        """Returns the previous consumption index.
        """
        return self._previous_index

    def get_current_index(self):
        """Returns the current consumption index."""
        return self._current_index

    def get_balance(self):
        """Returns the subscriber unpaid balance. """
        return self._unpaid_balance

    def update_balance(self, amount):
        """Updates the unpaid balance."""
        self._unpaid_balance = amount

    def update_current_index(self, index_value):
        """Updates the current index after validation."""

        if index_value >= self._previous_index:
            self._current_index = index_value
            return True
        return False

    def calculate_consumption(self):
        """Calculates consumption volume between indexes."""
        return self._current_index - self._previous_index

    def close_index_period(self):
        """Automatically shifts indexes for the next month."""
        self._previous_index = self._current_index

    def calculate_bill(self):
        """Calculates bill amount (generic method).

        """
        return 0.0


class SocialSubscriber(Subscriber):
    """Class representing a subscriber under social domestic pricing."""

    def calculate_bill(self):
        """Calculates social bill based on consumption and previous debt."""

        # Immutable tuple used to secure calculations
        social_calculation_data = (
            self.calculate_consumption(),
            config.SOCIAL_RATE
        )

        consumed_volume = social_calculation_data[0]
        unit_price = social_calculation_data[1]

        monthly_amount = consumed_volume * unit_price

        return monthly_amount + self._unpaid_balance


class CommercialSubscriber(Subscriber):
    """Class representing a subscriber under commercial pricing."""

    def calculate_bill(self):
        """Calculates commercial bill with fixed maintenance tax."""

        # Grouping billing constants in a structural tuple
        billing_parameters = (
            config.COMMERCIAL_RATE,
            config.MAINTENANCE_TAX
        )

        unit_rate = billing_parameters[0]
        fixed_tax = billing_parameters[1]

        consumed_volume = self.calculate_consumption()

        monthly_amount = (
            consumed_volume * unit_rate
        ) + fixed_tax

        return monthly_amount + self._unpaid_balance


# END OF  MODELS.PY 
        
