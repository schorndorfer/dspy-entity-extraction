"""Command-line interface for DSPy Entity Extraction."""

from typing import Annotated, Optional
import cyclopts


app = cyclopts.App(
    name="dspy-entity-extraction",
    help="A CLI tool for entity extraction using DSPy framework"
)


@app.command
def extract(
    text: Annotated[str, cyclopts.Parameter(help="Text to extract entities from")],
    model: Annotated[Optional[str], cyclopts.Parameter(help="Model to use for extraction")] = None,
    output_format: Annotated[str, cyclopts.Parameter(help="Output format (json|text)")] = "json",
    confidence_threshold: Annotated[float, cyclopts.Parameter(help="Minimum confidence threshold")] = 0.5,
):
    """Extract entities from the provided text."""
    print(f"Extracting entities from: {text}")
    print(f"Model: {model or 'default'}")
    print(f"Output format: {output_format}")
    print(f"Confidence threshold: {confidence_threshold}")

    # TODO: Implement actual entity extraction logic
    print("Entity extraction not yet implemented")


@app.command
def train(
    dataset: Annotated[str, cyclopts.Parameter(help="Path to training dataset")],
    output_dir: Annotated[str, cyclopts.Parameter(help="Output directory for trained model")] = "./models",
    epochs: Annotated[int, cyclopts.Parameter(help="Number of training epochs")] = 10,
):
    """Train a new entity extraction model."""
    print(f"Training model with dataset: {dataset}")
    print(f"Output directory: {output_dir}")
    print(f"Epochs: {epochs}")

    # TODO: Implement training logic
    print("Model training not yet implemented")


@app.command
def evaluate(
    model_path: Annotated[str, cyclopts.Parameter(help="Path to model to evaluate")],
    test_dataset: Annotated[str, cyclopts.Parameter(help="Path to test dataset")],
):
    """Evaluate model performance on test dataset."""
    print(f"Evaluating model: {model_path}")
    print(f"Test dataset: {test_dataset}")

    # TODO: Implement evaluation logic
    print("Model evaluation not yet implemented")


@app.command
def version():
    """Show version information."""
    from dspy_entity_extraction import __version__
    print(f"dspy-entity-extraction version {__version__}")


def main():
    """Main entry point for the CLI application."""
    app()


if __name__ == "__main__":
    main()