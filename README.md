# EthereumAnalyzerProject

My colleague and I are co-owning this project for a blockchain hackathon at EY.

Our hackathon idea is completed and fully checked into this project repo. It consists of a web collector that queries the Ethereum blockchain for transactions to use as training data. Then it takes that training data and loads it into a Neo4j graph database. Through the Neo4j graph database we run the training data through a series of algorithms so that we can carry out an unsupervised learning experiment. The algorithms primarily measure on centrality and betweenness between addresses. The algorithmic output from the Neo4j graph database is then output into a JSON format, which we then serve up to the front-end UI using a force directed graph visualization through the use of D3.

The front end is not pretty, as many of the nodes seem to go off the screen. Nonetheless, clusterings are clear, and we can continue add new data to teach our graph database, so that it can continuously update its graph metrics for better identifying meaningful clusters.
