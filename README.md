# Bitcoin Price Tracker ![license](https://img.shields.io/static/v1?label=license&message=MIT&color=red) ![license](https://img.shields.io/static/v1?label=Python&message=3.6.9&color=yellow&labelColor=blue)
![Sytle Guide Check](https://github.com/csantana1121/BitcoinData/actions/workflows/github-actions.yaml/badge.svg) ![example branch parameter](https://github.com/csantana1121/BitcoinData/actions/workflows/github-bitcoin-tests.yaml/badge.svg?branch=master)

## Project Description
This project makes use of Coindesk API (https://www.coindesk.com/coindesk-api)
to track price information on bitcoin to do the follow:
* Track the current price of Bitcoin in USD, EUR, and GBP
* Tell the user the current price of Bitcoin in a neat human readable format:
![Output](https://github.com/csantana1121/BitcoinData/blob/master/data/images/image.png?raw=true)
* Store the current price of into a database for data analysis and tracking purposes
* Export and save the database onto a cloud to allow it to be shared between devices
* Allow the user to access historical data on the price of Bitcoin
    
## To Do List

- [ ] Generate graphs tracking all known price indexes of Bitcoin
> Working beta version of graphing system:
![Output](https://github.com/csantana1121/BitcoinData/blob/master/data/images/Historicalgraphbeta.png?raw=true)
- [ ] Grab historical Bitcoin Data on user request
> Currently stores the previous 30 days worth of Bitcoin price information
- [ ] Add a graphical user interface to allow for the user to interact and ask for Bitcoin information
- [ ] Write an automated script that pulls the current price index of Bitcoin at timed intervals.


## License
See LICENSE.md in the root directory.