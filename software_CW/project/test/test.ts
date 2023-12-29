import { expect } from "chai";
import { ethers, upgrades } from "hardhat";

describe("Jordan1RetroChicago", function () {
  it("Test contract", async function () {
    const ContractFactory = await ethers.getContractFactory("Jordan1RetroChicago");

    const initialOwner = (await ethers.getSigners())[0].address;

    const instance = await upgrades.deployProxy(ContractFactory, [initialOwner]);
    await instance.waitForDeployment();

    expect(await instance.uri(0)).to.equal("https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/fe8ec8e6-4013-4e2a-8082-d062e7628ddc/air-jordan-1-chicago-dz5485-612-%E7%99%BC%E5%94%AE%E6%97%A5%E6%9C%9F.jpg");
  });
});
