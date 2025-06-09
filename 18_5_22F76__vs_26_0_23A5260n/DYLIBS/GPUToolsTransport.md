## GPUToolsTransport

> `/System/Library/PrivateFrameworks/GPUToolsTransport.framework/GPUToolsTransport`

```diff

-304.7.0.0.0
-  __TEXT.__text: 0x317ac
-  __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0x584c
-  __TEXT.__const: 0x50e
-  __TEXT.__cstring: 0x26e1
-  __TEXT.__oslogstring: 0x7a9
-  __TEXT.__unwind_info: 0xbb8
-  __TEXT.__objc_classname: 0x10a9
-  __TEXT.__objc_methname: 0x900b
-  __TEXT.__objc_methtype: 0x1875
-  __TEXT.__objc_stubs: 0x4880
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0xad0
-  __DATA_CONST.__objc_classlist: 0x4c0
-  __DATA_CONST.__objc_protolist: 0x150
+310.22.0.0.0
+  __TEXT.__text: 0x3dd48
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__objc_methlist: 0x6094
+  __TEXT.__const: 0x548
+  __TEXT.__cstring: 0x34f0
+  __TEXT.__oslogstring: 0x10d1
+  __TEXT.__unwind_info: 0xe70
+  __TEXT.__objc_classname: 0x13c4
+  __TEXT.__objc_methname: 0x9923
+  __TEXT.__objc_methtype: 0x1b0a
+  __TEXT.__objc_stubs: 0x5860
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__const: 0xd20
+  __DATA_CONST.__objc_classlist: 0x588
+  __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2200
-  __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_classrefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x468
+  __DATA_CONST.__objc_selrefs: 0x2560
+  __DATA_CONST.__objc_protorefs: 0xb0
+  __DATA_CONST.__objc_classrefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x5e8
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x30e0
-  __AUTH_CONST.__objc_const: 0xccf8
+  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0x3b60
+  __AUTH_CONST.__objc_const: 0xe310
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x2f80
-  __DATA.__objc_ivar: 0x7b0
-  __DATA.__data: 0xfdc
+  __AUTH.__objc_data: 0x3750
+  __DATA.__objc_ivar: 0x7f4
+  __DATA.__data: 0x1480
+  __DATA.__bss: 0x100034
   __DATA.__common: 0x18
-  __DATA.__bss: 0x100048
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AEC45BBF-DE41-3811-92A4-CD9272A18A5F
-  Functions: 1708
-  Symbols:   6304
-  CStrings:  3014
+  UUID: 7514565A-F5E7-3965-8F31-ECB9569FD43F
+  Functions: 1938
+  Symbols:   7184
+  CStrings:  3379
 
Symbols:
+ +[GTDisplayRequest supportsSecureCoding]
+ +[GTDisplayResponse supportsSecureCoding]
+ +[GTDisplayShowTextureRequest supportsSecureCoding]
+ +[GTDisplayUpdateOverlaysRequest supportsSecureCoding]
+ +[GTDisplayUpdateTerminationRequest supportsSecureCoding]
+ +[GTDisplayUpdateWindowConfigurationRequest supportsSecureCoding]
+ +[GTRejectedConnectionReport supportsSecureCoding]
+ +[GTReplayDecodeGenericAccelerationStructure supportsSecureCoding]
+ +[GTReplayFetchInto supportsSecureCoding]
+ +[GTReplayFetchIntoTexture supportsSecureCoding]
+ +[GTReplayFetchMLGraph supportsSecureCoding]
+ +[GTReplayFetchMLGraphData supportsSecureCoding]
+ +[GTReplayFetchMLIntermediateData supportsSecureCoding]
+ +[GTReplayFetchPipelineBinaries supportsSecureCoding]
+ +[GTReplayFetchTensor supportsSecureCoding]
+ -[DYMTLDeviceProfile setVersion:]
+ -[DYMTLDeviceProfile version]
+ -[GTCaptureConfiguration presentDownloadSize]
+ -[GTCaptureConfiguration setPresentDownloadSize:]
+ -[GTDisplayRequest encodeWithCoder:]
+ -[GTDisplayRequest initWithCoder:]
+ -[GTDisplayRequest init]
+ -[GTDisplayRequest requestID]
+ -[GTDisplayRequest setRequestID:]
+ -[GTDisplayRequestToken .cxx_destruct]
+ -[GTDisplayRequestToken completed]
+ -[GTDisplayRequestToken initWithID:]
+ -[GTDisplayRequestToken requestID]
+ -[GTDisplayRequestToken waitUntilCompleted]
+ -[GTDisplayResponse .cxx_destruct]
+ -[GTDisplayResponse encodeWithCoder:]
+ -[GTDisplayResponse error]
+ -[GTDisplayResponse initWithCoder:]
+ -[GTDisplayResponse initWithID:]
+ -[GTDisplayResponse requestID]
+ -[GTDisplayResponse setError:]
+ -[GTDisplayResponse setRequestID:]
+ -[GTDisplayServiceXPCDispatcher .cxx_destruct]
+ -[GTDisplayServiceXPCDispatcher broadcastDisconnect:replyConnection:]
+ -[GTDisplayServiceXPCDispatcher initWithService:properties:]
+ -[GTDisplayServiceXPCDispatcher show_completionHandler_:replyConnection:]
+ -[GTDisplayServiceXPCDispatcher show_completionHandler_:replyConnection:].cold.1
+ -[GTDisplayServiceXPCDispatcher terminateProcess:replyConnection:]
+ -[GTDisplayServiceXPCDispatcher update_completionHandler_:replyConnection:]
+ -[GTDisplayServiceXPCDispatcher update_completionHandler_:replyConnection:].cold.1
+ -[GTDisplayServiceXPCProxy .cxx_destruct]
+ -[GTDisplayServiceXPCProxy initWithConnection:remoteProperties:]
+ -[GTDisplayServiceXPCProxy respondsToSelector:]
+ -[GTDisplayServiceXPCProxy show:completionHandler:]
+ -[GTDisplayServiceXPCProxy terminateProcess]
+ -[GTDisplayServiceXPCProxy update:completionHandler:]
+ -[GTDisplayShowTextureRequest depth]
+ -[GTDisplayShowTextureRequest dispatchUID]
+ -[GTDisplayShowTextureRequest encodeWithCoder:]
+ -[GTDisplayShowTextureRequest height]
+ -[GTDisplayShowTextureRequest initWithCoder:]
+ -[GTDisplayShowTextureRequest level]
+ -[GTDisplayShowTextureRequest pixelFormat]
+ -[GTDisplayShowTextureRequest plane]
+ -[GTDisplayShowTextureRequest replayServicePort]
+ -[GTDisplayShowTextureRequest setDepth:]
+ -[GTDisplayShowTextureRequest setDispatchUID:]
+ -[GTDisplayShowTextureRequest setHeight:]
+ -[GTDisplayShowTextureRequest setLevel:]
+ -[GTDisplayShowTextureRequest setPixelFormat:]
+ -[GTDisplayShowTextureRequest setPlane:]
+ -[GTDisplayShowTextureRequest setReplayServicePort:]
+ -[GTDisplayShowTextureRequest setSlice:]
+ -[GTDisplayShowTextureRequest setStreamRef:]
+ -[GTDisplayShowTextureRequest setWidth:]
+ -[GTDisplayShowTextureRequest slice]
+ -[GTDisplayShowTextureRequest streamRef]
+ -[GTDisplayShowTextureRequest width]
+ -[GTDisplayUpdateOverlaysRequest encodeWithCoder:]
+ -[GTDisplayUpdateOverlaysRequest initWithCoder:]
+ -[GTDisplayUpdateOverlaysRequest overlays]
+ -[GTDisplayUpdateOverlaysRequest setOverlays:]
+ -[GTDisplayUpdateTerminationRequest .cxx_destruct]
+ -[GTDisplayUpdateTerminationRequest connection]
+ -[GTDisplayUpdateTerminationRequest encodeWithCoder:]
+ -[GTDisplayUpdateTerminationRequest initWithCoder:]
+ -[GTDisplayUpdateTerminationRequest path]
+ -[GTDisplayUpdateTerminationRequest setConnection:]
+ -[GTDisplayUpdateTerminationRequest setPath:]
+ -[GTDisplayUpdateWindowConfigurationRequest .cxx_destruct]
+ -[GTDisplayUpdateWindowConfigurationRequest encodeWithCoder:]
+ -[GTDisplayUpdateWindowConfigurationRequest initWithCoder:]
+ -[GTDisplayUpdateWindowConfigurationRequest orientation]
+ -[GTDisplayUpdateWindowConfigurationRequest setOrientation:]
+ -[GTDisplayUpdateWindowConfigurationRequest setVisible:]
+ -[GTDisplayUpdateWindowConfigurationRequest setWindowTitle:]
+ -[GTDisplayUpdateWindowConfigurationRequest visible]
+ -[GTDisplayUpdateWindowConfigurationRequest windowTitle]
+ -[GTErrorReportServiceObserver notifyRejectedConnections:]
+ -[GTErrorReportServiceReplyStream .cxx_destruct]
+ -[GTErrorReportServiceReplyStream initWithObserver:]
+ -[GTErrorReportServiceReplyStream notifyRejectedConnections_:replyConnection:]
+ -[GTErrorReportServiceXPCDispatcher .cxx_destruct]
+ -[GTErrorReportServiceXPCDispatcher broadcastDisconnect:replyConnection:]
+ -[GTErrorReportServiceXPCDispatcher deregisterObserver_:replyConnection:]
+ -[GTErrorReportServiceXPCDispatcher fetchRejectedConnections_:replyConnection:]
+ -[GTErrorReportServiceXPCDispatcher initWithService:properties:]
+ -[GTErrorReportServiceXPCDispatcher registerObserver_:replyConnection:]
+ -[GTErrorReportServiceXPCProxy .cxx_destruct]
+ -[GTErrorReportServiceXPCProxy deregisterObserver:]
+ -[GTErrorReportServiceXPCProxy fetchRejectedConnections:]
+ -[GTErrorReportServiceXPCProxy initWithConnection:remoteProperties:]
+ -[GTErrorReportServiceXPCProxy registerObserver:]
+ -[GTErrorReportServiceXPCProxy respondsToSelector:]
+ -[GTErrorReportServiceXPCProxy returnRejectedConnections:]
+ -[GTFileWriterService beginTransferSessionWithFileEntries:basePath:toDevice:options:sessionID:completionHandler:].cold.1
+ -[GTFileWriterService beginTransferSessionWithFileEntries:basePath:toDevice:options:sessionID:completionHandler:].cold.2
+ -[GTFileWriterService beginTransferSessionWithFileEntries:basePath:toDevice:options:sessionID:completionHandler:].cold.3
+ -[GTFileWriterService beginTransferSessionWithFileEntries:basePath:toDevice:options:sessionID:completionHandler:].cold.4
+ -[GTFileWriterService initiateTransfer:basePath:fromDevice:toURL:options:completionHandler:].cold.1
+ -[GTFileWriterService initiateTransfer:basePath:fromDevice:toURL:options:completionHandler:].cold.2
+ -[GTFileWriterService initiateTransfer:basePath:fromDevice:toURL:options:completionHandler:].cold.3
+ -[GTFileWriterService startTransfer:basePath:fromDevice:toDirectory:options:completionHandler:]
+ -[GTFileWriterService startTransfer:basePath:fromDevice:toDirectory:options:completionHandler:].cold.1
+ -[GTFileWriterService startTransfer:basePath:fromDevice:toDirectory:options:completionHandler:].cold.2
+ -[GTFileWriterServiceXPCDispatcher beginTransferSessionWithFileEntries_basePath_toDevice_options_sessionID_completionHandler_:replyConnection:].cold.1
+ -[GTFileWriterServiceXPCDispatcher beginTransferSessionWithFileEntries_basePath_toDevice_options_sessionID_completionHandler_:replyConnection:].cold.2
+ -[GTFileWriterServiceXPCDispatcher initiateTransfer_basePath_fromDevice_options_completionHandler_:replyConnection:].cold.1
+ -[GTFileWriterServiceXPCDispatcher initiateTransfer_basePath_fromDevice_options_completionHandler_:replyConnection:].cold.2
+ -[GTFileWriterServiceXPCDispatcher startTransfer_basePath_fromDevice_options_completionHandler_:replyConnection:].cold.1
+ -[GTFileWriterServiceXPCDispatcher startTransfer_basePath_fromDevice_options_completionHandler_:replyConnection:].cold.2
+ -[GTFileWriterServiceXPCDispatcher startTransfer_basePath_fromDevice_toDirectory_options_completionHandler_:replyConnection:]
+ -[GTFileWriterServiceXPCDispatcher startTransfer_basePath_fromDevice_toDirectory_options_completionHandler_:replyConnection:].cold.1
+ -[GTFileWriterServiceXPCDispatcher startTransfer_basePath_fromDevice_toDirectory_options_completionHandler_:replyConnection:].cold.2
+ -[GTFileWriterServiceXPCDispatcher startTransfer_basePath_fromDevice_toDirectory_options_completionHandler_:replyConnection:].cold.3
+ -[GTFileWriterServiceXPCProxy startTransfer:basePath:fromDevice:toDirectory:options:completionHandler:]
+ -[GTFileWriterSessionCompressed initWithFileEntries:relativeToURL:options:error:].cold.1
+ -[GTFileWriterSessionUncompressed _closeCurrentFileDescriptor:].cold.1
+ -[GTFileWriterSessionUncompressed _closeCurrentFileDescriptor:].cold.2
+ -[GTFileWriterSessionUncompressed _openNextFile:].cold.1
+ -[GTFileWriterSessionUncompressed _openNextFile:].cold.2
+ -[GTFileWriterSessionUncompressed _writeUncompressedFileData:length:error:].cold.1
+ -[GTLaunchRequest disableDisplay]
+ -[GTLaunchRequest preferXPCService]
+ -[GTLaunchRequest setDisableDisplay:]
+ -[GTLaunchRequest setPreferXPCService:]
+ -[GTLoopbackService echo:].cold.1
+ -[GTLoopbackService echo:completionHandler:].cold.1
+ -[GTLoopbackService echo:repeat:callback:].cold.1
+ -[GTLoopbackService echo:repeat:callback:complete:].cold.1
+ -[GTMTLReplayServiceXPCDispatcher fetchInto_:replyConnection:]
+ -[GTMTLReplayServiceXPCDispatcher fetchInto_:replyConnection:].cold.1
+ -[GTMTLReplayServiceXPCProxy deviceUDID]
+ -[GTMTLReplayServiceXPCProxy fetchInto:]
+ -[GTMTLReplayServiceXPCProxy servicePort]
+ -[GTRejectedConnectionReport .cxx_destruct]
+ -[GTRejectedConnectionReport encodeWithCoder:]
+ -[GTRejectedConnectionReport initWithCoder:]
+ -[GTRejectedConnectionReport initWithCoder:].cold.1
+ -[GTRejectedConnectionReport name]
+ -[GTRejectedConnectionReport pid]
+ -[GTRejectedConnectionReport setName:]
+ -[GTRejectedConnectionReport setPid:]
+ -[GTRejectedConnectionReport setTimestamp:]
+ -[GTRejectedConnectionReport timestamp]
+ -[GTRelayedXPCConnection initWithConnection:routingInfo:]
+ -[GTRemoteDeviceBrowserXPCProxy registerObserver:].cold.1
+ -[GTReplayConfiguration enableLiveICBs]
+ -[GTReplayConfiguration forceResourcesResident]
+ -[GTReplayConfiguration setEnableLiveICBs:]
+ -[GTReplayConfiguration setForceResourcesResident:]
+ -[GTReplayDecodeGenericAccelerationStructure dispatchUID]
+ -[GTReplayDecodeGenericAccelerationStructure encodeWithCoder:]
+ -[GTReplayDecodeGenericAccelerationStructure initWithCoder:]
+ -[GTReplayDecodeGenericAccelerationStructure setDispatchUID:]
+ -[GTReplayDecodeGenericAccelerationStructure setStreamRef:]
+ -[GTReplayDecodeGenericAccelerationStructure streamRef]
+ -[GTReplayFetchInto .cxx_destruct]
+ -[GTReplayFetchInto decodeXPCOnlyObjects:]
+ -[GTReplayFetchInto dest]
+ -[GTReplayFetchInto dispatchUID]
+ -[GTReplayFetchInto encodeWithCoder:]
+ -[GTReplayFetchInto encodeXPCOnlyObjects:]
+ -[GTReplayFetchInto event]
+ -[GTReplayFetchInto initWithCoder:]
+ -[GTReplayFetchInto setDest:]
+ -[GTReplayFetchInto setDispatchUID:]
+ -[GTReplayFetchInto setEvent:]
+ -[GTReplayFetchIntoTexture depth]
+ -[GTReplayFetchIntoTexture encodeWithCoder:]
+ -[GTReplayFetchIntoTexture initWithCoder:]
+ -[GTReplayFetchIntoTexture level]
+ -[GTReplayFetchIntoTexture plane]
+ -[GTReplayFetchIntoTexture resolveMultisampleTexture]
+ -[GTReplayFetchIntoTexture setDepth:]
+ -[GTReplayFetchIntoTexture setLevel:]
+ -[GTReplayFetchIntoTexture setPlane:]
+ -[GTReplayFetchIntoTexture setResolveMultisampleTexture:]
+ -[GTReplayFetchIntoTexture setSlice:]
+ -[GTReplayFetchIntoTexture setStreamRef:]
+ -[GTReplayFetchIntoTexture slice]
+ -[GTReplayFetchIntoTexture streamRef]
+ -[GTReplayFetchMLGraph dispatchUID]
+ -[GTReplayFetchMLGraph encodeWithCoder:]
+ -[GTReplayFetchMLGraph initWithCoder:]
+ -[GTReplayFetchMLGraph pipelineRef]
+ -[GTReplayFetchMLGraph setDispatchUID:]
+ -[GTReplayFetchMLGraph setPipelineRef:]
+ -[GTReplayFetchMLGraphData .cxx_destruct]
+ -[GTReplayFetchMLGraphData dispatchUID]
+ -[GTReplayFetchMLGraphData encodeWithCoder:]
+ -[GTReplayFetchMLGraphData initWithCoder:]
+ -[GTReplayFetchMLGraphData mlModuleKey]
+ -[GTReplayFetchMLGraphData mlResourceKey]
+ -[GTReplayFetchMLGraphData pipelineRef]
+ -[GTReplayFetchMLGraphData setDispatchUID:]
+ -[GTReplayFetchMLGraphData setMlModuleKey:]
+ -[GTReplayFetchMLGraphData setMlResourceKey:]
+ -[GTReplayFetchMLGraphData setPipelineRef:]
+ -[GTReplayFetchMLIntermediateData .cxx_destruct]
+ -[GTReplayFetchMLIntermediateData dispatchUID]
+ -[GTReplayFetchMLIntermediateData encodeWithCoder:]
+ -[GTReplayFetchMLIntermediateData initWithCoder:]
+ -[GTReplayFetchMLIntermediateData intermediateOps]
+ -[GTReplayFetchMLIntermediateData pipelineRef]
+ -[GTReplayFetchMLIntermediateData setDispatchUID:]
+ -[GTReplayFetchMLIntermediateData setIntermediateOps:]
+ -[GTReplayFetchMLIntermediateData setPipelineRef:]
+ -[GTReplayFetchPipelineBinaries dispatchUID]
+ -[GTReplayFetchPipelineBinaries encodeWithCoder:]
+ -[GTReplayFetchPipelineBinaries initWithCoder:]
+ -[GTReplayFetchPipelineBinaries setDispatchUID:]
+ -[GTReplayFetchPipelineBinaries setStreamRef:]
+ -[GTReplayFetchPipelineBinaries streamRef]
+ -[GTReplayFetchTensor dispatchUID]
+ -[GTReplayFetchTensor encodeWithCoder:]
+ -[GTReplayFetchTensor initWithCoder:]
+ -[GTReplayFetchTensor setDispatchUID:]
+ -[GTReplayFetchTensor setSlice:]
+ -[GTReplayFetchTensor setStreamRef:]
+ -[GTReplayFetchTensor slice]
+ -[GTReplayFetchTensor streamRef]
+ -[GTReplayRequest decodeXPCOnlyObjects:]
+ -[GTReplayRequest encodeXPCOnlyObjects:]
+ -[GTServiceProvider _registerService:forProcess:forPort:].cold.1
+ -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:]
+ -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:].cold.1
+ -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:].cold.2
+ -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:].cold.3
+ -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:].cold.4
+ -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:].cold.5
+ -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:].cold.6
+ -[GTURLAccessProvider copyIdentifier:toDevice:directory:completionHandler:]
+ -[GTURLAccessProviderXPCDispatcher copyIdentifier_toDevice_completionHandler_:replyConnection:].cold.1
+ -[GTURLAccessProviderXPCDispatcher copyIdentifier_toDevice_directory_completionHandler_:replyConnection:]
+ -[GTURLAccessProviderXPCDispatcher copyIdentifier_toDevice_directory_completionHandler_:replyConnection:].cold.1
+ -[GTURLAccessProviderXPCDispatcher copyIdentifier_toDevice_directory_completionHandler_:replyConnection:].cold.2
+ -[GTURLAccessProviderXPCProxy copyIdentifier:toDevice:directory:completionHandler:]
+ -[GTURLAccessProviderXPCProxy securityScopedURLFromSandboxID:completionHandler:].cold.1
+ _APP_SANDBOX_READ_WRITE
+ _ActivateServiceDaemonConnection
+ _CFDataGetBytePtr
+ _CompareUInt32
+ _ConnectToServiceDaemon
+ _DispatchCaptureBatchRequest
+ _Encode
+ _Encode.cold.1
+ _FinalizeCompressionStream.cold.1
+ _GTCapabilitiesSerializationCompressionAlgorithmDefault
+ _GTCoreLogUseOsLog
+ _GTCoreLog_getLogForTag.s_logs
+ _GTDecodeFunctionTypeShortString
+ _GTFenum_isSupported
+ _GTFileTransferCompressionAlgorithmToString
+ _GTFileWriterTransferFileEntries.cold.1
+ _GTFileWriterTransferFileEntries.cold.2
+ _GTFileWriterTransferFileEntries.cold.3
+ _GTMTLTensorExtentsDecode
+ _GTMTLTensorExtentsEncode
+ _GTMTLTensorSliceDecode
+ _GTMTLTensorSliceEncode
+ _GTTransportLaunchedProcessConnectionNew
+ _LocalArchiveURL
+ _MessageRemoteRoutingInfoGet
+ _MessageRemoteRoutingInfoSet
+ _NSClassFromString
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_GTDisplayRequest
+ _OBJC_CLASS_$_GTDisplayRequestToken
+ _OBJC_CLASS_$_GTDisplayResponse
+ _OBJC_CLASS_$_GTDisplayServiceXPCDispatcher
+ _OBJC_CLASS_$_GTDisplayServiceXPCProxy
+ _OBJC_CLASS_$_GTDisplayShowRequest
+ _OBJC_CLASS_$_GTDisplayShowTextureRequest
+ _OBJC_CLASS_$_GTDisplayUpdateOverlaysRequest
+ _OBJC_CLASS_$_GTDisplayUpdateRequest
+ _OBJC_CLASS_$_GTDisplayUpdateTerminationRequest
+ _OBJC_CLASS_$_GTDisplayUpdateWindowConfigurationRequest
+ _OBJC_CLASS_$_GTErrorReportServiceObserver
+ _OBJC_CLASS_$_GTErrorReportServiceReplyStream
+ _OBJC_CLASS_$_GTErrorReportServiceXPCDispatcher
+ _OBJC_CLASS_$_GTErrorReportServiceXPCProxy
+ _OBJC_CLASS_$_GTRejectedConnectionReport
+ _OBJC_CLASS_$_GTReplayDecodeGenericAccelerationStructure
+ _OBJC_CLASS_$_GTReplayFetchInto
+ _OBJC_CLASS_$_GTReplayFetchIntoRenderMask
+ _OBJC_CLASS_$_GTReplayFetchIntoTexture
+ _OBJC_CLASS_$_GTReplayFetchIntoWireframe
+ _OBJC_CLASS_$_GTReplayFetchMLGraph
+ _OBJC_CLASS_$_GTReplayFetchMLGraphData
+ _OBJC_CLASS_$_GTReplayFetchMLIntermediateData
+ _OBJC_CLASS_$_GTReplayFetchPipelineBinaries
+ _OBJC_CLASS_$_GTReplayFetchTensor
+ _OBJC_CLASS_$_MTLFXFrameInterpolatorDescriptor
+ _OBJC_CLASS_$_MTLFXTemporalDenoisedScalerDescriptor
+ _OBJC_CLASS_$_MTLSharedTextureHandle
+ _OBJC_IVAR_$_DYGTMTLDeviceProfile._version
+ _OBJC_IVAR_$_GTCaptureConfiguration._presentDownloadSize
+ _OBJC_IVAR_$_GTDisplayRequest._requestID
+ _OBJC_IVAR_$_GTDisplayRequestToken._requestID
+ _OBJC_IVAR_$_GTDisplayRequestToken._sem
+ _OBJC_IVAR_$_GTDisplayResponse._error
+ _OBJC_IVAR_$_GTDisplayResponse._requestID
+ _OBJC_IVAR_$_GTDisplayServiceXPCDispatcher._service
+ _OBJC_IVAR_$_GTDisplayServiceXPCProxy._connection
+ _OBJC_IVAR_$_GTDisplayServiceXPCProxy._ignoreMethods
+ _OBJC_IVAR_$_GTDisplayShowTextureRequest._depth
+ _OBJC_IVAR_$_GTDisplayShowTextureRequest._dispatchUID
+ _OBJC_IVAR_$_GTDisplayShowTextureRequest._height
+ _OBJC_IVAR_$_GTDisplayShowTextureRequest._level
+ _OBJC_IVAR_$_GTDisplayShowTextureRequest._pixelFormat
+ _OBJC_IVAR_$_GTDisplayShowTextureRequest._plane
+ _OBJC_IVAR_$_GTDisplayShowTextureRequest._replayServicePort
+ _OBJC_IVAR_$_GTDisplayShowTextureRequest._slice
+ _OBJC_IVAR_$_GTDisplayShowTextureRequest._streamRef
+ _OBJC_IVAR_$_GTDisplayShowTextureRequest._width
+ _OBJC_IVAR_$_GTDisplayUpdateOverlaysRequest._overlays
+ _OBJC_IVAR_$_GTDisplayUpdateTerminationRequest._connection
+ _OBJC_IVAR_$_GTDisplayUpdateTerminationRequest._path
+ _OBJC_IVAR_$_GTDisplayUpdateWindowConfigurationRequest._orientation
+ _OBJC_IVAR_$_GTDisplayUpdateWindowConfigurationRequest._visible
+ _OBJC_IVAR_$_GTDisplayUpdateWindowConfigurationRequest._windowTitle
+ _OBJC_IVAR_$_GTErrorReportServiceReplyStream._observer
+ _OBJC_IVAR_$_GTErrorReportServiceXPCDispatcher._service
+ _OBJC_IVAR_$_GTErrorReportServiceXPCProxy._connection
+ _OBJC_IVAR_$_GTErrorReportServiceXPCProxy._ignoreMethods
+ _OBJC_IVAR_$_GTErrorReportServiceXPCProxy._observerIdToPort
+ _OBJC_IVAR_$_GTLaunchRequest._disableDisplay
+ _OBJC_IVAR_$_GTLaunchRequest._preferXPCService
+ _OBJC_IVAR_$_GTMTLReplayServiceXPCProxy._deviceUDID
+ _OBJC_IVAR_$_GTMTLReplayServiceXPCProxy._servicePort
+ _OBJC_IVAR_$_GTMTLReplayServiceXPCProxy._version
+ _OBJC_IVAR_$_GTRejectedConnectionReport._name
+ _OBJC_IVAR_$_GTRejectedConnectionReport._pid
+ _OBJC_IVAR_$_GTRejectedConnectionReport._timestamp
+ _OBJC_IVAR_$_GTRelayedXPCConnection._routingInfo
+ _OBJC_IVAR_$_GTReplayConfiguration._enableLiveICBs
+ _OBJC_IVAR_$_GTReplayConfiguration._forceResourcesResident
+ _OBJC_IVAR_$_GTReplayDecodeGenericAccelerationStructure._dispatchUID
+ _OBJC_IVAR_$_GTReplayDecodeGenericAccelerationStructure._streamRef
+ _OBJC_IVAR_$_GTReplayFetchInto._dest
+ _OBJC_IVAR_$_GTReplayFetchInto._dispatchUID
+ _OBJC_IVAR_$_GTReplayFetchInto._event
+ _OBJC_IVAR_$_GTReplayFetchIntoTexture._depth
+ _OBJC_IVAR_$_GTReplayFetchIntoTexture._level
+ _OBJC_IVAR_$_GTReplayFetchIntoTexture._plane
+ _OBJC_IVAR_$_GTReplayFetchIntoTexture._resolveMultisampleTexture
+ _OBJC_IVAR_$_GTReplayFetchIntoTexture._slice
+ _OBJC_IVAR_$_GTReplayFetchIntoTexture._streamRef
+ _OBJC_IVAR_$_GTReplayFetchMLGraph._dispatchUID
+ _OBJC_IVAR_$_GTReplayFetchMLGraph._pipelineRef
+ _OBJC_IVAR_$_GTReplayFetchMLGraphData._dispatchUID
+ _OBJC_IVAR_$_GTReplayFetchMLGraphData._mlModuleKey
+ _OBJC_IVAR_$_GTReplayFetchMLGraphData._mlResourceKey
+ _OBJC_IVAR_$_GTReplayFetchMLGraphData._pipelineRef
+ _OBJC_IVAR_$_GTReplayFetchMLIntermediateData._dispatchUID
+ _OBJC_IVAR_$_GTReplayFetchMLIntermediateData._intermediateOps
+ _OBJC_IVAR_$_GTReplayFetchMLIntermediateData._pipelineRef
+ _OBJC_IVAR_$_GTReplayFetchPipelineBinaries._dispatchUID
+ _OBJC_IVAR_$_GTReplayFetchPipelineBinaries._streamRef
+ _OBJC_IVAR_$_GTReplayFetchTensor._dispatchUID
+ _OBJC_IVAR_$_GTReplayFetchTensor._slice
+ _OBJC_IVAR_$_GTReplayFetchTensor._streamRef
+ _OBJC_METACLASS_$_GTDisplayRequest
+ _OBJC_METACLASS_$_GTDisplayRequestToken
+ _OBJC_METACLASS_$_GTDisplayResponse
+ _OBJC_METACLASS_$_GTDisplayServiceXPCDispatcher
+ _OBJC_METACLASS_$_GTDisplayServiceXPCProxy
+ _OBJC_METACLASS_$_GTDisplayShowRequest
+ _OBJC_METACLASS_$_GTDisplayShowTextureRequest
+ _OBJC_METACLASS_$_GTDisplayUpdateOverlaysRequest
+ _OBJC_METACLASS_$_GTDisplayUpdateRequest
+ _OBJC_METACLASS_$_GTDisplayUpdateTerminationRequest
+ _OBJC_METACLASS_$_GTDisplayUpdateWindowConfigurationRequest
+ _OBJC_METACLASS_$_GTErrorReportServiceObserver
+ _OBJC_METACLASS_$_GTErrorReportServiceReplyStream
+ _OBJC_METACLASS_$_GTErrorReportServiceXPCDispatcher
+ _OBJC_METACLASS_$_GTErrorReportServiceXPCProxy
+ _OBJC_METACLASS_$_GTRejectedConnectionReport
+ _OBJC_METACLASS_$_GTReplayDecodeGenericAccelerationStructure
+ _OBJC_METACLASS_$_GTReplayFetchInto
+ _OBJC_METACLASS_$_GTReplayFetchIntoRenderMask
+ _OBJC_METACLASS_$_GTReplayFetchIntoTexture
+ _OBJC_METACLASS_$_GTReplayFetchIntoWireframe
+ _OBJC_METACLASS_$_GTReplayFetchMLGraph
+ _OBJC_METACLASS_$_GTReplayFetchMLGraphData
+ _OBJC_METACLASS_$_GTReplayFetchMLIntermediateData
+ _OBJC_METACLASS_$_GTReplayFetchPipelineBinaries
+ _OBJC_METACLASS_$_GTReplayFetchTensor
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _ProcessCompressionStream.cold.1
+ _ProxyCaptureBatchRequest
+ __CFURLCopySecurityScopeFromFileURL
+ __OBJC_$_CLASS_METHODS_GTDisplayRequest
+ __OBJC_$_CLASS_METHODS_GTDisplayResponse
+ __OBJC_$_CLASS_METHODS_GTDisplayShowTextureRequest
+ __OBJC_$_CLASS_METHODS_GTDisplayUpdateOverlaysRequest
+ __OBJC_$_CLASS_METHODS_GTDisplayUpdateTerminationRequest
+ __OBJC_$_CLASS_METHODS_GTDisplayUpdateWindowConfigurationRequest
+ __OBJC_$_CLASS_METHODS_GTRejectedConnectionReport
+ __OBJC_$_CLASS_METHODS_GTReplayDecodeGenericAccelerationStructure
+ __OBJC_$_CLASS_METHODS_GTReplayFetchInto
+ __OBJC_$_CLASS_METHODS_GTReplayFetchIntoTexture
+ __OBJC_$_CLASS_METHODS_GTReplayFetchMLGraph
+ __OBJC_$_CLASS_METHODS_GTReplayFetchMLGraphData
+ __OBJC_$_CLASS_METHODS_GTReplayFetchMLIntermediateData
+ __OBJC_$_CLASS_METHODS_GTReplayFetchPipelineBinaries
+ __OBJC_$_CLASS_METHODS_GTReplayFetchTensor
+ __OBJC_$_CLASS_PROP_LIST_GTDisplayRequest
+ __OBJC_$_CLASS_PROP_LIST_GTDisplayResponse
+ __OBJC_$_CLASS_PROP_LIST_GTDisplayShowRequest
+ __OBJC_$_CLASS_PROP_LIST_GTDisplayShowTextureRequest
+ __OBJC_$_CLASS_PROP_LIST_GTDisplayUpdateOverlaysRequest
+ __OBJC_$_CLASS_PROP_LIST_GTDisplayUpdateRequest
+ __OBJC_$_CLASS_PROP_LIST_GTDisplayUpdateTerminationRequest
+ __OBJC_$_CLASS_PROP_LIST_GTDisplayUpdateWindowConfigurationRequest
+ __OBJC_$_CLASS_PROP_LIST_GTRejectedConnectionReport
+ __OBJC_$_CLASS_PROP_LIST_GTReplayDecodeGenericAccelerationStructure
+ __OBJC_$_CLASS_PROP_LIST_GTReplayFetchInto
+ __OBJC_$_CLASS_PROP_LIST_GTReplayFetchMLGraph
+ __OBJC_$_CLASS_PROP_LIST_GTReplayFetchMLGraphData
+ __OBJC_$_CLASS_PROP_LIST_GTReplayFetchMLIntermediateData
+ __OBJC_$_CLASS_PROP_LIST_GTReplayFetchPipelineBinaries
+ __OBJC_$_CLASS_PROP_LIST_GTReplayFetchTensor
+ __OBJC_$_INSTANCE_METHODS_GTDisplayRequest
+ __OBJC_$_INSTANCE_METHODS_GTDisplayRequestToken
+ __OBJC_$_INSTANCE_METHODS_GTDisplayResponse
+ __OBJC_$_INSTANCE_METHODS_GTDisplayServiceXPCDispatcher
+ __OBJC_$_INSTANCE_METHODS_GTDisplayServiceXPCProxy
+ __OBJC_$_INSTANCE_METHODS_GTDisplayShowTextureRequest
+ __OBJC_$_INSTANCE_METHODS_GTDisplayUpdateOverlaysRequest
+ __OBJC_$_INSTANCE_METHODS_GTDisplayUpdateTerminationRequest
+ __OBJC_$_INSTANCE_METHODS_GTDisplayUpdateWindowConfigurationRequest
+ __OBJC_$_INSTANCE_METHODS_GTErrorReportServiceObserver
+ __OBJC_$_INSTANCE_METHODS_GTErrorReportServiceReplyStream
+ __OBJC_$_INSTANCE_METHODS_GTErrorReportServiceXPCDispatcher
+ __OBJC_$_INSTANCE_METHODS_GTErrorReportServiceXPCProxy
+ __OBJC_$_INSTANCE_METHODS_GTRejectedConnectionReport
+ __OBJC_$_INSTANCE_METHODS_GTReplayDecodeGenericAccelerationStructure
+ __OBJC_$_INSTANCE_METHODS_GTReplayFetchInto
+ __OBJC_$_INSTANCE_METHODS_GTReplayFetchIntoTexture
+ __OBJC_$_INSTANCE_METHODS_GTReplayFetchMLGraph
+ __OBJC_$_INSTANCE_METHODS_GTReplayFetchMLGraphData
+ __OBJC_$_INSTANCE_METHODS_GTReplayFetchMLIntermediateData
+ __OBJC_$_INSTANCE_METHODS_GTReplayFetchPipelineBinaries
+ __OBJC_$_INSTANCE_METHODS_GTReplayFetchTensor
+ __OBJC_$_INSTANCE_VARIABLES_GTDisplayRequest
+ __OBJC_$_INSTANCE_VARIABLES_GTDisplayRequestToken
+ __OBJC_$_INSTANCE_VARIABLES_GTDisplayResponse
+ __OBJC_$_INSTANCE_VARIABLES_GTDisplayServiceXPCDispatcher
+ __OBJC_$_INSTANCE_VARIABLES_GTDisplayServiceXPCProxy
+ __OBJC_$_INSTANCE_VARIABLES_GTDisplayShowTextureRequest
+ __OBJC_$_INSTANCE_VARIABLES_GTDisplayUpdateOverlaysRequest
+ __OBJC_$_INSTANCE_VARIABLES_GTDisplayUpdateTerminationRequest
+ __OBJC_$_INSTANCE_VARIABLES_GTDisplayUpdateWindowConfigurationRequest
+ __OBJC_$_INSTANCE_VARIABLES_GTErrorReportServiceReplyStream
+ __OBJC_$_INSTANCE_VARIABLES_GTErrorReportServiceXPCDispatcher
+ __OBJC_$_INSTANCE_VARIABLES_GTErrorReportServiceXPCProxy
+ __OBJC_$_INSTANCE_VARIABLES_GTRejectedConnectionReport
+ __OBJC_$_INSTANCE_VARIABLES_GTReplayDecodeGenericAccelerationStructure
+ __OBJC_$_INSTANCE_VARIABLES_GTReplayFetchInto
+ __OBJC_$_INSTANCE_VARIABLES_GTReplayFetchIntoTexture
+ __OBJC_$_INSTANCE_VARIABLES_GTReplayFetchMLGraph
+ __OBJC_$_INSTANCE_VARIABLES_GTReplayFetchMLGraphData
+ __OBJC_$_INSTANCE_VARIABLES_GTReplayFetchMLIntermediateData
+ __OBJC_$_INSTANCE_VARIABLES_GTReplayFetchPipelineBinaries
+ __OBJC_$_INSTANCE_VARIABLES_GTReplayFetchTensor
+ __OBJC_$_PROP_LIST_GTDisplayRequest
+ __OBJC_$_PROP_LIST_GTDisplayRequestToken
+ __OBJC_$_PROP_LIST_GTDisplayResponse
+ __OBJC_$_PROP_LIST_GTDisplayShowTextureRequest
+ __OBJC_$_PROP_LIST_GTDisplayUpdateOverlaysRequest
+ __OBJC_$_PROP_LIST_GTDisplayUpdateTerminationRequest
+ __OBJC_$_PROP_LIST_GTDisplayUpdateWindowConfigurationRequest
+ __OBJC_$_PROP_LIST_GTRejectedConnectionReport
+ __OBJC_$_PROP_LIST_GTReplayDecodeGenericAccelerationStructure
+ __OBJC_$_PROP_LIST_GTReplayFetchInto
+ __OBJC_$_PROP_LIST_GTReplayFetchIntoTexture
+ __OBJC_$_PROP_LIST_GTReplayFetchMLGraph
+ __OBJC_$_PROP_LIST_GTReplayFetchMLGraphData
+ __OBJC_$_PROP_LIST_GTReplayFetchMLIntermediateData
+ __OBJC_$_PROP_LIST_GTReplayFetchPipelineBinaries
+ __OBJC_$_PROP_LIST_GTReplayFetchTensor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GTDisplayService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GTDisplayServiceXPCDispatcher
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GTErrorReportService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GTErrorReportServiceObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GTErrorReportServiceObserverXPCDispatcher
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GTErrorReportServiceXPCDispatcher
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GTObservableService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GTObserverXPCDispatcher
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GTDisplayService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GTDisplayServiceXPCDispatcher
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GTErrorReportService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GTErrorReportServiceObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GTErrorReportServiceObserverXPCDispatcher
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GTErrorReportServiceXPCDispatcher
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GTObservableService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GTObserverXPCDispatcher
+ __OBJC_$_PROTOCOL_REFS_GTErrorReportService
+ __OBJC_$_PROTOCOL_REFS_GTErrorReportServiceXPCDispatcher
+ __OBJC_$_PROTOCOL_REFS_GTMTLCaptureService
+ __OBJC_$_PROTOCOL_REFS_GTMTLDiagnosticsService
+ __OBJC_$_PROTOCOL_REFS_GTMTLReplayService
+ __OBJC_$_PROTOCOL_REFS_GTMTLTelemetryService
+ __OBJC_$_PROTOCOL_REFS_GTRemoteDeviceBrowser
+ __OBJC_$_PROTOCOL_REFS_GTServiceProvider
+ __OBJC_CLASS_PROTOCOLS_$_GTDisplayRequest
+ __OBJC_CLASS_PROTOCOLS_$_GTDisplayResponse
+ __OBJC_CLASS_PROTOCOLS_$_GTDisplayServiceXPCDispatcher
+ __OBJC_CLASS_PROTOCOLS_$_GTDisplayServiceXPCProxy
+ __OBJC_CLASS_PROTOCOLS_$_GTDisplayShowRequest
+ __OBJC_CLASS_PROTOCOLS_$_GTDisplayShowTextureRequest
+ __OBJC_CLASS_PROTOCOLS_$_GTDisplayUpdateOverlaysRequest
+ __OBJC_CLASS_PROTOCOLS_$_GTDisplayUpdateRequest
+ __OBJC_CLASS_PROTOCOLS_$_GTDisplayUpdateTerminationRequest
+ __OBJC_CLASS_PROTOCOLS_$_GTDisplayUpdateWindowConfigurationRequest
+ __OBJC_CLASS_PROTOCOLS_$_GTErrorReportServiceObserver
+ __OBJC_CLASS_PROTOCOLS_$_GTErrorReportServiceReplyStream
+ __OBJC_CLASS_PROTOCOLS_$_GTErrorReportServiceXPCDispatcher
+ __OBJC_CLASS_PROTOCOLS_$_GTErrorReportServiceXPCProxy
+ __OBJC_CLASS_PROTOCOLS_$_GTObservableService
+ __OBJC_CLASS_PROTOCOLS_$_GTRejectedConnectionReport
+ __OBJC_CLASS_PROTOCOLS_$_GTReplayDecodeGenericAccelerationStructure
+ __OBJC_CLASS_PROTOCOLS_$_GTReplayFetchInto
+ __OBJC_CLASS_PROTOCOLS_$_GTReplayFetchMLGraph
+ __OBJC_CLASS_PROTOCOLS_$_GTReplayFetchMLGraphData
+ __OBJC_CLASS_PROTOCOLS_$_GTReplayFetchMLIntermediateData
+ __OBJC_CLASS_PROTOCOLS_$_GTReplayFetchPipelineBinaries
+ __OBJC_CLASS_PROTOCOLS_$_GTReplayFetchTensor
+ __OBJC_CLASS_RO_$_GTDisplayRequest
+ __OBJC_CLASS_RO_$_GTDisplayRequestToken
+ __OBJC_CLASS_RO_$_GTDisplayResponse
+ __OBJC_CLASS_RO_$_GTDisplayServiceXPCDispatcher
+ __OBJC_CLASS_RO_$_GTDisplayServiceXPCProxy
+ __OBJC_CLASS_RO_$_GTDisplayShowRequest
+ __OBJC_CLASS_RO_$_GTDisplayShowTextureRequest
+ __OBJC_CLASS_RO_$_GTDisplayUpdateOverlaysRequest
+ __OBJC_CLASS_RO_$_GTDisplayUpdateRequest
+ __OBJC_CLASS_RO_$_GTDisplayUpdateTerminationRequest
+ __OBJC_CLASS_RO_$_GTDisplayUpdateWindowConfigurationRequest
+ __OBJC_CLASS_RO_$_GTErrorReportServiceObserver
+ __OBJC_CLASS_RO_$_GTErrorReportServiceReplyStream
+ __OBJC_CLASS_RO_$_GTErrorReportServiceXPCDispatcher
+ __OBJC_CLASS_RO_$_GTErrorReportServiceXPCProxy
+ __OBJC_CLASS_RO_$_GTRejectedConnectionReport
+ __OBJC_CLASS_RO_$_GTReplayDecodeGenericAccelerationStructure
+ __OBJC_CLASS_RO_$_GTReplayFetchInto
+ __OBJC_CLASS_RO_$_GTReplayFetchIntoRenderMask
+ __OBJC_CLASS_RO_$_GTReplayFetchIntoTexture
+ __OBJC_CLASS_RO_$_GTReplayFetchIntoWireframe
+ __OBJC_CLASS_RO_$_GTReplayFetchMLGraph
+ __OBJC_CLASS_RO_$_GTReplayFetchMLGraphData
+ __OBJC_CLASS_RO_$_GTReplayFetchMLIntermediateData
+ __OBJC_CLASS_RO_$_GTReplayFetchPipelineBinaries
+ __OBJC_CLASS_RO_$_GTReplayFetchTensor
+ __OBJC_LABEL_PROTOCOL_$_GTDisplayService
+ __OBJC_LABEL_PROTOCOL_$_GTDisplayServiceXPCDispatcher
+ __OBJC_LABEL_PROTOCOL_$_GTErrorReportService
+ __OBJC_LABEL_PROTOCOL_$_GTErrorReportServiceObserver
+ __OBJC_LABEL_PROTOCOL_$_GTErrorReportServiceObserverXPCDispatcher
+ __OBJC_LABEL_PROTOCOL_$_GTErrorReportServiceXPCDispatcher
+ __OBJC_LABEL_PROTOCOL_$_GTObservableService
+ __OBJC_LABEL_PROTOCOL_$_GTObserverXPCDispatcher
+ __OBJC_METACLASS_RO_$_GTDisplayRequest
+ __OBJC_METACLASS_RO_$_GTDisplayRequestToken
+ __OBJC_METACLASS_RO_$_GTDisplayResponse
+ __OBJC_METACLASS_RO_$_GTDisplayServiceXPCDispatcher
+ __OBJC_METACLASS_RO_$_GTDisplayServiceXPCProxy
+ __OBJC_METACLASS_RO_$_GTDisplayShowRequest
+ __OBJC_METACLASS_RO_$_GTDisplayShowTextureRequest
+ __OBJC_METACLASS_RO_$_GTDisplayUpdateOverlaysRequest
+ __OBJC_METACLASS_RO_$_GTDisplayUpdateRequest
+ __OBJC_METACLASS_RO_$_GTDisplayUpdateTerminationRequest
+ __OBJC_METACLASS_RO_$_GTDisplayUpdateWindowConfigurationRequest
+ __OBJC_METACLASS_RO_$_GTErrorReportServiceObserver
+ __OBJC_METACLASS_RO_$_GTErrorReportServiceReplyStream
+ __OBJC_METACLASS_RO_$_GTErrorReportServiceXPCDispatcher
+ __OBJC_METACLASS_RO_$_GTErrorReportServiceXPCProxy
+ __OBJC_METACLASS_RO_$_GTRejectedConnectionReport
+ __OBJC_METACLASS_RO_$_GTReplayDecodeGenericAccelerationStructure
+ __OBJC_METACLASS_RO_$_GTReplayFetchInto
+ __OBJC_METACLASS_RO_$_GTReplayFetchIntoRenderMask
+ __OBJC_METACLASS_RO_$_GTReplayFetchIntoTexture
+ __OBJC_METACLASS_RO_$_GTReplayFetchIntoWireframe
+ __OBJC_METACLASS_RO_$_GTReplayFetchMLGraph
+ __OBJC_METACLASS_RO_$_GTReplayFetchMLGraphData
+ __OBJC_METACLASS_RO_$_GTReplayFetchMLIntermediateData
+ __OBJC_METACLASS_RO_$_GTReplayFetchPipelineBinaries
+ __OBJC_METACLASS_RO_$_GTReplayFetchTensor
+ __OBJC_PROTOCOL_$_GTDisplayService
+ __OBJC_PROTOCOL_$_GTDisplayServiceXPCDispatcher
+ __OBJC_PROTOCOL_$_GTErrorReportService
+ __OBJC_PROTOCOL_$_GTErrorReportServiceObserver
+ __OBJC_PROTOCOL_$_GTErrorReportServiceObserverXPCDispatcher
+ __OBJC_PROTOCOL_$_GTErrorReportServiceXPCDispatcher
+ __OBJC_PROTOCOL_$_GTObservableService
+ __OBJC_PROTOCOL_$_GTObserverXPCDispatcher
+ __OBJC_PROTOCOL_REFERENCE_$_GTDisplayService
+ __OBJC_PROTOCOL_REFERENCE_$_GTErrorReportService
+ __OBJC_PROTOCOL_REFERENCE_$_GTErrorReportServiceObserver
+ ___103-[GTFileWriterServiceXPCProxy startTransfer:basePath:fromDevice:toDirectory:options:completionHandler:]_block_invoke
+ ___105-[GTURLAccessProviderXPCDispatcher copyIdentifier_toDevice_directory_completionHandler_:replyConnection:]_block_invoke
+ ___113-[GTFileWriterService beginTransferSessionWithFileEntries:basePath:toDevice:options:sessionID:completionHandler:]_block_invoke.262
+ ___113-[GTFileWriterService beginTransferSessionWithFileEntries:basePath:toDevice:options:sessionID:completionHandler:]_block_invoke.262.cold.1
+ ___113-[GTFileWriterService beginTransferSessionWithFileEntries:basePath:toDevice:options:sessionID:completionHandler:]_block_invoke.270
+ ___113-[GTFileWriterService beginTransferSessionWithFileEntries:basePath:toDevice:options:sessionID:completionHandler:]_block_invoke.cold.1
+ ___125-[GTFileWriterServiceXPCDispatcher startTransfer_basePath_fromDevice_toDirectory_options_completionHandler_:replyConnection:]_block_invoke
+ ___42-[GTMTLReplayServiceXPCProxy shaderdebug:]_block_invoke_2
+ ___42-[GTMTLReplayServiceXPCProxy shaderdebug:]_block_invoke_3
+ ___57-[GTErrorReportServiceXPCProxy fetchRejectedConnections:]_block_invoke
+ ___58-[GTErrorReportServiceXPCProxy returnRejectedConnections:]_block_invoke
+ ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke.70
+ ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke.70.cold.1
+ ___73-[GTDisplayServiceXPCDispatcher show_completionHandler_:replyConnection:]_block_invoke
+ ___73-[GTDisplayServiceXPCDispatcher show_completionHandler_:replyConnection:]_block_invoke.cold.1
+ ___75-[GTDisplayServiceXPCDispatcher update_completionHandler_:replyConnection:]_block_invoke
+ ___75-[GTDisplayServiceXPCDispatcher update_completionHandler_:replyConnection:]_block_invoke.cold.1
+ ___79-[GTErrorReportServiceXPCDispatcher fetchRejectedConnections_:replyConnection:]_block_invoke
+ ___83-[GTURLAccessProviderXPCProxy copyIdentifier:toDevice:directory:completionHandler:]_block_invoke
+ ___89-[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:]_block_invoke
+ ___89-[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:]_block_invoke.115
+ ___89-[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:]_block_invoke_2
+ ___95-[GTFileWriterService startTransfer:basePath:fromDevice:toDirectory:options:completionHandler:]_block_invoke
+ ___95-[GTFileWriterService startTransfer:basePath:fromDevice:toDirectory:options:completionHandler:]_block_invoke.cold.1
+ ___95-[GTFileWriterService startTransfer:basePath:fromDevice:toDirectory:options:completionHandler:]_block_invoke.cold.2
+ ___95-[GTFileWriterService startTransfer:basePath:fromDevice:toDirectory:options:completionHandler:]_block_invoke.cold.3
+ ___95-[GTFileWriterService startTransfer:basePath:fromDevice:toDirectory:options:completionHandler:]_block_invoke.cold.4
+ ___ActivateServiceDaemonConnection_block_invoke
+ ___ActivateServiceDaemonConnection_block_invoke_2
+ ___ActivateServiceDaemonConnection_block_invoke_2.cold.1
+ ___ActivateServiceDaemonConnection_block_invoke_2.cold.2
+ ___DeleteAllArchives_block_invoke
+ ___DeleteAllArchives_block_invoke.cold.1
+ ___DispatchCaptureBatchRequest_block_invoke
+ ___DispatchCaptureBatchRequest_block_invoke_2
+ ___Encode_block_invoke
+ ___Encode_block_invoke.cold.1
+ ___GTCoreLog_getLogForTag_block_invoke
+ ___ProxyCaptureBatchRequest_block_invoke
+ ___block_descriptor_44_e5_v8?0l
+ ___block_descriptor_48_8_32r40r_e27_B24?0"NSURL"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_8_32r_e36_B24?0Q8"NSObject<OS_xpc_object>"16lr32l8
+ ___block_descriptor_48_8_32s40bs_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_8_32s40s_e27_v16?0"GTCaptureResponse"8ls32l8s40l8
+ ___block_descriptor_48_8_32s40s_e27_v16?0"GTDisplayResponse"8ls32l8s40l8
+ ___block_descriptor_48_8_32s40s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_8_32s40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_8_32s40s48bs_e15_v16?0"NSURL"8ls48l8s32l8s40l8
+ ___block_descriptor_56_8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_56_8_32s40s48bs_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_8_32s40s48w_e34_v16?0"GTCaptureCompletionState"8lw48l8s32l8s40l8
+ ___block_descriptor_64_8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_64_8_32s40s48s56bs_e17_v16?0"NSError"8ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_8_32s40s48s56bs_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_8_32s40s48s56s_e8_v16?0Q8ls32l8s40l8s48l8s56l8
+ ___stderrp
+ ___stdoutp
+ __os_log_disabled
+ _chown
+ _fprintf
+ _gt_tagged_log
+ _nextRequestID
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$bufferRobustnessSupport
+ _objc_msgSend$code
+ _objc_msgSend$copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:
+ _objc_msgSend$copyIdentifier:toDevice:directory:completionHandler:
+ _objc_msgSend$createMachPort
+ _objc_msgSend$decodeTopLevelObjectOfClass:forKey:error:
+ _objc_msgSend$decodeXPCOnlyObjects:
+ _objc_msgSend$defaultTextureWriteRoundingMode
+ _objc_msgSend$device
+ _objc_msgSend$deviceCreationFlags
+ _objc_msgSend$domain
+ _objc_msgSend$encodeXPCOnlyObjects:
+ _objc_msgSend$eventPort
+ _objc_msgSend$fetchInto:
+ _objc_msgSend$fetchRejectedConnections:
+ _objc_msgSend$initWithID:
+ _objc_msgSend$initWithMachPort:
+ _objc_msgSend$initWithTransactionScopedXPCConnection:messageQueue:
+ _objc_msgSend$isQuadDataSharingSupported
+ _objc_msgSend$latestSupportedGenericBVHVersion
+ _objc_msgSend$limits
+ _objc_msgSend$maxAccelerationStructureTraversalDepth
+ _objc_msgSend$maxRasterizationRateLayerCount
+ _objc_msgSend$newSharedEventHandle
+ _objc_msgSend$newSharedEventWithMachPort:
+ _objc_msgSend$newSharedTextureHandle
+ _objc_msgSend$newSharedTextureWithHandle:
+ _objc_msgSend$notifyRejectedConnections:
+ _objc_msgSend$programData
+ _objc_msgSend$requiresBFloat16Emulation
+ _objc_msgSend$setProgramData:
+ _objc_msgSend$show:completionHandler:
+ _objc_msgSend$sparseTexturesSupport
+ _objc_msgSend$startTransfer:basePath:fromDevice:toDirectory:options:completionHandler:
+ _objc_msgSend$supportPriorityBand
+ _objc_msgSend$supportedInputContentMaxScaleForDevice:
+ _objc_msgSend$supportedInputContentMinScaleForDevice:
+ _objc_msgSend$supports32BitFloatFiltering
+ _objc_msgSend$supportsAnisoSampleFix
+ _objc_msgSend$supportsArrayOfSamplers
+ _objc_msgSend$supportsArrayOfTextures
+ _objc_msgSend$supportsAtomicUlongVoidMinMax
+ _objc_msgSend$supportsBaseVertexInstanceDrawing
+ _objc_msgSend$supportsBfloat16Buffers
+ _objc_msgSend$supportsBinaryArchives
+ _objc_msgSend$supportsBufferBoundsChecking
+ _objc_msgSend$supportsBufferPrefetchStatistics
+ _objc_msgSend$supportsCommandBufferJump
+ _objc_msgSend$supportsCompressedTextureViewSPI
+ _objc_msgSend$supportsComputeCompressedTextureWrite
+ _objc_msgSend$supportsCountingOcclusionQuery
+ _objc_msgSend$supportsDeadlineProfile
+ _objc_msgSend$supportsDevicePartitioning
+ _objc_msgSend$supportsDynamicControlPointCount
+ _objc_msgSend$supportsExplicitVisibilityGroups
+ _objc_msgSend$supportsFP32TessFactors
+ _objc_msgSend$supportsFastMathInfNaNPropagation
+ _objc_msgSend$supportsFillTexture
+ _objc_msgSend$supportsFixedLinePointFillDepthGradient
+ _objc_msgSend$supportsFloat16BCubicFiltering
+ _objc_msgSend$supportsFloat16InfNanFiltering
+ _objc_msgSend$supportsForceSeamsOnCubemaps
+ _objc_msgSend$supportsForkJoin
+ _objc_msgSend$supportsFragmentBufferWrites
+ _objc_msgSend$supportsFragmentOnlyEncoders
+ _objc_msgSend$supportsIABHashForTools
+ _objc_msgSend$supportsImageBlockSampleCoverageControl
+ _objc_msgSend$supportsImageBlocks
+ _objc_msgSend$supportsIndirectStageInRegion
+ _objc_msgSend$supportsIndirectTessellation
+ _objc_msgSend$supportsIndirectTextures
+ _objc_msgSend$supportsIndirectWritableTextures
+ _objc_msgSend$supportsInt64
+ _objc_msgSend$supportsInterchangeTiled
+ _objc_msgSend$supportsIntersectionFunctionBuffers
+ _objc_msgSend$supportsInvariantVertexPosition
+ _objc_msgSend$supportsLargeFramebufferConfigs
+ _objc_msgSend$supportsMemoryOrderAtomics
+ _objc_msgSend$supportsMipLevelsSmallerThanBlockSize
+ _objc_msgSend$supportsMutableTier1ArgumentBuffers
+ _objc_msgSend$supportsNativeHardwareFP16
+ _objc_msgSend$supportsNonZeroTextureWriteLOD
+ _objc_msgSend$supportsNorm16BCubicFiltering
+ _objc_msgSend$supportsOpenCLTextureWriteSwizzles
+ _objc_msgSend$supportsPacked32TextureBufferWrites
+ _objc_msgSend$supportsPerformanceStateAssertion
+ _objc_msgSend$supportsPipelineLibraries
+ _objc_msgSend$supportsPostDepthCoverage
+ _objc_msgSend$supportsPrimitiveRestartOverride
+ _objc_msgSend$supportsPrimitiveType:
+ _objc_msgSend$supportsProgrammableBlending
+ _objc_msgSend$supportsPullModelInterpolation
+ _objc_msgSend$supportsQuadGroup
+ _objc_msgSend$supportsQuadReduction
+ _objc_msgSend$supportsQuadShufflesAndBroadcast
+ _objc_msgSend$supportsQueryTextureLOD
+ _objc_msgSend$supportsRTZRounding
+ _objc_msgSend$supportsRasterOrderGroups
+ _objc_msgSend$supportsRasterOrderGroupsColorAttachment
+ _objc_msgSend$supportsRayTracingTraversalMetrics
+ _objc_msgSend$supportsRaytracingFromRender
+ _objc_msgSend$supportsReadWriteBufferArguments
+ _objc_msgSend$supportsReadWriteTextureArguments
+ _objc_msgSend$supportsReadWriteTextureArgumentsTier2
+ _objc_msgSend$supportsReadWriteTextureCubeArguments
+ _objc_msgSend$supportsRenderPassWithoutRenderTarget
+ _objc_msgSend$supportsRenderTextureWrites
+ _objc_msgSend$supportsSIMDGroup
+ _objc_msgSend$supportsSIMDGroupMatrix
+ _objc_msgSend$supportsSIMDReduction
+ _objc_msgSend$supportsSIMDShuffleAndFill
+ _objc_msgSend$supportsSIMDShufflesAndBroadcast
+ _objc_msgSend$supportsSeparateVisibilityAndShadingRate
+ _objc_msgSend$supportsSetThreadgroupPackingDisabled
+ _objc_msgSend$supportsShaderBarycentricCoordinates
+ _objc_msgSend$supportsShaderLODAverage
+ _objc_msgSend$supportsShaderMinLODClamp
+ _objc_msgSend$supportsStackOverflowErrorCode
+ _objc_msgSend$supportsStencilFeedback
+ _objc_msgSend$supportsStreamingCodecSignaling
+ _objc_msgSend$supportsTessellation
+ _objc_msgSend$supportsTextureOutOfBoundsReads
+ _objc_msgSend$supportsTextureWriteRoundingMode:
+ _objc_msgSend$supportsUnalignedVertexFetch
+ _objc_msgSend$supportsVirtualSubstreams
+ _objc_msgSend$supportsWritableArrayOfTextures
+ _objc_msgSend$takeUploadedDataForHandle:
+ _objc_msgSend$update:completionHandler:
+ _objc_msgSend$uploadData:completionHandler:
+ _objc_release_x1
+ _objc_setProperty_atomic
+ _protocol_copyProtocolList
+ _qsort
+ _readlink
+ _s_tagInfo
+ _stat
+ _xpc_array_get_dictionary
+ _xpc_dictionary_copy_mach_send
+ _xpc_dictionary_get_count
+ _xpc_dictionary_get_nsobject_any
+ _xpc_dictionary_set_mach_send
- +[GTProfileInfo supportsSecureCoding]
- -[GTMTLCaptureServiceXPCProxy stop].cold.1
- -[GTProfileInfo .cxx_destruct]
- -[GTProfileInfo activePerEncoderDrawCallCount]
- -[GTProfileInfo analyzeBinaries]
- -[GTProfileInfo batchFilteredDerivedCounters]
- -[GTProfileInfo blitEncoderIndices]
- -[GTProfileInfo counterConfig]
- -[GTProfileInfo counters]
- -[GTProfileInfo derivedCounterData]
- -[GTProfileInfo derivedCounterInfo]
- -[GTProfileInfo encodeWithCoder:]
- -[GTProfileInfo encoderBatchPriorityList]
- -[GTProfileInfo gpuState]
- -[GTProfileInfo gpuTarget]
- -[GTProfileInfo highPriorityBatchInfo]
- -[GTProfileInfo highPriorityBatches]
- -[GTProfileInfo initFromProfileInfo:]
- -[GTProfileInfo initWithCoder:]
- -[GTProfileInfo metalPluginName]
- -[GTProfileInfo pause]
- -[GTProfileInfo perCommandBufferEncoderCount]
- -[GTProfileInfo perEncoderDrawCallCount]
- -[GTProfileInfo perEncoderIndexDrawCallCount]
- -[GTProfileInfo perEncoderKickCount]
- -[GTProfileInfo perFrameCommandBufferCount]
- -[GTProfileInfo profileCounters]
- -[GTProfileInfo profilingConfig]
- -[GTProfileInfo resume]
- -[GTProfileInfo setActivePerEncoderDrawCallCount:]
- -[GTProfileInfo setAnalyzeBinaries:]
- -[GTProfileInfo setBatchFilteredDerivedCounters:]
- -[GTProfileInfo setBlitEncoderIndices:]
- -[GTProfileInfo setCounterConfig:]
- -[GTProfileInfo setCounters:]
- -[GTProfileInfo setDerivedCounterData:]
- -[GTProfileInfo setDerivedCounterInfo:]
- -[GTProfileInfo setEncoderBatchPriorityList:]
- -[GTProfileInfo setGpuState:]
- -[GTProfileInfo setGpuTarget:]
- -[GTProfileInfo setHighPriorityBatchInfo:]
- -[GTProfileInfo setHighPriorityBatches:]
- -[GTProfileInfo setMetalPluginName:]
- -[GTProfileInfo setPause:]
- -[GTProfileInfo setPerCommandBufferEncoderCount:]
- -[GTProfileInfo setPerEncoderDrawCallCount:]
- -[GTProfileInfo setPerEncoderIndexDrawCallCount:]
- -[GTProfileInfo setPerEncoderKickCount:]
- -[GTProfileInfo setPerFrameCommandBufferCount:]
- -[GTProfileInfo setProfileCounters:]
- -[GTProfileInfo setProfilingConfig:]
- -[GTProfileInfo setResume:]
- -[GTProfileInfo setSplitEncoderCommandCount:]
- -[GTProfileInfo setSplitPerEncoderKickCount:]
- -[GTProfileInfo setTimelineConfig:]
- -[GTProfileInfo setTotalDrawCallCount:]
- -[GTProfileInfo setUseOverlap:]
- -[GTProfileInfo setWithoutBlitEncoderToDrawCallCountDict:]
- -[GTProfileInfo setXpState:]
- -[GTProfileInfo splitEncoderCommandCount]
- -[GTProfileInfo splitPerEncoderKickCount]
- -[GTProfileInfo timelineConfig]
- -[GTProfileInfo toDictionary]
- -[GTProfileInfo totalDrawCallCount]
- -[GTProfileInfo useOverlap]
- -[GTProfileInfo withoutBlitEncoderToDrawCallCountDict]
- -[GTProfileInfo xpState]
- -[GTRelayedXPCConnection initWithConnection:]
- -[GTRelayedXPCConnection initWithConnection:relayPort:relayPid:]
- -[GTRelayedXPCConnection updateRelayPort:pid:]
- -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:]
- -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:].cold.1
- -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:].cold.2
- -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:].cold.3
- -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:].cold.4
- -[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:].cold.5
- _GetPathRelativeToBase
- _OBJC_CLASS_$_GTProfileInfo
- _OBJC_IVAR_$_GTBulkDataService._log
- _OBJC_IVAR_$_GTBulkDataServiceXPCProxy._log
- _OBJC_IVAR_$_GTFileWriterService._log
- _OBJC_IVAR_$_GTFileWriterSessionUncompressed._log
- _OBJC_IVAR_$_GTLoopbackService._log
- _OBJC_IVAR_$_GTMTLCaptureServiceXPCProxy._log
- _OBJC_IVAR_$_GTMTLDiagnosticsService._log
- _OBJC_IVAR_$_GTMTLReplayServiceXPCDispatcher._log
- _OBJC_IVAR_$_GTMTLReplayServiceXPCProxy._log
- _OBJC_IVAR_$_GTMTLTelemetryServiceXPCProxy._log
- _OBJC_IVAR_$_GTProfileInfo._activePerEncoderDrawCallCount
- _OBJC_IVAR_$_GTProfileInfo._analyzeBinaries
- _OBJC_IVAR_$_GTProfileInfo._batchFilteredDerivedCounters
- _OBJC_IVAR_$_GTProfileInfo._blitEncoderIndices
- _OBJC_IVAR_$_GTProfileInfo._counterConfig
- _OBJC_IVAR_$_GTProfileInfo._counters
- _OBJC_IVAR_$_GTProfileInfo._derivedCounterData
- _OBJC_IVAR_$_GTProfileInfo._derivedCounterInfo
- _OBJC_IVAR_$_GTProfileInfo._encoderBatchPriorityList
- _OBJC_IVAR_$_GTProfileInfo._gpuState
- _OBJC_IVAR_$_GTProfileInfo._gpuTarget
- _OBJC_IVAR_$_GTProfileInfo._highPriorityBatchInfo
- _OBJC_IVAR_$_GTProfileInfo._highPriorityBatches
- _OBJC_IVAR_$_GTProfileInfo._metalPluginName
- _OBJC_IVAR_$_GTProfileInfo._pause
- _OBJC_IVAR_$_GTProfileInfo._perCommandBufferEncoderCount
- _OBJC_IVAR_$_GTProfileInfo._perEncoderDrawCallCount
- _OBJC_IVAR_$_GTProfileInfo._perEncoderIndexDrawCallCount
- _OBJC_IVAR_$_GTProfileInfo._perEncoderKickCount
- _OBJC_IVAR_$_GTProfileInfo._perFrameCommandBufferCount
- _OBJC_IVAR_$_GTProfileInfo._profileCounters
- _OBJC_IVAR_$_GTProfileInfo._profilingConfig
- _OBJC_IVAR_$_GTProfileInfo._resume
- _OBJC_IVAR_$_GTProfileInfo._splitEncoderCommandCount
- _OBJC_IVAR_$_GTProfileInfo._splitPerEncoderKickCount
- _OBJC_IVAR_$_GTProfileInfo._timelineConfig
- _OBJC_IVAR_$_GTProfileInfo._totalDrawCallCount
- _OBJC_IVAR_$_GTProfileInfo._useOverlap
- _OBJC_IVAR_$_GTProfileInfo._version
- _OBJC_IVAR_$_GTProfileInfo._withoutBlitEncoderToDrawCallCountDict
- _OBJC_IVAR_$_GTProfileInfo._xpState
- _OBJC_IVAR_$_GTRelayedXPCConnection._relayPid
- _OBJC_IVAR_$_GTRelayedXPCConnection._relayPort
- _OBJC_IVAR_$_GTReplayADSReplyStream._log
- _OBJC_IVAR_$_GTReplayProfileReplyStream._log
- _OBJC_IVAR_$_GTServiceProvider._log
- _OBJC_IVAR_$_GTServiceProviderXPCProxy._log
- _OBJC_IVAR_$_GTTransportClient._log
- _OBJC_IVAR_$_GTURLAccessProvider._log
- _OBJC_IVAR_$_GTXPCDispatcher._log
- _OBJC_METACLASS_$_GTProfileInfo
- __OBJC_$_CLASS_METHODS_GTProfileInfo
- __OBJC_$_CLASS_PROP_LIST_GTProfileInfo
- __OBJC_$_INSTANCE_METHODS_GTProfileInfo
- __OBJC_$_INSTANCE_VARIABLES_GTProfileInfo
- __OBJC_$_PROP_LIST_GTProfileInfo
- __OBJC_$_PROTOCOL_REFS_GTBulkDataServiceXPCDispatcher
- __OBJC_$_PROTOCOL_REFS_GTDeviceCapabilitiesXPCDispatcher
- __OBJC_$_PROTOCOL_REFS_GTFileWriterServiceXPCDispatcher
- __OBJC_$_PROTOCOL_REFS_GTLoopbackServiceXPCDispatcher
- __OBJC_$_PROTOCOL_REFS_GTMTLCaptureServiceObserverXPCDispatcher
- __OBJC_$_PROTOCOL_REFS_GTMTLDiagnosticsServiceObserverXPCDispatcher
- __OBJC_$_PROTOCOL_REFS_GTMTLReplayServiceObserverXPCDispatcher
- __OBJC_$_PROTOCOL_REFS_GTMTLTelemetryServiceObserverXPCDispatcher
- __OBJC_$_PROTOCOL_REFS_GTRemoteDeviceBrowserObserverXPCDispatcher
- __OBJC_$_PROTOCOL_REFS_GTServiceProviderObserverXPCDispatcher
- __OBJC_$_PROTOCOL_REFS_GTURLAccessProviderXPCDispatcher
- __OBJC_CLASS_PROTOCOLS_$_GTProfileInfo
- __OBJC_CLASS_RO_$_GTProfileInfo
- __OBJC_METACLASS_RO_$_GTProfileInfo
- __ZL24ProxyCaptureBatchRequestP19GTServiceConnectionPU30objcproto19GTMTLCaptureService11objc_objectP21GTCaptureRequestBatchPKc
- __ZL27DispatchCaptureBatchRequestPU26objcproto15GTXPCConnection11objc_objectPU24objcproto13OS_xpc_object8NSObject
- __ZL31xpc_dictionary_get_nsobject_anyPU24objcproto13OS_xpc_object8NSObjectPKc
- ___113-[GTFileWriterService beginTransferSessionWithFileEntries:basePath:toDevice:options:sessionID:completionHandler:]_block_invoke.340
- ___113-[GTFileWriterService beginTransferSessionWithFileEntries:basePath:toDevice:options:sessionID:completionHandler:]_block_invoke_2
- ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke.39
- ___72-[GTURLAccessProvider securityScopedURLFromSandboxID:completionHandler:]_block_invoke.39.cold.1
- ___79-[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:]_block_invoke
- ___79-[GTURLAccessProvider copyIdentifier:toDevice:allowLocalURL:completionHandler:]_block_invoke_2
- ___GTTransportServiceDaemonConnectionNew_block_invoke
- ___GTTransportServiceDaemonConnectionNew_block_invoke_2
- ____ZL24ProxyCaptureBatchRequestP19GTServiceConnectionPU30objcproto19GTMTLCaptureService11objc_objectP21GTCaptureRequestBatchPKc_block_invoke
- ____ZL27DispatchCaptureBatchRequestPU26objcproto15GTXPCConnection11objc_objectPU24objcproto13OS_xpc_object8NSObject_block_invoke
- ____ZL27DispatchCaptureBatchRequestPU26objcproto15GTXPCConnection11objc_objectPU24objcproto13OS_xpc_object8NSObject_block_invoke_2
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_40_a8_32s_e27_v16?0"GTServiceObserver"8ls32l8
- ___block_descriptor_48_8_32s40w_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8w40l8
- ___block_descriptor_48_a8_32r_e36_B24?0Q8"NSObject<OS_xpc_object>"16lr32l8
- ___block_descriptor_48_a8_32s40s_e27_v16?0"GTCaptureResponse"8ls32l8s40l8
- ___block_descriptor_48_a8_32s40s_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8s40l8
- ___block_descriptor_48_a8_32s40s_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_8_32s40s48bs_e15_v16?0"NSURL"8ls32l8s48l8s40l8
- ___block_descriptor_56_8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_56_8_32s40s48bs_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8s48l8s40l8
- ___block_descriptor_56_a8_32s40s48bs_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_56_a8_32s40s48w_e34_v16?0"GTCaptureCompletionState"8lw48l8s32l8s40l8
- ___block_descriptor_64_8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___gt_default_log_block_invoke
- __os_log_impl
- _gt_default_log
- _gt_default_log.onceToken
- _objc_msgSend$URLByResolvingSymlinksInPath
- _objc_msgSend$copyIdentifier:toDevice:allowLocalURL:completionHandler:
- _objc_msgSend$initWithConnection:relayPort:relayPid:
- _objc_msgSend$numberWithUnsignedInt:
CStrings:
+ "%s\n"
+ "%s.%s.enableLog"
+ ".dimensions"
+ ".extents"
+ ".origin"
+ ".rank"
+ "@\"<GTDisplayService>\""
+ "@\"<GTErrorReportService>\""
+ "@\"<GTErrorReportServiceObserver>\""
+ "@\"<MTLSharedEvent>\""
+ "@\"<MTLTexture>\""
+ "@\"GTDisplayRequestToken\"32@0:8@\"GTDisplayShowRequest\"16@?<v@?@\"GTDisplayResponse\">24"
+ "@\"GTDisplayRequestToken\"32@0:8@\"GTDisplayUpdateRequest\"16@?<v@?@\"GTDisplayResponse\">24"
+ "@\"NSDate\""
+ "@24@0:8^@16"
+ "@56@0:8@16{MessageRemoteRoutingInfo=QQQB[7c]}24"
+ "API unavailable"
+ "BoundaryTracker"
+ "CommandBuffers"
+ "Critical"
+ "Directory enumeration failed whilst deleting archives %@"
+ "DispatchSorter"
+ "EventTracker"
+ "Failed to archive display request %@"
+ "Failed to archive display show response %@"
+ "Failed to archive display update response %@"
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
+ "Failed to register observer %@"
+ "Failed to resize file %@"
+ "Failed to resize file %@ (%d)"
+ "Failed to stat directory %@ after transfer: %{darwin.errno}d"
+ "Failed to unarchive display response %@"
+ "Failed to unarchive display show request %@"
+ "Failed to unarchive display update request %@"
+ "Failed to update owner of archive %@ after transfer: %{darwin.errno}d"
+ "Failed to update owner of one or more files inside archive %@ after transfer"
+ "Failed to write to fd (%d)"
+ "Failure whilst decoding timestamp for GTRejectedConnectionReport, %@"
+ "File writer service for %@ is unavailable"
+ "File writer service is too old. Missing selector %@"
+ "GPUToolsReplayerPreferXPCService"
+ "GTDisplayRequest"
+ "GTDisplayRequestToken"
+ "GTDisplayResponse"
+ "GTDisplayService"
+ "GTDisplayServiceXPCDispatcher"
+ "GTDisplayServiceXPCProxy"
+ "GTDisplayShowRequest"
+ "GTDisplayShowTextureRequest"
+ "GTDisplayUpdateOverlaysRequest"
+ "GTDisplayUpdateRequest"
+ "GTDisplayUpdateTerminationRequest"
+ "GTDisplayUpdateWindowConfigurationRequest"
+ "GTErrorReportService"
+ "GTErrorReportServiceObserver"
+ "GTErrorReportServiceObserverXPCDispatcher"
+ "GTErrorReportServiceReplyStream"
+ "GTErrorReportServiceXPCDispatcher"
+ "GTErrorReportServiceXPCProxy"
+ "GTObserverXPCDispatcher"
+ "GTRejectedConnectionReport"
+ "GTReplayDecodeGenericAccelerationStructure"
+ "GTReplayFetchInto"
+ "GTReplayFetchIntoRenderMask"
+ "GTReplayFetchIntoTexture"
+ "GTReplayFetchIntoWireframe"
+ "GTReplayFetchMLGraph"
+ "GTReplayFetchMLGraphData"
+ "GTReplayFetchMLIntermediateData"
+ "GTReplayFetchPipelineBinaries"
+ "GTReplayFetchTensor"
+ "Harvest"
+ "Invalid archive passed to UpdateArchiveOwner"
+ "Invalid destination directory passed to copyIdentifier"
+ "Invalid destination directory passed to initiateTransfer"
+ "Invalid options sent to beginTransferSessionWithFileEntries"
+ "Invalid options sent to initiateTransfer"
+ "Invalid sandbox ID %@"
+ "MTLFXFrameInterpolatorDescriptor"
+ "MTLFXTemporalDenoisedScalerDescriptor"
+ "Profiling"
+ "Remote connection for %@ is unavailable"
+ "Restores"
+ "Start transfer of %@ to %@"
+ "T@\"<MTLSharedEvent>\",&,N,V_event"
+ "T@\"<MTLTexture>\",&,N,V_dest"
+ "T@\"NSArray\",&,N,V_intermediateOps"
+ "T@\"NSDate\",&,V_timestamp"
+ "T@\"NSString\",&,N,V_mlModuleKey"
+ "T@\"NSString\",&,N,V_mlResourceKey"
+ "T@\"NSString\",&,N,V_windowTitle"
+ "T@\"NSString\",&,V_name"
+ "T@\"NSString\",R,N,V_deviceUDID"
+ "TB,N,V_disableDisplay"
+ "TB,N,V_enableLiveICBs"
+ "TB,N,V_forceResourcesResident"
+ "TB,N,V_preferXPCService"
+ "TB,N,V_visible"
+ "TI,N,V_presentDownloadSize"
+ "TQ,N,V_height"
+ "TQ,N,V_overlays"
+ "TQ,N,V_pipelineRef"
+ "TQ,N,V_pixelFormat"
+ "TQ,N,V_replayServicePort"
+ "TQ,N,V_width"
+ "TQ,R,N,V_servicePort"
+ "TQ,V_pid"
+ "Target path for symlink %@ is too long (%zd bytes >= %lu bytes [PATH_MAX])"
+ "The gputrace file transfer service is too old to support remote macOS debugging. Try updating your device's DDI by installing a newer Xcode."
+ "Tq,N,V_orientation"
+ "Tq,N,V_version"
+ "TraceStore"
+ "T{GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}},N,V_slice"
+ "Updating owner of archive %@ to %u:%u"
+ "_batch_requestXPCObjs"
+ "_dest"
+ "_disableDisplay"
+ "_enableLiveICBs"
+ "_event"
+ "_forceResourcesResident"
+ "_height"
+ "_intermediateOps"
+ "_mlModuleKey"
+ "_mlResourceKey"
+ "_orientation"
+ "_overlays"
+ "_pid"
+ "_pipelineRef"
+ "_pixelFormat"
+ "_preferXPCService"
+ "_presentDownloadSize"
+ "_remoteDeviceRelayRemotePid"
+ "_replayServicePort"
+ "_routingInfo"
+ "_sem"
+ "_timestamp"
+ "_visible"
+ "_width"
+ "_windowTitle"
+ "addObjectsFromArray:"
+ "beginTransferSessionWithFileEntries timed out waiting for final write to complete"
+ "beginTransferSessionWithFileEntries timed out waiting for transfer to complete"
+ "boolForKey:"
+ "bufferRobustnessSupport"
+ "code"
+ "com.apple.gputools.ASBuilder"
+ "com.apple.gputools.ASViewer"
+ "com.apple.gputools.cli"
+ "com.apple.gputools.core"
+ "com.apple.gputools.diagnostics"
+ "com.apple.gputools.filewriter"
+ "com.apple.gputools.replay"
+ "copyIdentifier %@ to device %@"
+ "copyIdentifier:toDevice:allowLocalURL:directory:completionHandler:"
+ "copyIdentifier:toDevice:directory:completionHandler:"
+ "copyIdentifier_toDevice_directory_completionHandler_:replyConnection:"
+ "createMachPort"
+ "decodeTopLevelObjectOfClass:forKey:error:"
+ "decodeXPCOnlyObjects:"
+ "defaultTextureWriteRoundingMode"
+ "dest"
+ "destPort"
+ "deviceCreationFlags"
+ "dir"
+ "directory"
+ "dirse"
+ "disableDisplay"
+ "domain"
+ "enableLiveICBs"
+ "encodeXPCOnlyObjects:"
+ "event"
+ "eventPort"
+ "fail: Invalid log tag: %u"
+ "fetchInto not supported for remote devices"
+ "fetchInto:"
+ "fetchInto_:replyConnection:"
+ "fetchRejectedConnections:"
+ "fetchRejectedConnections_:replyConnection:"
+ "forceResourcesResident"
+ "fragment"
+ "height"
+ "initWithConnection:routingInfo:"
+ "initWithID:"
+ "initWithMachPort:"
+ "intermediateOps"
+ "isQuadDataSharingSupported"
+ "kernel"
+ "latestSupportedGenericBVHVersion"
+ "limits"
+ "maxAccelerationStructureTraversalDepth"
+ "maxRasterizationRateLayerCount"
+ "mesh"
+ "mlModuleKey"
+ "mlResourceKey"
+ "newSharedEventHandle"
+ "newSharedEventWithMachPort:"
+ "newSharedTextureHandle"
+ "newSharedTextureWithHandle:"
+ "notifyRejectedConnections:"
+ "notifyRejectedConnections_:replyConnection:"
+ "object"
+ "orientation"
+ "overlays"
+ "pid"
+ "pipelineRef"
+ "pixelFormat"
+ "preferXPCService"
+ "presentDownloadSize"
+ "programDataHandle"
+ "replayServicePort"
+ "requiresBFloat16Emulation"
+ "returnRejectedConnections:"
+ "setDest:"
+ "setDisableDisplay:"
+ "setEnableLiveICBs:"
+ "setEvent:"
+ "setForceResourcesResident:"
+ "setIntermediateOps:"
+ "setMlModuleKey:"
+ "setMlResourceKey:"
+ "setOrientation:"
+ "setOverlays:"
+ "setPid:"
+ "setPipelineRef:"
+ "setPreferXPCService:"
+ "setPresentDownloadSize:"
+ "setReplayServicePort:"
+ "setTimestamp:"
+ "setVisible:"
+ "setWindowTitle:"
+ "show:completionHandler:"
+ "show_completionHandler_:replyConnection:"
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
+ "supportsTessellation"
+ "supportsTextureOutOfBoundsReads"
+ "supportsTextureWriteRoundingMode:"
+ "supportsUnalignedVertexFetch"
+ "supportsVirtualSubstreams"
+ "supportsWritableArrayOfTextures"
+ "timestamp"
+ "unknown"
+ "update:completionHandler:"
+ "update_completionHandler_:replyConnection:"
+ "v16@?0@\"GTDisplayResponse\"8"
+ "v16@?0Q8"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v288@0:8{GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}16"
+ "v48@0:8@\"NSURL\"16@\"NSString\"24@\"NSURL\"32@?<v@?@\"NSURL\"@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
+ "v52@0:8@16@24B32@36@?44"
+ "v64@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSURL\"40@\"GTFileTransferOptions\"48@?<v@?@\"NSURL\"@\"NSError\">56"
+ "vertex"
+ "visible"
+ "width"
+ "windowTitle"
+ "{GTMTLTensorSlice=\"origin\"{GTMTLTensorExtents=\"rank\"Q\"extents\"[16Q]}\"dimensions\"{GTMTLTensorExtents=\"rank\"Q\"extents\"[16Q]}}"
+ "{GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}16@0:8"
+ "{MessageRemoteRoutingInfo=\"hostPort\"Q\"hostPid\"Q\"remotePid\"Q\"onRemote\"B\"_padding\"[7c]}"
- "@\"NSObject<OS_os_log>\""
- "@36@0:8@16Q24i32"
- "AnalyzeBinaries"
- "BulkData"
- "BulkDataProxy"
- "CaptureProxy"
- "ConnectionVersioning"
- "DiagnosticsService"
- "Failed to close file"
- "Failed to flush file"
- "Failed to initialize compression stream"
- "Failed to open file for writing"
- "Failed to resize file"
- "Failed to write to file"
- "FileWriterService"
- "FileWriterSession"
- "GPUTOOLS(warning): Log uninitialized, please call GTCoreLogInit(), logging to OS_LOG_DEFAULT instead"
- "GTProfileInfo"
- "HighPriorityBatchInfo"
- "Invalid sandbox ID"
- "Loopback"
- "Q24@0:8@\"<GTMTLCaptureServiceObserver>\"16"
- "Q24@0:8@\"<GTMTLDiagnosticsServiceObserver>\"16"
- "Q24@0:8@\"<GTMTLReplayServiceObserver>\"16"
- "Q24@0:8@\"<GTMTLTelemetryServiceObserver>\"16"
- "Q24@0:8@\"<GTRemoteDeviceBrowserObserver>\"16"
- "Q24@0:8@\"<GTServiceProviderObserver>\"16"
- "ReplayDispatcher"
- "ReplayProxy"
- "ServiceDaemonConnection"
- "ServiceProvider"
- "ServiceProviderProxy"
- "T@\"NSArray\",&,N,V_activePerEncoderDrawCallCount"
- "T@\"NSArray\",&,N,V_batchFilteredDerivedCounters"
- "T@\"NSArray\",&,N,V_blitEncoderIndices"
- "T@\"NSArray\",&,N,V_counters"
- "T@\"NSArray\",&,N,V_encoderBatchPriorityList"
- "T@\"NSArray\",&,N,V_highPriorityBatches"
- "T@\"NSArray\",&,N,V_perCommandBufferEncoderCount"
- "T@\"NSArray\",&,N,V_perEncoderKickCount"
- "T@\"NSArray\",&,N,V_perFrameCommandBufferCount"
- "T@\"NSArray\",&,N,V_profileCounters"
- "T@\"NSArray\",&,N,V_splitEncoderCommandCount"
- "T@\"NSArray\",&,N,V_splitPerEncoderKickCount"
- "T@\"NSDictionary\",&,N,V_counterConfig"
- "T@\"NSDictionary\",&,N,V_derivedCounterData"
- "T@\"NSDictionary\",&,N,V_derivedCounterInfo"
- "T@\"NSDictionary\",&,N,V_highPriorityBatchInfo"
- "T@\"NSDictionary\",&,N,V_perEncoderDrawCallCount"
- "T@\"NSDictionary\",&,N,V_perEncoderIndexDrawCallCount"
- "T@\"NSDictionary\",&,N,V_profilingConfig"
- "T@\"NSDictionary\",&,N,V_timelineConfig"
- "T@\"NSDictionary\",&,N,V_withoutBlitEncoderToDrawCallCountDict"
- "T@\"NSString\",&,N,V_gpuTarget"
- "T@\"NSString\",&,N,V_metalPluginName"
- "TB,N,V_analyzeBinaries"
- "TB,N,V_pause"
- "TB,N,V_resume"
- "TB,N,V_useOverlap"
- "TI,N,V_gpuState"
- "TI,N,V_totalDrawCallCount"
- "TI,N,V_xpState"
- "TelemetryProxy"
- "URLAccessProvider"
- "URLByResolvingSymlinksInPath"
- "XPState"
- "_activePerEncoderDrawCallCount"
- "_analyzeBinaries"
- "_batchFilteredDerivedCounters"
- "_blitEncoderIndices"
- "_counterConfig"
- "_counters"
- "_derivedCounterData"
- "_derivedCounterInfo"
- "_encoderBatchPriorityList"
- "_gpuState"
- "_gpuTarget"
- "_highPriorityBatchInfo"
- "_highPriorityBatches"
- "_log"
- "_metalPluginName"
- "_pause"
- "_perCommandBufferEncoderCount"
- "_perEncoderDrawCallCount"
- "_perEncoderIndexDrawCallCount"
- "_perEncoderKickCount"
- "_perFrameCommandBufferCount"
- "_profileCounters"
- "_profilingConfig"
- "_relayPid"
- "_relayPort"
- "_resume"
- "_splitEncoderCommandCount"
- "_splitPerEncoderKickCount"
- "_timelineConfig"
- "_totalDrawCallCount"
- "_useOverlap"
- "_withoutBlitEncoderToDrawCallCountDict"
- "_xpState"
- "activePerEncoderDrawCallCount"
- "analyzeBinaries"
- "batchFilteredDerivedCounters"
- "beginTransferSessionWithFileEntires timed out waiting for final write to complete"
- "beginTransferSessionWithFileEntires timed out waiting for transfer to complete"
- "blitEncoderIndices"
- "com.apple.gputools.filestreamer"
- "copyIdentifier:toDevice:allowLocalURL:completionHandler:"
- "counterConfig"
- "counters"
- "derivedCounterData"
- "derivedCounterInfo"
- "encoderBatchPriorityList"
- "gpuState"
- "gpuTarget"
- "highPriorityBatchInfo"
- "highPriorityBatches"
- "initFromProfileInfo:"
- "initWithConnection:relayPort:relayPid:"
- "metalPluginName"
- "numberWithUnsignedInt:"
- "perCommandBufferEncoderCount"
- "perEncoderDrawCallCount"
- "perEncoderIndexDrawCallCount"
- "perEncoderKickCount"
- "perFrameCommandBufferCount"
- "profileCounters"
- "profilingConfig"
- "setActivePerEncoderDrawCallCount:"
- "setAnalyzeBinaries:"
- "setBatchFilteredDerivedCounters:"
- "setBlitEncoderIndices:"
- "setCounterConfig:"
- "setCounters:"
- "setDerivedCounterData:"
- "setDerivedCounterInfo:"
- "setEncoderBatchPriorityList:"
- "setGpuState:"
- "setGpuTarget:"
- "setHighPriorityBatchInfo:"
- "setHighPriorityBatches:"
- "setMetalPluginName:"
- "setPause:"
- "setPerCommandBufferEncoderCount:"
- "setPerEncoderDrawCallCount:"
- "setPerEncoderIndexDrawCallCount:"
- "setPerEncoderKickCount:"
- "setPerFrameCommandBufferCount:"
- "setProfileCounters:"
- "setProfilingConfig:"
- "setResume:"
- "setSplitEncoderCommandCount:"
- "setSplitPerEncoderKickCount:"
- "setTimelineConfig:"
- "setTotalDrawCallCount:"
- "setUseOverlap:"
- "setWithoutBlitEncoderToDrawCallCountDict:"
- "setXpState:"
- "splitEncoderCommandCount"
- "splitPerEncoderKickCount"
- "timelineConfig"
- "toDictionary"
- "totalDrawCallCount"
- "transferIdentifier %@ to device %@"
- "updateRelayPort:pid:"
- "useOverlap"
- "v28@0:8Q16i24"
- "v44@0:8@16@24B32@?36"
- "withoutBlitEncoderToDrawCallCountDict"
- "xpState"

```
