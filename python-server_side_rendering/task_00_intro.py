import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Invalid input type. Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Invalid input type. Attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output_content = template
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            output_content = output_content.replace(f"{{{placeholder}}}", str(value))
        
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as out_file:
            out_file.write(output_content)
