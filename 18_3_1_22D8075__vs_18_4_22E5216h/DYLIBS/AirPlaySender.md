## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-845.6.1.0.0
-  __TEXT.__text: 0x1c9b54
-  __TEXT.__auth_stubs: 0x5090
-  __TEXT.__objc_methlist: 0x340
-  __TEXT.__cstring: 0x7287d
-  __TEXT.__const: 0xfd70
-  __TEXT.__gcc_except_tab: 0x41c
-  __TEXT.__oslogstring: 0x69f
-  __TEXT.__unwind_info: 0x2af0
+850.17.1.0.0
+  __TEXT.__text: 0x1e0424
+  __TEXT.__auth_stubs: 0x50e0
+  __TEXT.__objc_methlist: 0x67c
+  __TEXT.__cstring: 0x74136
+  __TEXT.__const: 0xfd80
+  __TEXT.__gcc_except_tab: 0x940
+  __TEXT.__dlopen_cstrs: 0x61d
+  __TEXT.__oslogstring: 0x6da
+  __TEXT.__unwind_info: 0x49e0
   __TEXT.__eh_frame: 0xaa8
   __TEXT.__objc_classname: 0x174
-  __TEXT.__objc_methname: 0x19a5
+  __TEXT.__objc_methname: 0x1a01
   __TEXT.__objc_methtype: 0xa56
-  __TEXT.__objc_stubs: 0x1760
-  __DATA_CONST.__got: 0x1d38
-  __DATA_CONST.__const: 0x5fb8
+  __TEXT.__objc_stubs: 0x17c0
+  __DATA_CONST.__got: 0x1d68
+  __DATA_CONST.__const: 0x6390
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x680
+  __DATA_CONST.__objc_selrefs: 0x7c8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x2858
+  __AUTH_CONST.__auth_got: 0x2880
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x7a60
-  __AUTH_CONST.__cfstring: 0x10d00
-  __AUTH_CONST.__objc_const: 0x1178
+  __AUTH_CONST.__const: 0x77e0
+  __AUTH_CONST.__cfstring: 0x10e20
+  __AUTH_CONST.__objc_const: 0xb88
   __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0x738
+  __AUTH.__data: 0x580
   __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x183d8
-  __DATA.__bss: 0x9d0
+  __DATA.__data: 0x183c8
+  __DATA.__bss: 0x9c8
   __DATA.__common: 0xa08
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0xd30
-  __DATA_DIRTY.__bss: 0x2d0
+  __DATA_DIRTY.__data: 0xc50
+  __DATA_DIRTY.__bss: 0x2f0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/MediaControlSender.framework/MediaControlSender
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3359
-  Symbols:   6302
-  CStrings:  9769
+  Functions: 8759
+  Symbols:   12058
+  CStrings:  9901
 
