
# MAIN.PY 

"""Main module and master entry point of the WattaFaso-Manager application."""

from utils import database
from services import operations
from services import services


def secure_input(input_prompt):
    """Forces the user to enter a valid positive integer or zero."""

    while True:

        try:

            raw_text = input(input_prompt).strip()

            numeric_choice = int(raw_text)

            if numeric_choice < 0:

                print(
                    "Internal Input Error: "
                    "Negative values are not allowed."
                )

                continue

            return numeric_choice

        except ValueError:

            print(
                "Internal Input Error: "
                "A valid integer is required."
            )


def main_system_execution():
    """Handles the main interactive console loop."""

    subscriber_database = database.load_database()

    system_running = True

    while system_running:

        print(
            "\n=== WATTAFASO-MANAGER : MASTER CONSOLE ==="
        )

        print(
            "1. Display the global subscriber registry"
        )

        print(
            "2. Register a new subscriber "
            "(Automatic code generation)"
        )

        print(
            "3. Record meter reading "
            "and process payment"
        )

        print(
            "4. View fraud alerts and suspicions"
        )

        print(
            "5. Save current data"
        )

        print(
            "6. Display the supervision dashboard"
        )

        print(
            "7. Save data and shut down the system"
        )

        choice = secure_input(
            "Enter your option (1-7): "
        )

        if choice == 1:

            print(
                "\n--- GLOBAL SUBSCRIBER REGISTRY ---"
            )

            if not subscriber_database:

                print(
                    "The registry is empty."
                )

            else:

                for key in subscriber_database:

                    client = subscriber_database[key]

                    # Use updated current index
                    print(
                        "Code: "
                        + client.get_code()
                        + " | Name: "
                        + client.get_name()
                        + " | Current Index: "
                        + str(client.get_current_index())
                        + " | Unpaid Balance: "
                        + str(client.get_balance())
                        + " CFA Francs."
                    )

        elif choice == 2:

            operations.register_new_subscriber(
                subscriber_database
            )

            database.save_database(
                subscriber_database
            )

        elif choice == 3:

            session_cart = (
                operations.execute_meter_and_payment_session(
                    subscriber_database,
                    secure_input
                )
            )

            if session_cart:

                services.save_and_print_report(
                    session_cart
                )

                database.save_database(
                    subscriber_database
                )

                print(
                    "\nSynchronization completed: "
                    "Database updated."
                )

        elif choice == 4:

            services.run_anti_fraud_analysis(
                subscriber_database
            )

        elif choice == 5:

            database.save_database(
                subscriber_database
            )

            print(
                "Data successfully saved in memory."
            )

        elif choice == 6:

            services.display_global_dashboard(
                subscriber_database
            )

        elif choice == 7:

            database.save_database(
                subscriber_database
            )

            print(
                "\nSecurity backup completed. "
                "Shutting down WattaFaso-Manager."
            )

            system_running = False

        else:

            print(
                "Unavailable option. "
                "Please enter a number from 1 to 7."
            )


# Safe launch against Ctrl+C interruption
if __name__ == "__main__":

    try:

        main_system_execution()

    except KeyboardInterrupt:

        print(
            "\n\n[System] Program safely interrupted "
            "by the user (Ctrl+C)."
        )


# END OF SOFTWARE ARCHITECTURE 
