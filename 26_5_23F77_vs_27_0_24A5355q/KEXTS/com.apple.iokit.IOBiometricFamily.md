## com.apple.iokit.IOBiometricFamily

> `com.apple.iokit.IOBiometricFamily`

```diff

-545.100.10.0.0
+570.0.0.0.0
   __TEXT.__os_log: 0x125b
-  __TEXT.__cstring: 0x1c99
-  __TEXT.__const: 0x18
-  __TEXT_EXEC.__text: 0xf450
+  __TEXT.__cstring: 0x1297
+  __TEXT.__const: 0x20
+  __TEXT_EXEC.__text: 0xf540
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcc
   __DATA.__common: 0x3c0
-  __DATA_CONST.__auth_got: 0x208
-  __DATA_CONST.__got: 0x70
   __DATA_CONST.__mod_init_func: 0x48
   __DATA_CONST.__mod_term_func: 0x48
   __DATA_CONST.__const: 0x3200
   __DATA_CONST.__kalloc_type: 0x680
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: 759CCA0A-4B6C-3977-AF83-920A6119A74E
-  Functions: 498
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0x70
+  UUID: 391439A1-4D37-3716-95BA-33E0E485A5C3
+  Functions: 509
   Symbols:   0
-  CStrings:  308
+  CStrings:  278
 
CStrings:
+ "AssertMacros: %s (value = 0x%lx), version: BiometricKit-570~3842, %s file: %s, line: %d\n"
+ "IOBioMemorySharing.cpp"
+ "IOBioPool.cpp"
+ "IOBioQueue.cpp"
+ "IOBioSEPSharedBuffer.cpp"
+ "IOBiometricService.cpp"
+ "IOBiometricUserClient.cpp"
+ "IOBiometricUtilities.cpp"
+ "IOSEPBiometricService.cpp"
+ "MCDataMessagingKernel.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/BiometricBase/IOBiometricFamily/IOBioFoundation/IOBioMemorySharing.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/BiometricBase/IOBiometricFamily/IOBioFoundation/IOBioPool.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/BiometricBase/IOBiometricFamily/IOBioFoundation/IOBioQueue.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/BiometricBase/IOBiometricFamily/IOBioFoundation/IOBioSEPSharedBuffer.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/BiometricBase/IOBiometricFamily/IOBiometricService.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/BiometricBase/IOBiometricFamily/IOBiometricUserClient.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/BiometricBase/IOBiometricFamily/IOBiometricUtilities.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/BiometricBase/IOBiometricFamily/IOSEPBiometricService.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/BiometricBase/MCDataMessaging/MCDataMessagingKernel.cpp"
- "AssertMacros: %s, %s file: %s, line: %d, value: %lld\n"
- "ERROR: %s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n"
- "ERROR: IOBioArrayQueue::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n"
- "ERROR: IOBioSEPSharedBufferFactory::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n"
- "ERROR: IOBioSharedMemoryTransferQueue::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n"
- "ERROR: IOBiometricService::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n"
- "ERROR: IOBiometricUserClient::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n"
- "ERROR: IOBiometricUtilities::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n"
- "ERROR: IOSEPBiometricService::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n"
- "ERROR: IOSEPSharedBuffer::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n"
- "ERROR: MCDataMessaging::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n"
- "cacheProtectedConfiguration"
- "cacheSysProtectedConfiguration"
- "checkBioMatchTimer"
- "checkBioTokenTimer"
- "checkBiometricCommand"
- "checkPasscodeInputTimer"
- "dropUnlockTokenCommandHandler"
- "getShareableMemory"
- "initWithServiceAndUserID"
- "iterateObjects"
- "lock"
- "removeMatchingObject"
- "setUserAccountsInfo"
- "setupCachedContextForUser"
- "unlock"
- "unlockItem"
- "userTimerEventSource"
- "withAllocNameAndBufferSizeAndSEP"
- "withNameAndCapacity"
- "withPoolAndAllocNameAndBufferSizeAndSEP"

```
