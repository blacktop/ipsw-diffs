## ActivitySharingDaemonCore

> `/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore`

```diff

-2026.1.1.0.0
-  __TEXT.__text: 0x7d72c
+2026.1.2.0.0
+  __TEXT.__text: 0x7d8c8
   __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_methlist: 0x45ac
+  __TEXT.__objc_methlist: 0x45b4
   __TEXT.__const: 0x1d8
   __TEXT.__cstring: 0x2ffc
   __TEXT.__gcc_except_tab: 0xfec
-  __TEXT.__oslogstring: 0xe93b
+  __TEXT.__oslogstring: 0xe96d
   __TEXT.__unwind_info: 0x1bd8
   __TEXT.__objc_classname: 0x9fd
-  __TEXT.__objc_methname: 0x1143d
+  __TEXT.__objc_methname: 0x1144f
   __TEXT.__objc_methtype: 0x2a59
-  __TEXT.__objc_stubs: 0xc6c0
+  __TEXT.__objc_stubs: 0xc6e0
   __DATA_CONST.__got: 0xa30
   __DATA_CONST.__const: 0x3b60
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37f0
+  __DATA_CONST.__objc_selrefs: 0x37f8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xf0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA13222A-ED03-330D-B903-25FB5F8EE822
-  Functions: 2361
-  Symbols:   8805
-  CStrings:  4212
+  UUID: BA81C56E-8C27-3E2F-8DEA-BF0F6CE22A89
+  Functions: 2364
+  Symbols:   8814
+  CStrings:  4214
 
Symbols:
+ -[ASCloudKitManager allObserversReady]
+ -[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:].cold.1
+ GCC_except_table186
+ ___38-[ASCloudKitManager allObserversReady]_block_invoke
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.315
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.317
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.319
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.326
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.328
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.316
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.320
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.327
+ _objc_msgSend$allObserversReady
- GCC_except_table184
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.314
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.316
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.318
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.320
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.327
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.315
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.319
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.326
CStrings:
+ "CloudKit manager is not ready to process requests"
+ "allObserversReady"

```
