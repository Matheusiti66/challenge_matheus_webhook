import os
import starkbank
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), 'core', '.env')
load_dotenv(dotenv_path)

class StarkBank:
    
    def __init__(self):
        starkbank.user = starkbank.Project(
                            environment="sandbox",
                            id=os.getenv("PROJECT_ID"),
                            private_key=os.getenv("PRIVATE_KEY")
                        )


    def calculate_tax(self, amount, fine_tax, interest_tax):
        """responsible for calculating fees before sending the transfer

        Args:
            amount (int): amount of transact
            fine_tax (float): tax of fine
            interest_tax (float): tax of interest

        Returns:
            int: calculated amount of the amount to be transferred
        """
        fine = amount * (fine_tax / 100)
        interest = amount * (interest_tax / 100)
        amount = int((amount - fine - interest)*100)
        return amount
        
        
        
    def send_transfer(self, data):
        """responsible for receiving the webhook payload and creating the transfer submission

        Args:
            data (obj): object with paid invoice data received by the webhook

        Returns:
            json: transfer status information
        """
        amount = self.calculate_tax(amount=data['event']['log']['invoice']['amount'],
                                    fine_tax=data['event']['log']['invoice']['fine'],
                                    interest_tax=data['event']['log']['invoice']['interest'])
        try:
            starkbank.transfer.create([
                            starkbank.Transfer(
                                amount=amount,
                                bank_code="20018183",
                                branch_code="0001",
                                account_number="6341320293482496",
                                account_type="payment",
                                tax_id="20.018.183/0001-80",
                                name="Stark Bank SA"
                        )])
            return {"message":"the transfer has been sent",
                    "status": "OK",
                    "statusCode": 200}
        
        except Exception as Err:
            return {"message":Err,
                    "status": "NOK",
                    "statusCode": 500}
