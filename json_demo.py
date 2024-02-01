import json

class ProgrammingLanguageManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    
    def load_data(self):
        with open(self.file_path) as f:
            self.data = json.load(f)
            return self.data['programmingLanguages']
          
    
    def remove_paradigms(self):
        for language in self.data['programmingLanguages']:
            del language['paradigms']
    
    def save_data(self, output_file_path):
        with open(output_file_path, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    @property
    def programming_languages(self):
        return self.data['programmingLanguages']
    
    @property
    def language_count(self):
        return len(self.data['programmingLanguages'])
        
# # Create an instance of ProgrammingLanguageManager
# manager = ProgrammingLanguageManager('data/programming_language.json')

# # Load the data from the JSON file
# manager.load_data()

# # Remove the 'paradigms' key from each language
# manager.remove_paradigms()

# # Save the modified data to a new JSON file
# manager.save_data('data/new_programming_language.json')
