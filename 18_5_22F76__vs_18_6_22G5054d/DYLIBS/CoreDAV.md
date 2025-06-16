## CoreDAV

> `/System/Library/PrivateFrameworks/CoreDAV.framework/CoreDAV`

```diff

-1230.5.2.0.0
-  __TEXT.__text: 0x51d68
+1230.7.2.0.0
+  __TEXT.__text: 0x51ec8
   __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x56a0
+  __TEXT.__objc_methlist: 0x56d0
   __TEXT.__cstring: 0x3d18
   __TEXT.__const: 0xe0
   __TEXT.__oslogstring: 0x4402
   __TEXT.__gcc_except_tab: 0x810
   __TEXT.__unwind_info: 0xf50
   __TEXT.__objc_classname: 0xd42
-  __TEXT.__objc_methname: 0xbb23
+  __TEXT.__objc_methname: 0xbbd9
   __TEXT.__objc_methtype: 0x19e9
-  __TEXT.__objc_stubs: 0x75e0
+  __TEXT.__objc_stubs: 0x7620
   __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0xf78
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2748
+  __DATA_CONST.__objc_selrefs: 0x2768
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x540
   __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__cfstring: 0x5c00
-  __AUTH_CONST.__objc_const: 0xad60
+  __AUTH_CONST.__objc_const: 0xad90
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_ivar: 0x790
+  __DATA.__objc_ivar: 0x794
   __DATA.__data: 0x920
   __DATA.__bss: 0xf0
   __DATA_DIRTY.__objc_data: 0x22b0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 72B1E243-B508-35A1-B179-FC637001EFC4
-  Functions: 1707
-  Symbols:   6447
-  CStrings:  4093
+  UUID: C5791C3A-9989-3006-B954-D6AAD233DFF4
+  Functions: 1710
+  Symbols:   6457
+  CStrings:  4099
 
Symbols:
+ +[CoreDAVContainerSyncTaskGroup _isInsufficientStorage:]
+ -[CoreDAVContainerSyncTaskGroup insufficientStorageRetryCount]
+ -[CoreDAVContainerSyncTaskGroup setInsufficientStorageRetryCount:]
+ _OBJC_IVAR_$_CoreDAVContainerSyncTaskGroup._insufficientStorageRetryCount
+ __OBJC_$_CLASS_METHODS_CoreDAVContainerSyncTaskGroup
+ ___68-[CoreDAVContainerSyncTaskGroup propFindTask:parsedResponses:error:]_block_invoke.97
+ _objc_msgSend$_isInsufficientStorage:
+ _objc_msgSend$shouldSkipAddForOverQuota
- ___68-[CoreDAVContainerSyncTaskGroup propFindTask:parsedResponses:error:]_block_invoke.95
CStrings:
+ "TQ,N,V_insufficientStorageRetryCount"
+ "_insufficientStorageRetryCount"
+ "_isInsufficientStorage:"
+ "insufficientStorageRetryCount"
+ "setInsufficientStorageRetryCount:"
+ "shouldSkipAddForOverQuota"

```
