# Copyright (c) 2024, shalindra and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Invoice(WebsiteGenerator):
    def before_save(self):
        total = 0
        for item in self.items:
            total += item.quantity * item.unit_price  

        if total > 50000:
            disc = total * (20 / 100)  
        else:
            disc = total*(10/100) 

        self.total_amount = total - disc
        self.discount = disc 
		



