// SPDX-License-Identifier: MIT
pragma solidity 0.8.7;

import "@openzeppelin/contracts/access/Ownable.sol";

interface ILatchWeb3 {   
    function getStatus(address accountClient) external view returns (bool);
}

abstract contract Latcheable is Ownable {
    address private PROXY_LATCH;
    
    function setProxyLatch(address proxyLatch) external onlyOwner {
        PROXY_LATCH = proxyLatch;
    }

    modifier isLatcheable() {
        require(!ILatchWeb3(PROXY_LATCH).getStatus(msg.sender), "LatchClosed");
        _;
    }

    function getLatchStatus() external view returns (bool) {
        return ILatchWeb3(PROXY_LATCH).getStatus(msg.sender);
    }

}
