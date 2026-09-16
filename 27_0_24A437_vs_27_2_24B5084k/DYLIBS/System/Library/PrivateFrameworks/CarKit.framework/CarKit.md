## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-799.3.0.0.0
-  __TEXT.__text: 0x5f6c8
+807.2.0.0.0
+  __TEXT.__text: 0x6022c
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x6354
+  __TEXT.__objc_methlist: 0x63ec
   __TEXT.__const: 0x558
-  __TEXT.__gcc_except_tab: 0x9f8
-  __TEXT.__oslogstring: 0x6ae6
-  __TEXT.__cstring: 0x5a9d
+  __TEXT.__gcc_except_tab: 0xa1c
+  __TEXT.__oslogstring: 0x6c86
+  __TEXT.__cstring: 0x5bbd
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__constg_swiftt: 0x1a0
-  __TEXT.__swift5_typeref: 0x188
+  __TEXT.__swift5_typeref: 0x17e
   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_reflstr: 0x88
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x25e0
+  __TEXT.__unwind_info: 0x2608
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2040
+  __DATA_CONST.__const: 0x20a0
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x36f0
+  __DATA_CONST.__objc_selrefs: 0x3750
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0xc0
-  __DATA_CONST.__got: 0x870
-  __AUTH_CONST.__const: 0x1bb0
-  __AUTH_CONST.__cfstring: 0x5c60
-  __AUTH_CONST.__objc_const: 0x102b8
+  __DATA_CONST.__got: 0x880
+  __AUTH_CONST.__const: 0x1bc0
+  __AUTH_CONST.__cfstring: 0x5d80
+  __AUTH_CONST.__objc_const: 0x10390
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0xac8
+  __AUTH_CONST.__auth_got: 0xae0
   __AUTH.__objc_data: 0x1400
   __AUTH.__data: 0x1b8
-  __DATA.__objc_ivar: 0x72c
-  __DATA.__data: 0x11a0
+  __DATA.__objc_ivar: 0x738
+  __DATA.__data: 0x1190
   __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3044
-  Symbols:   6002
-  CStrings:  1419
+  Functions: 3058
+  Symbols:   6033
+  CStrings:  1436
 
