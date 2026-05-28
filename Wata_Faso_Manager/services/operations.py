# SECURED AND STABILIZED PYTHON CODE FOR OPERATIONS.PY

"""Field and counter operations module for WattaFaso-Manager."""

from datetime import datetime
from models import models


def register_new_subscriber(client_dictionary):
    """Registers a new subscriber with a guaranteed unique ID."""

    print("\n--- AUTOMATIC SUBSCRIPTION ASSIGNMENT ---")

    entered_name = input(
        "Enter the full name of the new client: "
    ).strip()

    if not entered_name:

        print(
            "Error: Name cannot be empty. Operation cancelled."
        )

        return

    print("Choose the pricing profile:")
    print("1. Social Profile (Households)")
    print("2. Commercial Profile (Shops/Workshops)")

    choice = input(
        "Your choice (1 or 2): "
    ).strip()

    if choice == "1":

        prefix = "SOC"

    elif choice == "2":

        prefix = "COM"

    else:

        print(
            "Error: Invalid choice. Procedure cancelled."
        )

        return

    # Improvement D:
    # Dynamic extraction of the current year
    current_year = str(datetime.now().year)

    # Improvement C:
    # Search algorithm for maximum number
    # to avoid duplicate IDs
    max_number = 0

    for key in client_dictionary:

        # Valid code example:
        # SOC-2026-003

        segments = key.split("-")

        if (
            len(segments) == 3
            and segments[0] == prefix
            and segments[1] == current_year
        ):

            try:

                extracted_number = int(segments[2])

                if extracted_number > max_number:

                    max_number = extracted_number

            except ValueError:

                continue

    sequential_number = max_number + 1

    unique_code = (
        prefix
        + "-"
        + current_year
        + "-"
        + str(sequential_number).zfill(3)
    )

    # Object creation with indexes
    # and balance initialized to zero
    if prefix == "SOC":

        new_client = models.SocialSubscriber(
            unique_code,
            entered_name,
            0,
            0,
            0
        )

    else:

        new_client = models.CommercialSubscriber(
            unique_code,
            entered_name,
            0,
            0,
            0
        )

    client_dictionary[unique_code] = new_client

    print(
        "Success: Registration completed by the system."
    )

    print(
        "Machine-generated unique code: "
        + unique_code
    )


def execute_meter_and_payment_session(
    client_dictionary,
    secure_input_function
):
    """Handles meter reading updates and payment collection."""

    invoice_cart = []

    continue_input = "YES"

    while continue_input == "YES":

        print(
            "\n--- METER UPDATE AND PAYMENT COLLECTION ---"
        )

        entered_code = input(
            "Enter the subscriber unique code: "
        ).strip()

        if entered_code not in client_dictionary:

            print(
                "Error: This code does not exist "
                "in the network."
            )

            continue

        active_client = client_dictionary[entered_code]

        print(
            "Client found: "
            + active_client.get_name()
        )

        print(
            "Previous unpaid balance: "
            + str(active_client.get_balance())
            + " CFA Francs."
        )

        new_reading = secure_input_function(
            "Enter the new meter index value: "
        )

        # Strict use of setter for encapsulation
        if not active_client.update_current_index(
            new_reading
        ):

            print(
                "Error: The entered index is lower "
                "than the previous index."
            )

            continue

        volume = active_client.calculate_consumption()

        total_amount_due = (
            active_client.calculate_bill()
        )

        print(
            "Total amount to pay "
            "(including unpaid balance): "
            + str(total_amount_due)
            + " CFA Francs."
        )

        paid_amount = secure_input_function(
            "Enter the amount paid at the counter: "
        )

        # Secure debt management
        remaining_balance = (
            total_amount_due - paid_amount
        )

        if remaining_balance < 0:

            print(
                "The system returns change: "
                + str(abs(remaining_balance))
                + " CFA Francs."
            )

            active_client.update_balance(0)

        else:

            active_client.update_balance(
                remaining_balance
            )

            if remaining_balance > 0:

                print(
                    "Notice: An unpaid balance of "
                    + str(remaining_balance)
                    + " CFA Francs will be carried over."
                )

        # Automatic index cycle rollover
        active_client.close_index_period()

        # Store transaction for cash report
        invoice_line = (
            active_client,
            volume,
            paid_amount
        )

        invoice_cart.append(invoice_line)

        response = input(
            "Do you want to process another subscriber? "
            "(YES/NO): "
        ).strip()

        continue_input = response.upper()

    return invoice_cart


# END OF OPERATIONS.PY CODE
