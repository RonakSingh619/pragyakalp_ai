# import socket
# import psutil

# def is_connected():
#     """
#     Checks if the machine has internet connectivity.
#     Tries connecting to Google's web server (port 80).
#     """
#     try:
#         socket.create_connection(("www.google.com", 80), timeout=3)
#         return True
#     except OSError:
#         return False

# # def is_ethernet_connected():
# #     """
# #     Detects if there is an active Ethernet connection.
# #     Looks for typical Ethernet interface names and if they are up.
# #     """
# #     interfaces = psutil.net_if_stats()
# #     for iface_name, iface_stats in interfaces.items():
# #         if iface_stats.isup and any(keyword in iface_name.lower() for keyword in ['eth', 'en', 'ethernet']):
# #             return True
# #     return False

# def check_internet_and_ethernet():
#     """
#     Combines internet and Ethernet checks.
#     Returns a dictionary with the results.
#     """
#     return {
#         "internet": is_connected(),
#         # "ethernet_connected": is_ethernet_connected()
#     }

# # Example usage
# if __name__ == "__main__":
#     result = check_internet_and_ethernet()
#     print("Internet Connected:", result["internet"])
#     # print("Ethernet Connected:", result["ethernet_connected"])

txt = """
Shivaji I (Shivaji Shahaji Bhonsale, Marathi pronunciation: [ʃiˈʋaːdʑiː ˈbʱos(ə)le]; c. 19 February 1630 – 3 April 1680)[6] was an Indian ruler and a member of the Bhonsle dynasty.[7] Shivaji carved out his own independent kingdom from the Sultanate of Bijapur that formed the genesis of the Maratha Empire. In 1674, he was formally crowned the Chhatrapati of his realm at Raigad Fort.[8]

Shivaji offered passage and his service to the Mughal emperor Aurangzeb to invade the declining Sultanate of Bijapur. After Aurangzeb's departure for the north due to a war of succession, Shivaji conquered territories ceded by Bijapur in the name of the Mughals.[9]: 63  Following his defeat at the hands of Jai Singh I, the senior most general ("Mirza Raja") of the Mughal Empire, in the Battle of Purandar, Shivaji entered into vassalage with the Mughal empire, assuming the role of a Mughal chief and was conferred with the title of Raja by Aurangzeb.[10] He undertook military expeditions on behalf of the Mughal Empire for a brief duration.[11] Over the course of his life, Shivaji engaged in both alliances and hostilities with the Mughal Empire, the Sultanate of Golconda, the Sultanate of Bijapur and the European colonial powers. 
"""

srch = 'Bijapur'

if srch.lower() in txt.lower():
    print("Found")
else:
    print("Not Found")