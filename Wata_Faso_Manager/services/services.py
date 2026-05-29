# SERVICES.PY 

"""Analytics and reporting services module for WattaFaso-Manager."""

from utils import config


# Central list storing detected fraud/anomaly alerts
fraud_alert_registry = []


def save_and_print_report(invoice_cart):
    """Saves the session payment history to disk."""

    if not invoice_cart:
        return

    try:
        with open(config.HISTORY_PATH, "a", encoding="utf-8") as file:

            file.write(
                "\n--- CHRONOLOGICAL PAYMENT REPORT ---\n"
            )

            for element in invoice_cart:

                client = element[0]
                payment = element[2]

                file.write(
                    "Client: "
                    + client.get_name()
                    + " | Received: "
                    + str(payment)
                    + " CFA Francs.\n"
                )

    except IOError:

        print(
            "Critical error: Unable to write report to disk."
        )


def run_anti_fraud_analysis(client_dictionary):
    """OPTION 4:
    Analysis of fraud suspicions and unpaid balances.
    """

    print(
        "\n--- ANTI-FRAUD ANALYSIS AND ALERTS ---"
    )

    # Reset the list for a new analysis
    fraud_alert_registry.clear()

    for key in client_dictionary:

        client = client_dictionary[key]

        consumption = client.calculate_consumption()

        if consumption > config.MAX_CONSUMPTION_LIMIT:

            alert_text = (
                "Overconsumption alert for client "
                + client.get_name()
            )

            # Meaningful use of append()
            fraud_alert_registry.append(alert_text)

            print(
                "⚠️ MAXIMUM CONSUMPTION ALERT: "
                + client.get_name()
                + " ("
                + str(consumption)
                + " units)."
            )

        if client.get_balance() > 0:

            print(
                "ℹ️ UNPAID BALANCE ALERT: "
                + client.get_name()
                + " owes "
                + str(client.get_balance())
                + " CFA Francs."
            )

    if not fraud_alert_registry:

        print(
            "Congratulations: No anomalies detected "
            "on network meters."
        )


def display_global_dashboard(client_dictionary):
    """OPTION 6:
    Global supervision and logistics dashboard.
    """

    print("\n==================================================")
    print("      OPTION 6: GLOBAL SUPERVISION DASHBOARD")
    print("==================================================")

    # Fuel logistics monitoring
    if (
        config.FUEL_STOCK_LITERS
        <= config.CRITICAL_FUEL_THRESHOLD
    ):

        print(
            "⚠️ LOGISTICS: CRITICAL fuel stock ("
            + str(config.FUEL_STOCK_LITERS)
            + " L)!"
        )

    else:

        print(
            "✅ LOGISTICS: Stable fuel stock ("
            + str(config.FUEL_STOCK_LITERS)
            + " L)."
        )

    total_distributed_volume = 0
    total_unpaid_amount = 0

    for key in client_dictionary:

        client = client_dictionary[key]

        total_distributed_volume += (
            client.calculate_consumption()
        )

        total_unpaid_amount += (
            client.get_balance()
        )

    print("\n--- GLOBAL PERFORMANCE STATISTICS ---")

    print(
        "- Total volume distributed on the network: "
        + str(total_distributed_volume)
        + " units."
    )

    print(
        "- Total unpaid arrears: "
        + str(total_unpaid_amount)
        + " CFA Francs."
    )

    # Using the list to display a key statistic
    number_of_incidents = len(fraud_alert_registry)

    print(
        "- Number of consumption anomalies in memory: "
        + str(number_of_incidents)
    )

    print("==================================================")


# END OF SERVICES.PY
