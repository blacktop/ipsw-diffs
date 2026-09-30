## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-800.68.1.0.0
-  __TEXT.__text: 0x1c402c
-  __TEXT.__auth_stubs: 0x5060
+830.2.0.0.0
+  __TEXT.__text: 0x1c6ac0
+  __TEXT.__auth_stubs: 0x5010
   __TEXT.__objc_methlist: 0x340
-  __TEXT.__cstring: 0x719be
-  __TEXT.__const: 0xfe40
+  __TEXT.__cstring: 0x71c6d
+  __TEXT.__const: 0xfd30
   __TEXT.__gcc_except_tab: 0x3d8
   __TEXT.__oslogstring: 0x69f
-  __TEXT.__unwind_info: 0x2a58
-  __TEXT.__eh_frame: 0xb28
+  __TEXT.__unwind_info: 0x2a78
+  __TEXT.__eh_frame: 0xaa8
   __TEXT.__objc_classname: 0x174
   __TEXT.__objc_methname: 0x19a5
   __TEXT.__objc_methtype: 0xa56
   __TEXT.__objc_stubs: 0x1760
-  __DATA_CONST.__got: 0x1d18
+  __DATA_CONST.__got: 0x1d20
   __DATA_CONST.__const: 0x5e78
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x680
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x2840
+  __AUTH_CONST.__auth_got: 0x2818
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x7d20
-  __AUTH_CONST.__cfstring: 0x10be0
+  __AUTH_CONST.__const: 0x79c0
+  __AUTH_CONST.__cfstring: 0x10bc0
   __AUTH_CONST.__objc_const: 0x1178
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x608
   __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x18360
+  __DATA.__data: 0x18320
   __DATA.__bss: 0x9a8
-  __DATA.__common: 0x9f0
+  __DATA.__common: 0xa04
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xd30
   __DATA_DIRTY.__bss: 0x2d8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3301
-  Symbols:   6261
-  CStrings:  9715
+  Functions: 3327
+  Symbols:   6257
+  CStrings:  9700
 
