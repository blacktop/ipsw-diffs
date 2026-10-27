## PosterUIFoundation

> `/System/iOSSupport/System/Library/PrivateFrameworks/PosterUIFoundation.framework/Versions/A/PosterUIFoundation`

```diff

-355.0.0.0.0
-  __TEXT.__text: 0x932b4
-  __TEXT.__objc_methlist: 0xab04
-  __TEXT.__const: 0xdb4
-  __TEXT.__oslogstring: 0x3861
-  __TEXT.__cstring: 0x65a3
-  __TEXT.__gcc_except_tab: 0x163c
+355.2.12.100.0
+  __TEXT.__text: 0x95d34
+  __TEXT.__objc_methlist: 0xab9c
+  __TEXT.__const: 0xde4
+  __TEXT.__oslogstring: 0x4041
+  __TEXT.__cstring: 0x67c3
+  __TEXT.__gcc_except_tab: 0x1860
   __TEXT.__dlopen_cstrs: 0x1c0
   __TEXT.__swift5_typeref: 0x80a
   __TEXT.__constg_swiftt: 0x708

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x2870
+  __TEXT.__unwind_info: 0x28e0
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2710
-  __DATA_CONST.__objc_classlist: 0x4f0
+  __DATA_CONST.__const: 0x2790
+  __DATA_CONST.__objc_classlist: 0x508
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x58a0
+  __DATA_CONST.__objc_selrefs: 0x5938
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x410
-  __DATA_CONST.__objc_arraydata: 0x1980
-  __DATA_CONST.__got: 0xf48
-  __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x7f20
-  __AUTH_CONST.__objc_const: 0x1e998
-  __AUTH_CONST.__objc_dictobj: 0xd48
+  __DATA_CONST.__objc_arraydata: 0x19d0
+  __DATA_CONST.__got: 0xfa8
+  __AUTH_CONST.__const: 0x1100
+  __AUTH_CONST.__cfstring: 0x80e0
+  __AUTH_CONST.__objc_const: 0x1ec10
+  __AUTH_CONST.__objc_dictobj: 0xd70
   __AUTH_CONST.__objc_intobj: 0xe10
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1010
+  __AUTH_CONST.__auth_got: 0x1088
   __AUTH_CONST.__auth_ptr: 0x2e0
-  __AUTH.__objc_data: 0x2320
+  __AUTH.__objc_data: 0x2410
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0xbdc
-  __DATA.__data: 0x17a8
-  __DATA.__bss: 0x8b0
+  __DATA.__objc_ivar: 0xbe8
+  __DATA.__data: 0x17e0
+  __DATA.__bss: 0x8f0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xe10
   __DATA_DIRTY.__bss: 0xe0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4134
-  Symbols:   9676
-  CStrings:  1486
+  Functions: 4169
+  Symbols:   9766
+  CStrings:  1534
 
Symbols:
+ -[FBSMutableSceneSettings(PosterUIFoundation) pui_setRenderSessionTimeoutInterval:]
+ -[FBSSceneSettings(PosterUIFoundation) pui_renderSessionTimeoutInterval]
+ -[PUIPosterRenderingSceneSpecification allowsHostedSoftwareKeyboard]
+ -[PUIPosterSnapshotBundle _cacheImage:forLevelSet:decodedFromIdentifier:]
+ -[PUIPosterSnapshotBundle _pui_afscObserveCompressionIfNeeded]
+ -[PUIPosterSnapshotBundle dealloc]
+ -[PUIPosterSnapshotHostConfigurationDescriptor captureTimeoutInterval]
+ -[PUIPosterSnapshotHostConfigurationDescriptor copyWithCaptureTimeoutInterval:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor initWithHostWorkQueue:waitUntilReady:inProcessSnapshot:abortsIfBacklightNotFull:captureTimeoutInterval:]
+ GCC_except_table7
+ OBJC_IVAR_$_PUIPosterSnapshotBundle._afscCompressionObserver
+ OBJC_IVAR_$_PUIPosterSnapshotBundle._decodedImages
+ OBJC_IVAR_$_PUIPosterSnapshotHostConfigurationDescriptor._captureTimeoutInterval
+ PUIAFSCCompressFilesAtPaths
+ PUIAFSCEnqueueCompressionForURL
+ _NSURLContentTypeKey
+ _NSURLFileResourceIdentifierKey
+ _NSURLIsDirectoryKey
+ _NSURLIsRegularFileKey
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_PUIPosterEditingSceneSpecification
+ _OBJC_CLASS_$_PUIPosterRenderingSceneSpecification
+ _OBJC_CLASS_$_PUIPosterSceneSpecification
+ _OBJC_METACLASS_$_PUIPosterEditingSceneSpecification
+ _OBJC_METACLASS_$_PUIPosterRenderingSceneSpecification
+ _OBJC_METACLASS_$_PUIPosterSceneSpecification
+ _OBJC_METACLASS_$_UIApplicationSceneSpecification
+ _PUIAFSCCompressFilesAtPaths
+ _PUIAFSCCompressionBundleURLKey
+ _PUIAFSCCompressionFileNamesKey
+ _PUIAFSCDidCompressBundleNotificationForBundle
+ _PUIAFSCEnqueueCompressionForURL
+ _PUIPosterSceneSpecificationForSceneRole
+ _PUIPosterSnapshotDefaultCaptureTimeoutInterval
+ _UTTypeImage
+ __OBJC_$_INSTANCE_METHODS_PUIPosterRenderingSceneSpecification
+ __OBJC_CLASS_RO_$_PUIPosterEditingSceneSpecification
+ __OBJC_CLASS_RO_$_PUIPosterRenderingSceneSpecification
+ __OBJC_CLASS_RO_$_PUIPosterSceneSpecification
+ __OBJC_METACLASS_RO_$_PUIPosterEditingSceneSpecification
+ __OBJC_METACLASS_RO_$_PUIPosterRenderingSceneSpecification
+ __OBJC_METACLASS_RO_$_PUIPosterSceneSpecification
+ __PUIAFSCEnqueueCompressionForURL_block_invoke
+ ___62-[PUIPosterSnapshotBundle _pui_afscObserveCompressionIfNeeded]_block_invoke
+ ___PUIAFSCEnqueueCompressionForURL_block_invoke
+ ___PUIAFSCEnqueueCompressionForURL_block_invoke_2
+ ____pui_afscQueue_block_invoke
+ ____pui_afscWorkBegan_block_invoke
+ ___block_descriptor_40_e8_32s_e24_v16?0"NSNotification"8ls32l8
+ ___block_descriptor_40_e8_32s_e27_B24?0"NSURL"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e31_v16?0"PUISceneConfiguration"8ls32l8s40l8s48l8
+ ___getkAFSCIgnoreXattrErrorsSymbolLoc_block_invoke
+ ___pui_afscWorkBegan_block_invoke
+ __pui_afscCloneProtectionVerdict
+ __pui_afscLock
+ __pui_afscLock_assertion
+ __pui_afscLock_generation
+ __pui_afscLock_pendingCount
+ __pui_afscPathIsAlreadyCompressed
+ _clonefile
+ _close
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _fcntl
+ _listxattr
+ _malloc_type_malloc
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_msgSend$_cacheImage:forLevelSet:decodedFromIdentifier:
+ _objc_msgSend$_pui_afscObserveCompressionIfNeeded
+ _objc_msgSend$acquireWithInvalidationHandler:
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$bytes
+ _objc_msgSend$captureTimeoutInterval
+ _objc_msgSend$conformsToType:
+ _objc_msgSend$currentProcess
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$pf_prewarmRuntimeAssertionForReason:target:invalidationHandler:
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$pui_renderSessionTimeoutInterval
+ _objc_msgSend$pui_setRenderSessionTimeoutInterval:
+ _objc_msgSend$setBoostWhitePoint:
+ _objc_msgSend$setCountLimit:
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$stringWithFileSystemRepresentation:length:
+ _open
+ _pread
+ _pui_afscQueue.onceToken
+ _pui_afscQueue.queue
+ _renamex_np
+ _stat
+ _unlink
+ getkAFSCIgnoreXattrErrorsSymbolLoc.ptr
- -[PUIPosterSnapshotHostConfigurationDescriptor initWithHostWorkQueue:waitUntilReady:inProcessSnapshot:abortsIfBacklightNotFull:]
- GCC_except_table40
- PUIAFSCCompressFileAtPath
- ___block_descriptor_40_e8_32s_e31_v16?0"PUISceneConfiguration"8ls32l8
CStrings:
+ "%lu file(s)"
+ "%{public}@"
+ "(%p) waiting up to %.1fs for scene readiness"
+ "(could not compare)"
+ "AFSC CompressFile refused %{public}@; leaving it uncompressed"
+ "AFSC clone of %{public}@ did not keep the source's protection class; discarding it"
+ "AFSC clone of %{public}@ lost xattr %{public}@; discarding it"
+ "AFSC compressed %lu file(s) under %{public}@ in %.1fms"
+ "AFSC compressed %lu of %lu file(s) under %{public}@ in %.1fms: %{public}@"
+ "AFSC compressed %{public}@ (%lld -> %lld bytes, %.0f%% smaller) in %.1fms (inode %llu -> %llu)"
+ "AFSC compressing %lu file(s) under %{public}@"
+ "AFSC compressing poster snapshots"
+ "AFSC could not clone %{public}@ (%{darwin.errno}d); leaving it uncompressed"
+ "AFSC could not compare the protection class of %{public}@ (%{darwin.errno}d); discarding the compressed copy"
+ "AFSC could not determine whether %{public}@ is a directory: %{public}@"
+ "AFSC could not discard the clone of %{public}@ (%{darwin.errno}d); it stays on disk until the next sweep"
+ "AFSC could not identify %{public}@, so no holder will drop its cached decodes: %{public}@"
+ "AFSC could not stat %{public}@ (%{darwin.errno}d); skipping it"
+ "AFSC could not swap in %{public}@ (%{darwin.errno}d); discarding the compressed copy"
+ "AFSC enumeration error under %{public}@ at %{public}@: %{public}@"
+ "AFSC failed on %lu of %lu file(s); see the per-file errors above"
+ "AFSC left %{public}@ (%lld bytes) uncompressed after %.1fms"
+ "AFSC prewarm assertion invalidated or failed to acquire; remaining compression is unprotected: %{public}@"
+ "AFSC produced no usable compressed copy of %{public}@: %{public}@ (%{darwin.errno}d)"
+ "AFSC skipped %lu already-compressed file(s) under %{public}@; nothing to do"
+ "AFSC skipped %{public}@ (%lld bytes), already compressed"
+ "AFSC source %{public}@ was rewritten during compression (inode %llu -> %llu); discarding the compressed copy"
+ "AFSC source %{public}@ went away during compression (%{darwin.errno}d); discarding the compressed copy"
+ "AFSC swapped in %{public}@ but could not read its new inode"
+ "AFSC swapped in %{public}@ but could not remove the old copy (%{darwin.errno}d)"
+ "AFSC swept a stale clone at %{public}@"
+ "AFSC work ended without a matching begin"
+ "B24@?0@\"NSURL\"8@\"NSError\"16"
+ "No path was on an AFSC-capable volume"
+ "PUIAFSCCompressFile"
+ "PUIAFSCCompressFilesAtPaths"
+ "PUIAFSCCompressionBundleURL"
+ "PUIAFSCCompressionFileNames"
+ "PUIAFSCDidCompressBundle-%@"
+ "Unable to interpret path"
+ "_captureTimeoutInterval"
+ "afsctmp"
+ "already compressed"
+ "captureTimeoutInterval"
+ "com.apple.posteruifoundation.afsc-compression"
+ "compressed %lu, declined %lu, already %lu, failed %lu"
+ "compressed=%d"
+ "iPhone19,7"
+ "kAFSCIgnoreXattrErrors"
+ "stat failed"
+ "the clone is not the size the source was"
+ "the clone reports the right size but its last byte will not decode"
+ "the clone vanished"
+ "the clone would not open"
+ "v16@?0@\"NSNotification\"8"
- "AFSC CompressFile rejected the path"
- "AFSC compression failed for %{public}@ (uncompressed file left in place): %{public}@"
- "CompressFile rejected"
- "PUIAFSCCompressFileAtPath"
- "Volume does not support AFSC"
- "success"
- "unsupported"
```
