## PosterUIFoundation

> `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`

```diff

-355.3.7.0.0
-  __TEXT.__text: 0x96008
-  __TEXT.__objc_methlist: 0xafe4
-  __TEXT.__const: 0xe34
-  __TEXT.__cstring: 0x6b53
-  __TEXT.__oslogstring: 0x4141
-  __TEXT.__gcc_except_tab: 0x1920
+355.3.12.0.0
+  __TEXT.__text: 0x97a08
+  __TEXT.__objc_methlist: 0xb0a4
+  __TEXT.__const: 0xe44
+  __TEXT.__cstring: 0x6be3
+  __TEXT.__oslogstring: 0x4491
+  __TEXT.__gcc_except_tab: 0x1964
   __TEXT.__dlopen_cstrs: 0x272
   __TEXT.__swift5_typeref: 0x80a
   __TEXT.__constg_swiftt: 0x708

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x3568
+  __TEXT.__unwind_info: 0x35d0
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2888
-  __DATA_CONST.__objc_classlist: 0x550
+  __DATA_CONST.__const: 0x28d0
+  __DATA_CONST.__objc_classlist: 0x558
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5be0
+  __DATA_CONST.__objc_selrefs: 0x5c38
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x428
+  __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0x1a60
-  __DATA_CONST.__got: 0x1090
+  __DATA_CONST.__got: 0x1098
   __AUTH_CONST.__const: 0x1140
-  __AUTH_CONST.__cfstring: 0x8400
-  __AUTH_CONST.__objc_const: 0x201f0
+  __AUTH_CONST.__cfstring: 0x84a0
+  __AUTH_CONST.__objc_const: 0x203d8
   __AUTH_CONST.__objc_dictobj: 0xde8
   __AUTH_CONST.__objc_intobj: 0xe70
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1138
-  __AUTH.__objc_data: 0x2730
+  __AUTH_CONST.__auth_got: 0x1148
+  __AUTH.__objc_data: 0x2780
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0xc18
+  __DATA.__objc_ivar: 0xc2c
   __DATA.__data: 0x18b0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xdc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4262
-  Symbols:   7667
-  CStrings:  1566
+  Functions: 4294
+  Symbols:   7719
+  CStrings:  1584
 
Symbols:
+ -[FBSMutableSceneClientSettings(PosterUIFoundation) pui_setArbitrationBlockingReasons:]
+ -[FBSSceneClientSettings(PosterUIFoundation) pui_arbitrationBlockingReasons]
+ -[FBSSceneClientSettingsDiff(PosterUIFoundation) pui_arbitrationBlockingReasonsDidChange]
+ -[PUIPosterSceneSnapshotter scene:clientDidConnect:]
+ -[_PUIAFSCBundleRun .cxx_destruct]
+ -[_PUIAFSCBundleRun completions]
+ -[_PUIAFSCBundleRun initWithURL:key:]
+ -[_PUIAFSCBundleRun key]
+ -[_PUIAFSCBundleRun setStartQoS:]
+ -[_PUIAFSCBundleRun setWaiterQoS:]
+ -[_PUIAFSCBundleRun startQoS]
+ -[_PUIAFSCBundleRun url]
+ -[_PUIAFSCBundleRun waiterQoS]
+ GCC_except_table15
+ GCC_except_table45
+ _NSStringFromPUIPosterArbitrationBlockingReason
+ _OBJC_CLASS_$__PUIAFSCBundleRun
+ _OBJC_IVAR_$__PUIAFSCBundleRun._completions
+ _OBJC_IVAR_$__PUIAFSCBundleRun._key
+ _OBJC_IVAR_$__PUIAFSCBundleRun._startQoS
+ _OBJC_IVAR_$__PUIAFSCBundleRun._url
+ _OBJC_IVAR_$__PUIAFSCBundleRun._waiterQoS
+ _OBJC_METACLASS_$__PUIAFSCBundleRun
+ _PUIAFSCCompressBundleAtURL
+ _PUIAFSCCompressBundleAtURLWithQoS
+ _PUIAFSCMaximumBundleCompressionQoS
+ _PUIAFSCMaximumConcurrentBundleCompressions
+ _PUIAFSCPendingWorkCountForTesting
+ _PUIAFSCPrefaultFileIfCompressed
+ _PUIAFSCRaiseBundleCompressionQoS
+ _PUIAFSCSetBundleCompressorForTesting
+ _PUIAFSCSetVolumeSupportCheckForTesting
+ __OBJC_$_INSTANCE_METHODS__PUIAFSCBundleRun
+ __OBJC_$_INSTANCE_VARIABLES__PUIAFSCBundleRun
+ __OBJC_$_PROP_LIST__PUIAFSCBundleRun
+ __OBJC_CLASS_RO_$__PUIAFSCBundleRun
+ __OBJC_METACLASS_RO_$__PUIAFSCBundleRun
+ ___PUIAFSCCompressBundleAtURLWithQoS_block_invoke
+ ____pui_afscCallBackWithoutRunning_block_invoke
+ ____pui_afscCompressBundleNow_block_invoke
+ ____pui_afscFinishRun_block_invoke
+ ____pui_afscStartRuns_block_invoke
+ ___block_descriptor_32_e20_v24?0Q8"NSError"16l
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls40l8s32l8
+ __pui_afscBundleError
+ __pui_afscCallBackWithoutRunning
+ __pui_afscCompressFilesAtPaths
+ __pui_afscDispatchAtQoS
+ __pui_afscPOSIXError
+ __pui_afscReadBackImagesAtPaths
+ __pui_afscRunsLock
+ __pui_afscRunsLock_compressorForTesting
+ __pui_afscRunsLock_runningCount
+ __pui_afscRunsLock_runsByKey
+ __pui_afscRunsLock_takeStartableRuns
+ __pui_afscRunsLock_volumeSupportCheckForTesting
+ __pui_afscRunsLock_waitingRuns
+ __pui_afscStartRuns
+ _dispatch_block_create_with_qos_class
+ _os_unfair_recursive_lock_lock
+ _qos_class_self
+ _read
- GCC_except_table20
- GCC_except_table7
- _PUIAFSCEnqueueCompressionForURL
- ___PUIAFSCEnqueueCompressionForURL_block_invoke
- ___PUIAFSCEnqueueCompressionForURL_block_invoke_2
- ____pui_afscQueue_block_invoke
- __pui_afscQueue.onceToken
- __pui_afscQueue.queue
- _dispatch_queue_attr_make_with_qos_class
- _os_unfair_recursive_lock_lock_with_options
CStrings:
+ "%lu file(s), throttled=%d"
+ "(%{public}@) Deferring capture, client not connected"
+ "(%{public}@) clientDidConnect:'%@'"
+ "AFSC compressing %lu file(s) under %{public}@ (throttled IO: %{BOOL}d)"
+ "AFSC could not open compressed %{public}@ to prefault it (%{darwin.errno}d)"
+ "AFSC could not prefault %{public}@ after %lld bytes (%{darwin.errno}d)"
+ "AFSC could not read back %lu of %lu file(s)"
+ "AFSC could not read back %lu of %lu file(s) under %{public}@: %{public}@"
+ "AFSC could not read the bundle"
+ "AFSC could not stat %{public}@ to prefault it (%{darwin.errno}d)"
+ "AFSC finished a run without a running slot"
+ "AFSC is not supported on the volume of %{public}@; leaving it uncompressed"
+ "AFSC joined the compression already queued or running for %{public}@"
+ "AFSC prefaulted compressed %{public}@ (%lld bytes) in %.1fms"
+ "AFSC queued %{public}@ at QoS %#x with %lu running and %lu waiting"
+ "AFSC raised the waiting compression of %{public}@ to QoS %#x"
+ "AFSC skipped %lu already-compressed file(s) under %{public}@ and read them back in"
+ "AFSC was asked to compress a bundle without a path"
+ "AppleFSCompression didn't load; leaving %{public}@ uncompressed"
+ "extendedRenderSession"
+ "v24@?0Q8@\"NSError\"16"
+ "wakeRampInProgress"
- "%lu file(s)"
- "AFSC compressing %lu file(s) under %{public}@"
- "AFSC skipped %lu already-compressed file(s) under %{public}@; nothing to do"
- "com.apple.posteruifoundation.afsc-compression"
```
