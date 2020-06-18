# Title: Waikato Air Discounter
# Author: Jack Hawinkels
# Created: 24/04/2020 10:44am
# Modified: 30/04/2020
# Version: 4

# ***IMPORTS***
import tkinter as tk
import json
import random

# ---IMPORTS---

# ***GLOBALS***
with open('assets/json/locations.json') as f:
    locations = json.load(f)

master = tk.Tk()
new_location_dialog_input = ""


# ---GLOBALS---

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
            if percent > 100 or percent < 0 or len(value_if_allowed.split(" ")) > 1:
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

    tk.Label(master, text="Please enter the discounted prices below").grid(row=1, column=1, columnspan=5)
    tk.Label(master, text="Discounted Price ($)").grid(row=2, column=3)
    tk.Label(master, text="Discount % taken off").grid(row=2, column=5)
    for i in range(len(locations)):
        tk.Label(master, text=locations[i]["name"]).grid(column=1, row=i + 3)
        tk.Label(master, text="$").grid(column=2, row=i + 3)
        locations[i]["discounted_price"] = tk.Entry(master, validate='key', validatecommand=val_currency)
        locations[i]["discounted_price"].grid(column=3, row=i + 3)
        tk.Label(master, text="  %").grid(column=4, row=i + 3)
        locations[i]["discount"] = tk.Entry(master, validate='key', validatecommand=val_percent)
        locations[i]["discount"].grid(column=5, row=i + 3)

        tk.Button(master, text="delete", command=generate_delete_button(i)).grid(column=6, row=i + 3)

    tk.Label(master, text="- -").grid(row=len(locations) + 3, column=1, columnspan=6)

    tk.Button(text="Generate text & save to clipboard", command=generate).grid(row=len(locations) + 5, column=1, columnspan=6)
    tk.Button(text="Add location", command=new_location_dialog).grid(row=len(locations) + 6, column=1, columnspan=6)

    master.mainloop()


# This definition generates the output text and shows it in a window where it can be copied
def generate():
    text = "******************** WAIKATO AIR *********************\n******* These saver fares are for tommorow only ******"
    empty = False
    for i in range(len(locations)):
        # Generate cyphers
        if locations[i]["discounted_price"].get() == "" or locations[i]["discount"].get() == "":
            # A field is empty
            empty = True
            break

        cypher = locations[i]["name"][0:3].upper() + str(random.randint(100, 999))
        reduced_fare = format(float(locations[i]["discounted_price"].get()), '.2f')
        percentage = format(float(locations[i]["discount"].get()), '.2f')
        percentage_flt = float(locations[i]["discount"].get())
        original_fee = round((float(locations[i]["discounted_price"].get()) / (100 - percentage_flt)) * 10000) / 100
        text = text + "\n The fare for flight '" + cypher + "' to " + locations[i][
            "name"] + " is $" + reduced_fare + " - " + percentage + "% off original fee ($" + str(
            original_fee) + ") - "
        if percentage_flt <= 20:
            text = text + "Quick Saver"
        elif percentage_flt <= 50:
            text = text + "Smart Saver"
        else:
            text = text + "Super Saver"

    result_window = tk.Tk()
    if empty == False:
        tk.Label(result_window, text="Highlight & copy the text bellow").grid(row=1, column=1)
        results_output = tk.Text(result_window, height=len(locations) + 2, borderwidth=0)
        results_output.insert(tk.END, text)
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
def new_location():
    global master
    global new_location_dialog_input

    if new_location_dialog_input.get() != "":
        # Add the new location to the list, and save it
        locations.append({
            "name": new_location_dialog_input.get(),
            "discounted_price": 0,
            "discount": 0
        })

        locations_temp = locations
        for location in locations_temp:
            location["discounted_price"] = 0
            location["discount"] = 0

        with open('assets/json/locations.json', 'w') as json_file:
            json.dump(locations_temp, json_file)

        # Close the master window
        master.destroy()

        # Reopen the master window
        master = tk.Tk()
        main_window()


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

def exit():
    # Allows user to use Cmd + Q on a mac to close the program.
    master.destroy()
# ---DEFINITIONS---

# ***Main Script***

# ---Main Script---
main_window()