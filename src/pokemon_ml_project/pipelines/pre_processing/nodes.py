"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.19.2
"""

import os
import pandas as pd

"""Node for filtering data and cleaning Columns"""
def clean_pokemon_dateset(df:pd.DataFrame, selected_generations:list, remove_legendary:bool=True) -> pd.DataFrame:
    
    # Filter only best generations
    df = df[df.generation.isin(selected_generations)]

    # Removing Legendary's (Hard Coded)
    if remove_legendary:
        df = df[df.is_legendary == 0]

    # Rename type columns
    df = df.rename(columns={"type1": "primary_type", "type2": "secondary_type"})

    # Dropping NA values
    df = df.dropna()

    return df
    
"""Node for adding image"""
def add_pokemon_image(pokemon_stats: pd.DataFrame, image_directory: str = './data/01_raw/images'):
    
    # Listing the directory of images
    imgs = os.listdir(image_directory)

    # Creating a dataframe of image filenames
    pokemon_filenames = pd.DataFrame([[x.split('.')[0].split('-')[0] for x in imgs], imgs]).T
    pokemon_filenames.columns = ['name', 'filepath']
    pokemon_filenames.set_index('name')

    # Cleaning some filename
    pokemon_filenames['name'].replace(
        {
            'farfetchd': "farfetch'd",
            'flabebe': 'flabébé',
            'hakamo': 'hakamo-o',
            'ho': 'ho-oh',
            'jangmo': 'jangmo-o',
            'kommo': 'kommo-o',
            'mr': 'mr. mime',
            'mime': 'mime jr.',
            'type': 'type: null'
        },
        inplace=True
    )

    pokemon_filenames.loc[
        pokemon_filenames['filepath'] == 'nidoran-f.png', 'name'
    ] = 'nidoran (f)'
    pokemon_filenames.loc[
        pokemon_filenames['filepath'] == 'nidoran-m.png', 'name'
    ] = 'nidoran (m)'
    pokemon_filenames.loc[
        pokemon_filenames['filepath'] == 'tapu-fini.jpg', 'name'
    ] = 'tapu fini'
    pokemon_filenames.loc[
        pokemon_filenames['filepath'] == 'tapu-koko.jpg', 'name'
    ] = 'tapu koko'
    pokemon_filenames.loc[
        pokemon_filenames['filepath'] == 'tapu-bulu.jpg', 'name'
    ] = 'tapu bulu'
    pokemon_filenames.loc[
        pokemon_filenames['filepath'] == 'tapu-lele.jpg', 'name'
    ] = 'tapu lele'
    pokemon_filenames.loc[
        pokemon_filenames['filepath'] == 'porygon-z.png', 'name'
    ] = 'porygon-z'

    # Making names compatible
    pokemon_stats['name'] = pokemon_stats['name'].str.lower()
    pokemon_stats['name'].replace(
        {
            'nidoran♀': 'nidoran (f)',
            'nidoran♂': 'nidoran (m)'
        },
        inplace=True
    )

    # Joining data frames
    pokemon_joined = pokemon_stats.merge(pokemon_filenames, how='inner', on='name')

    return pokemon_joined
