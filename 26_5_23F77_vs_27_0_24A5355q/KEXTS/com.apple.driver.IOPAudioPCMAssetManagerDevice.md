## com.apple.driver.IOPAudioPCMAssetManagerDevice

> `com.apple.driver.IOPAudioPCMAssetManagerDevice`

```diff

-340.3.0.0.0
-  __TEXT.__cstring: 0x449
-  __TEXT.__os_log: 0x174
-  __TEXT_EXEC.__text: 0xc08
+400.34.0.0.0
+  __TEXT.__cstring: 0x99b
+  __TEXT.__os_log: 0x47b
+  __TEXT_EXEC.__text: 0x21fc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
-  __DATA.__common: 0x38
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x18
-  __DATA_CONST.__mod_init_func: 0x8
-  __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0x648
-  __DATA_CONST.__kalloc_type: 0x40
-  UUID: 9961859C-1C21-3C65-9841-0CF612033E14
-  Functions: 42
+  __DATA.__common: 0x60
+  __DATA_CONST.__mod_init_func: 0x10
+  __DATA_CONST.__mod_term_func: 0x10
+  __DATA_CONST.__const: 0xd48
+  __DATA_CONST.__kalloc_type: 0x80
+  __DATA_CONST.__auth_got: 0xe0
+  __DATA_CONST.__got: 0x38
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
