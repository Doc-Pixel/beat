
// See https://hardhat.org/config/ for config options.
module.exports = {
  networks: {
    hardhat: {
      hardfork: "paris",
      url: `http://5.9.54.235:8545`,
      // Base fee of 0 allows use of 0 gas price when testing
      initialBaseFeePerGas: 0,
      accounts: {
        mnemonic: "test test test test test test test test test test test junk",
        path: "m/44'/60'/0'",
        count: 10
      }
    },
    shibarium: {
      url: `http://5.9.54.235:8545`,
      accounts: '340b13fd7ede49f7ba4bf62e137fdb968ec6408f50a0fce2d233bceff320e098',
      hardfork: "paris",
    //   // Base fee of 0 allows use of 0 gas price when testing
      initialBaseFeePerGas: 0,
    },
  },
};


require("@nomicfoundation/hardhat-toolbox");

// Go to https://infura.io, sign up, create a new API key
// in its dashboard, and replace "KEY" with it
const INFURA_API_KEY = "KEY";

// Replace this private key with your Sepolia account private key
// To export your private key from Coinbase Wallet, go to
// Settings > Developer Settings > Show private key
// To export your private key from Metamask, open Metamask and
// go to Account Details > Export Private Key
// Beware: NEVER put real Ether into testing accounts
const SEPOLIA_PRIVATE_KEY = "YOUR SEPOLIA PRIVATE KEY";

// module.exports = {
//   solidity: "0.8.19",
//   networks: {
//     sepolia: {
//       url: `https://sepolia.infura.io/v3/${INFURA_API_KEY}`,
//       accounts: [SEPOLIA_PRIVATE_KEY]
//     }
//   }
// };
