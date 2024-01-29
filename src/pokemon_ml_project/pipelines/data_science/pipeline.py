"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.2
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import split_data, fit_best_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=split_data,
            inputs=["model_input", "params:test_data_ratio"],
            outputs={"train_x": "X_train", "train_y": "y_train", "test_x": "X_test", "test_y": "y_test"}
        ),
        node(
            func=fit_best_model,
            inputs=["X_train", "y_train", "X_test", "y_test", "params:primary_type_models"],
            outputs=['primary_type_classifier', 'model_name']
        )
    ])
