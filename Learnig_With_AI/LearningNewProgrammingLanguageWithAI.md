# Exercise: Learning a New Programming Language with AI

## Part 1: Create Your Learning Journey Plan

**Define goals**

- Build a smart contract in Solidity. 

- Successfuly deploy the smart contract to a testnet. 

**Lerrning plan**

**Learning Journey: Learning Solidity Coming From Python**

End Goal: Build a smart contract in Solidity and successfully deploy it to an Ethereum testnet.

**Phase 1: Solidity And Blockchain Fundamentals**

- Prerequisite: Comfortable with Python functions, variables, classes, dictionaries, and basic command-line usage.

- Learning Steps:
    1. Understand what smart contracts are and how they differ from normal Python programs.

    2. Learn Solidity file structure: SPDX-License-Identifier, pragma, contract, state variables, and functions.

    3. Compare Python dynamic typing with Solidity static typing: uint256, address, bool, string, mapping.

    4. Learn basic function visibility: public, private, external, internal.

    5. Learn blockchain basics: accounts, transactions, gas, blocks, and contract addresses.

- Verification:
    1. Write a SimpleStorage contract with set() and get() functions.

    2. Explain what data is stored on-chain versus temporary function data.

    3. Deploy and interact with the contract locally in Remix.

**Phase 2: Writing Useful Smart Contracts**

- Prerequisite: Understand basic Solidity syntax and how to compile a simple contract.

- Learning Steps:
    1. Learn state management using variables, structs, arrays, and mappings.

    2. Learn msg.sender, msg.value, constructors, and payable functions.

    3. Use require, revert, and custom errors for validation.

    4. Emit and read events for off-chain tracking.

    5. Build access control patterns such as “only owner can call this function.”

- Verification:
    1. Build a small ServiceRequest or TaskRegistry contract.

    2. Allow users to create, update, and complete requests.

    3. Emit events like RequestCreated and RequestCompleted.

    4. Confirm invalid actions fail with clear errors.

**Phase 3: Testing, Security, And Tooling**

- Prerequisite: Able to write a multi-function Solidity contract and understand transaction flow.

- Learning Steps:
    1. Set up a Solidity development environment using Hardhat or Foundry.

    2. Write automated tests for contract behavior.

    3. Learn common smart contract risks: reentrancy, bad access control, integer assumptions, unsafe external calls.

    4. Learn gas-aware design: storage is expensive, events are cheaper for history, loops can become dangerous.

    5. Learn how to read compiler warnings and run basic static analysis tools.

- Verification:
    1. Write tests for successful and failing contract interactions.
    
    2. Test that only authorized users can perform restricted actions.

    3. Test emitted events.

    4. Run your test suite from the command line.

    5. Refactor one function to reduce unnecessary storage writes.

**Phase 4: Testnet Deployment And Interaction**

- Prerequisite: Contract tested locally and comfortable using wallets, private keys, and environment variables.

- Learning Steps:
    1. Learn the difference between local networks, public testnets, and mainnet.

    2. Set up a wallet and get test ETH from a faucet, commonly for Sepolia.

    3. Configure a deployment tool such as Hardhat or Foundry with an RPC provider.

    4. Deploy your contract to a testnet.

    5. Verify the contract on a block explorer and interact with it after deployment.

- Verification:
    1. Successfully deploy your contract to a public testnet.

    2. Save the deployed contract address.

    3. Call at least one read function and one write function.

    4. View your transaction on a block explorer.
    
    5. Explain what gas was paid for and why the contract now has a permanent address.
