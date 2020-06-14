# Title: Waikato Air Discounter
# Author: Jack Hawinkels
# Created: 24/04/2020 10:44am
# Modified: 30/04/2020
# Version: 3

# ***IMPORTS***
import tkinter as tk
import json
import copy

# ---IMPORTS---

# ***GLOBALS***
with open('assets/json/locations.json') as f:
    locations = json.load(f)

master = tk.Tk()
new_location_dialog_input = ""

# ---GLOBALS---

# Constant for default locations
loc_default = [
    {
        "name": "Auckland",
        "discounted_price": 0,
        "discount": 0
    },
    {
        "name": "Wellington",
        "discounted_price": 0,
        "discount": 0
    },
    {
        "name": "Rotorua",
        "discounted_price": 0,
        "discount": 0
    }
]


# ***CLASSES***

# This class stores definitions that help validate the input fields
class Validation:
    @staticmethod
    # This definition validates that an input is in correct format to be a currency
    def currency(self, action, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        # Checks if entry widget input is correct format (if entry should be currency)
        try:
            check_value = float(value_if_allowed)
            print(check_value)
            #  len(value_if_allowed.split(" ")) > 1 -- Prevents user from entering spaces
            if check_value <= 0 or len(value_if_allowed.split(" ")) > 1:
                return False
            elif len(value_if_allowed) > 15:
                # Exceeds maximum length
                return False
            # Calculation compensates for slight inaccuracies when calculating with floats
            elif (round(check_value * 100) == check_value * 100) or round(check_value * 100) == (
                    check_value * 100 - 0.000000000001) or round(check_value * 100) == (
                    check_value * 100 + 0.000000000001):
                return True
            else:
                return False
        except:
            if value_if_allowed == "":
                return True
            else:
                return False

    @staticmethod
    # This definition helps validate percentage entry fields.
    def percent(self, action, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        try:
            percent = float(value_if_allowed)
            if percent >= 100 or percent < 0 or len(value_if_allowed.split(" ")) > 1:
                return False
            else:
                return True
        except:
            if value_if_allowed == "":
                return True
            else:
                return False


# ---CLASSES---

# ***DEFINITIONS***

# This definiton build the main window
def main_window():
    master.title("Waikato Air")

    val_currency = (master.register(Validation.currency), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    val_percent = (master.register(Validation.percent), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

    if len(locations) == 0:
        # Print this if there are no stored locations
        tk.Label(master, text="There are no stored locations at the momment. To get started, add one or restore the defaults.").grid(row=1, column=1, columnspan=2)
        tk.Button(text="Add location", command=new_location_dialog).grid(row=2, column=1)
        tk.Button(text="Restore Default", command=default_all).grid(row=2, column=2)
    else:
        # There are stored locations, so print them.
        tk.Label(master, text="Please enter the discounted prices below").grid(row=1, column=1, columnspan=2)
        tk.Label(master, text="Discounted Price ($)").grid(row=2, column=2)
        tk.Label(master, text="Discount percentage (amount taken off)(%)").grid(row=2, column=3)

        for i in range(len(locations)):
            tk.Label(master, text=locations[i]["name"]).grid(column=1, row=i + 3)
            locations[i]["discounted_price"] = tk.Entry(master, validate='key', validatecommand=val_currency)
            locations[i]["discounted_price"].grid(column=2, row=i + 3)

            locations[i]["discount"] = tk.Entry(master, validate='key', validatecommand=val_percent)
            locations[i]["discount"].grid(column=3, row=i + 3)

            tk.Button(master, text="delete", command=generate_delete_button(i)).grid(column=4, row=i + 3)

        tk.Label(master, text="- -").grid(row=len(locations) + 3, column=1, columnspan=3)

        tk.Button(text="Generate text & save to clipboard", command=generate).grid(row=len(locations) + 5, column=1,
                                                                                   columnspan=3)
        tk.Button(text="Add location", command=new_location_dialog).grid(row=len(locations) + 6, column=1, columnspan=2)
        tk.Button(text="Restore Default", command=default_all).grid(row=len(locations) + 6, column=3)

    master.mainloop()


# This definition generates the output text and shows it in a window where it can be copied
def generate():
    text_lines = []
    empty = False
    for i in range(len(locations)):
        # Generate cyphers
        if locations[i]["discounted_price"].get() == "" or locations[i]["discount"].get() == "":
            # A field is empty
            empty = True
            break

        cypher = locations[i]["name"][0:3].upper()
        reduced_fare = format(float(locations[i]["discounted_price"].get()), '.2f')
        percentage = format(float(locations[i]["discount"].get()), '.2f')
        percentage_flt = float(locations[i]["discount"].get())
        original_fee = round((float(locations[i]["discounted_price"].get()) / (100 - percentage_flt)) * 10000) / 100
        text_lines.append(cypher + " - " + locations[i][
            "name"] + " - $" + reduced_fare + " - " + percentage + "% off original fee ($" + str(
            original_fee) + ") - ")

        if percentage_flt <= 20:
            text_lines[-1] = text_lines[-1] + "Quick Saver"
        elif percentage_flt <= 50:
            text_lines[-1] = text_lines[-1] + "Smart Saver"
        else:
            text_lines[-1] = text_lines[-1] + "Super Saver"

    result_window = tk.Tk()
    if empty == False:
        result_window.title("Generated Text")

        width = len(max(text_lines, key=len))
        print(max(text_lines))
        print(text_lines)
        # The following calculation calcualtes the exact number of stars that need to be printed so that these fit on one line
        text_lines.insert(0, ("*" * round((width - 13) / 2)) + " WAIKATO AIR " + ("*" * round((width - 13) / 2)))
        text_lines.insert(1, ("*" * round((width - 41) / 2)) + " These saver fares are for tomorrow only " + (
                    "*" * round((width - 41) / 2)))

        tk.Label(result_window, text="Highlight & copy the text bellow").grid(row=1, column=1)
        results_output = tk.Text(result_window, width=width + 2, borderwidth=0)
        results_output.insert(tk.END, "\n".join(text_lines))
        results_output.grid(row=2, column=1)
    else:
        result_window.title("Error")
        tk.Label(result_window, text="Please fill in all fields before generating text.").pack()

    # results_output.configure(state="disabled")

    # results_output.configure(inactiveselectbackground=w.cget("selectbackground"))


# This definiton shows a window that allows the user to add new locations
def new_location_dialog():
    global master
    global new_location_dialog_input
    master.destroy()

    master = tk.Tk()
    master.title("Add a location")

    tk.Label(master, text="Enter the new location's name:").grid(row=1, column=1, columnspan=2)
    new_location_dialog_input = tk.Entry(master)
    new_location_dialog_input.grid(row=2, column=1, columnspan=2)

    tk.Button(master, text="Cancel", command=cancel_new_location).grid(row=3, column=1)
    tk.Button(master, text="Add", command=new_location).grid(row=3, column=2)


# This definiton grabs information from the window opened by new_location_dialog() and saves it
class new_location:
    def __init__(self):
        global master
        global new_location_dialog_input

        if new_location_dialog_input.get() != "":
            self.new_location_name = new_location_dialog_input.get()
            if self.new_location_name != self.new_location_name.title():
                self.verify_input()
            else:
                # Input is already titlecase
                self.save_input()

                # Close the master window
                master.destroy()

                # Reopen the master window
                master = tk.Tk()
                main_window()

    def verify_input(self):
        self.verify_window = tk.Tk()
        self.verify_window.title("Please verify")
        tk.Label(self.verify_window, text=self.new_location_name+"\n\nAre you sure that this is correct?").grid(row=1,column=1,columnspan=2)
        tk.Button(self.verify_window, text="No", command=self.verify_deny).grid(row=2, column=1)
        tk.Button(self.verify_window, text="Yes", command=self.verify_accept).grid(row=2, column=2)
    
    def verify_accept(self):
        global master

        self.verify_window.destroy()
        self.save_input()
        master.destroy()
        master = tk.Tk()
        main_window()

    def verify_deny(self):
        self.verify_window.destroy()

    def save_input(self):
        # Add the new location to the list, and save it
        locations.append({
            "name": self.new_location_name,
            "discounted_price": 0,
            "discount": 0
        })

        locations_temp = locations
        for location in locations_temp:
            location["discounted_price"] = 0
            location["discount"] = 0

        with open('assets/json/locations.json', 'w') as json_file:
            json.dump(locations_temp, json_file)


# This definition allows the user to cancel out of creating a new location if they wish
def cancel_new_location():
    global master

    # Close the master window
    master.destroy()

    # Reopen the master window
    master = tk.Tk()
    main_window()


# Returns a definiton that delete buttons can use to delete specific locations
def generate_delete_button(id):
    def temp_delete():
        global locations
        global master

        del locations[id]

        # Save the new locations list
        locations_temp = locations
        for location in locations_temp:
            location["discounted_price"] = 0
            location["discount"] = 0

        with open('assets/json/locations.json', 'w') as json_file:
            json.dump(locations_temp, json_file)

        # Re-print the master window
        master.destroy()
        master = tk.Tk()
        main_window()

    return temp_delete


# function to default all locations
def default_all():
    global master
    global locations
    global loc_default
    master.destroy()

    locations = []
    locations = copy.deepcopy(loc_default)

    # Save to file
    locations_temp = locations
    for location in locations_temp:
        location["discounted_price"] = 0
        location["discount"] = 0

    with open('assets/json/locations.json', 'w') as json_file:
        json.dump(locations_temp, json_file)

    # Re-open the main window
    master = tk.Tk()
    main_window()


# ---DEFINITIONS---

# ***Main Script***

# ---Main Script---
main_window()
