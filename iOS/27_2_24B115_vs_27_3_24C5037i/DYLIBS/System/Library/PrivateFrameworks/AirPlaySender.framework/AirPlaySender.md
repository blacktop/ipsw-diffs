## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-1005.13.1.1.0
-  __TEXT.__text: 0x23b9d0
+1015.5.1.0.0
+  __TEXT.__text: 0x246108
   __TEXT.__objc_methlist: 0x81c
-  __TEXT.__cstring: 0x901f4
-  __TEXT.__const: 0x6190
+  __TEXT.__cstring: 0x923b2
+  __TEXT.__const: 0x62c0
   __TEXT.__gcc_except_tab: 0xaf4
   __TEXT.__dlopen_cstrs: 0x61a
   __TEXT.__oslogstring: 0x1009
-  __TEXT.__unwind_info: 0x92d8
+  __TEXT.__unwind_info: 0x9618
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x77f8
+  __DATA_CONST.__const: 0x7988
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb78
+  __DATA_CONST.__objc_selrefs: 0xb98
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0x23d8
-  __AUTH_CONST.__const: 0x77d0
-  __AUTH_CONST.__cfstring: 0x14ac0
+  __DATA_CONST.__got: 0x2420
+  __AUTH_CONST.__const: 0x7a40
+  __AUTH_CONST.__cfstring: 0x14c60
   __AUTH_CONST.__objc_const: 0xed0
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_intobj: 0x150

   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x878
   __DATA.__objc_ivar: 0x88
-  __DATA.__data: 0x18620
+  __DATA.__data: 0x187e0
   __DATA.__common: 0xa04
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xfe8
-  __DATA_DIRTY.__bss: 0x788
+  __DATA_DIRTY.__bss: 0x7a0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11500
-  Symbols:   8723
-  CStrings:  11690
+  Functions: 11749
+  Symbols:   8839
+  CStrings:  11849
 
