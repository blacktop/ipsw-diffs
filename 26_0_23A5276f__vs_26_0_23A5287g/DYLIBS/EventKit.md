## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

```diff

-1929.0.0.0.0
-  __TEXT.__text: 0x14a748
+1930.0.0.0.0
+  __TEXT.__text: 0x14a8dc
   __TEXT.__auth_stubs: 0x1a00
-  __TEXT.__objc_methlist: 0x1559c
+  __TEXT.__objc_methlist: 0x155ac
   __TEXT.__const: 0xc50
   __TEXT.__cstring: 0xb8ee
   __TEXT.__oslogstring: 0xe23e

   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_capture: 0x10
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__unwind_info: 0x5318
+  __TEXT.__unwind_info: 0x53f0
   __TEXT.__eh_frame: 0x3a0
   __TEXT.__objc_classname: 0x1af1
-  __TEXT.__objc_methname: 0x2ea1d
+  __TEXT.__objc_methname: 0x2ea29
   __TEXT.__objc_methtype: 0x48ff
-  __TEXT.__objc_stubs: 0x20f60
+  __TEXT.__objc_stubs: 0x20f80
   __DATA_CONST.__got: 0x1770
   __DATA_CONST.__const: 0x4760
   __DATA_CONST.__objc_classlist: 0x760
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xab78
+  __DATA_CONST.__objc_selrefs: 0xab80
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x5d8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 226C0A8B-8CE5-38A8-AD9C-3C7C9AF62675
-  Functions: 8937
-  Symbols:   27061
-  CStrings:  11531
+  UUID: 13C3041E-A50A-3A5D-A61A-3855F487C733
+  Functions: 8941
+  Symbols:   27070
+  CStrings:  11532
 
Symbols:
+ +[EKDaemonConnection sharedQueue]
+ +[EKDaemonConnection sharedQueue].cold.1
+ ___33+[EKDaemonConnection sharedQueue]_block_invoke
+ ___52-[EKDaemonConnection _finishAllRepliesOnServerDeath]_block_invoke_2.cold.1
+ ___52-[EKDaemonConnection _finishAllRepliesOnServerDeath]_block_invoke_2.cold.2
+ ___64-[EKDaemonConnection CADClientReceivePredicateResults:forToken:]_block_invoke
+ ___85-[EKDaemonConnection CADClientReceiveDiagnosticsCollectionResults:forToken:finished:]_block_invoke
+ ___91-[EKDaemonConnection CADClientReceiveOccurrenceCacheSearchResults:forSearchToken:finished:]_block_invoke
+ _objc_msgSend$sharedQueue
+ _sharedQueue.onceToken
+ _sharedQueue.sharedQueue
- -[EKDaemonConnection _finishAllRepliesOnServerDeath].cold.1
- GCC_except_table36
- ___52-[EKDaemonConnection _finishAllRepliesOnServerDeath]_block_invoke_3
- ___52-[EKDaemonConnection _finishAllRepliesOnServerDeath]_block_invoke_3.cold.1
- ___52-[EKDaemonConnection _finishAllRepliesOnServerDeath]_block_invoke_3.cold.2
- __finishAllRepliesOnServerDeath.disconnectionQueue
- __finishAllRepliesOnServerDeath.onceToken
CStrings:
+ "EventKitClientConnectionQ"
+ "sharedQueue"
- "EventKitClientDisconnectionQ"

```
