from django import forms

class staff_form(forms.Form):
    Staff_Name= forms.CharField
    Staff_Address=forms.CharField
    Staff_Pancard=forms.CharField
    Staff_Aadhaar= forms.CharField
    Staff_phoneno= forms.CharField

class customer_form(forms.Form):
    customer_name= forms.CharField
    Customer_Address=forms.CharField
    Customer_Pancard=forms.CharField
    Cutomer_Aadhaar_No= forms.CharField
    Customer_Phone_No= forms.CharField

