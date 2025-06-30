## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-745.13.4.0.0
-  __TEXT.__text: 0x19957c
-  __TEXT.__auth_stubs: 0x4930
-  __TEXT.__objc_methlist: 0x2a4
+750.14.1.4.0
+  __TEXT.__text: 0x19e304
+  __TEXT.__auth_stubs: 0x4b20
+  __TEXT.__objc_methlist: 0x2f4
   __TEXT.__const: 0xe570
-  __TEXT.__cstring: 0x63e1d
-  __TEXT.__gcc_except_tab: 0x334
+  __TEXT.__cstring: 0x65a84
+  __TEXT.__gcc_except_tab: 0x3c8
   __TEXT.__oslogstring: 0x5df
-  __TEXT.__unwind_info: 0x2530
-  __TEXT.__objc_classname: 0x142
-  __TEXT.__objc_methname: 0x1664
-  __TEXT.__objc_methtype: 0x926
-  __TEXT.__objc_stubs: 0x1500
-  __DATA_CONST.__got: 0x1ac8
-  __DATA_CONST.__const: 0x59a0
+  __TEXT.__unwind_info: 0x261c
+  __TEXT.__objc_classname: 0x15b
+  __TEXT.__objc_methname: 0x180a
+  __TEXT.__objc_methtype: 0x94a
+  __TEXT.__objc_stubs: 0x16c0
+  __DATA_CONST.__got: 0x1b10
+  __DATA_CONST.__const: 0x5950
   __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xe88
-  __DATA_CONST.__objc_selrefs: 0x5c8
-  __AUTH_CONST.__cfstring: 0xf9a0
-  __AUTH_CONST.__const: 0x7260
-  __AUTH_CONST.__objc_const: 0x168
-  __AUTH_CONST.__auth_got: 0x24a8
-  __AUTH.__data: 0x570
+  __DATA_CONST.__objc_selrefs: 0x638
+  __AUTH_CONST.__cfstring: 0xfd00
+  __AUTH_CONST.__const: 0x7220
+  __AUTH_CONST.__objc_const: 0x1e8
+  __AUTH_CONST.__auth_got: 0x25a0
+  __AUTH.__data: 0x588
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_classrefs: 0xc0
+  __DATA.__objc_classrefs: 0xe0
   __DATA.__objc_superrefs: 0x28
   __DATA.__objc_ivar: 0x5c
-  __DATA.__data: 0x18590
-  __DATA.__bss: 0x520
+  __DATA.__data: 0x18600
+  __DATA.__bss: 0x538
   __DATA.__common: 0x9e4
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x7e8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DFF4B5B3-6BA3-3A50-8566-F01A8E742504
-  Functions: 3003
-  Symbols:   9837
-  CStrings:  10763
+  UUID: 04FBC1F6-24D9-3B35-ACA2-D67AC02DFE8F
+  Functions: 3039
+  Symbols:   9975
+  CStrings:  10943
 
