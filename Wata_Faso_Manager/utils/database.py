# DATABASE.PY

"""Data persistence management module for WattaFaso-Manager."""

from utils import config
from models import models


def load_database():
    """Loads the subscriber registry from the text storage file."""

    client_dictionary = {}

    try:

        with open(
            config.STOCK_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            for line_number, line in enumerate(file, 1):

                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                segments = cleaned_line.split(";")

                # CRITICAL FIX C:
                # Explicit structure validation
                if len(segments) != 6:

                    print(
                        "Error Line "
                        + str(line_number)
                        + ": Invalid structure ("
                        + str(len(segments))
                        + "/6 columns). "
                        + "Line ignored."
                    )

                    continue

                try:

                    client_type = segments[0]
                    identifier = segments[1]
                    client_name = segments[2]

                    previous_index = int(segments[3])
                    current_index = int(segments[4])

                    balance = float(segments[5])

                    if client_type == "SOCIAL":

                        client_object = (
                            models.SocialSubscriber(
                                identifier,
                                client_name,
                                previous_index,
                                current_index,
                                balance
                            )
                        )

                        client_dictionary[
                            identifier
                        ] = client_object

                    elif client_type == "COMMERCIAL":

                        client_object = (
                            models.CommercialSubscriber(
                                identifier,
                                client_name,
                                previous_index,
                                current_index,
                                balance
                            )
                        )

                        client_dictionary[
                            identifier
                        ] = client_object

                    else:

                        print(
                            "Warning Line "
                            + str(line_number)
                            + ": Unknown subscriber type '"
                            + str(client_type)
                            + "'."
                        )

                except ValueError:

                    print(
                        "Error Line "
                        + str(line_number)
                        + ": Corrupted numeric data."
                    )

                    continue

    except FileNotFoundError:

        print(
            "Note: Storage file not found. "
            "It will be created automatically."
        )

    return client_dictionary


def save_database(client_dictionary):
    """Saves the current state of the dictionary to the storage file."""

    try:

        with open(
            config.STOCK_PATH,
            "w",
            encoding="utf-8"
        ) as file:

            for key in client_dictionary:

                client = client_dictionary[key]

                if isinstance(
                    client,
                    models.SocialSubscriber
                ):

                    label = "SOCIAL"

                elif isinstance(
                    client,
                    models.CommercialSubscriber
                ):

                    label = "COMMERCIAL"

                else:

                    continue

                line = (
                    label + ";"
                    + client.get_code() + ";"
                    + client.get_name() + ";"
                    + str(client.get_previous_index()) + ";"
                    + str(client.get_current_index()) + ";"
                    + str(client.get_balance()) + "\n"
                )

                file.write(line)

    except IOError:

        print(
            "Critical error: Unable to write data to disk."
        )


# END OF DATABASE.PY 
