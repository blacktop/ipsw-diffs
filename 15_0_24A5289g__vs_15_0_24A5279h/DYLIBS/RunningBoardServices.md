## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices`

```diff

-942.0.0.0.0
-  __TEXT.__text: 0x47b88
+940.0.0.0.0
+  __TEXT.__text: 0x477d0
   __TEXT.__auth_stubs: 0xc60
   __TEXT.__objc_methlist: 0x5348
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x482f
-  __TEXT.__oslogstring: 0x28a9
+  __TEXT.__cstring: 0x4829
+  __TEXT.__oslogstring: 0x27c4
   __TEXT.__gcc_except_tab: 0x8f4
   __TEXT.__unwind_info: 0x1470
   __TEXT.__objc_classname: 0xee7
-  __TEXT.__objc_methname: 0x7be0
+  __TEXT.__objc_methname: 0x7bd6
   __TEXT.__objc_methtype: 0x1524
   __TEXT.__objc_stubs: 0x4ae0
   __DATA_CONST.__got: 0x4e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2123
-  Symbols:   4748
+  Functions: 2119
+  Symbols:   4744
   CStrings:  888
 
Symbols:
+ +[RBSProcessIdentity decodeFromJob:]
+ -[RBSDextProcessIdentity initWithDecodeFromJob:]
+ -[RBSMacAppProcessIdentity initWithDecodeFromJob:]
+ -[RBSMacAppProcessIdentity initWithDecodeFromJob:].cold.1
+ -[RBSOSServiceProcessIdentity initWithDecodeFromJob:]
+ -[RBSOpaqueProcessIdentity initWithDecodeFromJob:]
+ -[RBSProcessIdentity initWithDecodeFromJob:]
+ -[RBSXPCServiceProcessIdentity initWithDecodeFromJob:]
+ _objc_msgSend$decodeFromJob:
+ _objc_msgSend$initWithDecodeFromJob:
- +[RBSProcessIdentity decodeFromJob:uuid:]
- -[RBSDextProcessIdentity initWithDecodeFromJob:uuid:]
- -[RBSDextProcessIdentity initWithDecodeFromJob:uuid:].cold.1
- -[RBSMacAppProcessIdentity initWithDecodeFromJob:uuid:]
- -[RBSMacAppProcessIdentity initWithDecodeFromJob:uuid:].cold.1
- -[RBSMacAppProcessIdentity initWithDecodeFromJob:uuid:].cold.2
- -[RBSOSServiceProcessIdentity initWithDecodeFromJob:uuid:]
- -[RBSOSServiceProcessIdentity initWithDecodeFromJob:uuid:].cold.1
- -[RBSOpaqueProcessIdentity initWithDecodeFromJob:uuid:]
- -[RBSOpaqueProcessIdentity initWithDecodeFromJob:uuid:].cold.1
- -[RBSProcessIdentity initWithDecodeFromJob:uuid:]
- -[RBSXPCServiceProcessIdentity initWithDecodeFromJob:uuid:]
- _objc_msgSend$decodeFromJob:uuid:
- _objc_msgSend$initWithDecodeFromJob:uuid:
CStrings:
+ "-[RBSProcessIdentity initWithDecodeFromJob:]"
+ "u"
- "-[RBSProcessIdentity initWithDecodeFromJob:uuid:]"
- "hu"

```
