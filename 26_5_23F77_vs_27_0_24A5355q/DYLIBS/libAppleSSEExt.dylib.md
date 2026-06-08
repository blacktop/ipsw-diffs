## libAppleSSEExt.dylib

> `/usr/lib/libAppleSSEExt.dylib`

```diff

-320.0.0.0.0
-  __TEXT.__text: 0x3698
-  __TEXT.__auth_stubs: 0x330
+325.0.0.0.0
+  __TEXT.__text: 0x3260
   __TEXT.__objc_methlist: 0xbc
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__cstring: 0x1da
+  __TEXT.__gcc_except_tab: 0xc0
+  __TEXT.__cstring: 0x1dc
   __TEXT.__oslogstring: 0x536
-  __TEXT.__unwind_info: 0x138
-  __TEXT.__objc_classname: 0x13
-  __TEXT.__objc_methname: 0x38d
-  __TEXT.__objc_methtype: 0x87
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__unwind_info: 0x128
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x148
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x18
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BEB03664-8C4C-3F6C-9903-17185015BC19
-  Functions: 88
-  Symbols:   343
-  CStrings:  107
+  UUID: C1F00F8A-BBE2-35C9-A6E2-FC06806FAE43
+  Functions: 82
+  Symbols:   330
+  CStrings:  50
 
Symbols:
+ ___28+[BAASupport prepareLazily:]_block_invoke.18
+ ___block_literal_global.100
+ ___block_literal_global.103
+ ___block_literal_global.20
+ ___block_literal_global.77
+ ___block_literal_global.79
+ ___block_literal_global.82
+ ___block_literal_global.94
+ ___block_literal_global.97
+ ___scheduleBAACertificateIssuanceRetryTimer_block_invoke.95
+ ___scheduleBAACertificateRenewalTimer_block_invoke.101
- GCC_except_table52
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- ___28+[BAASupport prepareLazily:]_block_invoke.19
- ___block_literal_global.101
- ___block_literal_global.104
- ___block_literal_global.21
- ___block_literal_global.78
- ___block_literal_global.80
- ___block_literal_global.83
- ___block_literal_global.95
- ___block_literal_global.98
- ___scheduleBAACertificateIssuanceRetryTimer_block_invoke.96
- ___scheduleBAACertificateRenewalTimer_block_invoke.102
CStrings:
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_source>\""
- "B16@0:8"
- "BAASupport"
- "Timer"
- "_timer"
- "addObject:"
- "array"
- "arrayWithObjects:count:"
- "boolValue"
- "cancel"
- "componentsJoinedByString:"
- "confirmSigKey:status:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataWithBytes:length:"
- "dateWithTimeIntervalSinceNow:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "dictionaryWithObjects:forKeys:count:"
- "earlierDate:"
- "generateSigKey:keyData:attestation:pubKey:"
- "getCertificateExpirationDate:"
- "getCertificates:"
- "getSigKeyCertificates:certificates:"
- "getSigKeyExpDate:expirationDate:"
- "i16@0:8"
- "i20@0:8B16"
- "i24@0:8^@16"
- "i24@0:8^d16"
- "initialize"
- "isActive"
- "isEqualToDate:"
- "isEqualToString:"
- "isInternal"
- "issueNewCertificate"
- "lock"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "prepare"
- "prepareLazily"
- "prepareLazily:"
- "resetWithTimeInterval:block:"
- "setBlessedUser:keybagUUID:"
- "setDelegate:"
- "setSigKey:expirationDate:keyData:certificates:"
- "standardUserDefaults"
- "timeIntervalSinceNow"
- "timeIntervalSinceReferenceDate"
- "unlock"
- "unsignedIntValue"
- "unsignedLongValue"
- "v16@0:8"
- "v24@0:8@16"
- "v28@0:8I16[16C]20"
- "v32@0:8d16@?24"

```
