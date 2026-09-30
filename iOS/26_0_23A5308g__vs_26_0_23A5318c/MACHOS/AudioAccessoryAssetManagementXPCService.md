## AudioAccessoryAssetManagementXPCService

> `/System/Library/PrivateFrameworks/AudioAccessoryAssetManagement.framework/XPCServices/AudioAccessoryAssetManagementXPCService.xpc/AudioAccessoryAssetManagementXPCService`

```diff

-30.58.1.0.0
-  __TEXT.__text: 0x2ba4
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x2ec
+30.59.1.7.0
+  __TEXT.__text: 0x2f00
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x2f4
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__cstring: 0xd94
-  __TEXT.__objc_methname: 0xd7a
-  __TEXT.__objc_classname: 0xe1
-  __TEXT.__objc_methtype: 0x3b0
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0x198
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x1e0
+  __TEXT.__cstring: 0xf04
+  __TEXT.__objc_methname: 0xdcb
+  __TEXT.__objc_classname: 0xe3
+  __TEXT.__objc_methtype: 0x3e0
+  __TEXT.__unwind_info: 0x158
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__const: 0x208
   __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x648
-  __DATA.__objc_selrefs: 0x3d0
-  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_const: 0x688
+  __DATA.__objc_selrefs: 0x3d8
+  __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1f0
   - /System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A21BDD88-AA25-3E51-A311-5254CCAB8B86
-  Functions: 64
-  Symbols:   89
-  CStrings:  281
+  UUID: 0ACFC922-7FF9-3B91-9EAB-49258BE4D90B
+  Functions: 68
+  Symbols:   97
+  CStrings:  293
 
Symbols:
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_time
+ _objc_release_x28
CStrings:
+ "-[AudioAccessoryAssetManagementClientXPCConnection _postProgressUpdate:totalCount:]"
+ "-[AudioAccessoryAssetManagementClientXPCConnection _postProgressUpdate:totalCount:]_block_invoke"
+ "@\"NSObject<OS_dispatch_source>\""
+ "Artificial Update Timer fired"
+ "Q"
+ "_artificialUpdateTimer"
+ "_maxCompleteDownloadUnits"
+ "_postProgressUpdate %lu"
+ "_postProgressUpdate:totalCount:"
+ "completedDownloadUnits(%lu) > maxCompleteDownloadUnits(%lu)"
+ "completedDownloadUnits(%lu) is not greater maxCompleteDownloadUnits(%lu)"
+ "v32@0:8Q16Q24"

```
