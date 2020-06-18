# Title: Waikato Air Discounter
# Author: Jack Hawinkels
# Created: 24/04/2020 10:44am
# Modified: 24/04/2020
# Version: 1

# ***IMPORTS***
import tkinter as tk

# ---IMPORTS---

# ***GLOBALS***
locations = [{
    "name": "Auckland",
    "discounted_price": 0,
    "discount" : 0
},
    {
        "name": "Wellington",
        "discounted_price": 0,
        "discount" : 0
    },
    {
        "name": "Rotorua",
        "discounted_price": 0,
        "discount" : 0
    }
]
con_master = tk.Tk()


# ---GLOBALS---

# ***CLASSES***
class Validation:
    @staticmethod
    def currency(self, action, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        # Checks if entry widget input is correct format (if entry should be currency)
        try:
            check_value = float(value_if_allowed)
            print(check_value)
            if len(value_if_allowed) > 15:
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
    def percent(self, action, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        try:
            percent = float(value_if_allowed)
            if percent > 100 or percent < 0:
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
def input_box():
    con_master.title("Waikato Air")

    val_currency = (con_master.register(Validation.currency), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    val_percent = (con_master.register(Validation.percent), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

    tk.Label(con_master, text="Please enter the discounted prices below").grid(row=1, column=1, columnspan=2)
    tk.Label(con_master, text="Discounted Price").grid(row=2, column=2)
    tk.Label(con_master, text="Discount percentage (amount taken off)").grid(row=2, column=3)
    for i in range(len(locations)):
        tk.Label(con_master, text=locations[i]["name"]).grid(column=1, row=i + 3)
        locations[i]["discounted_price"] = tk.Entry(con_master, validate='key', validatecommand=val_currency)
        locations[i]["discounted_price"].grid(column=2, row=i + 3)

        locations[i]["discount"] = tk.Entry(con_master, validate='key', validatecommand=val_percent)
        locations[i]["discount"].grid(column=3, row=i + 3)

    tk.Label(con_master, text="- -").grid(row=len(locations) + 3, column=1, columnspan=3)

    tk.Button(text="Generate text & save to clipboard", command=generate).grid(row=len(locations) + 5, column=1, columnspan=3)

    con_master.mainloop()


def generate():
    text = "******************** WAIKATO AIR *********************\n******* These saver fares are for tommorow only ******"
    for i in range(len(locations)):
        # Generate cyphers
        cypher = locations[i]["name"][0:3].upper()
        reduced_fare = format(float(locations[i]["discounted_price"].get()), '.2f')
        percentage = format(float(locations[i]["discount"].get()), '.2f')
        percentage_flt = float(locations[i]["discount"].get())
        original_fee = round((float(locations[i]["discounted_price"].get()) / (100 - percentage_flt)) * 10000) / 100
        text = text + "\n" + locations[i]["name"] + " - " + cypher + " - $" + reduced_fare + " - " + percentage + "% off original fee ($" + str(original_fee) + ") - "
        if percentage_flt <= 20:
            text = text + "Quick Saver"
        elif percentage_flt <= 50:
            text = text + "Smart Saver"
        else:
            text = text + "Super Saver"

    result_window = tk.Tk()
    results_output = tk.Text(result_window, height=len(locations) + 2, borderwidth=0)
    results_output.insert(tk.END, text)
    results_output.pack()

    # results_output.configure(state="disabled")

    # results_output.configure(inactiveselectbackground=w.cget("selectbackground"))


# ---DEFINITIONS---

# ***Main Script***

# ---Main Script---
input_box()
