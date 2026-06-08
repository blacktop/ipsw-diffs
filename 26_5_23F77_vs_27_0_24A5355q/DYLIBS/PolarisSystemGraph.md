## PolarisSystemGraph

> `/System/Library/PrivateFrameworks/PolarisSystemGraph.framework/PolarisSystemGraph`

```diff

-220.100.15.0.3
-  __TEXT.__text: 0xb8f0
-  __TEXT.__auth_stubs: 0x3e0
+256.0.0.502.2
+  __TEXT.__text: 0xa9f8
   __TEXT.__objc_methlist: 0x12d8
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x73f
+  __TEXT.__cstring: 0x755
   __TEXT.__oslogstring: 0xe35
-  __TEXT.__unwind_info: 0x380
-  __TEXT.__objc_classname: 0x748
-  __TEXT.__objc_methname: 0x234f
-  __TEXT.__objc_methtype: 0x932
-  __TEXT.__objc_stubs: 0x1c80
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x950
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x2ea8
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xd8
   __DATA.__data: 0x120
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x1220
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D5658603-2CA3-3438-97C3-E131D855B138
+  UUID: C3A84917-9898-396E-8D71-2ED58CAC8030
   Functions: 312
-  Symbols:   1352
-  CStrings:  680
+  Symbols:   1358
+  CStrings:  139
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[PSSGContext contextWithKeys:encodedStreams:] : 120 -> 124
~ -[PSSGContext isEqual:] : 200 -> 184
~ -[PSSGContext hash] : 104 -> 96
~ -[PSSGContext setKeys:] : 64 -> 12
~ -[PSSGContext setKeysWithOptions:] : 64 -> 12
~ -[PSSGContext setEncodedStreams:] : 64 -> 12
~ -[PSSGResourceRequestEntry initWithKey:stride:graphName:] : 180 -> 196
~ +[PSSGResourceRequestEntry entryWithKey:stride:] : 116 -> 120
~ +[PSSGResourceRequestEntry entryWithKey:stride:graphName:] : 128 -> 136
~ -[PSSGResourceRequestEntry isEqual:] : 204 -> 188
~ -[PSSGResourceRequestEntry hash] : 104 -> 96
~ -[PSSGResourceRequestEntry description] : 192 -> 176
~ -[PSSGResourceRequest isEqual:] : 868 -> 804
~ -[PSSGResourceRequest hash] : 176 -> 160
~ -[PSSGResourceRequest description] : 304 -> 276
~ -[PSSGResourceRequest setResourcesWanted:] : 64 -> 12
~ -[PSSGResourceRequest setResourcesNoLongerWanted:] : 64 -> 12
~ -[PSSGResourceRequest setResourcesWantedWithStrides:] : 64 -> 12
~ -[PSSGResourceRequest setResourcesNoLongerWantedWithStrides:] : 64 -> 12
~ -[PSSGClient initWithSessionName:delegate:options:] : 132 -> 136
~ -[PSSGClient initWithSessionName:delegate:options:comms:] : 224 -> 232
~ -[PSSGClient publishContext:] : 332 -> 300
~ -[PSSGClient registerClient] : 124 -> 116
~ -[PSSGClient deregisterClient] : 124 -> 116
~ -[PSSGClient handleRegisterClientAck] : 92 -> 88
~ -[PSSGClient handleDeRegisterClientAck] : 92 -> 88
~ -[PSSGClient resetInternalState] : 280 -> 260
~ -[PSSGClient fetchContextsForSessionNames:] : 252 -> 232
~ -[PSSGClient fetchContextsForSessionsProvidingKeys:] : 252 -> 232
~ -[PSSGClient requestResourcesWithStrides:failedReason:] : 1032 -> 964
~ -[PSSGClient resourceRequestCompletedWithStrides:] : 176 -> 164
~ -[PSSGClient enteringSleep] : 148 -> 136
~ -[PSSGClient exitingSleep] : 148 -> 136
~ -[PSSGClient resourcesAreStopped:] : 176 -> 164
~ -[PSSGClient resourceRequestsFailed:reason:] : 184 -> 172
~ -[PSSGClient resourcesNoLongerWantedProcessed:] : 176 -> 164
~ -[PSSGClient resourcesNoLongerWantedFailed:] : 176 -> 164
~ -[PSSGClient setupRequestsAreComplete:] : 176 -> 164
~ -[PSSGClient failedToProcessSetupRequests:] : 176 -> 164
~ -[PSSGClient pauseRequestsAreComplete:] : 176 -> 164
~ -[PSSGClient failedToProcessPauseRequests:] : 176 -> 164
~ -[PSSGClient updateGraphs:] : 176 -> 164
~ -[PSSGClient requestAllGraphs:] : 220 -> 204
~ -[PSSGClient requestProcessMonitorStats] : 192 -> 176
~ -[PSSGClient requestSystemActionStatsStats] : 192 -> 176
~ -[PSSGClient requestProcessMonitorEventLog] : 192 -> 176
~ -[PSSGClient notifySystemReplayStarting] : 148 -> 136
~ -[PSSGClient notifySystemReplayStopping] : 148 -> 136
~ -[PSSGClient updateSystemHealth:] : 184 -> 172
~ -[PSSGClient handlePublishResourceKeysAndStridesMessage:] : 300 -> 276
~ -[PSSGClient handlePublishResourceStreamsMessage:] : 244 -> 220
~ -[PSSGClient didReceiveContextForSession:] : 476 -> 424
~ -[PSSGClient handleResourceAvailabilityUpdates:] : 128 -> 120
~ -[PSSGClient handleResourceRequestWithStridesCompletedMessage:] : 512 -> 480
~ -[PSSGClient handleResourceRequestsFailedMessage:] : 104 -> 100
~ -[PSSGClient handleResourceRequestWithStridesMessage:] : 128 -> 120
~ -[PSSGClient handlePublishAllGraphs:] : 164 -> 152
~ -[PSSGClient handleReportProcessMonitorStats:] : 164 -> 152
~ -[PSSGClient handleReportSystemActionStats:] : 164 -> 152
~ -[PSSGClient handleReportProcessMonitorEventLog:] : 164 -> 152
~ -[PSSGClient publishCurrentGraphs:] : 176 -> 164
~ -[PSSGClient fetchCurrentGraphsForAllSessions] : 348 -> 316
~ -[PSSGClient handlePublishCurrentGraphsMessage:] : 164 -> 148
~ -[PSSGClient handleRequestCurrentGraphsMessage:] : 68 -> 64
~ -[PSSGClient handleCompletedCurrentGraphsRequestMessage:] : 68 -> 64
~ -[PSSGClient handleSystemReplayStarting:] : 92 -> 88
~ -[PSSGClient handleSystemReplayEnding:] : 92 -> 88
~ -[PSSGClient handleRequestGraphResubmission:] : 68 -> 64
~ -[PSSGClient handleRequestReplayResources:] : 68 -> 64
~ -[PSSGClient handleSetupResourcesMessage:] : 128 -> 120
~ -[PSSGClient handlePauseResourcesMessage:] : 128 -> 120
~ -[PSSGClient requestDPTailspinWithReason:] : 176 -> 164
~ -[PSSGClient resourceAvailabilityHasChangedTo:] : 176 -> 164
~ -[PSSGClient requestResourceAvailabilityUpdates:] : 176 -> 164
~ -[PSSGClient stopResourceAvailabilityUpdates:] : 176 -> 164
~ -[PSSGClient deregisterSelfAfterCrash] : 148 -> 136
~ -[PSSGClient setSessionName:] : 64 -> 12
~ -[PSSGClient setComms:] : 64 -> 12
~ -[PSSGClient setSessionsPendingContexts:] : 64 -> 12
~ -[PSSGClient setResourceKeysPendingContexts:] : 64 -> 12
~ -[PSSGClient setResourceKeysPendingProduction:] : 64 -> 12
~ -[PSSGClient setContextMap:] : 64 -> 12
~ -[PSSGClient setAllGraphs:] : 64 -> 12
~ -[PSSGClient setProcessMonitorStats:] : 64 -> 12
~ -[PSSGClient setSystemActionStats:] : 64 -> 12
~ -[PSSGClient setProcessMonitorEventLog:] : 64 -> 12
~ -[PSSGClient setGraphsBySession:] : 64 -> 12
~ -[PSSGClient setCompletionSemaphore:] : 64 -> 12
~ -[PSSGClient setDeregisterSemaphore:] : 64 -> 12
~ -[PSSGComms registerForClient:] : 448 -> 420
~ -[PSSGComms deregisterForClient:] : 88 -> 84
~ -[PSSGComms dealloc] : 168 -> 160
~ -[PSSGComms sendRegisterMessage:] : 480 -> 424
~ -[PSSGComms sendDeregisterMessage:] : 100 -> 96
~ -[PSSGComms sendMessage:] : 248 -> 244
~ -[PSSGComms sendMessageonReceiveChannel:withReceiverPort:] : 224 -> 220
~ -[PSSGComms receiveMessageLoop] : 10176 -> 9432
~ -[PSSGComms setReceiveMessageThread:] : 64 -> 12
~ -[PSSGMessageBase initWithType:string1:stringSet1:stringSet2:data:] : 212 -> 224
~ -[PSSGMessageBase count1] : 60 -> 56
~ -[PSSGMessageBase count2] : 60 -> 56
~ -[PSSGMessageBase dataLength] : 60 -> 56
~ -[PSSGMessageBase initWithRawMessage:] : 476 -> 452
~ -[PSSGMessageBase serialize] : 796 -> 788
~ -[PSSGMessageBase isEqual:] : 416 -> 384
~ -[PSSGMessageBase hash] : 192 -> 176
~ -[PSSGMessageBase setString1:] : 64 -> 12
~ -[PSSGMessageBase setStringSet1:] : 64 -> 12
~ -[PSSGMessageBase setStringSet2:] : 64 -> 12
~ -[PSSGMessageBase setData:] : 64 -> 12
~ +[PSSGMessageRegister messageWithSessionName:] : 100 -> 96
~ +[PSSGResourceOptions optionsWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:availability:] : 144 -> 148
~ -[PSSGResourceOptions initWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:availability:] : 184 -> 192
~ -[PSSGResourceOptions isEqual:] : 232 -> 216
~ -[PSSGResourceOptions description] : 140 -> 132
~ -[PSSGResourceOptions setSupportedStrides:] : 64 -> 12
~ -[PSSGResourceOptions setBaseMSGSyncID:] : 64 -> 12
~ +[PSSGMessagePublishResourceKeysAndStrides messageWithKeysAndStrides:sender:] : 916 -> 880
~ -[PSSGMessagePublishResourceKeysAndStrides resourceOptions] : 648 -> 604
~ -[PSSGMessagePublishResourceKeysAndStrides isEqual:] : 256 -> 252
~ -[PSSGMessagePublishResourceKeysAndStrides description] : 152 -> 140
~ +[PSSGMessageSetResourceAvailability messageWithKeysAndResourceAvailability:sender:] : 468 -> 464
~ -[PSSGMessageSetResourceAvailability getResourceAvailabilityMap] : 332 -> 308
~ -[PSSGMessageSetResourceAvailability isEqual:] : 292 -> 288
~ -[PSSGMessageSetResourceAvailability hash] : 116 -> 108
~ -[PSSGMessageSetResourceAvailability description] : 152 -> 140
~ +[PSSGMessagePublishResourceStreams messageWithStreams:sender:] : 116 -> 120
~ -[PSSGMessagePublishResourceStreams description] : 152 -> 140
~ -[PSSGMessageRequestResourcesBase initWithType:sender:request:] : 180 -> 172
~ -[PSSGMessageRequestResourcesBase initWithRawMessage:] : 740 -> 700
~ -[PSSGMessageRequestResourcesBase serialize] : 1300 -> 1232
~ -[PSSGMessageRequestResourcesBase request] : 168 -> 160
~ -[PSSGMessageRequestResourcesBase isEqual:] : 272 -> 256
~ -[PSSGMessageRequestResourcesBase hash] : 116 -> 108
~ -[PSSGMessageRequestResourcesBase description] : 192 -> 176
~ -[PSSGMessageRequestResourcesBase setWantedResources:] : 64 -> 12
~ -[PSSGMessageRequestResourcesBase setNoLongerWantedResources:] : 64 -> 12
~ +[PSSGMessageRequestResourcesWithStrides messageWithResourceRequest:sender:] : 116 -> 120
~ +[PSSGMessageCompletedResourceRequestWithStrides messageWithResourceRequest:sender:] : 116 -> 120
~ +[PSSGMessageRequestContextForSessions messageWithSessionNames:sender:] : 116 -> 120
~ +[PSSGMessageRequestContextForResourceKeys messageWithResourceKeys:sender:] : 116 -> 120
~ +[PSSGMessageRequestResourceAvailabilityUpdates messageWithResourceKeys:sender:] : 116 -> 120
~ +[PSSGMessageStopResourceAvailabilityUpdates messageWithResourceKeys:sender:] : 116 -> 120
~ +[PSSGMessageSHUpdateGraphs messageWithGraphData:sender:] : 116 -> 120
~ +[PSSGMessageSHPublishAllGraphs messageWithData:sender:] : 116 -> 120
~ +[PSSGMessageSHReportProcessMonitorStats messageWithData:sender:] : 116 -> 120
~ +[PSSGMessageSHReportSystemActionStats messageWithData:sender:] : 116 -> 120
~ +[PSSGMessageSHReportProcessMonitorEventLog messageWithData:sender:] : 116 -> 120
~ +[PSSGMessageSHTriggerHealthUpdate messageWithHealthData:sender:] : 116 -> 120
~ +[PSSGMessagePublishCurrentGraphs messageWithGraphs:sender:] : 116 -> 120
~ +[PSSGMessageStoppedResources messageWithResourceKeys:sender:] : 116 -> 120
~ +[PSSGMessageResourceRequestsFailed messageWithResourceRequest:sender:reason:] : 124 -> 128
~ -[PSSGMessageResourceRequestsFailed description] : 244 -> 228
~ +[PSSGMessageResourcesNoLongerWantedProcessed messageWithResourceKeys:sender:] : 116 -> 120
~ +[PSSGMessageResourcesNoLongerWantedFailed messageWithResourceKeys:sender:] : 116 -> 120
~ +[PSSGMessageSetupResources messageWithResourceRequest:sender:] : 116 -> 120
~ +[PSSGMessageSetupResourcesCompleted messageWithResourceRequest:sender:] : 116 -> 120
~ +[PSSGMessageSetupResourcesFailed messageWithResourceKeys:sender:] : 116 -> 120
~ +[PSSGMessagePauseResources messageWithResourceKeys:sender:] : 116 -> 120
~ +[PSSGMessagePauseResourcesCompleted messageWithResourceKeys:sender:] : 116 -> 120
~ +[PSSGMessagePauseResourcesFailed messageWithResourceKeys:sender:] : 116 -> 120
~ -[PSSysHealthClient initWithName:] : 184 -> 180
~ -[PSSysHealthClient updateSystemHealth:] : 304 -> 248
~ -[PSSysHealthClient updateSystemHealthWithProfile:missesAllowed:poll_interval_secs:] : 392 -> 400
~ -[PSSysHealthClient dealloc] : 92 -> 88
~ -[PSSysHealthClient setName:] : 64 -> 12
~ -[PSSysHealthClient setSystemGraphClient:] : 64 -> 12
~ -[PSSGClient handlePublishResourceStreamsMessage:].cold.1 : 400 -> 368
~ -[PSSGComms disableSend].cold.1 : 312 -> 288
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PSSGComms>\""
- "@\"<PSSGDelegate>\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSThread\""
- "@\"PSSGClient\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^{pssg_tx_s={?={?=IIIIIi}{?=I}(?={?=IIb16b8b8}{?=^vb8b8b8b8I}{?=^vb8b8b8b8I}{?=IIb24b8}{?=Qb16b8b8I})}Q[256c](?={?=QQQQ}{?=i}{?=^v})}16"
- "@24@0:8r^{pssh_health_state_s=Q[4C]I}16"
- "@28@0:8@16i24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8Q16@24"
- "@36@0:8@16@24I32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24Q32"
- "@40@0:8Q16@24@32"
- "@44@0:8@16@24I32@36"
- "@48@0:8I16@20B28@32Q40"
- "@48@0:8Q16@24@32@40"
- "@48@0:8Q16@24@32Q40"
- "@56@0:8Q16@24@32@40@48"
- "AB"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<PSSGMessage>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B32@0:8@16^Q24"
- "I16@0:8"
- "NSObject"
- "PSSGClient"
- "PSSGComms"
- "PSSGContext"
- "PSSGMessage"
- "PSSGMessageBase"
- "PSSGMessageCompletedCurrentGraphsRequest"
- "PSSGMessageCompletedResourceRequestWithStrides"
- "PSSGMessageDeRegister"
- "PSSGMessageDeRegisterAck"
- "PSSGMessageEnteringSleep"
- "PSSGMessageExitingSleep"
- "PSSGMessageFlushCurrentGraphsForAllSessions"
- "PSSGMessagePBSLockFailure"
- "PSSGMessagePBSLockSuccess"
- "PSSGMessagePauseResources"
- "PSSGMessagePauseResourcesCompleted"
- "PSSGMessagePauseResourcesFailed"
- "PSSGMessagePublishCurrentGraphs"
- "PSSGMessagePublishResourceKeysAndStrides"
- "PSSGMessagePublishResourceStreams"
- "PSSGMessageReadyForServerRequest"
- "PSSGMessageRegister"
- "PSSGMessageRequestContextForResourceKeys"
- "PSSGMessageRequestContextForSessions"
- "PSSGMessageRequestCurrentGraphs"
- "PSSGMessageRequestCurrentGraphsForAllSessions"
- "PSSGMessageRequestDPTailspin"
- "PSSGMessageRequestGraphResubmission"
- "PSSGMessageRequestResourceAvailabilityUpdates"
- "PSSGMessageRequestResourceContext"
- "PSSGMessageRequestResourcesBase"
- "PSSGMessageRequestResourcesWithStrides"
- "PSSGMessageResourceRequestsFailed"
- "PSSGMessageResourcesNoLongerWantedFailed"
- "PSSGMessageResourcesNoLongerWantedProcessed"
- "PSSGMessageSHPublishAllGraphs"
- "PSSGMessageSHReportProcessMonitorEventLog"
- "PSSGMessageSHReportProcessMonitorStats"
- "PSSGMessageSHReportSystemActionStats"
- "PSSGMessageSHRequestAllGraphs"
- "PSSGMessageSHRequestProcessMonitorEventLog"
- "PSSGMessageSHRequestProcessMonitorStats"
- "PSSGMessageSHRequestSystemActionStats"
- "PSSGMessageSHTriggerHealthUpdate"
- "PSSGMessageSHUpdateGraphs"
- "PSSGMessageSetResourceAvailability"
- "PSSGMessageSetupResources"
- "PSSGMessageSetupResourcesCompleted"
- "PSSGMessageSetupResourcesFailed"
- "PSSGMessageStopResourceAvailabilityUpdates"
- "PSSGMessageStoppedResources"
- "PSSGMessageSystemReplayEnding"
- "PSSGMessageSystemReplayStarting"
- "PSSGMessageUserActive"
- "PSSGMessageUserInactive"
- "PSSGResourceOptions"
- "PSSGResourceRequest"
- "PSSGResourceRequestEntry"
- "PSSysHealthClient"
- "Q16@0:8"
- "T#,R"
- "T@\"<PSSGComms>\",&,N,V_comms"
- "T@\"<PSSGDelegate>\",W,N,V_delegate"
- "T@\"NSArray\",&,N,V_noLongerWantedResources"
- "T@\"NSArray\",&,N,V_resourcesNoLongerWantedWithStrides"
- "T@\"NSArray\",&,N,V_resourcesWantedWithStrides"
- "T@\"NSArray\",&,N,V_supportedStrides"
- "T@\"NSArray\",&,N,V_wantedResources"
- "T@\"NSData\",&,N,V_allGraphs"
- "T@\"NSData\",&,N,V_data"
- "T@\"NSData\",&,N,V_encodedStreams"
- "T@\"NSData\",&,N,V_processMonitorEventLog"
- "T@\"NSData\",&,N,V_processMonitorStats"
- "T@\"NSData\",&,N,V_systemActionStats"
- "T@\"NSData\",R,N"
- "T@\"NSDictionary\",&,N,V_keysWithOptions"
- "T@\"NSDictionary\",R,N"
- "T@\"NSMutableDictionary\",&,N,V_contextMap"
- "T@\"NSMutableDictionary\",&,N,V_graphsBySession"
- "T@\"NSMutableSet\",&,N,V_resourceKeysPendingContexts"
- "T@\"NSMutableSet\",&,N,V_resourceKeysPendingProduction"
- "T@\"NSMutableSet\",&,N,V_sessionsPendingContexts"
- "T@\"NSNumber\",&,N,V_baseMSGSyncID"
- "T@\"NSNumber\",R,N,V_stride"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_completionSemaphore"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_deregisterSemaphore"
- "T@\"NSSet\",&,N,V_keys"
- "T@\"NSSet\",&,N,V_resourcesNoLongerWanted"
- "T@\"NSSet\",&,N,V_resourcesWanted"
- "T@\"NSSet\",&,N,V_stringSet1"
- "T@\"NSSet\",&,N,V_stringSet2"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_sessionName"
- "T@\"NSString\",&,N,V_string1"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_graphName"
- "T@\"NSString\",R,N,V_resourceKey"
- "T@\"NSString\",W,N,V_sessionName"
- "T@\"NSThread\",&,N,V_receiveMessageThread"
- "T@\"PSSGClient\",&,N,V_systemGraphClient"
- "T@\"PSSGClient\",W,N,V_client"
- "T@\"PSSGResourceRequest\",R,N"
- "TAB,V_canSend"
- "TB,N,V_setupResumeSupported"
- "TB,V_canDeRegisterSelf"
- "TI,N,V_defaultStride"
- "TI,N,V_options"
- "TI,R,N"
- "TQ,N,V_availability"
- "TQ,N,V_lastMessageTypeSent"
- "TQ,N,V_resourceRequestsFailedReason"
- "TQ,N,V_status"
- "TQ,N,V_type"
- "TQ,R"
- "TQ,R,N,V_reason"
- "T^{PSCommsClient=},N,V_receiveChannel"
- "T^{PSCommsClient=},N,V_sendChannel"
- "Ti,N,V_pid"
- "UTF8String"
- "Vv16@0:8"
- "^[256c]"
- "^{?={pssg_tx_s={?={?=IIIIIi}{?=I}(?={?=IIb16b8b8}{?=^vb8b8b8b8I}{?=^vb8b8b8b8I}{?=IIb24b8}{?=Qb16b8b8I})}Q[256c](?={?=QQQQ}{?=i}{?=^v})}iI(?=^v^[256c]^{pssg_stream_entry_s}^{pssg_stream_request_s}^{pssg_stream_availability_entry_s})}16@0:8"
- "^{PSCommsClient=}"
- "^{PSCommsClient=}16@0:8"
- "^{_NSZone=}16@0:8"
- "_allGraphs"
- "_availability"
- "_baseMSGSyncID"
- "_canDeRegisterSelf"
- "_canSend"
- "_client"
- "_comms"
- "_completionSemaphore"
- "_contextMap"
- "_data"
- "_defaultStride"
- "_delegate"
- "_deregisterSemaphore"
- "_encodedStreams"
- "_graphName"
- "_graphsBySession"
- "_keys"
- "_keysWithOptions"
- "_lastMessageTypeSent"
- "_name"
- "_noLongerWantedResources"
- "_options"
- "_pid"
- "_processMonitorEventLog"
- "_processMonitorStats"
- "_reason"
- "_receiveChannel"
- "_receiveMessageThread"
- "_resourceKey"
- "_resourceKeysPendingContexts"
- "_resourceKeysPendingProduction"
- "_resourceRequestsFailedReason"
- "_resourcesNoLongerWanted"
- "_resourcesNoLongerWantedWithStrides"
- "_resourcesWanted"
- "_resourcesWantedWithStrides"
- "_sendChannel"
- "_serializedMessage"
- "_sessionName"
- "_sessionsPendingContexts"
- "_setupResumeSupported"
- "_status"
- "_stride"
- "_string1"
- "_stringArray"
- "_stringSet1"
- "_stringSet2"
- "_supportedStrides"
- "_systemActionStats"
- "_systemGraphClient"
- "_type"
- "_wantedResources"
- "addObject:"
- "allGraphs"
- "allKeys"
- "appendBytes:length:"
- "appendData:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "autorelease"
- "availability"
- "baseMSGSyncID"
- "bytes"
- "canDeRegisterSelf"
- "canSend"
- "cancel"
- "class"
- "client"
- "comms"
- "completionSemaphore"
- "conformsToProtocol:"
- "containsObject:"
- "contextMap"
- "contextWithKeys:encodedStreams:"
- "count"
- "count1"
- "count2"
- "countByEnumeratingWithState:objects:count:"
- "data"
- "dataLength"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithData:"
- "dataWithLength:"
- "deRegisterSelf:"
- "dealloc"
- "debugDescription"
- "defaultStride"
- "delegate"
- "deregisterClient"
- "deregisterForClient:"
- "deregisterSelfAfterCrash"
- "deregisterSemaphore"
- "description"
- "dictionary"
- "didReceiveContextForSession:"
- "didReceiveContextForSessionName:"
- "didReceiveContextForSessionProvidingKeys:"
- "didReceiveResourceAvailabilityUpdates:"
- "didReceiveResponseForResourceRequest:"
- "disableSend"
- "encodedGraphs"
- "encodedStreams"
- "enteringSleep"
- "entryWithKey:stride:"
- "entryWithKey:stride:graphName:"
- "exit"
- "exitingSleep"
- "failedToProcessPauseRequests:"
- "failedToProcessSetupRequests:"
- "fetchContextsForSessionNames:"
- "fetchContextsForSessionsProvidingKeys:"
- "fetchCurrentGraphsForAllSessions"
- "first:isEqual:"
- "getData"
- "getKeys"
- "getResourceAvailabilityMap"
- "graphName"
- "graphsBySession"
- "handleCompletedCurrentGraphsRequestMessage:"
- "handleDeRegisterClientAck"
- "handlePauseResourcesMessage:"
- "handlePublishAllGraphs:"
- "handlePublishCurrentGraphsMessage:"
- "handlePublishResourceKeysAndStridesMessage:"
- "handlePublishResourceStreamsMessage:"
- "handleRegisterClientAck"
- "handleReportProcessMonitorEventLog:"
- "handleReportProcessMonitorStats:"
- "handleReportSystemActionStats:"
- "handleRequestCurrentGraphsMessage:"
- "handleRequestGraphResubmission:"
- "handleRequestReplayResources:"
- "handleResourceAvailabilityUpdates:"
- "handleResourceRequestWithStridesCompletedMessage:"
- "handleResourceRequestWithStridesMessage:"
- "handleResourceRequestsFailedMessage:"
- "handleSetupResourcesMessage:"
- "handleSystemReplayEnding:"
- "handleSystemReplayStarting:"
- "hash"
- "i"
- "i16@0:8"
- "i28@0:8@16B24"
- "init"
- "initWithArray:"
- "initWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:availability:"
- "initWithKey:stride:graphName:"
- "initWithName:"
- "initWithRawMessage:"
- "initWithSessionName:delegate:"
- "initWithSessionName:delegate:options:"
- "initWithSessionName:delegate:options:comms:"
- "initWithTarget:selector:object:"
- "initWithType:sender:request:"
- "initWithType:sender:request:reason:"
- "initWithType:string1:"
- "initWithType:string1:data:"
- "initWithType:string1:stringSet1:stringSet2:"
- "initWithType:string1:stringSet1:stringSet2:data:"
- "initWithType:string1:stringSet:"
- "intValue"
- "intersectSet:"
- "isAbleToSend"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isPublished"
- "isRegistered"
- "isReplaying"
- "keys"
- "keysWithOptions"
- "lastMessageTypeSent"
- "length"
- "log"
- "messageWithData:sender:"
- "messageWithFilter:sender:"
- "messageWithGraphData:sender:"
- "messageWithGraphs:sender:"
- "messageWithHealthData:sender:"
- "messageWithKeysAndResourceAvailability:sender:"
- "messageWithKeysAndStrides:sender:"
- "messageWithResourceKey:"
- "messageWithResourceKeys:sender:"
- "messageWithResourceRequest:sender:"
- "messageWithResourceRequest:sender:reason:"
- "messageWithSessionName:"
- "messageWithSessionName:pid:"
- "messageWithSessionName:reason:"
- "messageWithSessionNames:sender:"
- "messageWithStreams:sender:"
- "minusSet:"
- "mutableBytes"
- "mutableCopy"
- "name"
- "noLongerWantedResources"
- "notifySystemReplayStarting"
- "notifySystemReplayStopping"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "options"
- "optionsWithDefaultStride:supportedStrides:setupSupported:baseMSGSyncID:availability:"
- "optionsWithoutStrides"
- "pauseRequestsAreComplete:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pid"
- "processMonitorEventLog"
- "processMonitorStats"
- "publishContext:"
- "publishCurrentGraphs:"
- "reason"
- "receiveChannel"
- "receiveMessageLoop"
- "receiveMessageThread"
- "registerClient"
- "registerForClient:"
- "release"
- "removeAllObjects"
- "removeObject:"
- "request"
- "requestAllGraphs:"
- "requestDPTailspinWithReason:"
- "requestProcessMonitorEventLog"
- "requestProcessMonitorStats"
- "requestResourceAvailabilityUpdates:"
- "requestResourcesWithStrides:failedReason:"
- "requestSystemActionStatsStats"
- "resetInternalState"
- "resourceAvailabilityHasChangedTo:"
- "resourceKey"
- "resourceKeysPendingContexts"
- "resourceKeysPendingProduction"
- "resourceOptions"
- "resourceRequestCompletedWithStrides:"
- "resourceRequestsFailed:reason:"
- "resourceRequestsFailedReason"
- "resourcesAreStopped:"
- "resourcesNoLongerWanted"
- "resourcesNoLongerWantedFailed:"
- "resourcesNoLongerWantedProcessed:"
- "resourcesNoLongerWantedWithStrides"
- "resourcesWanted"
- "resourcesWantedWithStrides"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "sendChannel"
- "sendDeregisterMessage:"
- "sendMessage:"
- "sendMessageonReceiveChannel:withReceiverPort:"
- "sendRegisterMessage:"
- "sender"
- "serialize"
- "serverRequestToPauseResources:"
- "serverRequestToSetupResources:"
- "serverRequestedCurrentGraphs"
- "serverRequestedGraphResubmission"
- "serverRequestedReplayResources"
- "serverRequestedResourcesWithStrides:"
- "sessionName"
- "sessionsPendingContexts"
- "set"
- "setAllGraphs:"
- "setAvailability:"
- "setBaseMSGSyncID:"
- "setCanDeRegisterSelf:"
- "setCanSend:"
- "setClient:"
- "setComms:"
- "setCompletionSemaphore:"
- "setContextMap:"
- "setData:"
- "setDefaultStride:"
- "setDelegate:"
- "setDeregisterSemaphore:"
- "setEncodedStreams:"
- "setGraphsBySession:"
- "setKeys:"
- "setKeysWithOptions:"
- "setLastMessageTypeSent:"
- "setName:"
- "setNoLongerWantedResources:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setPid:"
- "setProcessMonitorEventLog:"
- "setProcessMonitorStats:"
- "setPublished:"
- "setReceiveChannel:"
- "setReceiveMessageThread:"
- "setRegistered:"
- "setReplaying:"
- "setResourceKeysPendingContexts:"
- "setResourceKeysPendingProduction:"
- "setResourceRequestsFailedReason:"
- "setResourcesNoLongerWanted:"
- "setResourcesNoLongerWantedWithStrides:"
- "setResourcesWanted:"
- "setResourcesWantedWithStrides:"
- "setSendChannel:"
- "setSessionName:"
- "setSessionsPendingContexts:"
- "setSetupResumeSupported:"
- "setStatus:"
- "setString1:"
- "setStringSet1:"
- "setStringSet2:"
- "setSupportedStrides:"
- "setSystemActionStats:"
- "setSystemGraphClient:"
- "setThreadPriority:"
- "setType:"
- "setWantedResources:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObject:"
- "setupRequestsAreComplete:"
- "setupResumeSupported"
- "start"
- "stats"
- "status"
- "stopResourceAvailabilityUpdates:"
- "stride"
- "string1"
- "stringByAppendingPathExtension:"
- "stringSet1"
- "stringSet2"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "stringifyHealthData:"
- "superclass"
- "supportedStrides"
- "systemActionStats"
- "systemGraphClient"
- "systemReplayEnding"
- "systemReplayStarting"
- "type"
- "unionSet:"
- "unsignedIntValue"
- "updateGraphs:"
- "updateSystemHealth:"
- "updateSystemHealthWithProfile:missesAllowed:poll_interval_secs:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@\"<PSSGMessage>\"16"
- "v24@0:8@\"PSSGClient\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8^{?={pssg_tx_s={?={?=IIIIIi}{?=I}(?={?=IIb16b8b8}{?=^vb8b8b8b8I}{?=^vb8b8b8b8I}{?=IIb24b8}{?=Qb16b8b8I})}Q[256c](?={?=QQQQ}{?=i}{?=^v})}{?=II}}16"
- "v24@0:8^{PSCommsClient=}16"
- "v24@0:8^{pssh_health_state_s=Q[4C]I}16"
- "v32@0:8@16Q24"
- "v36@0:8Q16@24I32"
- "waitForMessageOnReceiveChannel:"
- "wantedResources"
- "zone"
- "{?=\"message\"{pssg_tx_s=\"header\"{?=\"header\"{?=\"msgh_bits\"I\"msgh_size\"I\"msgh_remote_port\"I\"msgh_local_port\"I\"msgh_voucher_port\"I\"msgh_id\"i}\"body\"{?=\"msgh_descriptor_count\"I}\"ool_port_data\"(?=\"port\"{?=\"name\"I\"pad1\"I\"pad2\"b16\"disposition\"b8\"type\"b8}\"out_of_line\"{?=\"address\"^v\"deallocate\"b8\"copy\"b8\"pad1\"b8\"type\"b8\"size\"I}\"ool_ports\"{?=\"address\"^v\"deallocate\"b8\"copy\"b8\"disposition\"b8\"type\"b8\"count\"I}\"type\"{?=\"pad1\"I\"pad2\"I\"pad3\"b24\"type\"b8}\"guarded_port\"{?=\"context\"Q\"flags\"b16\"disposition\"b8\"type\"b8\"name\"I})}\"type\"Q\"string1\"[256c]\"\"(?=\"\"{?=\"countArray1\"Q\"countArray2\"Q\"dataLength\"Q\"uint1\"Q}\"\"{?=\"pid\"i}\"\"{?=\"notifications\"^v})}\"pid\"i\"oolDataLength\"I\"\"(?=\"oolData\"^v\"strings\"^[256c]\"streamsWithStrides\"^{pssg_stream_entry_s}\"streamRequest\"^{pssg_stream_request_s}\"streamAvailability\"^{pssg_stream_availability_entry_s})}"

```
