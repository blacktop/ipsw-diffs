## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2145.45.1.11.2
-  __TEXT.__text: 0x788650
-  __TEXT.__auth_stubs: 0x5600
-  __TEXT.__objc_methlist: 0x354f0
-  __TEXT.__const: 0xc720
-  __TEXT.__cstring: 0x8dd7a
-  __TEXT.__oslogstring: 0x10c331
-  __TEXT.__gcc_except_tab: 0x2a04
+2145.50.1.0.0
+  __TEXT.__text: 0x78bd88
+  __TEXT.__auth_stubs: 0x55f0
+  __TEXT.__objc_methlist: 0x356d0
+  __TEXT.__const: 0xc730
+  __TEXT.__cstring: 0x8e250
+  __TEXT.__oslogstring: 0x10ca8f
+  __TEXT.__gcc_except_tab: 0x2a80
   __TEXT.__ustring: 0x1a8
-  __TEXT.__unwind_info: 0x10650
-  __TEXT.__objc_classname: 0x4e7d
-  __TEXT.__objc_methname: 0x7cc40
-  __TEXT.__objc_methtype: 0x28058
-  __TEXT.__objc_stubs: 0x4e2c0
-  __DATA_CONST.__got: 0x1a38
-  __DATA_CONST.__const: 0x6918
-  __DATA_CONST.__objc_classlist: 0x12d8
+  __TEXT.__unwind_info: 0x106a8
+  __TEXT.__objc_classname: 0x4eb2
+  __TEXT.__objc_methname: 0x7d10d
+  __TEXT.__objc_methtype: 0x2816a
+  __TEXT.__objc_stubs: 0x4e640
+  __DATA_CONST.__got: 0x1a40
+  __DATA_CONST.__const: 0x69b8
+  __DATA_CONST.__objc_classlist: 0x12e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16700
+  __DATA_CONST.__objc_selrefs: 0x167e0
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x10d8
+  __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x2628
-  __AUTH_CONST.__auth_got: 0x2b18
-  __AUTH_CONST.__const: 0x3b48
-  __AUTH_CONST.__cfstring: 0x25bc0
-  __AUTH_CONST.__objc_const: 0x62ba0
-  __AUTH_CONST.__objc_intobj: 0x4908
+  __AUTH_CONST.__auth_got: 0x2b10
+  __AUTH_CONST.__const: 0x3bc8
+  __AUTH_CONST.__cfstring: 0x25e00
+  __AUTH_CONST.__objc_const: 0x62f68
+  __AUTH_CONST.__objc_intobj: 0x4968
   __AUTH_CONST.__objc_arrayobj: 0x1b30
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2f8
-  __AUTH.__objc_data: 0x12c0
-  __DATA.__objc_ivar: 0x6b98
-  __DATA.__data: 0x7868
-  __DATA.__bss: 0xd48
+  __AUTH.__objc_data: 0x1360
+  __DATA.__objc_ivar: 0x6bd8
+  __DATA.__data: 0x7870
+  __DATA.__bss: 0xd80
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0xa9b0
-  __DATA_DIRTY.__data: 0x180
+  __DATA_DIRTY.__data: 0x160
   __DATA_DIRTY.__bss: 0x3f8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/TimeSync.framework/TimeSync
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing
+  - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager
   - /usr/lib/libCTGreenTeaLogger.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EF42EB9F-649C-3EB4-B785-34B262B4D552
-  Functions: 31383
-  Symbols:   96784
-  CStrings:  56733
+  UUID: E06201C6-A294-3DD4-8883-ED8FB0B5766A
+  Functions: 31444
+  Symbols:   96993
+  CStrings:  56855
 
