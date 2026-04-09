from math import nan


Category={'Backup Management': 0, 'Cast': 1, 'Check': 2, 'Cloud Security': 3, 'Data Security': 4, 'Email Sec': 5, 'External': 6, 'Info & Event Management': 7, 'Infrastructure': 8, 'Internet': 9, 'License Management': 10, 'Monitoring': 11, 'PAM': 12, 'Patch Management': 13, 'Servers': 14, 'Tool': 15, 'Vulnarability Management': 16, 'Zoom': 17}

Sub_category={'Access': 0, 'Adhoc Task': 1, 'Connectivity': 2, 'Incident': 3, 'Issue': 4, 'Permit': 5, 'Reports': 6, 'Rrequest': 7, 'Scheduled Task': 8, 'Service Request': 9, 'Spam': 10, 'Unknown': 11, 'Zoom Room': 12}

Impact={'High': 0, 'Low': 1, 'Medium': 2}

Type={'Incident': 0, 'Service Request': 1}

Priority={'High': 0, 'Low': 1, 'Medium': 2, 'Urgent': 3}

class_labels = ["Benign", "False Positive", "Report", "True Positive", "Wireless"]