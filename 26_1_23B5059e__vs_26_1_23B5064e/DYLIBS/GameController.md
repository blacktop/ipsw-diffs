## GameController

> `/System/Library/Frameworks/GameController.framework/GameController`

```diff

-13.1.7.0.0
-  __TEXT.__text: 0x10567c
+13.1.8.0.0
+  __TEXT.__text: 0x1056ec
   __TEXT.__auth_stubs: 0x1c30
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xfd8c
   __TEXT.__const: 0x3c74
   __TEXT.__cstring: 0xa179
-  __TEXT.__gcc_except_tab: 0x58f8
+  __TEXT.__gcc_except_tab: 0x5964
   __TEXT.__oslogstring: 0x97d8
   __TEXT.__dlopen_cstrs: 0xfd
   __TEXT.__swift5_typeref: 0x574

   __TEXT.__objc_classname: 0x41ad
   __TEXT.__objc_methname: 0x18f87
   __TEXT.__objc_methtype: 0x7bcc
-  __TEXT.__objc_stubs: 0xf3c0
+  __TEXT.__objc_stubs: 0xf3a0
   __DATA_CONST.__got: 0xba8
   __DATA_CONST.__const: 0x2d68
   __DATA_CONST.__objc_classlist: 0x990

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D903152C-46F7-3859-82D6-18E50E0F394F
-  Functions: 7371
-  Symbols:   27364
+  UUID: 3552C9CD-F4A7-3508-BCBC-859200AED616
+  Functions: 7372
+  Symbols:   27366
   CStrings:  9775
 
Symbols:
+ -[_GCDefaultLogicalDevice updateSystemGestureStateForSettings].cold.1
- _objc_msgSend$hasButtonThief
Functions:
+ -[_GCDefaultLogicalDevice updateSystemGestureStateForSettings]
~ -[_GCDefaultLogicalDevice activateLogical] : 500 -> 152
- -[_GCDefaultLogicalDevice updateSystemGestureStateForSettings]
+ -[_GCDefaultLogicalDevice updateSystemGestureStateForSettings].cold.1

```
