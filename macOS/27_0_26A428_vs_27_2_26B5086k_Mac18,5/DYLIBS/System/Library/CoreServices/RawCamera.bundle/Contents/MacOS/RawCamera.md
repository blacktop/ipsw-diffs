## RawCamera

> `/System/Library/CoreServices/RawCamera.bundle/Contents/MacOS/RawCamera`

```diff

-1821.21.1.0.0
-  __TEXT.__text: 0x231e04
-  __TEXT.__objc_methlist: 0x2424
-  __TEXT.__const: 0x186d4
-  __TEXT.__gcc_except_tab: 0x31b00
-  __TEXT.__oslogstring: 0x2880
-  __TEXT.__cstring: 0x12421
+1821.40.4.0.0
+  __TEXT.__text: 0x238ae4
+  __TEXT.__objc_methlist: 0x25ac
+  __TEXT.__const: 0x186e4
+  __TEXT.__gcc_except_tab: 0x325b0
+  __TEXT.__oslogstring: 0x2d42
+  __TEXT.__cstring: 0x128e1
   __TEXT.__ustring: 0x4b6
   __TEXT.__constg_swiftt: 0xa14
   __TEXT.__swift5_typeref: 0x5bf

   __TEXT.__swift5_types: 0xd8
   __TEXT.__swift5_capture: 0x4c
   __TEXT.__dof_RawCamera: 0x8f7
-  __TEXT.__unwind_info: 0xcfe0
+  __TEXT.__unwind_info: 0xd278
   __TEXT.__eh_frame: 0x11e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2300
-  __DATA_CONST.__objc_classlist: 0x240
+  __DATA_CONST.__const: 0x23a0
+  __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x16e8
-  __DATA_CONST.__objc_superrefs: 0x130
-  __DATA_CONST.__objc_arraydata: 0x3b50
-  __DATA_CONST.__got: 0xad8
-  __AUTH_CONST.__const: 0x3d0b0
-  __AUTH_CONST.__cfstring: 0x1ae40
-  __AUTH_CONST.__objc_const: 0x6de8
+  __DATA_CONST.__objc_selrefs: 0x1830
+  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_arraydata: 0x3b60
+  __DATA_CONST.__got: 0xae8
+  __AUTH_CONST.__const: 0x3d300
+  __AUTH_CONST.__cfstring: 0x1b0a0
+  __AUTH_CONST.__objc_const: 0x7058
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x5e8
   __AUTH_CONST.__objc_intobj: 0x3b58

   __AUTH_CONST.__objc_dictobj: 0x4d58
   __AUTH_CONST.__objc_floatobj: 0xd0
   __AUTH_CONST.__auth_got: 0x10f0
-  __AUTH.__objc_data: 0x1270
+  __AUTH.__objc_data: 0x13b0
   __AUTH.__data: 0x7a8
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x18
-  __DATA.__objc_ivar: 0x5e8
-  __DATA.__data: 0x20e68
+  __DATA.__objc_ivar: 0x614
+  __DATA.__data: 0x20e70
   __DATA.__common: 0x4
-  __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x248
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7794
-  Symbols:   930
-  CStrings:  4227
+  Functions: 7899
+  Symbols:   932
+  CStrings:  4293
 
Symbols:
+ _OBJC_CLASS_$_NSProgress
+ _RCModelDownloadStart
CStrings:
+ " (no model directory was resolved)"
+ "%@_v%d"
+ "%ld_v%d"
+ "%{public}s   raw MADownloadResult = %ld (%s)"
+ "%{public}s Failed to download V9 model asset for CFA class %ld (Err: %d)"
+ "%{public}s Failed to download model MobileAsset catalog (Err: %d)"
+ "%{public}s Failed to load the V9 ML demosaic model%s after waiting up to %.0fs for the Mobile Asset download; requesting decoder version 9 without it available."
+ "%{public}s Model MobileAsset catalog download successful"
+ "%{public}s Model MobileAsset catalog loaded after download."
+ "%{public}s Model MobileAsset catalog was updated."
+ "%{public}s Model MobileAsset query unsuccessful"
+ "%{public}s Prefetching V9 model asset for CFA class %ld"
+ "%{public}s RCMAAssetAttachProgress: MobileAsset not available or nil asset"
+ "%{public}s RCMAAssetQueryMetaDataSync: Result = %d (%s), raw MAQueryResult = %ld (%s)"
+ "%{public}s V9 model asset download successful for CFA class %ld"
+ "%{public}s V9 model for %@ not present on disk — %s, waiting up to %.0fs."
+ "%{public}s V9 model for %@: asset download failed — using fallback."
+ "%{public}s V9 model for %@: download complete — model now available."
+ "%{public}s V9 model for %@: download did not complete within %.0fs — using fallback."
+ "%{public}s V9 model for %@: using BUILT-IN bundled model"
+ "%{public}s V9 model for %@: using MOBILE ASSET model (%@)"
+ "%{public}s prefetchModelForClass for CFA class %ld"
+ "+[RAWDemosaicProcessorV9 getModelForCFAPattern:useQuarterRes:useAltModel:useMPSGraph:modelDirectory:]"
+ "-[CRawModelAssetManager ensureModelDownloadedForClass:timeout:]"
+ "-[CRawModelAssetManager installedModelDirectoryForClass:]"
+ "-[CRawModelAssetManager prefetchModelForClass:]"
+ "-[CRawModelAssetManager prefetchModelForClass:]_block_invoke"
+ "/%@.mil"
+ "/%@_model.mil"
+ "Bayer"
+ "GetModelAssetCatalog_block_invoke"
+ "GetModelAssetCatalog_block_invoke_2"
+ "MADownloadTimedOutBecameStalled"
+ "MADownloadTimedOutFrequentStalls"
+ "MADownloadTimedOutNoContent"
+ "MADownloadTimedOutSlowDownload"
+ "MAQueryBeforeFirstUnlock"
+ "MAQueryCannotCreateMessage"
+ "MAQueryCatalogNotDownloaded"
+ "MAQueryDaemonExit"
+ "MAQueryFailed"
+ "MAQueryNilAssetType"
+ "MAQueryNotEntitled"
+ "MAQueryParamsEncodeFailure"
+ "MAQuerySuccessful"
+ "MAQueryXpcError"
+ "ModelDirectory"
+ "ModelGroup"
+ "Quadra"
+ "RCMAAssetAttachProgress"
+ "RawCamera_ModelAsset_Prefetch_Queue"
+ "RawCamera_ModelCatalog_Access_Queue"
+ "XTrans"
+ "_ContentVersion"
+ "_model"
+ "_quarter_res_model"
+ "already downloading"
+ "bayer"
+ "com.apple.MobileAsset.RawCamera.MLModels"
+ "com.apple.MobileAsset.RawCamera.MLModels.ma.cached-metadata-updated"
+ "downloading now"
+ "inputModelDirectory"
+ "inputModelDownloadTimeout"
+ "quadra"
+ "see MADownloadResult in MAClientComms.h"
+ "unknown"
+ "v16@?0@\"MAProgressNotification\"8"
+ "v36@?0q8q16B24d28"
+ "xtrans"
- "%{public}s Failed to load the model."
- "%{public}s RCMAAssetQueryMetaDataSync: Result = %d (%s)"
- "+[RAWDemosaicProcessorV9 getModelForCFAPattern:useQuarterRes:useAltModel:useMPSGraph:]"
```
