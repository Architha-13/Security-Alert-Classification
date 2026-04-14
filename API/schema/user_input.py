from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated
from API.config.details import Category, Sub_category, Impact, Type, Priority

class Alert(BaseModel):
    category_input: Annotated[str, Field(description="Category of the alert", example="Email Sec")]
    impact_input: Annotated[str, Field(description="Impact level of the alert", example="High")]
    priority_input: Annotated[str, Field(description="Priority level of the alert", example="Urgent")]
    type_input: Annotated[str, Field(description="Type of the alert", example="Incident")]
    Created_time: Annotated[str, Field(description="Creation time of the alert in ISO format", example="2024-01-01T00:00:00Z")]    
    Due_by_Time: Annotated[str, Field(description="Due by time of the alert in ISO format", example="2024-01-02T00:00:00Z")]
    sub_category_input: Annotated[str, Field(description="Sub-category of the alert", example="Spam")]
    Status: Annotated[str, Field(description="Status of the alert", example="Report has been reviewed and remediation is in progress")]

    @field_validator('category_input')
    @classmethod
    def validate_category(cls, value):
        if value not in Category:
            raise ValueError(f"Invalid category: {value}")
        return Category[value]

    @field_validator('sub_category_input')
    @classmethod
    def validate_sub_category(cls, value):
        if value not in Sub_category:
            raise ValueError(f"Invalid sub-category: {value}")
        return Sub_category[value]

    @field_validator('impact_input')
    @classmethod
    def validate_impact(cls, value):
        if value not in Impact:
            raise ValueError(f"Invalid impact: {value}")
        return Impact[value]

    @field_validator('type_input')
    @classmethod
    def validate_type(cls, value):
        if value not in Type:
            raise ValueError(f"Invalid type: {value}")
        return Type[value]

    @field_validator('priority_input')
    @classmethod
    def validate_priority(cls, value):
        if value not in Priority:
            raise ValueError(f"Invalid priority: {value}")
        return Priority[value]

    @computed_field
    @property
    def time_to_close_seconds(self) -> int:
        from datetime import datetime
        created_time = datetime.fromisoformat(self.Created_time)
        due_by_time = datetime.fromisoformat(self.Due_by_Time)
        return int((due_by_time - created_time).total_seconds())