Symbols:
+ GCC_except_table77
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table80
+ GCC_except_table81
+ GCC_except_table82
+ GCC_except_table83
+ GCC_except_table95
+ GCC_except_table96
+ _APAudioFormatCopyPreferredBidirectionalAudioFormats
+ _APAudioFormatGetSupportedTransportAudioFormatsBidirectionalAudioSender
+ _APEndpointAddNowPlayingAppMetrics
+ _APEndpointFlushAndAddNowPlayingAppMetrics
+ _APEndpointShouldTrackNowPlayingApps
+ _APMetadataSourceBeginRecordingNowPlayingAppDurations
+ _APMetadataSourceFlushAndCopyNowPlayingAppDurations
+ _APMetadataSourceResetNowPlayingAppDurations
+ _APSAPAPExtensionConvertLoudnessInfoDictContentTypeToBBuf
+ _APSAPAPExtensionConvertLoudnessInfoDictLibraryLoudnessToBBuf
+ _APSIsBidirectionalAudioSenderEnabled
+ _APSRTPPacketHandlerGetRTPPayloadTypeForTransportMessageType
+ _APSRTPPacketHandlerGetTransportMessageTypeForRTPPayloadType
+ _BDAEndpointCreateWithEndpointDescription
+ _BDAEndpointDescriptionCreateWithTransportDevice
+ _BDAEndpointManagerCreate
+ _BDAEndpointManagerCreateEx
+ _BDAEndpointManagerGetShared
+ _BDAEndpointManagerGetShared.once
+ _BDAEndpointManagerGetShared.sBDAEndpointManager
+ _BDAGetEndpointManager
+ _BDAGetEndpointManager.sCreateOnce
+ _FigEndpointAudioSinkResume
+ _FigEndpointGetClassID
+ _FigEndpointManagerRemoteCopyBidirectionalAudioManager
+ __DefaultRuneLocale
+ ___APMetadataSourceBeginRecordingNowPlayingAppDurations_block_invoke
+ ___APMetadataSourceFlushAndCopyNowPlayingAppDurations_block_invoke
+ ___APMetadataSourceResetNowPlayingAppDurations_block_invoke
+ ___BDAEndpointManagerGetShared_block_invoke
+ ___BDAGetEndpointManager_block_invoke
+ ___audioStream_dissociateInternal_block_invoke
+ ___audioStream_handleIncomingInputDataMessage_block_invoke
+ ___audioStream_suspendInternal_block_invoke_2
+ ___bdaManager_Invalidate_block_invoke
+ ___bdaManager_createTransportDeviceFromInfo_block_invoke
+ ___maskrune
+ _apsession_getUsageDescription
+ _audioStream_getAPStreamType
+ _audioStream_handleIncomingInputDataMessage
+ _bdaDescription_CopyDebugDescription
+ _bdaDescription_CopyFeatures
+ _bdaDescription_CopyProperty
+ _bdaDescription_DescribesSameTransportDevice
+ _bdaDescription_Finalize
+ _bdaDescription_HasFeature
+ _bdaDescription_SetProperty
+ _bdaDescription_copyAudioFormats
+ _bdaDescription_copyDeviceID
+ _bdaDescription_copyMACAddress
+ _bdaDescription_copyName
+ _bdaDescription_copySourceVersion
+ _bdaEndpoint_Activate
+ _bdaEndpoint_CopyDebugDescription
+ _bdaEndpoint_CopyProperty
+ _bdaEndpoint_Deactivate
+ _bdaEndpoint_Dissociate
+ _bdaEndpoint_Finalize
+ _bdaEndpoint_SetDelegate
+ _bdaEndpoint_SetDelegateRouting
+ _bdaEndpoint_SetProperty
+ _bdaEndpoint_activateInternal
+ _bdaEndpoint_callDelegateHandleFailed
+ _bdaEndpoint_clearEndpointState
+ _bdaEndpoint_copyShowInfoDictionary
+ _bdaEndpoint_copyStreams
+ _bdaEndpoint_createAudioHALDevices
+ _bdaEndpoint_deactivateInternal
+ _bdaEndpoint_deferredHandleSenderSessionFailed
+ _bdaEndpoint_dissociateInternal
+ _bdaEndpoint_dissociateStreamsAndStopSenderSession
+ _bdaEndpoint_handleSenderSessionFailed
+ _bdaEndpoint_handleStreamFailed
+ _bdaEndpoint_isConnected
+ _bdaEndpoint_resetActivationState
+ _bdaEndpoint_stopListeningToSenderSessionAndStreamsNotifications
+ _bdaEndpoint_updateStatus
+ _bdaManager_CopyDebugDescription
+ _bdaManager_CopyProperty
+ _bdaManager_Finalize
+ _bdaManager_Invalidate
+ _bdaManager_create
+ _bdaManager_createEndpoint
+ _bdaManager_destroyEndpoint
+ _bdaManager_notifyAvailableEndpointsChanged
+ _bdaManager_removeEndpointForID
+ _gLogCategory_BDAEndpoint
+ _gLogCategory_BDAEndpointDescription
+ _gLogCategory_BDAEndpointManager
+ _gLogCategory_BDAEndpointManagerFactory
+ _kAPEndpointDescriptionProperty_SupportsReceiverSideCALMLoudness
+ _kAPEndpointNowPlayingAppHistogramBounds
+ _kAPEndpointSharedContextParsingAudioEngineOption_IsBidirectionalAudio
+ _kAPHALAudioDeviceCreationOptionDeviceType_BidirectionalAudio
+ _kBDAEndpointCreationOption_EventRecorder
+ _kBDAEndpointCreationOption_SenderSessionFactory
+ _kBDAEndpointDescriptionVTable
+ _kBDAEndpointDescription_BaseClassWrapper
+ _kBDAEndpointDescription_Class
+ _kBDAEndpointManagerVTable
+ _kBDAEndpointManager_BaseClassWrapper
+ _kBDAEndpointManager_FigEndpointManagerClassWrapper
+ _kBDAEndpointVTable
+ _kBDAEndpoint_BaseClassWrapper
+ _kBDAEndpoint_FigEndpointClassWrapper
+ _kFigEndpointInfoKey_DeviceName
+ _kFigEndpointInfoKey_NetworkAddress
+ _kFigEndpointInfoKey_NetworkPort
+ _kFigEndpointInfoKey_TXTRecord
+ _kFigEndpointManagerType_BidirectionalAudio
+ _kFigEndpointProperty_SnoopCollectionPathPattern
+ _kFigEndpointStreamProperty_SupportsReceiverSideCALMLoudness
+ _kFigEndpointType_BidirectionalAudio
+ _metadataSource_closeNowPlayingAppEntry
+ _objc_release_x24
+ _stream_isBidirectionalAudio
- GCC_except_table67
- GCC_except_table68
- GCC_except_table69
- GCC_except_table70
- GCC_except_table71
- GCC_except_table72
- GCC_except_table73
- GCC_except_table88
- _apsession_requiresHKPairVerify
CStrings:
+ "### BDAEndpoint %{ptr}: endpoint must be deactivated/dissociated before deallocation!\n"
+ "1015.5.1"
+ "<BDAEndpoint %p>"
+ "<BDAEndpointDescription %p, name=%@, advertiserInfo=%@>"
+ "<BDAEndpointManager %p, endpoints=%ld>"
+ "APEndpointStreamAudio.%{ptr}.inputDataProcessing"
+ "APStreamType APSRTPPacketHandlerGetRTPPayloadTypeForTransportMessageType(OSType)"
+ "AirPlayCALMLoudness"
+ "BDA"
+ "BDAEndpoint"
+ "BDAEndpoint.%{ptr}.%s"
+ "BDAEndpointCreateWithEndpointDescription"
+ "BDAEndpointDescription"
+ "BDAEndpointDescription.%{ptr}.notification"
+ "BDAEndpointDescriptionCreateWithTransportDevice"
+ "BDAEndpointManager"
+ "BDAEndpointManagerCreate"
+ "BDAEndpointManagerFactory"
+ "BDAGetEndpointManager_block_invoke"
+ "BDAManager: Using advertising override to create endpoint; info: %@"
+ "BidirectionalAudio"
+ "BidirectionalAudio Endpoint Manager [%{ptr}], err %#m\n"
+ "BidirectionalAudio Endpoint Manager creation failed with %#m\n"
+ "Boolean bdaDescription_HasFeature(APEndpointDescriptionRef, CFIndex)"
+ "Creating BidirectionalAudio Endpoint Manager\n"
+ "Creating BidirectionalAudio Endpoint Manager Local\n"
+ "HomeAccessoryBidirectional"
+ "IsBidirectionalAudio"
+ "OSStatus APMetadataSourceCreateWithNowPlayingAppPID(CFAllocatorRef, pid_t, APMetadataSourceRequestOptions, APMetadataSourceRef *)"
+ "OSStatus BDAEndpointCreateWithEndpointDescription(CFAllocatorRef, APEndpointDescriptionRef, CFDictionaryRef, FigEndpointRef *)"
+ "OSStatus BDAEndpointDescriptionCreateWithTransportDevice(CFAllocatorRef, APTransportDeviceRef, APEndpointDescriptionRef *)"
+ "OSStatus BDAGetEndpointManager(FigEndpointManagerRef *)"
+ "OSStatus BDAGetEndpointManager(FigEndpointManagerRef *)_block_invoke"
+ "OSStatus audioStream_createTransportAudioDataStream(APSenderSessionRef, APSNetworkClockRef, APTransportStreamSendBackingProviderRef, CFStringRef, CFStringRef, APTransportStreamRef *)"
+ "OSStatus audioStream_createTransportAudioInputStream(FigEndpointStreamRef, int *)"
+ "OSStatus audioStream_setupAudioStream(FigEndpointStreamRef, int, CFDictionaryRef, int, APSAudioFormatDescriptionRef, Boolean, CFDataRef, uint64_t, uint64_t *, int *, int *, CFDictionaryRef *, int *, uint32_t *, APSCryptorRef *, APSCryptorRef *)"
+ "OSStatus bdaDescription_CopyFeatures(APEndpointDescriptionRef, APSFeaturesRef *)"
+ "OSStatus bdaDescription_CopyProperty(CMBaseObjectRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus bdaDescription_SetProperty(CMBaseObjectRef, CFStringRef, CFTypeRef)"
+ "OSStatus bdaDescription_copyPropertyInternal(APEndpointDescriptionRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus bdaEndpoint_Activate(FigEndpointRef, FigEndpointFeatures, CFDictionaryRef, FigEndpointActivationCompletionCallback, void *)"
+ "OSStatus bdaEndpoint_CopyProperty(CMBaseObjectRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus bdaEndpoint_Deactivate(FigEndpointRef, CFDictionaryRef, FigEndpointActivationCompletionCallback, void *)"
+ "OSStatus bdaEndpoint_Dissociate(FigEndpointRef)"
+ "OSStatus bdaEndpoint_SetDelegateRouting(FigEndpointRef, const FigEndpointDelegateRouting *)"
+ "OSStatus bdaEndpoint_SetProperty(CMBaseObjectRef, CFStringRef, CFTypeRef)"
+ "OSStatus bdaEndpoint_createSenderSession(FigEndpointRef, APSNetworkClockRef, CFDictionaryRef, APSenderSessionRef *)"
+ "OSStatus bdaEndpoint_initStateFromEndpointDescription(FigEndpointRef)"
+ "OSStatus bdaEndpoint_setupAudioStream(FigEndpointRef, Boolean, FigEndpointStreamRef, Boolean, APAudioEngineVendorRef, CFDictionaryRef, CFStringRef)"
+ "OSStatus bdaEndpoint_setupStreams(FigEndpointRef, FigEndpointFeatures, CFDictionaryRef)"
+ "OSStatus bdaManager_CopyProperty(CMBaseObjectRef, CFStringRef, CFAllocatorRef, void *)"
+ "OSStatus bdaManager_Invalidate(CMBaseObjectRef)"
+ "OSStatus bdaManager_create(CFDictionaryRef, FigEndpointManagerRef *)"
+ "OSStatus bdaManager_createEndpoint(FigEndpointManagerRef, CFDictionaryRef, FigEndpointRef *)"
+ "OSStatus bdaManager_createTransportDeviceFromInfo(CFDictionaryRef, APTransportDeviceRef *)"
+ "OSStatus bdaManager_destroyEndpoint(FigEndpointManagerRef, FigEndpointRef)"
+ "OSType APSRTPPacketHandlerGetTransportMessageTypeForRTPPayloadType(OSType)"
+ "Remote Copy BidirectionalAudio Endpoint Manager\n"
+ "SupportsReceiverSideCALMLoudness"
+ "Unknown message type %c%c%c%c\n"
+ "[%{ptr}] %###s: %@"
+ "[%{ptr}] <BidirectionalAudioActivation> Activating endpoint %@ with seed %llu...\n"
+ "[%{ptr}] <BidirectionalAudioActivation> Activating endpoint '%@' with features %#ll{flags} and options %@\n"
+ "[%{ptr}] <BidirectionalAudioActivation> Deactivating endpoint %'@ with reason %'@...\n"
+ "[%{ptr}] <BidirectionalAudioActivation> Endpoint activated for features %#ll{flags}\n"
+ "[%{ptr}] <BidirectionalAudioActivation> Endpoint activation (seed %llu) failed with error %#m.\n"
+ "[%{ptr}] <BidirectionalAudioActivation> Request to deactivate endpoint...\n"
+ "[%{ptr}] <BidirectionalAudioDiscovery> %###s calling APTransportDeviceReconfirm\n"
+ "[%{ptr}] <BidirectionalAudioDiscovery> %###s inStatus = %#m; transportDevice = [%{ptr}]\n"
+ "[%{ptr}] AudioSink set to [%{ptr}]\n"
+ "[%{ptr}] BDAEndpoint invalidated APSenderSessionAirPlay [%{ptr}]\n"
+ "[%{ptr}] BDAEndpoint: Created APSenderSessionAirPlay [%{ptr}]\n"
+ "[%{ptr}] BDAEndpointDescription finalizing.\n"
+ "[%{ptr}] Bidirectional-audio endpoint [%{ptr}] is not tracked for [%@]"
+ "[%{ptr}] Bidirectional-audio endpoint already exists for [%@]"
+ "[%{ptr}] Bidirectional-audio stream requires CoreUtils pairing for encryption\n"
+ "[%{ptr}] Create: initial SupportsReceiverSideCALMLoudness=%d"
+ "[%{ptr}] Created BDAEndpoint with name %@\n"
+ "[%{ptr}] Created BDAEndpointManager"
+ "[%{ptr}] Created bidirectional-audio endpoint [%{ptr}] for [%@]"
+ "[%{ptr}] Created transport audio data input stream [%{ptr}]\n"
+ "[%{ptr}] Destroying bidirectional-audio endpoint [%{ptr}] for [%@]"
+ "[%{ptr}] Finalizing BDAEndpointManager"
+ "[%{ptr}] Ignoring AvoidAuthentication for bidirectional audio\n"
+ "[%{ptr}] Invalidating BDAEndpointManager"
+ "[%{ptr}] NowPlaying app duration recording started, seed %@\n"
+ "[%{ptr}] NowPlaying app entry closed after %.3f s: %@\n"
+ "[%{ptr}] Receiver-side CALM loudness %s supported across all substreams."
+ "[%{ptr}] Set up %@ stream (subType=%@)"
+ "[%{ptr}] Set up %@/%@ stream [%{ptr}]\n"
+ "[%{ptr}] Setting up streams ...\n"
+ "[%{ptr}] Setting up streams ...[done], err %#m\n"
+ "[%{ptr}] input data stream local port = %d\n"
+ "[%{ptr}] input message type '%C'\n"
+ "[%{ptr}] substream( %{ptr} support=%d )  SupportsReceiverSideCALMLoudness=%d"
+ "[%{ptr}] suspendDissociateAndReleaseStreams: audioStream=[%{ptr}], senderSession=[%{ptr}], teardown=[%{ptr}]\n"
+ "[%{ptr}][%@] Creating HAL device for Bidirectional audio\n"
+ "audioStream_createTransportAudioInputStream"
+ "audioStream_handleIncomingInputDataMessage"
+ "audioStream_processOneInputDataMessage"
+ "bdaDescription_CopyFeatures"
+ "bdaDescription_CopyProperty"
+ "bdaDescription_SetProperty"
+ "bdaDescription_copyAudioFormats"
+ "bdaDescription_copyDeviceID"
+ "bdaDescription_copyMACAddress"
+ "bdaDescription_copyName"
+ "bdaDescription_copySourceVersion"
+ "bdaDescription_hasFeatureInternal"
+ "bdaEndpoint_Activate"
+ "bdaEndpoint_CopyProperty"
+ "bdaEndpoint_Deactivate"
+ "bdaEndpoint_SetDelegate"
+ "bdaEndpoint_SetDelegateRouting"
+ "bdaEndpoint_SetProperty"
+ "bdaEndpoint_activateInternal"
+ "bdaEndpoint_addEndpointStreamNotificationListeners"
+ "bdaEndpoint_addSenderSessionNotificationListeners"
+ "bdaEndpoint_copyPropertyInternal"
+ "bdaEndpoint_copyShowInfoDictionary"
+ "bdaEndpoint_copyShowInfoForStreamsSetEntry"
+ "bdaEndpoint_copyStreams"
+ "bdaEndpoint_copyTeardownOptions"
+ "bdaEndpoint_createAudioHALDevice"
+ "bdaEndpoint_createAudioOptions"
+ "bdaEndpoint_createAudioStreamOptions"
+ "bdaEndpoint_createSenderSession"
+ "bdaEndpoint_deactivateInternal"
+ "bdaEndpoint_initStateFromEndpointDescription"
+ "bdaEndpoint_reportActivationMetrics"
+ "bdaEndpoint_setPropertyInternal"
+ "bdaEndpoint_setupAudioStream"
+ "bdaEndpoint_setupEventRecorder"
+ "bdaEndpoint_setupStreams"
+ "bdaEndpoint_updateStatus"
+ "bdaManager_CopyProperty"
+ "bdaManager_create"
+ "bdaManager_createEndpoint"
+ "bdaManager_createTransportDeviceFromInfo"
+ "bdaManager_destroyEndpoint"
+ "bidirectionalAudioStream"
+ "com.apple.airplay.bidirectionalAudioEndpointManager.notification"
+ "endpointAggregate_createAndStartMetadataSource"
+ "isBidirectionalAudio"
+ "isBidirectionalAudioSession"
+ "nowPlayingAppDurationHist"
+ "nowPlayingAppSwitchCount"
+ "void APMetadataSourceBeginRecordingNowPlayingAppDurations(APMetadataSourceRef, uint64_t)_block_invoke"
+ "void audioStream_handleIncomingInputDataMessage(APTransportStreamRef, OSType, CMBlockBufferRef, void *)"
+ "void bdaDescription_Finalize(CMBaseObjectRef)"
+ "void bdaDescription_setPropertyInternal(APEndpointDescriptionRef, CFStringRef, CFTypeRef)"
+ "void bdaEndpoint_Finalize(CMBaseObjectRef)"
+ "void bdaEndpoint_activateInternal(void *)"
+ "void bdaEndpoint_clearEndpointState(FigEndpointRef)"
+ "void bdaEndpoint_createAudioHALDevice(FigEndpointRef, CFStringRef)"
+ "void bdaEndpoint_createAudioHALDevices(void *)"
+ "void bdaEndpoint_deactivateInternal(void *)"
+ "void bdaEndpoint_dissociateInternal(void *)"
+ "void bdaEndpoint_dissociateStreamsAndStopSenderSession(void *)"
+ "void bdaEndpoint_handleSenderSessionFailed(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void bdaEndpoint_handleStreamFailed(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void bdaEndpoint_updateStatus(FigEndpointRef, OSStatus, BDAEndpointSessionState)"
+ "void bdaManager_Finalize(CMBaseObjectRef)"
+ "void bdaManager_notifyAvailableEndpointsChanged(FigEndpointManagerRef)"
+ "void metadataSource_closeNowPlayingAppEntry(APMetadataSourceRef, uint64_t)"
- "1005.13.1.1"
- "EB60D13B-DFB8-4C16-AE98-D24F06B33E29"
- "OSStatus APMetadataSourceCreateWithNowPlayingAppPID(CFAllocatorRef, pid_t, APMetadataSourceRef *)"
- "OSStatus audioStream_createTransportAudioDataStream(APSenderSessionRef, APSNetworkClockRef, APTransportStreamSendBackingProviderRef, CFStringRef, APTransportStreamRef *)"
- "OSStatus audioStream_setupAudioStream(FigEndpointStreamRef, int, CFDictionaryRef, APSAudioFormatDescriptionRef, Boolean, CFDataRef, uint64_t, uint64_t *, int *, int *, CFDictionaryRef *, int *, uint32_t *, APSCryptorRef *)"
- "SnoopCollectionPath"
```
