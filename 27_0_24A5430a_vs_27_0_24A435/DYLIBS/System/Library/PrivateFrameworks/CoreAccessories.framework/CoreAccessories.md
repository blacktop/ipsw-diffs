## CoreAccessories

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories`

```diff

 1216.2.2.0.0
-  __TEXT.__text: 0x26334
-  __TEXT.__objc_methlist: 0x1954
+  __TEXT.__text: 0x26e4c
+  __TEXT.__objc_methlist: 0x19bc
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x3ccf
-  __TEXT.__oslogstring: 0x4087
+  __TEXT.__cstring: 0x3dbf
+  __TEXT.__oslogstring: 0x4146
   __TEXT.__gcc_except_tab: 0x820
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0xa38
+  __TEXT.__unwind_info: 0xa60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1fb8
+  __DATA_CONST.__const: 0x2038
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf30
+  __DATA_CONST.__objc_selrefs: 0xf58
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xd8
   __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0xb40
-  __AUTH_CONST.__cfstring: 0x3b00
-  __AUTH_CONST.__objc_const: 0x2348
+  __AUTH_CONST.__cfstring: 0x3c00
+  __AUTH_CONST.__objc_const: 0x2368
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xdc
-  __DATA.__data: 0x758
+  __DATA.__data: 0x760
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x138
   __DATA_DIRTY.__bss: 0x68

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 821
-  Symbols:   2248
-  CStrings:  866
+  Functions: 832
+  Symbols:   2276
+  CStrings:  879
 
Symbols:
+ -[ACCHWComponentAuth authenticateRCAMWithChallenge:completionHandler:updateRegistry:]
+ -[ACCHWComponentAuth authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:]
+ -[ACCHWComponentAuth signRCAMChallenge:completionHandler:]
+ -[ACCHWComponentAuth signRCAMChallenge:completionHandler:componentIndex:]
+ -[ACCTransportPlugin endpointForConnectionWithUUID:forProtocol:]
+ _ACCUserDefaultsKey_BLEPairingConfigRequestDelayMs
+ _ACCUserDefaultsKey_BLEPairingDisableOOBPPlusFlow
+ _ACCUserDefaultsKey_BLEPairingDontEarlyInfoAsDeviceUID
+ _ACCUserDefaultsKey_BLEPairingIgnoreZeroEarlyInfo
+ _ACCUserDefaultsKey_PlatformIDOverride
+ _ACCUserDefaultsKey_TestCreateBLEPairingOnInductive
+ ___100-[ACCHWComponentAuth authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke
+ ___100-[ACCHWComponentAuth authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke_2
+ ___73-[ACCHWComponentAuth signRCAMChallenge:completionHandler:componentIndex:]_block_invoke
+ ___73-[ACCHWComponentAuth signRCAMChallenge:completionHandler:componentIndex:]_block_invoke_2
+ _kACCProperties_Connection_OOBPairingEarlyInfoBDADDR
+ _kACCProperties_Connection_OOBPairingEarlyInfoSessionState
+ _kCFACCProperties_Connection_OOBPairingEarlyInfoBDADDR
+ _kCFACCProperties_Connection_OOBPairingEarlyInfoSessionState
+ _kCFACCUserDefaultsKey_BLEPairingConfigRequestDelayMs
+ _kCFACCUserDefaultsKey_BLEPairingDisableOOBPPlusFlow
+ _kCFACCUserDefaultsKey_BLEPairingDontEarlyInfoAsDeviceUID
+ _kCFACCUserDefaultsKey_BLEPairingIgnoreZeroEarlyInfo
+ _kCFACCUserDefaultsKey_PlatformIDOverride
+ _kCFACCUserDefaultsKey_TestCreateBLEPairingOnInductive
+ _objc_msgSend$authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:
+ _objc_msgSend$endpointForConnectionWithUUID:forProtocol:
+ _objc_msgSend$signRCAMChallenge:completionHandler:componentIndex:
CStrings:
+ "Authenticating RCAM... (completionHandler: %s)"
+ "BLEPairingConfigRequestDelayMs"
+ "BLEPairingDisableOOBPPlusFlow"
+ "BLEPairingDontEarlyInfoAsDeviceUID"
+ "BLEPairingIgnoreZeroEarlyInfo"
+ "OOBPairingEarlyInfoBDADDR"
+ "OOBPairingEarlyInfoSessionState"
+ "PlatformIDOverride"
+ "RCAM"
+ "RCAM authPassed = %d, fdrValidationStatus %d, authError %d"
+ "Signing RCAM challenge... (completionHandler: %s)"
+ "TestCreateBLEPairingOnInductive"
+ "signed RCAM challenge authError %d"
```
