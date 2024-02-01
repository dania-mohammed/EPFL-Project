import json

class ProgrammingLanguageManager:
    def __init__(self, file_path):
        self.file_path = file_path  # Initialize the file path attribute
        self.data = None  # Initialize the data attribute as None
    
    def load_data(self):
        with open(self.file_path) as f:  # Open the file for reading
            self.data = json.load(f)  # Load the JSON data from the file
            return self.data['programmingLanguages']  # Return the list of programming languages
    
    def remove_paradigms(self):
        for language in self.data['programmingLanguages']:  # Iterate through the programming languages
            del language['paradigms']  # Remove the 'paradigms' key from each language
    
    def save_data(self, output_file_path):
        with open(output_file_path, 'w') as f:  # Open the output file for writing
            json.dump(self.data, f, indent=2)  # Write the JSON data to the output file with indentation
    
    @property
    def programming_languages(self):
        return self.data['programmingLanguages']  # Return the list of programming languages
    
    @property
    def language_count(self):
        return len(self.data['programmingLanguages'])  # Return the count of programming languages in the data
