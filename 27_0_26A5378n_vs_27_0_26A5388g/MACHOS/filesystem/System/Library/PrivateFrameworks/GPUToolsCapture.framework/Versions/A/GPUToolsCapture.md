## GPUToolsCapture

> `/System/Library/PrivateFrameworks/GPUToolsCapture.framework/Versions/A/GPUToolsCapture`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__AUTH_CONST.__interpose`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`
- `__DATA.__thread_bss`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-2027.0.33.0.0
-  __TEXT.__text: 0x2b303c
+2027.0.35.0.0
+  __TEXT.__text: 0x2b3620
   __TEXT.__auth_stubs: 0x17f0
   __TEXT.__objc_stubs: 0x19980
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1466c
-  __TEXT.__const: 0x9ff0
-  __TEXT.__cstring: 0x30f5d
+  __TEXT.__const: 0xa000
+  __TEXT.__cstring: 0x30f9b
   __TEXT.__oslogstring: 0x2418
   __TEXT.__gcc_except_tab: 0x377c
   __TEXT.__objc_methname: 0x1df33

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10122
-  Symbols:   17064
-  CStrings:  9702
+  Functions: 10124
+  Symbols:   17066
+  CStrings:  9703
 
Symbols:
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/DerivedSources/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/Objects-normal/arm64e/GPUToolsCapture_lto.o
+ _DYTraceDecode_MTLDevice_newSharedEventWithOptions
+ _DYTraceEncode_MTLDevice_newSharedEventWithOptions
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/DerivedSources/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/Objects-normal/arm64e/GPUToolsCapture_lto.o
Functions:
~ -[CaptureMTLDevice newSharedEventWithOptions:] : 132 -> 324
~ _ResourceTracker_addLibraries : 2480 -> 2492
~ _GTSMMTLSharedEvent_processTraceFuncWithMap : 440 -> 516
~ _GTSMMTLSharedEvent_processTraceFuncWithPool : 440 -> 516
~ _GTTraceFuncToFbuf : 232844 -> 233012
+ _DYTraceEncode_MTLDevice_newSharedEventWithOptions
~ _GTFenum_getConstructorType : 3072 -> 3088
~ _MakeDYMTLAccelerationStructureMotionTriangleGeometryDescriptor : 448 -> 456
~ _MakeDYMTLTensorAuxiliaryPlaneDescriptorMap : 140 -> 168
~ _DecodeDYMTLRasterizationRateMapDescriptor : 368 -> 392
~ _MakeDYMTLAccelerationStructureMotionBoundingBoxGeometryDescriptor : 176 -> 192
~ _MakeDYMTLAccelerationStructureMotionCurveGeometryDescriptor : 492 -> 508
~ _DecodeDYMTLTensorBufferAttachments : 164 -> 188
~ _MakeDYMTL4PrimitiveAccelerationStructureDescriptor : 228 -> 260
~ _MakeDYMTL4StaticLinkingDescriptor : 560 -> 576
~ _MakeDYMTLPrimitiveAccelerationStructureDescriptor : 300 -> 340
+ _DYTraceDecode_MTLDevice_newSharedEventWithOptions
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_hash.c:95"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_proc.c:33"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_proc_mutex.c:1155"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_random.c:135"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_random.c:136"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_tables.c:189"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_tables.c:271"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_tables.c:70"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_thread_mutex.c:50"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/capture/mtl/CaptureMTLTextureViewPool.m:53"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/core/GTCoreErrors.m:327"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/core/GTCoreErrors.m:339"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/core/GTCoreMetal.m:456"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/download/GTAccelerationStructureDescriptorDownloader.m:99"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/download/GTAccelerationStructureDescriptorDownloader_MTL4.m:57"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/download/memwatch/GTChunkTable.c:134"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/download/memwatch/GTChunkTable.c:142"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/dump/GTTraceDispatch.c:1175"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/dump/GTTraceDump.c:53"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:278"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:349"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:408"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:685"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTMTLCaptureManager_prepareForSerialization.m:564"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTMTLCaptureState.m:28"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/fbstream.m:37"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/sm/GTSMMTLBuilder.c:2613"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trace/GTTraceContext.c:162"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trace/GTTraceStoreDebug.c:143"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trace/GTTraceStoreDebug.c:166"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTCaptureBoundaryTracker.c:156"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTEventTracker.c:289"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTEventTracker.c:313"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTResourceHarvest.c:52"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTResourceTracker.c:232"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTResourceTracker_abs.c:570"
+ "Shared events created with certain options cannot be captured"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_hash.c:95"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_proc.c:33"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_proc_mutex.c:1155"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_random.c:135"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_random.c:136"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_tables.c:189"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_tables.c:271"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_tables.c:70"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_thread_mutex.c:50"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/capture/mtl/CaptureMTLTextureViewPool.m:53"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/core/GTCoreErrors.m:327"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/core/GTCoreErrors.m:339"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/core/GTCoreMetal.m:456"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/download/GTAccelerationStructureDescriptorDownloader.m:99"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/download/GTAccelerationStructureDescriptorDownloader_MTL4.m:57"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/download/memwatch/GTChunkTable.c:134"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/download/memwatch/GTChunkTable.c:142"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/dump/GTTraceDispatch.c:1175"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/dump/GTTraceDump.c:53"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:278"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:349"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:408"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:685"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTMTLCaptureManager_prepareForSerialization.m:564"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTMTLCaptureState.m:28"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/fbstream.m:37"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/sm/GTSMMTLBuilder.c:2612"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trace/GTTraceContext.c:162"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trace/GTTraceStoreDebug.c:143"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trace/GTTraceStoreDebug.c:166"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTCaptureBoundaryTracker.c:156"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTEventTracker.c:289"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTEventTracker.c:313"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTResourceHarvest.c:52"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTResourceTracker.c:232"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trackers/GTResourceTracker_abs.c:570"
```
