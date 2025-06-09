## gputoolsserviced

> `/usr/libexec/gputoolsserviced`

```diff

-304.7.0.0.0
-  __TEXT.__text: 0x1f424
-  __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_stubs: 0x39a0
-  __TEXT.__objc_methlist: 0x2a04
-  __TEXT.__const: 0x446
-  __TEXT.__cstring: 0x1bee
-  __TEXT.__objc_methname: 0x5a22
-  __TEXT.__oslogstring: 0x6e8
-  __TEXT.__objc_classname: 0x69f
-  __TEXT.__objc_methtype: 0xfd2
-  __TEXT.__unwind_info: 0x740
-  __DATA_CONST.__auth_got: 0x630
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x7e8
-  __DATA_CONST.__cfstring: 0x1fc0
-  __DATA_CONST.__objc_classlist: 0x208
-  __DATA_CONST.__objc_protolist: 0xc0
+310.22.0.0.0
+  __TEXT.__text: 0x28644
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_stubs: 0x4b20
+  __TEXT.__objc_methlist: 0x2ccc
+  __TEXT.__const: 0x498
+  __TEXT.__cstring: 0x26f3
+  __TEXT.__objc_classname: 0x726
+  __TEXT.__objc_methname: 0x6b41
+  __TEXT.__objc_methtype: 0x1156
+  __TEXT.__oslogstring: 0xfcc
+  __TEXT.__unwind_info: 0x848
+  __DATA_CONST.__auth_got: 0x6c8
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__const: 0xa18
+  __DATA_CONST.__cfstring: 0x2800
+  __DATA_CONST.__objc_classlist: 0x228
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_classrefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x5b50
-  __DATA.__objc_selrefs: 0x1600
-  __DATA.__objc_ivar: 0x3b0
-  __DATA.__objc_data: 0x1450
-  __DATA.__data: 0x910
-  __DATA.__bss: 0x38
+  __DATA.__objc_const: 0x5ee0
+  __DATA.__objc_selrefs: 0x1a98
+  __DATA.__objc_ivar: 0x3b8
+  __DATA.__objc_data: 0x1590
+  __DATA.__data: 0xc88
+  __DATA.__bss: 0x2c
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/GPUToolsDeviceServices.framework/GPUToolsDeviceServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6CBADCE2-BF0F-39CC-A5E7-566C34E65C8E
-  Functions: 860
-  Symbols:   274
-  CStrings:  1891
+  UUID: 4B21D160-0FA0-3A40-80B3-133D025497AE
+  Functions: 970
+  Symbols:   302
+  CStrings:  2257
 
Symbols:
+ _APP_SANDBOX_READ_WRITE
+ _CFDataGetBytePtr
+ _NSClassFromString
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_MTLFXFrameInterpolatorDescriptor
+ _OBJC_CLASS_$_MTLFXTemporalDenoisedScalerDescriptor
+ _OBJC_CLASS_$_NSDate
+ __CFURLCopySecurityScopeFromFileURL
+ ___stderrp
+ ___stdoutp
+ __dispatch_source_type_signal
+ __os_log_disabled
+ __os_log_fault_impl
+ _chown
+ _dispatch_resume
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _fprintf
+ _objc_retain_x28
+ _objc_setProperty_atomic
+ _proc_name
+ _protocol_copyProtocolList
+ _qsort
+ _readlink
+ _stat
+ _xpc_connection_create
+ _xpc_connection_get_pid
+ _xpc_connection_set_oneshot_instance
CStrings:
+ "\tB"
+ "%s\n"
+ "%s.%s.enableLog"
+ "1"
+ "???"
+ "@\"<GTErrorReportService>\""
+ "@\"GTErrorReportService\""
+ "@\"NSDate\""
+ "@\"NSMutableArray\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@56@0:8@16{MessageRemoteRoutingInfo=QQQB[7c]}24"
+ "BoundaryTracker"
+ "Cancelling incoming connection from disallowed pid %lu"
+ "CommandBuffers"
+ "Connected process is not debuggable"
+ "Critical"
+ "Directory enumeration failed whilst deleting archives %@"
+ "DispatchSorter"
+ "EventTracker"
+ "Expected 1 matching remote relay port for PID %lu, got %lu"
+ "Failed to close fd (%d), status %d"
+ "Failed to close file %@"
+ "Failed to close file %@ (%d)"
+ "Failed to delete archive %@ %@"
+ "Failed to flush fd (%d)"
+ "Failed to flush file %@"
+ "Failed to flush file %@ (%d)"
+ "Failed to get audit token for self (%d)"
+ "Failed to initialize decode compression stream"
+ "Failed to initialize encode compression stream"
+ "Failed to open file %@ for reading (%d)"
+ "Failed to open file %@ for writing"
+ "Failed to open file %@ for writing (%d)"
+ "Failed to read from file %@ (%d)"
+ "Failed to read symlink for %@"
+ "Failed to read symlink for %@ (%d)"
+ "Failed to resize file %@"
+ "Failed to resize file %@ (%d)"
+ "Failed to stat directory %@ after transfer: %{darwin.errno}d"
+ "Failed to update owner of archive %@ after transfer: %{darwin.errno}d"
+ "Failed to update owner of one or more files inside archive %@ after transfer"
+ "Failed to write to fd (%d)"
+ "Failure whilst decoding timestamp for GTRejectedConnectionReport, %@"
+ "File writer service for %@ is unavailable"
+ "File writer service is too old. Missing selector %@"
+ "GPUToolsReplayerPreferXPCService"
+ "GTErrorReportService"
+ "GTErrorReportServiceObserver"
+ "GTErrorReportServiceXPCDispatcher"
+ "GTObserverXPCDispatcher"
+ "GTRejectedConnectionReport"
+ "Harvest"
+ "Invalid archive passed to UpdateArchiveOwner"
+ "Invalid destination directory passed to copyIdentifier"
+ "Invalid destination directory passed to initiateTransfer"
+ "Invalid options sent to beginTransferSessionWithFileEntries"
+ "Invalid options sent to initiateTransfer"
+ "Invalid sandbox ID %@"
+ "MTLFXFrameInterpolatorDescriptor"
+ "MTLFXTemporalDenoisedScalerDescriptor"
+ "MTLREPLAYER_DISABLE_REPLAY_SERVICE"
+ "No matching relay for PID %lu, picking highest service port %lu (PID %lu)"
+ "Profiling"
+ "Remote connection for %@ is unavailable"
+ "Restores"
+ "Start transfer of %@ to %@"
+ "T@\"NSDate\",&,V_timestamp"
+ "T@\"NSString\",&,V_name"
+ "TB,N,V_disableDisplay"
+ "TB,N,V_preferXPCService"
+ "TI,N,V_presentDownloadSize"
+ "TQ,V_pid"
+ "Target path for symlink %@ is too long (%zd bytes >= %lu bytes [PATH_MAX])"
+ "The gputrace file transfer service is too old to support remote macOS debugging. Try updating your device's DDI by installing a newer Xcode."
+ "Tq,N,V_version"
+ "TraceStore"
+ "Unrecognized daemon message %lu"
+ "Updating owner of archive %@ to %u:%u"
+ "_disableDisplay"
+ "_errorReportService"
+ "_nextRejectedConnectionIndex"
+ "_pid"
+ "_preferXPCService"
+ "_presentDownloadSize"
+ "_rejectedConnections"
+ "_remoteDeviceRelayRemotePid"
+ "_remoteRoutingInfo"
+ "_routingInfo"
+ "_serviceListener"
+ "_sigtermSource"
+ "_timestamp"
+ "addObjectsFromArray:"
+ "beginTransferSessionWithFileEntries timed out waiting for final write to complete"
+ "beginTransferSessionWithFileEntries timed out waiting for transfer to complete"
+ "boolForKey:"
+ "bufferRobustnessSupport"
+ "clear"
+ "code"
+ "com.apple.gputools.ASBuilder"
+ "com.apple.gputools.ASViewer"
+ "com.apple.gputools.GPUToolsReplayService"
+ "com.apple.gputools.cli"
+ "com.apple.gputools.core"
+ "com.apple.gputools.diagnostics"
+ "com.apple.gputools.filewriter"
+ "com.apple.gputools.replay"
+ "copyIdentifier %@ to device %@"
+ "copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:"
+ "copyIdentifier:toDevice:directory:completionHandler:"
+ "copyIdentifier_toDevice_directory_completionHandler_:replyConnection:"
+ "date"
+ "decodeTopLevelObjectOfClass:forKey:error:"
+ "dedicatedMemorySize"
+ "defaultTextureWriteRoundingMode"
+ "deviceCreationFlags"
+ "dir"
+ "directory"
+ "dirse"
+ "disableDisplay"
+ "domain"
+ "doubleFPConfig"
+ "fail: Invalid log tag: %u"
+ "fetchRejectedConnections:"
+ "fetchRejectedConnections_:replyConnection:"
+ "getUUIDBytes:"
+ "halfFPConfig"
+ "initEventStreamHandler"
+ "initServiceListener"
+ "initSignalHandler"
+ "initSimulatorLaunchServiceListener"
+ "initSimulatorServiceListener"
+ "initWithConnection:routingInfo:"
+ "isQuadDataSharingSupported"
+ "latestSupportedGenericBVHVersion"
+ "launchReplayServiceApp:error:"
+ "launchReplayServiceXPC:error:"
+ "limits"
+ "maxAccelerationStructureTraversalDepth"
+ "maxRasterizationRateLayerCount"
+ "maximumComputeSubstreams"
+ "notifyRejectedConnections:"
+ "onRemoteDevice"
+ "pid"
+ "preferXPCService"
+ "presentDownloadSize"
+ "readWriteTextureSupport"
+ "removeAllObjects"
+ "reportRejectedConnection:"
+ "requiresBFloat16Emulation"
+ "requiresRaytracingEmulation"
+ "setDisableDisplay:"
+ "setObject:atIndexedSubscript:"
+ "setPid:"
+ "setPreferXPCService:"
+ "setPresentDownloadSize:"
+ "setTimestamp:"
+ "sharedMemorySize"
+ "singleFPConfig"
+ "sparseTexturesSupport"
+ "startTransfer:basePath:fromDevice:toDirectory:options:completionHandler:"
+ "startTransfer_basePath_fromDevice_toDirectory_options_completionHandler_:replyConnection:"
+ "supportPriorityBand"
+ "supportedInputContentMaxScaleForDevice:"
+ "supportedInputContentMinScaleForDevice:"
+ "supports32BitFloatFiltering"
+ "supportsAnisoSampleFix"
+ "supportsArrayOfSamplers"
+ "supportsArrayOfTextures"
+ "supportsAtomicUlongVoidMinMax"
+ "supportsBaseVertexInstanceDrawing"
+ "supportsBfloat16Buffers"
+ "supportsBinaryArchives"
+ "supportsBufferBoundsChecking"
+ "supportsBufferPrefetchStatistics"
+ "supportsCommandBufferJump"
+ "supportsCompressedTextureViewSPI"
+ "supportsComputeCompressedTextureWrite"
+ "supportsCountingOcclusionQuery"
+ "supportsDeadlineProfile"
+ "supportsDevicePartitioning"
+ "supportsDynamicControlPointCount"
+ "supportsExplicitVisibilityGroups"
+ "supportsFP32TessFactors"
+ "supportsFastMathInfNaNPropagation"
+ "supportsFillTexture"
+ "supportsFixedLinePointFillDepthGradient"
+ "supportsFloat16BCubicFiltering"
+ "supportsFloat16InfNanFiltering"
+ "supportsForceSeamsOnCubemaps"
+ "supportsForkJoin"
+ "supportsFragmentBufferWrites"
+ "supportsFragmentOnlyEncoders"
+ "supportsGlobalVariableRelocation"
+ "supportsGlobalVariableRelocationCompute"
+ "supportsGlobalVariableRelocationRender"
+ "supportsIABHashForTools"
+ "supportsImageBlockSampleCoverageControl"
+ "supportsImageBlocks"
+ "supportsIndirectStageInRegion"
+ "supportsIndirectTessellation"
+ "supportsIndirectTextures"
+ "supportsIndirectWritableTextures"
+ "supportsInt64"
+ "supportsInterchangeTiled"
+ "supportsIntersectionFunctionBuffers"
+ "supportsInvariantVertexPosition"
+ "supportsLargeFramebufferConfigs"
+ "supportsMemoryOrderAtomics"
+ "supportsMipLevelsSmallerThanBlockSize"
+ "supportsMutableTier1ArgumentBuffers"
+ "supportsNativeHardwareFP16"
+ "supportsNonZeroTextureWriteLOD"
+ "supportsNorm16BCubicFiltering"
+ "supportsOpenCLTextureWriteSwizzles"
+ "supportsPacked32TextureBufferWrites"
+ "supportsPerformanceStateAssertion"
+ "supportsPipelineLibraries"
+ "supportsPostDepthCoverage"
+ "supportsPrimitiveRestartOverride"
+ "supportsPrimitiveType:"
+ "supportsProgrammableBlending"
+ "supportsPullModelInterpolation"
+ "supportsQuadGroup"
+ "supportsQuadReduction"
+ "supportsQuadShufflesAndBroadcast"
+ "supportsQueryTextureLOD"
+ "supportsRTZRounding"
+ "supportsRasterOrderGroups"
+ "supportsRasterOrderGroupsColorAttachment"
+ "supportsRayTracingTraversalMetrics"
+ "supportsRaytracingFromRender"
+ "supportsReadWriteBufferArguments"
+ "supportsReadWriteTextureArguments"
+ "supportsReadWriteTextureArgumentsTier2"
+ "supportsReadWriteTextureCubeArguments"
+ "supportsRenderPassWithoutRenderTarget"
+ "supportsRenderTextureWrites"
+ "supportsSIMDGroup"
+ "supportsSIMDGroupMatrix"
+ "supportsSIMDReduction"
+ "supportsSIMDShuffleAndFill"
+ "supportsSIMDShufflesAndBroadcast"
+ "supportsSeparateVisibilityAndShadingRate"
+ "supportsSetThreadgroupPackingDisabled"
+ "supportsShaderBarycentricCoordinates"
+ "supportsShaderLODAverage"
+ "supportsShaderMinLODClamp"
+ "supportsStackOverflowErrorCode"
+ "supportsStencilFeedback"
+ "supportsStreamingCodecSignaling"
+ "supportsTLS"
+ "supportsTessellation"
+ "supportsTextureOutOfBoundsReads"
+ "supportsTextureWriteRoundingMode:"
+ "supportsUnalignedVertexFetch"
+ "supportsVirtualSubstreams"
+ "supportsWritableArrayOfTextures"
+ "timestamp"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v48@0:8@\"NSURL\"16@\"NSString\"24@\"NSURL\"32@?<v@?@\"NSURL\"@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
+ "v52@0:8@16@24B32@36@?44"
+ "v64@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSURL\"40@\"GTFileTransferOptions\"48@?<v@?@\"NSURL\"@\"NSError\">56"
+ "{MessageRemoteRoutingInfo=\"hostPort\"Q\"hostPid\"Q\"remotePid\"Q\"onRemote\"B\"_padding\"[7c]}"
- "\t"
- "@\"NSObject<OS_os_log>\""
- "@36@0:8@16Q24i32"
- "EntitlementConnection"
- "Failed to close file"
- "Failed to flush file"
- "Failed to initialize compression stream"
- "Failed to open file for writing"
- "Failed to resize file"
- "Failed to write to file"
- "FileWriterService"
- "FileWriterSession"
- "GPUTOOLS(warning): Log uninitialized, please call GTCoreLogInit(), logging to OS_LOG_DEFAULT instead"
- "Invalid sandbox ID"
- "Loopback"
- "Q24@0:8@\"<GTServiceProviderObserver>\"16"
- "ServiceDaemon"
- "ServiceProvider"
- "ServiceProviderProxy"
- "URLAccessProvider"
- "URLByResolvingSymlinksInPath"
- "_currentRemoteRelayPid"
- "_currentRemoteRelayPort"
- "_log"
- "_relayPid"
- "_relayPort"
- "beginTransferSessionWithFileEntires timed out waiting for final write to complete"
- "beginTransferSessionWithFileEntires timed out waiting for transfer to complete"
- "com.apple.gputools.filestreamer"
- "copyIdentifier:toDevice:allowLocalURL:completionHandler:"
- "initWithConnection:"
- "initWithConnection:relayPort:relayPid:"
- "transferIdentifier %@ to device %@"
- "updateRelayPort:pid:"
- "v28@0:8Q16i24"
- "v44@0:8@16@24B32@?36"

```
