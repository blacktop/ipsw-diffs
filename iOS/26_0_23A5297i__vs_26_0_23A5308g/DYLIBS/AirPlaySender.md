## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-890.73.1.11.1
-  __TEXT.__text: 0x212fc4
-  __TEXT.__auth_stubs: 0x5580
+890.77.2.0.0
+  __TEXT.__text: 0x211048
+  __TEXT.__auth_stubs: 0x55d0
   __TEXT.__objc_methlist: 0x7c4
-  __TEXT.__cstring: 0x8242f
+  __TEXT.__cstring: 0x8263f
   __TEXT.__const: 0x10070
   __TEXT.__gcc_except_tab: 0x96c
   __TEXT.__dlopen_cstrs: 0x61d
-  __TEXT.__oslogstring: 0x794
-  __TEXT.__unwind_info: 0x51d8
+  __TEXT.__oslogstring: 0x7c5
+  __TEXT.__unwind_info: 0x51f8
   __TEXT.__objc_classname: 0x1c5
   __TEXT.__objc_methname: 0x2116
   __TEXT.__objc_methtype: 0xd78

   __DATA_CONST.__objc_selrefs: 0x9b0
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x2ad0
-  __AUTH_CONST.__const: 0x7ea0
+  __AUTH_CONST.__auth_got: 0x2af8
+  __AUTH_CONST.__const: 0x7f00
   __AUTH_CONST.__cfstring: 0x12660
   __AUTH_CONST.__objc_const: 0xec0
   __AUTH_CONST.__objc_dictobj: 0xa0

   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x7b0
   __DATA.__objc_ivar: 0x88
-  __DATA.__data: 0x18648
-  __DATA.__bss: 0xa70
+  __DATA.__data: 0x186b8
+  __DATA.__bss: 0xa80
   __DATA.__common: 0xa10
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xcc8
-  __DATA_DIRTY.__bss: 0x300
+  __DATA_DIRTY.__bss: 0x2f0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7322F3B2-E83E-39E2-9360-5EED061C5E51
-  Functions: 9739
-  Symbols:   24511
-  CStrings:  13440
+  UUID: F03CA2D5-B16A-3BCF-98B8-5475AA4479A9
+  Functions: 9767
+  Symbols:   24578
+  CStrings:  13435
 
