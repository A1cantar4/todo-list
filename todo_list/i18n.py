import json
import os

class I18n:
    def __init__(self, lang="pt"):
        self.lang = lang
        self.translations = {}
        self.load_language(lang)
        
    def load_language(self, lang):
        base_path = os.path.join(os.path.dirname(__file__), "..", "settings", "locales")
        path = os.path.join(base_path, f"{lang}.json")
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.translations = json.load(f)
            self.lang = lang
        except FileNotFoundError:
            raise ValueError(f"Arquivo '{lang}' não encontrado!")
    
    def t(self, key):
        return self.translations.get(key, key)