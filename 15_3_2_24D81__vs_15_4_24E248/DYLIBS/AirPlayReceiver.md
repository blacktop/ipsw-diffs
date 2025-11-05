## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/Versions/A/AirPlayReceiver`

```diff

-845.5.1.0.0
-  __TEXT.__text: 0xd261c
+850.19.1.0.0
+  __TEXT.__text: 0xd2cc4
   __TEXT.__auth_stubs: 0x3370
-  __TEXT.__objc_methlist: 0x790
+  __TEXT.__objc_methlist: 0x8e4
   __TEXT.__const: 0xd2c5
-  __TEXT.__gcc_except_tab: 0x3c0
-  __TEXT.__cstring: 0x27368
-  __TEXT.__unwind_info: 0x1020
+  __TEXT.__dlopen_cstrs: 0xad
+  __TEXT.__gcc_except_tab: 0x710
+  __TEXT.__cstring: 0x27556
+  __TEXT.__unwind_info: 0x1080
   __TEXT.__objc_classname: 0x12c
   __TEXT.__objc_methname: 0x1e06
   __TEXT.__objc_methtype: 0x1480
   __TEXT.__objc_stubs: 0x1e60
   __DATA_CONST.__got: 0x718
-  __DATA_CONST.__const: 0x15a8
+  __DATA_CONST.__const: 0x15d8
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x840
+  __DATA_CONST.__objc_selrefs: 0x8d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x19c8
-  __AUTH_CONST.__const: 0x4b68
-  __AUTH_CONST.__cfstring: 0x9ae0
-  __AUTH_CONST.__objc_const: 0x15b0
+  __AUTH_CONST.__const: 0x4b28
+  __AUTH_CONST.__cfstring: 0x9be0
+  __AUTH_CONST.__objc_const: 0x1338
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x320
-  __AUTH.__data: 0x160
   __DATA.__objc_ivar: 0x14c
   __DATA.__data: 0x17410
-  __DATA.__bss: 0xeb8
+  __DATA.__bss: 0xf78
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/AudioUnit.framework/Versions/A/AudioUnit
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio

   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/Versions/A/DiagnosticExtensions
   - /System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience
   - /System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FD472A39-B8B3-3470-AB80-86215F9DA1D8
-  Functions: 1290
+  UUID: 4919BB3C-EB46-338F-AD24-9D405A2C26B1
+  Functions: 1264
   Symbols:   3275
-  CStrings:  5846
+  CStrings:  5861
 
Symbols:
+ APReceiverRequestProcessorCopyProperty.3349
+ APReceiverRequestProcessorCopyProperty.6226
+ APReceiverRequestProcessorCopyProperty.6682
+ APReceiverRequestProcessorSetProperty.3858
+ CMBaseObjectNotificationBarrier.2752
+ GCC_except_table1007
+ GCC_except_table1009
+ GCC_except_table104
+ GCC_except_table105
+ GCC_except_table110
+ GCC_except_table115
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table125
+ GCC_except_table137
+ GCC_except_table138
+ GCC_except_table155
+ GCC_except_table166
+ GCC_except_table182
+ GCC_except_table188
+ GCC_except_table189
+ GCC_except_table193
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table366
+ GCC_except_table37
+ GCC_except_table409
+ GCC_except_table426
+ GCC_except_table46
+ GCC_except_table475
+ GCC_except_table479
+ GCC_except_table486
+ GCC_except_table494
+ GCC_except_table51
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table62
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table72
+ GCC_except_table83
+ GCC_except_table84
+ GCC_except_table873
+ GCC_except_table892
+ GCC_except_table90
+ GCC_except_table943
+ GCC_except_table947
+ GCC_except_table95
+ GCC_except_table97
+ GCC_except_table99
+ GCC_except_table999
+ MediaRemoteLibraryCore.frameworkLibrary
+ NearbyInteractionLibraryCore.frameworkLibrary
+ _APReceiverMediaRemoteXPCService_enqueueAndPostEvent
+ _APSIsRestrictiveHKAccessControl
+ _FigCFArrayGetFirstValue
+ _Finalize.5534
+ _GetTypeID.5531
+ _MediaRemoteLibrary
+ _NearbyInteractionLibrary
+ __Block_byref_object_copy_.89
+ __Block_byref_object_dispose_.90
+ __IsRequestUnrestricted
+ ___MediaRemoteLibraryCore_block_invoke
+ ___NearbyInteractionLibraryCore_block_invoke
+ ___getMRMediaRemoteAddCommandHandlerBlockForPlayerSymbolLoc_block_invoke
+ ___getMRMediaRemoteBroadcastCommandSymbolLoc_block_invoke
+ ___getMRMediaRemoteCommandInfoCreateFromExternalRepresentationSymbolLoc_block_invoke
+ ___getMRMediaRemoteCommandInfoCreateSymbolLoc_block_invoke
+ ___getMRMediaRemoteCommandInfoSetCommandSymbolLoc_block_invoke
+ ___getMRMediaRemoteCommandInfoSetEnabledSymbolLoc_block_invoke
+ ___getMRMediaRemoteGetLocalOriginSymbolLoc_block_invoke
+ ___getMRMediaRemoteGetNowPlayingInfoForPlayerSymbolLoc_block_invoke
+ ___getMRMediaRemoteRemoveCommandHandlerBlockForPlayerSymbolLoc_block_invoke
+ ___getMRMediaRemoteRemovePlayerSymbolLoc_block_invoke
+ ___getMRMediaRemoteSetCanBeNowPlayingApplicationSymbolLoc_block_invoke
+ ___getMRMediaRemoteSetCanBeNowPlayingForPlayerSymbolLoc_block_invoke
+ ___getMRMediaRemoteSetNowPlayingApplicationOverrideEnabledSymbolLoc_block_invoke
+ ___getMRMediaRemoteSetNowPlayingInfoForPlayerSymbolLoc_block_invoke
+ ___getMRMediaRemoteSetNowPlayingPlayerSymbolLoc_block_invoke
+ ___getMRMediaRemoteSetPlaybackStateForPlayerSymbolLoc_block_invoke
+ ___getMRMediaRemoteSetSupportedCommandsForPlayerSymbolLoc_block_invoke
+ ___getMRMediaRemoteSyncClientPropertiesSymbolLoc_block_invoke
+ ___getMRNowPlayingClientCreateFromExternalRepresentationSymbolLoc_block_invoke
+ ___getMRNowPlayingSessionManagerActiveSessionWillBeHijackedByNativePlaybackSymbolLoc_block_invoke
+ ___getMRNowPlayingSessionManagerIsSilentPrimaryDidChangeSymbolLoc_block_invoke
+ ___getMRNowPlayingSessionManagerIsSilentPrimarySymbolLoc_block_invoke
+ ___getMRNowPlayingSessionManagerLocalDeviceRoutingContextIDDidChangeSymbolLoc_block_invoke
+ ___getMRNowPlayingSessionManagerLocalDeviceRoutingContextIDSymbolLoc_block_invoke
+ ___getMRNowPlayingSessionManagerStartSessionSymbolLoc_block_invoke
+ ___getMRNowPlayingSessionManagerStopSessionSymbolLoc_block_invoke
+ ___getMRPlayerClass_block_invoke
+ ___getMRPlayerPathClass_block_invoke
+ ___getNISessionClass_block_invoke
+ ___getNISpatialBrowsingConfigurationClass_block_invoke
+ ___getkMRMediaRemoteMediaTypeMusicSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoAlbumSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoArtistSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoArtworkDataSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoArtworkMIMETypeSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoDurationSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoElapsedTimeSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoMediaTypeSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoPlaybackRateSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoTitleSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoTotalTrackCountSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoTrackNumberSymbolLoc_block_invoke
+ ___getkMRMediaRemoteNowPlayingInfoUniqueIdentifierSymbolLoc_block_invoke
+ ___getkMRMediaRemoteOptionRemoteControlInterfaceIdentifierSymbolLoc_block_invoke
+ __block_descriptor_tmp.167.5432
+ __block_descriptor_tmp.168
+ __block_descriptor_tmp.1945
+ __block_descriptor_tmp.2680
+ __block_descriptor_tmp.2745
+ __block_descriptor_tmp.2893
+ __block_descriptor_tmp.3101
+ __block_descriptor_tmp.3217
+ __block_descriptor_tmp.3344
+ __block_descriptor_tmp.346
+ __block_descriptor_tmp.4623
+ __block_descriptor_tmp.5129
+ __block_descriptor_tmp.5308
+ __block_descriptor_tmp.6207
+ __block_descriptor_tmp.6297
+ __block_descriptor_tmp.642
+ __block_descriptor_tmp.6607
+ __block_descriptor_tmp.809
+ __block_literal_global.1331
+ __block_literal_global.144
+ __block_literal_global.155
+ __block_literal_global.1778
+ __block_literal_global.2071
+ __block_literal_global.2678
+ __block_literal_global.3099
+ __block_literal_global.3215
+ __block_literal_global.342
+ __block_literal_global.384
+ __block_literal_global.4878
+ __block_literal_global.5067
+ __block_literal_global.5127
+ __block_literal_global.6281
+ __block_literal_global.6605
+ __block_literal_global.807
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringMediaRemote
+ _audit_stringNearbyInteraction
+ _dlerror
+ _soft_MRMediaRemoteSetCanBeNowPlayingApplication
+ _soft_MRMediaRemoteSetCanBeNowPlayingForPlayer
+ _soft_MRMediaRemoteSetNowPlayingApplicationOverrideEnabled
+ _sysInfo_cancelPINUpdate
+ _sysInfo_schedulePINUpdate
+ audioSession_audioDecoderDecodeCallback.5393
+ audioSession_audioDecoderDecodeFrame.5380
+ audioSession_handleMediaDataControlRequest.3113
+ audioSession_handleMediaDataControlRequest.5282
+ audioSession_log.5405
+ audioSession_networkThread.5415
+ audioSession_performPeriodicTasks.5410
+ audioSession_sessionLock.5312
+ audioSession_sessionUnlock.5314
+ gAPReceiverMediaRemoteService.3
+ gAPReceiverMediaRemoteService.4
+ gAPReceiverMediaRemoteService.5
+ gAirTunesRelativeTimeOffset.5435
+ getMRMediaRemoteAddCommandHandlerBlockForPlayerSymbolLoc.ptr
+ getMRMediaRemoteBroadcastCommandSymbolLoc.ptr
+ getMRMediaRemoteCommandInfoCreateFromExternalRepresentationSymbolLoc.ptr
+ getMRMediaRemoteCommandInfoCreateSymbolLoc.ptr
+ getMRMediaRemoteCommandInfoSetCommandSymbolLoc.ptr
+ getMRMediaRemoteCommandInfoSetEnabledSymbolLoc.ptr
+ getMRMediaRemoteGetLocalOriginSymbolLoc.ptr
+ getMRMediaRemoteGetNowPlayingInfoForPlayerSymbolLoc.ptr
+ getMRMediaRemoteRemoveCommandHandlerBlockForPlayerSymbolLoc.ptr
+ getMRMediaRemoteRemovePlayerSymbolLoc.ptr
+ getMRMediaRemoteSetCanBeNowPlayingApplicationSymbolLoc.ptr
+ getMRMediaRemoteSetCanBeNowPlayingForPlayerSymbolLoc.ptr
+ getMRMediaRemoteSetNowPlayingApplicationOverrideEnabledSymbolLoc.ptr
+ getMRMediaRemoteSetNowPlayingInfoForPlayerSymbolLoc.ptr
+ getMRMediaRemoteSetNowPlayingPlayerSymbolLoc.ptr
+ getMRMediaRemoteSetPlaybackStateForPlayerSymbolLoc.ptr
+ getMRMediaRemoteSetSupportedCommandsForPlayerSymbolLoc.ptr
+ getMRMediaRemoteSyncClientPropertiesSymbolLoc.ptr
+ getMRNowPlayingClientCreateFromExternalRepresentationSymbolLoc.ptr
+ getMRNowPlayingSessionManagerActiveSessionWillBeHijackedByNativePlaybackSymbolLoc.ptr
+ getMRNowPlayingSessionManagerIsSilentPrimaryDidChangeSymbolLoc.ptr
+ getMRNowPlayingSessionManagerIsSilentPrimarySymbolLoc.ptr
+ getMRNowPlayingSessionManagerLocalDeviceRoutingContextIDDidChangeSymbolLoc.ptr
+ getMRNowPlayingSessionManagerLocalDeviceRoutingContextIDSymbolLoc.ptr
+ getMRNowPlayingSessionManagerStartSessionSymbolLoc.ptr
+ getMRNowPlayingSessionManagerStopSessionSymbolLoc.ptr
+ getMRPlayerClass.softClass
+ getMRPlayerPathClass.softClass
+ getNISessionClass.softClass
+ getNISpatialBrowsingConfigurationClass.softClass
+ getkMRMediaRemoteMediaTypeMusicSymbolLoc.ptr
+ getkMRMediaRemoteNowPlayingInfoAlbumSymbolLoc.ptr
+ getkMRMediaRemoteNowPlayingInfoArtistSymbolLoc.ptr
+ getkMRMediaRemoteNowPlayingInfoArtworkDataSymbolLoc.ptr
+ getkMRMediaRemoteNowPlayingInfoArtworkMIMETypeSymbolLoc.ptr
+ getkMRMediaRemoteNowPlayingInfoDurationSymbolLoc.ptr
+ getkMRMediaRemoteNowPlayingInfoElapsedTimeSymbolLoc.ptr
+ getkMRMediaRemoteNowPlayingInfoMediaTypeSymbolLoc.ptr
+ getkMRMediaRemoteNowPlayingInfoPlaybackRateSymbolLoc.ptr
+ getkMRMediaRemoteNowPlayingInfoTitleSymbolLoc.ptr
+ getkMRMediaRemoteNowPlayingInfoTotalTrackCountSymbolLoc.ptr
+ getkMRMediaRemoteNowPlayingInfoTrackNumberSymbolLoc.ptr
+ getkMRMediaRemoteNowPlayingInfoUniqueIdentifierSymbolLoc.ptr
+ getkMRMediaRemoteOptionRemoteControlInterfaceIdentifierSymbolLoc.ptr
+ kAPRRemoteControlSessionMediaRemoteVTable.2719
+ kAPRRemoteControlSessionMediaRemote_Class.2735
+ kAPRRemoteControlSessionSession_BaseClassWrapper.2750
- APReceiverRequestProcessorCopyProperty.3338
- APReceiverRequestProcessorCopyProperty.6200
- APReceiverRequestProcessorCopyProperty.6656
- APReceiverRequestProcessorSetProperty.3848
- CMBaseObjectNotificationBarrier.2746
- GCC_except_table1006
- GCC_except_table1014
- GCC_except_table1016
- GCC_except_table108
- GCC_except_table135
- GCC_except_table175
- GCC_except_table191
- GCC_except_table197
- GCC_except_table198
- GCC_except_table202
- GCC_except_table375
- GCC_except_table418
- GCC_except_table435
- GCC_except_table484
- GCC_except_table488
- GCC_except_table493
- GCC_except_table501
- GCC_except_table880
- GCC_except_table899
- GCC_except_table950
- GCC_except_table954
- MediaRemoteLibrary.sLib
- MediaRemoteLibrary.sOnce
- NearbyInteractionLibrary.sLib
- NearbyInteractionLibrary.sOnce
- _DataBuffer_AppendFile
- _DataBuffer_Commit
- _DataBuffer_RunProcessAndAppendOutput
- _Finalize.5524
- _GetTypeID.5521
- _MRNowPlayingSessionManagerActiveSessionWillBeHijackedByNativePlaybackFunction
- _MRNowPlayingSessionManagerIsSilentPrimaryDidChangeFunction
- _MRNowPlayingSessionManagerLocalDeviceRoutingContextIDDidChangeFunction
- _MRPlayerFunction
- _MRPlayerPathFunction
- _NISessionFunction
- _NISpatialBrowsingConfigurationFunction
- __RequestProcessorHandler
- ___MediaRemoteLibrary_block_invoke
- ___NearbyInteractionLibrary_block_invoke
- __block_descriptor_tmp.164
- __block_descriptor_tmp.165
- __block_descriptor_tmp.1925
- __block_descriptor_tmp.2674
- __block_descriptor_tmp.2739
- __block_descriptor_tmp.2886
- __block_descriptor_tmp.3089
- __block_descriptor_tmp.3205
- __block_descriptor_tmp.3332
- __block_descriptor_tmp.342
- __block_descriptor_tmp.4613
- __block_descriptor_tmp.5120
- __block_descriptor_tmp.5299
- __block_descriptor_tmp.6181
- __block_descriptor_tmp.6271
- __block_descriptor_tmp.639
- __block_descriptor_tmp.6581
- __block_descriptor_tmp.766
- __block_literal_global.126
- __block_literal_global.1289
- __block_literal_global.142
- __block_literal_global.151
- __block_literal_global.1745
- __block_literal_global.2046
- __block_literal_global.2672
- __block_literal_global.3087
- __block_literal_global.3203
- __block_literal_global.338
- __block_literal_global.367
- __block_literal_global.4868
- __block_literal_global.5058
- __block_literal_global.5118
- __block_literal_global.6255
- __block_literal_global.6579
- __block_literal_global.764
- __block_literal_global.89
- _airplayReqProcessor_requestProcessGetLog
- _classMRPlayer
- _classMRPlayerPath
- _classNISession
- _classNISpatialBrowsingConfiguration
- _constantValMRNowPlayingSessionManagerActiveSessionWillBeHijackedByNativePlayback
- _constantValMRNowPlayingSessionManagerIsSilentPrimaryDidChange
- _constantValMRNowPlayingSessionManagerLocalDeviceRoutingContextIDDidChange
- _constantValkMRMediaRemoteMediaTypeMusic
- _constantValkMRMediaRemoteNowPlayingInfoAlbum
- _constantValkMRMediaRemoteNowPlayingInfoArtist
- _constantValkMRMediaRemoteNowPlayingInfoArtworkData
- _constantValkMRMediaRemoteNowPlayingInfoArtworkMIMEType
- _constantValkMRMediaRemoteNowPlayingInfoDuration
- _constantValkMRMediaRemoteNowPlayingInfoElapsedTime
- _constantValkMRMediaRemoteNowPlayingInfoMediaType
- _constantValkMRMediaRemoteNowPlayingInfoPlaybackRate
- _constantValkMRMediaRemoteNowPlayingInfoTitle
- _constantValkMRMediaRemoteNowPlayingInfoTotalTrackCount
- _constantValkMRMediaRemoteNowPlayingInfoTrackNumber
- _constantValkMRMediaRemoteNowPlayingInfoUniqueIdentifier
- _constantValkMRMediaRemoteOptionRemoteControlInterfaceIdentifier
- _dlopen
- _fmod
- _getMRPlayerClass
- _getMRPlayerPathClass
- _getNISessionClass
- _getNISpatialBrowsingConfigurationClass
- _getkMRMediaRemoteMediaTypeMusic
- _getkMRMediaRemoteNowPlayingInfoAlbum
- _getkMRMediaRemoteNowPlayingInfoArtist
- _getkMRMediaRemoteNowPlayingInfoArtworkData
- _getkMRMediaRemoteNowPlayingInfoArtworkMIMEType
- _getkMRMediaRemoteNowPlayingInfoDuration
- _getkMRMediaRemoteNowPlayingInfoElapsedTime
- _getkMRMediaRemoteNowPlayingInfoMediaType
- _getkMRMediaRemoteNowPlayingInfoPlaybackRate
- _getkMRMediaRemoteNowPlayingInfoTitle
- _getkMRMediaRemoteNowPlayingInfoTotalTrackCount
- _getkMRMediaRemoteNowPlayingInfoTrackNumber
- _initMRMediaRemoteAddCommandHandlerBlockForPlayer
- _initMRMediaRemoteBroadcastCommand
- _initMRMediaRemoteCommandInfoCreate
- _initMRMediaRemoteCommandInfoCreateFromExternalRepresentation
- _initMRMediaRemoteCommandInfoSetCommand
- _initMRMediaRemoteCommandInfoSetEnabled
- _initMRMediaRemoteGetLocalOrigin
- _initMRMediaRemoteGetNowPlayingInfoForPlayer
- _initMRMediaRemoteRemoveCommandHandlerBlockForPlayer
- _initMRMediaRemoteRemovePlayer
- _initMRMediaRemoteSetCanBeNowPlayingApplication
- _initMRMediaRemoteSetCanBeNowPlayingForPlayer
- _initMRMediaRemoteSetNowPlayingApplicationOverrideEnabled
- _initMRMediaRemoteSetNowPlayingInfoForPlayer
- _initMRMediaRemoteSetNowPlayingPlayer
- _initMRMediaRemoteSetPlaybackStateForPlayer
- _initMRMediaRemoteSetSupportedCommandsForPlayer
- _initMRMediaRemoteSyncClientProperties
- _initMRNowPlayingClientCreateFromExternalRepresentation
- _initMRNowPlayingSessionManagerIsSilentPrimary
- _initMRNowPlayingSessionManagerLocalDeviceRoutingContextID
- _initMRNowPlayingSessionManagerStartSession
- _initMRNowPlayingSessionManagerStopSession
- _initMRPlayer
- _initMRPlayerPath
- _initNISession
- _initNISpatialBrowsingConfiguration
- _initValMRNowPlayingSessionManagerActiveSessionWillBeHijackedByNativePlayback
- _initValMRNowPlayingSessionManagerIsSilentPrimaryDidChange
- _initValMRNowPlayingSessionManagerLocalDeviceRoutingContextIDDidChange
- _initValkMRMediaRemoteMediaTypeMusic
- _initValkMRMediaRemoteNowPlayingInfoAlbum
- _initValkMRMediaRemoteNowPlayingInfoArtist
- _initValkMRMediaRemoteNowPlayingInfoArtworkData
- _initValkMRMediaRemoteNowPlayingInfoArtworkMIMEType
- _initValkMRMediaRemoteNowPlayingInfoDuration
- _initValkMRMediaRemoteNowPlayingInfoElapsedTime
- _initValkMRMediaRemoteNowPlayingInfoMediaType
- _initValkMRMediaRemoteNowPlayingInfoPlaybackRate
- _initValkMRMediaRemoteNowPlayingInfoTitle
- _initValkMRMediaRemoteNowPlayingInfoTotalTrackCount
- _initValkMRMediaRemoteNowPlayingInfoTrackNumber
- _initValkMRMediaRemoteNowPlayingInfoUniqueIdentifier
- _initValkMRMediaRemoteOptionRemoteControlInterfaceIdentifier
- _kMRMediaRemoteMediaTypeMusicFunction
- _kMRMediaRemoteNowPlayingInfoAlbumFunction
- _kMRMediaRemoteNowPlayingInfoArtistFunction
- _kMRMediaRemoteNowPlayingInfoArtworkDataFunction
- _kMRMediaRemoteNowPlayingInfoArtworkMIMETypeFunction
- _kMRMediaRemoteNowPlayingInfoDurationFunction
- _kMRMediaRemoteNowPlayingInfoElapsedTimeFunction
- _kMRMediaRemoteNowPlayingInfoMediaTypeFunction
- _kMRMediaRemoteNowPlayingInfoPlaybackRateFunction
- _kMRMediaRemoteNowPlayingInfoTitleFunction
- _kMRMediaRemoteNowPlayingInfoTotalTrackCountFunction
- _kMRMediaRemoteNowPlayingInfoTrackNumberFunction
- _kMRMediaRemoteNowPlayingInfoUniqueIdentifierFunction
- _kMRMediaRemoteOptionRemoteControlInterfaceIdentifierFunction
- _softLinkMRMediaRemoteAddCommandHandlerBlockForPlayer
- _softLinkMRMediaRemoteBroadcastCommand
- _softLinkMRMediaRemoteCommandInfoCreate
- _softLinkMRMediaRemoteCommandInfoCreateFromExternalRepresentation
- _softLinkMRMediaRemoteCommandInfoSetCommand
- _softLinkMRMediaRemoteCommandInfoSetEnabled
- _softLinkMRMediaRemoteGetLocalOrigin
- _softLinkMRMediaRemoteGetNowPlayingInfoForPlayer
- _softLinkMRMediaRemoteRemoveCommandHandlerBlockForPlayer
- _softLinkMRMediaRemoteRemovePlayer
- _softLinkMRMediaRemoteSetCanBeNowPlayingApplication
- _softLinkMRMediaRemoteSetCanBeNowPlayingForPlayer
- _softLinkMRMediaRemoteSetNowPlayingApplicationOverrideEnabled
- _softLinkMRMediaRemoteSetNowPlayingInfoForPlayer
- _softLinkMRMediaRemoteSetNowPlayingPlayer
- _softLinkMRMediaRemoteSetPlaybackStateForPlayer
- _softLinkMRMediaRemoteSetSupportedCommandsForPlayer
- _softLinkMRMediaRemoteSyncClientProperties
- _softLinkMRNowPlayingClientCreateFromExternalRepresentation
- _softLinkMRNowPlayingSessionManagerIsSilentPrimary
- _softLinkMRNowPlayingSessionManagerLocalDeviceRoutingContextID
- _softLinkMRNowPlayingSessionManagerStartSession
- _softLinkMRNowPlayingSessionManagerStopSession
- audioSession_audioDecoderDecodeCallback.5384
- audioSession_audioDecoderDecodeFrame.5371
- audioSession_handleMediaDataControlRequest.3101
- audioSession_handleMediaDataControlRequest.5273
- audioSession_log.5396
- audioSession_networkThread.5406
- audioSession_performPeriodicTasks.5401
- audioSession_sessionLock.5303
- audioSession_sessionUnlock.5305
- gAirTunesRelativeTimeOffset.5425
- kAPRRemoteControlSessionMediaRemoteVTable.2713
- kAPRRemoteControlSessionMediaRemote_Class.2729
- kAPRRemoteControlSessionSession_BaseClassWrapper.2744
CStrings:
+ "### [%{ptr}] Failed to tear down session [%{ptr}]\n"
+ "### [%{ptr}] Failed to tear down session [%{ptr}] for SDP audio\n"
+ "/System/Library/Frameworks/NearbyInteraction.framework/Contents/MacOS/NearbyInteraction"
+ "/System/Library/PrivateFrameworks/MediaRemote.framework/Contents/MacOS/MediaRemote"
+ "850.19.1"
+ "Failed to post event: %'@ %#m"
+ "Failed to unregister comm channel %@: unknown comm channel ID (err %#m)"
+ "Histogram_GlitchFreeDuration"
+ "Histogram_HLANetworkTransitTime"
+ "OSStatus _GetDecryptKey(AirPlayReceiverSessionRef, CFDictionaryRef, FPSAPContextRef *, int, AirPlayEncryptionType, uint8_t *, uint8_t *)"
+ "Posted events: %d%?{end}, remaining: %d"
+ "Unable to find class %s"
+ "[%{ptr}] Control pair-verify CU, type %u, is not allowed based on access control\n"
+ "connectAck"
+ "glitchFreeDurationHistogram"
+ "glitchFreeDurationHistogramCount"
+ "receiverNetworkTransitTimeHistogram"
+ "receiverNetworkTransitTimeHistogramCount"
+ "receiver_reportRTCMetricsIntervalS"
+ "softlink:r:path:/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote"
+ "void APReceiverMediaRemoteXPCService_enqueueAndPostEvent(CFStringRef, CFDictionaryRef)"
- "### Invalid session type: %d.\n"
- "+-+ syslog +--\n"
- "/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote"
- "/System/Library/PrivateFrameworks/NearbyInteraction.framework/NearbyInteraction"
- "/log"
- "/logs"
- "/tmp/AirPlay.log"
- "845.5.1"
- "===================\n"
- "APReceiverMediaRemoteXPCService_RegisterCommChannel"
- "AirPlay Diagnostics\n"
- "OSStatus _GetDecryptKey(AirPlayReceiverSessionRef, CFDictionaryRef, FPSAPContextRef, int, AirPlayEncryptionType, uint8_t *, uint8_t *)"
- "airplayReqProcessor_requestProcessGetLog"
- "syslog"
- "text/plain"

```
