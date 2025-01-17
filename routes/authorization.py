from config.data import *

@router.get("/authorize/")
async def authorize(bank_name: str, consent_id: str):
    if bank_name not in BANK_FUNCTIONS:
        raise HTTPException(status_code=404, detail="Bank not supported")

    bank = BANK_FUNCTIONS[bank_name]()
    
    # Construct the authorization URL with the consent_id
    auth_url = (
        f"{bank['AUTH_URL']}?"
        f"client_id={bank['CLIENT_ID']}&"
        f"response_type=code id_token&"
        f"scope=openid accounts&"
        f"redirect_uri={bank['REDIRECT_URI']}&"
        f"request={consent_id}"
    )
    print(auth_url)
    
    return RedirectResponse(url=auth_url)