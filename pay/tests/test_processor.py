from datetime import date
from pay.credit_card import CreditCard
from pay.processor import PaymentProcessor, luhn_checksum
import pytest
from dotenv import load_dotenv
import os
load_dotenv()


API_KEY=os.getenv("API_KEY") or ""

@pytest.fixture
def card()->CreditCard:
    year=date.today().year+2 
    return CreditCard("1249190007575069", 12, year,)

def test_card_number_invalid_luhn():
    assert not luhn_checksum("1249190007575068")

def test_api_key_validity(card:CreditCard):
        processor = PaymentProcessor(API_KEY)
        processor.charge(card,100) == True
    
def test_card_valid_date(card:CreditCard):
        processor = PaymentProcessor(API_KEY)    
        processor.charge(card,100) == True