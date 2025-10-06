## SafetyKit

> `/System/Library/Frameworks/SafetyKit.framework/SafetyKit`

```diff

-63.0.1.0.0
-  __TEXT.__text: 0xe1b0
+77.0.0.0.0
+  __TEXT.__text: 0xe384
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0xa20
-  __TEXT.__cstring: 0x15c6
-  __TEXT.__oslogstring: 0x1943
+  __TEXT.__objc_methlist: 0xa28
+  __TEXT.__cstring: 0x15eb
+  __TEXT.__oslogstring: 0x195e
   __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__unwind_info: 0x424
+  __TEXT.__unwind_info: 0x42c
   __TEXT.__objc_classname: 0x2c8
-  __TEXT.__objc_methname: 0x2967
+  __TEXT.__objc_methname: 0x2981
   __TEXT.__objc_methtype: 0xa61
-  __TEXT.__objc_stubs: 0x2280
+  __TEXT.__objc_stubs: 0x22a0
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0x88

   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x24a8
-  __DATA_CONST.__objc_selrefs: 0x958
+  __DATA_CONST.__objc_selrefs: 0x960
   __AUTH_CONST.__cfstring: 0x7c0
   __AUTH_CONST.__objc_const: 0x6b8
   __AUTH_CONST.__const: 0x120

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 49F64B6C-5249-3F77-9871-D72338532390
-  Functions: 398
-  Symbols:   1603
-  CStrings:  910
+  UUID: A399613E-BA2F-35BE-AF64-4E60CBE1E8D4
+  Functions: 401
+  Symbols:   1610
+  CStrings:  913
 
Symbols:
+ -[SAServer checkAndResetClientState]
+ -[SAServer checkAndResetClientState].cold.1
+ -[SAServer checkAndResetClientState].cold.2
+ GCC_except_table11
+ GCC_except_table24
+ GCC_except_table28
+ GCC_except_table32
+ GCC_except_table34
+ _objc_msgSend$checkAndResetClientState
- GCC_except_table23
- GCC_except_table27
- GCC_except_table31
- GCC_except_table33
CStrings:
+ "%s - Expiring client state"
+ "-[SAServer checkAndResetClientState]"
+ "checkAndResetClientState"

```
