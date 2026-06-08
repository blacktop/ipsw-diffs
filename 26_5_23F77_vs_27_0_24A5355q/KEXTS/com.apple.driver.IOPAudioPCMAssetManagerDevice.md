## com.apple.driver.IOPAudioPCMAssetManagerDevice

> `com.apple.driver.IOPAudioPCMAssetManagerDevice`

```diff

-340.3.0.0.0
-  __TEXT.__cstring: 0x449 sha256:2c6150e613f2b5c5dc5020ebfeec16b69fcfddf42597b029eb95ef31c9da8dbb
-  __TEXT.__os_log: 0x174 sha256:e9403ff916a4ad064306bca4d27f9f733f2e55938ebf356576d54049b0013c2c
-  __TEXT_EXEC.__text: 0xc08 sha256:dc95c144f1b3b8a0b42aff32d60aa63ff3160e170e22ab902310a131504ce415
+400.34.0.0.0
+  __TEXT.__cstring: 0x99b sha256:115146014f85ba2b59496b562ccbdbfe0374ebd5c9d2072daa48a05ffef4ac2a
+  __TEXT.__os_log: 0x47b sha256:8326cfe9be8edd39b830185924b1e0bf7233edd06aa10f538de06d43cb662dc4
+  __TEXT_EXEC.__text: 0x21fc sha256:b0befd9979e419c98ea6e6f0f4f0bca88764905fc1753bf4404ea5ac996a3603
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:9847753f7df3d778bece112ab9840c3dcf8dcd7fb7522649dddc629b2e28a2ed
-  __DATA.__common: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
-  __DATA_CONST.__auth_got: 0xa0 sha256:e66f5b2ac071c24f1d657a60c3e1a9ef3f44c2f37489a4ea48cf9fd6a72c51f5
-  __DATA_CONST.__got: 0x18 sha256:27f37e9d12a73cbd1c66040d45ae519a7486a8bb0d1f9c157348b337943f6989
-  __DATA_CONST.__mod_init_func: 0x8 sha256:9c46924c318504b5dec371539079daba32f4875f419fead08fd9e4c15f62f377
-  __DATA_CONST.__mod_term_func: 0x8 sha256:2805c94318a7a64c6345f020e98cc51bf01697120bff1d2d3a5779759572a8c7
-  __DATA_CONST.__const: 0x648 sha256:c1afa3d71a1b6f705494b959481db23e4f4ddee175332b312f111e20b3930a9f
-  __DATA_CONST.__kalloc_type: 0x40 sha256:3579d3e341203af54662f1d59552d05a5186ce7ed0cd4fad0105f2210c0c75d3
-  UUID: 9961859C-1C21-3C65-9841-0CF612033E14
-  Functions: 42
+  __DATA.__data: 0xc8 sha256:3aeaadcfb54772a35ece4882c11ad84357e7a6d874668317cc92a2561e46bd0b
+  __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
+  __DATA_CONST.__mod_init_func: 0x10 sha256:62d2f8e44053407b3e1ed486ef2df4cf3515d79ed45c614afc0a9c73e8ba89b3
+  __DATA_CONST.__mod_term_func: 0x10 sha256:16598776a974639d3ebc2ad157fd51361bf91550e7e863b9853d57b1f5d1c7af
+  __DATA_CONST.__const: 0xd48 sha256:ce628b1c1565e8b12a1a8564b2e237ce42fd846d0bf15a8a9a42a09f5e6894d3
+  __DATA_CONST.__kalloc_type: 0x80 sha256:a060a4dd2d95615a84686977ce1a7c17374bf2341de3c496534372bd0bfa9be6
+  __DATA_CONST.__auth_got: 0xe0 sha256:53918a39f9f6930c43ee55e4e1b9c4f2fc63602308dcbeed6800d145499806a6
+  __DATA_CONST.__got: 0x38 sha256:2208567874231c02fcd57245b0e2eabad7177cec86ace7eb256db20370c4e117
+  UUID: 8AA333DE-AC0B-3E78-B493-7276F950A560
+  Functions: 101
   Symbols:   0
-  CStrings:  19
+  CStrings:  49
 
CStrings:
+ "!((aopInternalDataPacket) == nullptr)"
+ "!((inArguments) == nullptr)"
+ "!((inArguments->scalarOutput) == nullptr)"
+ "!((inData) == nullptr)"
+ "!((ioMemory) == nullptr)"
+ "!((mAssetResourceData) == nullptr)"
+ "!((mDevice) == nullptr)"
+ "!((mMemoryResourceData) == nullptr)"
+ "!((resourceData) == nullptr)"
+ "!((userClient) == nullptr)"
+ "!((userClient->mDevice) == nullptr)"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/IOPAudioDrivers/src/kext/PCMAssetManagerDevice/UserClient/PCMAssetManagerDeviceUserClient.cpp"
+ "1211111212221212111111111111111"
+ "IOPAudio::PCMAssetManagerDevice::UserClient"
+ "IOPAudioPCMAssetManagerDeviceUserClient"
+ "IOUserClient::initWithTask(inOwningTask, inSecurityToken, inType, inProperties)"
+ "IOUserClientDefaultLocking"
+ "IOUserClientDefaultLockingSetProperties"
+ "IOUserClientDefaultLockingSingleThreadExternalMethod"
+ "IOUserClientEntitlements"
+ "assetBufferSize <= kMaximumSizeOfPCMResourceData"
+ "assetBufferSize > 0"
+ "com.apple.private.aea.haptics.user-access"
+ "entitlement == kOSBooleanTrue"
+ "mDevice->open(this)"
+ "ret = inNodeInterface->setNodeProperty({ .propertyID = kAssetPropertyID, .data = inData, .dataSize = inDataSize, }) == 0 "
+ "ret = mAssetResourceData->prepare(kIODirectionInOut) == 0 "
+ "ret = userClient->mDevice->getNumberOfSupportedAssets(numAssets) == 0 "
+ "site.IOPAudioPCMAssetManagerDeviceUserClient"
+ "super::start(inProvider)"

```
