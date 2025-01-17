from pydantic import BaseModel

class TokenExchangeRequest(BaseModel):
    code: str
    bank_name: str