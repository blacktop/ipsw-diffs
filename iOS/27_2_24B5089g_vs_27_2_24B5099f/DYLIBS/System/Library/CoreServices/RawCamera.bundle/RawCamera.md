## RawCamera

> `/System/Library/CoreServices/RawCamera.bundle/RawCamera`

```diff

-1821.40.4.0.0
-  __TEXT.__text: 0x22ba80
-  __TEXT.__objc_methlist: 0x25ac
-  __TEXT.__const: 0x18644
-  __TEXT.__gcc_except_tab: 0x324b4
-  __TEXT.__oslogstring: 0x2d42
-  __TEXT.__cstring: 0x128f1
+1821.40.6.0.0
+  __TEXT.__text: 0x22ecd0
+  __TEXT.__objc_methlist: 0x25dc
+  __TEXT.__const: 0x187e4
+  __TEXT.__gcc_except_tab: 0x32a3c
+  __TEXT.__oslogstring: 0x2f9d
+  __TEXT.__cstring: 0x12b11
   __TEXT.__ustring: 0x4b6
   __TEXT.__constg_swiftt: 0xa14
   __TEXT.__swift5_typeref: 0x5bf

   __TEXT.__swift5_types: 0xd8
   __TEXT.__swift5_capture: 0x4c
   __TEXT.__dof_RawCamera: 0x8f7
-  __TEXT.__unwind_info: 0xd210
-  __TEXT.__eh_frame: 0x13b8
+  __TEXT.__unwind_info: 0xd318
+  __TEXT.__eh_frame: 0x13e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2e38
+  __DATA_CONST.__const: 0x2f08
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1830
+  __DATA_CONST.__objc_selrefs: 0x1858
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x3b60
-  __DATA_CONST.__got: 0xae8
-  __AUTH_CONST.__const: 0x3c648
-  __AUTH_CONST.__cfstring: 0x1b0c0
+  __DATA_CONST.__got: 0xaf0
+  __AUTH_CONST.__const: 0x3c8a8
+  __AUTH_CONST.__cfstring: 0x1b140
   __AUTH_CONST.__objc_const: 0x7058
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x5e8

   __AUTH_CONST.__objc_doubleobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x4d58
   __AUTH_CONST.__objc_floatobj: 0xd0
-  __AUTH_CONST.__auth_got: 0x12a8
-  __AUTH.__objc_data: 0x1310
-  __AUTH.__data: 0x7a8
+  __AUTH_CONST.__auth_got: 0x12b0
+  __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x18
   __DATA.__objc_ivar: 0x614
-  __DATA.__data: 0x20e68
+  __DATA.__data: 0x206a0
   __DATA.__common: 0x4
-  __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__objc_data: 0x13b0
+  __DATA_DIRTY.__data: 0xf78
   __DATA_DIRTY.__bss: 0x248
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7853
-  Symbols:   987
-  CStrings:  4294
+  Functions: 7890
+  Symbols:   988
+  CStrings:  4314
 
Symbols:
+ _dispatch_after
CStrings:
+ "%{public}s All V9 model assets: %s."
+ "%{public}s Downloading ALL V9 model assets (%lu CFA families x %lu decoder versions)."
+ "%{public}s Exception in tile processing for tile %u: %s"
+ "%{public}s Model MobileAsset catalog fetch never reported back — no longer waiting on it."
+ "%{public}s RCMAAssetStartDownload: Download completed with result %d (%s), raw %ld (%s)"
+ "%{public}s Unknown exception in tile processing for tile %u"
+ "%{public}s V9 model for %@: a download has been in flight for %llds without installing — giving up on it. It may be a stalled task from an earlier run; `asutil --malist-tasks` / `--maclean-tasks` clears those."
+ "%{public}s V9 model for %@: a download is already in flight; watching it instead of starting a second one."
+ "%{public}s V9 model for %@: the in-flight download ended without installing (state=%d)."
+ "-[CRawModelAssetManager startAssetDownloadForClass:version:inCatalog:]_block_invoke"
+ "-[CRawModelAssetManager startDownloadForAllModelsWithCompletion:]"
+ "-[CRawModelAssetManager startDownloadForAllModelsWithCompletion:]_block_invoke"
+ "-[CRawModelAssetManager watchInFlightDownloadForClass:version:asset:deadline:]_block_invoke"
+ "@\"CIImage\"64@?0@\"CIImage\"8d16d24d32d40Q48Q56"
+ "DNGLosslessJpegUnpacker: AppleJPEG failed to decode tile"
+ "MADownloadAssetAlreadyInstalled"
+ "MADownloadSuccessful"
+ "RAWRecoverHighlightsV3"
+ "_DownloadSize"
+ "com.apple.MobileAsset.RawCamera.MLModel"
+ "com.apple.MobileAsset.RawCamera.MLModel.ma.cached-metadata-updated"
+ "every model is present"
+ "one or more did NOT download"
+ "srSCCDBoxH"
+ "srSCCDBoxV"
+ "srSCCDCombine"
+ "srSCCDDefringe"
+ "srSCCDDiff"
+ "srSCCDGreen"
+ "v12@?0B8"
+ "v16@?0@\"NSArray\"8"
- "%{public}s Exception in tile coordinate calculation for tile %u: %s"
- "%{public}s Exception in tile processing: %s"
- "%{public}s Exception in unpackSensorData: %s"
- "%{public}s RCMAAssetStartDownload: Download completed with result %d (%s)"
- "%{public}s Unknown exception in tile processing"
- "RAWRecoverHighlightsV2"
- "com.apple.MobileAsset.RawCamera.MLModels"
- "com.apple.MobileAsset.RawCamera.MLModels.ma.cached-metadata-updated"
- "deSuperCCDSR_v8"
- "deXtrans_draft"
- "deXtrans_v7_8bit"
```
