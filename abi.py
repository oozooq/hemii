# ABI контракту Gnosis Safe Proxy Factory
gnosis_abi = [
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "internalType": "contract GnosisSafeProxy", "name": "proxy", "type": "address"},
            {"indexed": False, "internalType": "address", "name": "singleton", "type": "address"}
        ],
        "name": "ProxyCreation",
        "type": "event"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_singleton", "type": "address"},
            {"internalType": "bytes", "name": "initializer", "type": "bytes"},
            {"internalType": "uint256", "name": "saltNonce", "type": "uint256"}
        ],
        "name": "calculateCreateProxyWithNonceAddress",
        "outputs": [
            {"internalType": "contract GnosisSafeProxy", "name": "proxy", "type": "address"}
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "singleton", "type": "address"},
            {"internalType": "bytes", "name": "data", "type": "bytes"}
        ],
        "name": "createProxy",
        "outputs": [
            {"internalType": "contract GnosisSafeProxy", "name": "proxy", "type": "address"}
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_singleton", "type": "address"},
            {"internalType": "bytes", "name": "initializer", "type": "bytes"},
            {"internalType": "uint256", "name": "saltNonce", "type": "uint256"},
            {"internalType": "contract IProxyCreationCallback", "name": "callback", "type": "address"}
        ],
        "name": "createProxyWithCallback",
        "outputs": [
            {"internalType": "contract GnosisSafeProxy", "name": "proxy", "type": "address"}
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_singleton", "type": "address"},
            {"internalType": "bytes", "name": "initializer", "type": "bytes"},
            {"internalType": "uint256", "name": "saltNonce", "type": "uint256"}
        ],
        "name": "createProxyWithNonce",
        "outputs": [
            {"internalType": "contract GnosisSafeProxy", "name": "proxy", "type": "address"}
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "proxyCreationCode",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "proxyRuntimeCode",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "pure",
        "type": "function"
    }
]

swap_abi = [
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "permit2",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "weth9",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "seaportV1_5",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "seaportV1_4",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "openseaConduit",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "nftxZap",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "x2y2",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "foundation",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "sudoswap",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "elementMarket",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "nft20Zap",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "cryptopunks",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "looksRareV2",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "routerRewardsDistributor",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "looksRareRewardsDistributor",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "looksRareToken",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "v2Factory",
                        "type": "address"
                    },
                    {
                        "internalType": "address",
                        "name": "v3Factory",
                        "type": "address"
                    },
                    {
                        "internalType": "bytes32",
                        "name": "pairInitCodeHash",
                        "type": "bytes32"
                    },
                    {
                        "internalType": "bytes32",
                        "name": "poolInitCodeHash",
                        "type": "bytes32"
                    }
                ],
                "internalType": "struct RouterParameters",
                "name": "params",
                "type": "tuple"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "BalanceTooLow",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "BuyPunkFailed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ContractLocked",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ETHNotAccepted",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "commandIndex",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "message",
                "type": "bytes"
            }
        ],
        "name": "ExecutionFailed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "FromAddressIsNotOwner",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InsufficientETH",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InsufficientToken",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidBips",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "commandType",
                "type": "uint256"
            }
        ],
        "name": "InvalidCommandType",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidOwnerERC1155",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidOwnerERC721",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidPath",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidReserves",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidSpender",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "LengthMismatch",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "SliceOutOfBounds",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TransactionDeadlinePassed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "UnableToClaim",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "UnsafeCast",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "V2InvalidPath",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "V2TooLittleReceived",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "V2TooMuchRequested",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "V3InvalidAmountOut",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "V3InvalidCaller",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "V3InvalidSwap",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "V3TooLittleReceived",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "V3TooMuchRequested",
        "type": "error"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "RewardsSent",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "bytes",
                "name": "looksRareClaim",
                "type": "bytes"
            }
        ],
        "name": "collectRewards",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes",
                "name": "commands",
                "type": "bytes"
            },
            {
                "internalType": "bytes[]",
                "name": "inputs",
                "type": "bytes[]"
            }
        ],
        "name": "execute",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes",
                "name": "commands",
                "type": "bytes"
            },
            {
                "internalType": "bytes[]",
                "name": "inputs",
                "type": "bytes[]"
            },
            {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "execute",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "uint256[]",
                "name": "",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "",
                "type": "uint256[]"
            },
            {
                "internalType": "bytes",
                "name": "",
                "type": "bytes"
            }
        ],
        "name": "onERC1155BatchReceived",
        "outputs": [
            {
                "internalType": "bytes4",
                "name": "",
                "type": "bytes4"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "",
                "type": "bytes"
            }
        ],
        "name": "onERC1155Received",
        "outputs": [
            {
                "internalType": "bytes4",
                "name": "",
                "type": "bytes4"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "",
                "type": "bytes"
            }
        ],
        "name": "onERC721Received",
        "outputs": [
            {
                "internalType": "bytes4",
                "name": "",
                "type": "bytes4"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "interfaceId",
                "type": "bytes4"
            }
        ],
        "name": "supportsInterface",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "int256",
                "name": "amount0Delta",
                "type": "int256"
            },
            {
                "internalType": "int256",
                "name": "amount1Delta",
                "type": "int256"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "uniswapV3SwapCallback",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "stateMutability": "payable",
        "type": "receive"
    }
]

erc20_abi = """
[
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "guy",
                "type": "address"
            },
            {
                "name": "wad",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "src",
                "type": "address"
            },
            {
                "name": "dst",
                "type": "address"
            },
            {
                "name": "wad",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "wad",
                "type": "uint256"
            }
        ],
        "name": "withdraw",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "dst",
                "type": "address"
            },
            {
                "name": "wad",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "",
                "type": "address"
            },
            {
                "name": "",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "payable": True,
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "src",
                "type": "address"
            },
            {
                "indexed": True,
                "name": "guy",
                "type": "address"
            },
            {
                "indexed": False,
                "name": "wad",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "src",
                "type": "address"
            },
            {
                "indexed": True,
                "name": "dst",
                "type": "address"
            },
            {
                "indexed": False,
                "name": "wad",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "dst",
                "type": "address"
            },
            {
                "indexed": False,
                "name": "wad",
                "type": "uint256"
            }
        ],
        "name": "Deposit",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "src",
                "type": "address"
            },
            {
                "indexed": False,
                "name": "wad",
                "type": "uint256"
            }
        ],
        "name": "Withdrawal",
        "type": "event"
    }
]"""

capsule_contract_abi = [
    [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_logic",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "admin_",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "_data",
                "type": "bytes"
            }
        ],
        "stateMutability": "payable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "previousAdmin",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "newAdmin",
                "type": "address"
            }
        ],
        "name": "AdminChanged",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "beacon",
                "type": "address"
            }
        ],
        "name": "BeaconUpgraded",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "implementation",
                "type": "address"
            }
        ],
        "name": "Upgraded",
        "type": "event"
    },
    {
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "inputs": [],
        "name": "admin",
        "outputs": [
            {
                "internalType": "address",
                "name": "admin_",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newAdmin",
                "type": "address"
            }
        ],
        "name": "changeAdmin",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "implementation",
        "outputs": [
            {
                "internalType": "address",
                "name": "implementation_",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            }
        ],
        "name": "upgradeTo",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "upgradeToAndCall",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "stateMutability": "payable",
        "type": "receive"
    }
]
]