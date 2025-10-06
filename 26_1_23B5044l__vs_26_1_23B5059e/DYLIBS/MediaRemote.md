## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4025.210.8.1.0
-  __TEXT.__text: 0x2edf8c
+4025.200.14.0.0
+  __TEXT.__text: 0x2f1a58
   __TEXT.__auth_stubs: 0x16f0
-  __TEXT.__objc_methlist: 0x2ac50
+  __TEXT.__objc_methlist: 0x2af50
   __TEXT.__const: 0x5f8
-  __TEXT.__cstring: 0x2b79b
-  __TEXT.__oslogstring: 0xd871
-  __TEXT.__gcc_except_tab: 0x63ac
+  __TEXT.__cstring: 0x2bae4
+  __TEXT.__oslogstring: 0xdb49
+  __TEXT.__gcc_except_tab: 0x648c
   __TEXT.__dlopen_cstrs: 0x514
   __TEXT.__ustring: 0x7a2
-  __TEXT.__unwind_info: 0xb108
-  __TEXT.__objc_classname: 0x4d17
-  __TEXT.__objc_methname: 0x4cc8e
-  __TEXT.__objc_methtype: 0x8f16
-  __TEXT.__objc_stubs: 0x27fa0
+  __TEXT.__unwind_info: 0xb220
+  __TEXT.__objc_classname: 0x4d83
+  __TEXT.__objc_methname: 0x4d2c8
+  __TEXT.__objc_methtype: 0x8fd0
+  __TEXT.__objc_stubs: 0x28320
   __DATA_CONST.__got: 0x1440
-  __DATA_CONST.__const: 0xad70
-  __DATA_CONST.__objc_classlist: 0x1188
+  __DATA_CONST.__const: 0xae18
+  __DATA_CONST.__objc_classlist: 0x11a0
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x258
+  __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xee38
+  __DATA_CONST.__objc_selrefs: 0xef78
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xfb8
+  __DATA_CONST.__objc_superrefs: 0xfc8
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb88
-  __AUTH_CONST.__const: 0x3020
-  __AUTH_CONST.__cfstring: 0x22d40
-  __AUTH_CONST.__objc_const: 0x45538
+  __AUTH_CONST.__const: 0x3080
+  __AUTH_CONST.__cfstring: 0x22fe0
+  __AUTH_CONST.__objc_const: 0x45b00
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x8250
+  __AUTH.__objc_data: 0x82f0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x31e0
-  __DATA.__data: 0x1c80
-  __DATA.__bss: 0x850
+  __DATA.__objc_ivar: 0x3220
+  __DATA.__data: 0x1ce0
+  __DATA.__bss: 0x870
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2d00
+  __DATA_DIRTY.__objc_data: 0x2d50
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x4e0
+  __DATA_DIRTY.__bss: 0x500
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7EB781F7-CFFD-3A43-8271-819B436839EE
-  Functions: 20033
-  Symbols:   54983
-  CStrings:  24205
+  UUID: 6EB46D04-0FB7-3198-8571-69660CCD8E63
+  Functions: 20132
+  Symbols:   55269
+  CStrings:  24332
 
