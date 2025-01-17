from config.data import *

@router.get("/accounts")
async def get_accounts(access_token: str, bank: str):
    bank_info = get_bank_info(bank)
    url = f"{bank_info.get("API_BASE_URL")}/accounts"
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/x-www-form-urlencoded"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        data = response.json()
        # Save to MongoDB
        #accounts.insert_one({"endpoint": "accounts", "response": data})

        return data


