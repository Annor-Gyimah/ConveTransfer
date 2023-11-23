def load_language_config(self):
    try:
        with open(self.language_config_file, 'r', encoding='utf-8') as config_file:
            #print(config_file.read().strip())
            
            return config_file.read().strip()
        
            
    except FileNotFoundError:
        return 'en'

def save_language_config(self, language):
    try:
        with open(self.language_config_file, 'w', encoding='utf-8') as config_file:
            config_file.write(language)
        return language
    except Exception as e:
        print(f"Error saving language configuration: {e}")
        return language