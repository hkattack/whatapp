import pipreqs

def generate_requirements_file(project_directory):
    pipreqs.pipreqs(project_directory)

# Usage example
project_directory = 'C:\\Users\\Hp\OneDrive\\Projects\\whatapp_chat_anyliser'
generate_requirements_file(project_directory)