Symbols:
+ -[MRHeadphonesRouteDetectorDataSource relevantRouteDetector:isEndpointRelevant:]
+ -[MRHeadphonesRouteDetectorDataSource relevantRouteDetector:isOutputDeviceRelevant:]
+ -[MRNowPlayingOriginClientManager playbackQueueDataSourceOperationQueue]
+ -[MRNowPlayingOriginClientManager playbackQueueDataSourceOperationQueue].cold.1
+ -[MRNowPlayingPlayerClientCallbacks registerNowPlayingInfoBackedPlaybackQueueDataSourceCallbacks].cold.1
+ -[MROperation .cxx_destruct]
+ -[MROperation cancel]
+ -[MROperation cancellationDate]
+ -[MROperation completionHandler]
+ -[MROperation creationDate]
+ -[MROperation endDate]
+ -[MROperation executionDuration]
+ -[MROperation initWithBlock:completionHandler:]
+ -[MROperation main]
+ -[MROperation operationBlock]
+ -[MROperation setCancellationDate:]
+ -[MROperation setCompletionHandler:]
+ -[MROperation setCreationDate:]
+ -[MROperation setEndDate:]
+ -[MROperation setOperationBlock:]
+ -[MROperation setStartDate:]
+ -[MROperation startDate]
+ -[MROperation totalDuration]
+ -[MROperation waitDuration]
+ -[MRRelevantRouteDetector .cxx_destruct]
+ -[MRRelevantRouteDetector _handleEndpointDidDisconnectNotification:]
+ -[MRRelevantRouteDetector _handleOutputDevicesDidChangeNotification:]
+ -[MRRelevantRouteDetector _isEndpointRelevant:]
+ -[MRRelevantRouteDetector _isEndpointRelevant:].cold.1
+ -[MRRelevantRouteDetector _isEndpointRelevant:].cold.2
+ -[MRRelevantRouteDetector _isOutputDeviceRelevant:]
+ -[MRRelevantRouteDetector _isOutputDeviceRelevant:].cold.1
+ -[MRRelevantRouteDetector _isOutputDeviceRelevant:].cold.2
+ -[MRRelevantRouteDetector _onQueue_addRelevantEndpoints:withReason:]
+ -[MRRelevantRouteDetector _onQueue_reevaluateWithReason:]
+ -[MRRelevantRouteDetector _onQueue_reevaluateWithReason:].cold.1
+ -[MRRelevantRouteDetector _onQueue_relevantRouteCurrentlyDetected]
+ -[MRRelevantRouteDetector _onQueue_startMonitoring]
+ -[MRRelevantRouteDetector _registerForNotificationsForEndpoint:]
+ -[MRRelevantRouteDetector _stopMonitoring]
+ -[MRRelevantRouteDetector _unregisterForNotificationsForEndpoint:]
+ -[MRRelevantRouteDetector dataSource]
+ -[MRRelevantRouteDetector dealloc]
+ -[MRRelevantRouteDetector debugDescription]
+ -[MRRelevantRouteDetector delegateQueue]
+ -[MRRelevantRouteDetector delegate]
+ -[MRRelevantRouteDetector description]
+ -[MRRelevantRouteDetector discoverySession]
+ -[MRRelevantRouteDetector initWithInitiator:delegate:dataSource:delegateQueue:]
+ -[MRRelevantRouteDetector initiator]
+ -[MRRelevantRouteDetector isMonitoring]
+ -[MRRelevantRouteDetector queue]
+ -[MRRelevantRouteDetector relevantEndpoints]
+ -[MRRelevantRouteDetector relevantRouteDetected]
+ -[MRRelevantRouteDetector setDelegate:]
+ -[MRRelevantRouteDetector setDiscoverySession:]
+ -[MRRelevantRouteDetector setIsMonitoring:]
+ -[MRRelevantRouteDetector setQueue:]
+ -[MRRelevantRouteDetector setRelevantEndpoints:]
+ -[MRRelevantRouteDetector setRelevantRouteDetected:]
+ -[MRRelevantRouteDetector startMonitoring]
+ -[MRRelevantRouteDetector stopMonitoring]
+ -[MRSharedSettings staticWaveform]
+ -[MRUserSettings staticWaveform]
+ -[MRUserSettings verbosePlaybackQueueRequestLogging]
+ GCC_except_table50
+ _MRPlaybackQueueDataSourceSetMaxConcurrentRequestCount
+ _MRRequestDetailsInitiatorWorkout
+ _OBJC_CLASS_$_MRHeadphonesRouteDetectorDataSource
+ _OBJC_CLASS_$_MROperation
+ _OBJC_CLASS_$_MRRelevantRouteDetector
+ _OBJC_CLASS_$_NSOperation
+ _OBJC_IVAR_$_MROperation._cancellationDate
+ _OBJC_IVAR_$_MROperation._completionHandler
+ _OBJC_IVAR_$_MROperation._creationDate
+ _OBJC_IVAR_$_MROperation._endDate
+ _OBJC_IVAR_$_MROperation._lock
+ _OBJC_IVAR_$_MROperation._operationBlock
+ _OBJC_IVAR_$_MROperation._startDate
+ _OBJC_IVAR_$_MRRelevantRouteDetector._dataSource
+ _OBJC_IVAR_$_MRRelevantRouteDetector._delegate
+ _OBJC_IVAR_$_MRRelevantRouteDetector._delegateQueue
+ _OBJC_IVAR_$_MRRelevantRouteDetector._discoverySession
+ _OBJC_IVAR_$_MRRelevantRouteDetector._initiator
+ _OBJC_IVAR_$_MRRelevantRouteDetector._isMonitoring
+ _OBJC_IVAR_$_MRRelevantRouteDetector._queue
+ _OBJC_IVAR_$_MRRelevantRouteDetector._relevantEndpoints
+ _OBJC_IVAR_$_MRRelevantRouteDetector._relevantRouteDetected
+ _OBJC_METACLASS_$_MRHeadphonesRouteDetectorDataSource
+ _OBJC_METACLASS_$_MROperation
+ _OBJC_METACLASS_$_MRRelevantRouteDetector
+ _OBJC_METACLASS_$_NSOperation
+ __MREnqueueAndHandlePlaybackQueueRequest
+ __MREnqueueAndHandlePlaybackQueueRequest.cold.1
+ __MREnqueueAndHandlePlaybackQueueRequest.cold.2
+ __MREnqueueAndHandlePlaybackQueueRequest.cold.3
+ __MREnqueueAndHandlePlaybackQueueRequest.cold.4
+ __OBJC_$_INSTANCE_METHODS_MRHeadphonesRouteDetectorDataSource
+ __OBJC_$_INSTANCE_METHODS_MROperation
+ __OBJC_$_INSTANCE_METHODS_MRRelevantRouteDetector
+ __OBJC_$_INSTANCE_VARIABLES_MROperation
+ __OBJC_$_INSTANCE_VARIABLES_MRRelevantRouteDetector
+ __OBJC_$_PROP_LIST_MRHeadphonesRouteDetectorDataSource
+ __OBJC_$_PROP_LIST_MROperation
+ __OBJC_$_PROP_LIST_MRRelevantRouteDetector
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MRRelevantRouteDetectorDataSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MRRelevantRouteDetectorDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MRRelevantRouteDetectorDataSource
+ __OBJC_$_PROTOCOL_REFS_MRRelevantRouteDetectorDataSource
+ __OBJC_CLASS_PROTOCOLS_$_MRHeadphonesRouteDetectorDataSource
+ __OBJC_CLASS_RO_$_MRHeadphonesRouteDetectorDataSource
+ __OBJC_CLASS_RO_$_MROperation
+ __OBJC_CLASS_RO_$_MRRelevantRouteDetector
+ __OBJC_LABEL_PROTOCOL_$_MRRelevantRouteDetectorDataSource
+ __OBJC_METACLASS_RO_$_MRHeadphonesRouteDetectorDataSource
+ __OBJC_METACLASS_RO_$_MROperation
+ __OBJC_METACLASS_RO_$_MRRelevantRouteDetector
+ __OBJC_PROTOCOL_$_MRRelevantRouteDetectorDataSource
+ ___111-[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:requestID:queue:completion:]_block_invoke.59
+ ___111-[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:requestID:queue:completion:]_block_invoke.62
+ ___131-[MRNowPlayingOriginClientManager _resolveActiveSystemEndpointWithType:requestName:requestType:requestID:timeout:queue:completion:]_block_invoke.113
+ ___131-[MRNowPlayingOriginClientManager _resolveActiveSystemEndpointWithType:requestName:requestType:requestID:timeout:queue:completion:]_block_invoke.92
+ ___131-[MRNowPlayingOriginClientManager _resolveActiveSystemEndpointWithType:requestName:requestType:requestID:timeout:queue:completion:]_block_invoke.92.cold.1
+ ___32-[MRUserSettings staticWaveform]_block_invoke
+ ___39-[MRRelevantRouteDetector isMonitoring]_block_invoke
+ ___41-[MRRelevantRouteDetector stopMonitoring]_block_invoke
+ ___42-[MRRelevantRouteDetector startMonitoring]_block_invoke
+ ___43-[MRRelevantRouteDetector debugDescription]_block_invoke
+ ___47-[MROperation initWithBlock:completionHandler:]_block_invoke
+ ___48-[MRRelevantRouteDetector relevantRouteDetected]_block_invoke
+ ___51-[MRRelevantRouteDetector _onQueue_startMonitoring]_block_invoke
+ ___51-[MRRelevantRouteDetector _onQueue_startMonitoring]_block_invoke_2
+ ___51-[MRRelevantRouteDetector _onQueue_startMonitoring]_block_invoke_3
+ ___52-[MRUserSettings verbosePlaybackQueueRequestLogging]_block_invoke
+ ___57-[MRRelevantRouteDetector _onQueue_reevaluateWithReason:]_block_invoke
+ ___66-[MRRelevantRouteDetector _onQueue_relevantRouteCurrentlyDetected]_block_invoke
+ ___66-[MRRelevantRouteDetector _onQueue_relevantRouteCurrentlyDetected]_block_invoke_2
+ ___68-[MRRelevantRouteDetector _handleEndpointDidDisconnectNotification:]_block_invoke
+ ___68-[MRRelevantRouteDetector _onQueue_addRelevantEndpoints:withReason:]_block_invoke
+ ___68-[MRRelevantRouteDetector _onQueue_addRelevantEndpoints:withReason:]_block_invoke.43
+ ___69-[MRRelevantRouteDetector _handleOutputDevicesDidChangeNotification:]_block_invoke
+ ___72-[MRNowPlayingOriginClientManager playbackQueueDataSourceOperationQueue]_block_invoke
+ ___96-[MRNowPlayingOriginClientManager resolveActiveSystemEndpointWithType:timeout:queue:completion:]_block_invoke.79
+ ___97-[MRNowPlayingPlayerClientCallbacks registerNowPlayingInfoBackedPlaybackQueueDataSourceCallbacks]_block_invoke
+ ___MRAnalyticsSendEvent_block_invoke.389
+ ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke
+ ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke.108
+ ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke.108.cold.1
+ ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke.109
+ ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke.cold.1
+ ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke_2
+ ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke_3
+ ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke_4
+ ____MREnqueueAndHandlePlaybackQueueRequest_block_invoke_5
+ ____MRHandlePlaybackQueueRequest_block_invoke.100
+ ___block_descriptor_40_e8_32bs_e21_v16?0"MROperation"8ls32l8
+ ___block_descriptor_40_e8_32s_e21_v16?0"MROperation"8ls32l8
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e21_v16?0"MROperation"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e37_v24?0"MRPlaybackQueue"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.385
+ _objc_msgSend$_isEndpointRelevant:
+ _objc_msgSend$_isOutputDeviceRelevant:
+ _objc_msgSend$_onQueue_addRelevantEndpoints:withReason:
+ _objc_msgSend$_onQueue_reevaluateWithReason:
+ _objc_msgSend$_onQueue_relevantRouteCurrentlyDetected
+ _objc_msgSend$_onQueue_startMonitoring
+ _objc_msgSend$_registerForNotificationsForEndpoint:
+ _objc_msgSend$_stopMonitoring
+ _objc_msgSend$_unregisterForNotificationsForEndpoint:
+ _objc_msgSend$addOperation:
+ _objc_msgSend$completionHandler
+ _objc_msgSend$executionDuration
+ _objc_msgSend$initWithBlock:completionHandler:
+ _objc_msgSend$isCancelled
+ _objc_msgSend$isMonitoring
+ _objc_msgSend$maxConcurrentOperationCount
+ _objc_msgSend$operationBlock
+ _objc_msgSend$operationCount
+ _objc_msgSend$playbackQueueDataSourceOperationQueue
+ _objc_msgSend$relevantEndpoints
+ _objc_msgSend$relevantRouteDetected
+ _objc_msgSend$relevantRouteDetector:didDetectRelevantRoute:
+ _objc_msgSend$relevantRouteDetector:isEndpointRelevant:
+ _objc_msgSend$relevantRouteDetector:isOutputDeviceRelevant:
+ _objc_msgSend$staticWaveform
+ _objc_msgSend$totalDuration
+ _objc_msgSend$verbosePlaybackQueueRequestLogging
+ _objc_msgSend$waitDuration
+ _playbackQueueDataSourceOperationQueue.onceToken
+ _playbackQueueDataSourceOperationQueue.operationQueue
+ _registerNowPlayingInfoBackedPlaybackQueueDataSourceCallbacks.onceToken
+ _registerNowPlayingInfoBackedPlaybackQueueDataSourceCallbacks.queue
+ _staticWaveform.__once
+ _staticWaveform.__static
+ _verbosePlaybackQueueRequestLogging.__once
+ _verbosePlaybackQueueRequestLogging.__should
- __MRHandlePlaybackQueueRequest.cold.5
- ___111-[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:requestID:queue:completion:]_block_invoke.53
- ___111-[MRNowPlayingOriginClientManager handleActiveSystemEndpointOutputDeviceUIDForType:requestID:queue:completion:]_block_invoke.56
- ___131-[MRNowPlayingOriginClientManager _resolveActiveSystemEndpointWithType:requestName:requestType:requestID:timeout:queue:completion:]_block_invoke.107
- ___131-[MRNowPlayingOriginClientManager _resolveActiveSystemEndpointWithType:requestName:requestType:requestID:timeout:queue:completion:]_block_invoke.86
- ___131-[MRNowPlayingOriginClientManager _resolveActiveSystemEndpointWithType:requestName:requestType:requestID:timeout:queue:completion:]_block_invoke.86.cold.1
- ___96-[MRNowPlayingOriginClientManager resolveActiveSystemEndpointWithType:timeout:queue:completion:]_block_invoke.73
- ___MRAnalyticsSendEvent_block_invoke.383
- ____MRHandlePlaybackQueueRequest_block_invoke.88
- ____MRHandlePlaybackQueueRequest_block_invoke_3
- ___block_descriptor_64_e8_32s40s48s56bs_e37_v24?0"MRPlaybackQueue"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
- ___block_literal_global.379
- ___block_literal_global.76
CStrings:
+ "5"
+ "<%@:%p initiator=%@, relevantRouteDetected=%@, isMonitoring=%@, relevantEndpoints=%@>"
+ "@\"<MRRelevantRouteDetectorDataSource>\""
+ "@\"<MRRelevantRouteDetectorDelegate>\""
+ "B32@0:8@\"MRRelevantRouteDetector\"16@\"MRAVEndpoint\"24"
+ "B32@0:8@\"MRRelevantRouteDetector\"16@\"MRAVOutputDevice\"24"
+ "Connected Endpoint"
+ "It has been more than <%lf> seconds since playbackQueueRequest=%@ was called and still waiting for operation to begin"
+ "MREnqueueAndHandlePlaybackQueueRequest"
+ "MRHandlePlaybackQueueRequest"
+ "MRHeadphonesRouteDetectorDataSource"
+ "MROperation"
+ "MRRelevantRouteDetector"
+ "MRRelevantRouteDetectorDataSource"
+ "StaticWaveform"
+ "T@\"<MRRelevantRouteDetectorDataSource>\",R,W,N,V_dataSource"
+ "T@\"<MRRelevantRouteDetectorDelegate>\",W,N,V_delegate"
+ "T@\"MRAVRoutingDiscoverySession\",&,N,V_discoverySession"
+ "T@\"NSDate\",&,N,V_cancellationDate"
+ "T@\"NSDate\",&,N,V_creationDate"
+ "T@\"NSMutableArray\",&,N,V_relevantEndpoints"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_delegateQueue"
+ "T@\"NSOperationQueue\",R,N"
+ "T@?,C,N,V_completionHandler"
+ "T@?,C,N,V_operationBlock"
+ "TB,N,V_isMonitoring"
+ "TB,N,V_relevantRouteDetected"
+ "TB,R,N,GisMonitoring"
+ "Unable to begin execution of playbackQueueRequest operation"
+ "Workout"
+ "[MRRelevantRouteDetector] %@: Adding endpoint=%@"
+ "[MRRelevantRouteDetector] %@: Connected endpoint=%@"
+ "[MRRelevantRouteDetector] %@: Connecting endpoint=%@"
+ "[MRRelevantRouteDetector] %@: DataSource doesn't implement isEndpointRelevant, defaulting to YES for local endpoint only"
+ "[MRRelevantRouteDetector] %@: DataSource doesn't implement isOutputDeviceRelevant, defaulting to NO"
+ "[MRRelevantRouteDetector] %@: DataSource says endpoint %@ is %@"
+ "[MRRelevantRouteDetector] %@: DataSource says output device %@ is %@"
+ "[MRRelevantRouteDetector] %@: Error connecting endpoint=%@, error=%@"
+ "[MRRelevantRouteDetector] %@: Querying endpoint relevance for %@"
+ "[MRRelevantRouteDetector] %@: Querying output device relevance for %@"
+ "[MRRelevantRouteDetector] %@: Reevaluate reason=%@"
+ "[MRRelevantRouteDetector] %@: Start Monitoring"
+ "[MRRelevantRouteDetector] %@: Stop Monitoring"
+ "[MRRelevantRouteDetector] %@: reason=%@, didDetectRelevantRoute -> %{BOOL}u"
+ "_cancellationDate"
+ "_completionHandler"
+ "_creationDate"
+ "_isEndpointRelevant:"
+ "_isMonitoring"
+ "_isOutputDeviceRelevant:"
+ "_onQueue_addRelevantEndpoints:withReason:"
+ "_onQueue_reevaluateWithReason:"
+ "_onQueue_relevantRouteCurrentlyDetected"
+ "_onQueue_startMonitoring"
+ "_operationBlock"
+ "_registerForNotificationsForEndpoint:"
+ "_relevantEndpoints"
+ "_relevantRouteDetected"
+ "_stopMonitoring"
+ "_unregisterForNotificationsForEndpoint:"
+ "addOperation:"
+ "cancellationDate"
+ "com.apple.MediaRemote.MRRelevantRouteDetector"
+ "com.apple.mediaremote.serviceclient.playbackqueue.%@"
+ "com.apple.mediaremote.serviceclient.playbackqueue.operation"
+ "com.apple.mediaremote.serviceclient.playbackqueue.operationqueue"
+ "completionHandler"
+ "connectToRelevantEndpoints"
+ "creationDate"
+ "endpointAdded"
+ "executionDuration"
+ "initWithBlock:completionHandler:"
+ "initWithInitiator:delegate:dataSource:delegateQueue:"
+ "isCancelled"
+ "isMonitoring"
+ "main"
+ "maxConcurrentOperationCount"
+ "mediaremotetool"
+ "monitoring"
+ "not relevant"
+ "operationBlock"
+ "operationCount"
+ "pendingOperationCount"
+ "playbackQueueDataSourceOperationQueue"
+ "relevant"
+ "relevantEndpoints"
+ "relevantRouteDetected"
+ "relevantRouteDetector:didDetectRelevantRoute:"
+ "relevantRouteDetector:isEndpointRelevant:"
+ "relevantRouteDetector:isOutputDeviceRelevant:"
+ "setCancellationDate:"
+ "setCompletionHandler:"
+ "setCreationDate:"
+ "setDiscoverySession:"
+ "setIsMonitoring:"
+ "setOperationBlock:"
+ "setRelevantEndpoints:"
+ "setRelevantRouteDetected:"
+ "staticWaveform"
+ "totalDuration"
+ "v16@?0@\"MROperation\"8"
+ "verbosePlaybackQueueRequestLogging"
+ "void _MREnqueueAndHandlePlaybackQueueRequest(MRPlayerPath *__strong, MRPlaybackQueueRequest *__strong, __strong _MRPlaybackQueueRequestCallbackCompletion)"
+ "waitDuration"
- "[MRPlaybackQueueServiceClient] Received playbackQueueRequest %{public}@ for path %{public}@"
- "[MRPlaybackQueueServiceClient] Responded to playbackQueueRequest %{public}@ for path %{public}@ with %{public}@"
- "[MRPlaybackQueueServiceClient] Responded to playbackQueueRequest %{public}@ for path %{public}@ with error %{public}@"
- "com.apple.mediaremote.playbackqueue.%@"

```
