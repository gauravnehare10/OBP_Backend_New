from config.data import *

@router.post("/exchange-token/")
async def exchange_token(code: str, bank_name: str):
    if bank_name not in BANK_FUNCTIONS:
        raise HTTPException(status_code=404, detail="Bank not supported")

    bank = BANK_FUNCTIONS[bank_name]()
    
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": bank["REDIRECT_URI"],
        "client_id": bank["CLIENT_ID"],
        "client_secret": bank["CLIENT_SECRET"],
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(bank["TOKEN_URL"], data=payload)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        
    return response.json()