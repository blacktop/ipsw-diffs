## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-860.7.1.0.0
-  __TEXT.__text: 0x147cc0
-  __TEXT.__auth_stubs: 0x36e0
-  __TEXT.__objc_methlist: 0xa94
-  __TEXT.__const: 0x322d5
+890.61.4.11.2
+  __TEXT.__text: 0x1533e8
+  __TEXT.__auth_stubs: 0x3810
+  __TEXT.__objc_methlist: 0xad4
+  __TEXT.__const: 0x322fe
   __TEXT.__dlopen_cstrs: 0xad
-  __TEXT.__gcc_except_tab: 0x7bc
-  __TEXT.__cstring: 0x2cec4
-  __TEXT.__unwind_info: 0x16f0
-  __TEXT.__eh_frame: 0x1b28
+  __TEXT.__gcc_except_tab: 0x7e8
+  __TEXT.__cstring: 0x2ecf8
+  __TEXT.__unwind_info: 0x1470
+  __TEXT.__eh_frame: 0xc0
   __TEXT.__objc_classname: 0x144
-  __TEXT.__objc_methname: 0x2653
-  __TEXT.__objc_methtype: 0x154e
-  __TEXT.__objc_stubs: 0x2780
-  __DATA_CONST.__got: 0x838
-  __DATA_CONST.__const: 0x1b90
+  __TEXT.__objc_methname: 0x2756
+  __TEXT.__objc_methtype: 0x1605
+  __TEXT.__objc_stubs: 0x2880
+  __DATA_CONST.__got: 0x870
+  __DATA_CONST.__const: 0x1d88
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb50
+  __DATA_CONST.__objc_selrefs: 0xb90
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1b80
-  __AUTH_CONST.__const: 0xadc8
-  __AUTH_CONST.__cfstring: 0xa740
-  __AUTH_CONST.__objc_const: 0x14f0
+  __AUTH_CONST.__auth_got: 0x1c18
+  __AUTH_CONST.__const: 0xafc0
+  __AUTH_CONST.__cfstring: 0xada0
+  __AUTH_CONST.__objc_const: 0x1530
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x168
-  __DATA.__data: 0x177e8
-  __DATA.__bss: 0x6d8
-  __DATA.__common: 0xa18
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x170
+  __DATA.__data: 0x17610
+  __DATA.__bss: 0x5a8
+  __DATA.__common: 0xa0c
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__data: 0x310
+  __DATA_DIRTY.__bss: 0x188
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D209688B-8A5E-3C05-9AE6-9F8291970A92
-  Functions: 1565
-  Symbols:   4935
-  CStrings:  6574
+  UUID: 6BB70C87-CB1C-3AB5-A7CB-47351C264717
+  Functions: 1585
+  Symbols:   5071
+  CStrings:  6806
 
