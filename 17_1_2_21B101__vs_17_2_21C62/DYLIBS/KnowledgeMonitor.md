## KnowledgeMonitor

> `/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor`

```diff

-442.3.1.0.0
-  __TEXT.__text: 0x2dc78
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x2b54
+442.3.2.0.0
+  __TEXT.__text: 0x2e078
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_methlist: 0x2b64
   __TEXT.__const: 0x1a0
   __TEXT.__gcc_except_tab: 0x66c
-  __TEXT.__cstring: 0x3641
-  __TEXT.__oslogstring: 0x243e
+  __TEXT.__cstring: 0x2bdd
+  __TEXT.__oslogstring: 0x251e
   __TEXT.__dlopen_cstrs: 0x49
-  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__unwind_info: 0xbe0
   __TEXT.__objc_classname: 0x607
-  __TEXT.__objc_methname: 0x8abc
+  __TEXT.__objc_methname: 0x8cba
   __TEXT.__objc_methtype: 0xd4a
-  __TEXT.__objc_stubs: 0x6e20
+  __TEXT.__objc_stubs: 0x6f80
   __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x920
+  __DATA_CONST.__const: 0x8a8
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3c50
-  __DATA_CONST.__objc_selrefs: 0x2198
+  __DATA_CONST.__objc_const: 0x3c30
+  __DATA_CONST.__objc_selrefs: 0x21f0
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__cfstring: 0x1ee0
+  __AUTH_CONST.__cfstring: 0x1f60
   __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_const: 0x1a18
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__auth_got: 0x5f8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0x480
+  __DATA.__objc_classrefs: 0x488
   __DATA.__objc_superrefs: 0x158
-  __DATA.__objc_ivar: 0x348
+  __DATA.__objc_ivar: 0x344
   __DATA.__data: 0x548
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xe10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1227
-  Symbols:   4542
-  CStrings:  2244
+  Functions: 1221
+  Symbols:   4536
+  CStrings:  2241
 
Symbols:
+ +[_DKNowPlayingMonitor _bmEventWithDKEvent:outputDevices:biomeEventMetadata:]
+ +[_DKNowPlayingMonitor _bmEventWithDKEvent:outputDevices:biomeEventMetadata:].cold.1
+ GCC_except_table20
+ GCC_except_table25
+ GCC_except_table34
+ _OBJC_CLASS_$_BMMediaNowPlaying
+ _OBJC_CLASS_$_BMMediaNowPlayingOutputDevice
+ _OBJC_CLASS_$_MRDeviceInfoRequest
+ _OBJC_IVAR_$__DKNowPlayingMonitor._previousBiomeEventMetadata
+ ___23-[_DKMonitor saveState]_block_invoke.cold.1
+ ___31-[_DKSunriseSunsetMonitor init]_block_invoke.32
+ ___31-[_DKSunriseSunsetMonitor init]_block_invoke_2.33
+ ___32-[_DKBluetoothMonitor saveState]_block_invoke.cold.1
+ ___32-[_DKBluetoothMonitor saveState]_block_invoke.cold.2
+ ___37-[_DKStarkMonitor sessionDidConnect:]_block_invoke.cold.1
+ ___40-[_DKStarkMonitor sessionDidDisconnect:]_block_invoke.cold.1
+ ___46-[_DKMotionMonitor computeDominantMotionState]_block_invoke.47
+ ___51-[_DKMonitor setCurrentEvent:inferHistoricalState:]_block_invoke.cold.1
+ ___63-[_DKNowPlayingMonitor _nowPlayingInfoDidChange:outputDevices:]_block_invoke.63
+ ___63-[_DKNowPlayingMonitor _nowPlayingInfoDidChange:outputDevices:]_block_invoke_2.65
+ ___76-[_DKUserIsFirstBacklightOnAfterWakeupMonitor registerHandleBacklightEvents]_block_invoke.145
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_literal_global.154
+ ___block_literal_global.156
+ ___block_literal_global.48
+ ___cd_dispatch_async_capture_tx_block_invoke
+ _objc_msgSend$Media
+ _objc_msgSend$NowPlaying
+ _objc_msgSend$_bmEventWithDKEvent:outputDevices:biomeEventMetadata:
+ _objc_msgSend$elapsed
+ _objc_msgSend$hasAirPlayActive
+ _objc_msgSend$hasParentGroupContainsDiscoverableGroupLeader
+ _objc_msgSend$initWithType:subType:outputDeviceID:
+ _objc_msgSend$initWithUniqueID:absoluteTimestamp:playbackState:album:artist:duration:genre:title:elapsed:mediaType:iTunesStoreIdentifier:iTunesSubscriptionIdentifier:isAirPlayVideo:outputDevices:bundleID:iTunesArtistIdentifier:iTunesAlbumIdentifier:groupIdentifier:isRemoteControl:itemMediaType:itemMediaSubtype:isAirPlayActive:parentGroupContainsDiscoverableGroupLeader:
+ _objc_msgSend$isAirPlayActive
+ _objc_msgSend$itemID
+ _objc_msgSend$localDeviceInfo
+ _objc_msgSend$parentGroupContainsDiscoverableGroupLeader
- GCC_except_table27
- GCC_except_table36
- _OBJC_CLASS_$_BMNowPlayingEvent
- _OBJC_CLASS_$_BMStreams
- _OBJC_IVAR_$__DKNowPlayingMonitor._previousAlbumStoreIdentifier
- _OBJC_IVAR_$__DKNowPlayingMonitor._previousArtistStoreIdentifier
- ___23-[_DKMonitor saveState]_block_invoke_2
- ___23-[_DKMonitor saveState]_block_invoke_2.cold.1
- ___25-[_DKMotionMonitor start]_block_invoke_4
- ___28-[_DKCalendarMonitor update]_block_invoke_2
- ___30-[_DKOrientationMonitor start]_block_invoke_3
- ___31-[_DKSunriseSunsetMonitor init]_block_invoke.33
- ___31-[_DKSunriseSunsetMonitor init]_block_invoke_2.35
- ___31-[_DKSunriseSunsetMonitor init]_block_invoke_3.36
- ___31-[_DKSunriseSunsetMonitor init]_block_invoke_4
- ___32-[_DKBluetoothMonitor saveState]_block_invoke_2
- ___32-[_DKBluetoothMonitor saveState]_block_invoke_2.cold.1
- ___32-[_DKBluetoothMonitor saveState]_block_invoke_2.cold.2
- ___37-[_DKStarkMonitor sessionDidConnect:]_block_invoke_2
- ___37-[_DKStarkMonitor sessionDidConnect:]_block_invoke_2.cold.1
- ___38-[_DKDeviceActivityLevelMonitor start]_block_invoke_7
- ___40-[_DKStarkMonitor sessionDidDisconnect:]_block_invoke_2
- ___40-[_DKStarkMonitor sessionDidDisconnect:]_block_invoke_2.cold.1
- ___46-[_DKMotionMonitor computeDominantMotionState]_block_invoke.48
- ___48-[_DKBluetoothMonitor receiveNotificationEvent:]_block_invoke_2
- ___48-[_DKNetworkQualityMonitor didStartTrackingNOI:]_block_invoke_2
- ___51-[_DKMonitor setCurrentEvent:inferHistoricalState:]_block_invoke_2.cold.1
- ___51-[_DKMonitor setCurrentEvent:inferHistoricalState:]_block_invoke_3
- ___58-[_DKAppInstallMonitor _applicationsDidChange:didInstall:]_block_invoke_2
- ___61-[_DKNotificationKeybagLockMonitor receiveNotificationEvent:]_block_invoke_2
- ___62-[_DKSunriseSunsetMonitor locationManager:didUpdateLocations:]_block_invoke_2
- ___63-[_DKNowPlayingMonitor _nowPlayingInfoDidChange:outputDevices:]_block_invoke.52
- ___63-[_DKNowPlayingMonitor _nowPlayingInfoDidChange:outputDevices:]_block_invoke_2.54
- ___66-[_DKUserIsFirstBacklightOnAfterWakeupMonitor showUINotification:]_block_invoke_2
- ___68-[_DKNotificationScreenLockImputedMonitor receiveNotificationEvent:]_block_invoke_2
- ___72-[_DKSunriseSunsetMonitor locationManager:didChangeAuthorizationStatus:]_block_invoke_2
- ___72-[_DKUserIsFirstBacklightOnAfterWakeupMonitor receiveNotificationEvent:]_block_invoke_2
- ___75-[_DKNetworkQualityMonitor observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
- ___76-[_DKUserIsFirstBacklightOnAfterWakeupMonitor registerHandleBacklightEvents]_block_invoke.147
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
- ___block_literal_global.155
- ___block_literal_global.157
- ___block_literal_global.50
- _objc_msgSend$initWithDKEvent:outputDevices:iTunesArtistIdentifier:iTunesAlbumIdentifier:
- _objc_retain_x9
CStrings:
+ "\x02\x11"
+ "-[_DKMonitor saveState]_block_invoke"
+ "-[_DKStarkMonitor sessionDidConnect:]_block_invoke"
+ "-[_DKStarkMonitor sessionDidDisconnect:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNowPlayingMonitor.m:475"
+ "BMMediaNowPlaying: unable to convert MRPlaybackState enum value: %@"
+ "BMMediaNowPlayingOutputDeviceSubType: Unrecognized value for outputSubtype: %ld"
+ "BMMediaNowPlayingOutputDeviceType: Unrecognized value for outputDevice: %ld"
+ "Media"
+ "_bmEventWithDKEvent:outputDevices:biomeEventMetadata:"
+ "_previousBiomeEventMetadata"
+ "cd_dispatch_async_tx"
+ "elapsed"
+ "hasAirPlayActive"
+ "hasParentGroupContainsDiscoverableGroupLeader"
+ "iTunesAlbumIdentifierKey"
+ "iTunesArtistIdentifierKey"
+ "initWithType:subType:outputDeviceID:"
+ "initWithUniqueID:absoluteTimestamp:playbackState:album:artist:duration:genre:title:elapsed:mediaType:iTunesStoreIdentifier:iTunesSubscriptionIdentifier:isAirPlayVideo:outputDevices:bundleID:iTunesArtistIdentifier:iTunesAlbumIdentifier:groupIdentifier:isRemoteControl:itemMediaType:itemMediaSubtype:isAirPlayActive:parentGroupContainsDiscoverableGroupLeader:"
+ "isAirPlayActive"
+ "itemID"
+ "localDeviceInfo"
+ "parentGroupContainsDiscoverableGroupLeader"
- "\x03\x11"
- "-[_DKMonitor saveState]_block_invoke_2"
- "-[_DKStarkMonitor sessionDidConnect:]_block_invoke_2"
- "-[_DKStarkMonitor sessionDidDisconnect:]_block_invoke_2"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKAppInstallMonitor.m:225"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBluetoothMonitor.m:588"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBluetoothMonitor.m:679"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKCalendarMonitor.m:141"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKDeviceActivityLevelMonitor.m:206"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKMotionMonitor.m:222"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNetworkQualityMonitor.m:208"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNetworkQualityMonitor.m:262"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNotificationKeybagLockMonitor.m:276"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNotificationMonitor.m:315"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNowPlayingMonitor.m:472"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKOrientationMonitor.m:109"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKStarkMonitor.m:110"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKStarkMonitor.m:120"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKSunriseSunsetMonitor.m:113"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKSunriseSunsetMonitor.m:145"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKSunriseSunsetMonitor.m:395"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKSunriseSunsetMonitor.m:406"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKUserIsFirstBacklightOnAfterWakeupMonitor.m:367"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKUserIsFirstBacklightOnAfterWakeupMonitor.m:463"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/_DKMonitor.m:150"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/_DKMonitor.m:309"
- "_previousAlbumStoreIdentifier"
- "_previousArtistStoreIdentifier"
- "initWithDKEvent:outputDevices:iTunesArtistIdentifier:iTunesAlbumIdentifier:"

```
