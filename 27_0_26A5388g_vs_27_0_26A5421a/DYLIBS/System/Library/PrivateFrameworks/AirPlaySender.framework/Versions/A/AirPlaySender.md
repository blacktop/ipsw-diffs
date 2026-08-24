## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/Versions/A/AirPlaySender`

```diff

-980.71.1.0.0
-  __TEXT.__text: 0x1d3c7c
+980.77.5.3.0
+  __TEXT.__text: 0x1d5f60
   __TEXT.__objc_methlist: 0x92c
-  __TEXT.__const: 0xd4f0
-  __TEXT.__gcc_except_tab: 0x5ec
-  __TEXT.__cstring: 0x702af
+  __TEXT.__const: 0xd580
+  __TEXT.__gcc_except_tab: 0x62c
+  __TEXT.__cstring: 0x70df9
   __TEXT.__dlopen_cstrs: 0x164
-  __TEXT.__oslogstring: 0xb29
-  __TEXT.__unwind_info: 0x4438
+  __TEXT.__oslogstring: 0xb55
+  __TEXT.__unwind_info: 0x44c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x42c8
+  __DATA_CONST.__const: 0x4318
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_selrefs: 0xb08
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0x1dd8
-  __AUTH_CONST.__const: 0x71d0
-  __AUTH_CONST.__cfstring: 0x10480
+  __DATA_CONST.__got: 0x1de0
+  __AUTH_CONST.__const: 0x7200
+  __AUTH_CONST.__cfstring: 0x10540
   __AUTH_CONST.__objc_const: 0xc58
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x1b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9003
-  Symbols:   8760
-  CStrings:  9175
+  Functions: 9056
+  Symbols:   8797
+  CStrings:  9188
 
Symbols:
+ GCC_except_table129
+ GCC_except_table23
+ _APBrowserControllerCreateTransportDevice
+ _APBrowserControllerDeregisterDiscoveryQueryObserver
+ _APBrowserControllerRegisterDiscoveryQueryObserver
+ _APBrowserDeregisterDiscoveryQueryObserver
+ _APBrowserRegisterDiscoveryQueryObserver
+ _APTNANDataSessionAutoPairWithCompletion
+ _FigCFDictionaryFindAnyKeyForValue
+ _FigSignalErrorAtGM
+ _OBJC_CLASS_$_NSOperationQueue
+ ___block_descriptor_48_e24_v20?0^{__CFNumber=}8I16l
+ ___block_descriptor_48_e8_32o40r_e8_v12?0i8l
+ ___block_descriptor_80_e5_v8?0l
+ ___manager_handleProactivePairingDeviceFound_block_invoke
+ ___manager_performProactiveNANAutoPair_block_invoke
+ ___manager_performProactiveNANBootstrap_block_invoke
+ ___manager_registerDiscoveryQueryObserver_block_invoke
+ ___manager_registerDiscoveryQueryObserver_block_invoke_2
+ __manager_registerDiscoveryQueryObserver_block_invoke_2
+ _emp_createEndpointPlusCreationOptions
+ _emp_isCacheableEndpointID
+ _emp_unmarkCacheableClusterID
+ _emp_unmarkCacheableEndpointID
+ _endpointCluster_copyAggregatedTransportType
+ _endpointCluster_updateCurrentAggregatedTransportType
+ _kAPEndpointStreamProperty_IsAggregateStream
+ _kAPEndpointStreamProperty_TerminusPeerCoordinator
+ _manager_createLookupOnlyTransportDeviceForDeviceID
+ _manager_invokeSendCommandCompletionBlock
+ _manager_performProactiveNANAutoPair
+ _manager_performProactiveNANBootstrap
+ _manager_registerDiscoveryQueryObserver
+ _objc_msgSend$addOperationWithBlock:
+ _objc_msgSend$cancelAllOperations
+ _objc_msgSend$setMaxConcurrentOperationCount:
+ emp_isCacheableEndpointID
+ epp_SetDelegate
+ epp_SetDelegateAuthorization
+ epp_SetDelegateVolumeAndMute
+ manager_createLookupOnlyTransportDeviceForDeviceID
+ streamAggregateAudio_SetProperty
- GCC_except_table22
- _FigSignalErrorAt3
- __completionCallbackContext_computeState_block_invoke
- _emp_isEndpointCacheable
- emp_isEndpointCacheable
CStrings:
+ "%s signalled err=%d at <>:%d"
+ "6G"
+ "980.77.5.3"
+ "<ProactiveNANPairing> [%{ptr}] Already proactively %s device %@; skipping"
+ "<ProactiveNANPairing> [%{ptr}] Clearing all proactive NAN AutoPairing tracking (%ld devices)"
+ "<ProactiveNANPairing> [%{ptr}] Clearing all proactive NAN bootstrapping tracking (%ld devices)"
+ "<ProactiveNANPairing> [%{ptr}] Clearing proactive NAN AutoPairing tracking for removed device %@"
+ "<ProactiveNANPairing> [%{ptr}] Clearing proactive NAN bootstrapping tracking for removed device %@"
+ "<ProactiveNANPairing> [%{ptr}] Deregistering discovery query observer for unpaired NAN Responsive Audio HomePods"
+ "<ProactiveNANPairing> [%{ptr}] Failed to activate RC endpoint [%{ptr}] for NAN bootstrapping device %@: %#m"
+ "<ProactiveNANPairing> [%{ptr}] Failed to copy NAN data session to AutoPair device %@: %#m"
+ "<ProactiveNANPairing> [%{ptr}] Failed to create RC endpoint for NAN bootstrapping device %@: %#m"
+ "<ProactiveNANPairing> [%{ptr}] Failed to send PerformNANPKExchange to RC endpoint [%{ptr}] for device %@: %#m"
+ "<ProactiveNANPairing> [%{ptr}] Failed to start AutoPair for device %@: %#m"
+ "<ProactiveNANPairing> [%{ptr}] NAN PK bootstrapping exchange failed for device %@%?{end}: %#m"
+ "<ProactiveNANPairing> [%{ptr}] NAN PK bootstrapping exchange timed out for device %@"
+ "<ProactiveNANPairing> [%{ptr}] Predicate matched device: %@ %{flags}"
+ "<ProactiveNANPairing> [%{ptr}] Proactive AutoPair of device %@ %s%?{end}: %#m"
+ "<ProactiveNANPairing> [%{ptr}] Proactive AutoPair of device %@ timed out"
+ "<ProactiveNANPairing> [%{ptr}] Proactively AutoPairing device %@"
+ "<ProactiveNANPairing> [%{ptr}] Proactively performing NAN PK bootstrapping for device %@ over RC endpoint [%{ptr}]"
+ "<ProactiveNANPairing> [%{ptr}] Registering discovery query observer for unpaired NAN Responsive Audio HomePods"
+ "AirPlayXPCServicesStart took %lld ms (err=%d)\n"
+ "AutoPairing"
+ "Boolean emp_isCacheableEndpointID(FigEndpointManagerRef, CFStringRef, APEndpointPlusType)"
+ "Bootstrapping"
+ "CachingMetrics"
+ "InternalManager"
+ "IsAggregateStream"
+ "IsClusterSubEndpoint"
+ "OSStatus APEndpointPlusCreate(APEndpointPlusType, CFDictionaryRef _Nullable, FigEndpointRef *)"
+ "OSStatus emp_processRealEndpointFound(FigEndpointManagerRef, CFStringRef, FigEndpointRef, APEndpointPlusType)"
+ "OSStatus epp_SetDelegate(FigEndpointRef, const FigEndpointDelegate *)"
+ "OSStatus epp_SetDelegateRemoteControl(FigEndpointRef, const FigEndpointDelegateRemoteControl *)"
+ "OSStatus epp_SetDelegateRouting(FigEndpointRef, const FigEndpointDelegateRouting *)"
+ "OSStatus epp_SetDelegateVolumeAndMute(FigEndpointRef, const FigEndpointDelegateVolumeAndMute *)"
+ "OSStatus manager_performProactiveNANAutoPair(FigEndpointManagerRef, CFNumberRef)"
+ "OSStatus manager_performProactiveNANBootstrap(FigEndpointManagerRef, CFNumberRef)"
+ "OSStatus manager_registerDiscoveryQueryObserver(FigEndpointManagerRef)"
+ "OSStatus manager_registerDiscoveryQueryObserver(FigEndpointManagerRef)_block_invoke_2"
+ "Relay"
+ "SenderDeviceID: %llu ReceiverDeviceID: %llu"
+ "[%{ptr}] Establish PTP Clock=%s (isClusterLeader=%s isHTSession=%s isSPPCSession=%s clusterType=%@ transportType=%@ isStereoBuddyConnection=%s)"
+ "[%{ptr}] Handling NAN Infra%s failure as a startup failure.\n"
+ "[%{ptr}] Mark cacheable device %@"
+ "[%{ptr}] Mark cacheable subEndpoint %@ for cluster %@"
+ "[%{ptr}] Setting authorization delegate proxy [%{ptr}] on inner [%{ptr}]"
+ "[%{ptr}] Setting remote control delegate proxy [%{ptr}] on inner [%{ptr}]"
+ "[%{ptr}] Setting routing delegate proxy [%{ptr}] on inner [%{ptr}]"
+ "[%{ptr}] Setting volume delegate proxy [%{ptr}] on inner [%{ptr}]"
+ "[%{ptr}] Unmark cacheable device %@"
+ "[%{ptr}] Unmark cacheable subEndpoint %@ for cluster %@"
+ "[%{ptr}] Update authorization delegate [%{ptr}]"
+ "[%{ptr}] Update remote control delegate [%{ptr}]"
+ "[%{ptr}] Update routing delegate [%{ptr}]"
+ "[%{ptr}] Update volume delegate [%{ptr}]"
+ "com.apple.airplay.apendpointManager.nanProactivePairing"
+ "emp_processRealEndpointFound"
+ "emp_processRealEndpointLost"
+ "emp_processRealEndpointsFound"
+ "enableProactiveNANPairingOverride"
+ "manager_clearProactivePairingTrackingForDeviceID"
+ "manager_copyExistingEndpointTransportDeviceForDeviceID"
+ "manager_createLookupOnlyTransportDeviceForDeviceID"
+ "manager_handleProactivePairingDeviceFound"
+ "manager_performProactiveNANAutoPair"
+ "manager_performProactiveNANBootstrap"
+ "manager_registerDiscoveryQueryObserver"
+ "v20@?0^{__CFNumber=}8I16"
+ "void emp_markCacheableClusterID(FigEndpointManagerRef, CFStringRef, CFStringRef)"
+ "void emp_markCacheableEndpointID(FigEndpointManagerRef, CFStringRef)"
+ "void emp_unmarkCacheableClusterID(FigEndpointManagerRef, CFStringRef)"
+ "void emp_unmarkCacheableEndpointID(FigEndpointManagerRef, CFStringRef)"
+ "void epp_updateDelegateRemoteControl(FigEndpointRef, const FigEndpointDelegateRemoteControl *)"
+ "void epp_updateDelegateRouting(FigEndpointRef, const FigEndpointDelegateRouting *)"
+ "void epp_updateDelegateVolumeAndMute(FigEndpointRef, const FigEndpointDelegateVolumeAndMute *)"
+ "void manager_clearAllProactivePairingTracking(FigEndpointManagerRef)"
+ "void manager_clearProactivePairingTrackingForDeviceID(FigEndpointManagerRef, CFNumberRef)"
+ "void manager_deregisterDiscoveryQueryObserver(FigEndpointManagerRef)"
+ "void manager_handleProactivePairingDeviceFound(FigEndpointManagerRef, CFNumberRef, APBrowserDevicePredicate)"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "-108"
- "-876"
- "-877"
- "-878"
- "-879"
- "-880"
- "980.71.1"
- "APAudioEngineBufferedAdapter.c"
- "APAudioSourceSharedMemory.c"
- "APEndpoint.m"
- "APEndpointPlaybackSessionRemoteControl.m"
- "APEndpointStreamAggregateAudio.c"
- "APSampleBufferConsumerForEndpointStreamAudioEngine.c"
- "APVirtualDisplayTestSink.c"
- "Action not supported"
- "Allocation error"
- "Audio source has been invalidated"
- "Boolean emp_isEndpointCacheable(FigEndpointManagerRef, CFStringRef, APEndpointPlusType)"
- "Cannot register path"
- "Failed allocating audio buffer"
- "Failed to create bufferMemObject"
- "Failed to create deep copy"
- "Failed to create stateMemObject"
- "Failed to de-serialize"
- "Failed to serialize"
- "Invalid Trigger Token"
- "Item is NULL"
- "NULL audioEngine"
- "NULL bufferMemObject in message"
- "NULL stateMemObject in message"
- "NULL trigger"
- "NULL triggerTokenOut"
- "No data in response"
- "No incoming message"
- "No matched request found"
- "No trigger installed"
- "OSStatus APEndpointPlusCreate(APEndpointPlusType, APEndpointPlusCreationContext * _Nullable, FigEndpointRef *)"
- "OSStatus emp_ensureRealEndpointWithType(FigEndpointManagerRef, CFStringRef, FigEndpointRef, APEndpointPlusType)"
- "Object invalidated"
- "Only support one trigger installed at a time"
- "[%{ptr}] Establish PTP Clock=%s (isClusterLeader=%s isHTSession=%s isSPPCSession=%s isRASession=%s isStereoBuddyConnection=%s)"
- "[%{ptr}] Handling NAN InfraRelay failure as a startup failure.\n"
- "[%{ptr}] Setting authorization delegate [%{ptr}] on inner [%{ptr}]"
- "[%{ptr}] Setting proxy authorization delegate [%{ptr}] on inner [%{ptr}]"
- "alloc failed"
- "bufferMemory region maps to NULL"
- "bufferMemorySize is zero"
- "can't find valid video track"
- "emp_ensureRealEndpointWithType"
- "emp_filterAndAddNewlyAvailableRealEndpoints"
- "emp_removeRealEndpointWithType"
- "err"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_Invalidated"
- "kCMBaseObjectError_ParamErr"
- "kCMBaseObjectError_ValueNotAvailable"
- "kFigEndpointError_AllocationFailed"
- "kFigEndpointPlaybackSessionError_AllocationFailed"
- "kFigEndpointPlaybackSessionError_InvalidParameter"
- "kFigEndpointStreamAudioEngineError_AllocationFailed"
- "messageID is missing in response event"
- "sbceas_InstallLowWaterTrigger_block_invoke"
- "sbceas_RemoveLowWaterTrigger_block_invoke"
- "stateMemObject maps to NULL"
- "stateMemoryLength < sizeof(RingState)"
- "type is missing in response event"
```
