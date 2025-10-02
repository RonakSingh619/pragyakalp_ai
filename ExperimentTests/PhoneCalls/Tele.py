import os

# Phone number to call
TO_NUMBER = '+919403672573'

# Trigger call via system's default telephony app
os.startfile(f'tel:{TO_NUMBER}')  # Windows only