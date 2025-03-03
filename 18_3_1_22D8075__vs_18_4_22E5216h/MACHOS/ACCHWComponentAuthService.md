## ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService`

```diff

-1025.82.1.0.0
-  __TEXT.__text: 0x10434
-  __TEXT.__auth_stubs: 0x790
+1043.100.29.0.0
+  __TEXT.__text: 0x1031c
+  __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_stubs: 0x960
-  __TEXT.__objc_methlist: 0x224
-  __TEXT.__const: 0x6890
+  __TEXT.__objc_methlist: 0x394
+  __TEXT.__const: 0x68f8
   __TEXT.__cstring: 0x124b
   __TEXT.__objc_classname: 0x9e
   __TEXT.__objc_methname: 0xa41
   __TEXT.__objc_methtype: 0x2df
   __TEXT.__oslogstring: 0xe8d
-  __TEXT.__unwind_info: 0x380
-  __DATA_CONST.__auth_got: 0x3d0
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1908
+  __TEXT.__unwind_info: 0x3c0
+  __DATA_CONST.__auth_got: 0x3c8
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x19f8
   __DATA_CONST.__cfstring: 0x12a0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x8f0
-  __DATA.__objc_selrefs: 0x2a8
+  __DATA.__objc_const: 0x648
+  __DATA.__objc_selrefs: 0x348
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 337
-  Symbols:   2216
+  Functions: 367
+  Symbols:   2335
   CStrings:  474
 
Symbols:
+ +[ACCUserDefaults sharedDefaultsIapd].cold.1
+ +[ACCUserDefaults sharedDefaultsLogging].cold.1
+ +[ACCUserDefaults sharedDefaults].cold.1
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.21
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.22
+ -[ACCHWComponentAuthService _verifyCertificate:].cold.3
+ -[ACCHWComponentAuthService authenticateBatteryWithChallenge:completionHandler:].cold.1
+ -[ACCHWComponentAuthService authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:].cold.1
+ -[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:].cold.1
+ -[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:].cold.1
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ __Img4DecodePayloadPropertyExistsWithValue
+ __oidQCCompliance
+ __oidQCDisclosures
+ __oidQCEuRetentionPeriod
+ __oidQCLimitValue
+ __oidQCStatements
+ __oidQCSyntaxv1
+ __oidQCSyntaxv2
+ __oidQCType
+ __oidQCTypeEseal
+ __oidQCTypeEsign
+ __oidQCTypeWeb
+ __oidSemanticsIdEidasLegal
+ __oidSemanticsIdEidasNatural
+ __oidSemanticsIdLegal
+ __oidSemanticsIdNatural
+ _memset
+ _oidQCCompliance
+ _oidQCDisclosures
+ _oidQCEuRetentionPeriod
+ _oidQCLimitValue
+ _oidQCStatements
+ _oidQCSyntaxv1
+ _oidQCSyntaxv2
+ _oidQCType
+ _oidQCTypeEseal
+ _oidQCTypeEsign
+ _oidQCTypeWeb
+ _oidSemanticsIdEidasLegal
+ _oidSemanticsIdEidasNatural
+ _oidSemanticsIdLegal
+ _oidSemanticsIdNatural
+ systemInfo_copyRegionCode.cold.1
+ systemInfo_isDeveloperBuild.cold.1
+ systemInfo_isInternalBuild.cold.1
+ systemInfo_systemSupportsPearl.cold.1
+ systemInfo_systemSupportsWAPI.cold.1
- __138-[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke.cold.1
- _objc_retain_x25
- _objc_retain_x27
- copyCertificateForFDRData.cold.1
- copyCertificateForFDRData.cold.2
- copyCertificateForFDRData.cold.3
- copyCertificateForFDRData.cold.4
- copyCertificateForFDRData.cold.5
- copyCertificateForFDRData.cold.6
- copyCertificateForFDRData.cold.7

```