Symbols:
+ -[CUPairedPeer(APPairingClientCoreUtils) patchedPairedPeerWithPeerInfo:]
+ -[CUPairingManager(APPairingClientCoreUtils) pairingGroupInfoForPairingGroupID:]
+ -[CUPairingManager(APPairingClientCoreUtils) peersMatchingPairingGroupID:]
+ -[CUPairingManager(APPairingClientCoreUtils) savePairedPeer:]
+ -[CUPairingManager(APPairingClientCoreUtils) updatePairingGroupInfo:forPairingGroupID:]
+ GCC_except_table10
+ GCC_except_table22
+ GCC_except_table31
+ _APAccTransportClientConnectionClose
+ _APAccTransportClientConnectionCopyEndpoint
+ _APAccTransportClientConnectionCreate
+ _APAccTransportClientConnectionGetTypeID
+ _APAccTransportClientConnectionInvalidateEndpoint
+ _APAccTransportClientConnectionOpen
+ _APAccTransportClientEndpointActivate
+ _APAccTransportClientEndpointCopyAuthenticationCertificateSerial
+ _APAccTransportClientEndpointDeactivate
+ _APAccTransportClientEndpointForwardData
+ _APAccTransportClientEndpointGetTypeID
+ _APAccTransportClientEndpointSecureTunnelDataSend
+ _APAccTransportClientEndpointSetAuthStatusHandler
+ _APAccTransportClientEndpointSetSecureTunnelDataReceiveHandler
+ _APBrokerManagerGetInfoFromBrokerGroup
+ _APPairingClientCoreUtilsCopyGroupInfo
+ _APPairingClientCoreUtilsCreateCombinedPairingGroupInfo
+ _APPairingClientCoreUtilsCreatePatchedPairedPeerWithPeerInfo
+ _APPairingClientCoreUtilsCreateUnpairedPeersFromGroupInfo
+ _APPairingClientCoreUtilsIsValidPairingGroupInfo
+ _APPairingClientCoreUtilsUpdateGroupInfo
+ _APSAudioFormatDescriptionListCopyChannelLayoutTags
+ _APSAudioFormatDescriptionListCreateFilteredListWithoutPassthroughFormats
+ _APSAudioFormatDescriptionListCreateIntersectionList
+ _APSBadgingFormatInfoCopyBadgeType
+ _APSCFArrayGetUInt64AtIndex
+ _APSCFArraySetUInt64AtIndex
+ _APSGetDeviceNameCString
+ _APSIsPairingGroupEnabled
+ _APSPriorityDispatcherAsync
+ _APSTimedInfoManagerAddTimedInfo
+ _APSTimedInfoManagerCreate
+ _APSTimedInfoManagerFlush
+ _APSTimedInfoManagerFlushWithinTimeRange
+ _APSTimedInfoManagerResume
+ _APSTimedInfoManagerSuspend
+ _APTransportDeviceCopyBrokeredReceiverInfo
+ _CC_SHA256
+ _CFArrayAppendInt64
+ _CFCopyTypeIDDescription
+ _CFDictionaryContainsValue
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterRemoveObserver
+ _CFPreferencesSynchronize
+ _CFStringCreateArrayBySeparatingStrings
+ _CFStringGetDoubleValue
+ _FigGetCFPreferenceBooleanWithDefault
+ _OBJC_CLASS_$_CUPairingManager
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSUUID
+ _PairingSessionGenerateTranscriptResultMFi4
+ _PairingSessionGetPairedPeer
+ _PairingSessionSetTranscriptType
+ __APAccTransportClientConnectionFinalize
+ __APAccTransportClientConnectionGetTypeID
+ __APAccTransportClientEndpointFinalize
+ __APAccTransportClientEndpointGetTypeID
+ __Block_object_assign
+ __OBJC_$_CATEGORY_CUPairedPeer_$_APPairingClientCoreUtils
+ __OBJC_$_CATEGORY_CUPairingManager_$_APPairingClientCoreUtils
+ __OBJC_$_INSTANCE_METHODS_CUPairedPeer(APPairingClientCoreUtils)
+ __OBJC_$_INSTANCE_METHODS_CUPairingManager(APPairingClientCoreUtils)
+ ___61-[CUPairingManager(APPairingClientCoreUtils) savePairedPeer:]_block_invoke
+ ___74-[CUPairingManager(APPairingClientCoreUtils) peersMatchingPairingGroupID:]_block_invoke
+ ___80-[CUPairingManager(APPairingClientCoreUtils) pairingGroupInfoForPairingGroupID:]_block_invoke
+ ___87-[CUPairingManager(APPairingClientCoreUtils) updatePairingGroupInfo:forPairingGroupID:]_block_invoke
+ ___APAccTransportClientConnectionClose_block_invoke
+ ___APAccTransportClientConnectionClose_block_invoke_2
+ ___APAccTransportClientConnectionCopyEndpoint_block_invoke
+ ___APAccTransportClientConnectionInvalidateEndpoint_block_invoke
+ ___APAccTransportClientConnectionOpen_block_invoke
+ ___APAccTransportClientEndpointActivate_block_invoke
+ ___APAccTransportClientEndpointActivate_block_invoke_2
+ ___APAccTransportClientEndpointActivate_block_invoke_3
+ ___APAccTransportClientEndpointCopyAuthenticationCertificateSerial_block_invoke
+ ___APAccTransportClientEndpointDeactivate_block_invoke
+ ___APAccTransportClientEndpointForwardData_block_invoke
+ ___APAccTransportClientEndpointSecureTunnelDataSend_block_invoke
+ ___APAccTransportClientEndpointSetAuthStatusHandler_block_invoke
+ ___APAccTransportClientEndpointSetAuthStatusHandler_block_invoke_2
+ ___APAccTransportClientEndpointSetAuthStatusHandler_block_invoke_3
+ ___APAccTransportClientEndpointSetSecureTunnelDataReceiveHandler_block_invoke
+ ___APAccTransportClientEndpointSetSecureTunnelDataReceiveHandler_block_invoke_2
+ ___APAccTransportClientEndpointSetSecureTunnelDataReceiveHandler_block_invoke_3
+ ___APPairingClientCoreUtilsCreateUnpairedPeersFromGroupInfo_block_invoke
+ ___APPairingClientCoreUtilsCreateUnpairedPeersFromGroupInfo_block_invoke_2
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___accTransportClientEndpointInvalidate_block_invoke
+ ___block_descriptor_40_e8_32o_e10_v16?0r^v8ls32l8
+ ___block_descriptor_40_e8_32o_e24_v20?0^{__CFString=}8B16ls32l8
+ ___block_descriptor_40_e8_32o_e29_v32?0"CUPairedPeer"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32o_e35_v24?0^{__CFString=}8^{__CFData=}16ls32l8
+ ___block_descriptor_40_e8_32o_e51_v32?0^{__CFString=}8^{__CFString=}16^{__CFData=}24ls32l8
+ ___block_descriptor_48_e29_v32?0"CUPairedPeer"8Q16^B24l
+ ___block_descriptor_48_e8_32o40o_e15_v24?0r^v8r^v16ls32l8s40l8
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_56_e8_32b40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32o40o48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32o40o48r_e29_v24?0"NSArray"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_69_e8_32b40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_tmp.1001
+ ___block_descriptor_tmp.1002
+ ___block_descriptor_tmp.1003
+ ___block_descriptor_tmp.1004
+ ___block_descriptor_tmp.1005
+ ___block_descriptor_tmp.1032
+ ___block_descriptor_tmp.1058
+ ___block_descriptor_tmp.1065
+ ___block_descriptor_tmp.1066
+ ___block_descriptor_tmp.1072
+ ___block_descriptor_tmp.1074
+ ___block_descriptor_tmp.1093
+ ___block_descriptor_tmp.1095
+ ___block_descriptor_tmp.1096
+ ___block_descriptor_tmp.1103
+ ___block_descriptor_tmp.1104
+ ___block_descriptor_tmp.1106
+ ___block_descriptor_tmp.1115
+ ___block_descriptor_tmp.1117
+ ___block_descriptor_tmp.1118
+ ___block_descriptor_tmp.1121
+ ___block_descriptor_tmp.1126
+ ___block_descriptor_tmp.1130
+ ___block_descriptor_tmp.1131
+ ___block_descriptor_tmp.115
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.135
+ ___block_descriptor_tmp.138
+ ___block_descriptor_tmp.186
+ ___block_descriptor_tmp.201
+ ___block_descriptor_tmp.204
+ ___block_descriptor_tmp.230
+ ___block_descriptor_tmp.248
+ ___block_descriptor_tmp.250
+ ___block_descriptor_tmp.253
+ ___block_descriptor_tmp.267
+ ___block_descriptor_tmp.278
+ ___block_descriptor_tmp.300
+ ___block_descriptor_tmp.306
+ ___block_descriptor_tmp.315
+ ___block_descriptor_tmp.327
+ ___block_descriptor_tmp.332
+ ___block_descriptor_tmp.350
+ ___block_descriptor_tmp.366
+ ___block_descriptor_tmp.384
+ ___block_descriptor_tmp.404
+ ___block_descriptor_tmp.409
+ ___block_descriptor_tmp.411
+ ___block_descriptor_tmp.415
+ ___block_descriptor_tmp.421
+ ___block_descriptor_tmp.459
+ ___block_descriptor_tmp.462
+ ___block_descriptor_tmp.465
+ ___block_descriptor_tmp.470
+ ___block_descriptor_tmp.484
+ ___block_descriptor_tmp.557
+ ___block_descriptor_tmp.602
+ ___block_descriptor_tmp.621
+ ___block_descriptor_tmp.657
+ ___block_descriptor_tmp.659
+ ___block_descriptor_tmp.661
+ ___block_descriptor_tmp.664
+ ___block_descriptor_tmp.666
+ ___block_descriptor_tmp.669
+ ___block_descriptor_tmp.710
+ ___block_descriptor_tmp.712
+ ___block_descriptor_tmp.713
+ ___block_descriptor_tmp.761
+ ___block_descriptor_tmp.762
+ ___block_descriptor_tmp.763
+ ___block_descriptor_tmp.764
+ ___block_descriptor_tmp.765
+ ___block_descriptor_tmp.784
+ ___block_descriptor_tmp.785
+ ___block_descriptor_tmp.786
+ ___block_descriptor_tmp.787
+ ___block_descriptor_tmp.808
+ ___block_descriptor_tmp.809
+ ___block_descriptor_tmp.886
+ ___block_literal_global.103
+ ___block_literal_global.137
+ ___block_literal_global.172
+ ___block_literal_global.269
+ ___block_literal_global.280
+ ___block_literal_global.30
+ ___block_literal_global.369
+ ___block_literal_global.424
+ ___block_literal_global.44
+ ___block_literal_global.471
+ ___block_literal_global.789
+ ___bufferedAudioEngine_soundCheckChanged_block_invoke
+ ___carEndpoint_activateInternal_block_invoke.113
+ ___carEndpoint_activateInternal_block_invoke_2.124
+ ___carEndpoint_activateInternal_block_invoke_2.132
+ ___carEndpoint_activateInternal_block_invoke_3.137
+ ___carEndpoint_setUpAPAccClientEndpointForIdType_block_invoke
+ ___coreUtilsPairing_getPairedPeerFromVerificationPairingSession_block_invoke
+ ___manager_handleDiscoveryBrokerRequest_block_invoke
+ ___manager_handleDiscoveryBrokerRequest_block_invoke_2
+ ___mfiMutualAuth_sendMessageMFi4_block_invoke
+ _accTransportClientEndpointDestroyEndpoint
+ _airPlayDescription_copyCarPlayAudioFormatsExtended
+ _airPlayDescription_isCarPlaySpatialAudioSupported
+ _airPlayDescription_isDCXSupportedForSpatialAudio
+ _apsession_copyAPPairingGroupInfo
+ _apsession_getTransportsRequiringBroker
+ _apsession_isBrokerAssistedConnection
+ _apsession_tryAPPairSetupAndVerify
+ _audioStream_audioHoseEnableLoudnessNormalization
+ _audioStream_audioHoseEnableLoudnessNormalizationInternal
+ _audioStream_copySupportedAudioCapabilities
+ _bufferedAudioEngine_adjustRemoteMediaTimeForDiscontinuity
+ _bufferedAudioEngine_handleTerminalSetRateError
+ _bufferedAudioEngine_handleTimedInfoManagerNotification
+ _bufferedAudioEngine_readSoundCheck
+ _bufferedAudioEngine_recordPreparedAudioDataAndAudioFormatDuration
+ _bufferedAudioEngine_soundCheckChanged
+ _carEndpoint_createAccConnectionIfNeeded
+ _carEndpoint_setUpAPAccClientEndpointForIdType
+ _coreUtilsPairing_CopyProperty
+ _gAPAccTransportClientConnectionInitOnce
+ _gAPAccTransportClientConnectionTypeID
+ _gAPAccTransportClientEndpointInitOnce
+ _gAPAccTransportClientEndpointTypeID
+ _gLogCategory_APAccTransportClientConnection
+ _gLogCategory_APAccTransportClientEndpoint
+ _gSoundCheckEnabled
+ _kAPAccTransportClientConnectionClass
+ _kAPAccTransportClientConnectionCreationOption_AuthenticationCertificateSerial
+ _kAPAccTransportClientEndpointClass
+ _kAPBrokerManagerGetInfoFromBrokerGroupCallbackResponseKey_BrokerGroupInfo
+ _kAPEndpointDescriptionProperty_SupportsDCXForSpatialAudio
+ _kAPEndpointStreamAudioEngineTimedInfoDictKey_ContentType
+ _kAPPairingClientProperty_PairingTranscriptData
+ _kAPSTimedInfoManagerNotification_TimerFired
+ _kAPSenderSessionKey_SoundCheckMediaKind
+ _kAPSenderSessionStreamKey_PacketFormatAPAP
+ _kAPTNANDataSessionStatisticsReportKey_TxCCA
+ _kAPTNANDataSessionStatisticsReportKey_TxErrorCount
+ _kFigEndpointProperty_SupportsDCXForSpatialAudio
+ _kFigEndpointStreamAudioEngineNotification_FormatInfoChanged
+ _kFigEndpointStreamNotification_AudioCapabilitiesChanged
+ _kFigEndpointStreamProperty_SupportedAudioCapabilities
+ _kFigEndpointStreamSupportedAudioCapabilities_SupportedChannelLayoutTags
+ _manager_handleDiscoveryBrokerRequest
+ _mfiMutualAuth_sendMessageMFi4
+ _objc_autorelease
+ _objc_msgSend$addObject:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$getPairedPeersWithGroupID:options:completion:
+ _objc_msgSend$groupInfo
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$pairingGroupInfoForPairingGroupID:
+ _objc_msgSend$patchedPairedPeerWithPeerInfo:
+ _objc_msgSend$peersMatchingPairingGroupID:
+ _objc_msgSend$savePairedPeer:
+ _objc_msgSend$savePairedPeer:options:completion:
+ _objc_msgSend$set
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$updatePairedPeersWithGroupID:groupInfo:options:completion:
+ _objc_msgSend$updatePairingGroupInfo:forPairingGroupID:
+ _objc_opt_new
+ _objc_retain
+ _streamAggregateAudio_copySupportedAudioCapabilities
- _APAuthenticationClientMFiMutualAuthCreateDecryptedMessage
- _APAuthenticationClientMFiMutualAuthCreateEncryptedMessage
- _APPairingClientCoreUtilsPatchPairedPeerDescriptionWithWoLInfo
- _APPairingClientMFi4Create
- _APPairingClientMFi4_BaseClassWrapper
- _APSAudioFormatDescriptionListCreateFilteredList
- _APiAPCopyAuthenticationCertificateSerial
- _APiAPDestroyEndpoint
- _APiAPHelperCreate
- _APiAPHelperForwardData
- _APiAPHelperGetConnectionUUID
- _APiAPHelperGetTypeID.sInitOnce
- _APiAPHelperGetTypeID.sTypeID
- _APiAPHelperInvalidate
- _APiAPHelperSecureTunnelDataSend
- _APiAPHelperSetAuthStatusHandler
- _APiAPHelperSetDataHandler
- _APiAPHelperSetSecureTunnelDataReceiveHandler
- _GetDeviceName
- _PairingSessionCopyPairedPeer
- ___APAuthenticationClientMFiMutualAuthCreateDecryptedMessage_block_invoke
- ___APAuthenticationClientMFiMutualAuthCreateEncryptedMessage_block_invoke
- ___APiAPCopyAuthenticationCertificateSerial_block_invoke
- ___APiAPDestroyEndpoint_block_invoke
- ___APiAPHelperForwardData_block_invoke
- ___APiAPHelperGetTypeID_block_invoke
- ___APiAPHelperInvalidate_block_invoke
- ___APiAPHelperSecureTunnelDataSend_block_invoke
- ___APiAPHelperSetAuthStatusHandler_block_invoke
- ___APiAPHelperSetAuthStatusHandler_block_invoke_2
- ___APiAPHelperSetAuthStatusHandler_block_invoke_3
- ___APiAPHelperSetDataHandler_block_invoke
- ___APiAPHelperSetDataHandler_block_invoke_2
- ___APiAPHelperSetDataHandler_block_invoke_3
- ___APiAPHelperSetSecureTunnelDataReceiveHandler_block_invoke
- ___APiAPHelperSetSecureTunnelDataReceiveHandler_block_invoke_2
- ___APiAPHelperSetSecureTunnelDataReceiveHandler_block_invoke_3
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.1000
- ___block_descriptor_tmp.1027
- ___block_descriptor_tmp.1048
- ___block_descriptor_tmp.1052
- ___block_descriptor_tmp.1055
- ___block_descriptor_tmp.1061
- ___block_descriptor_tmp.1069
- ___block_descriptor_tmp.1086
- ___block_descriptor_tmp.1088
- ___block_descriptor_tmp.1090
- ___block_descriptor_tmp.1098
- ___block_descriptor_tmp.1099
- ___block_descriptor_tmp.1101
- ___block_descriptor_tmp.1108
- ___block_descriptor_tmp.1110
- ___block_descriptor_tmp.1111
- ___block_descriptor_tmp.1114
- ___block_descriptor_tmp.1119
- ___block_descriptor_tmp.1123
- ___block_descriptor_tmp.1124
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.124
- ___block_descriptor_tmp.131
- ___block_descriptor_tmp.134
- ___block_descriptor_tmp.139
- ___block_descriptor_tmp.187
- ___block_descriptor_tmp.202
- ___block_descriptor_tmp.231
- ___block_descriptor_tmp.251
- ___block_descriptor_tmp.254
- ___block_descriptor_tmp.264
- ___block_descriptor_tmp.27
- ___block_descriptor_tmp.275
- ___block_descriptor_tmp.297
- ___block_descriptor_tmp.302
- ___block_descriptor_tmp.307
- ___block_descriptor_tmp.317
- ___block_descriptor_tmp.328
- ___block_descriptor_tmp.333
- ___block_descriptor_tmp.344
- ___block_descriptor_tmp.361
- ___block_descriptor_tmp.406
- ___block_descriptor_tmp.408
- ___block_descriptor_tmp.410
- ___block_descriptor_tmp.412
- ___block_descriptor_tmp.416
- ___block_descriptor_tmp.460
- ___block_descriptor_tmp.463
- ___block_descriptor_tmp.466
- ___block_descriptor_tmp.471
- ___block_descriptor_tmp.485
- ___block_descriptor_tmp.5
- ___block_descriptor_tmp.558
- ___block_descriptor_tmp.603
- ___block_descriptor_tmp.622
- ___block_descriptor_tmp.658
- ___block_descriptor_tmp.660
- ___block_descriptor_tmp.662
- ___block_descriptor_tmp.665
- ___block_descriptor_tmp.667
- ___block_descriptor_tmp.670
- ___block_descriptor_tmp.705
- ___block_descriptor_tmp.707
- ___block_descriptor_tmp.708
- ___block_descriptor_tmp.755
- ___block_descriptor_tmp.756
- ___block_descriptor_tmp.757
- ___block_descriptor_tmp.758
- ___block_descriptor_tmp.759
- ___block_descriptor_tmp.779
- ___block_descriptor_tmp.780
- ___block_descriptor_tmp.781
- ___block_descriptor_tmp.782
- ___block_descriptor_tmp.798
- ___block_descriptor_tmp.804
- ___block_descriptor_tmp.881
- ___block_descriptor_tmp.996
- ___block_descriptor_tmp.997
- ___block_descriptor_tmp.998
- ___block_descriptor_tmp.999
- ___block_literal_global.134
- ___block_literal_global.169
- ___block_literal_global.266
- ___block_literal_global.277
- ___block_literal_global.32
- ___block_literal_global.363
- ___block_literal_global.41
- ___block_literal_global.410
- ___block_literal_global.452
- ___block_literal_global.64
- ___block_literal_global.784
- ___carEndpoint_activateInternal_block_invoke.114
- ___carEndpoint_activateInternal_block_invoke_2.125
- ___carEndpoint_activateInternal_block_invoke_2.133
- ___carEndpoint_activateInternal_block_invoke_3.138
- ___carEndpoint_setUpAPiAPHelperForIdType_block_invoke
- ___manager_handleAuthenticateDiscoveryBroker_block_invoke
- _bufferedAudioEngine_hoseSetRateOrGetAnchorHitMaxRetries
- _carEndpoint_setUpAPiAPHelperForIdType
- _coreUtilsPairing_processMessageAndTransformIfNeeded
- _gLogCategory_APPairingClientMFi4
- _iAPHelperClientQueueFinalizer
- _iAPHelperFinalize
- _iAPHelperInvalidate
- _kAPPairingClientMFi4VTable
- _kAPPairingClientMFi4_APPairingClientClass
- _kAPPairingClientProperty_AuthenticationData
- _kAPiAPHelperClass
- _manager_handleAuthenticateDiscoveryBroker
- _mfi4Pairing_CopyDebugDescription
- _mfi4Pairing_CopyProperty
- _mfi4Pairing_DeriveKey
- _mfi4Pairing_Finalize
- _mfi4Pairing_IsPeerKnown
- _mfi4Pairing_PerformSetup
- _mfi4Pairing_PerformVerification
- _mfi4Pairing_ensureAuthenticated
- _mfi4Pairing_handleCreateDecryptedMessage
- _mfi4Pairing_handleCreateEncryptedMessage
- _objc_msgSend$label
- _objc_msgSend$setLabel:
CStrings:
+ "%{ptr} Enabling core captures on receiver.\n"
+ ","
+ "-[CUPairedPeer(APPairingClientCoreUtils) patchedPairedPeerWithPeerInfo:]"
+ "-[CUPairingManager(APPairingClientCoreUtils) peersMatchingPairingGroupID:]"
+ "-[CUPairingManager(APPairingClientCoreUtils) peersMatchingPairingGroupID:]_block_invoke"
+ "-[CUPairingManager(APPairingClientCoreUtils) savePairedPeer:]"
+ "-[CUPairingManager(APPairingClientCoreUtils) savePairedPeer:]_block_invoke"
+ "-[CUPairingManager(APPairingClientCoreUtils) updatePairingGroupInfo:forPairingGroupID:]"
+ "-[CUPairingManager(APPairingClientCoreUtils) updatePairingGroupInfo:forPairingGroupID:]_block_invoke"
+ "750.14.1"
+ "@24@0:8@16"
+ "ALAC/44100/20/2"
+ "ALAC/48000/20/2"
+ "APAC/48000/2"
+ "APAC/48000/5.1"
+ "APAC/48000/5.1.2"
+ "APAC/48000/5.1.4"
+ "APAC/48000/7.1"
+ "APAC/48000/7.1.2"
+ "APAC/48000/7.1.4"
+ "APAccTransportClientConnection"
+ "APAccTransportClientConnectionClose_block_invoke"
+ "APAccTransportClientConnectionCopyEndpoint"
+ "APAccTransportClientConnectionCopyEndpoint_block_invoke"
+ "APAccTransportClientConnectionCreate"
+ "APAccTransportClientConnectionInvalidateEndpoint"
+ "APAccTransportClientConnectionInvalidateEndpoint_block_invoke"
+ "APAccTransportClientConnectionOpen_block_invoke"
+ "APAccTransportClientEndpoint"
+ "APAccTransportClientEndpointActivate"
+ "APAccTransportClientEndpointActivate_block_invoke"
+ "APAccTransportClientEndpointCopyAuthenticationCertificateSerial_block_invoke"
+ "APAccTransportClientEndpointDeactivate_block_invoke"
+ "APAccTransportClientEndpointForwardData_block_invoke"
+ "APAccTransportClientEndpointSecureTunnelDataSend_block_invoke"
+ "APAccTransportClientEndpointSetAuthStatusHandler"
+ "APAccTransportClientEndpointSetAuthStatusHandler_block_invoke"
+ "APAccTransportClientEndpointSetSecureTunnelDataReceiveHandler"
+ "APAccTransportClientEndpointSetSecureTunnelDataReceiveHandler_block_invoke"
+ "APPairingClientCoreUtilsCopyGroupInfo"
+ "APPairingClientCoreUtilsCreateCombinedPairingGroupInfo"
+ "APPairingClientCoreUtilsCreateUnpairedPeersFromGroupInfo"
+ "APPairingClientCoreUtilsIsValidPairingGroupInfo"
+ "APPairingClientCoreUtilsUpdateGroupInfo"
+ "AirPlay/750.14.1"
+ "Authenticate"
+ "BAE [%{ptr}] %s### [0x%04X] hose [%{ptr}] has encountered terminal errors during SetRate, dissociating...\n"
+ "BAE [%{ptr}] %sSoundCheck preference updated to: %s"
+ "BAE [%{ptr}] %s[0x%04X] BadgeType changed to %@ at remoteMediaTime = %1.3f (%ld/%d) Source content: %@ Transport content: %@"
+ "BAE [%{ptr}] %s[0x%04X] RemoteMediaTimebase started. First audible time relative to now: %1.6f \n"
+ "BAE [%{ptr}] %s[0x%04X] Set Loudness Normalization Pref %s for hose [%{ptr}] \n"
+ "BAE [%{ptr}] %s[0x%04X] SetRate 1 FAILURE for hose [%{ptr}] err = %d, calling callback.\n"
+ "BAE [%{ptr}] %s[0x%04X] Update BadgeType to %@ at remoteMediaTime = %1.3f (%ld/%d)"
+ "Broker get info callback failed to handle response with error: %#m\n"
+ "Broker get info callback for request %'@. error: %#m%?s%?@\n"
+ "BrokerAuthString"
+ "BrokerGroupInfo"
+ "BrokerRequest"
+ "BrokerResponse"
+ "CUPairedPeer *coreUtilsPairing_getPairedPeerFromVerificationPairingSession(APPairingClientRef, CFDictionaryRef)"
+ "CUPairedPeer *coreUtilsPairing_getPairedPeerFromVerificationPairingSession(APPairingClientRef, CFDictionaryRef)_block_invoke"
+ "CarPlayProtocolData"
+ "CarPlayProtocolData2"
+ "ContentType"
+ "Created pairing group unpaired peer [%{ptr}] with identifier %'@\n"
+ "DCXEnabled"
+ "Failed to convert group peer identifier %'@ into UUID\n"
+ "Failed to get paired peers matching pairing group ID %@: %#m\n"
+ "Failed to save paired peer [%{ptr}]: %#m\n"
+ "Failed to update group info for pairing group ID %@: %#m\n"
+ "GetInfo"
+ "Getting paired peers matching pairing group ID %@\n"
+ "Got %d paired peers matching pairing group ID %@\n"
+ "LTPK for identifier %'@: is of %@ type instead of CFData type\n"
+ "MusicSoundCheckEnabledSetting"
+ "OSStatus APAccTransportClientConnectionClose(APAccTransportClientConnectionRef)_block_invoke"
+ "OSStatus APAccTransportClientConnectionCreate(CFDictionaryRef, APAccTransportClientConnectionRef *)"
+ "OSStatus APAccTransportClientConnectionOpen(APAccTransportClientConnectionRef)_block_invoke"
+ "OSStatus APAccTransportClientEndpointActivate(APAccTransportClientEndpointRef, ACCEndpoint_Protocol_t, Boolean, APAccTransportClientEndpointDataHandler)_block_invoke"
+ "OSStatus APAccTransportClientEndpointActivate(APAccTransportClientEndpointRef, ACCEndpoint_Protocol_t, Boolean, APAccTransportClientEndpointDataHandler)_block_invoke_2"
+ "OSStatus APAccTransportClientEndpointForwardData(APAccTransportClientEndpointRef, CFDataRef)_block_invoke"
+ "OSStatus APAccTransportClientEndpointSecureTunnelDataSend(APAccTransportClientEndpointRef, CFDataRef)_block_invoke"
+ "OSStatus APAccTransportClientEndpointSetAuthStatusHandler(APAccTransportClientEndpointRef, APAccTransportClientEndpointAuthStatusHandler)_block_invoke_2"
+ "OSStatus APAccTransportClientEndpointSetSecureTunnelDataReceiveHandler(APAccTransportClientEndpointRef, APAccTransportClientEndpointSecureTunnelDataReceiveHandler)_block_invoke_2"
+ "OSStatus APAuthenticationClientMFiMutualAuthCreate(CFAllocatorRef, FigTransportStreamRef, APAccTransportClientConnectionRef, CFDataRef, APAuthenticationClientRef *)"
+ "OSStatus APPairingClientCoreUtilsCreate(CFAllocatorRef, CFStringRef, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, CFStringRef, CFStringRef, CFDataRef, FigTransportStreamRef, APPairingClientRef *)"
+ "OSStatus APPairingClientCoreUtilsCreateUnpairedPeersFromGroupInfo(CFDictionaryRef, CFArrayRef, CFArrayRef *)_block_invoke_2"
+ "OSStatus accEndpointCreate(const char *, CFStringRef, CFDataRef, APAccTransportClientEndpointRef *)"
+ "OSStatus accTransportClientEndpointDestroyEndpoint(APAccTransportClientEndpointRef)"
+ "OSStatus apsession_createPairingClient(APSenderSessionRef, Boolean, Boolean, Boolean, Boolean, CFStringRef, CFDataRef, APPairingClientRef *)"
+ "OSStatus audioStream_copySupportedAudioCapabilities(FigEndpointStreamRef, CFDictionaryRef *)"
+ "OSStatus audioStream_setupAudioStream(FigEndpointStreamRef, APSenderSessionRef, Boolean, APSAudioFormatDescriptionRef, CFDataRef, CFStringRef, Boolean, Boolean, uint64_t, CFStringRef, CFNumberRef, CFStringRef, CFStringRef, Boolean, Boolean, CFDataRef, Boolean, uint64_t *, Boolean *, int *, int32_t *, int *, CFDataRef *)"
+ "OSStatus bufferedAudioEngine_enableLoudnessNormalizationOnAllHoses(FigEndpointStreamAudioEngineRef)"
+ "OSStatus carEndpoint_setUpAPAccClientEndpointForIdType(FigEndpointRef, CFStringRef, Boolean)_block_invoke"
+ "OSStatus manager_handleDiscoveryBrokerRequest(CFStringRef, CFDictionaryRef, CFDictionaryRef *)"
+ "OSStatus mfiMutualAuth_exchangeArea51Message(APAuthenticationClientRef, CMBlockBufferRef, CFDataRef *)"
+ "OSStatus mfiMutualAuth_initMFi4(APAuthenticationClientRef)_block_invoke"
+ "OSStatus mfiMutualAuth_sendAndVerifyPairingData(APAuthenticationClientRef)"
+ "OSStatus mfiMutualAuth_sendMessageMFi4(APAuthenticationClientRef, CFDataRef, CFDictionaryRef, CMBlockBufferRef *)"
+ "OSStatus streamAggregateAudio_copySupportedAudioCapabilities(FigEndpointStreamRef, CFDictionaryRef *)"
+ "Operation timed out on remote endpoint"
+ "PairingTranscriptData"
+ "Patched up CUPairedPeer info: %@\n"
+ "Post BrokerResponse event with payload %@\n"
+ "Processing broker get info request %'@ for brokerGroup %'@"
+ "Received discovery broker request with payload: %@\n"
+ "RequestType"
+ "RequestUUID"
+ "Saved paired peer [%{ptr}]: %@\n"
+ "Saving paired peer [%{ptr}]: %@\n"
+ "SecureTunnel-Failed"
+ "SecureTunnel-ProcessingArea51MessageCallback"
+ "SecureTunnel-ProcessingDecryptionCallback"
+ "SecureTunnel-ProcessingEncryptionCallback"
+ "SecureTunnel-WaitingForArea51Callback"
+ "SecureTunnel-WaitingForDecryptionCallback"
+ "SecureTunnel-WaitingForEncryptionCallback"
+ "SetRate encountered terminal error"
+ "SupportsDCXForSpatialAudio"
+ "Unsupported discovery broker request type: %@"
+ "Updated group info for pairing group ID %@\n"
+ "Updating group info for pairing group ID %@\n"
+ "X-Apple-PairingTranscript"
+ "[%{ptr}] APPairingClientCoreUtils created %c%c%c%c%c%c%c%c%c.\n"
+ "[%{ptr}] Area51 message: Forwarding %zu bytes to acc endpoint\n"
+ "[%{ptr}] AuthStatusDidChangeHandler, authenticated: %d\n"
+ "[%{ptr}] Authentication Exchange for a message is completed and signaled from the acc endpoint callback\n"
+ "[%{ptr}] Authentication Exchange is started, awaiting first callback from acc endpoint\n"
+ "[%{ptr}] Authentication succeeded\n"
+ "[%{ptr}] Combined group info: %1.64@\n"
+ "[%{ptr}] Connection is unexpectedly open during Finalize, cleaning up...\n"
+ "[%{ptr}] Connection opened, connectionUUID: %@\n"
+ "[%{ptr}] Copied peer group info from pair-verify session [%{ptr}]: %1.64@\n"
+ "[%{ptr}] Created %s pair-verify session [%{ptr}]\n"
+ "[%{ptr}] Created, inEndpointID: %s\n"
+ "[%{ptr}] DataHandler called unexpectedly during Authentication with inData %s\n"
+ "[%{ptr}] DataHandler called unexpectedly during Encryption with inData %s\n"
+ "[%{ptr}] DataHandler called with inData %s\n"
+ "[%{ptr}] Discarding self group info for pair-verify session [%{ptr}]\n"
+ "[%{ptr}] Failed to set self group info on pair-verify session [%{ptr}]: %#m\n"
+ "[%{ptr}] Finalizing\n"
+ "[%{ptr}] Forwarding %zu bytes to APAccTransportClientEndpoint (Crypto Operation: %d)\n"
+ "[%{ptr}] Forwarding %zu bytes to accTransportClientEndpoint\n"
+ "[%{ptr}] Initializing MFi4 Authentication (accTransportClientEndpoint: [%{ptr}])\n"
+ "[%{ptr}] LL Audio TTR currently allowed: %s; weighted highCCACount: %d < %d; txErrCount %d > %d"
+ "[%{ptr}] Posting 'AudioCapabilitiesChanged'!"
+ "[%{ptr}] Protocol operation for a message is completed and signaled from the acc endpoint callback\n"
+ "[%{ptr}] RCS ref creation complete for: %@\n"
+ "[%{ptr}] RCS ref creation start for: %@\n"
+ "[%{ptr}] Received %u bytes of data from receiver\n"
+ "[%{ptr}] Received %u bytes of decrypted data from SecureTunnel\n"
+ "[%{ptr}] Registering incoming RCS with commChannelID [%@] from subEndpoint [%{ptr}]\n"
+ "[%{ptr}] Returning existing RCS session: %@ : %@\n"
+ "[%{ptr}] Saving pairing group unpaired peer [%{ptr}] with identifier %@\n"
+ "[%{ptr}] SecureTunnel operation for a message has completed and signaled from the acc endpoint callback\n"
+ "[%{ptr}] SecureTunnelDataReceiveHandler called unexpectedly, dataReceived %s\n"
+ "[%{ptr}] SecureTunnelDataReceiveHandler called with inData %s\n"
+ "[%{ptr}] Sending %u bytes of data to receiver\n"
+ "[%{ptr}] Sent %u bytes of data to SecureTunnel to encrypt\n"
+ "[%{ptr}] Set Loudness Normalization Pref %s"
+ "[%{ptr}] Setting self group info on pair-verify session [%{ptr}]: %1.64@\n"
+ "[%{ptr}] Starting Authentication sequence\n"
+ "[%{ptr}] Starting Protocol Message Exchange with Core Accessories\n"
+ "[%{ptr}] Starting message exchange with CoreAccessories\n"
+ "[%{ptr}] Starting verification of Pairing Data\n"
+ "[%{ptr}] SupportedAudioCapabilities: %@"
+ "[%{ptr}] Verify Auth Certificate Serial requested\n"
+ "[%{ptr}] destroying of acc connection %s\n"
+ "[%{ptr}] destroying of acc endpoint was %s\n"
+ "[%{ptr}] mfiMutualAuth_copyAuthenticationData, authenticationData %s\n"
+ "[%{ptr}] sendAndVerifyPairingData succeeded\n"
+ "[%{ptr}] subtracting %d minutes ago High CCA counter value: %llu from High CCA counter val: %llu "
+ "[%{ptr}] subtracting %d minutes ago Tx Error counter value: %llu from Tx Error counter val: %llu "
+ "[%{ptr}] total session minutes: %llu; wifi index at %llu; resetting now."
+ "],"
+ "accEndpointCreate"
+ "accTransportClientEndpointDestroyEndpoint"
+ "addObject:"
+ "airPlayDescription_copyCarPlayAudioFormatsExtended"
+ "audioOutputFormatsExtended"
+ "audioStream_audioHoseEnableLoudnessNormalizationInternal"
+ "audioStream_copySupportedAudioCapabilities"
+ "audioStream_monitorWifiStatsForTTRThrottling"
+ "audioStream_startStatsTimer"
+ "bufferedAPACSurround"
+ "carEndpoint_createAccConnectionIfNeeded"
+ "carEndpoint_setUpAPAccClientEndpointForIdType"
+ "com.apple.APAccClientEndpoint"
+ "com.apple.APAccClientEndpointProtocolData1"
+ "com.apple.APAccClientEndpointProtocolData2"
+ "com.apple.APAccTransportClientConnection"
+ "com.apple.AccTransportClientEndpointMFi4Authentication"
+ "com.apple.mobileipod"
+ "com.apple.mobileipod-prefsChanged"
+ "containsObject:"
+ "coreUtilsPairing_CopyProperty"
+ "coreUtilsPairing_getPairedPeerFromVerificationPairingSession"
+ "coreUtilsPairing_performAdminPairingOperation"
+ "enumerateObjectsUsingBlock:"
+ "failed"
+ "getPairedPeersWithGroupID:options:completion:"
+ "groupID"
+ "groupInfo"
+ "groupInfoPeer"
+ "groupInfoSelf"
+ "highCCALLATTRWeightedThreshold"
+ "i24@0:8@16"
+ "i32@0:8@16@24"
+ "initWithCapacity:"
+ "initWithUUIDString:"
+ "loudnessNormalizationEnabled"
+ "manager_brokerManagerGetBrokerGroupInfoCallback"
+ "manager_handleDiscoveryBrokerRequest"
+ "mfiMutualAuth_exchangeArea51Message"
+ "mfiMutualAuth_sendAndVerifyPairingData"
+ "not set"
+ "packetFormatAPAP"
+ "pairingGroupInfoForPairingGroupID:"
+ "patchedPairedPeerWithPeerInfo:"
+ "peersMatchingPairingGroupID:"
+ "savePairedPeer:"
+ "savePairedPeer:options:completion:"
+ "set"
+ "setObject:forKeyedSubscript:"
+ "soundCheckMediaKind"
+ "streamAggregateAudio_copySupportedAudioCapabilities"
+ "streamAggregateAudio_supportedChannelLayoutTagsDidChange"
+ "successful"
+ "txErrLLATTRThreshold"
+ "updatePairedPeersWithGroupID:groupInfo:options:completion:"
+ "updatePairingGroupInfo:forPairingGroupID:"
+ "v32@?0@\"CUPairedPeer\"8Q16^B24"
+ "void _APAccTransportClientConnectionFinalize(CFTypeRef)"
+ "void _APAccTransportClientEndpointFinalize(CFTypeRef)"
+ "void audioStream_audioHoseEnableLoudnessNormalizationInternal(void *)"
+ "void audioStream_enableReceiverCoreCapturesInternal(void *)"
+ "void audioStream_monitorWifiStatsForTTRThrottling(FigEndpointStreamRef, CFDictionaryRef)"
+ "void bufferedAudioEngine_handleTerminalSetRateError(FigEndpointStreamAudioEngineRef, APSEndpointStreamAudioHoseRef, OSStatus, Boolean)"
+ "void bufferedAudioEngine_readSoundCheck(FigEndpointStreamAudioEngineRef)"
+ "void manager_brokerManagerGetBrokerGroupInfoCallback(CFStringRef, OSStatus, CFDictionaryRef)"
+ "void mfiMutualAuth_handleSecureTunnelCallback(APAuthenticationClientRef, CFDataRef)"
- "745.13.4"
- "<APPairingClientMFi4 for '%@'>"
- "APPairingClientMFi4"
- "APPairingClientMFi4Create"
- "APiAPCopyAuthenticationCertificateSerial_block_invoke"
- "APiAPHelperCreate"
- "APiAPHelperCreate[%{ptr}] Created, idType:%s\n"
- "APiAPHelperForwardData_block_invoke"
- "APiAPHelperSecureTunnelDataSend_block_invoke"
- "APiAPHelperSetAuthStatusHandler"
- "APiAPHelperSetAuthStatusHandler_block_invoke"
- "APiAPHelperSetDataHandler"
- "APiAPHelperSetDataHandler_block_invoke"
- "APiAPHelperSetSecureTunnelDataReceiveHandler"
- "APiAPHelperSetSecureTunnelDataReceiveHandler_block_invoke"
- "APiAPHelper[%{ptr}] AuthStatusDidChangeHandler, authenticated: %d\n"
- "APiAPHelper[%{ptr}] Finalizing\n"
- "APiAPHelper[%{ptr}] Received %u bytes of data from receiver\n"
- "APiAPHelper[%{ptr}] Received %u bytes of decrypted data from SecureTunnel\n"
- "APiAPHelper[%{ptr}] Sending %u bytes of data to receiver\n"
- "APiAPHelper[%{ptr}] Sent %u bytes of data to SecureTunnel to encrypt\n"
- "APiAPHelper[%{ptr}] Setting %s property\n"
- "AirPlay/745.13.4"
- "AuthError"
- "AuthRequestID"
- "AuthResponseReceived"
- "AuthenticateDiscoveryBroker"
- "BAE [%{ptr}] %s[0x%04X] RemoteMediaTimebase started. First audible time relative to now: %1.3f \n"
- "BAE [%{ptr}] %s[0x%04X] SetRate 1 FAILURE for hose [%{ptr}] err = %d\n"
- "Boolean mfi4Pairing_IsPeerKnown(APPairingClientRef)"
- "OSStatus APAuthenticationClientMFiMutualAuthCreate(CFAllocatorRef, FigTransportStreamRef, CFTypeRef, APAuthenticationClientRef *)"
- "OSStatus APPairingClientCoreUtilsCreate(CFAllocatorRef, CFStringRef, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, CFStringRef, FigTransportStreamRef, const APPairingClientSecureMessagingDelegate *, APPairingClientRef *)"
- "OSStatus APPairingClientCoreUtilsPatchPairedPeerDescriptionWithWoLInfo(CFTypeRef, CFDictionaryRef, CFTypeRef *)"
- "OSStatus APPairingClientMFi4Create(CFAllocatorRef, CFStringRef, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, CFStringRef, FigTransportStreamRef, CFTypeRef, APPairingClientRef *)"
- "OSStatus APiAPHelperCreate(CFAllocatorRef, const char *, CFDataRef, APiAPHelperRef *)"
- "OSStatus APiAPHelperForwardData(APiAPHelperRef, CFDataRef)_block_invoke"
- "OSStatus APiAPHelperSecureTunnelDataSend(APiAPHelperRef, CFDataRef)_block_invoke"
- "OSStatus APiAPHelperSetAuthStatusHandler(APiAPHelperRef, APiAPHelperAuthStatusHandler)_block_invoke_2"
- "OSStatus APiAPHelperSetDataHandler(APiAPHelperRef, CFStringRef, ACCEndpoint_Protocol_t, APiAPHelperDataHandler)_block_invoke"
- "OSStatus APiAPHelperSetDataHandler(APiAPHelperRef, CFStringRef, ACCEndpoint_Protocol_t, APiAPHelperDataHandler)_block_invoke_2"
- "OSStatus APiAPHelperSetSecureTunnelDataReceiveHandler(APiAPHelperRef, APiAPHelperSecureTunnelDataReceiveHandler)_block_invoke_2"
- "OSStatus apsession_createPairingClient(APSenderSessionRef, Boolean, Boolean, Boolean, Boolean, APPairingClientRef *)"
- "OSStatus audioStream_setupAudioStream(FigEndpointStreamRef, APSenderSessionRef, Boolean, APSAudioFormatDescriptionRef, CFDataRef, CFStringRef, Boolean, Boolean, uint64_t, CFStringRef, CFNumberRef, CFStringRef, CFStringRef, Boolean, Boolean, CFDataRef, uint64_t *, Boolean *, int *, int32_t *, int *, CFDataRef *)"
- "OSStatus carEndpoint_setUpAPiAPHelperForIdType(FigEndpointRef, CFStringRef, Boolean)_block_invoke"
- "OSStatus manager_handleAuthenticateDiscoveryBroker(CFStringRef, CFDictionaryRef, CFDictionaryRef *)"
- "OSStatus mfiMutualAuth_sendMessageMFi4(APAuthenticationClientRef, CFDataRef, CMBlockBufferRef *)"
- "Patched up info: %@\n"
- "Post AuthResponseReceived event with payload %@\n"
- "ProcessingDecryptionCallback"
- "ProcessingEncryptionCallback"
- "Received command %'@ with payload: %@\n"
- "WaitingForDecryptionCallback"
- "WaitingForEncryptionCallback"
- "[%{ptr}] APPairingClientCoreUtils created %c%c%c%c%c%c%c%c.\n"
- "[%{ptr}] APPairingClientMFi4 created\n"
- "[%{ptr}] Authentication Exchange for a message is completed and signaled from the APiAPHelper callback\n"
- "[%{ptr}] Authentication Exchange is started, awaiting first callback from iAPHelper\n"
- "[%{ptr}] Created %s Pair-verify session [%{ptr}]\n"
- "[%{ptr}] DataHandler called unexpectedly during Authentication with inData = %@\n"
- "[%{ptr}] DataHandler called unexpectedly during Encryption with inData = %@\n"
- "[%{ptr}] Enabling core captures on receiver. \n"
- "[%{ptr}] Forwarding %zu bytes to iAPHelper\n"
- "[%{ptr}] Forwarding %zu bytes to iAPHelper (Crypto Operation: %d), data = %@\n"
- "[%{ptr}] Initializing MFi4 Authentication (iAPHelper: %p)\n"
- "[%{ptr}] Registering incoming RCS with commChannelID [%@] from subEndpoint [%@]\n"
- "[%{ptr}] Returning existing RCS session: %@\n"
- "[%{ptr}] SecureTunnel operation for a message has completed and signaled from the APiAPHelper callback\n"
- "[%{ptr}] SecureTunnelDataReceiveHandler called unexpectedly, dataReceived = %@\n"
- "[%{ptr}] SecureTunnelDataReceiveHandler called with inData = %@\n"
- "[%{ptr}] mfi4Pairing_IsPeerKnown: %d\n"
- "[%{ptr}] mfiMutualAuth_copyAuthenticationData, authenticationData: %@\n"
- "carEndpoint_setUpAPiAPHelperForIdType"
- "com.apple.APiAPHelper"
- "com.apple.APiAPHelperMFi4Authentication"
- "com.apple.APiAPHelperProtocolData1"
- "com.apple.APiAPHelperProtocolData2"
- "coreUtilsPairing_processMessageAndTransformIfNeeded"
- "label"
- "manager_handleAuthenticateDiscoveryBroker"
- "mfi4Pairing_CopyProperty"
- "mfi4Pairing_DeriveKey"
- "mfi4Pairing_PerformSetup"
- "mfi4Pairing_PerformVerification"
- "mfi4Pairing_ensureAuthenticated"
- "mfi4Pairing_handleCreateDecryptedMessage"
- "mfi4Pairing_handleCreateEncryptedMessage"
- "setLabel:"
- "void audioStream_enableReceiverCoreCaptures(FigEndpointStreamRef, CFDictionaryRef)"
- "void bufferedAudioEngine_hoseSetRateOrGetAnchorHitMaxRetries(FigEndpointStreamAudioEngineRef, APSEndpointStreamAudioHoseRef, OSStatus)"
- "void iAPHelperFinalize(CFTypeRef)"
- "void mfiMutualAuth_handleEncryptionCallback(APAuthenticationClientRef, CFDataRef)"

```
