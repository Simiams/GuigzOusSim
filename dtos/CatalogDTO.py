class CatalogDTO:
    def __init__(self, catalog_type, name, pokemons=None, theme=None):
        self.catalog_type = catalog_type
        self.name = name
        self.pokemons = pokemons
        # self.last_index_pokemon = len(pokemons)
        self.theme = theme

    def __str__(self):
        return f"CatalogDTO(name={self.name}, catalog_type={self.catalog_type}, pokemons={self.pokemons}, theme={self.theme})"