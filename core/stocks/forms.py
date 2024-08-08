from django import forms

class TickerListForm(forms.Form):
    tickers = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter tickers separated by commas or new lines'}),
        label='Tickers',
        help_text='Enter stock tickers separated by commas or new lines.'
    )
    period = forms.ChoiceField(
        choices=(('1d', '1 Day'), ('5d', '5 Days'), ('1mo', '1 Month'), ('3mo', '3 Months'), ('6mo', '6 Months'),
                 ('1y', '1 Year'), ('2y', '2 Years'), ('5y', '5 Years'), ('10y', '10 Years'), ('ytd', 'YTD'),
                 ('max', 'Max')),
        label='Period',
        help_text='Select the period for the stock'
    )

    def clean_tickers(self):
        data = self.cleaned_data['tickers']
        # Split the tickers by commas or new lines
        tickers = [ticker.strip().upper() for ticker in data.replace(',', '\n').split('\n') if ticker.strip()]
        return tickers
