// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FoodSafetySystem {
    struct FoodItem {
        string name;
        string origin;
    }

    mapping(uint256 => FoodItem) public foodItems;
    uint256 public foodItemCount;

    event FoodItemAdded(uint256 itemId, string name, string origin);

    function addFoodItem(string memory _name, string memory _origin) public {
        uint256 itemId = foodItemCount++;
        foodItems[itemId] = FoodItem({
            name: _name,
            origin: _origin
        });

        emit FoodItemAdded(itemId, _name, _origin);
    }
}
