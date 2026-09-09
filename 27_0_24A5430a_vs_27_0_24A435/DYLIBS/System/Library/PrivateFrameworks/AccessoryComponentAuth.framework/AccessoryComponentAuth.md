## AccessoryComponentAuth

> `/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth`

```diff

 1216.2.2.0.0
-  __TEXT.__text: 0x1241c
-  __TEXT.__objc_methlist: 0x4ec
-  __TEXT.__const: 0xd700
-  __TEXT.__cstring: 0x14d2
-  __TEXT.__oslogstring: 0x11d7
-  __TEXT.__gcc_except_tab: 0x274
-  __TEXT.__unwind_info: 0x430
+  __TEXT.__text: 0x129d4
+  __TEXT.__objc_methlist: 0x534
+  __TEXT.__const: 0xd710
+  __TEXT.__cstring: 0x15c9
+  __TEXT.__oslogstring: 0x1248
+  __TEXT.__gcc_except_tab: 0x270
+  __TEXT.__unwind_info: 0x440
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1650
+  __DATA_CONST.__const: 0x1710
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x470
+  __DATA_CONST.__objc_selrefs: 0x498
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0xe0
-  __AUTH_CONST.__const: 0xc48
-  __AUTH_CONST.__cfstring: 0x1440
-  __AUTH_CONST.__objc_const: 0x6d0
+  __AUTH_CONST.__const: 0xc68
+  __AUTH_CONST.__cfstring: 0x1540
+  __AUTH_CONST.__objc_const: 0x6f0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x450
   __AUTH.__objc_data: 0xf0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 479
-  Symbols:   1582
-  CStrings:  339
+  Functions: 488
+  Symbols:   1603
+  CStrings:  351
 
Symbols:
+ -[ACCHWComponentAuthService authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:]
+ -[ACCHWComponentAuthService signRCAMChallenge:completionHandler:componentIndex:]
+ GCC_except_table70
+ _ACCUserDefaultsKey_BLEPairingConfigRequestDelayMs
+ _ACCUserDefaultsKey_BLEPairingDisableOOBPPlusFlow
+ _ACCUserDefaultsKey_BLEPairingDontEarlyInfoAsDeviceUID
+ _ACCUserDefaultsKey_BLEPairingIgnoreZeroEarlyInfo
+ _ACCUserDefaultsKey_PlatformIDOverride
+ _ACCUserDefaultsKey_TestCreateBLEPairingOnInductive
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ ___107-[ACCHWComponentAuthService authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke
+ ___107-[ACCHWComponentAuthService authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke_2
+ _authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:.RCAMQueue
+ _authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:.onceToken
+ _kCFACCUserDefaultsKey_BLEPairingConfigRequestDelayMs
+ _kCFACCUserDefaultsKey_BLEPairingDisableOOBPPlusFlow
+ _kCFACCUserDefaultsKey_BLEPairingDontEarlyInfoAsDeviceUID
+ _kCFACCUserDefaultsKey_BLEPairingIgnoreZeroEarlyInfo
+ _kCFACCUserDefaultsKey_PlatformIDOverride
+ _kCFACCUserDefaultsKey_TestCreateBLEPairingOnInductive
+ _objc_msgSend$createVillanovaNonce:IDSN:challenge:
- GCC_except_table67
CStrings:
+ "(moduleType=%d) %s: cpGetDeviceIDSN failed: ret=%x len=%zu"
+ "BLEPairingConfigRequestDelayMs"
+ "BLEPairingDisableOOBPPlusFlow"
+ "BLEPairingDontEarlyInfoAsDeviceUID"
+ "BLEPairingIgnoreZeroEarlyInfo"
+ "ComponentBusyError"
+ "Flags indicate rcam...do not call cpCopyCertificate()"
+ "PlatformIDOverride"
+ "RCAM"
+ "TestCreateBLEPairingOnInductive"
+ "com.apple.ACCHWComponentAuthService.rcam"
+ "prpc"
```
