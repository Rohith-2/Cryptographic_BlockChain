# Cryptographic_BlockChain
Simulating Blockchain with mining and peer verification

## Authors :  
Rohith Ramakrishnan  
[Isha Indhu S](https://github.com/ishaindhu)  
[Jayashree O](https://github.com/jayashree138)  
[Rama Sailaja](https://github.com/rsp-009)

## Blocks
We will define a class MinimalBlock that contains the following data members: 

* index - to store the No. of the block.     
* timestamp - time at which the block was created. 
* data - the content of the block. 
* previous_hash - hash of the previous block. 
* hash - hash of the current block. 
  
This class also possesses a function called hashing, which will perform the SHA-256 hashing process discussed in the previous section. Under this function the hash of all data members are individually performed and the concatenated result is returned as the final hash using the function "hexdigest". The disp function is a visual indicator for the integrity of the block. 

## Blockchain
This Class MinimalChain is developed to define a unique Block chain. The constructor creates a list with just the genesis block or the first entry in the blockchain. The function get\_genesis\_block returns an arbitrary block with default values that are predefined. Another function, disp\_chain, is also written to display the contents of the block in Json format and notice that for any valid entry the contents will be displayed in green while the tampered entries are displayed in red color to indicate the invalidity of that particular block. The add\_block function is utilised to enter a new valid block into the chain. A function to return the length of the chain has also been included to help us for future validation purposes. Function verify helps perform the mining step while adding a new block to the chain by validating the contents of the block.

## BlockNetwork 
This Class will contain a list that will hold the individual copies of the Blockchain that belong to the individuals or peers present in the network. The function add\_peers helps initialise a new peer into the network by appending new chains into the list. A function verify was implemented to validate the entire network and to prevent and detect tampering in any individual's copy of the blockchain. Inside the above mentioned, we iterate through all copies of the chains and initially check if the lengths of the chains are equal, if not, we can certainly conclude that the chains have been tampered with. Following that, we append the hashes into a list and check if the length of the set of hashes is not more than 1. This is done to check if all hashes are equal. In case the length is greater than 1, it indicates that one or more blocks in the network has been tampered with.

## Results
Valid Blockchain:  
![picture alt](https://github.com/Rohith-2/Cryptographic_BlockChain/blob/main/images/Blockchain_Valid.png). 

Invalid Blockchain after tampering with data:  
![picture alt](https://github.com/Rohith-2/Cryptographic_BlockChain/blob/main/images/Blockchain_inValid.png)
