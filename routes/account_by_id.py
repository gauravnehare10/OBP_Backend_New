from config.data import *

router = APIRouter()

@router.get("/accounts/{account_id}")
async def get_account_details(account_id: str, access_token: str, bank: str):
    bank_info = get_bank_info(bank)
    url = f"{bank_info.get("API_BASE_URL")}/accounts/{account_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        data = response.json()
        # Save to MongoDB
        #accounts.insert_one({"endpoint": f"accounts/{account_id}", "response": data})

        return data