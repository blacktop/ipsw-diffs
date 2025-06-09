## CoreDAV

> `/System/Library/PrivateFrameworks/CoreDAV.framework/CoreDAV`

```diff

-1230.5.2.0.0
-  __TEXT.__text: 0x51d68
+1235.0.0.0.0
+  __TEXT.__text: 0x52010
   __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x56a0
-  __TEXT.__cstring: 0x3d18
+  __TEXT.__objc_methlist: 0x56b0
+  __TEXT.__cstring: 0x3d21
   __TEXT.__const: 0xe0
   __TEXT.__oslogstring: 0x4402
   __TEXT.__gcc_except_tab: 0x810
-  __TEXT.__unwind_info: 0xf50
+  __TEXT.__unwind_info: 0xf58
   __TEXT.__objc_classname: 0xd42
-  __TEXT.__objc_methname: 0xbb23
+  __TEXT.__objc_methname: 0xbb7a
   __TEXT.__objc_methtype: 0x19e9
-  __TEXT.__objc_stubs: 0x75e0
+  __TEXT.__objc_stubs: 0x7600
   __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0xf78
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2748
+  __DATA_CONST.__objc_selrefs: 0x2760
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x540
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x5c00
-  __AUTH_CONST.__objc_const: 0xad60
+  __AUTH_CONST.__cfstring: 0x5c20
+  __AUTH_CONST.__objc_const: 0xada0
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x790
   __DATA.__data: 0x920
   __DATA.__bss: 0xf0
-  __DATA_DIRTY.__objc_data: 0x22b0
+  __DATA_DIRTY.__objc_data: 0x2260
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 72B1E243-B508-35A1-B179-FC637001EFC4
-  Functions: 1707
-  Symbols:   6447
-  CStrings:  4093
+  UUID: AC6FF994-CF9A-3026-A036-5B239425972A
+  Functions: 1708
+  Symbols:   6449
+  CStrings:  4099
 
Symbols:
+ -[CoreDAVContainerMultiGetTask allProperties]
+ __OBJC_$_PROP_LIST_CoreDAVAccountInfoProvider
+ ___43-[CoreDAVDiscoveryTaskGroup startTaskGroup]_block_invoke.286
+ ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.298
+ ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.299
+ ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.303
+ ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.307
+ ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.314
+ ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.315
+ _objc_msgSend$base64EncodedStringWithOptions:
- ___43-[CoreDAVDiscoveryTaskGroup startTaskGroup]_block_invoke.283
- ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.295
- ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.296
- ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.300
- ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.304
- ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.311
- ___53-[CoreDAVDiscoveryTaskGroup completeDiscovery:error:]_block_invoke.312
Functions:
+ sub_2196a9190
+ -[CoreDAVContainerMultiGetTask allProperties]
~ -[CoreDAVContainerMultiGetTask finishCoreDAVTaskWithError:] : 1812 -> 1784
~ -[CoreDAVTask performCoreDAVTask] : 6412 -> 6924
- sub_213bb0ff4
CStrings:
+ "Basic %@"
+ "T@\"NSDictionary\",?,R,N"
+ "allProperties"
+ "base64EncodedStringWithOptions:"
+ "contextDictionary"

```
