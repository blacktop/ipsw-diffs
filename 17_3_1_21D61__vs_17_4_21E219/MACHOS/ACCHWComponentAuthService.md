## ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService`

```diff

-898.80.3.0.0
-  __TEXT.__text: 0xfd60
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_stubs: 0x860
-  __TEXT.__objc_methlist: 0x1f4
+919.100.33.0.0
+  __TEXT.__text: 0x101a4
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__objc_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x20c
   __TEXT.__const: 0x5b90
-  __TEXT.__cstring: 0xe66
+  __TEXT.__cstring: 0xf97
   __TEXT.__objc_classname: 0x9e
-  __TEXT.__objc_methname: 0x8fb
-  __TEXT.__objc_methtype: 0x266
-  __TEXT.__oslogstring: 0xe7f
+  __TEXT.__objc_methname: 0x94b
+  __TEXT.__objc_methtype: 0x273
+  __TEXT.__oslogstring: 0xed9
   __TEXT.__unwind_info: 0x340
-  __DATA_CONST.__auth_got: 0x3b0
+  __DATA_CONST.__auth_got: 0x3b8
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x15f0
-  __DATA_CONST.__cfstring: 0xd60
+  __DATA_CONST.__const: 0x1688
+  __DATA_CONST.__cfstring: 0xf60
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x880
-  __DATA.__objc_selrefs: 0x260
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x68
-  __DATA.__objc_ivar: 0x1c
+  __DATA.__objc_const: 0x8b0
+  __DATA.__objc_selrefs: 0x278
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1b0
   __DATA.__bss: 0xc9

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 361
-  Symbols:   2208
-  CStrings:  405
+  Functions: 364
+  Symbols:   2266
+  CStrings:  433
 
Symbols:
+ -[ACCHWComponentAuthService _verifyModuleCertificate:forModuleType:].cold.12
+ -[ACCHWComponentAuthServiceParams setSkipComms:]
+ -[ACCHWComponentAuthServiceParams skipComms]
+ OBJC_IVAR_$_ACCHWComponentAuthServiceParams._skipComms
+ _ACCUserDefaultsKey_ForceAccInfoUpdateRelaySupport
+ _ACCUserDefaultsKey_ForceMFi4AuthOverNFC
+ _ACCUserDefaultsKey_IgnoreAccInfoUpdateRelaySupport
+ _ACCUserDefaultsKey_IgnoreAuthReset
+ _ACCUserDefaultsKey_MFi4ECDSADisallow
+ _ACCUserDefaultsKey_MFi4ECDSAOnly
+ _ACCUserDefaultsKey_MFi4SigmaIRequired
+ _ACCUserDefaultsKey_PacketLoggingPlainTextOnly
+ _ACCUserDefaultsKey_PretendNoDeviceIdentityCerts
+ _OBJC_CLASS_$_NSNumber
+ __block_literal_global.229
+ __block_literal_global.231
+ __block_literal_global.54
+ __block_literal_global.57
+ _arc4random_buf
+ _kCFACCUserDefaultsKey_ForceAccInfoUpdateRelaySupport
+ _kCFACCUserDefaultsKey_ForceMFi4AuthOverNFC
+ _kCFACCUserDefaultsKey_IgnoreAccInfoUpdateRelaySupport
+ _kCFACCUserDefaultsKey_IgnoreAuthReset
+ _kCFACCUserDefaultsKey_MFi4ECDSADisallow
+ _kCFACCUserDefaultsKey_MFi4ECDSAOnly
+ _kCFACCUserDefaultsKey_MFi4SigmaIRequired
+ _kCFACCUserDefaultsKey_PacketLoggingPlainTextOnly
+ _kCFACCUserDefaultsKey_PretendNoDeviceIdentityCerts
+ _objc_msgSend$charValue
+ _objc_msgSend$setSkipComms:
+ _objc_msgSend$skipComms
+ _objc_opt_isKindOfClass
- __block_literal_global.202
- __block_literal_global.204
- __block_literal_global.46
- __block_literal_global.49
- _objc_retain_x27
CStrings:
+ "%"
+ "(moduleType=%d) Error: signature==NULL"
+ "(moduleType=%d) Failure: cannot find touchTypeData"
+ "B"
+ "Challenge"
+ "ForceAccInfoUpdateRelaySupport"
+ "ForceMFi4AuthOverNFC"
+ "IgnoreAccInfoUpdateRelaySupport"
+ "IgnoreAuthReset"
+ "MFi4ECDSADisallow"
+ "MFi4ECDSAOnly"
+ "MFi4SigmaIRequired"
+ "PacketLoggingPlainTextOnly"
+ "PretendAuthFailure"
+ "PretendNoDeviceIdentityCerts"
+ "Signature"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_skipComms"
+ "_skipComms"
+ "authError"
+ "charValue"
+ "iPad"
+ "iPad Display"
+ "iPhone"
+ "iboot-auth"
+ "pretend_auth"
+ "setSkipComms:"
+ "skipComms"
+ "v20@0:8B16"
- "\x15"

```
