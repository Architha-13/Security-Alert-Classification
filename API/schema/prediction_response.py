from pydantic import BaseModel, Field
from typing import Dict


class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="Predicted alert classification category",
        example="High"
    )
    confidence: float = Field(
        ...,
        description="Model's confidence score for the predicted class (range: 0 to 1)",
        example=0.8432
    )
    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probability distribution across all possible classes",
        example={'Benign': 0.1, 'False Positive': 0.2, 'Report': 0.3, 'True Positive': 0.2, 'Wireless': 0.2}
    )