Symbols:
+ +[CARSession _stringForAppearanceMode:]
+ -[CARScreenInfo descriptionForScreenType]
+ -[CARSession _videoPlaybackAudioOnlyMode]
+ -[CARSession carPlaySnoopCollectionPath]
+ -[CARSession createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:sendSocketBufferSize:error:]
+ -[CARSession handleDDPChangeWithAppearance:screenID:]
+ -[CARSession lastPlayingVideoAppBundleId]
+ -[CARSession setLastPlayingVideoAppBundleId:]
+ -[CARSessionChannel initWithSession:channelType:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:sendSocketBufferSize:]
+ -[CARSessionChannel sendSocketBufferSize]
+ GCC_except_table104
+ GCC_except_table118
+ GCC_except_table123
+ GCC_except_table160
+ GCC_except_table184
+ GCC_except_table190
+ GCC_except_table218
+ _CARScreenTypeForDisplayIndex
+ _CARkAPEndpointProperty_SnoopCollectionPath
+ _CRFetchTapToRadarDraftBannerInfo
+ _OBJC_IVAR_$_CARSession._lastPlayingVideoAppBundleId
+ _OBJC_IVAR_$_CARSession._videoPlaybackAvailable
+ _OBJC_IVAR_$_CARSessionChannel._sendSocketBufferSize
+ __OBJC_$_CLASS_METHODS__TtC6CarKit18CRDisplayScaleInfo(CarKit|CarKit1)
+ __OBJC_$_INSTANCE_METHODS__TtC6CarKit18CRDisplayScaleInfo(CarKit|CarKit1)
+ ___132-[CARSession createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:sendSocketBufferSize:error:]_block_invoke
+ ___53-[CARSession handleDDPChangeWithAppearance:screenID:]_block_invoke
+ ___CRFetchTapToRadarDraftBannerInfo_block_invoke
+ ___CRFetchTapToRadarDraftBannerInfo_block_invoke_2
+ ___CRFetchTapToRadarDraftBannerInfo_block_invoke_3
+ ___block_descriptor_48_e8_32bs40bs_e33_v32?0q8"NSString"16"NSError"24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s_e5_v8?0ls32l8s40l8
+ _kFigEndpointAirPlayVideoPlaybackAudioOnlyMode_Forced
+ _kFigEndpointRemoteControlSessionCreationOption_SendSocketBufferSize
+ _kVideoPlayback_PlayerEventRef
+ _objc_msgSend$_stringForAppearanceMode:
+ _objc_msgSend$_videoPlaybackAudioOnlyMode
+ _objc_msgSend$createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:sendSocketBufferSize:error:
+ _objc_msgSend$fetchTapToRadarDraftBannerInfoWithReply:
+ _objc_msgSend$initWithSession:channelType:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:sendSocketBufferSize:
+ _objc_msgSend$lastPlayingVideoAppBundleId
+ _objc_msgSend$nameForScreenType:
+ _objc_msgSend$sendSocketBufferSize
+ _objc_msgSend$session:isPlayingVideoInAudioOnlyModeFromApp:
+ _objc_msgSend$setLastPlayingVideoAppBundleId:
+ _objc_msgSend$withDDPAppearance:forScreenID:
- -[CARSession createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:error:]
- -[CARSession handleDDPChangeAppearance:screenID:]
- GCC_except_table102
- GCC_except_table116
- GCC_except_table155
- GCC_except_table179
- GCC_except_table185
- GCC_except_table213
- __OBJC_$_INSTANCE_METHODS__TtC6CarKit18CRDisplayScaleInfo(CarKit)
- ___111-[CARSession createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:error:]_block_invoke
- ___49-[CARSession handleDDPChangeAppearance:screenID:]_block_invoke
- _objc_msgSend$createRemoteControlSession:channelID:withoutReply:sendAsIs:qualityOfService:streamPriority:error:
- _objc_msgSend$videoPlaybackAvailable
- _objc_msgSend$withDDPAppearanceMode:forScreenID:
- _symbolic _____ySSG s23_ContiguousArrayStorageC
CStrings:
+ " %@[ui=%@ map=%@]"
+ "%{public}s   %{public}s"
+ "%{public}s %{public}s"
+ "Attempting to start remote control session for channel %{public}@ channelID: %{public}@ withoutReply: %d sendAsIs: %d qualityOfService: %{public}@ streamPriority: %{public}@ sendSocketBufferSize: %{public}@"
+ "BackButton"
+ "DDP appearance: raw=%{public}@ resolved=%{public}@ screenID=%{public}@"
+ "HidVideoButton"
+ "No MFi certificate serial number for the current session"
+ "SnoopCollectionPath"
+ "Video is playing in audio only mode for app %@"
+ "Video playback player event: %@"
+ "VideoPlaybackPlayerEvent_ButtonTapped"
+ "VideoPlayback_PlayerEvent"
+ "[Appearance-Init]"
+ "[Appearance-Init] locationNightMode=%d, nightMode=%d, appearancePreference=%{public}@, resolved:%{public}@"
+ "[Appearance-State]"
+ "[Appearance-Update] Preference %{public}@ -> %{public}@"
+ "[Appearance-Update] Screen %{public}@: appearance %{public}@ -> %{public}@"
+ "[Appearance-Update] Screen %{public}@: mapAppearance %{public}@ -> %{public}@"
+ "[Appearance-Update] nightMode: %d -> %d"
+ "com.apple.WebKit.GPU"
+ "com.apple.mobilesafari"
+ "dark(1)"
+ "endpoint is MFi Mutual Authenticated"
+ "endpoint is MFi SAP authenticated"
+ "endpoint is NOT authenticated"
+ "endpoint is not authenticayed because it is missing serial data."
+ "light(0)"
+ "v32@?0q8@\"NSString\"16@\"NSError\"24"
- "Attempting to start remote control session for channel %{public}@"
- "DDP appearance: mode=%{public}@ screenID=%{public}@"
- "Forced"
- "Initial CARAppearanceState state: %{public}s"
- "Initial state: locationNightMode=%d, nightMode=%d, appearancePreference=%{public}@"
- "New state: %{public}s"
- "Preference %{public}@ -> %{public}@"
- "Screen %{public}@: appearance %{public}@ -> %{public}@"
- "Screen %{public}@: mapAppearance %{public}@ -> %{public}@"
- "endpoint is authenticated"
- "nightMode: %d -> %d"
- "withDDPAppearanceMode: undefined mode for screenID=%{public}s, keeping screen in AirPlay"
```
