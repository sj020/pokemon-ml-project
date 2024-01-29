"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.19.2
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import clean_pokemon_dateset, add_pokemon_image


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=clean_pokemon_dateset,
            inputs=["pokemon_database","params:pokemon_best_generations"],
            outputs="pokemon_database_best_generation"
        ),
        node(
            func=add_pokemon_image,
            inputs="pokemon_database_best_generation",
            outputs="pokemon_database_best_generation_with_images"
        )
    ])
