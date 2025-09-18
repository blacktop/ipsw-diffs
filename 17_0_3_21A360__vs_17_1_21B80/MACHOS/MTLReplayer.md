## MTLReplayer

> `/Applications/MTLReplayer.app/MTLReplayer`

```diff

-230.45.0.0.0
-  __TEXT.__text: 0x2a06e0
-  __TEXT.__auth_stubs: 0x2980
-  __TEXT.__objc_stubs: 0xbaa0
-  __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x57b8
-  __TEXT.__const: 0x1eec
-  __TEXT.__cstring: 0xb275a
-  __TEXT.__objc_methname: 0x11289
+240.6.0.0.0
+  __TEXT.__text: 0x29f4f4
+  __TEXT.__auth_stubs: 0x29a0
+  __TEXT.__objc_stubs: 0xbb40
+  __TEXT.__init_offsets: 0x8
+  __TEXT.__objc_methlist: 0x57d8
+  __TEXT.__const: 0x1efc
+  __TEXT.__cstring: 0xb2a34
+  __TEXT.__objc_methname: 0x11391
   __TEXT.__oslogstring: 0x1095
-  __TEXT.__objc_classname: 0xe63
-  __TEXT.__objc_methtype: 0xb815
-  __TEXT.__gcc_except_tab: 0x196a8
+  __TEXT.__objc_classname: 0xe64
+  __TEXT.__objc_methtype: 0xb85c
+  __TEXT.__gcc_except_tab: 0x1970c
   __TEXT.__ustring: 0x2aa
-  __TEXT.__unwind_info: 0x4790
+  __TEXT.__unwind_info: 0x47d0
   __TEXT.__eh_frame: 0x70
-  __DATA_CONST.__auth_got: 0x14d8
-  __DATA_CONST.__got: 0x228
+  __DATA_CONST.__auth_got: 0x14e8
+  __DATA_CONST.__got: 0x230
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x211a30
-  __DATA_CONST.__cfstring: 0xd7a0
+  __DATA_CONST.__const: 0x214620
+  __DATA_CONST.__cfstring: 0xd880
   __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0

   __DATA_CONST.__objc_dictobj: 0x910
   __DATA_CONST.__objc_arrayobj: 0x3a8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xe978
-  __DATA.__objc_selrefs: 0x3aa0
+  __DATA.__objc_const: 0xea28
+  __DATA.__objc_selrefs: 0x3ac8
   __DATA.__objc_protorefs: 0x50
   __DATA.__objc_classrefs: 0x5f8
   __DATA.__objc_superrefs: 0x3e0
-  __DATA.__objc_ivar: 0xa10
+  __DATA.__objc_ivar: 0xa24
   __DATA.__objc_data: 0x2800
-  __DATA.__data: 0xb98
+  __DATA.__data: 0xba0
   __DATA.__thread_vars: 0x30
   __DATA.__thread_bss: 0x31
-  __DATA.__bss: 0x100e90
-  __DATA.__common: 0x30
+  __DATA.__bss: 0x100ec8
+  __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - @rpath/LLDB.framework/LLDB
   - @rpath/MTLReplayController.framework/MTLReplayController
   - @rpath/libGTLLVMShaderProfilerHelper.dylib
-  UUID: BED1F3F9-72C4-35DC-AAE5-7356859FC7C3
-  Functions: 5027
-  Symbols:   836
-  CStrings:  17912
+  UUID: 38D77CDF-CE3A-3A11-87EA-820278197911
+  Functions: 5038
+  Symbols:   839
+  CStrings:  17944
 
Symbols:
+ _MTLDevice_newLibraryWithFile
+ _MTLLibraryErrorDomain
+ _strnlen
CStrings:
+ "\x01\x111\x15"
+ "\"/Library/Caches/com.apple.xbs/Sources/GPUToolsDevice/Dependencies/AGXProfilingSupport/AGXProfilingSupport/DerivedCounters/AGXPSLimiters.cpp\"_131_100"
+ "\"/Library/Caches/com.apple.xbs/Sources/GPUToolsDevice/Dependencies/AGXProfilingSupport/AGXProfilingSupport/DerivedCounters/AGXPSLimiters.cpp\"_134_102"
+ "\"/Library/Caches/com.apple.xbs/Sources/GPUToolsDevice/Dependencies/AGXProfilingSupport/AGXProfilingSupport/DerivedCounters/AGXPSLimiters.cpp\"_138_105"
+ "%llu.metallib"
+ "/\x041\x15"
+ "<blurb about the Other L1 Loads Utilization"
+ "<blurb about the Other L1 Stores Utilization"
+ "@\"NSObject<OS_dispatch_group>\""
+ "@24@0:8^{GTMTLReplayClient=^{apr_pool_t}^{GTMTLReplayController}Q{?=QQQdII}{?={?=II}IIfb1b1b1b1b28}@{GTMTLReplayWireframeRenderer=@@Q@@@Q@@@@@@@@@@@@@}{GTMTLReplayOperationQueues=@@}@@@}16"
+ "A measure of the number of L1 cache lines evicted by shader core private memory accesses . The more this number approaches 1.0 (100%), the more that the Occupancy Manager will attempt to reduce simdgroup occupancy."
+ "APSTraceDataFile"
+ "Compute Simdgroups Inflight Per Shader Core"
+ "Fragment Simdgroups Inflight Per Shader Core"
+ "Internal error: Failed to resolve compute encoder"
+ "L1 Other Bytes Occupancy"
+ "L1 Other Occupancy"
+ "Number of Other bytes cached in the L1."
+ "OMU_EVAL_WINDOW"
+ "Occupancy Management L1 Eviction Rate"
+ "Occupancy Manager Target"
+ "Other L1 Load Bandwidth"
+ "Other L1 Loads Utilization"
+ "Other L1 Store Bandwidth"
+ "Other L1 Stores Utilization"
+ "Percentage of the L1 caching Other Memory."
+ "SupportsSeparateAPSDataFile"
+ "TB,R,N,V_supportsSeparateAPSData"
+ "The number of compute simdgroups running concurrently on the shaders cores, normalized to max simdgroups inflight supported by the GPU."
+ "The number of compute simdgroups running concurrently per shader core."
+ "The number of fragment simdgroups running concurrently on the shaders cores, normalized to max simdgroups inflight supported by the GPU."
+ "The number of fragment simdgroups running concurrently per shader core."
+ "The number of simdgroups running concurrently on the shaders cores, normalized to max simdgroups inflight supported by the GPU."
+ "The number of simdgroups running concurrently per shaders core."
+ "The number of vertex simdgroups running concurrently on the shaders cores, normalized to max simdgroups inflight supported by the GPU."
+ "The number of vertex simdgroups running concurrently per shader core."
+ "The occupancy level to which the occupancy mangement unit is attempting to achieve."
+ "Total Simdgroups Inflight Per Shader Core"
+ "Unable to find child acceleration structure(s). Did you forgot to useResource or useHeap?"
+ "Vertex Simdgroups Inflight Per Shader Core"
+ "^{GTMTLReplayClient=^{apr_pool_t}^{GTMTLReplayController}Q{?=QQQdII}{?={?=II}IIfb1b1b1b1b28}@{GTMTLReplayWireframeRenderer=@@Q@@@Q@@@@@@@@@@@@@}{GTMTLReplayOperationQueues=@@}@@@}"
+ "_0965349a7930ddeeae0312bca50ac5672d7ecdb1e38a915536c0e7b8a1a3c321"
+ "_53c82a25ac54f8ecd1e94581a4020f0a20529b4813cab97e3977346ad0e270a8"
+ "_c5f3e2463ad7fa5ab5b1f302a7b6e4723cc862f7c9a663df1dbc634d50f4f63d"
+ "_copyForAddAPSData:"
+ "_downloadHighWaterMarkBytes"
+ "_downloadStoreBytes"
+ "_downloadTransmitOff"
+ "_downloadTransmitState"
+ "_stream"
+ "_supportsSeparateAPSData"
+ "_tempAPSCounterData"
+ "_tempAPSData"
+ "_tempAPSTimelineData"
+ "copyItemAtPath:toPath:error:"
+ "dataWithContentsOfFile:options:error:"
+ "dylib-"
+ "encodeAPSArrayForOldHost:array:"
+ "initWithDownloadHighWaterMark:"
+ "missing rejectAllFunction"
+ "omu_eval_window"
+ "rejectAllFunction is nil"
+ "supportsSeparateAPSData"
+ "takeDownloadDataForHandle:"
+ "v72@0:8^{GTMTLReplayClient=^{apr_pool_t}^{GTMTLReplayController}Q{?=QQQdII}{?={?=II}IIfb1b1b1b1b28}@{GTMTLReplayWireframeRenderer=@@Q@@@Q@@@@@@@@@@@@@}{GTMTLReplayOperationQueues=@@}@@@}16Q24@32@40@?48Q56@?64"
+ "waitUntilDownloadCapacity"
+ "{GTMTLReplayClient=\"pool\"^{apr_pool_t}\"replayController\"^{GTMTLReplayController}\"sessionId\"Q\"config\"{?=\"hostInfoType\"Q\"profilingSendPeriod\"Q\"profilingFlags\"Q\"xcodeOverrideScaleTessFactor\"d\"traceMode\"I\"xcodeOverrideFlags\"I}\"state\"{?=\"targetIndex\"{?=\"function\"I\"subCommand\"I}\"wireframeLineColor\"I\"outlineColor\"I\"wireframeLineWidth\"f\"enableDrawCallPresent\"b1\"enableWireframePresent\"b1\"enableOutlinePresent\"b1\"disablePresent\"b1\"_padding\"b28}\"generateThumbnails\"@\"NSMutableArray\"\"wireframe\"{GTMTLReplayWireframeRenderer=\"textureDescriptor\"@\"MTLTextureDescriptor\"\"renderPassDescriptor\"@\"MTLRenderPassDescriptor\"\"pixelFormat\"Q\"fragmentFunction\"@\"<MTLFunction>\"\"texture\"@\"<MTLTexture>\"\"solidTexture\"@\"<MTLTexture>\"\"textureSampleCount\"Q\"outlinePipelineState\"@\"<MTLComputePipelineState>\"\"outlinePipelineStateMS\"@\"<MTLComputePipelineState>\"\"postVertexDumpBuffer\"@\"<MTLBuffer>\"\"resizeRenderPipelineDescriptor\"@\"MTLRenderPipelineDescriptor\"\"resizeColorFunction\"@\"<MTLFunction>\"\"resizeColorUintFunction\"@\"<MTLFunction>\"\"resizeColorSintFunction\"@\"<MTLFunction>\"\"resizeDepthFunction\"@\"<MTLFunction>\"\"resizeStencilFunction\"@\"<MTLFunction>\"\"upscaleSamplerState\"@\"<MTLSamplerState>\"\"downscaleSamplerState\"@\"<MTLSamplerState>\"\"quadData\"@\"<MTLBuffer>\"\"resizeRenderPipelineStates\"@\"NSMutableDictionary\"}\"operationQueues\"{GTMTLReplayOperationQueues=\"serialQueue\"@\"NSOperationQueue\"\"parallelQueue\"@\"NSOperationQueue\"}\"cancelableOperations\"@\"NSMutableArray\"\"displayDelegate\"@\"<GTMTLReplayDisplayDelegate>\"\"bulkDataService\"@\"GTBulkDataService\"}"
+ "\xb3\x13\x1f\x06"
- "\x01\x11\x15"
- "\"/Library/Caches/com.apple.xbs/Sources/GPUToolsDevice/Dependencies/AGXProfilingSupport/AGXProfilingSupport/DerivedCounters/AGXPSLimiters.cpp\"_130_100"
- "\"/Library/Caches/com.apple.xbs/Sources/GPUToolsDevice/Dependencies/AGXProfilingSupport/AGXProfilingSupport/DerivedCounters/AGXPSLimiters.cpp\"_133_102"
- "\"/Library/Caches/com.apple.xbs/Sources/GPUToolsDevice/Dependencies/AGXProfilingSupport/AGXProfilingSupport/DerivedCounters/AGXPSLimiters.cpp\"_137_105"
- "\"/Library/Caches/com.apple.xbs/Sources/GPUToolsDevice/Dependencies/AGXProfilingSupport/AGXProfilingSupport/DerivedCounters/AGXPSLimiters.cpp\"_141_108"
- "\"/Library/Caches/com.apple.xbs/Sources/GPUToolsDevice/Dependencies/AGXProfilingSupport/AGXProfilingSupport/DerivedCounters/AGXPSLimiters.cpp\"_85_55"
- "/\x041\x12"
- "<blurb about Compute Occupancy"
- "<blurb about Fragment Occupancy"
- "<blurb about Total Occupancy"
- "<blurb about Vertex Occupancy"
- "<blurb about the Uncategorized L1 Loads Utilization"
- "<blurb about the Uncategorized L1 Stores Utilization"
- "@24@0:8^{GTMTLReplayClient=^{apr_pool_t}^{GTMTLReplayController}Q{?=QQQdII}{?={?=II}IIfb1b1b1b1b28}@{GTMTLReplayWireframeRenderer=@@Q@@@Q@@@@@@@@@@@@@}{GTMTLReplayOperationQueues=@@}@@}16"
- "Files have invalid data"
- "Internal error: Failed to set up resolve compute encoder"
- "L1 Uncategorized Bytes Occupancy"
- "L1 Uncategorized Occupancy"
- "Number of Uncategorized bytes cached in the L1."
- "Occupancy Throttler Target"
- "Percentage of the L1 caching Uncategorized Memory."
- "Simdgroup Packing Inefficiency"
- "Texture Cache Limiter GT"
- "Texture Cache Utilization GT"
- "Texture Read Limiter GT"
- "Texture Read Utilization GT"
- "The average percentage of unused threads per simdgroup. For example, on a GPU with 32 threads per simdgroup, 0.25 means 8 threads per simdgroup are unused."
- "The occupancy level to which the occupancy throttler is attempting to achieve."
- "Unable to find child acceleration structure(s). Did you forget to call useResource?"
- "Unable to find child acceleration structure. Did you forgot to useResource?"
- "Uncategorized L1 Loads Utilization"
- "Uncategorized L1 Stores Utilization"
- "Unclassified L1 Load Bandwidth"
- "Unclassified L1 Store Bandwidth"
- "^{GTMTLReplayClient=^{apr_pool_t}^{GTMTLReplayController}Q{?=QQQdII}{?={?=II}IIfb1b1b1b1b28}@{GTMTLReplayWireframeRenderer=@@Q@@@Q@@@@@@@@@@@@@}{GTMTLReplayOperationQueues=@@}@@}"
- "_addIfAPSBufferData:withData:"
- "_archiveRingBufferAPSData"
- "_perRingBufferAPSCounterData"
- "_perRingBufferAPSData"
- "_perRingBufferAPSTimelineData"
- "optimizeStreamData"
- "v72@0:8^{GTMTLReplayClient=^{apr_pool_t}^{GTMTLReplayController}Q{?=QQQdII}{?={?=II}IIfb1b1b1b1b28}@{GTMTLReplayWireframeRenderer=@@Q@@@Q@@@@@@@@@@@@@}{GTMTLReplayOperationQueues=@@}@@}16Q24@32@40@?48Q56@?64"
- "{GTMTLReplayClient=\"pool\"^{apr_pool_t}\"replayController\"^{GTMTLReplayController}\"sessionId\"Q\"config\"{?=\"hostInfoType\"Q\"profilingSendPeriod\"Q\"profilingFlags\"Q\"xcodeOverrideScaleTessFactor\"d\"traceMode\"I\"xcodeOverrideFlags\"I}\"state\"{?=\"targetIndex\"{?=\"function\"I\"subCommand\"I}\"wireframeLineColor\"I\"outlineColor\"I\"wireframeLineWidth\"f\"enableDrawCallPresent\"b1\"enableWireframePresent\"b1\"enableOutlinePresent\"b1\"disablePresent\"b1\"_padding\"b28}\"generateThumbnails\"@\"NSMutableArray\"\"wireframe\"{GTMTLReplayWireframeRenderer=\"textureDescriptor\"@\"MTLTextureDescriptor\"\"renderPassDescriptor\"@\"MTLRenderPassDescriptor\"\"pixelFormat\"Q\"fragmentFunction\"@\"<MTLFunction>\"\"texture\"@\"<MTLTexture>\"\"solidTexture\"@\"<MTLTexture>\"\"textureSampleCount\"Q\"outlinePipelineState\"@\"<MTLComputePipelineState>\"\"outlinePipelineStateMS\"@\"<MTLComputePipelineState>\"\"postVertexDumpBuffer\"@\"<MTLBuffer>\"\"resizeRenderPipelineDescriptor\"@\"MTLRenderPipelineDescriptor\"\"resizeColorFunction\"@\"<MTLFunction>\"\"resizeColorUintFunction\"@\"<MTLFunction>\"\"resizeColorSintFunction\"@\"<MTLFunction>\"\"resizeDepthFunction\"@\"<MTLFunction>\"\"resizeStencilFunction\"@\"<MTLFunction>\"\"upscaleSamplerState\"@\"<MTLSamplerState>\"\"downscaleSamplerState\"@\"<MTLSamplerState>\"\"quadData\"@\"<MTLBuffer>\"\"resizeRenderPipelineStates\"@\"NSMutableDictionary\"}\"operationQueues\"{GTMTLReplayOperationQueues=\"serialQueue\"@\"NSOperationQueue\"\"parallelQueue\"@\"NSOperationQueue\"}\"cancelableOperations\"@\"NSMutableArray\"\"displayDelegate\"@\"<GTMTLReplayDisplayDelegate>\"}"
- "\xb3\x13\x1f\x05"

```
