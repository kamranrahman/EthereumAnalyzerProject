# EthereumAnalyzerProject

The purpose of this project is to create an open-source framework for analyzing data from the Ethereum blockchain. The code will be imperfect, so if anyone has improvements, please share. As a non-developer, I am teaching myself Python in the process, and my colleague is taking the data results and running it through a Neo4j graph algorithm.

Right now, the only thing I have working is a data collector that collects transaction data from the Ethereum blockchain, and writes (and appends) to an existing csv file. 

If you have all the modules installed already, you should be able to just run the .py file without any issues. I've got it set to ping the API every 2 minutes. If you hit the API more frequently than that, you'll likely be throttled (unless you pay for more API call capacity).