Symbols:
+ +[AVConferenceXPCServer(XPCManagement) entitlementStatusForToken:]
+ +[AVConferenceXPCServer(XPCManagement) entitlementStatusForToken:].cold.1
+ +[AVConferenceXPCServer(XPCManagement) entitlementStatusForToken:].cold.2
+ +[LogDumpUtility newLogDumpListSortedByTimestamp:]
+ +[VCMediaStreamManager allowablePublicAPINames]
+ +[VCMediaStreamManager allowablePublicAPINames].cold.1
+ +[VCRemoteVideoManager allowablePublicAPINames]
+ +[VCRemoteVideoManager allowablePublicAPINames].cold.1
+ +[VCStreamInputManager allowablePublicAPINames]
+ +[VCStreamInputManager allowablePublicAPINames].cold.1
+ -[AVConferenceXPCServer registerBlockForService:block:queue:eventLogLevel:authorizationBlock:allowablePublicAPIs:]
+ -[VCAudioStreamReceiveGroup initWithConfig:].cold.2
+ -[VCAudioStreamReceiveGroup preferredOverlayToken]
+ -[VCConnectionTimeBooster audioCaptions]
+ -[VCConnectionTimeBooster captions:didChangeSourceLocale:]
+ -[VCConnectionTimeBooster captions:didProduceLanguageHypothesis:streamToken:]
+ -[VCConnectionTimeBooster captions:didStopLanguageDetectorWithError:streamToken:]
+ -[VCConnectionTimeBooster dealloc]
+ -[VCConnectionTimeBooster didConfigureCaptionsWithError:]
+ -[VCConnectionTimeBooster didDisableCaptions:error:]
+ -[VCConnectionTimeBooster didEnableCaptions:error:]
+ -[VCConnectionTimeBooster didStartCaptioningWithReason:streamToken:]
+ -[VCConnectionTimeBooster didStopCaptioningWithReason:streamToken:]
+ -[VCConnectionTimeBooster didUpdateCaptions:]
+ -[VCConnectionTimeBooster init]
+ -[VCConnectionTimeBooster init].cold.1
+ -[VCConnectionTimeBooster init].cold.2
+ -[VCConnectionTimeBooster init].cold.3
+ -[VCConnectionTimeBooster initiateBoost]
+ -[VCConnectionTimeBooster setAudioCaptions:]
+ -[VCConnectionTimeBooster setUpAudioCaptionsSpeechRecognizer]
+ -[VCMediaStream cleanUpWiFiChannelSequenceMonitor]
+ -[VCMediaStream setUpWiFiChannelSequenceMonitor]
+ -[VCMediaStream setWifiChannelSequenceMonitor:]
+ -[VCMediaStream wifiChannelSequenceMonitor]
+ -[VCRedundancyControlAlgorithmVideo checkAndEnablePersonaBDATv2RedundancyWithStats:]
+ -[VCSessionParticipant configureFECFeedbackVersionAndGenerator:withStreamGroupID:]
+ -[VCWiFiChannelSequenceMonitor activate]
+ -[VCWiFiChannelSequenceMonitor activate].cold.1
+ -[VCWiFiChannelSequenceMonitor awdlStateMonitor]
+ -[VCWiFiChannelSequenceMonitor copyAWDLChannelSequence:twoPtFourGHzChannelCount:fiveGHzChannelCount:dfsChannelCount:inactiveSlotCount:]
+ -[VCWiFiChannelSequenceMonitor currentChannelSequence]
+ -[VCWiFiChannelSequenceMonitor dealloc]
+ -[VCWiFiChannelSequenceMonitor dealloc].cold.1
+ -[VCWiFiChannelSequenceMonitor init]
+ -[VCWiFiChannelSequenceMonitor invalidate]
+ -[VCWiFiChannelSequenceMonitor invalidate].cold.1
+ -[VCWiFiChannelSequenceMonitor processNewChannelSequence:]
+ -[VCWiFiChannelSequenceMonitor processNewChannelSequence:].cold.1
+ -[VCWiFiChannelSequenceMonitor setAwdlStateMonitor:]
+ -[VCWiFiChannelSequenceMonitor setCurrentChannelSequence:]
+ -[VCWiFiChannelSequenceMonitor setState:]
+ -[VCWiFiChannelSequenceMonitor setStateLock:]
+ -[VCWiFiChannelSequenceMonitor stateLock]
+ -[VCWiFiChannelSequenceMonitor state]
+ -[VCXPCServerUser authorizationBlock]
+ -[VCXPCServerUser setAuthorizationBlock:]
+ GCC_except_table52
+ GCC_except_table76
+ _OBJC_CLASS_$_VCConnectionTimeBooster
+ _OBJC_CLASS_$_VCWiFiChannelSequenceMonitor
+ _OBJC_CLASS_$_WiFiP2PAWDLStateMonitor
+ _OBJC_IVAR_$_AVCStatisticsCollector._shouldUseStatisticsForBWE
+ _OBJC_IVAR_$_VCAVFoundationCapture._deviceSupportsTrueDepthSwitchForEffects
+ _OBJC_IVAR_$_VCAudioStreamReceiveGroup._currentOverlayToken
+ _OBJC_IVAR_$_VCAudioStreamReceiveGroup._syncGroupIdToOverlayTokenMap
+ _OBJC_IVAR_$_VCAudioTransmitter._mainPayloadBytesPerBundle
+ _OBJC_IVAR_$_VCConnectionTimeBooster._audioCaptions
+ _OBJC_IVAR_$_VCConnectionTimeBooster._dispatchQueue
+ _OBJC_IVAR_$_VCMediaStream._wifiChannelSequenceMonitor
+ _OBJC_IVAR_$_VCRateControlBandwidthEstimator._lastPacketInProbingSequenceSendTime
+ _OBJC_IVAR_$_VCRateControlBandwidthEstimator._referencePacketSendTime
+ _OBJC_IVAR_$_VCRedundancyControlAlgorithmVideo._redundancyThresholdForBDATv2
+ _OBJC_IVAR_$_VCSession._connectionTimeBooster
+ _OBJC_IVAR_$_VCSessionParticipantRemote._streamIDMLEnhanceState
+ _OBJC_IVAR_$_VCWiFiChannelSequenceMonitor._awdlStateMonitor
+ _OBJC_IVAR_$_VCWiFiChannelSequenceMonitor._currentChannelSequence
+ _OBJC_IVAR_$_VCWiFiChannelSequenceMonitor._state
+ _OBJC_IVAR_$_VCWiFiChannelSequenceMonitor._stateLock
+ _OBJC_IVAR_$_VCXPCServerUser._authorizationBlock
+ _OBJC_METACLASS_$_VCConnectionTimeBooster
+ _OBJC_METACLASS_$_VCWiFiChannelSequenceMonitor
+ _RTCPSetEnableReceptionFromMultipleSSRC
+ _SRTPUpdateRTCPReceiveSSRCAndDeriveNewKeys
+ _VCConnectionIDS_IsP2PEncryptionSupported
+ _VCConnectionIDS_IsP2PEncryptionSupported.cold.1
+ _VCDatagramChannelIDS_Token.cold.1
+ _VCDatagramChannelIDS_Token.lastReportedTime
+ _VCDatagramChannelIDS_Token.nilInstanceCounter
+ _VCImageQueue_EnqueueFrame.cold.2
+ _VCImageQueue_EnqueueFrame.cold.3
+ _VCImageQueue_EnqueueFrame.cold.4
+ _VCImageQueue_EnqueueFrame.cold.5
+ _VCImageQueue_EnqueueFrame.cold.6
+ _VCImageQueue_EnqueueFrame.cold.7
+ _VCImageQueue_EnqueueFrame.cold.8
+ _VCImageQueue_EnqueueFrame.cold.9
+ _VCPCompressionSessionCompleteFrames
+ _VCRateControlAlgorithmBase_IsPeriodicLogOrLogDumpEnabled
+ _VCRateControlBandwidthEstimator_CalculateBandwidthEstimationWithSendTime
+ _VCRateControlBandwidthEstimator_CalculateBandwidthEstimationWithSendTime.cold.1
+ _VCRedundancyPLRThresholdForBDATv2
+ _VideoUtil_CreateBufferPoolForFrameAttributes
+ _VideoUtil_CreateDeserializedHEVCParameterSetsFromInputBuffer
+ __OBJC_$_CLASS_METHODS_AVConferenceXPCServer(XPCManagement)
+ __OBJC_$_CLASS_METHODS_VCRemoteVideoManager
+ __OBJC_$_INSTANCE_METHODS_VCConnectionTimeBooster
+ __OBJC_$_INSTANCE_METHODS_VCWiFiChannelSequenceMonitor
+ __OBJC_$_INSTANCE_VARIABLES_VCConnectionTimeBooster
+ __OBJC_$_INSTANCE_VARIABLES_VCWiFiChannelSequenceMonitor
+ __OBJC_$_PROP_LIST_VCConnectionTimeBooster
+ __OBJC_$_PROP_LIST_VCWiFiChannelSequenceMonitor
+ __OBJC_CLASS_PROTOCOLS_$_VCConnectionTimeBooster
+ __OBJC_CLASS_RO_$_VCConnectionTimeBooster
+ __OBJC_CLASS_RO_$_VCWiFiChannelSequenceMonitor
+ __OBJC_METACLASS_RO_$_VCConnectionTimeBooster
+ __OBJC_METACLASS_RO_$_VCWiFiChannelSequenceMonitor
+ __SRTPUpdateEncryptionInfo
+ __VideoReceiver_ReportDegradedEvent
+ ___114-[AVConferenceXPCServer registerBlockForService:block:queue:eventLogLevel:authorizationBlock:allowablePublicAPIs:]_block_invoke
+ ___28-[VCSession dispatchedStart]_block_invoke.603
+ ___34-[VCAudioCaptions enableCaptions:]_block_invoke.63
+ ___34-[VCAudioCaptions enableCaptions:]_block_invoke.66
+ ___35-[VCAudioCaptions setSourceLocale:]_block_invoke.85
+ ___40-[VCConnectionTimeBooster initiateBoost]_block_invoke
+ ___40-[VCWiFiChannelSequenceMonitor activate]_block_invoke
+ ___45-[VCAudioCaptions stopWithCompletionHandler:]_block_invoke.104
+ ___47+[VCMediaStreamManager allowablePublicAPINames]_block_invoke
+ ___47+[VCRemoteVideoManager allowablePublicAPINames]_block_invoke
+ ___47+[VCStreamInputManager allowablePublicAPINames]_block_invoke
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke.192
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.193
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.193.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.222
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.225
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.225.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.225.cold.2
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.228
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.242
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.242.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.242.cold.2
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.242.cold.3
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.242.cold.4
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.270
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.284
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.284.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.284.cold.2
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.292
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.292.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.292.cold.2
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.297
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.328
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.328.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.343
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.354.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.361
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.361.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.368
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.368.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.375
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.375.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.382
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.382.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.389
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.389.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.396
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.396.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.403
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.414
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.425
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.427
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.429
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.435
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.301
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.320
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.347
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.347.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.410
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.410.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.421
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.421.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.433
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.305
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.305.cold.1
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.322
+ ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.322.cold.1
+ ___48-[VCRemoteVideoManager registerBlocksForService]_block_invoke.179
+ ___48-[VCRemoteVideoManager registerBlocksForService]_block_invoke.187
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.594
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.598
+ ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke_2.599
+ ___49-[VCSession vcSessionParticipantDidStopReacting:]_block_invoke.282
+ ___50+[LogDumpUtility newLogDumpListSortedByTimestamp:]_block_invoke
+ ___50-[VCAudioStreamReceiveGroup preferredOverlayToken]_block_invoke
+ ___50-[VCSession dispatchedParticipant:didStart:error:]_block_invoke.615
+ ___51-[VCMediaStreamSendGroup updateActiveStreamsCount:]_block_invoke.70
+ ___51-[VCRemoteVideoManager releaseQueueForStreamToken:]_block_invoke.98
+ ___51-[VCSession vcSessionParticipant:reactionDidStart:]_block_invoke.277
+ ___53-[VCSession dispatchedStopWithError:didRemoteCancel:]_block_invoke.614
+ ___63-[VCSession vcSessionParticipant:audioPaused:didSucceed:error:]_block_invoke.231
+ ___63-[VCSession vcSessionParticipant:videoPaused:didSucceed:error:]_block_invoke.241
+ ___64-[VCSession vcSessionParticipant:audioEnabled:didSucceed:error:]_block_invoke.203
+ ___64-[VCSession vcSessionParticipant:videoEnabled:didSucceed:error:]_block_invoke.213
+ ___65-[VCSession vcSessionParticipant:screenEnabled:didSucceed:error:]_block_invoke.218
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.219.cold.1
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.219.cold.2
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.219.cold.3
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.219.cold.4
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.220
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.227
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.229
+ ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke_2.221
+ ___69-[VCSession rateController:targetBitrateDidChange:rateChangeCounter:]_block_invoke.290
+ ___69-[VCSession updateParticipantConfigurations:sessionPresentationInfo:]_block_invoke.346
+ ___71-[VCAudioStreamReceiveGroup vcMediaStream:remoteMediaStalled:duration:]_block_invoke.20
+ ___71-[VCAudioStreamReceiveGroup vcMediaStream:remoteMediaStalled:duration:]_block_invoke.23
+ ___83-[VCSession vcSessionParticipant:mediaMixingDidChangeForMediaType:mixingMediaType:]_block_invoke.267
+ ___84-[VCSession vcSessionParticipant:mediaStateDidChange:forMediaType:didSucceed:error:]_block_invoke.266
+ ___block_descriptor_32_e39_B64?0"NSDictionary"8{?=[8I]}16q48^56l
+ ___block_descriptor_32_e449_v28?0i8^v12^{_VTPPacket=d{sockaddr_storage=CC[6c]q[112c]}I{tagIPPORT=i[16c](?=I[16C])S}{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBBI}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}}20l
+ ___block_descriptor_40_e8_32o_e400_v56?0"NSObject<OS_dispatch_data>"8"NSObject<OS_nw_content_context>"16^{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBBI}24Q32Q40Q48ls32l8
+ ___block_descriptor_40_e8_32r_e35_v32?0"NSNumber"8"NSNumber"16^B24lr32l8
+ ___block_descriptor_41_e8_32b_e39_B64?0"NSDictionary"8{?=[8I]}16q48^56ls32l8
+ ___block_descriptor_64_e8_32o40o_e400_v56?0"NSObject<OS_dispatch_data>"8"NSObject<OS_nw_content_context>"16^{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBBI}24Q32Q40Q48ls32l8s40l8
+ ___block_descriptor_72_e8_32o40o48o56o64b_e5_v8?0ls64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32o40o48r_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8r48l8
+ ___block_descriptor_tmp.240
+ ___block_descriptor_tmp.281
+ ___block_descriptor_tmp.293
+ ___block_literal_global.184
+ ___block_literal_global.2
+ ___block_literal_global.233
+ ___block_literal_global.273
+ ___block_literal_global.299
+ ___block_literal_global.303
+ ___block_literal_global.330
+ ___block_literal_global.384
+ ___block_literal_global.391
+ ___block_literal_global.398
+ ___block_literal_global.404
+ ___block_literal_global.405
+ ___block_literal_global.412
+ ___block_literal_global.416
+ ___block_literal_global.423
+ ___block_literal_global.431
+ ___block_literal_global.74
+ ___block_literal_global.80
+ _allowablePublicAPINames._allowableAPIs
+ _allowablePublicAPINames.onceToken
+ _objc_msgSend$allowablePublicAPINames
+ _objc_msgSend$audioCaptions
+ _objc_msgSend$authorizationBlock
+ _objc_msgSend$awdlStateMonitor
+ _objc_msgSend$beginMonitoring
+ _objc_msgSend$channelNumber
+ _objc_msgSend$checkAndEnablePersonaBDATv2RedundancyWithStats:
+ _objc_msgSend$cleanUpWiFiChannelSequenceMonitor
+ _objc_msgSend$configureFECFeedbackVersionAndGenerator:withStreamGroupID:
+ _objc_msgSend$copyAWDLChannelSequence:twoPtFourGHzChannelCount:fiveGHzChannelCount:dfsChannelCount:inactiveSlotCount:
+ _objc_msgSend$currentChannelSequence
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$endMonitoring
+ _objc_msgSend$entitlementStatusForToken:
+ _objc_msgSend$initiateBoost
+ _objc_msgSend$is2_4GHz
+ _objc_msgSend$is5GHz
+ _objc_msgSend$isDFS
+ _objc_msgSend$isRemoteDuplicating
+ _objc_msgSend$newLogDumpListSortedByTimestamp:
+ _objc_msgSend$preferredOverlayToken
+ _objc_msgSend$processNewChannelSequence:
+ _objc_msgSend$registerBlockForService:block:queue:eventLogLevel:authorizationBlock:allowablePublicAPIs:
+ _objc_msgSend$setAudioCaptions:
+ _objc_msgSend$setAuthorizationBlock:
+ _objc_msgSend$setAwdlStateMonitor:
+ _objc_msgSend$setChannelSequenceUpdatedEventHandler:
+ _objc_msgSend$setCurrentChannelSequence:
+ _objc_msgSend$setUpAudioCaptionsSpeechRecognizer
+ _objc_msgSend$setUpWiFiChannelSequenceMonitor
+ _objc_msgSend$setUseVAD:
+ _objc_msgSend$setWifiChannelSequenceMonitor:
+ _objc_msgSend$wifiChannelSequenceMonitor
- +[LogDumpUtility createLogDumpListSortedByTimestamp:]
- +[VCWiFiUtils copyAWDLChannelSequence:twoPtFourGhzChannelCount:fiveGhzChannelCount:dfsChannelCount:inactiveSlotCount:]
- +[VCWiFiUtils copyAWDLChannelSequence:twoPtFourGhzChannelCount:fiveGhzChannelCount:dfsChannelCount:inactiveSlotCount:isPresent:]
- +[VCWiFiUtils isWiFiPresent]
- -[AVCScreenCapture reportScreenShareIsStarting:]
- -[VCAudioCaptions shouldSetLocale:withError:].cold.1
- -[VCRedundancyControlAlgorithmVideo enableRedundancyForPersona]
- GCC_except_table49
- _CVBufferHasAttachment
- _FigCFDictionarySetAllValuesFromDictionary
- _OBJC_IVAR_$_VCAudioTransmitter._totalEncodedBytesPerBundle
- _OBJC_IVAR_$_VCSessionPresentationInfo._areTilesShowing
- _VCAudioStreamGroup_OverlayToken
- _VCFECFeedbackAnalyzer_GetVPLR.cold.1
- _VideoUtil_DeserializeHEVCParameterSetsFromInputBuffer
- _VideoUtil_NewBufferPoolForFrameAttributes
- __OBJC_$_CLASS_METHODS_AVConferenceXPCServer
- __VCImageQueue_EnqueueDataBuffer
- __VCImageQueue_EnqueueDataBuffer.cold.1
- __VCImageQueue_EnqueueDataBuffer.cold.2
- __VCImageQueue_EnqueueDataBuffer.cold.3
- __VCImageQueue_EnqueueDataBuffer.cold.4
- __VCImageQueue_EnqueueDataBuffer.cold.5
- __VCImageQueue_EnqueueDataBuffer.cold.6
- __VCImageQueue_EnqueueDataBuffer.cold.7
- __VCImageQueue_EnqueueDataBuffer.cold.8
- __VCVideoStream_NotifyVideoStreamDelegate
- ___28-[VCSession dispatchedStart]_block_invoke.601
- ___34-[VCAudioCaptions enableCaptions:]_block_invoke.69
- ___34-[VCAudioCaptions enableCaptions:]_block_invoke.72
- ___35-[VCAudioCaptions setSourceLocale:]_block_invoke.91
- ___45-[VCAudioCaptions stopWithCompletionHandler:]_block_invoke.110
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke.193
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.194
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.194.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.186
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.189
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.189.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.189.cold.2
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.192
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.206
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.206.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.206.cold.2
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.206.cold.3
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.206.cold.4
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.235
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.235.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.235.cold.2
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.243
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.243.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.243.cold.2
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.248
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.263
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.279
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.279.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.294
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.305
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.305.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.312.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.319
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.319.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.326
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.326.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.333
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.333.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.340
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.340.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.347
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.347.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.365
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.376
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.378
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.380
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke.386
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.252
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.271
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.298
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.298.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.361
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.361.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.372
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.372.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_2.384
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.256
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.256.cold.1
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.273
- ___48-[VCMediaStreamManager registerBlocksForService]_block_invoke_3.273.cold.1
- ___48-[VCRemoteVideoManager registerBlocksForService]_block_invoke.167
- ___48-[VCRemoteVideoManager registerBlocksForService]_block_invoke.175
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.593
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke.596
- ___48-[VCSession dispatchedAddParticipantWithConfig:]_block_invoke_2.598
- ___49-[VCSession vcSessionParticipantDidStopReacting:]_block_invoke.281
- ___50-[VCSession dispatchedParticipant:didStart:error:]_block_invoke.611
- ___51-[VCMediaStreamSendGroup updateActiveStreamsCount:]_block_invoke.67
- ___51-[VCRemoteVideoManager releaseQueueForStreamToken:]_block_invoke.86
- ___51-[VCSession vcSessionParticipant:reactionDidStart:]_block_invoke.276
- ___53+[LogDumpUtility createLogDumpListSortedByTimestamp:]_block_invoke
- ___53-[VCSession dispatchedStopWithError:didRemoteCancel:]_block_invoke.610
- ___63-[VCSession vcSessionParticipant:audioPaused:didSucceed:error:]_block_invoke.230
- ___63-[VCSession vcSessionParticipant:videoPaused:didSucceed:error:]_block_invoke.240
- ___64-[VCSession vcSessionParticipant:audioEnabled:didSucceed:error:]_block_invoke.202
- ___64-[VCSession vcSessionParticipant:videoEnabled:didSucceed:error:]_block_invoke.212
- ___65-[VCSession vcSessionParticipant:screenEnabled:didSucceed:error:]_block_invoke.217
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.211
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.211.cold.1
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.211.cold.2
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.211.cold.3
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.211.cold.4
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.212
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke.221
- ___69-[AVConferenceXPCServer(XPCManagement) _xpc_handle_incoming_request:]_block_invoke_2.213
- ___69-[VCSession rateController:targetBitrateDidChange:rateChangeCounter:]_block_invoke.289
- ___69-[VCSession updateParticipantConfigurations:sessionPresentationInfo:]_block_invoke.345
- ___71-[VCAudioStreamReceiveGroup vcMediaStream:remoteMediaStalled:duration:]_block_invoke.12
- ___71-[VCAudioStreamReceiveGroup vcMediaStream:remoteMediaStalled:duration:]_block_invoke.15
- ___83-[VCSession vcSessionParticipant:mediaMixingDidChangeForMediaType:mixingMediaType:]_block_invoke.266
- ___84-[VCSession vcSessionParticipant:mediaStateDidChange:forMediaType:didSucceed:error:]_block_invoke.265
- ___block_descriptor_32_e448_v28?0i8^v12^{_VTPPacket=d{sockaddr_storage=CC[6c]q[112c]}I{tagIPPORT=i[16c](?=I[16C])S}{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBB}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}}20l
- ___block_descriptor_40_e8_32o_e399_v56?0"NSObject<OS_dispatch_data>"8"NSObject<OS_nw_content_context>"16^{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBB}24Q32Q40Q48ls32l8
- ___block_descriptor_64_e8_32o40o_e399_v56?0"NSObject<OS_dispatch_data>"8"NSObject<OS_nw_content_context>"16^{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBB}24Q32Q40Q48ls32l8s40l8
- ___block_descriptor_80_e8_32o40o_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
- ___block_descriptor_tmp.234
- ___block_descriptor_tmp.275
- ___block_descriptor_tmp.287
- ___block_literal_global.172
- ___block_literal_global.250
- ___block_literal_global.265
- ___block_literal_global.300
- ___block_literal_global.328
- ___block_literal_global.335
- ___block_literal_global.367
- ___block_literal_global.374
- ___block_literal_global.382
- ___block_literal_global.403
- ___block_literal_global.56
- _constantkWiFiManagerPropertyInterfaceName
- _init_WiFiManagerCreate
- _init_WiFiManagerCreate.cold.1
- _init_WiFiManagerDoApple80211
- _init_WiFiManagerDoApple80211.cold.1
- _init_WiFiManagerSetProperty
- _init_WiFiManagerSetProperty.cold.1
- _initkWiFiManagerPropertyInterfaceName
- _initkWiFiManagerPropertyInterfaceName.cold.1
- _kWiFiManagerPropertyInterfaceNameFunction
- _objc_msgSend$copyAWDLChannelSequence:twoPtFourGhzChannelCount:fiveGhzChannelCount:dfsChannelCount:inactiveSlotCount:
- _objc_msgSend$copyAWDLChannelSequence:twoPtFourGhzChannelCount:fiveGhzChannelCount:dfsChannelCount:inactiveSlotCount:isPresent:
- _objc_msgSend$createLogDumpListSortedByTimestamp:
- _objc_msgSend$enableRedundancyForPersona
- _objc_msgSend$isWiFiPresent
- _objc_msgSend$reportScreenShareIsStarting:
CStrings:
+ " [%s] %s:%d %@(%p) Already activated"
+ " [%s] %s:%d %@(%p) Already invalidated"
+ " [%s] %s:%d %@(%p) Attempting to overwrite existing locale=%@ with locale=%@"
+ " [%s] %s:%d %@(%p) ChannelSequence update not received"
+ " [%s] %s:%d %@(%p) Failed to allocate overlay token map"
+ " [%s] %s:%d %@(%p) Failed to create VCAudioStreamGroupCommon"
+ " [%s] %s:%d %@(%p) Failed to init queue"
+ " [%s] %s:%d %@(%p) Failed to set up audio captions for connection time boost"
+ " [%s] %s:%d %@(%p) Finalized fecHeader version is %d for streamGroupID=%s"
+ " [%s] %s:%d %@(%p) Not activated"
+ " [%s] %s:%d %@(%p) Not invalidated"
+ " [%s] %s:%d %@(%p) Prewarming captions for a connection time boost."
+ " [%s] %s:%d %@(%p) Set targetBitrate=%d, Max=%d, Min=%d"
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: [%p] TX AFB Update(isFullBleed=%d, lastFrameIsAFB=%d fkeyFrameNow=%d, fIDRNow=%d, data=%@"
+ " [%s] %s:%d @:@ AVCCaptionsClient-didConfigureCaptionsWithError (%p) error=%@"
+ " [%s] %s:%d Already activated"
+ " [%s] %s:%d Already invalidated"
+ " [%s] %s:%d Attempting to overwrite existing locale=%@ with locale=%@"
+ " [%s] %s:%d ChannelSequence update not received"
+ " [%s] %s:%d Checking public access VCMediaStreamConfig. allowedStreamType=%d allowedStreamMode=%d allowedCaptureSource=%d captureSource=%d"
+ " [%s] %s:%d Failed to allocate overlay token map"
+ " [%s] %s:%d Failed to init queue"
+ " [%s] %s:%d Failed to set up audio captions for connection time boost"
+ " [%s] %s:%d Finalized fecHeader version is %d for streamGroupID=%s"
+ " [%s] %s:%d New WiFiChannelSequence=%@"
+ " [%s] %s:%d Not invalidated"
+ " [%s] %s:%d Prewarming captions for a connection time boost."
+ " [%s] %s:%d Set targetBitrate=%d, Max=%d, Min=%d"
+ " [%s] %s:%d [%p] Failed updating the remote SSRC onto the SRTP context. dwSSRC=%u packetSSRC=%u error=(%X)"
+ " [%s] %s:%d nil instance passed counter=%u"
+ " [%s] %s:%d redundancy percentage changed from previousRedundancy=%u to _redundancyPercentage=%u _plrEnvelope=%f currentLossPercentage=%f"
+ " [%s] %s:%d super init failed"
+ "+[AVConferenceXPCServer(XPCManagement) entitlementStatusForToken:]"
+ "+[LogDumpUtility newLogDumpListSortedByTimestamp:]"
+ "-[AVCCaptionsClient didConfigureCaptionsWithError:]"
+ "-[AVConferenceXPCServer registerBlockForService:block:queue:eventLogLevel:authorizationBlock:allowablePublicAPIs:]"
+ "-[VCConnectionTimeBooster init]"
+ "-[VCConnectionTimeBooster initiateBoost]_block_invoke"
+ "-[VCMediaStream setUpWiFiChannelSequenceMonitor]"
+ "-[VCRedundancyControlAlgorithmVideo checkAndEnablePersonaBDATv2RedundancyWithStats:]"
+ "-[VCSessionParticipant configureFECFeedbackVersionAndGenerator:withStreamGroupID:]"
+ "-[VCVideoTransmitterDefault setTargetBitrate:]"
+ "-[VCWiFiChannelSequenceMonitor activate]"
+ "-[VCWiFiChannelSequenceMonitor copyAWDLChannelSequence:twoPtFourGHzChannelCount:fiveGHzChannelCount:dfsChannelCount:inactiveSlotCount:]"
+ "-[VCWiFiChannelSequenceMonitor dealloc]"
+ "-[VCWiFiChannelSequenceMonitor invalidate]"
+ "-[VCWiFiChannelSequenceMonitor processNewChannelSequence:]"
+ "2145.50.1"
+ "@\"VCAudioCaptionsSpeechRecognizer\""
+ "@\"VCConnectionTimeBooster\""
+ "@\"VCWiFiChannelSequenceMonitor\""
+ "@\"WiFiP2PAWDLStateMonitor\""
+ "@32@0:8i16I20C24B28"
+ "@40@0:8^{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}16^{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=@})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBB@I}24^^{tagVCIDSChannelDataFormat}32"
+ "@44@0:8@16i24{VCRedundancyControllerVideoParameters_t=@IBCB}28"
+ "@:@ AVCCaptionsClient-didConfigureCaptionsWithError"
+ "AVConferenceXPCServer [%s] %s:%d API name=%@ failed authorization check error=%@, entitlementStatus=%ld"
+ "AVConferenceXPCServer [%s] %s:%d Failed to create SecTask from audit token"
+ "AVConferenceXPCServer [%s] %s:%d Process %s (PID=%d) encountered error while checking entitlement=%s, ignoring connection"
+ "AVConferenceXPCServer [%s] %s:%d VCXPCServer: error=%@ accessing entitlement=%s"
+ "Aggregate PLR:\t%.2f%%\tEnvelope PLR:\t%.2f%%\n"
+ "B32@0:8^{_VCMediaStreamTransportSetupInfo=C(?={?=ii}{?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}}{?=^v^?BBBi}@)IIB}16^@24"
+ "B64@0:8@16^{_VCMediaStreamTransportSetupInfo=C(?={?=ii}{?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}}{?=^v^?BBBi}@)IIB}24B32B36@40@48^@56"
+ "B64@?0@\"NSDictionary\"8{?=[8I]}16q48^@56"
+ "Bandwidth Estimation: ArrivalTime:%.4f, probingID:%u, isProbing:%d, seq:%u, BWD:%.2f, state:%d, divergeCount:%d, prob_seq:[duration:%.4f, sendDuration:%.4f, send:%.4f, size:%d, count:%d], EstimatedBandwidth:%.2f\n"
+ "Bandwidth Estimation: Bandwidth estimator qualification parameters with RAT=%d, mode=%d. [maxBW=%f, minWin=%f, maxOverRange=%d, minPacketCount=%d]\n"
+ "RTCPSetEnableReceptionFromMultipleSSRC"
+ "SRTPUpdateRTCPReceiveSSRCAndDeriveNewKeys"
+ "T@\"NSArray\",&,V_currentChannelSequence"
+ "T@\"VCAudioCaptionsSpeechRecognizer\",&,N,V_audioCaptions"
+ "T@\"VCWiFiChannelSequenceMonitor\",&,V_wifiChannelSequenceMonitor"
+ "T@\"WiFiP2PAWDLStateMonitor\",&,V_awdlStateMonitor"
+ "T@?,C,N,V_authorizationBlock"
+ "Ti,N,V_redundancyControllerMode"
+ "Ti,N,V_redundancyMode"
+ "Ti,R,N,V_mode"
+ "Tq,V_state"
+ "T{os_unfair_lock_s=I},V_stateLock"
+ "T{tagAVCSessionPresentationInfo={CGRect={CGPoint=dd}{CGSize=dd}}IIC},N"
+ "VCConnectionIDS_IsP2PEncryptionSupported"
+ "VCConnectionTimeBooster"
+ "VCMediaStream [%s] %s:%d %@(%p) Channel sequence has inactive slots %s"
+ "VCMediaStream [%s] %s:%d %@(%p) Failed with result=%x"
+ "VCMediaStream [%s] %s:%d %@(%p) copyAWDLChannelSequence failed, error=%x"
+ "VCMediaStream [%s] %s:%d Failed with result=%x"
+ "VCMediaStream [%s] %s:%d copyAWDLChannelSequence failed, error=%x"
+ "VCRateControlBandwidthEstimator_CalculateBandwidthEstimationWithSendTime"
+ "VCSession [%s] %s:%d %@(%p) Session already stopped. _state=%d, stopError=%p"
+ "VCSession [%s] %s:%d Session already stopped. _state=%d, stopError=%p"
+ "VCVideoStream [%s] %s:%d VCVideoStream[%p] remoteScreenAttributes=%@, cachedRemoteScreenAttributes=%@"
+ "VCVideoStream [%s] %s:%d VCVideoStream[%p] remoteScreenAttributesDidChange=%p, _cachedRemoteScreenAttributes=%@, "
+ "VCWiFiChannelSequenceMonitor"
+ "VTSCDSMAX"
+ "VTSCRSMAX"
+ "VideoUtil_CreateDeserializedHEVCParameterSetsFromInputBuffer"
+ "[512{VCStatisticsStatsHistoryElement=\"linkID\"C\"statsUpdateTime\"d\"statsTimestamp\"I\"totalPacketSent\"I\"totalPacketReceived\"I\"totalByteSent\"Q\"totalByteReceived\"Q\"totalByteServerStatsUsed\"Q\"maxBurstyLoss\"I\"packetSeqNumber\"S}]"
+ "_authorizationBlock"
+ "_awdlStateMonitor"
+ "_connectionTimeBooster"
+ "_currentChannelSequence"
+ "_currentOverlayToken"
+ "_deviceSupportsTrueDepthSwitchForEffects"
+ "_lastPacketInProbingSequenceSendTime"
+ "_mainPayloadBytesPerBundle"
+ "_redundancyThresholdForBDATv2"
+ "_referencePacketSendTime"
+ "_shouldUseStatisticsForBWE"
+ "_streamIDMLEnhanceState"
+ "_syncGroupIdToOverlayTokenMap"
+ "_wifiChannelSequenceMonitor"
+ "allowablePublicAPINames"
+ "audioCaptions"
+ "authorizationBlock"
+ "awdlStateMonitor"
+ "beginMonitoring"
+ "channelNumber"
+ "checkAndEnablePersonaBDATv2RedundancyWithStats:"
+ "cleanUpWiFiChannelSequenceMonitor"
+ "com.apple.AVConference.VCConnectionTimeBooster.connectionTimeBoosterQueue"
+ "configureFECFeedbackVersionAndGenerator:withStreamGroupID:"
+ "copyAWDLChannelSequence:twoPtFourGHzChannelCount:fiveGHzChannelCount:dfsChannelCount:inactiveSlotCount:"
+ "currentChannelSequence"
+ "decodeIntegerForKey:"
+ "displayRect=[%.0f, %.0f, %.0f, %.0f] layout=%u state=%u"
+ "encodeInteger:forKey:"
+ "endMonitoring"
+ "entitlementStatusForToken:"
+ "facetimeconnectionbooster"
+ "forceConnectionTimeBoost"
+ "i28@0:8i16B20B24"
+ "i56@0:8^@16^i24^i32^i40^i48"
+ "initiateBoost"
+ "is2_4GHz"
+ "is5GHz"
+ "isDFS"
+ "newLogDumpListSortedByTimestamp:"
+ "p2pTLE"
+ "preferredOverlayToken"
+ "processNewChannelSequence:"
+ "q48@0:8{?=[8I]}16"
+ "registerBlockForService:block:queue:eventLogLevel:authorizationBlock:allowablePublicAPIs:"
+ "setAudioCaptions:"
+ "setAuthorizationBlock:"
+ "setAwdlStateMonitor:"
+ "setChannelSequenceUpdatedEventHandler:"
+ "setCurrentChannelSequence:"
+ "setStateLock:"
+ "setUpAudioCaptionsSpeechRecognizer"
+ "setUpWiFiChannelSequenceMonitor"
+ "setUseVAD:"
+ "setWifiChannelSequenceMonitor:"
+ "v16@?0^{VCPacket=^{OpaqueCMBlockBuffer}{?=BB[12S]CCBQBB[4Q]{?=iiBQ}Sd(?={?=II[16C]BB}{?=dCBCI})}{?=^{VCPacket}}}8"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v28@?0i8^v12^{_VTPPacket=d{sockaddr_storage=CC[6c]q[112c]}I{tagIPPORT=i[16c](?=I[16C])S}{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=@})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBB@I}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}}20"
+ "v28@?0i8^v12^{_VTPPacket=d{sockaddr_storage=CC[6c]q[112c]}I{tagIPPORT=i[16c](?=I[16C])S}{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=^{nw_connection}})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBB^{nw_protocol_metadata}I}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}}20"
+ "v56@?0@\"NSObject<OS_dispatch_data>\"8@\"NSObject<OS_nw_content_context>\"16^{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=@})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBB@I}24Q32Q40Q48"
+ "v60@0:8r*16@?24@32i40@?44@52"
+ "v64@0:8{tagAVCSessionPresentationInfo={CGRect={CGPoint=dd}{CGSize=dd}}IIC}16"
+ "vc-red-plr-threshold-for-bdatv2"
+ "wifiChannelSequenceMonitor"
+ "{?=\"context\"^v\"creationCallback\"^?\"isReceiveExternallyScheduled\"B\"requiresLargeReceiveBuffer\"B\"isRTCPReceiveFromMultipleSSRCsEnabled\"B\"transportStreamIndex\"i}"
+ "{_VCMediaStreamTransportSetupInfo=\"setupType\"C\"\"(?=\"socketInfo\"{?=\"rtpSocket\"i\"rtcpSocket\"i}\"ipInfo\"{?=\"srcIPPORT\"{tagIPPORT=\"iFlags\"i\"szIfName\"[16c]\"IP\"(?=\"dwIPv4\"I\"abIPv6\"[16C])\"wPort\"S}\"srcRTPIPPort\"{tagIPPORT=\"iFlags\"i\"szIfName\"[16c]\"IP\"(?=\"dwIPv4\"I\"abIPv6\"[16C])\"wPort\"S}}\"transportStreamInfo\"{?=\"context\"^v\"creationCallback\"^?\"isReceiveExternallyScheduled\"B\"requiresLargeReceiveBuffer\"B\"isRTCPReceiveFromMultipleSSRCsEnabled\"B\"transportStreamIndex\"i}\"nwConnection\"@\"NSObject<OS_nw_connection>\")\"sourceRate\"I\"datagramChannelToken\"I\"isSessionIDValid\"B}"
+ "{os_unfair_lock_s=I}16@0:8"
+ "{tagAVCSessionPresentationInfo={CGRect={CGPoint=dd}{CGSize=dd}}IIC}16@0:8"
- " [%s] %s:%d %@(%p) Attempting to overwrite locale=%@"
- " [%s] %s:%d %@(%p) Finalized fecHeader version is %d"
- " [%s] %s:%d /Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: [%p] TX AFB Update(isFullBleed=%d, lastFrameIsAFB=%d fkeyFrameNow=%d, fIDRNow=%d, dict=%@, data=%@"
- " [%s] %s:%d /Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/VCVideoEncoder_VCP.c:%d: [%p] expect no attachment, but attachments=%@"
- " [%s] %s:%d Attempting to overwrite locale=%@"
- " [%s] %s:%d Finalized fecHeader version is %d"
- " [%s] %s:%d [%p] Attachments=%@"
- " [%s] %s:%d redundancy percentage changed from previousRedundancy=%u to _redundancyPercentage=%u"
- "+[LogDumpUtility createLogDumpListSortedByTimestamp:]"
- "-[AVConferenceXPCServer registerBlockForService:block:queue:eventLogLevel:]"
- "-[VCRedundancyControlAlgorithmVideo enableRedundancyForPersona]"
- "2145.45.1.11.2"
- "<FaceTime>[FaceTime][com.apple.AVConference]:Expanse Screen Share %@"
- "@32@0:8I16I20C24B28"
- "@40@0:8^{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}16^{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=@})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBB@}24^^{tagVCIDSChannelDataFormat}32"
- "@44@0:8@16I24{VCRedundancyControllerVideoParameters_t=@IBCB}28"
- "AVConferenceXPCServer [%s] %s:%d Process %s (PID=%d) is missing entitlement %s, ignoring connection"
- "B32@0:8^{_VCMediaStreamTransportSetupInfo=C(?={?=ii}{?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}}{?=^v^?BBi}@)IIB}16^@24"
- "B56@0:8^@16^i24^i32^i40^i48"
- "B64@0:8@16^{_VCMediaStreamTransportSetupInfo=C(?={?=ii}{?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}}{?=^v^?BBi}@)IIB}24B32B36@40@48^@56"
- "B64@0:8^@16^i24^i32^i40^i48^B56"
- "Bandwidth Estimation: Bandwidth estimator qualification parameters with RAT=%d, mode=%d. [maxBW=%f, minWin=%f, maxOverRange=%d, minPacketCount=%d]"
- "I28@0:8i16B20B24"
- "TI,N,V_redundancyControllerMode"
- "TI,N,V_redundancyMode"
- "TI,R,N,V_mode"
- "T{tagAVCSessionPresentationInfo={CGRect={CGPoint=dd}{CGSize=dd}}IICB},N"
- "VCSession [%s] %s:%d %@(%p) Session already stopped. stopError=%p"
- "VCSession [%s] %s:%d Session already stopped. stopError=%p"
- "VCVideoStream [%s] %s:%d VCVideoStream[%p] remoteScreenAttributes=%@, cachedRemoteScreenAttributes=%@, self.videoStreamDelegate=%p"
- "VCVideoStream [%s] %s:%d VCVideoStream[%p] remoteScreenAttributesForDelegate=%@, self.videoStreamDelegate=%p"
- "VideoUtil_DeserializeHEVCParameterSetsFromInputBuffer"
- "WiFiManagerCreate"
- "WiFiManagerDoApple80211"
- "WiFiManagerSetProperty"
- "[500{VCStatisticsStatsHistoryElement=\"linkID\"C\"statsUpdateTime\"d\"statsTimestamp\"I\"totalPacketSent\"I\"totalPacketReceived\"I\"totalByteSent\"Q\"totalByteReceived\"Q\"totalByteServerStatsUsed\"Q\"maxBurstyLoss\"I\"packetSeqNumber\"S}]"
- "_VCVideoStream_NotifyVideoStreamDelegate"
- "_areTilesShowing"
- "_totalEncodedBytesPerBundle"
- "afb"
- "areTilesShowing=%s displayRect=[%.0f, %.0f, %.0f, %.0f] layout=%u state=%u"
- "awdl0"
- "com.apple.TelephonyUtilities"
- "copyAWDLChannelSequence:twoPtFourGhzChannelCount:fiveGhzChannelCount:dfsChannelCount:inactiveSlotCount:"
- "copyAWDLChannelSequence:twoPtFourGhzChannelCount:fiveGhzChannelCount:dfsChannelCount:inactiveSlotCount:isPresent:"
- "createLogDumpListSortedByTimestamp:"
- "en"
- "enableRedundancyForPersona"
- "isWiFiPresent"
- "kWiFiManagerPropertyInterfaceName"
- "reportScreenShareIsStarting:"
- "und"
- "v16@?0^{VCPacket=^{OpaqueCMBlockBuffer}{?=BB[12S]CCBQBB[4Q]{?=iiBQ}Sd(?={?=II[16C]BB}{?=dCBC})}{?=^{VCPacket}}}8"
- "v28@?0i8^v12^{_VTPPacket=d{sockaddr_storage=CC[6c]q[112c]}I{tagIPPORT=i[16c](?=I[16C])S}{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=@})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBB@}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}}20"
- "v28@?0i8^v12^{_VTPPacket=d{sockaddr_storage=CC[6c]q[112c]}I{tagIPPORT=i[16c](?=I[16C])S}{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=^{nw_connection}})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBB^{nw_protocol_metadata}}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}}20"
- "v56@?0@\"NSObject<OS_dispatch_data>\"8@\"NSObject<OS_nw_content_context>\"16^{tagVPKTFLAG=iIIBBBBii{tagVCSourceDestinationInfo=i(?={?={tagIPPORT=i[16c](?=I[16C])S}{tagIPPORT=i[16c](?=I[16C])S}{?=BS}}{?=ii{tagIPPORT=i[16c](?=I[16C])S}i}{?=I{?=cSCSC}B}{?=@})I^{tagVCSourceDestinationInfo}^v}CiiiiiBBB{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagPKT_TAG=[4Q]}I[16C]BBBCBB@}24Q32Q40Q48"
- "v64@0:8{tagAVCSessionPresentationInfo={CGRect={CGPoint=dd}{CGSize=dd}}IICB}16"
- "{?=\"context\"^v\"creationCallback\"^?\"isReceiveExternallyScheduled\"B\"requiresLargeReceiveBuffer\"B\"transportStreamIndex\"i}"
- "{_VCMediaStreamTransportSetupInfo=\"setupType\"C\"\"(?=\"socketInfo\"{?=\"rtpSocket\"i\"rtcpSocket\"i}\"ipInfo\"{?=\"srcIPPORT\"{tagIPPORT=\"iFlags\"i\"szIfName\"[16c]\"IP\"(?=\"dwIPv4\"I\"abIPv6\"[16C])\"wPort\"S}\"srcRTPIPPort\"{tagIPPORT=\"iFlags\"i\"szIfName\"[16c]\"IP\"(?=\"dwIPv4\"I\"abIPv6\"[16C])\"wPort\"S}}\"transportStreamInfo\"{?=\"context\"^v\"creationCallback\"^?\"isReceiveExternallyScheduled\"B\"requiresLargeReceiveBuffer\"B\"transportStreamIndex\"i}\"nwConnection\"@\"NSObject<OS_nw_connection>\")\"sourceRate\"I\"datagramChannelToken\"I\"isSessionIDValid\"B}"
- "{tagAVCSessionPresentationInfo={CGRect={CGPoint=dd}{CGSize=dd}}IICB}16@0:8"

```
