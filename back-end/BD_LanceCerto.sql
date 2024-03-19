create database LanceCerto;
use LanceCerto;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    type ENUM('seller', 'buyer') NOT NULL
);


CREATE TABLE crops (
    crop_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    seller_id INT NOT NULL,
    start_date DATETIME,
    end_date DATETIME,
    FOREIGN KEY (seller_id) REFERENCES users(user_id)
);



CREATE TABLE auctions (
    auction_id INT PRIMARY KEY,
    crop_id INT NOT NULL,
    start_price DECIMAL(10, 2) NOT NULL,
    current_price DECIMAL(10, 2),
    status ENUM('active', 'closed') NOT NULL DEFAULT 'active',
    FOREIGN KEY (crop_id) REFERENCES crops(crop_id)
);


CREATE TABLE bids (
    bid_id INT PRIMARY KEY,
    auction_id INT NOT NULL,
    buyer_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    timestamp DATETIME,
    FOREIGN KEY (auction_id) REFERENCES auctions(auction_id),
    FOREIGN KEY (buyer_id) REFERENCES users(user_id)
);


CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    auction_id INT NOT NULL,
    buyer_id INT NOT NULL,
    bid_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    final_pay DECIMAL(10, 2) NOT NULL,
    timestamp DATETIME,
    FOREIGN KEY (auction_id) REFERENCES auctions(auction_id),
    FOREIGN KEY (buyer_id) REFERENCES users(user_id),
    FOREIGN KEY (bid_id) REFERENCES bids(bid_id)
);