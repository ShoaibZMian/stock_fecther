# Stock Data Fetcher

Et Python script til at hente aktiekurser fra Yahoo Finance og gemme dem i CSV format.

## Installation

1. **Klon/download filerne**
2. **Opret virtual environment:**
   ```bash
   python3 -m venv stock_env
   source stock_env/bin/activate
   ```
3. **Installer dependencies:**
   ```bash
   pip install yfinance pandas
   ```

## Brug

### Enkelt aktie

Hent data for en enkelt aktie:

```bash
python stock_fetcher.py --ticker AAPL --start 2023-01-01 --end 2023-12-31
```

**Parametre:**
- `--ticker` eller `-t`: Aktie ticker symbol (f.eks. AAPL, MSFT)
- `--start` eller `-s`: Start dato (YYYY-MM-DD format)
- `--end` eller `-e`: Slut dato (YYYY-MM-DD format)
- `--output` eller `-o`: Output filnavn (valgfrit)

### Flere aktier

Hent data for flere aktier samtidig:

```bash
python stock_fetcher.py --tickers AAPL MSFT GOOGL --start 2023-01-01 --end 2023-12-31
```

### Danske aktier

For danske aktier, brug ticker symboler med `.CO` suffix:

```bash
python stock_fetcher.py --ticker NOVO-B.CO --start 2023-10-01 --end 2023-10-31 --output novo_data.csv
```

**Almindelige danske tickers:**
- Novo Nordisk: `NOVO-B.CO`
- Maersk: `MAERSK-B.CO`
- Carlsberg: `CARL-B.CO`
- DSV: `DSV.CO`

## Eksempler

### Apple aktie for hele 2023
```bash
python stock_fetcher.py --ticker AAPL --start 2023-01-01 --end 2023-12-31
```

### Flere amerikanske tech aktier
```bash
python stock_fetcher.py --tickers AAPL MSFT GOOGL AMZN --start 2023-06-01 --end 2023-12-31 --output tech_stocks.csv
```

### Novo Nordisk for oktober 2023
```bash
python stock_fetcher.py --ticker NOVO-B.CO --start 2023-10-01 --end 2023-10-31 --output novo_oktober.csv
```

## Output format

CSV filen indeholder følgende kolonner:
- `Date`: Handelsdato
- `Ticker`: Aktie symbol
- `Open`: Åbningskurs
- `High`: Højeste kurs
- `Low`: Laveste kurs
- `Close`: Lukkekurs
- `Volume`: Handelsvolumen

## Fejlhåndtering

Scriptet vil:
- Vise fejlmeddelelse hvis ticker ikke findes
- Kontrollere dato format (skal være YYYY-MM-DD)
- Rapportere hvis ingen data findes for den givne periode

## Tips

- Weekend og helligdage er ikke inkluderet (kun handelsdage)
- Brug Yahoo Finance ticker symboler
- For internationale aktier, check det korrekte suffix (.CO for Danmark, .L for London, osv.)
- Data er justeret for splits og dividender

## Systemkrav

- Python 3.6+
- Internet forbindelse (til at hente data fra Yahoo Finance)