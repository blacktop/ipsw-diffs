## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/Versions/A/AirPlaySender`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__data`

```diff

-980.67.2.0.0
-  __TEXT.__text: 0x1d8898
+980.71.1.0.0
+  __TEXT.__text: 0x1d3c7c
   __TEXT.__objc_methlist: 0x92c
   __TEXT.__const: 0xd4f0
   __TEXT.__gcc_except_tab: 0x5ec
-  __TEXT.__cstring: 0x72046
+  __TEXT.__cstring: 0x702af
   __TEXT.__dlopen_cstrs: 0x164
   __TEXT.__oslogstring: 0xb29
-  __TEXT.__unwind_info: 0x44a0
+  __TEXT.__unwind_info: 0x4438
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4328
+  __DATA_CONST.__const: 0x42c8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_selrefs: 0xaf0
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0x1dd0
-  __AUTH_CONST.__const: 0x7390
-  __AUTH_CONST.__cfstring: 0x10b60
+  __DATA_CONST.__got: 0x1dd8
+  __AUTH_CONST.__const: 0x71d0
+  __AUTH_CONST.__cfstring: 0x10480
   __AUTH_CONST.__objc_const: 0xc58
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x1b8

   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x840
   __DATA.__objc_ivar: 0x84
-  __DATA.__data: 0x17990
-  __DATA.__bss: 0xe80
+  __DATA.__data: 0x17920
+  __DATA.__bss: 0xe58
   __DATA_DIRTY.__data: 0xcf0
-  __DATA_DIRTY.__bss: 0x2a8
+  __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9129
-  Symbols:   8804
-  CStrings:  9337
+  Functions: 9003
+  Symbols:   8760
+  CStrings:  9175
 
Symbols:
+ GCC_except_table128
+ _APEndpointDescriptionCopyEndpointID
+ _APSCFDictionarySetDictionaryCopy
+ _APSTapToRadarInvokeWithUserNotification
+ _CMPropagateAttachments
+ _CMSampleBufferSetOutputPresentationTimeStamp
+ ___block_descriptor_50_e47_v28?0i8^{__CFString=}12^{OpaqueFigEndpoint=}20l
+ __emp_introspector_copyDescription_block_invoke
+ _apsession_flushFallbackToInfraReasonsToRTC
+ _apsession_stageFallbackToInfraReason
+ _emp_cancelCachePromotionDeadlineIfNecessary
+ _emp_unmarkTransientEndpoint
+ _kAPSAudioProtocolDriverHoseProperty_IsRoutedViaPrimaryAssist
+ _kAPTTerminusMonitorDeviceInfoKey_IsRoutedViaPrimaryAssist
- APEndpointPlusUtils_CopyDeviceIDFromEndpointDescription
- APMulticastProbeSenderCreate
- APMulticastProbeSenderGetShared
- APMulticastProbeSenderGetShared.multicastProbeSender
- APMulticastProbeSenderGetShared.once
- APMulticastProbeSenderReleaseSSMGroupInfo
- APMulticastProbeSenderUnregister
- GCC_except_table129
- _APMulticastProbeSenderCopySSMGroupInfo
- _APMulticastProbeSenderCreate
- _APMulticastProbeSenderGetCMBaseObject
- _APMulticastProbeSenderGetShared
- _APMulticastProbeSenderRegister
- _APMulticastProbeSenderReleaseSSMGroupInfo
- _APMulticastProbeSenderUnregister
- _APMulticastProbeSenderUpdateMC2UC
- _APSCFStringToSockAddr
- _APSCopyNetworkInterfaceType
- _SocketSetMulticastInterface
- __APMulticastProbeSenderFormattingDescription
- __APMulticastProbeSenderGetShared_block_invoke
- ___APMulticastProbeSenderGetShared_block_invoke
- ___block_descriptor_41_e47_v28?0i8^{__CFString=}12^{OpaqueFigEndpoint=}20l
- ___multicastProbeSender_GetClassID_block_invoke
- ___multicastProbeSender_clearSocketList_block_invoke
- ___multicastProbeSender_createMC2UCProbingTimer_block_invoke
- ___multicastProbeSender_probeForMC2UC_block_invoke
- ___multicastProbeSender_updateTxProbePacketsForClients_block_invoke
- __emp_restartCachePromotionDeadlineIfNecessary_block_invoke
- __multicastProbeSender_createMC2UCProbingTimer_block_invoke
- __multicastProbeSender_updateTxProbePacketsForClients_block_invoke
- _connect
- _endpoint_handleUpdateMC2UCStatus
- _gLogCategory_APMulticastProbeSender
- _getsockname
- _if_nametoindex
- _kAPMulticastProbeSenderVTable
- _kAPMulticastProbeSender_APMulticastProbeSenderClassWrapper
- _kAPMulticastProbeSender_BaseClassWrapper
- _kAPSenderSessionProperty_MC2UCToken
- _kSCNetworkInterfaceTypeIEEE80211
- _multicastProbeSender_Finalize
- _multicastProbeSender_Invalidate
- _multicastProbeSender_constructMulticastGroupInfoForAddressFamily
- _multicastProbeSender_decrementRefCountForSSMGroupInfo
- _multicastProbeSender_incrementRefCountForSSMGroupInfo
- _multicastProbeSender_probeForMC2UC
- _multicastProbeSender_registerDeviceForAddressFamily
- _send
- apsession_determineTransportAvailabilityAndWaitIfNeeded
- multicastProbeSender_GetClassID.classID
- multicastProbeSender_GetClassID.descriptor
- multicastProbeSender_GetClassID.onceToken
- multicastProbeSender_constructMulticastGroupInfoForAddressFamily
- multicastProbeSender_create.isMC2UCDetectionEnabled
- multicastProbeSender_decrementRefCountForSSMGroupInfo
- multicastProbeSender_incrementRefCountForSSMGroupInfo
- multicastProbeSender_registerDeviceForAddressFamily
CStrings:
+ "    [0x%04X]\n"
+ "980.71.1"
+ "APEndpointDescriptionCopyEndpointID"
+ "AirPlay Internal Error"
+ "Available Endpoints: %lu\n"
+ "Boolean apsession_determineTransportAvailabilityAndWaitIfNeeded(APSenderSessionRef, APSenderSessionConnectionType, APSenderSessionConnectionType, APSenderSessionConnectionType *, Boolean, OSStatus *, APTransportDeviceUnavailableReason *)"
+ "Boolean apsession_isTransportRecommended(APSenderSessionRef, APSenderSessionConnectionType, APTransportDeviceUnavailableReason *)"
+ "ID: %@\n"
+ "OSStatus bufferedAudioEngine_applyTargetLatencyIfNeeded(FigEndpointStreamAudioEngineRef, CFDictionaryRef, Boolean, Boolean)"
+ "OSStatus bufferedAudioEngine_updateLatencies(FigEndpointStreamAudioEngineRef, CFDictionaryRef, Boolean, Boolean)"
+ "OSStatus emp_addEndpoint(FigEndpointManagerRef, CFStringRef, FigEndpointRef, APEndpointPlusType, Boolean)"
+ "OSStatus emp_removeEndpoint(FigEndpointManagerRef, CFStringRef, APEndpointPlusType, Boolean)"
+ "PersistentConnectionConfigChanged"
+ "Transient Endpoints: %lu\n"
+ "We need your help!\nAirPlay has detected an error under active investigation. Please file a Radar to help us resolve this issue.\n\nThank you!"
+ "[%{ptr}] %s %s Plus [%{ptr}] %@ %'@ to [%{ptr}]"
+ "[%{ptr}] Clear transient endpoints"
+ "[%{ptr}] Mark transient endpoint [%{ptr}]"
+ "[%{ptr}] Storing fallback to infra reasons=%#{flags}"
+ "[%{ptr}] Unmark transient endpoint [%{ptr}]"
+ "[%{ptr}] dedicated socket has no encryption context; skipping diagnostics key broadcast\n"
+ "[%{ptr}] shared-connection RCS; skipping diagnostics key broadcast\n"
+ "fallbackToInfraReasons"
+ "void apEndpointRemoteControlSession_sendDiagnosticDataForTransportStreamIfNeeded(FigEndpointRemoteControlSessionRef, APTransportStreamRef, int64_t, CFStringRef, Boolean)"
+ "void apsession_flushFallbackToInfraReasonsToRTC(APSenderSessionRef)"
+ "void emp_clearTransientEndpoints(FigEndpointManagerRef)"
+ "void emp_markTransientEndpoint(FigEndpointManagerRef, FigEndpointRef)"
+ "void emp_unmarkTransientEndpoint(FigEndpointManagerRef, FigEndpointRef)"
- "\tDetection stats\t: \"MC2UC Status [IPv6]\" = %s\n"
- "\tDetection stats\t: \"MC2UC Status\" = %s\n"
- "\tDetection stats\t: \"Percentage of time (Enabled) [IPv6]\" = %u%%\n"
- "\tDetection stats\t: \"Percentage of time (Enabled)\" = %u%%\n"
- "\tDetection stats\t: \"Probes Rx [IPv6]\" = %d\n"
- "\tDetection stats\t: \"Probes Rx\" = %d\n"
- "\tDetection stats\t: \"Probes Tx [IPv6]\" = %d\n"
- "\tDetection stats\t: \"Probes Tx\" = %d\n"
- "\tDetection stats\t: \"Time-to-detect [IPv6]\" = %dms\n"
- "\tDetection stats\t: \"Time-to-detect\" = %dms\n"
- "\tDetection stats : \"Percentage of time (Disabled) [IPv6]\" = %u%%\n"
- "\tDetection stats : \"Percentage of time (Disabled)\" = %u%%\n"
- "\tDetection stats : \"Status flip count [IPv6]\" = %d\n"
- "\tDetection stats : \"Status flip count\" = %d\n"
- "%p-%llu"
- "%s_%u"
- "980.67.2"
- "APEndpointPlusUtils_CopyDeviceIDFromEndpointDescription"
- "APMulticastProbeSender"
- "APMulticastProbeSender Finalized\n"
- "APMulticastProbeSenderCopySSMGroupInfo"
- "APMulticastProbeSenderRegister"
- "APMulticastProbeSenderReleaseSSMGroupInfo"
- "APMulticastProbeSenderUnregister"
- "APMulticastProbeSenderUpdateMC2UC"
- "AirPlay Issue"
- "AirPlayMulticastProbeSenderQueue"
- "AudioAccessory1,"
- "AudioAccessory5,"
- "AudioAccessory6,"
- "Available Endpoints:\n"
- "Boolean apsession_determineTransportAvailabilityAndWaitIfNeeded(APSenderSessionRef, APSenderSessionConnectionType, APSenderSessionConnectionType, APSenderSessionConnectionType *, Boolean, OSStatus *)"
- "Boolean apsession_isTransportRecommended(APSenderSessionRef, APSenderSessionConnectionType)"
- "CFDataRef multicastProbeSender_createPayloadForMC2UC(APMulticastProbeSenderRef, uint32_t)"
- "DeviceID: %llu\n"
- "Disabled"
- "Enabled"
- "Failed to create APMulticastProbeSender with err=%#m, %s\n"
- "MC2UCCryptor"
- "MC2UCDetection"
- "MC2UCDisabledTotalTimeTicks"
- "MC2UCDisabledTotalTimeTicksIPv6"
- "MC2UCEnabledTotalTimeTicks"
- "MC2UCEnabledTotalTimeTicksIPv6"
- "MC2UCInterface"
- "MC2UCInterfaceName"
- "MC2UCLastStatusChangeTimeTicks"
- "MC2UCLastStatusChangeTimeTicksIPv6"
- "MC2UCReferenceCount"
- "MC2UCRxCount"
- "MC2UCRxCountIPv6"
- "MC2UCSSMGroupInfo"
- "MC2UCSocketFd"
- "MC2UCStatus"
- "MC2UCStatusFlipCount"
- "MC2UCStatusFlipCountIPv6"
- "MC2UCStatusIPv6"
- "MC2UCStatusLatest"
- "MC2UCStatusLatestIPv6"
- "MC2UCTimeToDetect"
- "MC2UCTimeToDetectIPv6"
- "MC2UCToken"
- "MC2UCTxCount"
- "MC2UCTxCountIPv6"
- "No mc2uc metrics found\n"
- "OSStatus APMulticastProbeSenderRegister(CMBaseObjectRef, CFStringRef, CFStringRef)"
- "OSStatus APMulticastProbeSenderReleaseSSMGroupInfo(CMBaseObjectRef, CFStringRef)"
- "OSStatus APMulticastProbeSenderUnregister(CMBaseObjectRef, CFStringRef, CFDictionaryRef *)"
- "OSStatus APMulticastProbeSenderUpdateMC2UC(CMBaseObjectRef, CFStringRef, uint32_t, MC2UCFeatureStatus, int32_t, APMC2UCIPVersion)"
- "OSStatus bufferedAudioEngine_applyTargetLatencyIfNeeded(FigEndpointStreamAudioEngineRef, CFDictionaryRef, const Boolean)"
- "OSStatus bufferedAudioEngine_updateLatencies(FigEndpointStreamAudioEngineRef, CFDictionaryRef, const Boolean)"
- "OSStatus emp_addEndpoint(FigEndpointManagerRef, CFStringRef, FigEndpointRef, APEndpointPlusType)"
- "OSStatus emp_removeEndpoint(FigEndpointManagerRef, CFStringRef, APEndpointPlusType)"
- "OSStatus multicastProbeSender_Invalidate(CMBaseObjectRef)"
- "OSStatus multicastProbeSender_constructMulticastGroupInfoForAddressFamily(APMulticastProbeSenderRef, CFStringRef, sa_family_t, CFMutableDictionaryRef *)"
- "OSStatus multicastProbeSender_create(CFDictionaryRef, APMulticastProbeSenderRef *)"
- "OSStatus multicastProbeSender_createEncryptionKeyAndCryptor(APMulticastProbeSenderRef, CFDataRef *, APSCryptorRef *)"
- "OSStatus multicastProbeSender_createMC2UCProbingTimer(APMulticastProbeSenderRef)"
- "OSStatus multicastProbeSender_createMulticastGroupInfo(APMulticastProbeSenderRef, CFStringRef, CFDictionaryRef *)"
- "OSStatus multicastProbeSender_decrementRefCountForSSMGroupInfo(APMulticastProbeSenderRef, const char *, sa_family_t)"
- "OSStatus multicastProbeSender_incrementRefCountForSSMGroupInfo(APMulticastProbeSenderRef, CFStringRef, CFMutableDictionaryRef)"
- "OSStatus multicastProbeSender_probeForMC2UC(CMBaseObjectRef, sa_family_t)"
- "OSStatus multicastProbeSender_probeForMC2UC(CMBaseObjectRef, sa_family_t)_block_invoke"
- "OSStatus multicastProbeSender_registerDeviceForAddressFamily(APMulticastProbeSenderRef, CFStringRef, CFStringRef, sa_family_t)"
- "OSStatus multicastProbeSender_updateTxProbePacketsForClients(CMBaseObjectRef, int, sa_family_t)_block_invoke"
- "[%{ptr}] APMulticastProbeSender Finalizing\n"
- "[%{ptr}] APMulticastProbeSenderUpdateMC2UC deviceName=%@, probeBurstID=%u, IP ver=%u, mc2ucStatus=%d packetCount=%d\n"
- "[%{ptr}] An entry already exists for ifaceName_addressFamily='%@', socket=%d\n"
- "[%{ptr}] ChaCha Cryptor created with shared key\n"
- "[%{ptr}] Cleared socketList.\n"
- "[%{ptr}] Closed socket[%d] for key='%@'\n"
- "[%{ptr}] Connecting to ssmGroupIPv4Addr=%##a"
- "[%{ptr}] Connecting to ssmGroupIPv6Addr=%##a"
- "[%{ptr}] Created APMulticastProbeSender\n"
- "[%{ptr}] Failed to add MC2UC group info with err=%#m\n"
- "[%{ptr}] Failed to create socket with err=%#m\n"
- "[%{ptr}] Failed to encrypt probing msg\n"
- "[%{ptr}] Failed to form msg data\n"
- "[%{ptr}] Failed to register [%@] for MC2UC detection, error=%#m.\n"
- "[%{ptr}] Failed to register device for MC2UC detection.\n"
- "[%{ptr}] Failed to remove reference for < interfaceName_addressFamily, <socket, SSM group info> >.\n"
- "[%{ptr}] Failed to send MC2UC probe packets on IPv%u.\n"
- "[%{ptr}] Invalid addressFamily=%u!\n"
- "[%{ptr}] Invalid inAddressFamily=%u!\n"
- "[%{ptr}] Invalid inFamily=%u!\n"
- "[%{ptr}] Invalidated\n"
- "[%{ptr}] MC2UC - Decrement the ref count for interface=%@ by 1\n"
- "[%{ptr}] MC2UC - Unregistered device name=%@\n"
- "[%{ptr}] MC2UC - Unregistering device name=%@\n"
- "[%{ptr}] MC2UC Successfully registered device='%@' for MC2UC probing on IPv%u\n"
- "[%{ptr}] MC2UC added entry for interface_family [%@]\n"
- "[%{ptr}] MC2UC periodic probing timer created.\n"
- "[%{ptr}] MC2UC probing on IPv6 is unsupported!\n"
- "[%{ptr}] MC2UC probing periodic timer is resumed.\n"
- "[%{ptr}] MC2UC probing periodic timer stopped.\n"
- "[%{ptr}] Mc2UcDetectionEnabled=%d, isGroupPlaybackSession=%d, interfaceName=%@"
- "[%{ptr}] Received MC2UC feedback from [%@] [IPv4] MC2UCProbeBurstID=%d, TimeToDetect(RTT)=%dms, MC2UCStatus=%s.\n"
- "[%{ptr}] Received MC2UC feedback from [%@] [IPv6] MC2UCProbeBurstID=%d, TimeToDetect(RTT)=%dms, MC2UCStatus=%s.\n"
- "[%{ptr}] Registering device name=%@, interface=%@ for MC2UC probing.\n"
- "[%{ptr}] Report MC2UC KPIs for [%@]:\n"
- "[%{ptr}] Sent a probe packet, burstID:%u, src:%##a dest:%##a on interface[%s] bytesSent=%d"
- "[%{ptr}] Set refCount=%d for key='%@'\n"
- "[%{ptr}] Socket address %##a\n"
- "[%{ptr}] SocketSetMulticastInterface failed with err=%#m\n"
- "[%{ptr}] Unsupported inFamily=%u!\n"
- "[%{ptr}] Updated reference count=%d for key='%@'\n"
- "[%{ptr}] [IPv%u] Updated Tx probe packet count for '%@' with TxProbePktsCount=%d.\n"
- "[%{ptr}] [IPv4] MC2UC status for [%@] changed from old MC2UCStatus=%s to new MC2UCStatus=%s, MC2UCProbeBurstID=%d, timeSinceLastStateChange=%lus, TotalTimeSpentSoFarInStatus[%s]=%lus, statusFlipCount=%d.\n"
- "[%{ptr}] [IPv6] MC2UC status for [%@] changed from old MC2UCStatus=%s to new MC2UCStatus=%s, MC2UCProbeBurstID=%d, timeSinceLastStateChange=%lus, TotalTimeSpentSoFarInStatus[%s]=%lus, statusFlipCount=%d\n"
- "[%{ptr}] [probeBurstID=%u] keysDict = %@\n"
- "[%{ptr}] connect failed with err=%#m\n"
- "[%{ptr}] defaults write ssmGroupIPv4Addr=%@"
- "[%{ptr}] defaults write ssmGroupIPv6Addr=%@"
- "[%{ptr}] getsockname failed with err=%#m\n"
- "[%{ptr}] probeForMC2UC: addressFamily=%u, probeBurstID=%u\n"
- "[%{ptr}] registerForMC2UCDetection [DeviceName '%@' - Supports MC2UCDetection=%d], isMC2UCDetectionEnabled=%d, isGroupPlayback=%d\n"
- "[%{ptr}] ssmGroupIPv4Addr=%##a"
- "[%{ptr}] ssmGroupIPv6Addr=%##a"
- "[APMulticastProbeSender %p]"
- "apsession_registerForMC2UCDetection"
- "burstID"
- "endpoint_collectMC2UCMetrics"
- "endpoint_handleUpdateMC2UCStatus"
- "groupEncryptionKey"
- "groupIPv4Addr"
- "groupIPv6Addr"
- "mc2ucDetectionSSMGroupIPv4Addr"
- "mc2ucDetectionSSMGroupIPv6Addr"
- "mc2ucDetectionSSMGroupInfo"
- "mc2ucIPVersion"
- "mc2ucPktCnt"
- "mc2ucProbeBurstID"
- "mc2ucStatus"
- "multicastProbeSender_constructMulticastGroupInfoForAddressFamily"
- "multicastProbeSender_create"
- "multicastProbeSender_create isMC2UCDetectionEnabled=%d"
- "multicastProbeSender_createEncryptionKeyAndCryptor"
- "multicastProbeSender_createMC2UCProbingTimer"
- "multicastProbeSender_createMulticastGroupInfo"
- "multicastProbeSender_createPayloadForMC2UC"
- "multicastProbeSender_decrementRefCountForSSMGroupInfo"
- "multicastProbeSender_incrementRefCountForSSMGroupInfo"
- "multicastProbeSender_probeForMC2UC"
- "multicastProbeSender_probeForMC2UC_block_invoke"
- "multicastProbeSender_registerDeviceForAddressFamily"
- "multicastProbeSender_updateTxProbePacketsForClients"
- "multicastToUnicastDisabledTimePercent"
- "multicastToUnicastEnabledTimePercent"
- "multicastToUnicastIPv6DisabledTimePercent"
- "multicastToUnicastIPv6EnabledTimePercent"
- "multicastToUnicastIPv6ReceivedPacketCount"
- "multicastToUnicastIPv6Status"
- "multicastToUnicastIPv6StatusFlipCount"
- "multicastToUnicastIPv6TimeToDetectMs"
- "multicastToUnicastIPv6TransmittedPacketCount"
- "multicastToUnicastReceivedPacketCount"
- "multicastToUnicastStatus"
- "multicastToUnicastStatusFlipCount"
- "multicastToUnicastTimeToDetectMs"
- "multicastToUnicastTransmittedPacketCount"
- "sourceIPv4Addr"
- "sourceIPv6Addr"
- "updateMC2UCStatus"
- "void apEndpointRemoteControlSession_sendDiagnosticDataForTransportStreamIfNeeded(FigEndpointRemoteControlSessionRef, APTransportStreamRef, int64_t, CFStringRef)"
- "void apsession_addMC2UCDetectionInfo(APSenderSessionRef, CFMutableDictionaryRef)"
- "void apsession_registerForMC2UCDetection(APSenderSessionRef)"
- "void endpoint_collectMC2UCMetrics(FigEndpointRef, APSenderSessionRef, CFMutableDictionaryRef)"
- "void multicastProbeSender_Finalize(CMBaseObjectRef)"
- "void multicastProbeSender_clearSocketList(APMulticastProbeSenderRef)"
- "void multicastProbeSender_configureSSM(APMulticastProbeSenderRef, sa_family_t)"
```
