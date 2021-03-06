from __future__ import annotations

from pydantic import BaseModel, Field
from ..schemas.datamodel import Document
from core.annotation_modul.datamodels.knowledge_object_model import KnowledgeObject
from core.annotation_modul.datamodels.annotation_model import Annotation
from typing import List


class DocumentAnalysis(BaseModel):
    """ A Dataclass containg all the data """
    document: Document
    annotations: List[Annotation] = []
    knowledgeObjects: List[KnowledgeObject] = []

    class Config:
        # Allows to use Classes that are not validated
        arbitrary_types_allowed = True

    def to_output_model(self) -> Document:
        """ Saves the data as an ExtractedData-Object. """
        return self.document
