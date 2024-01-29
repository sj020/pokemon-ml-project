"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.2
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import create_model_input


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=create_model_input,
            inputs="pokemon_database_best_generation_with_images",
            outputs=["model_input", "label_encoder"]
        )
    ])
