# NSE Data Scraper

A Python-based tool for scraping financial data from the National Stock Exchange (NSE) of India. Currently supports fetching underlying securities data with planned support for contracts information.

## Features

- Fetches underlying securities data from NSE
- Exports data to CSV and JSON formats
- Automated data updates
- Coming soon: Contract information scraping

## Prerequisites

- Python 3.8 or higher
- Poetry (Python package manager)
- Node.js (for some helper scripts)

## Installation

1. Clone the repository: 
```bash
git clone https://github.com/yourusername/nse-data-scraper.git
cd nse-data-scraper
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Install Node.js dependencies (if using helper scripts):
```bash
npm install
```

## Usage

1. Activate the Poetry virtual environment:
```bash
poetry shell
```

2. Run the data fetching script:
```bash
python fetchData.py
```

The script will:
- Fetch the latest underlying securities data from NSE
- Save the data to `underlyings.csv`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- [x] Underlying securities data scraping
- [ ] Contracts information fetching
- [ ] Historical data support
- [ ] Real-time data updates
- [ ] API endpoint creation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- National Stock Exchange of India for providing the data
- Contributors and maintainers of the project

## Disclaimer

This project is for educational purposes only. Please ensure you comply with NSE's terms of service and data usage policies when using this tool.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.