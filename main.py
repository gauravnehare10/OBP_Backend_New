from fastapi import FastAPI
from routes import create_consent, authorization, exchange_token, accounts, account_by_id, transactions_by_id, beneficiaries_by_id, balances_by_id, direct_debits_by_id, standing_orders_by_id, product_by_id, scheduled_payments_by_id, statements_by_id, offers_by_id
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(create_consent.router)
app.include_router(authorization.router)
app.include_router(exchange_token.router)
app.include_router(accounts.router)
app.include_router(account_by_id.router)
app.include_router(transactions_by_id.router)
app.include_router(beneficiaries_by_id.router)
app.include_router(balances_by_id.router)
app.include_router(direct_debits_by_id.router)
app.include_router(standing_orders_by_id.router)
app.include_router(product_by_id.router)
app.include_router(scheduled_payments_by_id.router)
app.include_router(statements_by_id.router)
app.include_router(offers_by_id.router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust the frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)