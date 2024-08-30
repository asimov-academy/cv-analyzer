from pydantic import BaseModel

class File(BaseModel):
    file_id: str
    job_id: str