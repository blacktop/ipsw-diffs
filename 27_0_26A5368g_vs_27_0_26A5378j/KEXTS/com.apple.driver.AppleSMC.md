## com.apple.driver.AppleSMC

> `com.apple.driver.AppleSMC`

```diff

-  __TEXT.__cstring: 0x8607
-  __TEXT.__const: 0x220
+  __TEXT.__cstring: 0x85e7
+  __TEXT.__const: 0x280
   __TEXT.__os_log: 0xd97
-  __TEXT_EXEC.__text: 0x28218
+  __TEXT_EXEC.__text: 0x281ec
   __TEXT_EXEC.__auth_stubs: 0x9e0
   __DATA.__data: 0xcc
   __DATA.__common: 0x490

   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x8
   Functions: 892
-  Symbols:   1831
-  CStrings:  1039
+  Symbols:   1830
+  CStrings:  1038
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
- __ZL16wakeEventClaimed
Functions:
~ __ZN20AppleSMCKeysEndpoint19_keyEndpointHandlerEPvS0_ : 2144 -> 2164
~ __ZN20AppleSMCKeysEndpoint22_powerStateActionGatedEmPv : 1292 -> 1288
~ __ZN8AppleSMC37sensorHubDirectWriteSensorExchangeKeyEjP17SMCSensorEx_Jumbo : 364 -> 376
~ __ZN8AppleSMC34_returnSizeOfSMCExchangeCacheEntryEj : 64 -> 68
~ __ZN8AppleSMC33_storeSizeOfSMCExchangeCacheEntryEjh : 68 -> 76
~ __ZN8AppleSMC13setPowerStateEmP9IOService : 552 -> 468
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.B4kUse/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCACAMDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.B4kUse/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCBinaryLogDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.B4kUse/Sources/AppleSMC/AppleSMCEmbedded.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.B4kUse/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCCharger.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.B4kUse/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCChargerUtil.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.B4kUse/Sources/AppleSMC/AppleSMCEmbeddedFunctions.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.B4kUse/Sources/AppleSMC/AppleSMCEmbeddedPMU/AppleSMCPMU.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.B4kUse/Sources/AppleSMC/AppleSMCKeysEndpoint.cpp"
+ "121111121222121211121211111111112111212222111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222"
+ "12111112122212121112121111111111211121222211111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222222222211122211112"
+ "21:11:07"
+ "21:11:09"
+ "AppleSMCEmbedded::%s(): ENTER powerStateOrdinal=%x, prevState=%x\n"
+ "Jun 29 2026"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fGi51K/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCACAMDriver.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fGi51K/Sources/AppleSMC/AppleSMCBinaryLog/AppleSMCBinaryLogDriver.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fGi51K/Sources/AppleSMC/AppleSMCEmbedded.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fGi51K/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCCharger.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fGi51K/Sources/AppleSMC/AppleSMCEmbeddedCharger/AppleSMCChargerUtil.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fGi51K/Sources/AppleSMC/AppleSMCEmbeddedFunctions.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fGi51K/Sources/AppleSMC/AppleSMCEmbeddedPMU/AppleSMCPMU.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fGi51K/Sources/AppleSMC/AppleSMCKeysEndpoint.cpp"
- "12111112122212121112121111111111211112222111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222222222"
- "1211111212221212111212111111111121111222211111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222222222211122211112"
- "22:28:14"
- "22:28:16"
- "AppleSMCEmbedded::%s(): ENTER powerStateOrdinal=%x, newState=%x\n"
- "AppleSMCEmbedded::%s(): kPowerOff\n"
- "Jun 15 2026"

```