Symbols:
+ _APAudioEngineCarPlayCreate.cold.4
+ _APAudioEngineRealTimeCreate.cold.39
+ _APAudioEngineVendorCreate.cold.1
+ _APAudioEngineVendorCreate.cold.2
+ _APAudioEngineVendorCreate.cold.3
+ _APAudioEngineVendorCreate.cold.4
+ _APCUGetFairPlayHWInfoEx
+ _APEndpointManagerGetShared.once
+ _APEndpointManagerGetShared.sAPEndpointManager
+ _APEndpointUGLWrapper_CopyProperty.cold.1
+ _APEndpointUGLWrapper_CopyProperty.cold.2
+ _APSCopyDeviceName
+ _APSCopyPersistentGroupInfo
+ _APSIsLocalClusterWithStaticLeadershipEnabled
+ _APSIsLowLatencyAudioSendingEnabled
+ _CFObjectSetPropertyInt64
+ _FigEndpointSubTypeToGestaltDeviceClass
+ _FigSignalErrorAtGM
+ _OUTLINED_FUNCTION_144
+ __MergedGlobals.896
+ ___block_descriptor_tmp.27
+ ___block_descriptor_tmp.31
+ ___block_descriptor_tmp.69
+ ___block_descriptor_tmp.805
+ ___block_descriptor_tmp.808
+ ___block_descriptor_tmp.811
+ ___block_descriptor_tmp.821
+ ___block_descriptor_tmp.840
+ ___block_literal_global.173
+ ___block_literal_global.179
+ ___block_literal_global.183
+ ___block_literal_global.599
+ ___block_literal_global.89
+ ___block_literal_global.96
+ _audioEngineCarPlay_Finalize.cold.1
+ _endpointCluster_getSubEndpointDeviceClass
+ _endpointCluster_getSubEndpointDeviceClass.cold.1
+ _endpointCluster_isSubEndpointStaticLeader
+ _endpointUGLWrapper_activateInternal.cold.10
+ _endpointUGLWrapper_activateInternal.cold.11
+ _endpointUGLWrapper_activateInternal.cold.4
+ _endpointUGLWrapper_activateInternal.cold.5
+ _endpointUGLWrapper_activateInternal.cold.6
+ _endpointUGLWrapper_activateInternal.cold.7
+ _endpointUGLWrapper_activateInternal.cold.8
+ _endpointUGLWrapper_activateInternal.cold.9
+ _endpointUGLWrapper_copyWrappedEndpoint
+ _endpointUGLWrapper_createMXDescriptor.cold.2
+ _endpointUGLWrapper_updateMXDescriptor.cold.2
+ _endpoint_isInLocalClusterOfStaticLeader
+ _gAPAudioEngineVendorInitOnce
+ _gAPAudioEngineVendorTypeID
+ _gLogCategory_APAudioEngineVendor
+ _manager_create.cold.47
+ _manager_handlePreferencesChanged.cold.10
+ _manager_handlePreferencesChanged.cold.11
+ _manager_handlePreferencesChanged.cold.12
+ _manager_handlePreferencesChanged.cold.13
+ _manager_handlePreferencesChanged.cold.14
+ _manager_handlePreferencesChanged.cold.15
+ _manager_handlePreferencesChanged.cold.16
+ _manager_handlePreferencesChanged.cold.17
+ _manager_handlePreferencesChanged.cold.18
+ _manager_handlePreferencesChanged.cold.4
+ _manager_handlePreferencesChanged.cold.5
+ _manager_handlePreferencesChanged.cold.6
+ _manager_handlePreferencesChanged.cold.7
+ _manager_handlePreferencesChanged.cold.8
+ _manager_handlePreferencesChanged.cold.9
+ _manager_handleUpdateLocalInfoDictCommand.cold.1
+ _manager_updateLocalInfoDict
+ _multicastProbeSender_constructMulticastGroupInfoForAddressFamily.cold.16
+ _multicastProbeSender_decrementRefCountForSSMGroupInfo.cold.4
+ _multicastProbeSender_incrementRefCountForSSMGroupInfo.cold.2
+ _multicastProbeSender_registerDeviceForAddressFamily.cold.25
+ _uglWrapper_deactivationCompletionCallback.cold.3
+ _uglWrapper_updateAirPlayEndpointProperties
+ _uglWrapper_updateAirPlayEndpointProperties.cold.1
- _APEndpointClusterCreate.cold.15
- _FigSignalErrorAt3
- _GetFairPlayHWInfo
- __MergedGlobals.895
- ___block_descriptor_tmp.124
- ___block_descriptor_tmp.29
- ___block_descriptor_tmp.58
- ___block_descriptor_tmp.62
- ___block_descriptor_tmp.804
- ___block_descriptor_tmp.807
- ___block_descriptor_tmp.810
- ___block_descriptor_tmp.820
- ___block_descriptor_tmp.839
- ___block_descriptor_tmp.93
- ___block_literal_global.178
- ___block_literal_global.182
- ___block_literal_global.588
- ___block_literal_global.95
- _bufferedAudioEngine_flushWithinSampleRangeInternal.cold.14
- _endpointUGLWrapper_copyWrappedEndpointCreatingIfNeeded
- _endpointUGLWrapper_copyWrappedEndpointCreatingIfNeeded.cold.1
- _endpointUGLWrapper_copyWrappedEndpointCreatingIfNeeded.cold.2
- _endpointUGLWrapper_copyWrappedEndpointCreatingIfNeeded.cold.3
- _endpointUGLWrapper_copyWrappedEndpointCreatingIfNeeded.cold.4
- _endpointUGLWrapper_copyWrappedEndpointCreatingIfNeeded.cold.5
- _endpointUGLWrapper_copyWrappedEndpointCreatingIfNeeded.cold.6
- _endpointUGLWrapper_copyWrappedEndpointCreatingIfNeeded.cold.7
- _endpointUGLWrapper_copyWrappedEndpointCreatingIfNeeded.cold.8
- _endpointUGLWrapper_getActivationSeed
- _multicastProbeSender_Finalize.cold.1
- _multicastProbeSender_Finalize.cold.2
- _multicastProbeSender_Finalize.cold.3
CStrings:
+ "%@ Allocated\n"
+ "%@ Created\n"
+ "%s signalled err=%d at <>:%d"
+ "%{ptr} Dissociating"
+ "890.77.2"
+ "APAudioEngineVendorCreate"
+ "APEndpointStreamInterruptibleWrapper created: %{ptr}; subStream: %{ptr}; routingContextUUID: [%@]\n"
+ "APEndpointStreamInterruptingWrapper created: %{ptr}; subStream: %{ptr}; interruptibleStream: %{ptr}; routingContextUUID: [%@]\n"
+ "APEndpointUGLWrapper_CopyProperty"
+ "AP_SIGNPOST_CAR_ACTIVATED_ENDPOINTS_CHANGED_SEND"
+ "BAE [%{ptr}] %sReceived truncated sample (duration:%1.3f), adjust nextRemoteMediaTimestamp to duration of the sample: %1.3f\n"
+ "BAE [%{ptr}] %s[0x%04X] Skip flushing hose [%{ptr}] (%@), seq Num range empty\n"
+ "GestaltDeviceClass endpointCluster_getSubEndpointDeviceClass(FigEndpointRef, FigEndpointRef)"
+ "IsRepresentingUGLSender"
+ "Local HT cluster action [%{ptr}]: activate b/c not in use\n"
+ "Local HT cluster action [%{ptr}]: none b/c not in use\n"
+ "Local SP cluster action [%{ptr}]: activate b/c cluster leader & not in use\n"
+ "Local SP cluster action [%{ptr}]: deactivate b/c not cluster leader & in use\n"
+ "Local SP cluster action [%{ptr}]: none b/c cluster leader (%s) == not in use (%s)\n"
+ "Mac"
+ "OSStatus APAudioEngineVendorCreate(APSNetworkClockRef, CFDictionaryRef, APAudioEngineCreationFunc, APAudioEngineVendorRef *)"
+ "OSStatus audioEngineCarPlay_SetProperty(CMBaseObjectRef, CFStringRef, CFTypeRef)"
+ "OSStatus manager_setLocalEndpointInfoFromPrefs(FigEndpointManagerRef)"
+ "OSStatus multicastProbeSender_Invalidate(CMBaseObjectRef)"
+ "Updated local info with properties: deviceName=%@ pgUUID=%@ pgType=%d pgSize=%d pgMemberID=%@ pgModel=%@ pgName=%@\n"
+ "[%{ptr}] <APUGLActivation> ActivateForFeaturesWithCompletionCallback(0x%llx) already %s; returning Error_AlreadyActivated"
+ "[%{ptr}] <APUGLActivation> ActivateForFeaturesWithCompletionCallback(0x%llx, seed %lld)"
+ "[%{ptr}] <APUGLActivation> Activating wrapped endpoint [%{ptr}], seed %lld"
+ "[%{ptr}] <APUGLActivation> Calling activation callback with error %#m"
+ "[%{ptr}] Created internal engine [%{ptr}]"
+ "[%{ptr}] Finalized\n"
+ "[%{ptr}] ForceZeroBasedSampleTimes changed to %s\n"
+ "[%{ptr}] Invalidated\n"
+ "[%{ptr}] Using internal local endpoint strategy for local playback\n"
+ "[%{ptr}] Want subEndpoint activation [%{ptr}]: %s - local HT subEndpoints activated only from static cluster leader\n"
+ "[%{ptr}] Warning! Wrapped endpoint [%{ptr}] doesn't match internal [%{ptr}]"
+ "activating"
+ "endpointCluster_getSubEndpointDeviceClass"
+ "manager_setLocalEndpointInfoFromPrefs"
+ "multicastToUnicastIPv6ReceivedPacketCount"
+ "multicastToUnicastIPv6Status"
+ "multicastToUnicastIPv6TimeToDetectMs"
+ "multicastToUnicastIPv6TransmittedPacketCount"
+ "uglWrapper_updateAirPlayEndpointProperties"
+ "void audioEngineCarPlay_Finalize(CMBaseObjectRef)"
+ "void endpointUGLWrapper_activateInternal(EndpointActivationCallbackContext *)"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "%{ptr} Dissociate called"
- "890.73.1.11.1"
- "APAudioEngineBufferedAdapter.c"
- "APEndpoint.m"
- "APEndpointPlaybackSessionRemoteControl.m"
- "APEndpointStreamAggregateAudio.c"
- "APEndpointStreamInterruptibleWrapper created: %{ptr}; subStream: %{ptr}; routingContextUUID: %@\n"
- "APEndpointStreamInterruptingWrapper created: %{ptr}; subStream: %{ptr}; interruptibleStream: %{ptr} routingContextUUID [%@]\n"
- "APVirtualDisplayTestSink.c"
- "Action not supported"
- "Allocation error"
- "BAE [%{ptr}] %s[0x%04X] Seq Num range empty, skip sending flush within sample range command over the wire\n"
- "Cannot register path"
- "Failed allocating audio buffer"
- "Failed to create deep copy"
- "Failed to de-serialize"
- "Failed to serialize"
- "Item is NULL"
- "Local cluster action [%{ptr}]: activate b/c HT ATV not in use\n"
- "Local cluster action [%{ptr}]: activate b/c cluster leader & not in use\n"
- "Local cluster action [%{ptr}]: deactivate b/c not cluster leader & in use\n"
- "Local cluster action [%{ptr}]: none b/c HT ATV not in use\n"
- "Local cluster action [%{ptr}]: none b/c cluster leader (%s) == not in use (%s)\n"
- "MetadataSourceTestingOnly"
- "No data in response"
- "No incoming message"
- "No matched request found"
- "OSStatus endpointUGLWrapper_activateInternal(EndpointActivationCallbackContext *)"
- "Object invalidated"
- "[%{ptr}] <APUGLActivation> Activating wrapped endpoint [%{ptr}]"
- "[%{ptr}] ActivateForFeaturesWithCompletionCallback(0x%llx)"
- "[%{ptr}] Created (ForceZeroBasedSampleTime: %s)\n"
- "[%{ptr}] Want subEndpoint activation [%{ptr}]: %s - local HT subEndpoints activated only from ATV\n"
- "alloc failed"
- "can't find valid video track"
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
- "multicastToUnicastReceivedPacketCountIPv6"
- "multicastToUnicastStatusIPv6"
- "multicastToUnicastTimeToDetectMsIPv6"
- "multicastToUnicastTransmittedPacketCountIPv6"
- "type is missing in response event"

```
