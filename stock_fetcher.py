import yfinance as yf
import pandas as pd
import argparse
from datetime import datetime
import sys

def fetch_stock_data(ticker, start_date, end_date, output_file=None):
    """
    Henter aktiekurser for et givet ticker symbol i en specifik periode
    og gemmer dataene i en CSV fil.
    
    Args:
        ticker (str): Aktie ticker symbol (f.eks. 'AAPL', 'NOVO-B.CO')
        start_date (str): Start dato i format 'YYYY-MM-DD'
        end_date (str): Slut dato i format 'YYYY-MM-DD'
        output_file (str): Navn på output CSV fil (valgfri)
    """
    try:
        # Hent aktiedata
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        
        if data.empty:
            print(f"Ingen data fundet for {ticker} i perioden {start_date} til {end_date}")
            return False
        
        # Tilføj ticker kolonne
        data['Ticker'] = ticker
        
        
        # Reorganiser kolonner
        data = data[['Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']]
        
        # Generer output filnavn hvis ikke angivet
        if output_file is None:
            output_file = f"{ticker}_{start_date}_til_{end_date}.csv"
        
        # Gem til CSV
        data.to_csv(output_file, index=True, sep=';')
        
        print(f"Data for {ticker} gemt i {output_file}")
        print(f"Antal dage: {len(data)}")
        print(f"Periode: {data.index[0].strftime('%Y-%m-%d')} til {data.index[-1].strftime('%Y-%m-%d')}")
        
        return True
        
    except Exception as e:
        print(f"Fejl ved hentning af data for {ticker}: {str(e)}")
        return False

def fetch_multiple_stocks(tickers, start_date, end_date, output_file=None):
    """
    Henter data for flere aktier og gemmer i en samlet CSV fil.
    
    Args:
        tickers (list): Liste af ticker symboler
        start_date (str): Start dato i format 'YYYY-MM-DD'
        end_date (str): Slut dato i format 'YYYY-MM-DD'
        output_file (str): Navn på output CSV fil (valgfri)
    """
    all_data = []
    
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(start=start_date, end=end_date)
            
            if not data.empty:
                data['Ticker'] = ticker
                data = data[['Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']]
                all_data.append(data)
                print(f"✓ Hentet data for {ticker}")
            else:
                print(f"✗ Ingen data fundet for {ticker}")
                
        except Exception as e:
            print(f"✗ Fejl ved hentning af {ticker}: {str(e)}")
    
    if all_data:
        # Kombiner alle data
        combined_data = pd.concat(all_data)
        
        # Generer output filnavn hvis ikke angivet
        if output_file is None:
            output_file = f"aktier_{start_date}_til_{end_date}.csv"
        
        # Gem til CSV
        combined_data.to_csv(output_file, index=True, sep=';')
        
        print(f"\nAlle data gemt i {output_file}")
        print(f"Antal aktier: {len(tickers)}")
        print(f"Total antal datapunkter: {len(combined_data)}")
        
        return True
    else:
        print("Ingen data kunne hentes")
        return False

def main():
    parser = argparse.ArgumentParser(description='Hent aktiekurser og gem i CSV fil')
    parser.add_argument('--ticker', '-t', type=str, help='Aktie ticker symbol (f.eks. AAPL)')
    parser.add_argument('--tickers', '-ts', type=str, nargs='+', help='Flere ticker symboler')
    parser.add_argument('--start', '-s', type=str, required=True, help='Start dato (YYYY-MM-DD)')
    parser.add_argument('--end', '-e', type=str, required=True, help='Slut dato (YYYY-MM-DD)')
    parser.add_argument('--output', '-o', type=str, help='Output CSV fil navn')
    
    args = parser.parse_args()
    
    # Valider datoer
    try:
        datetime.strptime(args.start, '%Y-%m-%d')
        datetime.strptime(args.end, '%Y-%m-%d')
    except ValueError:
        print("Fejl: Datoer skal være i format YYYY-MM-DD")
        sys.exit(1)
    
    # Hent data
    if args.ticker:
        success = fetch_stock_data(args.ticker, args.start, args.end, args.output)
    elif args.tickers:
        success = fetch_multiple_stocks(args.tickers, args.start, args.end, args.output)
    else:
        print("Fejl: Du skal angive enten --ticker eller --tickers")
        sys.exit(1)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    # Eksempel på brug hvis scriptet køres direkte uden argumenter
    if len(sys.argv) == 1:
        print("Eksempel på brug:")
        print("python stock_fetcher.py --ticker AAPL --start 2023-01-01 --end 2023-12-31")
        print("python stock_fetcher.py --tickers AAPL MSFT GOOGL --start 2023-01-01 --end 2023-12-31")
        print("python stock_fetcher.py --ticker NOVO-B.CO --start 2023-06-01 --end 2023-12-31 --output novo_data.csv")
    else:
        main()