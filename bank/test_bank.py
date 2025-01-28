import unittest
from bank import Bank

class TestBank(unittest.TestCase):

    def setUp(self):
        """Set up the test environment before each test."""
        self.bank = Bank()

    def test_deposit(self):
        """Test the deposit functionality."""
        self.bank.deposit(100)
        self.assertGreater(self.bank.bal, 0, "Deposit should increase balance")

    def test_withdraw_sufficient_funds(self):
        """Test withdrawal with sufficient funds."""
        self.bank.bal = 100
        self.bank.withdraw(50)
        self.assertEqual(self.bank.bal, 50, "Withdrawal should reduce balance")

    def test_withdraw_insufficient_funds(self):
        """Test withdrawal with insufficient funds."""
        self.bank.bal = 50
        self.bank.withdraw(100)
        self.assertEqual(self.bank.bal, 50, "Balance should remain the same")

    def test_show(self):
      """Test that show method returns correct value"""
      self.bank.bal = 100
      show_bal = self.bank.bal
      self.assertEqual(self.bank.bal, show_bal, "Balance should show correctly")

    def test_enquiry(self):
      """Test that the enquiry method returns correct value"""
      self.bank.bal = 100
      enq_bal = self.bank.bal
      self.assertEqual(self.bank.bal, enq_bal, "Balance should be displayed correctly")

    def test_credit(self):
      """Test the credit functionality"""
      self.bank.set_credit_limit(1000) 
      self.bank.credit(100)
      self.assertGreater(self.bank.bal, 0, "Credit should increase balance")

    def test_credit_over_limit(self):
      """Test credit fails if over credit limit"""
      self.bank.set_credit_limit(100)
      self.bank.credit(200)
      self.assertEqual(self.bank.bal, 0, "Balance should not change when crediting above limit")


    def test_debit_sufficient_funds(self):
      """Test debit with sufficient funds."""
      self.bank.bal = 100
      self.bank.set_debit_limit(100)
      self.bank.debit(50)
      self.assertEqual(self.bank.bal, 50, "Debit should reduce balance")

    def test_debit_insufficient_funds(self):
      """Test debit with insufficient funds."""
      self.bank.bal = 50
      self.bank.set_debit_limit(100)
      self.bank.debit(100)
      self.assertEqual(self.bank.bal, 50, "Debit with insufficient funds should not affect balance")

    def test_debit_over_limit(self):
        """Test debit fails if over debit limit"""
        self.bank.bal = 100
        self.bank.set_debit_limit(50)
        self.bank.debit(100)
        self.assertEqual(self.bank.bal, 100, "Debit with over debit limit should not affect balance")

    def test_set_loan_credit(self):
        self.bank.set_loan_credit()
        self.assertTrue(self.bank.credit_loan, "Credit loan should be enabled")

    def test_set_loan_debit(self):
        self.bank.set_loan_debit()
        self.assertTrue(self.bank.debit_loan, "Debit loan should be enabled")

    def test_set_credit_limit(self):
      self.bank.set_credit_limit(1000)
      self.assertEqual(self.bank.credit_limit, 1000, "Credit limit should be set correctly")

    def test_set_debit_limit(self):
        self.bank.set_debit_limit(100)
        self.assertEqual(self.bank.debit_limit, 100, "Debit limit should be set correctly")

    def test_credit_loan_amount(self):
      self.bank.set_loan_credit()
      self.bank.credit_loan_amount(100)
      self.assertGreater(self.bank.loan_bal, 0, "Credit loan amount should add to loan balance")

    def test_credit_loan_amount_disabled(self):
        self.bank.credit_loan_amount(100)
        self.assertEqual(self.bank.loan_bal, 0, "Credit loan amount should not be applied if disabled")

    def test_debit_loan_amount(self):
        self.bank.set_loan_debit()
        self.bank.loan_bal = 100
        self.bank.debit_loan_amount(50)
        self.assertEqual(self.bank.loan_bal, 50, "Debit loan amount should reduce loan balance")

    def test_debit_loan_amount_disabled(self):
        self.bank.debit_loan_amount(100)
        self.assertEqual(self.bank.loan_bal, 0, "Debit loan amount should not be applied if disabled")
    
    def test_show_balance(self):
      self.bank.bal = 100
      self.bank.show_balance()
      self.assertEqual(self.bank.bal, 100, "Balance should be shown correctly")

    def test_show_loan_detail(self):
      self.bank.loan_bal = 100
      self.bank.show_loan_detail()
      self.assertEqual(self.bank.loan_bal, 100, "Loan balance should be displayed correctly")
    
    def test_show_all_details(self):
      self.bank.bal = 100
      self.bank.loan_bal = 100
      self.bank.set_credit_limit(100) 
      self.bank.set_debit_limit(100) 
      self.bank.set_loan_credit()
      self.bank.set_loan_debit()
      self.bank.show_all_details()
      self.assertEqual(self.bank.bal, 100, "Balance should be shown correctly in all details")
      self.assertEqual(self.bank.loan_bal, 100, "Loan balance should be shown correctly in all details")
      self.assertEqual(self.bank.credit_limit, 100, "Credit limit should be shown correctly in all details")
      self.assertEqual(self.bank.debit_limit, 100, "Debit limit should be shown correctly in all details")
      self.assertTrue(self.bank.credit_loan, "Credit loan status should be correct in all details")
      self.assertTrue(self.bank.debit_loan, "Debit loan status should be correct in all details")

    def test_show_credit_limit(self):
        self.bank.set_credit_limit(100)
        self.bank.show_credit_limit()
        self.assertEqual(self.bank.credit_limit, 100, "Credit limit should be shown correctly")
    
    def test_show_debit_limit(self):
      self.bank.set_debit_limit(100)
      self.bank.show_debit_limit()
      self.assertEqual(self.bank.debit_limit, 100, "Debit limit should be displayed correctly")

if __name__ == '__main__':
    unittest.main()
