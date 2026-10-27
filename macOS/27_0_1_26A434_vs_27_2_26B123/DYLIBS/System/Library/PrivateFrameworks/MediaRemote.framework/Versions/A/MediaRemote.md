## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote`

```diff

-4026.140.2.0.0
-  __TEXT.__text: 0x3201a0
-  __TEXT.__objc_methlist: 0x2b8bc
-  __TEXT.__const: 0x5d8
-  __TEXT.__cstring: 0x2c5ce
-  __TEXT.__oslogstring: 0xd361
-  __TEXT.__gcc_except_tab: 0x5898
+4026.240.3.0.0
+  __TEXT.__text: 0x3211a8
+  __TEXT.__objc_methlist: 0x2b9a4
+  __TEXT.__const: 0x678
+  __TEXT.__cstring: 0x2c65f
+  __TEXT.__oslogstring: 0xd42d
+  __TEXT.__gcc_except_tab: 0x5934
   __TEXT.__dlopen_cstrs: 0x40b
   __TEXT.__ustring: 0x7b8
   __TEXT.__unwind_info: 0xb1c8

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4b80
+  __DATA_CONST.__const: 0x4c10
   __DATA_CONST.__objc_classlist: 0x11c0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf130
+  __DATA_CONST.__objc_selrefs: 0xf1a8
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xff0
   __DATA_CONST.__objc_arraydata: 0x260
-  __DATA_CONST.__got: 0x1420
-  __AUTH_CONST.__const: 0xa420
-  __AUTH_CONST.__cfstring: 0x23e40
-  __AUTH_CONST.__objc_const: 0x46660
+  __DATA_CONST.__got: 0x1428
+  __AUTH_CONST.__const: 0xa460
+  __AUTH_CONST.__cfstring: 0x24020
+  __AUTH_CONST.__objc_const: 0x467c8
+  __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xa90
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x8430
-  __DATA.__objc_ivar: 0x32f0
+  __AUTH.__objc_data: 0x5d20
+  __DATA.__objc_ivar: 0x3308
   __DATA.__data: 0x1a08
   __DATA.__bss: 0x8a8
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2d50
+  __DATA_DIRTY.__objc_data: 0x5460
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x5a0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 20601
-  Symbols:   35160
-  CStrings:  6512
+  Functions: 20622
+  Symbols:   35204
+  CStrings:  6529
 
Symbols:
+ +[MRCBProductInfo isWXDeviceWithModelID:]
+ -[MRAVConcreteOutputDevice supportsDiscoveredIsPlaying]
+ -[MRAVConcreteRoutingDiscoverySession detailsList]
+ -[MRAVDistantOutputDevice supportsDiscoveredIsPlaying]
+ -[MRAVEndpoint supportsDiscoveredIsPlaying]
+ -[MRAVOutputDevice isWXDevice]
+ -[MRAVOutputDevice supportsDiscoveredIsPlaying]
+ -[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]
+ -[MRCompanionLinkClientEvent setStatusFlags:]
+ -[MRCompanionLinkClientEvent statusFlags]
+ -[MRGroupComposition addHomeAccessoryWithModelIdentifier:]
+ -[MRGroupComposition homeAccessoryCount]
+ -[MRGroupComposition setHomeAccessoryCount:]
+ -[MRGroupComposition setSpeakerGroupCount:]
+ -[MRGroupComposition setTvAndSpeakerCount:]
+ -[MRGroupComposition setWalledHomeAccessoryCount:]
+ -[MRGroupComposition speakerGroupCount]
+ -[MRGroupComposition tvAndSpeakerCount]
+ -[MRGroupComposition walledHomeAccessoryCount]
+ -[MRMediaRemoteService requestPushToStartTokenWithCompletion:]
+ -[MRNowPlayingPushTokenManager requestStartToken]
+ -[MRUserSettings remoteSessionStalenessGraceInterval]
+ -[_MRCommandOptionsProtobuf hasRequestDetails]
+ -[_MRCommandOptionsProtobuf requestDetails]
+ -[_MRCommandOptionsProtobuf setRequestDetails:]
+ GCC_except_table126
+ GCC_except_table255
+ GCC_except_table287
+ GCC_except_table356
+ OBJC_IVAR_$_MRCompanionLinkClientEvent._statusFlags
+ OBJC_IVAR_$_MRGroupComposition._homeAccessoryCount
+ OBJC_IVAR_$_MRGroupComposition._speakerGroupCount
+ OBJC_IVAR_$_MRGroupComposition._tvAndSpeakerCount
+ OBJC_IVAR_$_MRGroupComposition._walledHomeAccessoryCount
+ OBJC_IVAR_$__MRCommandOptionsProtobuf._requestDetails
+ _MRAVOutputDeviceB525ModelID
+ _MRAVOutputDeviceB525ModelIDPrefix
+ _MRAVOutputDeviceJ490ModelID
+ _MRAVOutputDeviceJ491ModelID
+ _MRAVVolumeClientEndpointVolumeCategoryDidChangeNotification
+ _MRRequestDetailsInitiatorCorianderLockScreen
+ _MRRequestDetailsInitiatorNowPlayingPlatter
+ _RPOptionStatusFlags
+ __49-[MRNowPlayingPushTokenManager requestStartToken]_block_invoke
+ __72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke
+ ___49-[MRNowPlayingPushTokenManager requestStartToken]_block_invoke
+ ___50-[MRAVConcreteRoutingDiscoverySession detailsList]_block_invoke
+ ___53-[MRUserSettings remoteSessionStalenessGraceInterval]_block_invoke
+ ___62-[MRMediaRemoteService requestPushToStartTokenWithCompletion:]_block_invoke
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_2
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_3
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_4
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_5
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_6
+ ___72-[MRAVRoutingDiscoverySessionWrapper _onNotifyQueue_reevaluateAndNotify]_block_invoke_7
+ ___75-[MRActiveRoutesObserver _handleActiveSystemEndpointDidRemoveOutputDevice:]_block_invoke_3
+ ___block_descriptor_184_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r_e45_v32?0"MRAVOutputDevice"8I16I20"NSString"24l
+ ___copy_helper_block_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r
+ ___destroy_helper_block_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r
+ _objc_msgSend$_onNotifyQueue_reevaluateAndNotify
+ _objc_msgSend$addHomeAccessoryWithModelIdentifier:
+ _objc_msgSend$hasDeviceIsPlaying
+ _objc_msgSend$homeAccessoryCount
+ _objc_msgSend$isWXDeviceWithModelID:
+ _objc_msgSend$requestPushToStartTokenWithCompletion:
+ _objc_msgSend$setHomeAccessoryCount:
+ _objc_msgSend$setRequestDetails:
+ _objc_msgSend$setSpeakerGroupCount:
+ _objc_msgSend$setTvAndSpeakerCount:
+ _objc_msgSend$setWalledHomeAccessoryCount:
+ _objc_msgSend$speakerGroupCount
+ _objc_msgSend$supportsDiscoveredIsPlaying
+ _objc_msgSend$tvAndSpeakerCount
+ _objc_msgSend$walledHomeAccessoryCount
+ remoteSessionStalenessGraceInterval.__interval
+ remoteSessionStalenessGraceInterval.__once
- -[MRAVRoutingDiscoverySessionWrapper _currentVisibleEndpointsForSession:]
- -[MRAVRoutingDiscoverySessionWrapper _currentVisibleOutputDevicesForSession:]
- -[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]
- -[MRAVRoutingDiscoverySessionWrapper _shouldNotify]
- -[MRMediaRemoteService remoteSessionAssertionsWithCompletion:]
- -[MRUserSettings remoteSessionDefaultAssertionInterval]
- GCC_except_table125
- GCC_except_table254
- GCC_except_table285
- GCC_except_table355
- __58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke
- ___55-[MRUserSettings remoteSessionDefaultAssertionInterval]_block_invoke
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_2
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_3
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_4
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_5
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_6
- ___58-[MRAVRoutingDiscoverySessionWrapper _reevaluateAndNotify]_block_invoke_7
- ___62-[MRMediaRemoteService remoteSessionAssertionsWithCompletion:]_block_invoke
- ___block_descriptor_160_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r_e45_v32?0"MRAVOutputDevice"8I16I20"NSString"24l
- ___copy_helper_block_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r
- ___destroy_helper_block_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r
- _objc_msgSend$_currentVisibleEndpointsForSession:
- _objc_msgSend$_currentVisibleOutputDevicesForSession:
- _objc_msgSend$_reevaluateAndNotify
- _objc_msgSend$_shouldNotify
- _objc_msgSend$contents
- _objc_msgSend$dataByteSize
- _objc_msgSend$startOffset
- _objc_msgSend$variableFramesInPacket
- remoteSessionDefaultAssertionInterval.__interval
- remoteSessionDefaultAssertionInterval.__once
CStrings:
+ "-[MRAVOutputDevice supportsDiscoveredIsPlaying]"
+ "AudioAccessory11,"
+ "AudioAccessory11,1"
+ "CorianderLockScreen"
+ "GROUPSESSION_ROUTE_HOMEACCESSORY"
+ "GracePeriod"
+ "HomeAccessory"
+ "HomeAccessory17,1"
+ "HomeAccessory17,2"
+ "Localizable-J490"
+ "MRAVVolumeClientEndpointVolumeCategoryDidChangeNotification"
+ "NowPlayingPlatter"
+ "OB"
+ "SpeakerGroup"
+ "TVAndSpeaker"
+ "Update: %{public}@<%{public}@> localGroupID detected. Substituting picked localDevice "
+ "[MRNowPlayingPushTokenManager] requestStartToken"
+ "[MRNowPlayingPushTokenManager] requestStartToken failed: %{public}@"
+ "hifispeaker.2"
+ "homeAccessory: %lu;"
+ "remoteSessionStalenessGraceInterval"
+ "requestDetails"
+ "speakerGroup: %lu;"
+ "tv.and.hifispeaker.fill"
+ "tvAndSpeaker: %lu;"
+ "walledHomeAccessory: %lu;"
- "MRAudioDataBlock.m"
- "MRDeviceInfo *MRMediaRemoteServiceCopyDeviceInfo(MRMediaRemoteServiceRef, MRPlayerPath *__strong)"
- "O"
- "Trying to call CopyDeviceInfo from Daemon"
- "assertions"
- "invalid buffer size for decoding voice input message (%lu > (%lu * %lu))"
- "iphone"
- "packet descriptions exceed maximum packet capacity (%lu > %lu)"
- "remoteSessionDefaultAssertionInterval"
```
