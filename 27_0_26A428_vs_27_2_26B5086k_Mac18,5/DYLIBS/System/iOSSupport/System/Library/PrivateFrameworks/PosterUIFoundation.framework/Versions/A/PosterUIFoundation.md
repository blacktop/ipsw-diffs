## PosterUIFoundation

> `/System/iOSSupport/System/Library/PrivateFrameworks/PosterUIFoundation.framework/Versions/A/PosterUIFoundation`

```diff

-355.0.0.0.0
-  __TEXT.__text: 0x8f688
-  __TEXT.__objc_methlist: 0xab04
-  __TEXT.__const: 0xdb4
-  __TEXT.__oslogstring: 0x3861
-  __TEXT.__cstring: 0x65a3
-  __TEXT.__gcc_except_tab: 0x163c
+355.2.4.0.0
+  __TEXT.__text: 0x90624
+  __TEXT.__objc_methlist: 0xab64
+  __TEXT.__const: 0xdc4
+  __TEXT.__oslogstring: 0x39e1
+  __TEXT.__cstring: 0x6683
+  __TEXT.__gcc_except_tab: 0x1784
   __TEXT.__dlopen_cstrs: 0x1c0
   __TEXT.__swift5_typeref: 0x80a
   __TEXT.__constg_swiftt: 0x708

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x32a0
+  __TEXT.__unwind_info: 0x32e0
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2710
+  __DATA_CONST.__const: 0x2738
   __DATA_CONST.__objc_classlist: 0x4f0
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x58a0
+  __DATA_CONST.__objc_selrefs: 0x58f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x410
-  __DATA_CONST.__objc_arraydata: 0x1980
-  __DATA_CONST.__got: 0xf48
-  __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x7f20
-  __AUTH_CONST.__objc_const: 0x1e998
-  __AUTH_CONST.__objc_dictobj: 0xd48
+  __DATA_CONST.__objc_arraydata: 0x19d0
+  __DATA_CONST.__got: 0xf68
+  __AUTH_CONST.__const: 0x1100
+  __AUTH_CONST.__cfstring: 0x7fc0
+  __AUTH_CONST.__objc_const: 0x1ea20
+  __AUTH_CONST.__objc_dictobj: 0xd70
   __AUTH_CONST.__objc_intobj: 0xe10
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1010
+  __AUTH_CONST.__auth_got: 0x1038
   __AUTH.__objc_data: 0x2320
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0xbdc
+  __DATA.__objc_ivar: 0xbe0
   __DATA.__data: 0x17a8
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xe10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4134
-  Symbols:   9676
-  CStrings:  1486
+  Functions: 4150
+  Symbols:   9718
+  CStrings:  1501
 
Symbols:
+ -[FBSMutableSceneSettings(PosterUIFoundation) pui_setRenderSessionTimeoutInterval:]
+ -[FBSSceneSettings(PosterUIFoundation) pui_renderSessionTimeoutInterval]
+ -[PUIPosterSnapshotHostConfigurationDescriptor captureTimeoutInterval]
+ -[PUIPosterSnapshotHostConfigurationDescriptor copyWithCaptureTimeoutInterval:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor initWithHostWorkQueue:waitUntilReady:inProcessSnapshot:abortsIfBacklightNotFull:captureTimeoutInterval:]
+ OBJC_IVAR_$_PUIPosterSnapshotHostConfigurationDescriptor._captureTimeoutInterval
+ PUIAFSCCompressFilesAtPaths
+ PUIAFSCEnqueueCompressionForURL
+ _NSURLContentTypeKey
+ _NSURLIsDirectoryKey
+ _NSURLIsRegularFileKey
+ _PUIAFSCCompressFilesAtPaths
+ _PUIAFSCEnqueueCompressionForURL
+ _PUIPosterSnapshotDefaultCaptureTimeoutInterval
+ _UTTypeImage
+ __PUIAFSCEnqueueCompressionForURL_block_invoke
+ ___PUIAFSCEnqueueCompressionForURL_block_invoke
+ ___PUIAFSCEnqueueCompressionForURL_block_invoke_2
+ ____pui_afscQueue_block_invoke
+ ____pui_afscWorkBegan_block_invoke
+ ___block_descriptor_40_e8_32s_e27_B24?0"NSURL"8"NSError"16ls32l8
+ ___getkAFSCIgnoreXattrErrorsSymbolLoc_block_invoke
+ ___pui_afscWorkBegan_block_invoke
+ __pui_afscLock
+ __pui_afscLock_assertion
+ __pui_afscLock_generation
+ __pui_afscLock_pendingCount
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_msgSend$acquireWithInvalidationHandler:
+ _objc_msgSend$captureTimeoutInterval
+ _objc_msgSend$conformsToType:
+ _objc_msgSend$currentProcess
+ _objc_msgSend$pf_prewarmRuntimeAssertionForReason:target:invalidationHandler:
+ _objc_msgSend$pui_renderSessionTimeoutInterval
+ _objc_msgSend$pui_setRenderSessionTimeoutInterval:
+ _objc_msgSend$setBoostWhitePoint:
+ _objc_msgSend$stringWithFileSystemRepresentation:length:
+ _pui_afscQueue.onceToken
+ _pui_afscQueue.queue
+ getkAFSCIgnoreXattrErrorsSymbolLoc.ptr
- -[PUIPosterSnapshotHostConfigurationDescriptor initWithHostWorkQueue:waitUntilReady:inProcessSnapshot:abortsIfBacklightNotFull:]
- PUIAFSCCompressFileAtPath
CStrings:
+ "%lu file(s)"
+ "%{public}@"
+ "(%p) waiting up to %.1fs for scene readiness"
+ "AFSC CompressFile rejected every path"
+ "AFSC compressed %lu of %lu file(s) under %{public}@ (remainder left uncompressed): %{public}@"
+ "AFSC compressing poster snapshots"
+ "AFSC could not determine whether %{public}@ is a directory: %{public}@"
+ "AFSC enumeration error under %{public}@ at %{public}@: %{public}@"
+ "AFSC prewarm assertion invalidated or failed to acquire; remaining compression is unprotected: %{public}@"
+ "AFSC work ended without a matching begin"
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "No path was on an AFSC-capable volume"
+ "PUIAFSCCompressFile"
+ "PUIAFSCCompressFilesAtPaths"
+ "Unable to interpret path"
+ "_captureTimeoutInterval"
+ "captureTimeoutInterval"
+ "com.apple.posteruifoundation.afsc-compression"
+ "compressed %lu of %lu"
+ "compressed=%d"
+ "iPhone19,7"
+ "kAFSCIgnoreXattrErrors"
- "AFSC CompressFile rejected the path"
- "AFSC compression failed for %{public}@ (uncompressed file left in place): %{public}@"
- "CompressFile rejected"
- "PUIAFSCCompressFileAtPath"
- "Volume does not support AFSC"
- "success"
- "unsupported"
```
