from config.data import *

@router.post("/create-consent/")
async def create_consent(bank_name: str):
    if bank_name not in BANK_FUNCTIONS:
        raise HTTPException(status_code=404, detail="Bank not supported")

    bank = BANK_FUNCTIONS[bank_name]()
    # Step 1: Get the access token using client credentials
    payload = {
        "grant_type": "client_credentials",
        "client_id": bank["CLIENT_ID"],
        "client_secret": bank["CLIENT_SECRET"],
        "scope": "accounts",
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(bank["TOKEN_URL"], data=payload)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        access_token = response.json().get("access_token")

    # Step 2: Create Account Access Consent with the access token
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    consent_payload = {
        "Data": {
            "Permissions": [
                "ReadAccountsDetail",
                "ReadBalances",
                "ReadBeneficiariesDetail",
                "ReadDirectDebits",
                "ReadProducts",
                "ReadStandingOrdersDetail",
                "ReadTransactionsCredits",
                "ReadTransactionsDebits",
                "ReadTransactionsDetail",
                "ReadScheduledPaymentsBasic",
                "ReadScheduledPaymentsDetail",
                "ReadStatementsBasic", 
                "ReadStatementsDetail",
                "ReadOffers"
            ]
        },
        "Risk": {},
    }

    async with httpx.AsyncClient() as client:
        consent_response = await client.post(
            f"{bank['API_BASE_URL']}/account-access-consents",
            headers=headers,
            json=consent_payload,
        )
        if consent_response.status_code != 201:
            raise HTTPException(status_code=consent_response.status_code, detail=consent_response.text)

        consent_data = consent_response.json()
        print(consent_data)
        consent_id = consent_data["Data"]["ConsentId"]
        return {"consent_id": consent_id}