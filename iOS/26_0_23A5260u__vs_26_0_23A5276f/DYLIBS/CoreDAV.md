## CoreDAV

> `/System/Library/PrivateFrameworks/CoreDAV.framework/CoreDAV`

```diff

-1235.0.0.0.0
-  __TEXT.__text: 0x52010
+1236.0.0.0.0
+  __TEXT.__text: 0x5219c
   __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x56b0
+  __TEXT.__objc_methlist: 0x56e0
   __TEXT.__cstring: 0x3d21
   __TEXT.__const: 0xe0
   __TEXT.__oslogstring: 0x4402
   __TEXT.__gcc_except_tab: 0x810
   __TEXT.__unwind_info: 0xf58
   __TEXT.__objc_classname: 0xd42
-  __TEXT.__objc_methname: 0xbb7a
+  __TEXT.__objc_methname: 0xbc30
   __TEXT.__objc_methtype: 0x19e9
-  __TEXT.__objc_stubs: 0x7600
+  __TEXT.__objc_stubs: 0x7640
   __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0xf78
   __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2760
+  __DATA_CONST.__objc_selrefs: 0x2780
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x540
   __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__cfstring: 0x5c20
-  __AUTH_CONST.__objc_const: 0xada0
+  __AUTH_CONST.__objc_const: 0xadd0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x790
+  __DATA.__objc_ivar: 0x794
   __DATA.__data: 0x920
   __DATA.__bss: 0xf0
   __DATA_DIRTY.__objc_data: 0x2260

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: AC6FF994-CF9A-3026-A036-5B239425972A
-  Functions: 1708
-  Symbols:   6449
-  CStrings:  4099
+  UUID: 5E47DCAC-816C-3066-A778-6F3A5FB1E933
+  Functions: 1711
+  Symbols:   6459
+  CStrings:  4105
 
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
