## ScreenshotServices

> `/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices`

```diff

-414.101.0.0.0
-  __TEXT.__text: 0x1d320
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x254c
-  __TEXT.__const: 0x43c
+417.0.0.0.0
+  __TEXT.__text: 0x1db4c
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_methlist: 0x2564
+  __TEXT.__const: 0x448
   __TEXT.__cstring: 0x1e71
-  __TEXT.__oslogstring: 0x1219
+  __TEXT.__oslogstring: 0x1468
   __TEXT.__gcc_except_tab: 0x398
   __TEXT.__dlopen_cstrs: 0x4ae
-  __TEXT.__unwind_info: 0xab8
+  __TEXT.__unwind_info: 0xac8
   __TEXT.__objc_classname: 0x832
-  __TEXT.__objc_methname: 0x65bf
+  __TEXT.__objc_methname: 0x6600
   __TEXT.__objc_methtype: 0xfc5
-  __TEXT.__objc_stubs: 0x59e0
+  __TEXT.__objc_stubs: 0x5a20
   __DATA_CONST.__got: 0x6a0
   __DATA_CONST.__const: 0xb00
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b78
+  __DATA_CONST.__objc_selrefs: 0x1b88
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__auth_got: 0x4b8
   __AUTH_CONST.__const: 0x700
   __AUTH_CONST.__cfstring: 0x1f20
   __AUTH_CONST.__objc_const: 0x4b90
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x780
   __DATA.__objc_ivar: 0x268

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F4EBB495-D16B-3F75-A360-50E26C7CB367
-  Functions: 942
-  Symbols:   3805
-  CStrings:  2047
+  UUID: D71650D3-FA0C-341A-9020-3084508BB639
+  Functions: 947
+  Symbols:   3818
+  CStrings:  2059
 
Symbols:
+ -[SSRemoteAlertHandleProvider _cleanupCurrentHandleNotifyDelegate:]
+ -[SSRemoteAlertHandleProvider dealloc]
+ -[SSScreenshotAssetManagerPhotoLibraryBackend removeEntryWithIdentifier:completionHandler:].cold.1
+ GCC_except_table39
+ _OUTLINED_FUNCTION_4
+ ___162-[SSScreenshotAssetManagerPhotoLibraryBackend updateImageData:withModificationData:forEntryWithIdentifier:registrationOptions:imageDescription:completionHandler:]_block_invoke.cold.2
+ ___block_descriptor_81_e8_32s40s48s56s64s72bs_e48_v24?0"PHContentEditingInput"8"NSDictionary"16ls32l8s40l8s48l8s56l8s72l8s64l8
+ ___block_literal_global.143
+ _objc_msgSend$_cleanupCurrentHandleNotifyDelegate:
+ _objc_msgSend$registerObserver:
+ _objc_msgSend$ss_imageDataWithDataType:sdrImage:hdrImage:properties:imageDescription:
+ _objc_msgSend$unregisterObserver:
+ _objc_retain_x26
- GCC_except_table38
- ___block_descriptor_81_e8_32s40s48s56s64s72bs_e48_v24?0"PHContentEditingInput"8"NSDictionary"16ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.142
- _objc_msgSend$addObserver:
- _objc_msgSend$ss_imageDataWithDataType:image:hdrImage:properties:imageDescription:
CStrings:
+ "Asset deletion failed: photo library is nil for identifier %@"
+ "Asset update failed: photo library is nil for identifier %@"
+ "Asset update skipped: asset with identifier %@ not found in photo library"
+ "Asset with identifier %@ not found, assume already deleted"
+ "Invalidating remote alert handle: %p"
+ "Preparing remote alert handle: %p"
+ "Remote alert handle did activate, handle: %p"
+ "Remote alert handle did deactivate, handle: %p"
+ "Remote alert handle did invalidate with error %@, handle: %p"
+ "_cleanupCurrentHandleNotifyDelegate:"
+ "activate remote alert handle: %p"
+ "clean up remote alert handle: %p"
+ "dealloc - remote alert handle provider: %p, handle: %p"
+ "init - remote alert handle provider: %p, handle: %p"
+ "preheat remote alert handle: %p"
+ "registerObserver:"
+ "remove persistable calling completion block for unhandled delete options: %ld"
+ "ss_imageDataWithDataType:sdrImage:hdrImage:properties:imageDescription:"
+ "unregisterObserver:"
- "Invalidating remote alert handle"
- "Preparing remote alert handle"
- "Remote alert handle activated"
- "Remote alert handle deactivated"
- "Remote alert handle invalidated with error %@"
- "addObserver:"
- "ss_imageDataWithDataType:image:hdrImage:properties:imageDescription:"

```