Symbols:
+ _APEndpointStreamScreenOverrideCanvasSize
+ _APSThreadSafeDictionaryAddEntriesToDictionaryWithRecursion
+ _APSWiFiTransactionUpdateTransaction
+ _CFPropertyListAppendFormatted
+ _FigSignalErrorAt3
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSString
+ __sl_dlopen
+ _abort_report_np
+ _dlerror
+ _fig_log_get_emitter
+ _kAPEndpointCarPlayNotificationPayloadKey_DisconnectReason
+ _kFigEndpointNotification_BufferedAudioCapabilitiesChanged
+ _kFigEndpointNotification_VolumeCacheShouldBeCleared
+ _kFigEndpointProperty_BufferedAudioCapabilities
+ _kFigEndpointProperty_OverrideCanvasSize
+ _kFigVirtualDisplayOption_OverrideCanvasHeight
+ _kFigVirtualDisplayOption_OverrideCanvasWidth
- _APSWiFiTransactionCreate
- _FigSignalErrorAt
- _dlopen
- _kAPEndpointDescriptionProperty_WASCalibrationSupportsMATAtmos
- _kAPSEndpointStreamAudioHoseProtocolProperty_IsAppleTV
- _kAPSEndpointStreamAudioHoseProtocolProperty_WASCalibrationSupportsMATAtmos
CStrings:
+ "### [%{ptr}] Can't forward iAP Channel event, Endpoint not activated\n"
+ "%@ Received override canvas size command\n"
+ "%@ Setting %@: %d, %@: %d\n"
+ "%@ max times to reencode idle frame: %d\n"
+ "%kO=%i"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "(Fig)"
+ "850.17.1"
+ "APAccTransportClient.m"
+ "APCarPlayAudioFormats.m"
+ "APCarPlayCarServicesInterface.m"
+ "APCarPlayPolicyMonitor.m"
+ "APCarPlayPreferences.m"
+ "APCarPlaySiriInterface.m"
+ "APEndpoint.c"
+ "APEndpointManagerCarPlay.m"
+ "APEndpointPlaybackSessionRemoteControl.m"
+ "APEndpointStreamAggregateAudio.c"
+ "APEndpointStreamScreenUDP.m"
+ "APSenderMediaRemoteSoftLinking.h"
+ "APVirtualDisplayTestSink.c"
+ "AP_SIGNPOST_ALTERNATESCREEN_[%d]_DISPLAYING"
+ "AP_SIGNPOST_CAR_CONTROLSERVER_STARTEDSERVER"
+ "AP_SIGNPOST_DNS_RESOLVED"
+ "AP_SIGNPOST_MAINSCREEN_DISPLAYING"
+ "Action not supported"
+ "Allocation error"
+ "BAE [%{ptr}] %s[0x%04X] Discarding sbuf with opts %1.3f for current flush time range: start = %1.3f, end = %1.3f \n"
+ "Boolean soft_MRMediaRemoteSendCommand(MRMediaRemoteCommand, CFDictionaryRef)"
+ "CFDataRef soft_MRMediaRemoteCommandInfoCreateExternalRepresentation(CFAllocatorRef, MRMediaRemoteCommandInfoRef)"
+ "CFDataRef soft_MRNowPlayingClientCreateExternalRepresentation(MRNowPlayingClientRef)"
+ "CFDictionaryRef soft_acc_transportClient_copyPropertiesForEndpointWithUUID(CFStringRef)"
+ "CFStringRef getkCFACCProperties_Connection_MFi4Auth_AccessoryCertInfoToMatch(void)"
+ "CFStringRef getkMRMediaRemoteMediaTypeMusic(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoAlbum(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoArtist(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoArtworkData(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoArtworkMIMEType(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoComposer(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoDiscNumber(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoDuration(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoElapsedTime(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoGenre(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoIsAlwaysLive(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoIsExplicitTrack(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoIsMusicApp(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoMediaType(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoPlaybackRate(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoQueueIndex(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoRepeatMode(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoShuffleMode(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoTimestamp(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoTitle(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoTotalDiscCount(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoTotalQueueCount(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoTotalTrackCount(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoTrackNumber(void)"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoUniqueIdentifier(void)"
+ "CFStringRef soft_acc_transportClient_createConnection(ACCConnection_Type_t, CFStringRef)"
+ "CFStringRef soft_acc_transportClient_createEndpoint(CFStringRef, ACCEndpoint_TransportType_t, ACCEndpoint_Protocol_t, CFStringRef, ACCTransportClientDataOutHandlerCF, _Bool)"
+ "Cannot register path"
+ "CarPlay Endpoint reported disconnect reason: %d\n"
+ "Class getAVCDaemonProcessInfoClass(void)_block_invoke"
+ "Class getAVCMediaStreamNegotiatorClass(void)_block_invoke"
+ "Class getAVCScreenCaptureClass(void)_block_invoke"
+ "Class getAVCScreenCaptureConfigurationClass(void)_block_invoke"
+ "Class getAVCVideoStreamClass(void)_block_invoke"
+ "Class getCARConnectionEventClass(void)_block_invoke"
+ "Class getCARConnectionTimeStoreClass(void)_block_invoke"
+ "Class getCRCarPlayPreferencesClass(void)_block_invoke"
+ "Class getCRFeatureAvailabilityClass(void)_block_invoke"
+ "Class getCRSAppHistoryControllerClass(void)_block_invoke"
+ "Class getCRSSessionControllerClass(void)_block_invoke"
+ "Class getCRVehiclePolicyMonitorClass(void)_block_invoke"
+ "Class getCSCoreSpeechServicesClass(void)_block_invoke"
+ "Class getEAAccessoryManagerClass(void)_block_invoke"
+ "Class getMRClientClass(void)_block_invoke"
+ "Class getMRDestinationClass(void)_block_invoke"
+ "Class getMRNowPlayingControllerClass(void)_block_invoke"
+ "Class getMRNowPlayingControllerConfigurationClass(void)_block_invoke"
+ "Class getMRPlaybackQueueRequestClass(void)_block_invoke"
+ "Class getMRPlayerPathClass(void)_block_invoke"
+ "Class getVTPreferencesClass(void)_block_invoke"
+ "DeviceClass"
+ "DeviceMainScreenOrientation"
+ "E9459FD0-BCAD-4C45-820F-1E72447EF2F2"
+ "Endpoint %{ptr}: waiting for auth completion timeout after %u secs\n"
+ "Failed to create deep copy"
+ "Failed to de-serialize"
+ "Failed to serialize"
+ "Item is NULL"
+ "NSString *getAVCKeyDaemonProcessInfoUniquePID(void)"
+ "NSString *getAVCMediaStreamNegotiatorHDRMode(void)"
+ "NSString *getkAVCMediaStreamOptionClientPID(void)"
+ "NSString *getkAVCMediaStreamOptionRunInProcess(void)"
+ "No data in response"
+ "No incoming message"
+ "No matched request found"
+ "OSStatus APPairingClientCoreUtilsCreate(CFAllocatorRef, CFStringRef, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, CFStringRef, CFStringRef, CFDataRef, FigTransportStreamRef, APPairingClientRef *)"
+ "OSStatus audioStream_reportRTCMetrics(FigEndpointStreamRef, CFDictionaryRef)"
+ "OSStatus carEndpoint_copyStateProperty(FigEndpointRef, CFStringRef, CFAllocatorRef, void *)_block_invoke"
+ "OSStatus carEndpoint_createiAPChannelIfNeeded(FigEndpointRef)"
+ "OSStatus carEndpoint_forceKeyFrame(FigEndpointRef, CFDictionaryRef)"
+ "OSStatus carEndpoint_sendCommandOverRCSChannel(FigEndpointRef, FigEndpointRemoteControlSessionRef, CFStringRef, CFDataRef)"
+ "OSStatus endpoint_copyPropertyInternal(FigEndpointRef, CFStringRef, CFAllocatorRef, CFTypeRef *)"
+ "OSStatus screenstream_handleOverrideCanvasSize(FigEndpointStreamRef, CFDictionaryRef)"
+ "Object invalidated"
+ "OverrideCanvasSize"
+ "Previous session was disconnected by the user, not reporting 'session reset' event to Analytics"
+ "Unable to find class %s"
+ "[%{ptr}] %###s: failed to send %'@ command with error: %d\n"
+ "[%{ptr}] %'@ command is not supported for Accessories with sourceVersion: %u"
+ "[%{ptr}] APPairingClientCoreUtils created %c%c%c%c%c%c%c%c%c.\n"
+ "[%{ptr}] APSenderSessionBroadcastKeysForDiagnosticsData() failed: %m (encryptionContext = %@, remoteDataPort = %d)"
+ "[%{ptr}] APSenderSessionBroadcastKeysForDiagnosticsData() with RemotePort = %d, LocalSendsWithReadKey = %d"
+ "[%{ptr}] Buffered audio is not supported\n"
+ "[%{ptr}] Buffered audio stream doesn't exist during copy property\n"
+ "[%{ptr}] CarPlay SessionManagement: %s\n"
+ "[%{ptr}] Creating RCS channel for iAP"
+ "[%{ptr}] Deactivation skipped - error %#m\n"
+ "[%{ptr}] Force Key Frame, params: %@"
+ "[%{ptr}] Posting %@ after setting up buffered audio stream\n"
+ "[%{ptr}] Posting %@ on behalf of [%{ptr}]\n"
+ "[%{ptr}] Posting %@ when deactivating endpoint\n"
+ "[%{ptr}] Posting %@ when dissociating endpoint\n"
+ "[%{ptr}] ReportRTCMetrics '%@'\n"
+ "[%{ptr}] Sending AirPlay Signposts to Timestore: %@"
+ "[%{ptr}] Setting `%@`: %@"
+ "[%{ptr}] Updating stream (%@, displayIndex: %d) first resume time to %lf"
+ "[%{ptr}] carEndpoint_deactivateInternal() completed, activationSeed = %d, previousActivationSeed: %d\n"
+ "[%{ptr}] forwarding volume cache clear from subEndpoint [%{ptr}].\n"
+ "[%{ptr}], iAPChannel = %d"
+ "[0x%04X] RemoteMediaTimebase started. First audible time relative to now: %1.6f (startup time: %1.3f)\n"
+ "_Bool soft_acc_transportClient_destroyConnection(CFStringRef)"
+ "_Bool soft_acc_transportClient_destroyEndpoint(CFStringRef)"
+ "_Bool soft_acc_transportClient_processIncomingData(CFDataRef, CFStringRef)"
+ "_Bool soft_acc_transportClient_setPropertyForEndpointWithUUID(CFStringRef, CFTypeRef, CFStringRef)"
+ "alloc failed"
+ "can't find valid video track"
+ "carEndpoint_SetProperty_block_invoke_3"
+ "carEndpoint_createiAPChannelIfNeeded"
+ "carEndpoint_handleiAPChannelEvent"
+ "carEndpoint_sendCommandOverRCSChannel"
+ "currentHandler"
+ "dictionaryWithDictionary:"
+ "disconnectReason"
+ "enableSessionManagement"
+ "enableiAPChannel"
+ "err"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "iAPChannel"
+ "int soft_MKBDeviceUnlockedSinceBoot()"
+ "kCMBaseObjectError_Invalidated"
+ "kCMBaseObjectError_ParamErr"
+ "kFigBaseObjectError_AllocationFailed"
+ "kFigBaseObjectError_ValueNotAvailable"
+ "kFigEndpointError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_InvalidParameter"
+ "main-screen-orientation"
+ "messageID is missing in response event"
+ "resetSession"
+ "screenstream_handleOverrideCanvasSize"
+ "sessionManagement"
+ "sessionManagementInfo"
+ "softlink:r:path:/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AVConference.framework/AVConference"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CarKit.framework/CarKit"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag"
+ "softlink:r:path:/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger"
+ "stopSession"
+ "stringWithUTF8String:"
+ "type is missing in response event"
+ "void *AVConferenceLibrary(void)"
+ "void *AssistantServicesLibrary(void)"
+ "void *CarKitLibrary(void)"
+ "void *CarPlayServicesLibrary(void)"
+ "void *CoreAccessoriesLibrary(void)"
+ "void *CoreSpeechLibrary(void)"
+ "void *ExternalAccessoryLibrary(void)"
+ "void *MediaRemoteLibrary(void)"
+ "void *MobileKeyBagLibrary(void)"
+ "void *VoiceTriggerLibrary(void)"
+ "void carEndpoint_handleStreamResumed(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)_block_invoke_3"
+ "void carEndpoint_handleiAPChannelEvent(FigEndpointRemoteControlSessionRef, CFStringRef, CFDataRef, CFTypeRef)"
+ "void carManager_handleEndpointDeactivatedOrDissociated(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)_block_invoke"
+ "void endpointAggregate_handleBufferedAudioCapabilitiesChanged(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void endpointAggregate_handleSubEndpointVolumeCacheClear(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void endpointCluster_handleSubEndpointVolumeCacheClear(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void endpointLocal_handleBufferedAudioCapabilitiesChanged(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void soft_AFSiriActivationCarPlayDeviceVoice(uint64_t, NSString *, NSDictionary *, void (^)(BOOL, NSError *))"
+ "void soft_CRFetchCarPlayCapabilities(void (^)(NSDictionary *, NSError *))"
+ "void soft_CRFetchInstrumentClusterURLs(void (^)(NSArray<NSURL *> *, NSError *))"
+ "void soft_CRFetchScaledDisplays(NSArray<NSDictionary *> *, void (^)(NSArray<NSDictionary *> *, NSError *))"
+ "void soft_acc_transportClient_endpointSecureTunnelDataSend(CFStringRef, uint8_t, CFDataRef)"
+ "void soft_acc_transportClient_serverDisconnectedHandler(ACCTransportClientServerDisconnectedCF)"
+ "void soft_acc_transportClient_setConnectionAuthStatusDidChangeHandler(ACCTransportClientConnectionAuthStatusDidChangeHandlerCF)"
+ "void soft_acc_transportClient_setEndpointSecureTunnelDataReceiveHandler(CFStringRef, ACCTransportClientSecureTunnelDataReceiveHandlerCF)"
+ "wirelessdisplay_maxtimesreencodeidle"
+ "{%kO=%O%kO=%D%kO=%D%kO=%s%kO=%.6a%kO=%.6a%kO=%i%kO=%O%kO=%.6a%kO=%i%kO=%O%kO=%O%kO=%O}"
- " with new value"
- "/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory"
- "/System/Library/PrivateFrameworks/AVConference.framework/AVConference"
- "/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices"
- "/System/Library/PrivateFrameworks/CarKit.framework/CarKit"
- "/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices"
- "/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories"
- "/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech"
- "/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport"
- "/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication"
- "/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote"
- "/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth"
- "/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag"
- "/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger"
- "845.6.1"
- "APCarPlay_wasFirmwareVersion"
- "APCarPlay_wasManufacturer"
- "APCarPlay_wasModel"
- "APCarPlay_wasWireless"
- "APEndpointPlaybackSessionUpdateNowPlayingTransaction"
- "APEndpointStreamUpdateNowPlayingTransaction"
- "BAE [%{ptr}] %sflushWithinRangeLimitTime set to %1.1f seconds\n"
- "Boolean coreUtilsPairing_IsPeerKnown(APPairingClientRef)"
- "CFArrayRef manager_copyEndpoints(FigEndpointManagerRef, APEndpointManagerCopyEndpointsQualifier)"
- "Endpoint %{ptr}: waiting for auth completion timeout after 30 secs\n"
- "First audible time relative to now: %1.6f \n"
- "OSStatus APPairingClientCoreUtilsCreate(CFAllocatorRef, CFStringRef, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, CFStringRef, CFStringRef, CFDataRef, FigTransportStreamRef, CFStringRef, APPairingClientRef *)"
- "OSStatus coreUtilsPairingPeerCache_SavePeer(const void *, size_t, const uint8_t *, void *)"
- "OSStatus coreUtilsPairingPeerCache_SavePeer(const void *, size_t, const uint8_t *, void *)_block_invoke_2"
- "Peer Cache"
- "PeerIdentifier"
- "PeerPublicKey"
- "Stored new"
- "Updated"
- "WASCalibrationSupportsMATAtmos"
- "[%{ptr}] %s item in %s%s:\n\"%@\" :\n%@"
- "[%{ptr}] %s playing"
- "[%{ptr}] %s[%u]:\n%@ :\n%@"
- "[%{ptr}] APPairingClientCoreUtils created %c%c%c%c%c%c%c%c%c%c.\n"
- "[%{ptr}] APSenderSessionBroadcastKeysForDiagnosticsData() failed: %m (encryptionContext = %@, localPort = %d, remoteDataPort = %d)"
- "[%{ptr}] APSenderSessionBroadcastKeysForDiagnosticsData() with localPort = %d, RemotePort = %d, LocalSendsWithReadKey = %d"
- "[%{ptr}] All items in %s:"
- "[%{ptr}] Forcing coreUtilsPairing_IsPeerKnown to return false\n"
- "[%{ptr}] Forcing coreUtilsPairing_IsPeerKnown to return true\n"
- "[%{ptr}] Is peer known: %d, peerIdentifier: %s (processing time: %llu ms, err: %d)\n"
- "[%{ptr}] Number of items in %s: %d"
- "[%{ptr}] PairingSessionCopyPeerIdentifier returned %s (err: %d) \n"
- "[%{ptr}] Removing random item from %s:\n\"%@\" :\n%@"
- "[%{ptr}] Set MATAtmos Playback Pref %s"
- "[%{ptr}] Unsupported copyEndpoints qualifier: %d\n"
- "[%{ptr}] Using %s with size: %d\n"
- "[%{ptr}] carEndpoint_deactivateInternal() completed, activationSeed = %d \n"
- "audioStream_audioHoseEnableMATAtmosPlaybackInternal"
- "bufferedAudioEngine_updateMATAtmosPlaybackPreferenceIfNecessary"
- "bufferedAudio_flushForwardLimitSecs"
- "coreUtilsPairingPeerCache_SavePeer"
- "en"
- "forcePeerKnown"
- "forcePeerUnknown"
- "initWithObjectsAndKeys:"
- "kAVCMediaStreamOptionCallID"
- "matAtmosPlaybackEnabled"
- "started"
- "stopped"
- "void APEndpointPlaybackSessionUpdateNowPlayingTransaction(FigEndpointPlaybackSessionRef, Boolean, LogCategory *, APSWiFiTransactionRef *)"
- "void APEndpointStreamUpdateNowPlayingTransaction(FigEndpointStreamRef, Boolean, LogCategory *, APSWiFiTransactionRef *)"
- "void audioStream_audioHoseEnableMATAtmosPlaybackInternal(void *)"
- "{%kO=%O%kO=%D%kO=%D%kO=%s%kO=%.6a%kO=%.6a%kO=%i%kO=%i%kO=%O%kO=%.6a%kO=%i%kO=%O%kO=%O%kO=%O}"

```
