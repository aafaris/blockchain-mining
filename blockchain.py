# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import datetime
import hashlib

class Block:
	# block structure
	block_number = 0
	data = None
	next = None
	hash = None
	nonce = 0
	prev_hash = 0x0
	timestamp = datetime.datetime.now()

	def __init__(self, data):
		self.data = data

	def hash(self):
		h = hashlib.sha256()
		h.update(
			str(self.nonce).encode('utf-8') +
			str(self.data).encode('utf-8') +
			str(self.prev_hash).encode('utf-8') +
			str(self.timestamp).encode('utf-8') +
			str(self.block_number).encode('utf-8')
			)
		return h.hexdigest()

	def __str__(self) -> str:
		return "Block Hash: " + str(self.hash()) + \
			   "\nBlock Number: " + str(self.block_number) + \
			   "\nBlock Data: " + str(self.data) + \
			   "\nHashes: " + str(self.nonce) + \
			   "\n--------------"

class Blockchain:

	difficulty = 20
	max_nonce = 2**32
	target = 2**(256-difficulty)

	block = Block("Genesis")
	dummy = head = block

	def add(self, block):

		block.prev_hash = self.block.hash()
		block.block_number = self.block.block_number + 1

		self.block.next = block
		self.block = self.block.next

	def mine(self, block):
		for i in range(self.max_nonce):
			if int(block.hash(), 16) <= self.target:
				self.add(block)
				print(block)
				break
			else:
				block.nonce += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	# instantiate blockchain class
	blockchain = Blockchain()

	# generate 10 random blocks
	for i in range(5):
		blockchain.mine(Block("Block " + str(i + 1)))

	while blockchain.head != None:
		print(blockchain.head)
		blockchain.head = blockchain.head.next