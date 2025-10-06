## DaemonUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils`

```diff

-1394.82.1.0.0
-  __TEXT.__text: 0xd9c0
+1394.100.151.0.1
+  __TEXT.__text: 0xe088
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x10c4
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0xe2e
+  __TEXT.__objc_methlist: 0x10dc
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0xed9
   __TEXT.__oslogstring: 0xd84
   __TEXT.__gcc_except_tab: 0x1a0
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__unwind_info: 0x4ec
   __TEXT.__objc_classname: 0x286
-  __TEXT.__objc_methname: 0x333c
+  __TEXT.__objc_methname: 0x33a6
   __TEXT.__objc_methtype: 0x7af
-  __TEXT.__objc_stubs: 0x28c0
+  __TEXT.__objc_stubs: 0x29e0
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x460
+  __DATA_CONST.__const: 0x4b0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x26a8
-  __DATA_CONST.__objc_selrefs: 0xd00
+  __DATA_CONST.__objc_selrefs: 0xd20
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__cfstring: 0xe40
+  __AUTH_CONST.__cfstring: 0xf60
   __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__objc_const: 0x940
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x368
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x180
-  __DATA.__objc_superrefs: 0xa0
   __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x240
   __DATA.__bss: 0x88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA08259A-2417-3588-9C91-FDCB97016982
-  Functions: 444
-  Symbols:   1789
-  CStrings:  1112
+  UUID: E8497AF0-C6A0-3CB9-8021-DF980178FE48
+  Functions: 448
+  Symbols:   1808
+  CStrings:  1137
 
Symbols:
+ -[BiometryHelper _dumpEnvironmentForUser:]
+ -[BiometryHelper dumpStatus]
+ ___42-[BiometryHelper _dumpEnvironmentForUser:]_block_invoke
+ ___42-[BiometryHelper _dumpEnvironmentForUser:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40s_e15_"NSString"8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e52_"NSObject<NSCoding><NSCopying><NSSecureCoding>"8?0ls32l8s40l8
+ ___block_literal_global.130
+ ___block_literal_global.137
+ ___block_literal_global.201
+ _objc_msgSend$_dumpEnvironmentForUser:
+ _objc_msgSend$biometryDatabaseHashForUser:error:
+ _objc_msgSend$catacombUUID:
+ _objc_msgSend$isAnyUserEnrolledWithError:
+ _objc_msgSend$isBiometryOnForApplePay:
+ _objc_msgSend$isIdentificationEnabled:
+ _objc_msgSend$isPeriocularMatchingEnabledForUser:
+ _objc_msgSend$isStrictModeEnabled
+ _objc_msgSend$numberWithUnsignedInteger:
- ___block_literal_global.129
- ___block_literal_global.136
- ___block_literal_global.200
CStrings:
+ "@\"NSObject<NSCoding><NSCopying><NSSecureCoding>\"8@?0"
+ "@\"NSString\"8@?0"
+ "ApplePay"
+ "T@\"NSString\",?,R,C"
+ "_dumpEnvironmentForUser:"
+ "biometryDbHash"
+ "catacombUUID"
+ "dumpStatus"
+ "identification"
+ "isStrictModeEnabled"
+ "lockoutState"
+ "numberWithUnsignedInteger:"
+ "periocular"
+ "unlock"
+ "user %@"

```
