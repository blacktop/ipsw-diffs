## Announce

> `/System/Library/PrivateFrameworks/Announce.framework/Announce`

```diff

-304.4.1.0.0
-  __TEXT.__text: 0x36e24
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x23b0
+314.0.0.0.0
+  __TEXT.__text: 0x41324
+  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__objc_methlist: 0x30c8
   __TEXT.__const: 0x1ce4
-  __TEXT.__cstring: 0x44f7
-  __TEXT.__oslogstring: 0x162a
-  __TEXT.__gcc_except_tab: 0x47c
-  __TEXT.__constg_swiftt: 0x854
+  __TEXT.__cstring: 0x3fc9
+  __TEXT.__oslogstring: 0x201a
+  __TEXT.__gcc_except_tab: 0x690
   __TEXT.__swift5_typeref: 0x920
+  __TEXT.__constg_swiftt: 0x860
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x8e2
-  __TEXT.__swift5_fieldmd: 0x6e8
+  __TEXT.__swift5_reflstr: 0x902
+  __TEXT.__swift5_fieldmd: 0x6f4
   __TEXT.__swift5_assocty: 0x1d8
   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x80
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x4c
-  __TEXT.__swift5_capture: 0x114
-  __TEXT.__unwind_info: 0x1088
-  __TEXT.__eh_frame: 0x9a8
-  __TEXT.__objc_classname: 0x5ab
-  __TEXT.__objc_methname: 0x46e6
-  __TEXT.__objc_methtype: 0xe9e
-  __TEXT.__objc_stubs: 0x3540
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0xc30
-  __DATA_CONST.__objc_classlist: 0x178
-  __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0xf8
+  __TEXT.__swift5_capture: 0x104
+  __TEXT.__unwind_info: 0x1428
+  __TEXT.__eh_frame: 0x9e8
+  __TEXT.__objc_classname: 0x977
+  __TEXT.__objc_methname: 0x7247
+  __TEXT.__objc_methtype: 0x1868
+  __TEXT.__objc_stubs: 0x45e0
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0xfb0
+  __DATA_CONST.__objc_classlist: 0x190
+  __DATA_CONST.__objc_catlist: 0x48
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1278
+  __DATA_CONST.__objc_selrefs: 0x1b60
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __AUTH_CONST.__auth_got: 0x770
-  __AUTH_CONST.__const: 0x14f0
-  __AUTH_CONST.__cfstring: 0x2f20
-  __AUTH_CONST.__objc_const: 0x4558
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__const: 0x14e0
+  __AUTH_CONST.__cfstring: 0x3020
+  __AUTH_CONST.__objc_const: 0x5358
   __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__objc_doubleobj: 0x110
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x11e8
-  __AUTH.__data: 0x3e0
-  __DATA.__objc_ivar: 0x1e8
-  __DATA.__data: 0xe10
-  __DATA.__bss: 0x2620
-  __DATA.__common: 0x20
+  __AUTH_CONST.__objc_doubleobj: 0x110
+  __AUTH.__objc_data: 0x12d8
+  __AUTH.__data: 0x470
+  __DATA.__objc_ivar: 0x224
+  __DATA.__data: 0x1168
+  __DATA.__bss: 0x2660
+  __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x580
-  __DATA_DIRTY.__data: 0x100
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__data: 0x108
+  __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/Frameworks/Speech.framework/Speech
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift
+  - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
+  - /System/Library/PrivateFrameworks/HomeMessagingUtils.framework/HomeMessagingUtils
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B6A1BC02-5A71-3D8B-88FB-163DBE26470F
-  Functions: 1497
-  Symbols:   3454
-  CStrings:  2093
+  UUID: 57683018-FC8A-37A6-AD39-F31C511A3399
+  Functions: 1671
+  Symbols:   4015
+  CStrings:  2554
 
Symbols:
+ +[ANDevice isAnnounceSupported]
+ +[ANHomeManager bundleForLocationAuthorization]
+ +[ANHomeManager defaultHomeOptions]
+ +[ANHomeManager shared]
+ -[ANAccessorySettingsCache .cxx_destruct]
+ -[ANAccessorySettingsCache _fetchSettingsForAccessory:useCache:]
+ -[ANAccessorySettingsCache _removeSettingsForAccessoryWithIdentifier:]
+ -[ANAccessorySettingsCache _updateSettings:forAccessoryWithIdentifier:]
+ -[ANAccessorySettingsCache accessorySettingsDataSource:didReceiveSettingsUpdatesForAccessoryWithIdentifier:settings:]
+ -[ANAccessorySettingsCache accessorySettingsDataSource]
+ -[ANAccessorySettingsCache cachedAccessorySettings]
+ -[ANAccessorySettingsCache initWithAccessorySettingsDataSource:]
+ -[ANAccessorySettingsCache lastAccessorySettingsFetch]
+ -[ANAccessorySettingsCache log]
+ -[ANAccessorySettingsCache settingsForAccessory:]
+ -[ANAccessorySettingsCache settingsQueue]
+ -[ANAnalyticsCounter append:]
+ -[ANAnalyticsCounter count]
+ -[ANAnalyticsCounter finished]
+ -[ANAnalyticsCounter hexCount]
+ -[ANAnalyticsCounter initWithHexCount:]
+ -[ANAnalyticsCounter init]
+ -[ANAnalyticsCounter payload:keyTwo:]
+ -[ANAnnouncementContext creationTimestamp]
+ -[ANHomeManager .cxx_destruct]
+ -[ANHomeManager _executeBlockForDelegates:]
+ -[ANHomeManager _notifyManagerLoadedHomes:]
+ -[ANHomeManager accessoryDidUpdateControllable:]
+ -[ANHomeManager accessoryDidUpdateName:]
+ -[ANHomeManager accessoryDidUpdateSupportsAudioAnalysis:]
+ -[ANHomeManager accessoryDidUpdateSupportsDropIn:]
+ -[ANHomeManager accessorySettingsCache]
+ -[ANHomeManager addDelegate:queue:]
+ -[ANHomeManager allHomes]
+ -[ANHomeManager currentAccessory]
+ -[ANHomeManager currentHome]
+ -[ANHomeManager delegatesToQueues]
+ -[ANHomeManager home:didAddAccessory:]
+ -[ANHomeManager home:didAddUser:]
+ -[ANHomeManager home:didRemoveAccessory:]
+ -[ANHomeManager home:didRemoveUser:]
+ -[ANHomeManager home:didUpdateAccessControlForUser:]
+ -[ANHomeManager homeDidUpdateAccessControlForCurrentUser:]
+ -[ANHomeManager homeManager:didAddHome:]
+ -[ANHomeManager homeManager:didRemoveHome:]
+ -[ANHomeManager homeManagerDidUpdateHomes:]
+ -[ANHomeManager homeManager]
+ -[ANHomeManager homesLoadedCompletionHandlers]
+ -[ANHomeManager homesLoaded]
+ -[ANHomeManager homesSupportingAnnounce]
+ -[ANHomeManager homes]
+ -[ANHomeManager initWithCaching:]
+ -[ANHomeManager initWithCaching:homeOptions:]
+ -[ANHomeManager init]
+ -[ANHomeManager loadHomeSynchronous]
+ -[ANHomeManager loadHomes:]
+ -[ANHomeManager loadHomesStart]
+ -[ANHomeManager refreshHomeSynchronous]
+ -[ANHomeManager registerDelegate:queue:]
+ -[ANHomeManager serialQueue]
+ -[ANHomeManager setHomesLoaded:]
+ -[ANHomeManager(Home) homeForID:]
+ -[ANHomeManager(Home) homeWithName:]
+ -[ANHomeManager(Home) homesSupportingAnnounceFromHomes:]
+ -[ANHomeManager(Home) homesSupportingAnnounce]
+ -[ANHomeManager(Home) homesWithRoomNames:]
+ -[ANHomeManager(Home) homesWithZoneNames:]
+ -[ANHomeManager(Home) isEndpointWithUUID:inRoomWithName:]
+ -[ANHomeManager(Home) isLocalDeviceInRoom:]
+ -[ANRemotePlaybackSession setPlaybackStoppedForAnnouncement:userInitiated:]
+ -[HMAccessory(Announce_ObjC) an_announceSettingFromAccessorySettings]
+ -[HMAccessory(Announce_ObjC) an_announceSettingFromAccessorySettings].cold.1
+ -[HMHome(Announce_ObjC) _usersWithAnnounceEnabledIncludingCurrentUser:]
+ -[HMHome(Announce_ObjC) announceAccessAllowedForCurrentUser]
+ -[HMHome(Announce_ObjC) announceAccessAllowedForUser:]
+ -[HMHome(Announce_ObjC) isAnnounceAvailable]
+ -[HMHome(Announce_ObjC) isAnnounceEnabledForAnyAccessoryOrUser]
+ -[HMHome(Announce_ObjC) isAnnounceEnabledForAnyAccessory]
+ -[HMHome(Announce_ObjC) isAnnounceSupported]
+ -[HMHome(Announce_ObjC) usersIncludingCurrentUserWithAnnounceAndRemoteAccessEnabled]
+ -[HMHome(Announce_ObjC) usersIncludingCurrentUserWithAnnounceEnabled]
+ -[HMHome(Announce_ObjC) usersWithAnnounceEnabled]
+ -[NSArray(ANAnnouncements) an_identifiers]
+ -[NSArray(ANAnnouncements) an_playedAnnouncements]
+ -[NSArray(ANAnnouncements) an_unplayedAnnouncements]
+ -[NSArray(ANAnnouncements) identifiers]
+ -[NSArray(ANAnnouncements) playedAnnouncements]
+ -[NSArray(ANAnnouncements) unplayedAnnouncements]
+ GCC_except_table11
+ GCC_except_table28
+ GCC_except_table41
+ GCC_except_table44
+ _ANCreationTimestampKey
+ _ANLogHandleAccessory_Announce.logger
+ _ANLogHandleAccessory_Announce.once
+ _ANLogHandleHomeManager
+ _ANLogHandleHomeManager.cold.1
+ _ANLogHandleHomeManager.logger
+ _ANLogHandleHomeManager.once
+ _ANLogHandleHome_Announce
+ _ANLogHandleHome_Announce.cold.1
+ _ANLogHandleHome_Announce.logger
+ _ANLogHandleHome_Announce.once
+ _ANSettingKeyPathAnnounceEnabled
+ _ANSettingKeyPathAnnounceGroup
+ _ANTestAnnounceDate
+ _ANTestAnnouncer
+ _OBJC_CLASS_$_ANAccessorySettingsCache
+ _OBJC_CLASS_$_ANAnalyticsCounter
+ _OBJC_CLASS_$_ANHomeManager
+ _OBJC_CLASS_$_HMAccessory
+ _OBJC_CLASS_$_HMBooleanSetting
+ _OBJC_CLASS_$_HMFLocationAuthorization
+ _OBJC_CLASS_$_HMHome
+ _OBJC_CLASS_$_HMHomeManager
+ _OBJC_CLASS_$_HMImmutableSetting
+ _OBJC_CLASS_$_HMMutableHomeManagerConfiguration
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_IVAR_$_ANAccessorySettingsCache._accessorySettingsDataSource
+ _OBJC_IVAR_$_ANAccessorySettingsCache._cachedAccessorySettings
+ _OBJC_IVAR_$_ANAccessorySettingsCache._lastAccessorySettingsFetch
+ _OBJC_IVAR_$_ANAccessorySettingsCache._log
+ _OBJC_IVAR_$_ANAccessorySettingsCache._settingsQueue
+ _OBJC_IVAR_$_ANAnalyticsCounter._count
+ _OBJC_IVAR_$_ANAnalyticsCounter._hexCount
+ _OBJC_IVAR_$_ANAnnouncementContext._creationTimestamp
+ _OBJC_IVAR_$_ANHomeManager._accessorySettingsCache
+ _OBJC_IVAR_$_ANHomeManager._delegatesToQueues
+ _OBJC_IVAR_$_ANHomeManager._homeManager
+ _OBJC_IVAR_$_ANHomeManager._homesLoaded
+ _OBJC_IVAR_$_ANHomeManager._homesLoadedCompletionHandlers
+ _OBJC_IVAR_$_ANHomeManager._loadHomesStart
+ _OBJC_IVAR_$_ANHomeManager._serialQueue
+ _OBJC_METACLASS_$_ANAccessorySettingsCache
+ _OBJC_METACLASS_$_ANAnalyticsCounter
+ _OBJC_METACLASS_$_ANHomeManager
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ __OBJC_$_CATEGORY_HMAccessory_$_Announce_ObjC
+ __OBJC_$_CATEGORY_HMHome_$_Announce_ObjC
+ __OBJC_$_CLASS_METHODS_ANHomeManager
+ __OBJC_$_CLASS_METHODS_HMAccessory(Announce_ObjC|Announce)
+ __OBJC_$_CLASS_PROP_LIST_ANHomeManager
+ __OBJC_$_INSTANCE_METHODS_ANAccessorySettingsCache
+ __OBJC_$_INSTANCE_METHODS_ANAnalyticsCounter
+ __OBJC_$_INSTANCE_METHODS_ANHomeManager(Home)
+ __OBJC_$_INSTANCE_METHODS_HMAccessory(Announce_ObjC|Announce)
+ __OBJC_$_INSTANCE_METHODS_HMHome(Announce_ObjC|Announce)
+ __OBJC_$_INSTANCE_METHODS_NSArray(ANParticipant|ANAnnouncements)
+ __OBJC_$_INSTANCE_VARIABLES_ANAccessorySettingsCache
+ __OBJC_$_INSTANCE_VARIABLES_ANAnalyticsCounter
+ __OBJC_$_INSTANCE_VARIABLES_ANHomeManager
+ __OBJC_$_PROP_LIST_ANAccessorySettingsCache
+ __OBJC_$_PROP_LIST_ANAnalyticsCounter
+ __OBJC_$_PROP_LIST_ANAnalyticsDailyHomesProvider
+ __OBJC_$_PROP_LIST_DICHomeManagerProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ANAnalyticsDailyHomesProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DICHomeManagerProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMAccessoryDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMAccessoryDelegatePrivate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMAccessorySettingsDataSourceDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMHomeDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMHomeDelegatePrivate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMHomeManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ANAnalyticsDailyHomesProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DICHomeManagerProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMAccessoryDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMAccessoryDelegatePrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMAccessorySettingsDataSourceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMHomeDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMHomeDelegatePrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMHomeManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_ANAnalyticsDailyHomesProvider
+ __OBJC_$_PROTOCOL_REFS_DICHomeManagerProviding
+ __OBJC_$_PROTOCOL_REFS_HMAccessoryDelegate
+ __OBJC_$_PROTOCOL_REFS_HMAccessoryDelegatePrivate
+ __OBJC_$_PROTOCOL_REFS_HMAccessorySettingsDataSourceDelegate
+ __OBJC_$_PROTOCOL_REFS_HMHomeDelegate
+ __OBJC_$_PROTOCOL_REFS_HMHomeDelegatePrivate
+ __OBJC_$_PROTOCOL_REFS_HMHomeManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_ANAccessorySettingsCache
+ __OBJC_CLASS_PROTOCOLS_$_ANHomeManager
+ __OBJC_CLASS_RO_$_ANAccessorySettingsCache
+ __OBJC_CLASS_RO_$_ANAnalyticsCounter
+ __OBJC_CLASS_RO_$_ANHomeManager
+ __OBJC_LABEL_PROTOCOL_$_ANAnalyticsDailyHomesProvider
+ __OBJC_LABEL_PROTOCOL_$_DICHomeManagerProviding
+ __OBJC_LABEL_PROTOCOL_$_HMAccessoryDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMAccessoryDelegatePrivate
+ __OBJC_LABEL_PROTOCOL_$_HMAccessorySettingsDataSourceDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMHomeDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMHomeDelegatePrivate
+ __OBJC_LABEL_PROTOCOL_$_HMHomeManagerDelegate
+ __OBJC_METACLASS_RO_$_ANAccessorySettingsCache
+ __OBJC_METACLASS_RO_$_ANAnalyticsCounter
+ __OBJC_METACLASS_RO_$_ANHomeManager
+ __OBJC_PROTOCOL_$_ANAnalyticsDailyHomesProvider
+ __OBJC_PROTOCOL_$_DICHomeManagerProviding
+ __OBJC_PROTOCOL_$_HMAccessoryDelegate
+ __OBJC_PROTOCOL_$_HMAccessoryDelegatePrivate
+ __OBJC_PROTOCOL_$_HMAccessorySettingsDataSourceDelegate
+ __OBJC_PROTOCOL_$_HMHomeDelegate
+ __OBJC_PROTOCOL_$_HMHomeDelegatePrivate
+ __OBJC_PROTOCOL_$_HMHomeManagerDelegate
+ ___117-[ANAccessorySettingsCache accessorySettingsDataSource:didReceiveSettingsUpdatesForAccessoryWithIdentifier:settings:]_block_invoke
+ ___23+[ANHomeManager shared]_block_invoke
+ ___25-[ANHomeManager allHomes]_block_invoke
+ ___27-[ANHomeManager loadHomes:]_block_invoke
+ ___32-[ANAnnounce announcementForID:]_block_invoke.101
+ ___33-[ANAnnounce prewarmWithHandler:]_block_invoke.117
+ ___33-[ANHomeManager home:didAddUser:]_block_invoke
+ ___33-[ANHomeManager home:didAddUser:]_block_invoke.46
+ ___34-[ANAnnounce homeNamesForContext:]_block_invoke.111
+ ___34-[ANAnnounce isLocalDeviceInRoom:]_block_invoke.112
+ ___35-[ANAnnounce receivedAnnouncements]_block_invoke.103
+ ___35-[ANAnnounce unplayedAnnouncements]_block_invoke.104
+ ___36-[ANHomeManager home:didRemoveUser:]_block_invoke
+ ___36-[ANHomeManager home:didRemoveUser:]_block_invoke.49
+ ___37-[ANAnnounce receivedAnnouncementIDs]_block_invoke.99
+ ___37-[ANAnnounce sendRequest:completion:]_block_invoke.94
+ ___37-[ANRemotePlaybackSession endSession]_block_invoke.99
+ ___38-[ANAnnounce contextFromAnnouncement:]_block_invoke.109
+ ___38-[ANHomeManager home:didAddAccessory:]_block_invoke
+ ___38-[ANHomeManager home:didAddAccessory:]_block_invoke.40
+ ___39-[ANHomeManager refreshHomeSynchronous]_block_invoke
+ ___40-[ANHomeManager accessoryDidUpdateName:]_block_invoke
+ ___40-[ANHomeManager accessoryDidUpdateName:]_block_invoke.56
+ ___40-[ANHomeManager homeManager:didAddHome:]_block_invoke
+ ___40-[ANHomeManager homeManager:didAddHome:]_block_invoke.28
+ ___40-[ANHomeManager registerDelegate:queue:]_block_invoke
+ ___41-[ANAnnounce initWithEndpointIdentifier:]_block_invoke.87
+ ___41-[ANHomeManager home:didRemoveAccessory:]_block_invoke
+ ___41-[ANHomeManager home:didRemoveAccessory:]_block_invoke.43
+ ___43-[ANHomeManager _executeBlockForDelegates:]_block_invoke
+ ___43-[ANHomeManager _executeBlockForDelegates:]_block_invoke_2
+ ___43-[ANHomeManager homeManager:didRemoveHome:]_block_invoke
+ ___43-[ANHomeManager homeManager:didRemoveHome:]_block_invoke.31
+ ___43-[ANHomeManager homeManagerDidUpdateHomes:]_block_invoke
+ ___43-[ANHomeManager homeManagerDidUpdateHomes:]_block_invoke.24
+ ___44-[ANAnnounce _sendRequestLegacy:completion:]_block_invoke.119
+ ___48-[ANAnnounce isEndpointWithUUID:inRoomWithName:]_block_invoke.114
+ ___48-[ANHomeManager accessoryDidUpdateControllable:]_block_invoke
+ ___48-[ANHomeManager accessoryDidUpdateControllable:]_block_invoke.53
+ ___49-[ANAccessorySettingsCache settingsForAccessory:]_block_invoke
+ ___50-[ANHomeManager accessoryDidUpdateSupportsDropIn:]_block_invoke
+ ___50-[ANHomeManager accessoryDidUpdateSupportsDropIn:]_block_invoke.62
+ ___52-[ANHomeManager home:didUpdateAccessControlForUser:]_block_invoke
+ ___52-[ANHomeManager home:didUpdateAccessControlForUser:]_block_invoke.37
+ ___52-[ANHomeManager home:didUpdateAccessControlForUser:]_block_invoke_2
+ ___53-[ANAnnounce isAnnounceEnabledForAnyAccessoryInHome:]_block_invoke.115
+ ___56-[ANAnnounce validateDestinationFromContext:completion:]_block_invoke.118
+ ___57-[ANHomeManager accessoryDidUpdateSupportsAudioAnalysis:]_block_invoke
+ ___57-[ANHomeManager accessoryDidUpdateSupportsAudioAnalysis:]_block_invoke.59
+ ___58-[ANHomeManager homeDidUpdateAccessControlForCurrentUser:]_block_invoke
+ ___58-[ANHomeManager homeDidUpdateAccessControlForCurrentUser:]_block_invoke.34
+ ___59-[ANAnnounce isAnnounceEnabledForAnyAccessoryOrUserInHome:]_block_invoke.116
+ ___64-[ANAccessorySettingsCache _fetchSettingsForAccessory:useCache:]_block_invoke
+ ___64-[ANAccessorySettingsCache _fetchSettingsForAccessory:useCache:]_block_invoke.10
+ ___64-[ANAccessorySettingsCache _fetchSettingsForAccessory:useCache:]_block_invoke.13
+ ___64-[ANAccessorySettingsCache _fetchSettingsForAccessory:useCache:]_block_invoke.9
+ ___64-[ANAccessorySettingsCache _fetchSettingsForAccessory:useCache:]_block_invoke.cold.1
+ ___69-[HMAccessory(Announce_ObjC) an_announceSettingFromAccessorySettings]_block_invoke
+ ___69-[HMAccessory(Announce_ObjC) an_announceSettingFromAccessorySettings]_block_invoke.8
+ ___71-[ANRemotePlaybackSession startSessionForGroupID:announcementsHandler:]_block_invoke.97
+ ___71-[HMHome(Announce_ObjC) _usersWithAnnounceEnabledIncludingCurrentUser:]_block_invoke
+ ___75-[ANAnnounce mockAnnouncement:forHomeWithName:playbackDeadline:completion:]_block_invoke.105
+ ___75-[ANRemotePlaybackSession setPlaybackStoppedForAnnouncement:userInitiated:]_block_invoke
+ ___ANLogHandleAccessory_Announce_block_invoke
+ ___ANLogHandleHomeManager_block_invoke
+ ___ANLogHandleHome_Announce_block_invoke
+ ___block_descriptor_32_e28_B16?0"HMAccessorySetting"8l
+ ___block_descriptor_32_e33_B16?0"HMAccessorySettingGroup"8l
+ ___block_descriptor_40_e8_32s_e16_B16?0"HMUser"8ls32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_40_e8_32s_e33_v16?0"<ANHomeManagerDelegate>"8ls32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e33_v16?0"<ANHomeManagerDelegate>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_56_e8_32s40r48w_e5_v8?0lw48l8r40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56w_e5_v8?0lw56l8s32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8s40l8s48l8w56l8
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8s40l8w56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72w_e29_v24?0"NSError"8"NSArray"16lw72l8s32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
+ ___block_literal_global.108
+ ___block_literal_global.11
+ ___block_literal_global.162
+ ___block_literal_global.180
+ ___block_literal_global.347
+ ___block_literal_global.96
+ ___swift_allocate_value_buffer
+ ___swift_project_value_buffer
+ _dispatch_assert_queue_not$V2
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _objc_msgSend$_executeBlockForDelegates:
+ _objc_msgSend$_fetchSettingsForAccessory:useCache:
+ _objc_msgSend$_notifyManagerLoadedHomes:
+ _objc_msgSend$_refreshBeforeDate:completionHandler:
+ _objc_msgSend$_updateSettings:forAccessoryWithIdentifier:
+ _objc_msgSend$_usersWithAnnounceEnabledIncludingCurrentUser:
+ _objc_msgSend$accessories
+ _objc_msgSend$accessoryDidUpdateControllable:
+ _objc_msgSend$accessoryDidUpdateName:
+ _objc_msgSend$accessoryDidUpdateSupportedCapabilities:
+ _objc_msgSend$accessorySettingsCache
+ _objc_msgSend$accessorySettingsDataSource
+ _objc_msgSend$accessoryWithUniqueIdentifier:
+ _objc_msgSend$allHomes
+ _objc_msgSend$allObjects
+ _objc_msgSend$an_announceSettingFromAccessorySettings
+ _objc_msgSend$an_identifiers
+ _objc_msgSend$an_isAnnounceEnabled
+ _objc_msgSend$an_isAppleAnnounceAccessory
+ _objc_msgSend$an_isAppleAnnounceHostAccessory
+ _objc_msgSend$an_playedAnnouncements
+ _objc_msgSend$an_supportsAnnounce
+ _objc_msgSend$an_unplayedAnnouncements
+ _objc_msgSend$announceAccessAllowedForCurrentUser
+ _objc_msgSend$announceAccessAllowedForUser:
+ _objc_msgSend$announceAccessoriesWithAnnounceEnabledFromAccessories:
+ _objc_msgSend$announceDeviceNotificationModeToString:
+ _objc_msgSend$announceUserSettings
+ _objc_msgSend$announcementForID:
+ _objc_msgSend$announcementForID:reply:
+ _objc_msgSend$appleAnnounceAccessories
+ _objc_msgSend$bundleForLocationAuthorization
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$cachedAccessorySettings
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$checkInWithCompletionHandler:
+ _objc_msgSend$contextFromAnnouncement:
+ _objc_msgSend$createAccessorySettingsDataSource
+ _objc_msgSend$currentAccessory
+ _objc_msgSend$currentHome
+ _objc_msgSend$currentUser
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$defaultHomeOptions
+ _objc_msgSend$delegatesToQueues
+ _objc_msgSend$device
+ _objc_msgSend$deviceNotificationMode
+ _objc_msgSend$didAddHome:
+ _objc_msgSend$didRemoveHome:
+ _objc_msgSend$didUpdateHomes:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$fetchAccessorySettingsWithHomeIdentifier:accessoryIdentifier:keyPaths:completionHandler:
+ _objc_msgSend$fetchCachedAccessorySettingsWithHomeIdentifier:accessoryIdentifier:keyPaths:completionHandler:
+ _objc_msgSend$groups
+ _objc_msgSend$hmu_accessoriesExcludingCurrentAccessoryFromAccessories:
+ _objc_msgSend$hmu_accessoriesFromAccessories:excludingStereoCompanionForAccessory:
+ _objc_msgSend$hmu_allUsersIncludingCurrentUser
+ _objc_msgSend$hmu_homesFromHomes:withRoomNames:
+ _objc_msgSend$hmu_homesFromHomes:withZoneNames:
+ _objc_msgSend$hmu_isEndpoint
+ _objc_msgSend$hmu_isHomePod
+ _objc_msgSend$hmu_isRemoteAccessAllowedForUser:
+ _objc_msgSend$home
+ _objc_msgSend$home:didAddAccessory:
+ _objc_msgSend$home:didAddUser:
+ _objc_msgSend$home:didRemoveAccessory:
+ _objc_msgSend$home:didRemoveUser:
+ _objc_msgSend$home:didUpdateAccessControlForUser:
+ _objc_msgSend$homeAccessControlForUser:
+ _objc_msgSend$homeDidUpdateAccessControlForCurrentUser:
+ _objc_msgSend$homeLocationToString:
+ _objc_msgSend$homeManager
+ _objc_msgSend$homeNamesForContext:
+ _objc_msgSend$homes
+ _objc_msgSend$homesLoaded
+ _objc_msgSend$homesLoadedCompletionHandlers
+ _objc_msgSend$homesSupportingAnnounceFromHomes:
+ _objc_msgSend$initWithAccessorySettingsDataSource:
+ _objc_msgSend$initWithBundle:
+ _objc_msgSend$initWithCaching:
+ _objc_msgSend$initWithCaching:homeOptions:
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$initWithOptions:cachePolicy:
+ _objc_msgSend$initWithURL:options:
+ _objc_msgSend$isAnnounceAccessAllowed
+ _objc_msgSend$isAnnounceEnabledForAnyAccessoryOrUser
+ _objc_msgSend$isAnnounceSupported
+ _objc_msgSend$isControllable
+ _objc_msgSend$isEndpointWithUUID:inRoomWithName:
+ _objc_msgSend$isEqualToDate:
+ _objc_msgSend$isInternalBuild
+ _objc_msgSend$keyEnumerator
+ _objc_msgSend$keyPath
+ _objc_msgSend$lastAccessorySettingsFetch
+ _objc_msgSend$lastPlayedAnnouncementInfo
+ _objc_msgSend$loadHomeSynchronous
+ _objc_msgSend$loadHomes:
+ _objc_msgSend$loadHomesStart
+ _objc_msgSend$lock
+ _objc_msgSend$managerDidInterruptConnection:
+ _objc_msgSend$managerDidPerformDaemonCheckIn:
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
+ _objc_msgSend$na_filter:
+ _objc_msgSend$na_firstObjectPassingTest:
+ _objc_msgSend$numberForDefault:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$prewarmWithHandler:
+ _objc_msgSend$processAudioTranscription:
+ _objc_msgSend$processName
+ _objc_msgSend$receivedAnnouncements
+ _objc_msgSend$registerDelegate:queue:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$room
+ _objc_msgSend$rootGroup
+ _objc_msgSend$setDelegateQueue:
+ _objc_msgSend$setDiscretionary:
+ _objc_msgSend$setEndpointIdentifier:
+ _objc_msgSend$setHomeKitUserIdentifier:
+ _objc_msgSend$setHomesLoaded:
+ _objc_msgSend$setInactiveUpdatingLevel:
+ _objc_msgSend$setLocationAuthorization:
+ _objc_msgSend$setPlaybackStoppedForAnnouncement:userInitiated:
+ _objc_msgSend$setTranscription:
+ _objc_msgSend$settingsForAccessory:
+ _objc_msgSend$settingsQueue
+ _objc_msgSend$supportsAnnounce
+ _objc_msgSend$supportsAudioAnalysis
+ _objc_msgSend$supportsDropIn
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$uniqueIdentifier
+ _objc_msgSend$unlock
+ _objc_msgSend$unplayedAnnouncements
+ _objc_msgSend$users
+ _objc_msgSend$usersIncludingCurrentUserWithAnnounceEnabled
+ _objc_msgSend$usersWithAnnounceEnabled
+ _objc_msgSend$value
+ _objc_opt_isKindOfClass
+ _objc_retainBlock
+ _objc_retain_x26
+ _objc_retain_x28
+ _shared.manager
+ _swift_dynamicCastObjCClass
+ _symbolic So8NSObjectCSg
+ _symbolic _____Sg 10Foundation4DateV
- -[ANAnnounce lastPlayedAnnouncementInfo:]
- -[ANRemotePlaybackSession setPlaybackEndedForAnnouncement:]
- -[NSArray(ANAnnouncement) identifiers]
- -[NSArray(ANAnnouncement) playedAnnouncements]
- -[NSArray(ANAnnouncement) unplayedAnnouncements]
- __OBJC_$_INSTANCE_METHODS_NSArray(ANParticipant|ANAnnouncement)
- ___32-[ANAnnounce announcementForID:]_block_invoke.103
- ___33-[ANAnnounce prewarmWithHandler:]_block_invoke.119
- ___34-[ANAnnounce homeNamesForContext:]_block_invoke.113
- ___34-[ANAnnounce isLocalDeviceInRoom:]_block_invoke.114
- ___35-[ANAnnounce receivedAnnouncements]_block_invoke.105
- ___35-[ANAnnounce unplayedAnnouncements]_block_invoke.106
- ___37-[ANAnnounce receivedAnnouncementIDs]_block_invoke.101
- ___37-[ANAnnounce sendRequest:completion:]_block_invoke.96
- ___37-[ANRemotePlaybackSession endSession]_block_invoke.97
- ___38-[ANAnnounce contextFromAnnouncement:]_block_invoke.111
- ___41-[ANAnnounce initWithEndpointIdentifier:]_block_invoke.91
- ___41-[ANAnnounce lastPlayedAnnouncementInfo:]_block_invoke
- ___44-[ANAnnounce _sendRequestLegacy:completion:]_block_invoke.121
- ___48-[ANAnnounce isEndpointWithUUID:inRoomWithName:]_block_invoke.116
- ___53-[ANAnnounce isAnnounceEnabledForAnyAccessoryInHome:]_block_invoke.117
- ___56-[ANAnnounce validateDestinationFromContext:completion:]_block_invoke.120
- ___59-[ANAnnounce isAnnounceEnabledForAnyAccessoryOrUserInHome:]_block_invoke.118
- ___61-[ANRemotePlaybackSession setPlaybackStoppedForAnnouncement:]_block_invoke
- ___71-[ANRemotePlaybackSession startSessionForGroupID:announcementsHandler:]_block_invoke.95
- ___75-[ANAnnounce mockAnnouncement:forHomeWithName:playbackDeadline:completion:]_block_invoke.107
- ___block_literal_global.110
- ___block_literal_global.160
- ___block_literal_global.182
- ___block_literal_global.340
- ___block_literal_global.94
- ___swift_memcpy32_8
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$lastPlayedAnnouncementInfo:
- _objc_msgSend$setPlaybackStoppedForAnnouncement:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _swift_weakDestroy
- _swift_weakInit
- _swift_weakLoadStrong
- _symbolic _____SgXw 8Announce0A7ServiceC
- _symbolic _____SgXwz_Xx 8Announce0A7ServiceC
- _type_layout_string 8Announce30SendAnnouncementIntentResponseV
CStrings:
+ " (including current user)"
+ "%@%lu accessor%s with announce enabled"
+ "%@%lu accessor%s with announce enabled.  %ld user%s with announce enabled"
+ "%@Access Control Changed for Current User in Home: %@"
+ "%@Access Control Changed for User %@ in Home: %@"
+ "%@Accessory Controllable Updated: %@, %@"
+ "%@Accessory Name Updated: %@, %@"
+ "%@Accessory Supports Audio Analysis Updated: %@, %@, Supports Audio Analysis = %d"
+ "%@Accessory Supports Drop In Updated: %@, %@, Supports Drop In = %d"
+ "%@Added Accessory %@, %@"
+ "%@Added Home %@, %@"
+ "%@Announce Access Allowed For User (Name = %@, ID = %@): %@"
+ "%@Announce is DISABLED For User (Name = %@, ID = %@)"
+ "%@Failed to find Announce Setting Group in Accessory Settings %@"
+ "%@Home has %ld users%s, %ld have intercom enabled"
+ "%@Home manager refresh %@"
+ "%@Home manager refresh start (%.2fs timeout)"
+ "%@HomeKit Added User %@, %@, %@"
+ "%@HomeKit Removed User %@, %@, %@"
+ "%@Homes Already Loaded"
+ "%@Homes Loaded: %@"
+ "%@Load Homes took %f seconds"
+ "%@Loaded Homes Synchronous: %@"
+ "%@Loaded homes %@"
+ "%@Loading Homes"
+ "%@No bundle for location authorization"
+ "%@Notifying Homes Loaded to %i handlers"
+ "%@Notifying delegate homes loaded: %@"
+ "%@Removed Accessory %@, %@"
+ "%@Removed Home %@, %@"
+ "%@[Override] Force Allow Announce For User (Name = %@, ID = %@) Enabled"
+ "%@[Override] Setting HomeKit Cache Policy to None. Actual = %lu"
+ "%@allHomes timeout waiting for loaded Homes after %d seconds"
+ "-[ANRemotePlaybackSession setPlaybackStoppedForAnnouncement:userInitiated:]_block_invoke"
+ "/System/Library/LocationBundles/HomeKitDaemon.framework"
+ "@\"ANAccessorySettingsCache\""
+ "@\"HMAccessory\"16@0:8"
+ "@\"HMAccessorySettingsDataSource\""
+ "@\"HMHome\"16@0:8"
+ "@\"HMHomeManager\""
+ "@\"NSArray\"16@0:8"
+ "@\"NSMapTable\""
+ "@\"NSMutableArray\""
+ "@20@0:8B16"
+ "@28@0:8@16B24"
+ "@28@0:8B16Q20"
+ "ANAccessorySettingsCache"
+ "ANAnalyticsCounter"
+ "ANAnalyticsDailyHomesProvider"
+ "ANAnnouncements"
+ "ANHomeManager"
+ "AccessorySettingsCache"
+ "Accessory_Announce"
+ "Announce Enabled Setting For Accessory %@: %{bool}d"
+ "Announce is DISABLED For Accessory %@"
+ "Announce setting not found in accessory settings"
+ "Announce setting not found in settings from data source"
+ "Announce_ObjC"
+ "Attempting to use locally-cached settings"
+ "B16@?0@\"HMAccessorySetting\"8"
+ "B16@?0@\"HMAccessorySettingGroup\"8"
+ "B16@?0@\"HMUser\"8"
+ "B24@0:8q16"
+ "Cached Settings"
+ "Current User Announce Notification Mode: %{public}s"
+ "Current User is not in Home %@ (Current Home Location Status = %s (%ld). Not posting user notification."
+ "DICHomeManagerProviding"
+ "Failed to retrieve %{public}@ for Accessory %@, %@: %@"
+ "Fetched %{public}@ for Accessory %@, %@: %@"
+ "Fetching %{public}@ for Accessory %@, %@"
+ "HMAccessoryDelegate"
+ "HMAccessoryDelegatePrivate"
+ "HMAccessorySettingsDataSourceDelegate"
+ "HMHomeDelegate"
+ "HMHomeDelegatePrivate"
+ "HMHomeManagerDelegate"
+ "HomeManager"
+ "Home_Announce"
+ "I"
+ "I16@0:8"
+ "Override Home Location Status: %s (%ld), Current Home Location Status: %s (%ld), Home: %@"
+ "Received Settings Updates for Accessory Identifier %@: %@"
+ "Settings"
+ "Settings need refresh for accessory %@, %@"
+ "Settings not found in settings from data source"
+ "Supports Announce for Accessory %@: %{bool}d"
+ "T@\"ANAccessorySettingsCache\",R,N,V_accessorySettingsCache"
+ "T@\"HMAccessory\",R,N"
+ "T@\"HMAccessorySettingsDataSource\",R,N,V_accessorySettingsDataSource"
+ "T@\"HMHome\",R,N"
+ "T@\"HMHomeManager\",R,N,V_homeManager"
+ "T@\"NSArray\",N,R"
+ "T@\"NSDate\",R,N,V_creationTimestamp"
+ "T@\"NSDate\",R,N,V_loadHomesStart"
+ "T@\"NSMapTable\",R,N,V_delegatesToQueues"
+ "T@\"NSMutableArray\",R,N,V_homesLoadedCompletionHandlers"
+ "T@\"NSMutableDictionary\",R,N,V_cachedAccessorySettings"
+ "T@\"NSMutableDictionary\",R,N,V_lastAccessorySettingsFetch"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_settingsQueue"
+ "TB,N,V_homesLoaded"
+ "TI,R,V_count"
+ "TQ,R,V_hexCount"
+ "Timed-out waiting for Accessory %{public}@ for %@, %@"
+ "User1"
+ "WARNING: Using cached settings for accessory. Value may be stale. %@, %@"
+ "[BOOL] Include recipients in communication user notifications"
+ "[Override] Force Allow Announce For Accessory %@ Enabled"
+ "[Override] Force Announce Notifications Enabled"
+ "[Override] Force Announce Supported For Accessory %@ Enabled"
+ "_accessorySettingsCache"
+ "_accessorySettingsDataSource"
+ "_cachedAccessorySettings"
+ "_count"
+ "_delegatesToQueues"
+ "_executeBlockForDelegates:"
+ "_fetchSettingsForAccessory:useCache:"
+ "_hexCount"
+ "_homeManager"
+ "_homesLoaded"
+ "_homesLoadedCompletionHandlers"
+ "_lastAccessorySettingsFetch"
+ "_loadHomesStart"
+ "_notifyManagerLoadedHomes:"
+ "_refreshBeforeDate:completionHandler:"
+ "_removeSettingsForAccessoryWithIdentifier:"
+ "_settingsQueue"
+ "_updateSettings:forAccessoryWithIdentifier:"
+ "_usersWithAnnounceEnabledIncludingCurrentUser:"
+ "accessories"
+ "accessoriesWithAnnounceEnabledFromAccessories:"
+ "accessory:didAddControlTarget:"
+ "accessory:didAddProfile:"
+ "accessory:didAddSymptomsHandler:"
+ "accessory:didRemoveControlTarget:"
+ "accessory:didRemoveProfile:"
+ "accessory:didUpdateApplicationDataForService:"
+ "accessory:didUpdateAssociatedServiceTypeForService:"
+ "accessory:didUpdateBulletinBoardNotificationForService:"
+ "accessory:didUpdateBundleID:"
+ "accessory:didUpdateConfigurationStateForService:"
+ "accessory:didUpdateConfiguredNameForService:"
+ "accessory:didUpdateDefaultNameForService:"
+ "accessory:didUpdateDevice:"
+ "accessory:didUpdateFirmwareUpdateAvailable:"
+ "accessory:didUpdateFirmwareVersion:"
+ "accessory:didUpdateHH1EOLEnabled:"
+ "accessory:didUpdateHasAuthorizationDataForCharacteristic:"
+ "accessory:didUpdateLastKnownOperatingStateResponseForService:"
+ "accessory:didUpdateLastKnownSleepDiscoveryModeForService:"
+ "accessory:didUpdateLoggedInAccount:"
+ "accessory:didUpdateNameForService:"
+ "accessory:didUpdatePairingIdentity:"
+ "accessory:didUpdateServiceSubtypeForService:"
+ "accessory:didUpdateSettings:"
+ "accessory:didUpdateSoftwareVersion:"
+ "accessory:didUpdateStoreID:"
+ "accessory:didUpdateSupportsUWBUnlock:"
+ "accessory:didUpdateSupportsWalletKey:"
+ "accessory:didUpdateWifiNetworkInfo:"
+ "accessory:service:didUpdateValueForCharacteristic:"
+ "accessoryDidRemoveSymptomsHandler:"
+ "accessoryDidSetHasOnboardedForAdaptiveTemperatureAutomations:"
+ "accessoryDidSetHasOnboardedForCleanEnergyAutomation:"
+ "accessoryDidSetHasOnboardedForNaturalLighting:"
+ "accessoryDidUpdateAdditionalSetupRequired:"
+ "accessoryDidUpdateApplicationData:"
+ "accessoryDidUpdateAudioDestination:"
+ "accessoryDidUpdateAudioDestinationController:"
+ "accessoryDidUpdateAudioReturnChannelSupport:"
+ "accessoryDidUpdateCalibrationStatus:"
+ "accessoryDidUpdateControllable:"
+ "accessoryDidUpdateDiagnosticsTransferSupport:"
+ "accessoryDidUpdateHomeLevelLocationServiceSettingSupport:"
+ "accessoryDidUpdateMultiUserSupport:"
+ "accessoryDidUpdateName:"
+ "accessoryDidUpdatePairingIdentity:"
+ "accessoryDidUpdatePendingConfigurationIdentifier:"
+ "accessoryDidUpdatePreferredMediaUser:"
+ "accessoryDidUpdateReachability:"
+ "accessoryDidUpdateReachableTransports:"
+ "accessoryDidUpdateServices:"
+ "accessoryDidUpdateSupportedCapabilities:"
+ "accessoryDidUpdateSupportsAnnounce:"
+ "accessoryDidUpdateSupportsAudioAnalysis:"
+ "accessoryDidUpdateSupportsCompanionInitiatedObliterate:"
+ "accessoryDidUpdateSupportsCompanionInitiatedRestart:"
+ "accessoryDidUpdateSupportsDoorbellChime:"
+ "accessoryDidUpdateSupportsDropIn:"
+ "accessoryDidUpdateSupportsJustSiri:"
+ "accessoryDidUpdateSupportsMediaActions:"
+ "accessoryDidUpdateSupportsMediaContentProfile:"
+ "accessoryDidUpdateSupportsMusicAlarm:"
+ "accessoryDidUpdateSupportsPreferredMediaUser:"
+ "accessoryDidUpdateSupportsRMVonAppleTV:"
+ "accessoryDidUpdateSupportsThirdPartyMusic:"
+ "accessoryDidUpdateSupportsUserMediaSettings:"
+ "accessoryDidUpdateTargetControlSupport:"
+ "accessorySettingsCache"
+ "accessorySettingsDataSource"
+ "accessorySettingsDataSource:didReceiveSettingsUpdatesForAccessoryWithIdentifier:settings:"
+ "accessoryWithUniqueIdentifier:"
+ "addDelegate:queue:"
+ "allHomes"
+ "allObjects"
+ "an_announceNotificationsEnabledForCurrentUserWithOverrideHomeLocationStatus:"
+ "an_announceSettingFromAccessorySettings"
+ "an_identifiers"
+ "an_isAnnounceEnabled"
+ "an_isAppleAnnounceAccessory"
+ "an_isAppleAnnounceHostAccessory"
+ "an_playedAnnouncements"
+ "an_supportsAnnounce"
+ "an_unplayedAnnouncements"
+ "announceAccessAllowedForCurrentUser"
+ "announceAccessAllowedForUser:"
+ "announceAccessoriesFromAccessories:"
+ "announceAccessoriesWithAnnounceEnabledFromAccessories:"
+ "announceDeviceNotificationModeToString:"
+ "announceUserSettings"
+ "append:"
+ "appleAnnounceAccessories"
+ "appleAnnounceAccessoriesFromAccessories:"
+ "appleAnnounceCapableAccessories"
+ "appleAnnounceHostAccessoriesFromAccessories:"
+ "bundleForLocationAuthorization"
+ "bundleWithPath:"
+ "cachedAccessorySettings"
+ "caseInsensitiveCompare:"
+ "com.apple.announce.homeManager"
+ "com.apple.announce.settingsCache"
+ "createAccessorySettingsDataSource"
+ "currentAccessory"
+ "currentHome"
+ "currentUser"
+ "dateByAddingTimeInterval:"
+ "defaultHomeOptions"
+ "delegatesToQueues"
+ "device"
+ "deviceNotificationMode"
+ "didAddHome:"
+ "didRemoveHome:"
+ "didUpdateHomes:"
+ "fetchAccessorySettingsWithHomeIdentifier:accessoryIdentifier:keyPaths:completionHandler:"
+ "fetchCachedAccessorySettingsWithHomeIdentifier:accessoryIdentifier:keyPaths:completionHandler:"
+ "finished"
+ "groups"
+ "hexCount"
+ "hmu_accessoriesExcludingCurrentAccessoryFromAccessories:"
+ "hmu_accessoriesFromAccessories:excludingStereoCompanionForAccessory:"
+ "hmu_allUsersIncludingCurrentUser"
+ "hmu_homesFromHomes:withRoomNames:"
+ "hmu_homesFromHomes:withZoneNames:"
+ "hmu_isEndpoint"
+ "hmu_isHomePod"
+ "hmu_isRemoteAccessAllowedForUser:"
+ "home:didAddAccessory:"
+ "home:didAddAccessoryNetworkProtectionGroup:"
+ "home:didAddActionSet:"
+ "home:didAddMediaSystem:"
+ "home:didAddResidentDevice:"
+ "home:didAddRoom:"
+ "home:didAddRoom:toZone:"
+ "home:didAddService:toServiceGroup:"
+ "home:didAddServiceGroup:"
+ "home:didAddTrigger:"
+ "home:didAddUser:"
+ "home:didAddZone:"
+ "home:didEncounterError:forAccessory:"
+ "home:didFailAccessorySetupWithError:"
+ "home:didRemoveAccessory:"
+ "home:didRemoveAccessoryNetworkProtectionGroup:"
+ "home:didRemoveActionSet:"
+ "home:didRemoveMediaSystem:"
+ "home:didRemoveResidentDevice:"
+ "home:didRemoveRoom:"
+ "home:didRemoveRoom:fromZone:"
+ "home:didRemoveService:fromServiceGroup:"
+ "home:didRemoveServiceGroup:"
+ "home:didRemoveTrigger:"
+ "home:didRemoveUser:"
+ "home:didRemoveZone:"
+ "home:didUnblockAccessory:"
+ "home:didUpdateAccessControlForUser:"
+ "home:didUpdateAccessoryInvitationsForUser:"
+ "home:didUpdateAccessoryNetworkProtectionGroup:"
+ "home:didUpdateActionSet:isExecuting:"
+ "home:didUpdateActionsForActionSet:"
+ "home:didUpdateApplicationDataForActionSet:"
+ "home:didUpdateApplicationDataForRoom:"
+ "home:didUpdateApplicationDataForServiceGroup:"
+ "home:didUpdateAreBulletinNotificationsSupported:"
+ "home:didUpdateAudioAnalysisClassifierOptions:"
+ "home:didUpdateAutomaticSoftwareUpdateEnabled:"
+ "home:didUpdateAutomaticThirdPartyAccessorySoftwareUpdateEnabled:"
+ "home:didUpdateDismissedWalletKeyUWBUnlockOnboarding:"
+ "home:didUpdateEventLogDuration:"
+ "home:didUpdateEventLogEnabled:"
+ "home:didUpdateHasOnboardedForWalletKey:"
+ "home:didUpdateHomeActivityState:isActivityStateHoldActive:activityStateHoldEndDate:transitionalStateEndDate:"
+ "home:didUpdateHomeActivityStateSchedule:"
+ "home:didUpdateHomeHubState:"
+ "home:didUpdateLastExecutionDateForActionSet:"
+ "home:didUpdateLocation:"
+ "home:didUpdateMediaPassword:"
+ "home:didUpdateMediaPeerToPeerEnabled:"
+ "home:didUpdateMinimumMediaUserPrivilege:"
+ "home:didUpdateNameForActionSet:"
+ "home:didUpdateNameForRoom:"
+ "home:didUpdateNameForServiceGroup:"
+ "home:didUpdateNameForTrigger:"
+ "home:didUpdateNameForZone:"
+ "home:didUpdateOnboardAudioAnalysis:"
+ "home:didUpdatePersonManagerSettings:"
+ "home:didUpdateReprovisionStateForAccessory:"
+ "home:didUpdateRoom:forAccessory:"
+ "home:didUpdateSiriPhraseOptions:"
+ "home:didUpdateStateForOutgoingInvitations:"
+ "home:didUpdateSupportsResidentActionSetStateEvaluation:"
+ "home:didUpdateTimeZone:"
+ "home:didUpdateTrigger:"
+ "homeAccessControlForUser:"
+ "homeDidAddWalletKey:"
+ "homeDidEnableLocationServices:"
+ "homeDidEnableMultiUser:"
+ "homeDidOnboardLocationServices:"
+ "homeDidRemoveWalletKey:"
+ "homeDidSetEnableDoorbellChime:"
+ "homeDidSetHasAnyUserAcknowledgedCameraRecordingOnboarding:"
+ "homeDidSetHasOnboardedForAccessCode:"
+ "homeDidUpdateAccessControlForCurrentUser:"
+ "homeDidUpdateApplicationData:"
+ "homeDidUpdateAssistantIdentifiers:"
+ "homeDidUpdateAutoSelectedPreferredResident:"
+ "homeDidUpdateHomeLocationStatus:"
+ "homeDidUpdateName:"
+ "homeDidUpdateNetworkRouterSupport:"
+ "homeDidUpdateOnboardedEventLog:"
+ "homeDidUpdatePrimaryResidentNetworkInfo:"
+ "homeDidUpdateProtectionMode:"
+ "homeDidUpdateSoundCheck:"
+ "homeDidUpdateSupportedFeatures:"
+ "homeDidUpdateSupportsResidentSelection:"
+ "homeDidUpdateToROAR:"
+ "homeDidUpdateUserSelectedPreferredResident:"
+ "homeForID:"
+ "homeLocationToString:"
+ "homeManager"
+ "homeManager:didAddHome:"
+ "homeManager:didReceiveAddAccessoryRequest:"
+ "homeManager:didRemoveHome:"
+ "homeManager:didUpdateAuthorizationStatus:"
+ "homeManagerDidUpdateHomes:"
+ "homeManagerDidUpdatePrimaryHome:"
+ "homeWithName:"
+ "homes"
+ "homesLoaded"
+ "homesLoadedCompletionHandlers"
+ "homesSupportingAnnounce"
+ "homesSupportingAnnounceFromHomes:"
+ "homesWithRoomNames:"
+ "homesWithZoneNames:"
+ "ies"
+ "initWithAccessorySettingsDataSource:"
+ "initWithBundle:"
+ "initWithCaching:"
+ "initWithCaching:homeOptions:"
+ "initWithConfiguration:"
+ "initWithHexCount:"
+ "initWithOptions:cachePolicy:"
+ "isAnnounceAccessAllowed"
+ "isAnnounceAvailable"
+ "isAnnounceEnabledForAnyAccessory"
+ "isAnnounceEnabledForAnyAccessoryOrUser"
+ "isAnnounceSupported"
+ "isControllable"
+ "isEqualToDate:"
+ "keyEnumerator"
+ "keyPath"
+ "lastAccessorySettingsFetch"
+ "loadHomeSynchronous"
+ "loadHomes:"
+ "loadHomesStart"
+ "mapTableWithKeyOptions:valueOptions:"
+ "na_filter:"
+ "na_firstObjectPassingTest:"
+ "numberWithUnsignedInt:"
+ "payload:keyTwo:"
+ "refreshHomeSynchronous"
+ "registerDelegate:queue:"
+ "removeAllObjects"
+ "room"
+ "root.announce"
+ "root.announce.enabled"
+ "rootGroup"
+ "s"
+ "setDelegateQueue:"
+ "setDiscretionary:"
+ "setHomesLoaded:"
+ "setInactiveUpdatingLevel:"
+ "setLocationAuthorization:"
+ "setPlaybackStoppedForAnnouncement:userInitiated:"
+ "settingsForAccessory:"
+ "settingsQueue"
+ "supportsAnnounce"
+ "supportsAudioAnalysis"
+ "supportsDropIn"
+ "timeIntervalSince1970"
+ "uniqueIdentifier"
+ "usersIncludingCurrentUserWithAnnounceAndRemoteAccessEnabled"
+ "usersIncludingCurrentUserWithAnnounceEnabled"
+ "usersWithAnnounceEnabled"
+ "v16@?0@\"<ANHomeManagerDelegate>\"8"
+ "v24@0:8@\"HMAccessory\"16"
+ "v24@0:8@\"HMHome\"16"
+ "v24@0:8@\"HMHomeManager\"16"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v24@?0@\"NSError\"8@\"NSArray\"16"
+ "v28@0:8@\"HMAccessory\"16B24"
+ "v28@0:8@\"HMHome\"16B24"
+ "v28@0:8@\"NSString\"16B24"
+ "v32@0:8@\"<DICHomeManagerDelegate>\"16@\"NSObject<OS_dispatch_queue>\"24"
+ "v32@0:8@\"HMAccessory\"16@\"ACAccount\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMAccessory\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMAccessoryProfile\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMAccessorySettings\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMCharacteristic\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMDevice\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMFPairingIdentity\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMFSoftwareVersion\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMFWiFiNetworkInfo\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMService\"24"
+ "v32@0:8@\"HMAccessory\"16@\"HMSymptomsHandler\"24"
+ "v32@0:8@\"HMAccessory\"16@\"NSString\"24"
+ "v32@0:8@\"HMHome\"16@\"CLLocation\"24"
+ "v32@0:8@\"HMHome\"16@\"HMAccessory\"24"
+ "v32@0:8@\"HMHome\"16@\"HMAccessoryNetworkProtectionGroup\"24"
+ "v32@0:8@\"HMHome\"16@\"HMActionSet\"24"
+ "v32@0:8@\"HMHome\"16@\"HMHomeActivityStateSchedule\"24"
+ "v32@0:8@\"HMHome\"16@\"HMHomePersonManagerSettings\"24"
+ "v32@0:8@\"HMHome\"16@\"HMMediaSystem\"24"
+ "v32@0:8@\"HMHome\"16@\"HMResidentDevice\"24"
+ "v32@0:8@\"HMHome\"16@\"HMRoom\"24"
+ "v32@0:8@\"HMHome\"16@\"HMServiceGroup\"24"
+ "v32@0:8@\"HMHome\"16@\"HMTrigger\"24"
+ "v32@0:8@\"HMHome\"16@\"HMUser\"24"
+ "v32@0:8@\"HMHome\"16@\"HMZone\"24"
+ "v32@0:8@\"HMHome\"16@\"NSArray\"24"
+ "v32@0:8@\"HMHome\"16@\"NSError\"24"
+ "v32@0:8@\"HMHome\"16@\"NSString\"24"
+ "v32@0:8@\"HMHome\"16@\"NSTimeZone\"24"
+ "v32@0:8@\"HMHome\"16Q24"
+ "v32@0:8@\"HMHome\"16q24"
+ "v32@0:8@\"HMHomeManager\"16@\"HMAddAccessoryRequest\"24"
+ "v32@0:8@\"HMHomeManager\"16@\"HMHome\"24"
+ "v32@0:8@\"HMHomeManager\"16Q24"
+ "v32@0:8@16q24"
+ "v36@0:8@\"HMHome\"16@\"HMActionSet\"24B32"
+ "v36@0:8@16@24B32"
+ "v40@0:8@\"HMAccessory\"16@\"HMService\"24@\"HMCharacteristic\"32"
+ "v40@0:8@\"HMAccessorySettingsDataSource\"16@\"NSUUID\"24@\"NSArray\"32"
+ "v40@0:8@\"HMHome\"16@\"HMRoom\"24@\"HMAccessory\"32"
+ "v40@0:8@\"HMHome\"16@\"HMRoom\"24@\"HMZone\"32"
+ "v40@0:8@\"HMHome\"16@\"HMService\"24@\"HMServiceGroup\"32"
+ "v40@0:8@\"HMHome\"16@\"NSError\"24@\"HMAccessory\"32"
+ "v40@0:8@16@24@32"
+ "v52@0:8@\"HMHome\"16Q24B32@\"NSDate\"36@\"NSDate\"44"
+ "v52@0:8@16Q24B32@36@44"
+ "y"
- "-[ANAnnounce lastPlayedAnnouncementInfo:]_block_invoke"
- "-[ANRemotePlaybackSession setPlaybackStoppedForAnnouncement:]_block_invoke"
- "[BOOL] Include recipients in communication user notificaitons"
- "lastPlayedAnnouncementInfo:"
- "setPlaybackEndedForAnnouncement:"
- "v24@0:8@?<v@?@\"NSDictionary\">16"

```
