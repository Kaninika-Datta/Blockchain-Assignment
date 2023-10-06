from flask import Flask, render_template, request, redirect, url_for
from web3 import Web3
import json

app = Flask(__name__)

# Connect to a local Ganache blockchain
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))  # Update with your Ganache URL

# Load the compiled smart contract ABI
with open("FoodSafetySystem.json", "r") as abi_file:
    abi = json.load(abi_file)["abi"]

# Contract address (deployed on Ganache)
contract_address = "0xYourContractAddress"  # Replace with your contract address
contract = w3.eth.contract(address=contract_address, abi=abi)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        origin = request.form["origin"]
        # Add a new food item to the blockchain
        tx_hash = contract.functions.addFoodItem(name, origin).transact()
        w3.eth.waitForTransactionReceipt(tx_hash)

    # Retrieve food items from the blockchain
    food_items = []
    for i in range(contract.functions.foodItemCount().call()):
        item = contract.functions.foodItems(i).call()
        food_items.append({"id": i, "name": item[0], "origin": item[1]})

    return render_template("index.html", food_items=food_items)

if __name__ == "__main__":
    app.run(debug=True)