Symbols:
+ _APSAudioFormatDescriptionListCopyRichestFormatAsFigEndpointStreamAudioFormatDescription
+ _CFPropertyListCreateFromFilePath
+ _FigSignalErrorAt
+ _kAPEndpointClusterActivateOptionKey_ForceClusterChange
+ _kAPSenderSessionShowInfoKey_IsCancelled
+ _kFigEndpointStreamProperty_RichestAudioFormatDescription
- _APSLocalAudioCapabilityMonitorInitialize
- _FigSignalErrorAt3
- _fclose
- _fig_log_get_emitter
- _fopen
- _fprintf
- _fscanf
- _kAPEndpointShowInfoKey_NAPS
- _kAPEndpointShowInfoKey_SelectionState
- _kAPEndpointShowInfoKey_VideoPlaying
- _kAPEndpointShowInfoSelectionState_AV
- _kAPEndpointShowInfoSelectionState_None
- _kAPEndpointShowInfoSelectionState_Screen
- _remove
CStrings:
+ " State=%!c(MISSING)"
+ "### [%!{(MISSING)ptr}] Failed to set up senderNetworkClock [%!{(MISSING)ptr}], err = %!m(MISSING)\n"
+ "830.2"
+ "APEndpointManagerLocalClusterAction manager_determineLocalClusterAction(FigEndpointManagerRef, FigEndpointRef)"
+ "BAE [%!{(MISSING)ptr}] %!s(MISSING)[0x%!X(MISSING)] Reset sbufEndOutputPTS(%!f(MISSING)). SbufOPTS(%!f(MISSING))"
+ "Boolean apsession_determineTransportAvailabilityAndWaitIfNeeded(APSenderSessionRef, APSenderSessionConnectionType, APSenderSessionConnectionType, APSenderSessionConnectionType *, Boolean, OSStatus *)"
+ "Boolean apsession_isCancelled(APSenderSessionRef)"
+ "CFAbsoluteTime carManager_getLastSessionDeactivationTime(FigEndpointManagerRef)"
+ "CarPlayActiveEndpoint.plist"
+ "Cluster change: Deactivating obsolete cluster endpoint [%!{(MISSING)ptr}]\n"
+ "Cluster change: Old cluster endpoint [%!{(MISSING)ptr}] vs. new [%!{(MISSING)ptr}]\n"
+ "EAC3/48000/5.1"
+ "ForceClusterChange"
+ "Last Session deactivation time: %!f(MISSING)\n"
+ "Local cluster action [%!{(MISSING)ptr}]: activate b/c HT ATV not in use\n"
+ "Local cluster action [%!{(MISSING)ptr}]: activate b/c cluster leader & not in use\n"
+ "Local cluster action [%!{(MISSING)ptr}]: deactivate b/c not cluster leader & in use\n"
+ "Local cluster action [%!{(MISSING)ptr}]: none b/c HT ATV not in use\n"
+ "Local cluster action [%!{(MISSING)ptr}]: none b/c cluster leader (%!s(MISSING)) == not in use (%!s(MISSING))\n"
+ "Local endpoint [%!{(MISSING)ptr}] cluster ID changed: %!@(MISSING) -> %!@(MISSING) / cluster [%!{(MISSING)ptr}] -> [%!{(MISSING)ptr}]. Simulate system request to stop.\n"
+ "OSStatus apsession_determineTransportAvailabilityAndPreferredConnectionType(APSenderSessionRef, APSenderSessionConnectionType *, APSenderSessionConnectionType *, Boolean *)"
+ "Reporting analytics for previous session: %!@(MISSING)\n"
+ "Storing CarPlay endpoint activation state (active: %!d(MISSING), PID: %!d(MISSING), EndpointActivationStateTime: %!f(MISSING))\n"
+ "[%!{(MISSING)ptr}] <AirPlayActivation> Forcing cluster failure for deactivation"
+ "[%!{(MISSING)ptr}] APSLocalAudioCapabilityMonitor [%!{(MISSING)ptr}]"
+ "[%!{(MISSING)ptr}] Cluster change: Deactivation required (NeedsDeactivationForClusterChange notification). Starting suppression of local endpoints\n"
+ "[%!{(MISSING)ptr}] Network clock [%!{(MISSING)ptr}] started\n"
+ "[%!{(MISSING)ptr}] session cancelled"
+ "activation_time"
+ "apsession_determineTransportAvailabilityAndPreferredConnectionType"
+ "carplaysource_WritePackets"
+ "deactivation_time"
+ "isCancelled"
+ "void carManager_storeEndpointActivationStateForCurrentProcess(FigEndpointManagerRef, Boolean, CFAbsoluteTime)"
+ "void endpointaggregate_handleSubEndpointUpdateFeaturesCompletedInternal(FigEndpointRef, FigEndpointFeatures, uint64_t, OSStatus, SubEndpointUpdateFeaturesCallbackContext *)"
+ "void localStream_getSharedInstanceOfAPSLocalAudioCapabilityMonitorIfAvaliable(FigEndpointStreamRef)"
+ "void manager_deactivateLocalCluster(FigEndpointManagerRef, FigEndpointRef, Boolean)"
- " Sel=%!@(MISSING)"
- " State=%!c(MISSING)%!c(MISSING)"
- "### [%!{(MISSING)ptr}] Failed to set up senderNetworkClock err = %!m(MISSING)\n"
- "%!(BADWIDTH)%!s(MISSING) %!d(MISSING)"
- "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
- "%!s(MISSING): %!d(MISSING)\n"
- "(Fig)"
- "800.68.1"
- "A/V"
- "APEndpoint.c"
- "APEndpointPlaybackSessionRemoteControl.m"
- "APEndpointStreamAggregateAudio.c"
- "APVirtualDisplayTestSink.c"
- "Action not supported"
- "Allocation error"
- "BAE [%!{(MISSING)ptr}] %!s(MISSING)[0x%!X(MISSING)] Reset sbufEndOutputPTS"
- "Boolean apsession_determineTransportAvailabilityAndWaitIfNeeded(APSenderSessionRef, APSenderSessionConnectionType, APSenderSessionConnectionType, APSenderSessionConnectionType *, Boolean)"
- "Cannot register path"
- "CarPlayActiveEndpoint.txt"
- "Failed to create deep copy"
- "Failed to de-serialize"
- "Failed to serialize"
- "Item is NULL"
- "Local endpoint [%!{(MISSING)ptr}] cluster ID changed: %!@(MISSING) -> %!@(MISSING). Simulate system request to stop.\n"
- "NAPS"
- "No"
- "No data in response"
- "No incoming message"
- "No matched request found"
- "Object invalidated"
- "Scr"
- "SelectionState"
- "Storing CarPlay endpoint activation state (active: %!d(MISSING), PID: %!d(MISSING))\n"
- "VideoPlaying"
- "[%!{(MISSING)ptr}] APSLocalAudioCapabilityMonitor created"
- "alloc failed"
- "can't find valid video track"
- "err"
- "kCMBaseObjectError_Invalidated"
- "kCMBaseObjectError_ParamErr"
- "kFigBaseObjectError_AllocationFailed"
- "kFigBaseObjectError_ValueNotAvailable"
- "kFigEndpointError_AllocationFailed"
- "kFigEndpointPlaybackSessionError_AllocationFailed"
- "kFigEndpointPlaybackSessionError_InvalidParameter"
- "messageID is missing in response event"
- "type is missing in response event"
- "void apsession_determineTransportAvailabilityAndPreferredConnectionType(APSenderSessionRef, APSenderSessionConnectionType *, APSenderSessionConnectionType *, Boolean *)"
- "void carManager_storeEndpointActivationStateForCurrentProcess(FigEndpointManagerRef, Boolean)"
- "void endpointaggregate_handleSubEndpointUpdateFeaturesCompleted(FigEndpointRef, FigEndpointFeatures, uint64_t, OSStatus, void *)"
- "void manager_deactivateLocalCluster(FigEndpointManagerRef, FigEndpointRef)"
- "w"

```