Symbols:
+ +[AirPlayReceiverPlatform _setMediaAVAudioSessionActiveSync:]
+ -[AirPlayReceiverContext startNowPlayingSessionTask]
+ -[AirPlayReceiverMediaRemoteHelper startNowPlayingSessionWithCompletion:]
+ -[AirPlayReceiverPlatform _setMediaAVAudioSessionActive:]
+ -[AirPlayReceiverPlatform _startNowPlayingSessionAsync:]
+ GCC_except_table102
+ GCC_except_table103
+ GCC_except_table1049
+ GCC_except_table1068
+ GCC_except_table107
+ GCC_except_table109
+ GCC_except_table1119
+ GCC_except_table1123
+ GCC_except_table114
+ GCC_except_table116
+ GCC_except_table1176
+ GCC_except_table1184
+ GCC_except_table1186
+ GCC_except_table119
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table135
+ GCC_except_table139
+ GCC_except_table140
+ GCC_except_table146
+ GCC_except_table150
+ GCC_except_table157
+ GCC_except_table158
+ GCC_except_table173
+ GCC_except_table184
+ GCC_except_table202
+ GCC_except_table208
+ GCC_except_table209
+ GCC_except_table213
+ GCC_except_table219
+ GCC_except_table404
+ GCC_except_table453
+ GCC_except_table499
+ GCC_except_table50
+ GCC_except_table51
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table555
+ GCC_except_table559
+ GCC_except_table566
+ GCC_except_table574
+ GCC_except_table62
+ GCC_except_table68
+ GCC_except_table699
+ GCC_except_table81
+ GCC_except_table85
+ GCC_except_table87
+ GCC_except_table91
+ _APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName
+ _APMulticastProbeReceiverGetTypeID.initOnce
+ _APMulticastProbeReceiverGetTypeID.typeID
+ _APReceiverAudioSessionBufferedHoseCreate
+ _APReceiverRequestProcessorCopyProperty.3919
+ _APReceiverRequestProcessorCopyProperty.6935
+ _APReceiverRequestProcessorCopyProperty.7421
+ _APReceiverRequestProcessorSetProperty.4399
+ _APSAudioFormatDescriptionListCreateForMediumLatencyReceiver
+ _APSAudioProtocolDriverHoseDataAPATProtocolGetProtocolID
+ _APSAudioProtocolDriverReceiverAPATCreate
+ _APSAudioProtocolDriverReceiverGetCMBaseObject
+ _APSCFDictionaryGetSockAddr
+ _APSCryptorGetNull
+ _APSDisplayUtilsGetAggregatedDisplayProtectionBits
+ _APSIsOpenNANReceiverEnabled
+ _APSIsWHAParallelSetupProcessingEnabled
+ _APSStatsHistogramRemoveAllValues
+ _APSTXTRecordUtilsCopyCFStringFromTXTRecord
+ _APSTXTRecordUtilsGetBooleanFromTXTRecord
+ _APSTXTRecordUtilsGetInt64FromTXTRecord
+ _APTransportConnectionUnbufferedNWCreate
+ _Base64EncodeEx
+ _CFAllocatorAllocateTyped
+ _CMBaseObjectCopyProperty
+ _CMBaseObjectNotificationBarrier.3302
+ _CMBlockBufferGetTypeID
+ _FigCFArrayAppendArray
+ _FigCFArrayCreateMutableCopy
+ _FigCFArrayRemoveLastElementOfValue
+ _FigCFDictionarySetUInt32
+ _OBJC_CLASS_$_APSDeferredTask
+ _OBJC_IVAR_$_AirPlayReceiverContext._startNowPlayingSessionTask
+ _OBJC_IVAR_$_AirPlayReceiverPlatform._mediaAVAudioSessionActivationQueue
+ _ServerSocketOpenEx2
+ __APAdvertiserAddSubAdvertiserInfo
+ __APAdvertiserInfoAddAirPlayData
+ __APAdvertiserUpdateAdvertiserInfoCorrelationID
+ __APAdvertiserWantSubAdvertiserToBeStarted
+ __APMulticastProbeReceiverClassRegister
+ __AirPlayReceiverSessionUpdateMC2UCStatus
+ __Finalize.2350
+ __Finalize.6216
+ __GetTypeID.6213
+ __Init
+ __OBJC_$_CLASS_METHODS_AirPlayReceiverPlatform
+ __UpdateAVAudioSessionAudioMode.5313
+ ___56-[AirPlayReceiverPlatform _startNowPlayingSessionAsync:]_block_invoke
+ ___56-[AirPlayReceiverPlatform _startNowPlayingSessionAsync:]_block_invoke_2
+ ___57-[AirPlayReceiverPlatform _setMediaAVAudioSessionActive:]_block_invoke
+ ___73-[AirPlayReceiverMediaRemoteHelper startNowPlayingSessionWithCompletion:]_block_invoke
+ ___73-[AirPlayReceiverMediaRemoteHelper startNowPlayingSessionWithCompletion:]_block_invoke_2
+ ___73-[AirPlayReceiverMediaRemoteHelper startNowPlayingSessionWithCompletion:]_block_invoke_3
+ ___APMulticastProbeReceiverCreate_block_invoke
+ ___APMulticastProbeReceiverCreate_block_invoke_2
+ ___Block_byref_object_copy_.215
+ ___Block_byref_object_copy_.2881
+ ___Block_byref_object_dispose_.216
+ ___Block_byref_object_dispose_.2882
+ ____AirPlayReceiverSessionUpdateMC2UCStatus_block_invoke
+ ____Finalize_block_invoke
+ ____ScreenStart_block_invoke
+ ___block_descriptor_40_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32o40b_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32o40r48r_e20_v16?0^{__CFError=}8lr40l8r48l8s32l8
+ ___block_descriptor_59_e5_v8?0l
+ ___block_descriptor_60_e8_32o40o_e8_v12?0i8ls32l8s40l8
+ ___block_descriptor_68_e5_v8?0l
+ ___block_descriptor_tmp.105
+ ___block_descriptor_tmp.107
+ ___block_descriptor_tmp.113
+ ___block_descriptor_tmp.141
+ ___block_descriptor_tmp.143
+ ___block_descriptor_tmp.147
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.171
+ ___block_descriptor_tmp.171.6096
+ ___block_descriptor_tmp.172
+ ___block_descriptor_tmp.172.6097
+ ___block_descriptor_tmp.2265
+ ___block_descriptor_tmp.263
+ ___block_descriptor_tmp.28.2258
+ ___block_descriptor_tmp.29.3277
+ ___block_descriptor_tmp.297
+ ___block_descriptor_tmp.305
+ ___block_descriptor_tmp.313
+ ___block_descriptor_tmp.3236
+ ___block_descriptor_tmp.3295
+ ___block_descriptor_tmp.343
+ ___block_descriptor_tmp.3446
+ ___block_descriptor_tmp.345
+ ___block_descriptor_tmp.347
+ ___block_descriptor_tmp.349
+ ___block_descriptor_tmp.351
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.3663
+ ___block_descriptor_tmp.373
+ ___block_descriptor_tmp.3781
+ ___block_descriptor_tmp.3915
+ ___block_descriptor_tmp.40.7006
+ ___block_descriptor_tmp.413
+ ___block_descriptor_tmp.455
+ ___block_descriptor_tmp.49.3804
+ ___block_descriptor_tmp.52
+ ___block_descriptor_tmp.52.7346
+ ___block_descriptor_tmp.5210
+ ___block_descriptor_tmp.5778
+ ___block_descriptor_tmp.5968
+ ___block_descriptor_tmp.60.3259
+ ___block_descriptor_tmp.62
+ ___block_descriptor_tmp.646
+ ___block_descriptor_tmp.662
+ ___block_descriptor_tmp.665
+ ___block_descriptor_tmp.67
+ ___block_descriptor_tmp.69
+ ___block_descriptor_tmp.6915
+ ___block_descriptor_tmp.7009
+ ___block_descriptor_tmp.7339
+ ___block_descriptor_tmp.750
+ ___block_descriptor_tmp.786
+ ___block_descriptor_tmp.788
+ ___block_descriptor_tmp.88
+ ___block_descriptor_tmp.89
+ ___block_descriptor_tmp.90
+ ___block_descriptor_tmp.95
+ ___block_descriptor_tmp.957
+ ___block_literal_global.109
+ ___block_literal_global.115
+ ___block_literal_global.148
+ ___block_literal_global.149
+ ___block_literal_global.1562
+ ___block_literal_global.157
+ ___block_literal_global.2065
+ ___block_literal_global.2379
+ ___block_literal_global.261
+ ___block_literal_global.2854
+ ___block_literal_global.3234
+ ___block_literal_global.3314
+ ___block_literal_global.364
+ ___block_literal_global.3661
+ ___block_literal_global.3779
+ ___block_literal_global.448
+ ___block_literal_global.494
+ ___block_literal_global.5495
+ ___block_literal_global.561
+ ___block_literal_global.5719
+ ___block_literal_global.5776
+ ___block_literal_global.6992
+ ___block_literal_global.7337
+ ___block_literal_global.783
+ ___block_literal_global.955
+ ___sbufsink_EnqueueFrameWithUserData_block_invoke
+ _airplayReqProcessor_copyPairingType
+ _airplayReqProcessor_reportPerfMetricsIfNeeded
+ _airplayReqProcessor_updateLastControlMessage
+ _aprscreen_decryptBuffer
+ _audioSessionBufferedHose_copyProtocolDriverDataBBufsCallback
+ _audioSessionBufferedHose_copyRTPDataCallback
+ _audioSessionBufferedHose_protocolDriverReceiverAudioDataAvailableCallback
+ _audioSessionBufferedHose_protocolDriverTickTimerFire
+ _audioSessionBufferedHose_readyToSendBatchCallback
+ _audioSessionBufferedHose_receiveDataCallback
+ _audioSession_audioDecoderDecodeCallback.6058
+ _audioSession_audioDecoderDecodeFrame.6045
+ _audioSession_handleMediaDataControlRequest.3675
+ _audioSession_handleMediaDataControlRequest.5935
+ _audioSession_log.6069
+ _audioSession_networkThread.6079
+ _audioSession_performPeriodicTasks.6074
+ _audioSession_reportAudioPerformance
+ _audioSession_sessionLock.5972
+ _audioSession_sessionUnlock.5974
+ _bind
+ _gAirTunesRelativeTimeOffset.6100
+ _gHoseDataRTCPCallbacks
+ _gHoseDataRTPCallbacks
+ _gHoseRegistrarCopyFromProtocolDriverCallbacks
+ _gHoseRegistrarCopyFromTransportCallbacks
+ _gLogCategory_APMulticastProbeReceiver
+ _gLogCategory_APReceiverAudioSessionRealTimeRTCP
+ _gLogCategory_APReceiverAudioSessionRealTimeSocket
+ _gProtocolDriverCallbacks
+ _getsockopt
+ _kAPAdvertiserInfoProperty_CorrelationID
+ _kAPAdvertiserInfoProperty_NANServiceType
+ _kAPAdvertiserP2PConfig_AllowOpenFullNANAdvertising
+ _kAPAdvertiserP2PConfig_AllowOpenPartialNANAdvertising
+ _kAPAdvertiserP2PConfig_AllowSecurePartialNANAdvertising
+ _kAPMulticastProbeReceiverClass
+ _kAPRRemoteControlSessionMediaRemoteVTable.3270
+ _kAPRRemoteControlSessionMediaRemote_Class.3287
+ _kAPRRemoteControlSessionSession_BaseClassWrapper.3300
+ _kAPReceiverAudioSessionOption_DisableAudioRendering
+ _kAPReceiverAudioSessionOption_EncryptionReadKey
+ _kAPReceiverAudioSessionOption_EncryptionWriteKey
+ _kAPReceiverAudioSessionOption_ShouldAdjustPresentationByOutputLatency
+ _kAPReceiverAudioSessionOption_UseUDP
+ _kAPReceiverScreenSessionOption_PWDCryptor
+ _kAPReceiverSystemInfoProperty_AccessControlLevelHK
+ _kAPReceiverSystemInfoProperty_AccessControlType
+ _kAPReceiverSystemInfoProperty_GroupContainsDiscoverableLeader
+ _kAPReceiverSystemInfoProperty_IsAirPlayGroupLeader
+ _kAPReceiverSystemInfoProperty_IsPairingRequiredForAllClients
+ _kAPReceiverSystemInfoProperty_IsSilentPrimary
+ _kAPReceiverSystemInfoProperty_ParentGroupLeaderSupportsGroupCohesion
+ _kAPReceiverUIControllerParam_IsProtectedMirroring
+ _kAPSAudioPerformanceReportKey_LiveAdaptiveGlitchHistogram
+ _kAPSAudioProtocolDriverReceiverProperty_RTCPSignatureFailureCount
+ _kAPSAudioProtocolDriverReceiverProperty_RTPSignatureFailureCount
+ _kAPSEndpointStreamAudioHoseSBARCreationOption_IsSourceUnordered
+ _kAPTransportConnectionOption_IsPackageArrivalTicksEnabled
+ _kAPTransportConnectionOption_TransportProtocol
+ _kAPTransportConnectionPackageType_Datagram
+ _kAirPlayReceiverServerOption_UGLRCServerMode
+ _objc_msgSend$_setMediaAVAudioSessionActive:
+ _objc_msgSend$_setMediaAVAudioSessionActiveSync:
+ _objc_msgSend$_startNowPlayingSessionAsync:
+ _objc_msgSend$result
+ _objc_msgSend$setNotCompleted
+ _objc_msgSend$setResult:
+ _objc_msgSend$startNowPlayingSessionTask
+ _objc_msgSend$startNowPlayingSessionWithCompletion:
+ _recvmsg
+ _sbufsink_EnqueueFrameWithUserData
+ _socket
+ _soft_MRNowPlayingSessionManagerStartSession
+ _strerror
+ _sysInfo_updatePlayPassword
- GCC_except_table101
- GCC_except_table1020
- GCC_except_table1039
- GCC_except_table104
- GCC_except_table106
- GCC_except_table108
- GCC_except_table1090
- GCC_except_table1094
- GCC_except_table111
- GCC_except_table1147
- GCC_except_table1155
- GCC_except_table1157
- GCC_except_table117
- GCC_except_table122
- GCC_except_table127
- GCC_except_table131
- GCC_except_table132
- GCC_except_table136
- GCC_except_table145
- GCC_except_table160
- GCC_except_table171
- GCC_except_table187
- GCC_except_table193
- GCC_except_table194
- GCC_except_table198
- GCC_except_table203
- GCC_except_table390
- GCC_except_table42
- GCC_except_table43
- GCC_except_table439
- GCC_except_table44
- GCC_except_table45
- GCC_except_table46
- GCC_except_table478
- GCC_except_table534
- GCC_except_table538
- GCC_except_table545
- GCC_except_table553
- GCC_except_table60
- GCC_except_table65
- GCC_except_table67
- GCC_except_table678
- GCC_except_table69
- GCC_except_table79
- GCC_except_table94
- GCC_except_table95
- GCC_except_table99
- _APAdvertiserInfoCopyCFStringFromTXTRecord
- _APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName
- _APAdvertiserInfoGetBooleanFromTXTRecord
- _APAdvertiserInfoGetInt64FromTXTRecord
- _APReceiverRequestProcessorCopyProperty.3905
- _APReceiverRequestProcessorCopyProperty.6843
- _APReceiverRequestProcessorCopyProperty.7301
- _APReceiverRequestProcessorSetProperty.4376
- _APSEndpointStreamAudioHoseCopyProperty
- _APSHasNANSupport
- _APSNetworkClockRemoveAllPeers
- _APSShouldClusterEngageOnActivation
- _APTransportConnectionTCPUnbufferedNWCreate
- _BonjourDevice_GetInt64
- _CFAllocatorAllocate
- _CMBaseObjectNotificationBarrier.3296
- __Finalize.6125
- __GetTypeID.6122
- __SetVolumeSliderValue
- __UpdateAVAudioSessionAudioMode.5233
- ___Block_byref_object_copy_.178
- ___Block_byref_object_copy_.2875
- ___Block_byref_object_dispose_.179
- ___Block_byref_object_dispose_.2876
- ___block_descriptor_48_e8_32o40o_e20_v16?0^{__CFError=}8ls32l8s40l8
- ___block_descriptor_50_e5_v8?0l
- ___block_descriptor_tmp.102
- ___block_descriptor_tmp.104
- ___block_descriptor_tmp.110
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.137
- ___block_descriptor_tmp.138
- ___block_descriptor_tmp.138.5103
- ___block_descriptor_tmp.167
- ___block_descriptor_tmp.167.6005
- ___block_descriptor_tmp.168
- ___block_descriptor_tmp.168.6006
- ___block_descriptor_tmp.226
- ___block_descriptor_tmp.2349
- ___block_descriptor_tmp.286
- ___block_descriptor_tmp.294
- ___block_descriptor_tmp.3225
- ___block_descriptor_tmp.327
- ___block_descriptor_tmp.3289
- ___block_descriptor_tmp.329
- ___block_descriptor_tmp.331
- ___block_descriptor_tmp.333
- ___block_descriptor_tmp.335
- ___block_descriptor_tmp.3439
- ___block_descriptor_tmp.35
- ___block_descriptor_tmp.357
- ___block_descriptor_tmp.3659
- ___block_descriptor_tmp.3777
- ___block_descriptor_tmp.3902
- ___block_descriptor_tmp.394
- ___block_descriptor_tmp.418
- ___block_descriptor_tmp.46
- ___block_descriptor_tmp.49.3800
- ___block_descriptor_tmp.5137
- ___block_descriptor_tmp.56
- ___block_descriptor_tmp.5692
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.57.3253
- ___block_descriptor_tmp.58
- ___block_descriptor_tmp.5876
- ___block_descriptor_tmp.61
- ___block_descriptor_tmp.632
- ___block_descriptor_tmp.642
- ___block_descriptor_tmp.6822
- ___block_descriptor_tmp.6916
- ___block_descriptor_tmp.7226
- ___block_descriptor_tmp.727
- ___block_descriptor_tmp.75
- ___block_descriptor_tmp.763
- ___block_descriptor_tmp.765
- ___block_descriptor_tmp.80
- ___block_descriptor_tmp.82
- ___block_descriptor_tmp.968
- ___block_literal_global.106
- ___block_literal_global.112
- ___block_literal_global.113
- ___block_literal_global.144
- ___block_literal_global.153
- ___block_literal_global.1615
- ___block_literal_global.2117
- ___block_literal_global.224
- ___block_literal_global.2455
- ___block_literal_global.2848
- ___block_literal_global.3223
- ___block_literal_global.3308
- ___block_literal_global.343
- ___block_literal_global.3657
- ___block_literal_global.3775
- ___block_literal_global.415
- ___block_literal_global.458
- ___block_literal_global.517
- ___block_literal_global.5412
- ___block_literal_global.5633
- ___block_literal_global.5690
- ___block_literal_global.6900
- ___block_literal_global.7224
- ___block_literal_global.791
- ___block_literal_global.966
- __os_feature_enabled_impl
- _audioSession_audioDecoderDecodeCallback.5966
- _audioSession_audioDecoderDecodeFrame.5953
- _audioSession_estimateRenderDeadline
- _audioSession_handleMediaDataControlRequest.3671
- _audioSession_handleMediaDataControlRequest.5843
- _audioSession_log.5978
- _audioSession_networkThread.5988
- _audioSession_performPeriodicTasks.5983
- _audioSession_retransmitsUpdate
- _audioSession_sessionLock.5880
- _audioSession_sessionUnlock.5882
- _audioSession_trackDups
- _audioSession_trackLosses
- _gAirTunesRelativeTimeOffset.6009
- _gHoseRegistrarCallbacks
- _kAPAdvertiserP2PConfig_AllowFullNANAdvertising
- _kAPAdvertiserP2PConfig_AllowPartialNANAdvertising
- _kAPRRemoteControlSessionMediaRemoteVTable.3265
- _kAPRRemoteControlSessionMediaRemote_Class.3281
- _kAPRRemoteControlSessionSession_BaseClassWrapper.3294
- _kAPReceiverAudioSessionOption_EncryptionKey
- _kAPTransportConnectionOption_UseQUIC
- _ntpClientLegacy_ClearLocalPeerInfo
- _sessionManager_handleSenderSessionStateChange
- _strnlen
CStrings:
+ "\n %-*s: soloSourceNearby=%s, enforceSoloAdvertising=%s"
+ "\n %-*s: started=%-3s, requested=%-3s, blocked=%-3s, allow=%-3s"
+ " allowOpenFullNANAdvertising=%s"
+ " allowOpenPartialNANAdvertising=%s"
+ " allowSecurePartialNANAdvertising=%s"
+ "### %@ Error: wrong transport setup, audioConnectionType APAT only works with BufferedNW \n"
+ "### %@ RTCP UDP server socket setup on %##a if:%u failed: %#m\n"
+ "### Cleaning up for reason: %#m\n"
+ "### Finalized APMulticastProbeReceiver!\n"
+ "### [%{ptr}] APAP/APAT only supported for BufferedAudio!\n"
+ "%@ Buffered audio receiver started: localAddr %##a remoteAddr %##a\n"
+ "%@ Created UnbufferedNW connection [%{ptr}]\n"
+ "%@ Created media data control server [%{ptr}]"
+ "%@ Listening for RTP on port %d"
+ "%@ RTCP localAddr=%##a remoteAddr=%##a\n"
+ "%@ Receiving RTP packets from %##a"
+ "%@ [inSession] oldLiveAdaptiveRenderDeadlineMinMs=%lld newLiveAdaptiveRenderDeadlineMinMs=%lld\n"
+ "%@ sender perceived cluster type %u\n"
+ "%C:%@"
+ "%s AVAudioSession %s"
+ "+[AirPlayReceiverPlatform _setMediaAVAudioSessionActiveSync:]"
+ ", bonjour=%s._%s._%s."
+ ", infraAssist=%-3s"
+ "-[AirPlayReceiverMediaRemoteHelper associateNowPlayingSessionWithAudioSession:]_block_invoke"
+ "-[AirPlayReceiverMediaRemoteHelper startNowPlayingSessionWithCompletion:]"
+ "-[AirPlayReceiverMediaRemoteHelper startNowPlayingSessionWithCompletion:]_block_invoke_2"
+ "-[AirPlayReceiverPlatform _setMediaAVAudioSessionActive:]"
+ "-[AirPlayReceiverPlatform _startNowPlayingSessionAsync:]"
+ "-[AirPlayReceiverPlatform _startNowPlayingSessionAsync:]_block_invoke"
+ "-[AirPlayReceiverPlatform _startNowPlayingSessionAsync:]_block_invoke_2"
+ "890.61.4.11.2"
+ "<APUGL> AirPlay Group ID changed: %@ -> %@\n"
+ "<APUGL> Initializing airPlayGroupID to bootUUID %@\n"
+ "<PWDKeyExchange> [%{ptr}] Created PWD key exchange receiver [%{ptr}]%?{end} with protectionBits=0x%x"
+ "@\"APSDeferredTask\""
+ "@32@0:8^{OpaqueAPReceiverSystemInfo={__CFRuntimeBase=QAQ}@iiiiiii^{OpaqueAPAdvertiserInfo}C^{__CFDictionary}C^{__CFBoolean}[6C][16C]^{__CFString}CCC^{__CFString}^{__CFString}CC^{__CFString}CCC^{__CFString}C^{__CFString}^{__CFString}^{__CFString}^{__CFString}CCC^{__CFDictionary}qi^{__CFString}^{__CFString}C^{__CFString}^{__CFString}^{__CFString}CCCCCCCCCCCCii@[64c]*CCC^{__CFString}CiCC[8c]Q^{__CFString}^{__CFString}[8c]C[64c]@Cii@^{__CFString}{CGSize=dd}{CGSize=dd}{CGSize=dd}^{__CFString}^{__CFString}^{__CFString}^{__CFString}iiCCCCCIf^{__CFNumber}^{__CFNumber}CC^{__CFData}@^{OpaqueAPSPowerAssertion}C^{__CFDictionary}^{__CFData}}16@24"
+ "APAC/48000/9.1.6"
+ "APAT_Buffered"
+ "APAdvertiserInfoCreateWithDeviceTXTRecordDataAndDeviceName"
+ "APMulticastProbeReceiver"
+ "APMulticastProbeReceiverCreate"
+ "APReceiverAudioSessionBufferedHose.%{ptr}.tick"
+ "APReceiverAudioSessionRealTimeRTCP"
+ "APReceiverAudioSessionRealTimeSocket"
+ "APReceiverMediaAVAudioSessionActivation"
+ "Activate"
+ "AirPlayMulticastProbeReceiverQueue"
+ "Cannot set AirPlayGroup ID unless UGL server"
+ "ChaCha Cryptor created with shared key\n"
+ "CoordinatedAirPlayVideo"
+ "Created APMulticastProbeReceiver [%{ptr}]\n"
+ "Creating APMulticastProbeReceiver with srcAddr=%##a, grpAddr=%##a\n"
+ "Deactivate"
+ "DisableAudioRendering"
+ "Display protection change detected to lower level, from 0x%x --> 0x%x. Terminating the session [%{ptr}]"
+ "EncryptionReadKey"
+ "EncryptionWriteKey"
+ "EnsurePlatformIsReadyToAcceptAudio"
+ "Failed to bind to configured port=%u with err=%#m, %s\n"
+ "Failed to create dispatch source from recv socket\n"
+ "Failed to create socket with err=%#m, %s\n"
+ "Failed to get IP_RECV_LINK_ADDR_TYPE on socket with error: %s\n"
+ "Failed to join source MC group with error: %#m\n"
+ "Failed to send MC2UC detection status feedback"
+ "Failed to set IP_RECV_LINK_ADDR_TYPE on socket with error: %s\n"
+ "Failed to set SO_REUSEPORT on socket with error: %s\n"
+ "Forward frame user data changed: '%d' -> '%d'\n"
+ "ForwardFrameUserData"
+ "Generated random airPlayPairingIdentity: %@, systemPairingIdentity: %@\n"
+ "Histogram_LiveAdaptiveGlitchDuration"
+ "IP_RECV_LINK_ADDR_TYPE default setting=%d\n"
+ "IP_RECV_LINK_ADDR_TYPE enabled=%d\n"
+ "Is RC-only server: %s\n"
+ "IsSilentPrimary: %d -> %d\n"
+ "MC2UCDetection"
+ "Media AVAudioSessionID changed: %u -> %u\n"
+ "MirroredAudio_LiveAdaptiveLatency"
+ "OSStatus APAdvertiserInfoCopyAirPlayP2PDataWithNANServiceType(APAdvertiserInfoRef, APAdvertiserInfoDeviceIDType, APSNANServiceType, CFDataRef *)"
+ "OSStatus APMulticastProbeReceiverCreate(CFDictionaryRef, const char *, APMulticastProbeReceiverDelegate *, APMulticastProbeReceiverRef *)"
+ "OSStatus APReceiverAudioSessionCreate(APStreamType, sockaddr_ip, sockaddr_ip, uint8_t *, CFDictionaryRef, APReceiverAudioSessionRef *)"
+ "OSStatus APReceiverAudioSessionRealTimeCreate(APReceiverAudioSessionRef, CFStringRef, sockaddr_ip, sockaddr_ip, uint8_t *, CFDictionaryRef, void **)"
+ "OSStatus _APAdvertiserSetAdvertiserInfo(APAdvertiserRef, APAdvertiserInfoRef)"
+ "OSStatus _AirPlayReceiverSessionUpdateMC2UCStatus(CFTypeRef, uint32_t, MC2UCFeatureStatus, int)"
+ "OSStatus _AirPlayReceiverSessionUpdateMC2UCStatus(CFTypeRef, uint32_t, MC2UCFeatureStatus, int)_block_invoke"
+ "OSStatus _EnsurePlatformIsReadyToAcceptAudioIfNeeded(AirPlayReceiverSessionRef, APStreamType, CFDictionaryRef)"
+ "OSStatus _HandleHTTPConnectionInitialize(HTTPConnectionRef, void *)"
+ "OSStatus airplayReqProcessor_reportPerfMetricsIfNeeded(APReceiverRequestProcessorRef)"
+ "OSStatus aprscreen_decryptBuffer(APReceiverScreenSessionRef, uint8_t *, uint32_t *)"
+ "OSStatus audioSession_receiveRTPSocket(APReceiverAudioSessionRealTimeStateRef)"
+ "OSStatus audioSession_setupRealTimeAudio(APReceiverAudioSessionRef, sockaddr_ip, sockaddr_ip, uint8_t *, CFDictionaryRef)"
+ "OSStatus sbufsink_EnqueueFrameWithUserData(APReceiverScreenSinkRef, CMBlockBufferRef, CFDictionaryRef, uint64_t, CFDictionaryRef, Boolean)"
+ "OSStatus sysInfo_copyInfoDictInternal(APReceiverSystemInfoRef, CFArrayRef, CFAllocatorRef, CFDictionaryRef *)_block_invoke"
+ "Open Full NAN"
+ "Open Partial NAN"
+ "PCM/48000/16/9.1.6"
+ "PCM/48000/32f/9.1.6"
+ "PWDCryptor"
+ "ParentGroupLeaderSupportsGroupCohesion"
+ "RASP::ShouldAdjustPresentationByOutputLatency"
+ "Request received from %##a on connection [%{ptr}], Header %zu bytes, Body %zu bytes, ID 0x%04llX%?{end}, queryReason=%.*s"
+ "Screen session %{ptr}: accepted connection from %##a on %##a\n"
+ "Secure Partial NAN"
+ "Session: [%{ptr}], currentMainMediaSession: [%{ptr}], shouldHandleMRCommands? %s\n"
+ "ShouldAdjustPresentationByOutputLatency"
+ "Started NowPlayingSession for [%{ptr}] with err: %#m"
+ "Starting NowPlayingSession for [%{ptr}] asynchronously"
+ "Starting NowPlayingSession synchronously"
+ "Systems Available: WiFi=%-3s AWDL=%-3s\n"
+ "UGL-RCServer Info changed: %d -> %d\n"
+ "UGL-RCServer Info cleared\n"
+ "UGL-RCServer Info provided to info dict: [%{ptr}]\n"
+ "UGLRCServerMode"
+ "Update Open Full NAN link status: %d"
+ "Update Open Partial NAN link status: %d"
+ "Update Secure Partial NAN link status: %d"
+ "UseUDP"
+ "X-Apple-QR"
+ "[%{ptr} '%@'] accepted connection from %##a on %##a\n"
+ "[%{ptr}] APReceiverAudioSession [%{ptr}] created with stream ID %llu.\n"
+ "[%{ptr}] APReceiverAudioSession [%{ptr}] with stream ID %llu removed.\n"
+ "[%{ptr}] Activation from %##a %s, duration: %llu ms (pair-setup: %llu ms (%llu calls), pair-verify: %llu ms (%llu calls), add session: %llu ms (nowPlayingSession: %llu ms), start clock: %llu ms), overall duration: %llu ms%?{end}, err: %#m\n"
+ "[%{ptr}] Associating AudioSessionID %u\n"
+ "[%{ptr}] Connection [%{ptr}] %s UI controller [%{ptr}]"
+ "[%{ptr}] Copying AirPlayP2PData\n"
+ "[%{ptr}] Correlation ID changed from %@ to %@\n"
+ "[%{ptr}] CorrelationID requested. Available: %s\n"
+ "[%{ptr}] Created media data control server [%{ptr}]"
+ "[%{ptr}] Created multicastProbeReceiver [%{ptr}]"
+ "[%{ptr}] Created session [%{ptr}] (RO=%d TS=%d PC=%c SAI=%d TP=%@ SC=%s)\n"
+ "[%{ptr}] Failed to decrypt probing msg\n"
+ "[%{ptr}] Failed to send MC2UC detection status feedback\n"
+ "[%{ptr}] Failed to set AudioSessionID %u for playerPath %@: %#m\n"
+ "[%{ptr}] Finished setting AudioSessionID %u for playerPath %@\n"
+ "[%{ptr}] Hijacking active connection and becoming main session, as HT session got media audio setup for clientID %@.\n"
+ "[%{ptr}] Hijacking active connection and becoming main session, as persistent session became media session.\n"
+ "[%{ptr}] MC2UC - Unexpected link address type: %d\n"
+ "[%{ptr}] Non-media audio - skip waiting for platform readiness\n"
+ "[%{ptr}] RC-only server doesn't allow non-RC sessions\n"
+ "[%{ptr}] Received StartNowPlayingSession result from task [%{ptr}]: %#m\n"
+ "[%{ptr}] Received a MC2UC probe packet on a multicast link address\n"
+ "[%{ptr}] Received a MC2UC probe packet on a unicast link address\n"
+ "[%{ptr}] Received a probe packet with probeBurstID=%u and address type=%d\n"
+ "[%{ptr}] Send MC2UC detection status feedback: probeBurstID=%u, mc2ucStatus=%d, packetCount=%d\n"
+ "[%{ptr}] Setting correlation ID %@ on incoming advertiser info\n"
+ "[%{ptr}] Setting correlation ID on advertiser info: %@\n"
+ "[%{ptr}] Setup Completed in %lld ms\n"
+ "[%{ptr}] Setup started\n"
+ "[%{ptr}] Skipping stopping now playing session because playerPath=nil\n"
+ "[%{ptr}] Starting now playing session asynchronously\n"
+ "[%{ptr}] Starting now playing session synchronously\n"
+ "[%{ptr}] Starting video playback, streamID %llu\n"
+ "[%{ptr}] Stopping video playback, streamID %llu\n"
+ "[%{ptr}] TearDown on stream %llu with reason: %#m\n"
+ "[%{ptr}] Unable to create session. No active persistent connection"
+ "[%{ptr}] Unable to create session. No shared persistent clock"
+ "[%{ptr}] Unsupported request denied: %'C for RC-only server\n"
+ "[%{ptr}] Waiting for StartNowPlayingSession result from task [%{ptr}]\n"
+ "[%{ptr}] Waiting for platform to be ready to accept audio from main media session [%{ptr}]\n"
+ "[%{ptr}] created startNowPlayingSessionTask [%{ptr}]"
+ "[%{ptr}] recvmsg() failed with err=%s\n"
+ "^{AirPlayReceiverServerPrivate={__CFRuntimeBase=QAQ}^v@i^{OpaqueAPAdvertiser}CCCCCC@C^{APSWiFiTransactionPrivate}^{HTTPServerPrivate}@^{HTTPServerPrivate}[16C]fCiCC@IQ^{OpaqueAPReceiverSystemInfo}C^{__CFDictionary}^{__CFDictionary}^{__CFDictionary}IiI^{APReceiverSessionManagerOpaque}^{OpaqueFigValeria}^?^{__CFString}CCCCCCCCCCC^{__CFString}S^{__CFString}^{opaqueAPSRTCReportingAgent}}"
+ "^{AirPlayReceiverSessionPrivate={__CFRuntimeBase=QAQ}@^{AirPlayReceiverServerPrivate}^{OpaqueAPReceiverRequestProcessor}^{APReceiverSessionManagerOpaque}^v{?=^v^v^?^?^?^?^?^?}[32c][17c]^{OpaqueAPReceiverStatsCollector}@I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16C]iQ[6C]^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}QIQQ{?=^{_CCCryptor}[16C]}^{?}[16C][16C]C^vCC^{OpaqueAPSNetworkClock}CCC^{HTTPClientPrivate}Iiii^{APPairingServicesPrivate}iIIQQQIQiiC^{__CFDictionary}^{APReceiverAudioSessionPrivate}I^{OpaqueFigValeria}^{OpaqueAPReceiverUIController}I^{OpaqueAPReceiverScreenSession}dCCII^{OpaqueFigPWDKeyExchangeReceiver}C@^{__CFString}CCCCCQ^{__CFDictionary}^{__CFArray}fCICd^{__CFDictionary}^{__CFSet}CCC^{__CFData}^{APMulticastProbeReceiverPrivate}}"
+ "_APAdvertiserGenerateNewCorrelationID"
+ "_APAdvertiserInfoAddAirPlayNANData"
+ "_AirPlayReceiverSessionUpdateMC2UCStatus"
+ "_AirPlayReceiverSessionUpdateMC2UCStatus_block_invoke"
+ "_EnsurePlatformIsReadyToAcceptAudioIfNeeded"
+ "_GenerateUGLServicePassword"
+ "_NotifySessionsSystemInfoChange_block_invoke"
+ "_SetSWVolumeSliderValue"
+ "_handleReadDispatchSource"
+ "_mediaAVAudioSessionActivationQueue"
+ "_setMediaAVAudioSessionActive:"
+ "_setMediaAVAudioSessionActiveSync:"
+ "_startNowPlayingSessionAsync:"
+ "_startNowPlayingSessionTask"
+ "activationErr"
+ "activationMs"
+ "activationRequestHandlingDurationMs"
+ "activationStatus"
+ "airplayReqProcessor_reportPerfMetricsIfNeeded"
+ "allowOpenFullNANAdvertising"
+ "allowOpenPartialNANAdvertising"
+ "allowSecurePartialNANAdvertising"
+ "aprscreen_decryptBuffer"
+ "asynchronously"
+ "audioSessionBufferedHose_copyProtocolDriverDataBBufsCallback"
+ "audioSessionBufferedHose_protocolDriverReceiverAudioDataAvailableCallback"
+ "audioSessionBufferedHose_protocolDriverTickTimerFire"
+ "audioSessionBufferedHose_readyToSendBatchCallback"
+ "audioSessionBufferedHose_receiveDataCallback"
+ "burstID"
+ "cid"
+ "correlationID"
+ "created"
+ "disableAdvertiser"
+ "failed"
+ "failed to allocate packages array"
+ "forwardFrameUserData"
+ "groupEncryptionKey"
+ "groupIPv4Addr"
+ "inCreatePackageFunc is NULL"
+ "interface index=%u\n"
+ "lastControlMessageType"
+ "lastControlMessageTypeCount"
+ "mc2ucDetectionSSMGroupInfo"
+ "mc2ucPktCnt"
+ "mc2ucProbeBurstID"
+ "mc2ucStatus"
+ "mediumLatencyAudioStream"
+ "mediumLatencyPathway"
+ "nanServiceType"
+ "networkClockStartDurationMs"
+ "nowPlayingSessionStartDurationMs"
+ "outPackages is NULL"
+ "pairSetupCount"
+ "pairSetupDurationMs"
+ "pairVerifyCount"
+ "pairVerifyDurationMs"
+ "parallelSetupProcessingEnabled"
+ "protectedMirroring"
+ "protocolDriverAPATTickIntervalMS"
+ "result"
+ "rtcpSignatureFailureCount"
+ "rtpSignatureFailureCount"
+ "sbufsink_EnqueueFrameWithUserData"
+ "sessionManagerAddSessionDurationMs"
+ "setNotCompleted"
+ "setResult:"
+ "shared"
+ "sourceIPv4Addr"
+ "sourceSpecificMulticastPortIPv4 is not set, exit!\n"
+ "startNowPlayingSessionTask"
+ "startNowPlayingSessionWithCompletion:"
+ "streamConnectionTypeAPAT"
+ "succeeded"
+ "supportsCoordinatedAirPlayVideo"
+ "supportsV2ArtworkMetadata"
+ "synchronously"
+ "terminated"
+ "ugl"
+ "uglAssistedDiscovery"
+ "uglServerInfo"
+ "updateMC2UCStatus"
+ "v32@0:8^{AirPlayReceiverSessionPrivate={__CFRuntimeBase=QAQ}@^{AirPlayReceiverServerPrivate}^{OpaqueAPReceiverRequestProcessor}^{APReceiverSessionManagerOpaque}^v{?=^v^v^?^?^?^?^?^?}[32c][17c]^{OpaqueAPReceiverStatsCollector}@I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16C]iQ[6C]^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}QIQQ{?=^{_CCCryptor}[16C]}^{?}[16C][16C]C^vCC^{OpaqueAPSNetworkClock}CCC^{HTTPClientPrivate}Iiii^{APPairingServicesPrivate}iIIQQQIQiiC^{__CFDictionary}^{APReceiverAudioSessionPrivate}I^{OpaqueFigValeria}^{OpaqueAPReceiverUIController}I^{OpaqueAPReceiverScreenSession}dCCII^{OpaqueFigPWDKeyExchangeReceiver}C@^{__CFString}CCCCCQ^{__CFDictionary}^{__CFArray}fCICd^{__CFDictionary}^{__CFSet}CCC^{__CFData}^{APMulticastProbeReceiverPrivate}}16i24i28"
+ "void APReceiverSystemInfoSetParentGroupInfo(APReceiverSystemInfoRef, CFStringRef, Boolean, Boolean, Boolean, CFDictionaryRef)_block_invoke"
+ "void _APAdvertiserUpdateAdvertiserInfoCorrelationID(APAdvertiserRef, CFStringRef)"
+ "void _AirPlayReceiverSessionDisplayProtectionMonitor(AirPlayReceiverSessionRef)"
+ "void _AirPlayReceiverSessionSetupMC2UC(AirPlayReceiverSessionRef, CFDictionaryRef)"
+ "void _Cleanup(APMulticastProbeReceiverRef, OSStatus, int *)"
+ "void _handleReadDispatchSource(SocketRef, APMulticastProbeReceiverRef)"
+ "void audioSession_reportAudioPerformance(APReceiverAudioSessionRealTimeStateRef, Boolean)"
+ "{?=\"mediaAudioSessions\"^{__CFSet}\"mediaVideoSessions\"^{__CFSet}\"screenSessions\"^{__CFSet}\"auxAudioSessions\"^{__CFSet}\"isAmbientAudioActive\"C\"isMediaAudioActive\"C\"isVideoActive\"C\"isScreenActive\"C\"playbackPrevented\"C\"wifiDiagnosticExtension\"@\"DEExtension\"\"wifiDECaptureUUID\"@\"NSString\"\"stalledSessionCount\"Q\"activeNANLinkRetainCount\"I\"volumeSliderValue\"f\"isMuted\"C\"isHandlingMRCommands\"C\"receiverSessionCount\"Q\"mediaAVAudioSessionID\"I\"nowPlaying\"(?=\"singlePrimary\"{?=\"isAirPlayReceiverMRNowPlayingApp\"C}\"multiPrimaries\"{?=\"nowPlayingSessionStarted\"C\"mainMediaReceiverSession\"^{OpaqueAPReceiverRequestProcessor}})}"
- "\n %-13s: soloSourceNearby=%s, enforceSoloAdvertising=%s"
- "\n %-13s: started=%-3s, allow=%-3s"
- "\n %-13s: started=%-3s, allow=%-3s, bonjour=%s._%s._%s."
- "\n %-13s: started=%-3s, allow=%-3s, infraAssist=%-3s"
- " allowFullNANAdvertising=%s"
- " allowPartialNANAdvertising=%s"
- "### Setting media AVAudioSession to [%s] failed with error %@\n"
- "### [%{ptr}] APAP only supported for BufferedAudio!\n"
- "### [%{ptr}] Failed to set AudioSessionID for playerPath: %@\n"
- "%@ Enqueued ts=%u with redundant packet %u[%u]\n"
- "%@ RFC2198Payload seq=%u ts=%u pt=%u tso=%u level=%u\n"
- "%@ RTCP portLocal=%d remoteAddr=%##a\n"
- "%@ Using future Packet Processor Version."
- "%@ Using future process packet version is %d"
- "-[AirPlayReceiverMediaRemoteHelper associateNowPlayingSessionWithAudioSession:]_block_invoke_2"
- "860.7.1"
- "<PWDKeyExchange> [%{ptr}] Created PWD key exchange receiver [%{ptr}]%?{end} with isProvisionedForHDCP2=%s, protectionBits=0x%llx"
- "@32@0:8^{OpaqueAPReceiverSystemInfo={__CFRuntimeBase=QAQ}@iiiiiii^{OpaqueAPAdvertiserInfo}C^{__CFDictionary}C^{__CFBoolean}[6C][16C]^{__CFString}CCC^{__CFString}^{__CFString}CC^{__CFString}CC^{__CFString}C^{__CFString}^{__CFString}^{__CFString}^{__CFString}CCC^{__CFDictionary}qi^{__CFString}^{__CFString}C^{__CFString}^{__CFString}^{__CFString}CCCCCCCCCii@[64c]*CCC^{__CFString}CiCC[8c]Q^{__CFString}^{__CFString}[8c]C[64c]@Cii@^{__CFString}{CGSize=dd}{CGSize=dd}{CGSize=dd}^{__CFString}^{__CFString}^{__CFString}^{__CFString}iiCCCCIf^{__CFNumber}^{__CFNumber}CC^{__CFData}@^{OpaqueAPSPowerAssertion}C^{__CFData}}16@24"
- "APAdvertiserInfoCopyCFStringFromTXTRecord"
- "APAdvertiserInfoCreateWithRAOPAndAirPlayDataAndDeviceName"
- "APAdvertiserInfoGetBooleanFromTXTRecord"
- "APAdvertiserInfoGetInt64FromTXTRecord"
- "AirPlayPerf_LocalStereoPairClusterPersistentConnection"
- "EncryptionKey"
- "Full NAN"
- "HomePod"
- "JuneBug"
- "OSStatus APAdvertiserInfoCopyAirPlayP2PDataWithNANServiceType(APAdvertiserInfoRef, APSNANServiceType, CFDataRef *)"
- "OSStatus APReceiverAudioSessionCreate(APStreamType, sockaddr_ip, uint8_t *, CFDictionaryRef, APReceiverAudioSessionRef *)"
- "OSStatus APReceiverAudioSessionRealTimeCreate(APReceiverAudioSessionRef, CFStringRef, sockaddr_ip, uint8_t *, CFDictionaryRef, void **)"
- "OSStatus aprscreen_decryptFrameBuf(APReceiverScreenSessionRef, uint8_t *)"
- "OSStatus audioSession_processPacketFuture(APReceiverAudioSessionRealTimeStateRef, APSRTPPassThroughJitterBufferNode *, size_t, Boolean)"
- "OSStatus audioSession_setupRealTimeAudio(APReceiverAudioSessionRef, sockaddr_ip, uint8_t *, CFDictionaryRef)"
- "OSStatus sbufsink_EnqueueFrame(APReceiverScreenSinkRef, CMBlockBufferRef, uint64_t, CFDictionaryRef, Boolean)"
- "Overriding allowOpenNANAdvertising to true based on prefs\n"
- "Partial NAN"
- "Request received from %##a on connection [%{ptr}], Header %zu bytes, Body %zu bytes, ID 0x%04llX\n"
- "Screen session %{ptr}: accepted connection from %##a\n"
- "Set media AVAudioSession to [%s]\n"
- "Update Full NAN link status: %d"
- "Update Partial NAN link status: %d"
- "[%{ptr} '%@'] accepted connection from %##a.\n"
- "[%{ptr}] APReceiverAudioSession [%{ptr}] created with stream ID %@.\n"
- "[%{ptr}] APReceiverAudioSession [%{ptr}] with stream ID %@ removed.\n"
- "[%{ptr}] Associating AudioSessionID\n"
- "[%{ptr}] Created session [%{ptr}] (RO=%d TS=%d PC=%c SAI=%d TP=%@)\n"
- "[%{ptr}] Finished setting AudioSessionID for playerPath\n"
- "[%{ptr}] Got HT audio setup %d for clientID %@, setting HT session as main and hijacking active connection\n"
- "[%{ptr}] Setup\n"
- "[%{ptr}] Starting now playing session\n"
- "[%{ptr}] Starting video playback, streamID %@\n"
- "[%{ptr}] Stopping video playback, streamID %@\n"
- "[%{ptr}] TearDown on stream %@ with reason: %#m\n"
- "^{AirPlayReceiverServerPrivate={__CFRuntimeBase=QAQ}^v@i^{OpaqueAPAdvertiser}CCCCC@C^{APSWiFiTransactionPrivate}^{HTTPServerPrivate}@^{HTTPServerPrivate}[16C]fCiCC@IQ^{OpaqueAPReceiverSystemInfo}C^{__CFDictionary}^{__CFDictionary}^{__CFDictionary}IiI^{APReceiverSessionManagerOpaque}^{OpaqueFigValeria}^?^{__CFString}CCCCCCCC^{__CFString}S}"
- "^{AirPlayReceiverSessionPrivate={__CFRuntimeBase=QAQ}@^{AirPlayReceiverServerPrivate}^{OpaqueAPReceiverRequestProcessor}^{APReceiverSessionManagerOpaque}^v{?=^v^v^?^?^?^?^?^?}[32c][17c]^{OpaqueAPReceiverStatsCollector}@I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16C]iQ[6C]^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}QIQQ{?=^{_CCCryptor}[16C]}^{?}[16C][16C]C^vCC^{OpaqueAPSNetworkClock}CCC^{HTTPClientPrivate}Iiii^{APPairingServicesPrivate}iIIQQQIQiiC^{__CFDictionary}^{APReceiverAudioSessionPrivate}I^{OpaqueFigValeria}^{OpaqueAPReceiverUIController}I^{OpaqueAPReceiverScreenSession}dCCI^{OpaqueFigPWDKeyExchangeReceiver}^{__CFString}CCCCCQ^{__CFDictionary}^{__CFArray}fCICd^{__CFDictionary}^{__CFSet}CCC^{__CFData}C}"
- "_NotifySessionsSystemInfoChange"
- "_SetVolumeSliderValue"
- "allowFullNANAdvertising"
- "allowOpenNANAdvertising"
- "allowPartialNANAdvertising"
- "aprscreen_decryptFrameBuf"
- "audioSession_processPacketFuture"
- "isProvisionedForHDCP2"
- "protectionBits"
- "realTimeReceiver_UseFutureProcessPacket"
- "sbufsink_EnqueueFrame"
- "txt"
- "v32@0:8^{AirPlayReceiverSessionPrivate={__CFRuntimeBase=QAQ}@^{AirPlayReceiverServerPrivate}^{OpaqueAPReceiverRequestProcessor}^{APReceiverSessionManagerOpaque}^v{?=^v^v^?^?^?^?^?^?}[32c][17c]^{OpaqueAPReceiverStatsCollector}@I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16C]iQ[6C]^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}QIQQ{?=^{_CCCryptor}[16C]}^{?}[16C][16C]C^vCC^{OpaqueAPSNetworkClock}CCC^{HTTPClientPrivate}Iiii^{APPairingServicesPrivate}iIIQQQIQiiC^{__CFDictionary}^{APReceiverAudioSessionPrivate}I^{OpaqueFigValeria}^{OpaqueAPReceiverUIController}I^{OpaqueAPReceiverScreenSession}dCCI^{OpaqueFigPWDKeyExchangeReceiver}^{__CFString}CCCCCQ^{__CFDictionary}^{__CFArray}fCICd^{__CFDictionary}^{__CFSet}CCC^{__CFData}C}16i24i28"
- "void APReceiverSystemInfoSetParentGroupInfo(APReceiverSystemInfoRef, CFStringRef, Boolean, Boolean)_block_invoke"
- "void _DetermineP2PSettings(AirPlayReceiverServerRef)"
- "void audioSession_reportAudioPerformance(APReceiverAudioSessionRealTimeStateRef)"
- "{?=\"mediaAudioSessions\"^{__CFSet}\"mediaVideoSessions\"^{__CFSet}\"screenSessions\"^{__CFSet}\"auxAudioSessions\"^{__CFSet}\"isAmbientAudioActive\"C\"isMediaAudioActive\"C\"isVideoActive\"C\"isScreenActive\"C\"playbackPrevented\"C\"wifiDiagnosticExtension\"@\"DEExtension\"\"wifiDECaptureUUID\"@\"NSString\"\"stalledSessionCount\"Q\"activeNANLinkRetainCount\"I\"volumeSliderValue\"f\"isMuted\"C\"isHandlingMRCommands\"C\"receiverSessionCount\"Q\"nowPlaying\"(?=\"singlePrimary\"{?=\"isAirPlayReceiverMRNowPlayingApp\"C}\"multiPrimaries\"{?=\"nowPlayingSessionStarted\"C\"mainMediaReceiverSession\"^{OpaqueAPReceiverRequestProcessor}})}"

```
