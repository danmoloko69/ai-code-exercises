// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract InventoryChecker {

    struct Product {
        uint256 quantity;
        bool exists;
    }

    address public owner;
    mapping(string => Product) private inventory;

    event ProductUpdated(string indexed productName, uint256 quantity, address indexed updatedBy);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can update inventory");
        _;
    }

    function setItem(string calldata productName, uint256 quantity) external onlyOwner {
        inventory[productName] = Product(quantity, quantity > 0);
        emit ProductUpdated(productName, quantity, msg.sender);
    }

    function getQuantity(string calldata productName) external view returns (uint256) {
        return inventory[productName].quantity;
    }

    function itemExists(string calldata productName) external view returns (bool) {
        return inventory[productName].exists;
    }
}