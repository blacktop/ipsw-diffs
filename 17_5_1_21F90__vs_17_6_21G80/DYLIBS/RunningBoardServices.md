## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`

```diff

-874.122.2.0.0
-  __TEXT.__text: 0x3f5e4
+874.140.4.0.0
+  __TEXT.__text: 0x3f950
   __TEXT.__auth_stubs: 0xde0
   __TEXT.__objc_methlist: 0x51d8
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x44e6
-  __TEXT.__oslogstring: 0x25d0
+  __TEXT.__cstring: 0x44ec
+  __TEXT.__oslogstring: 0x26b5
   __TEXT.__gcc_except_tab: 0x70c
-  __TEXT.__unwind_info: 0x1408
+  __TEXT.__unwind_info: 0x1410
   __TEXT.__objc_classname: 0xe9b
-  __TEXT.__objc_methname: 0x791b
+  __TEXT.__objc_methname: 0x7923
   __TEXT.__objc_methtype: 0x14fb
   __TEXT.__objc_stubs: 0x4860
   __DATA_CONST.__got: 0x100

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 03D1B7EB-1F38-3722-BF99-BEE6D411D810
-  Functions: 2057
-  Symbols:   6554
-  CStrings:  3550
+  UUID: 26D3A64B-CAEE-39CD-BE69-4816308DED43
+  Functions: 2061
+  Symbols:   6562
+  CStrings:  3554
 
Symbols:
+ +[RBSProcessIdentity decodeFromJob:uuid:]
+ -[RBSDextProcessIdentity initWithDecodeFromJob:uuid:]
+ -[RBSDextProcessIdentity initWithDecodeFromJob:uuid:].cold.1
+ -[RBSEmbeddedAppProcessIdentity initWithDecodeFromJob:uuid:]
+ -[RBSEmbeddedAppProcessIdentity initWithDecodeFromJob:uuid:].cold.1
+ -[RBSEmbeddedAppProcessIdentity initWithDecodeFromJob:uuid:].cold.2
+ -[RBSOSServiceProcessIdentity initWithDecodeFromJob:uuid:]
+ -[RBSOSServiceProcessIdentity initWithDecodeFromJob:uuid:].cold.1
+ -[RBSOpaqueProcessIdentity initWithDecodeFromJob:uuid:]
+ -[RBSOpaqueProcessIdentity initWithDecodeFromJob:uuid:].cold.1
+ -[RBSProcessIdentity initWithDecodeFromJob:uuid:]
+ -[RBSXPCServiceProcessIdentity initWithDecodeFromJob:uuid:]
+ _objc_msgSend$decodeFromJob:uuid:
+ _objc_msgSend$initWithDecodeFromJob:uuid:
- +[RBSProcessIdentity decodeFromJob:]
- -[RBSDextProcessIdentity initWithDecodeFromJob:]
- -[RBSEmbeddedAppProcessIdentity initWithDecodeFromJob:]
- -[RBSEmbeddedAppProcessIdentity initWithDecodeFromJob:].cold.1
- -[RBSOSServiceProcessIdentity initWithDecodeFromJob:]
- -[RBSOpaqueProcessIdentity initWithDecodeFromJob:]
- -[RBSProcessIdentity initWithDecodeFromJob:]
- -[RBSXPCServiceProcessIdentity initWithDecodeFromJob:]
- _objc_msgSend$decodeFromJob:
- _objc_msgSend$initWithDecodeFromJob:
CStrings:
+ "-[RBSProcessIdentity initWithDecodeFromJob:uuid:]"
+ "There is no reason a daemon should have a UUID: %@"
+ "There is no reason an app identity should have a UUID: %@"
+ "There is no reason an dext identity should have a UUID: %@"
+ "There is no reason an opaque identity should have a UUID %@:"
+ "decodeFromJob:uuid:"
+ "hu"
+ "initWithDecodeFromJob:uuid:"
- "-[RBSProcessIdentity initWithDecodeFromJob:]"
- "decodeFromJob:"
- "initWithDecodeFromJob:"
- "u"

```
