class sham_wallet:
    """
        A class used to emulate a crypto currency wallet to practice trading.
    """

    def __init__(self, coin, init_amount, max_buy):
        """
        Parameters
        ----------
        balance : float
            the initial wallet balance

        max_buy : float
            the maximum amount of money to spend

        crypto_price : float
            the price of one unit of a specified crypto currency

        crypto_balance : float
            the balance for specified crypto currency

        selling_fee : float
            potential fee for buying crypto

        buying_fee : float
            potential fee for selling crytpo
        """
        self.coin = coin
        self.balance = round(init_amount, 2)
        self.max_buy = max_buy
        self.crypto_price = 0
        self.crypto_amount = 0
        self.selling_fee = 0
        self.buying_fee = 0
    
    def market_buy(self, current_crypto_price):
        """
        For placing a market buy
        """
        buy_at = self.max_buy
        if self.wallet_amount <= buy_at:
            buy_at = self.wallet_amount
        self.crypto_amount += (buy_at - self.buying_fee) / current_crypto_price
        self.wallet_amount -= buy_at

    def market_sell(self, current_crypto_price):
        """
        For placing a market sell
        """
        worth = self.crypto_amount * current_crypto_price
        self.wallet_amount += (worth - self.selling_fee)
        self.crypto_amount = 0