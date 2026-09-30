## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-950.7.1.0.0
-  __TEXT.__text: 0x20fe58
+960.4.3.0.0
+  __TEXT.__text: 0x210ae8
   __TEXT.__auth_stubs: 0x5700
   __TEXT.__objc_methlist: 0x7d4
-  __TEXT.__cstring: 0x852c5
+  __TEXT.__cstring: 0x857be
   __TEXT.__const: 0x101e0
   __TEXT.__gcc_except_tab: 0x9f8
   __TEXT.__dlopen_cstrs: 0x671
   __TEXT.__oslogstring: 0x7c5
-  __TEXT.__unwind_info: 0x52f0
+  __TEXT.__unwind_info: 0x52f8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x1c5
   __TEXT.__objc_methname: 0x2220
   __TEXT.__objc_methtype: 0xd78
   __TEXT.__objc_stubs: 0x1f20
   __DATA_CONST.__got: 0x1ff0
-  __DATA_CONST.__const: 0x6ee8
+  __DATA_CONST.__const: 0x6f10
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_arraydata: 0x170
   __AUTH_CONST.__auth_got: 0x2b90
   __AUTH_CONST.__const: 0x72a8
-  __AUTH_CONST.__cfstring: 0x12ea0
+  __AUTH_CONST.__cfstring: 0x12f60
   __AUTH_CONST.__objc_const: 0xec8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_intobj: 0x138

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A9D7F0CA-5D24-3F1F-B09A-1442C9C7A553
-  Functions: 10656
-  Symbols:   26624
-  CStrings:  13729
+  UUID: 5D43D927-A94A-3108-8FBB-99A41A83FF48
+  Functions: 10660
+  Symbols:   26637
+  CStrings:  13775
 
Symbols:
+ _FigSignalErrorAt3
+ ___block_descriptor_tmp.124
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.188
+ ___block_descriptor_tmp.200
+ ___block_descriptor_tmp.282
+ ___block_descriptor_tmp.284
+ ___block_descriptor_tmp.287
+ ___block_descriptor_tmp.323
+ ___block_descriptor_tmp.334
+ ___block_literal_global.176
+ ___block_literal_global.182
+ ___block_literal_global.186
+ ___block_literal_global.603
+ ___endpointAggregate_generateRemoteSubEndpointModelMetrics_block_invoke
+ _carEndpoint_updateErrorStatusIfNotSet.cold.2
+ _endpointAggregate_gatherTopologyState
+ _endpointAggregate_reportTopologyChangeMetrics
- _FigSignalErrorAtGM
- ___block_descriptor_tmp.121
- ___block_descriptor_tmp.123
- ___block_descriptor_tmp.125
- ___block_descriptor_tmp.164
- ___block_descriptor_tmp.167
- ___block_descriptor_tmp.276
- ___block_descriptor_tmp.278
- ___block_descriptor_tmp.281
- ___block_descriptor_tmp.317
- ___block_descriptor_tmp.328
- ___block_literal_global.173
- ___block_literal_global.179
- ___block_literal_global.183
- ___block_literal_global.600
- ___carEndpoint_Dissociate_block_invoke_2.cold.1
- _carEndpoint_notifyRoutingDelegateAboutFailure.cold.1
- _endpointAggregate_addEndpointInternal.cold.10
- _endpointAggregate_removeEntryForSubEndpoint.cold.1
- _endpointAggregate_removeEntryForSubEndpoint.cold.2
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "960.4.3"
+ "APAudioEngineBufferedAdapter.c"
+ "APEndpoint.m"
+ "APEndpointPlaybackSessionRemoteControl.m"
+ "APEndpointStreamAggregateAudio.c"
+ "APVirtualDisplayTestSink.c"
+ "Action not supported"
+ "Allocation error"
+ "Cannot register path"
+ "Failed allocating audio buffer"
+ "Failed to create deep copy"
+ "Failed to de-serialize"
+ "Failed to serialize"
+ "Item is NULL"
+ "No data in response"
+ "No incoming message"
+ "No matched request found"
+ "OSStatus endpointAggregate_addEntryForSubEndpoint(FigEndpointAggregateRef, FigEndpointRef, Boolean *, uint32_t *)"
+ "OSStatus endpointAggregate_reportTopologyChangeMetrics(FigEndpointRef, TopologyChangeMetrics *, uint64_t)"
+ "Object invalidated"
+ "[%{ptr}] Topology change metrics: %@\n"
+ "alloc failed"
+ "can't find valid video track"
+ "connectionDurationSecs"
+ "containsLocal"
+ "enablePWDKeyExchangePreRoll"
+ "endpointAggregate_generateRemoteSubEndpointModelMetrics_block_invoke"
+ "endpointAggregate_reportTopologyChangeMetrics"
+ "err"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_Invalidated"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_ValueNotAvailable"
+ "kFigEndpointError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_InvalidParameter"
+ "kFigEndpointStreamAudioEngineError_AllocationFailed"
+ "messageID is missing in response event"
+ "receiverModelContainedInGroup"
+ "remoteEndpointCountBucket"
+ "totalConnectionDurationSecs"
+ "type is missing in response event"
- "%s signalled err=%d at <>:%d"
- "950.7.1"
- "OSStatus endpointAggregate_addEntryForSubEndpoint(FigEndpointAggregateRef, FigEndpointRef, uint32_t *)"

```
