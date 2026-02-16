## AnnounceDaemon

> `/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon`

```diff

-304.4.1.0.0
-  __TEXT.__text: 0x60a98
-  __TEXT.__auth_stubs: 0x12c0
-  __TEXT.__objc_methlist: 0x4294
-  __TEXT.__const: 0x1a08
-  __TEXT.__cstring: 0x2bd5
-  __TEXT.__oslogstring: 0x5f28
-  __TEXT.__gcc_except_tab: 0x1110
+314.0.0.0.0
+  __TEXT.__text: 0x5ad40
+  __TEXT.__auth_stubs: 0x1280
+  __TEXT.__objc_methlist: 0x364c
+  __TEXT.__const: 0x1978
+  __TEXT.__cstring: 0x2274
+  __TEXT.__oslogstring: 0x5538
+  __TEXT.__gcc_except_tab: 0xe44
   __TEXT.__constg_swiftt: 0x350
-  __TEXT.__swift5_typeref: 0xa6e
+  __TEXT.__swift5_typeref: 0xa6a
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x5c6
-  __TEXT.__swift5_assocty: 0x228
-  __TEXT.__swift5_proto: 0x14c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x1c0
+  __TEXT.__swift5_reflstr: 0x5a6
   __TEXT.__swift5_fieldmd: 0x368
+  __TEXT.__swift5_assocty: 0x210
+  __TEXT.__swift5_proto: 0x148
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1930
-  __TEXT.__eh_frame: 0x7e0
-  __TEXT.__objc_classname: 0xa1c
-  __TEXT.__objc_methname: 0xbb58
-  __TEXT.__objc_methtype: 0x2b5d
-  __TEXT.__objc_stubs: 0x8a60
-  __DATA_CONST.__got: 0x938
-  __DATA_CONST.__const: 0x16e8
-  __DATA_CONST.__objc_classlist: 0x170
-  __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x1c8
+  __TEXT.__unwind_info: 0x1790
+  __TEXT.__eh_frame: 0x808
+  __TEXT.__objc_classname: 0xaa9
+  __TEXT.__objc_methname: 0x9fe9
+  __TEXT.__objc_methtype: 0x26f5
+  __TEXT.__objc_stubs: 0x8720
+  __DATA_CONST.__got: 0x8c8
+  __DATA_CONST.__const: 0x14b8
+  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__objc_catlist: 0x88
+  __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d40
+  __DATA_CONST.__objc_selrefs: 0x26d0
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x108
-  __AUTH_CONST.__auth_got: 0x970
-  __AUTH_CONST.__const: 0x1540
-  __AUTH_CONST.__cfstring: 0x13a0
-  __AUTH_CONST.__objc_const: 0x5b60
+  __DATA_CONST.__objc_superrefs: 0xf0
+  __AUTH_CONST.__auth_got: 0x950
+  __AUTH_CONST.__const: 0x14a0
+  __AUTH_CONST.__cfstring: 0x12c0
+  __AUTH_CONST.__objc_const: 0x4ef0
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x7d8
+  __AUTH.__objc_data: 0x788
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x298
-  __DATA.__data: 0x1770
-  __DATA.__bss: 0x2a90
-  __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x9b8
+  __DATA.__objc_ivar: 0x264
+  __DATA.__data: 0x14f0
+  __DATA.__bss: 0x29f0
+  __DATA.__common: 0x10
+  __DATA_DIRTY.__objc_data: 0x918
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x110
+  __DATA_DIRTY.__bss: 0xf0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/Announce.framework/Announce
+  - /System/Library/PrivateFrameworks/AnnounceAppIntents.framework/AnnounceAppIntents
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/DropIn.framework/DropIn
   - /System/Library/PrivateFrameworks/DropInCore.framework/DropInCore
-  - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
   - /System/Library/PrivateFrameworks/HomeMessagingUtils.framework/HomeMessagingUtils
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 64D1504C-BE7D-3C45-B89E-ED0B82CBA9AC
-  Functions: 2014
-  Symbols:   5782
-  CStrings:  3268
+  UUID: AAED9681-D013-36BC-B787-E1B1A237B86C
+  Functions: 1835
+  Symbols:   5389
+  CStrings:  2881
 
Symbols:
+ +[ANAnnouncementManager managerWithEndpointID:storageManager:notificationController:]
+ -[ANAnnouncementCoordinator(Playback) setPlaybackStartedForAnnouncement:endpointID:clientIdentifier:]
+ -[ANAnnouncementCoordinator(Playback) setPlaybackStoppedForAnnouncement:endpointID:clientIdentifier:userInitiated:]
+ -[ANAnnouncementManager initWithEndpointID:storageManager:notificationController:]
+ -[ANAnnouncementManager notificationController]
+ -[ANAnnouncementManager storageManager]
+ -[ANPlaybackManager _updatePlaybackInfoForAnnouncementID:options:player:clientIdentifier:userInitiated:]
+ -[ANPlaybackManager _updatePlaybackInfoForAnnouncementID:options:player:clientIdentifier:userInitiated:].cold.1
+ -[ANPlaybackManager lastAnnouncementIndex]
+ -[ANPlaybackManager setLastAnnouncementIndex:]
+ -[ANPlaybackManager updatePlaybackForAnnouncementID:options:clientIdentifier:userInitiated:]
+ -[ANPlaybackSessionServiceListener setPlaybackStoppedForAnnouncement:userInitiated:]
+ _ANCreationTimestampKey
+ _OBJC_IVAR_$_ANAnnouncementManager._notificationController
+ _OBJC_IVAR_$_ANAnnouncementManager._storageManager
+ _OBJC_IVAR_$_ANPlaybackManager._lastAnnouncementIndex
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ __OBJC_$_CATEGORY_ANHomeManager_$_HomeContext
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_ANHomeManager_$_HomeContext
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_RPCompanionLinkDevice_Announce
+ __OBJC_$_CATEGORY_NSArray_$_RPCompanionLinkDevice_Announce
+ __OBJC_$_PROP_LIST_NSArray_$_RPCompanionLinkDevice_Announce
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ANAnnouncementManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ANAnnouncementStorage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ANUserNotificationControlling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ANAnnouncementManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ANAnnouncementStorage
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ANUserNotificationControlling
+ __OBJC_$_PROTOCOL_REFS_ANAnnouncementManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_ANAnnouncementStorage
+ __OBJC_$_PROTOCOL_REFS_ANUserNotificationControlling
+ __OBJC_CLASS_PROTOCOLS_$_ANUserNotificationController
+ __OBJC_LABEL_PROTOCOL_$_ANAnnouncementManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_ANAnnouncementStorage
+ __OBJC_LABEL_PROTOCOL_$_ANUserNotificationControlling
+ __OBJC_PROTOCOL_$_ANAnnouncementManagerDelegate
+ __OBJC_PROTOCOL_$_ANAnnouncementStorage
+ __OBJC_PROTOCOL_$_ANUserNotificationControlling
+ ___101-[ANAnnouncementCoordinator(Playback) setPlaybackStartedForAnnouncement:endpointID:clientIdentifier:]_block_invoke
+ ___115-[ANAnnouncementCoordinator(Playback) setPlaybackStoppedForAnnouncement:endpointID:clientIdentifier:userInitiated:]_block_invoke
+ ___49-[ANAnnouncementManager _loadStoredAnnouncements]_block_invoke.26
+ ___57-[ANAnnouncementCoordinator _handleReceivedAnnouncement:]_block_invoke.20
+ ___59-[ANAnnouncementManager addAnnouncement:completionHandler:]_block_invoke.5
+ ___71-[ANPlaybackSessionServiceListener listener:shouldAcceptNewConnection:]_block_invoke.22
+ ___92-[ANPlaybackManager updatePlaybackForAnnouncementID:options:clientIdentifier:userInitiated:]_block_invoke
+ ___96-[ANPlaybackSessionServiceListener _updateConnectionForReceivedAnnouncement:groupID:endpointID:]_block_invoke.77
+ ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.148
+ ___block_literal_global.28
+ ___block_literal_global.31
+ _objc_msgSend$_updatePlaybackInfoForAnnouncementID:options:player:clientIdentifier:userInitiated:
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$an_identifiers
+ _objc_msgSend$an_playedAnnouncements
+ _objc_msgSend$an_unplayedAnnouncements
+ _objc_msgSend$contentBodyForAnnouncers:inHome:
+ _objc_msgSend$contentByUpdatingWithProvider:error:
+ _objc_msgSend$hasCurrentCalls
+ _objc_msgSend$homesSupportingAnnounceFromHomes:
+ _objc_msgSend$initWithEndpointID:storageManager:notificationController:
+ _objc_msgSend$isPressDemoModeEnabled:
+ _objc_msgSend$isSecureDemoModeEnabled:
+ _objc_msgSend$isStoreDemoModeEnabled:
+ _objc_msgSend$lastAnnouncementIndex
+ _objc_msgSend$managerWithEndpointID:storageManager:notificationController:
+ _objc_msgSend$model
+ _objc_msgSend$notificationController
+ _objc_msgSend$observer:
+ _objc_msgSend$observer:didUpdateActiveCallStatus:
+ _objc_msgSend$playSystemSoundWithFileURL:completionHandler:
+ _objc_msgSend$playWithCompletionHandler:
+ _objc_msgSend$retrieveSessionWithID:
+ _objc_msgSend$setAnnouncement:
+ _objc_msgSend$setAssumedIdentity:
+ _objc_msgSend$setAttribute:forKey:error:
+ _objc_msgSend$setCompletionHandler:
+ _objc_msgSend$setFirstName:
+ _objc_msgSend$setInterruptionLevel:
+ _objc_msgSend$setLastAnnouncementIndex:
+ _objc_msgSend$setPlaybackStartedForAnnouncement:endpointID:clientIdentifier:
+ _objc_msgSend$setPlaybackStoppedForAnnouncement:endpointID:clientIdentifier:userInitiated:
+ _objc_msgSend$setShouldSuppressScreenLightUp:
+ _objc_msgSend$setThreadIdentifier:
+ _objc_msgSend$setType:
+ _objc_msgSend$setUnderlyingQueue:
+ _objc_msgSend$storageManager
+ _objc_msgSend$uniqueAnnouncersInAnnouncements:
+ _objc_msgSend$updatePlaybackForAnnouncementID:options:clientIdentifier:userInitiated:
- +[ANAnnouncementManager managerWithEndpointID:]
- +[ANHomeManager bundleForLocationAuthorization]
- +[ANHomeManager defaultHomeOptions]
- +[ANHomeManager shared]
- -[ANAccessorySettingsCache .cxx_destruct]
- -[ANAccessorySettingsCache _fetchSettingsForAccessory:useCache:]
- -[ANAccessorySettingsCache _removeSettingsForAccessoryWithIdentifier:]
- -[ANAccessorySettingsCache _updateSettings:forAccessoryWithIdentifier:]
- -[ANAccessorySettingsCache accessorySettingsDataSource:didReceiveSettingsUpdatesForAccessoryWithIdentifier:settings:]
- -[ANAccessorySettingsCache accessorySettingsDataSource]
- -[ANAccessorySettingsCache cachedAccessorySettings]
- -[ANAccessorySettingsCache initWithAccessorySettingsDataSource:]
- -[ANAccessorySettingsCache lastAccessorySettingsFetch]
- -[ANAccessorySettingsCache log]
- -[ANAccessorySettingsCache settingsForAccessory:]
- -[ANAccessorySettingsCache settingsQueue]
- -[ANAnalyticsCounter append:]
- -[ANAnalyticsCounter count]
- -[ANAnalyticsCounter finished]
- -[ANAnalyticsCounter hexCount]
- -[ANAnalyticsCounter initWithHexCount:]
- -[ANAnalyticsCounter init]
- -[ANAnalyticsCounter payload:keyTwo:]
- -[ANAnalyticsCounter setCount:]
- -[ANAnalyticsCounter setHexCount:]
- -[ANAnnounceServiceListener lastPlayedAnnouncementInfo:]
- -[ANAnnouncementCoordinator(Playback) setPlaybackStartedForAnnouncement:endpointID:]
- -[ANAnnouncementCoordinator(Playback) setPlaybackStoppedForAnnouncement:endpointID:]
- -[ANAnnouncementManager initWithEndpointID:]
- -[ANHomeManager .cxx_destruct]
- -[ANHomeManager _executeBlockForDelegates:]
- -[ANHomeManager _notifyManagerLoadedHomes:]
- -[ANHomeManager accessoryDidUpdateControllable:]
- -[ANHomeManager accessoryDidUpdateName:]
- -[ANHomeManager accessoryDidUpdateSupportsAudioAnalysis:]
- -[ANHomeManager accessoryDidUpdateSupportsDropIn:]
- -[ANHomeManager accessorySettingsCache]
- -[ANHomeManager addDelegate:queue:]
- -[ANHomeManager allHomes]
- -[ANHomeManager currentAccessory]
- -[ANHomeManager currentHome]
- -[ANHomeManager delegatesToQueues]
- -[ANHomeManager home:didAddAccessory:]
- -[ANHomeManager home:didAddUser:]
- -[ANHomeManager home:didRemoveAccessory:]
- -[ANHomeManager home:didRemoveUser:]
- -[ANHomeManager home:didUpdateAccessControlForUser:]
- -[ANHomeManager homeDidUpdateAccessControlForCurrentUser:]
- -[ANHomeManager homeManager:didAddHome:]
- -[ANHomeManager homeManager:didRemoveHome:]
- -[ANHomeManager homeManagerDidUpdateHomes:]
- -[ANHomeManager homeManager]
- -[ANHomeManager homesLoadedCompletionHandlers]
- -[ANHomeManager homesLoaded]
- -[ANHomeManager homes]
- -[ANHomeManager initWithCaching:]
- -[ANHomeManager initWithCaching:homeOptions:]
- -[ANHomeManager init]
- -[ANHomeManager loadHomeSynchronous]
- -[ANHomeManager loadHomes:]
- -[ANHomeManager loadHomesStart]
- -[ANHomeManager refreshHomeSynchronous]
- -[ANHomeManager registerDelegate:queue:]
- -[ANHomeManager serialQueue]
- -[ANHomeManager setHomesLoaded:]
- -[ANHomeManager(Home) homeForID:]
- -[ANHomeManager(Home) homeWithName:]
- -[ANHomeManager(Home) homesSupportingAnnounce]
- -[ANHomeManager(Home) homesWithRoomNames:]
- -[ANHomeManager(Home) homesWithZoneNames:]
- -[ANHomeManager(Home) isEndpointWithUUID:inRoomWithName:]
- -[ANHomeManager(Home) isLocalDeviceInRoom:]
- -[ANPlaybackManager _updatePlaybackInfoForAnnouncementID:options:player:]
- -[ANPlaybackManager _updatePlaybackInfoForAnnouncementID:options:player:].cold.1
- -[ANPlaybackManager lastAnnoucementIndex]
- -[ANPlaybackManager setLastAnnoucementIndex:]
- -[ANPlaybackManager updatePlaybackForAnnouncementID:options:]
- -[ANPlaybackSessionServiceListener appIntentConnectionListener]
- -[ANPlaybackSessionServiceListener setAppIntentConnectionListener:]
- -[ANPlaybackSessionServiceListener setPlaybackStoppedForAnnouncement:]
- -[HMAccessory(Announce) an_announceSettingFromAccessorySettings]
- -[HMAccessory(Announce) an_announceSettingFromAccessorySettings].cold.1
- -[HMHome(Announce) _usersWithAnnounceEnabledIncludingCurrentUser:]
- -[HMHome(Announce) announceAccessAllowedForCurrentUser]
- -[HMHome(Announce) announceAccessAllowedForUser:]
- -[HMHome(Announce) isAnnounceAvailable]
- -[HMHome(Announce) isAnnounceEnabledForAnyAccessoryOrUser]
- -[HMHome(Announce) isAnnounceEnabledForAnyAccessory]
- -[HMHome(Announce) isAnnounceSupported]
- -[HMHome(Announce) usersIncludingCurrentUserWithAnnounceAndRemoteAccessEnabled]
- -[HMHome(Announce) usersIncludingCurrentUserWithAnnounceEnabled]
- -[HMHome(Announce) usersWithAnnounceEnabled]
- -[NSArray(HMHome_Announce) an_homesSupportingAnnounce]
- GCC_except_table24
- GCC_except_table27
- GCC_except_table33
- GCC_except_table36
- GCC_except_table40
- GCC_except_table46
- GCC_except_table55
- GCC_except_table58
- GCC_except_table61
- _ANDefaultAccessorySettingsFetchTimeout
- _ANDefaultAccessorySettingsRefreshInterval
- _ANDefaultDisableHomeKitCaching
- _ANDefaultForceAllowAnnounceForAllAccessories
- _ANDefaultForceAllowAnnounceForAllUsers
- _ANDefaultForceAnnounceNotificationsForAllUsers
- _ANDefaultForceSupportsAnnounceForAllAccessories
- _ANDefaultHomeKitRefreshTimeout
- _ANLogHandleAccessory_Announce.logger
- _ANLogHandleAccessory_Announce.once
- _ANLogHandleHomeManager
- _ANLogHandleHomeManager.cold.1
- _ANLogHandleHomeManager.logger
- _ANLogHandleHomeManager.once
- _ANLogHandleHome_Announce
- _ANLogHandleHome_Announce.cold.1
- _ANLogHandleHome_Announce.logger
- _ANLogHandleHome_Announce.once
- _ANSettingKeyPathAnnounceEnabled
- _ANSettingKeyPathAnnounceGroup
- _OBJC_CLASS_$_ANAccessorySettingsCache
- _OBJC_CLASS_$_HMBooleanSetting
- _OBJC_CLASS_$_HMFLocationAuthorization
- _OBJC_CLASS_$_HMHomeManager
- _OBJC_CLASS_$_HMImmutableSetting
- _OBJC_CLASS_$_HMMutableHomeManagerConfiguration
- _OBJC_IVAR_$_ANAccessorySettingsCache._accessorySettingsDataSource
- _OBJC_IVAR_$_ANAccessorySettingsCache._cachedAccessorySettings
- _OBJC_IVAR_$_ANAccessorySettingsCache._lastAccessorySettingsFetch
- _OBJC_IVAR_$_ANAccessorySettingsCache._log
- _OBJC_IVAR_$_ANAccessorySettingsCache._settingsQueue
- _OBJC_IVAR_$_ANAnalyticsCounter._count
- _OBJC_IVAR_$_ANAnalyticsCounter._hexCount
- _OBJC_IVAR_$_ANHomeManager._accessorySettingsCache
- _OBJC_IVAR_$_ANHomeManager._delegatesToQueues
- _OBJC_IVAR_$_ANHomeManager._homeManager
- _OBJC_IVAR_$_ANHomeManager._homesLoaded
- _OBJC_IVAR_$_ANHomeManager._homesLoadedCompletionHandlers
- _OBJC_IVAR_$_ANHomeManager._loadHomesStart
- _OBJC_IVAR_$_ANHomeManager._serialQueue
- _OBJC_IVAR_$_ANPlaybackManager._lastAnnoucementIndex
- _OBJC_IVAR_$_ANPlaybackSessionServiceListener._appIntentConnectionListener
- _OBJC_METACLASS_$_ANAccessorySettingsCache
- _OBJC_METACLASS_$_ANAnalyticsCounter
- _OBJC_METACLASS_$_ANHomeManager
- __OBJC_$_CATEGORY_HMAccessory_$_Announce
- __OBJC_$_CATEGORY_HMHome_$_Announce
- __OBJC_$_CATEGORY_NSArray_$_HMHome_Announce
- __OBJC_$_CLASS_METHODS_ANHomeManager
- __OBJC_$_CLASS_METHODS_HMAccessory(Announce|AnnounceDaemon|AnnounceDaemon1)
- __OBJC_$_CLASS_PROP_LIST_ANHomeManager
- __OBJC_$_INSTANCE_METHODS_ANAccessorySettingsCache
- __OBJC_$_INSTANCE_METHODS_ANAnalyticsCounter
- __OBJC_$_INSTANCE_METHODS_ANHomeManager(Home|HomeContext)
- __OBJC_$_INSTANCE_METHODS_HMAccessory(Announce|AnnounceDaemon|AnnounceDaemon1)
- __OBJC_$_INSTANCE_METHODS_HMHome(Announce|AnnounceDaemon)
- __OBJC_$_INSTANCE_METHODS_NSArray(HMHome_Announce|RPCompanionLinkDevice_Announce)
- __OBJC_$_INSTANCE_VARIABLES_ANAccessorySettingsCache
- __OBJC_$_INSTANCE_VARIABLES_ANAnalyticsCounter
- __OBJC_$_INSTANCE_VARIABLES_ANHomeManager
- __OBJC_$_PROP_LIST_ANAccessorySettingsCache
- __OBJC_$_PROP_LIST_ANAnalyticsCounter
- __OBJC_$_PROP_LIST_ANAnalyticsDailyHomesProvider
- __OBJC_$_PROP_LIST_DICHomeManagerProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ANAnalyticsDailyHomesProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ANAnnouncementManagerDelegte
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_DICHomeManagerProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMAccessoryDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMAccessoryDelegatePrivate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMAccessorySettingsDataSourceDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMHomeDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMHomeDelegatePrivate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMHomeManagerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_ANAnalyticsDailyHomesProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_ANAnnouncementManagerDelegte
- __OBJC_$_PROTOCOL_METHOD_TYPES_DICHomeManagerProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_HMAccessoryDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_HMAccessoryDelegatePrivate
- __OBJC_$_PROTOCOL_METHOD_TYPES_HMAccessorySettingsDataSourceDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_HMHomeDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_HMHomeDelegatePrivate
- __OBJC_$_PROTOCOL_METHOD_TYPES_HMHomeManagerDelegate
- __OBJC_$_PROTOCOL_REFS_ANAnalyticsDailyHomesProvider
- __OBJC_$_PROTOCOL_REFS_ANAnnouncementManagerDelegte
- __OBJC_$_PROTOCOL_REFS_DICHomeManagerProviding
- __OBJC_$_PROTOCOL_REFS_HMAccessoryDelegate
- __OBJC_$_PROTOCOL_REFS_HMAccessoryDelegatePrivate
- __OBJC_$_PROTOCOL_REFS_HMAccessorySettingsDataSourceDelegate
- __OBJC_$_PROTOCOL_REFS_HMHomeDelegate
- __OBJC_$_PROTOCOL_REFS_HMHomeDelegatePrivate
- __OBJC_$_PROTOCOL_REFS_HMHomeManagerDelegate
- __OBJC_CLASS_PROTOCOLS_$_ANAccessorySettingsCache
- __OBJC_CLASS_PROTOCOLS_$_ANHomeManager
- __OBJC_CLASS_RO_$_ANAccessorySettingsCache
- __OBJC_CLASS_RO_$_ANAnalyticsCounter
- __OBJC_CLASS_RO_$_ANHomeManager
- __OBJC_LABEL_PROTOCOL_$_ANAnalyticsDailyHomesProvider
- __OBJC_LABEL_PROTOCOL_$_ANAnnouncementManagerDelegte
- __OBJC_LABEL_PROTOCOL_$_DICHomeManagerProviding
- __OBJC_LABEL_PROTOCOL_$_HMAccessoryDelegate
- __OBJC_LABEL_PROTOCOL_$_HMAccessoryDelegatePrivate
- __OBJC_LABEL_PROTOCOL_$_HMAccessorySettingsDataSourceDelegate
- __OBJC_LABEL_PROTOCOL_$_HMHomeDelegate
- __OBJC_LABEL_PROTOCOL_$_HMHomeDelegatePrivate
- __OBJC_LABEL_PROTOCOL_$_HMHomeManagerDelegate
- __OBJC_METACLASS_RO_$_ANAccessorySettingsCache
- __OBJC_METACLASS_RO_$_ANAnalyticsCounter
- __OBJC_METACLASS_RO_$_ANHomeManager
- __OBJC_PROTOCOL_$_ANAnalyticsDailyHomesProvider
- __OBJC_PROTOCOL_$_ANAnnouncementManagerDelegte
- __OBJC_PROTOCOL_$_DICHomeManagerProviding
- __OBJC_PROTOCOL_$_HMAccessoryDelegate
- __OBJC_PROTOCOL_$_HMAccessoryDelegatePrivate
- __OBJC_PROTOCOL_$_HMAccessorySettingsDataSourceDelegate
- __OBJC_PROTOCOL_$_HMHomeDelegate
- __OBJC_PROTOCOL_$_HMHomeDelegatePrivate
- __OBJC_PROTOCOL_$_HMHomeManagerDelegate
- ___117-[ANAccessorySettingsCache accessorySettingsDataSource:didReceiveSettingsUpdatesForAccessoryWithIdentifier:settings:]_block_invoke
- ___23+[ANHomeManager shared]_block_invoke
- ___25-[ANHomeManager allHomes]_block_invoke
- ___27-[ANHomeManager loadHomes:]_block_invoke
- ___33-[ANHomeManager home:didAddUser:]_block_invoke
- ___33-[ANHomeManager home:didAddUser:]_block_invoke.46
- ___36-[ANHomeManager home:didRemoveUser:]_block_invoke
- ___36-[ANHomeManager home:didRemoveUser:]_block_invoke.49
- ___38-[ANHomeManager home:didAddAccessory:]_block_invoke
- ___38-[ANHomeManager home:didAddAccessory:]_block_invoke.40
- ___39-[ANHomeManager refreshHomeSynchronous]_block_invoke
- ___40-[ANHomeManager accessoryDidUpdateName:]_block_invoke
- ___40-[ANHomeManager accessoryDidUpdateName:]_block_invoke.56
- ___40-[ANHomeManager homeManager:didAddHome:]_block_invoke
- ___40-[ANHomeManager homeManager:didAddHome:]_block_invoke.28
- ___40-[ANHomeManager registerDelegate:queue:]_block_invoke
- ___41-[ANHomeManager home:didRemoveAccessory:]_block_invoke
- ___41-[ANHomeManager home:didRemoveAccessory:]_block_invoke.43
- ___43-[ANHomeManager _executeBlockForDelegates:]_block_invoke
- ___43-[ANHomeManager _executeBlockForDelegates:]_block_invoke_2
- ___43-[ANHomeManager homeManager:didRemoveHome:]_block_invoke
- ___43-[ANHomeManager homeManager:didRemoveHome:]_block_invoke.31
- ___43-[ANHomeManager homeManagerDidUpdateHomes:]_block_invoke
- ___43-[ANHomeManager homeManagerDidUpdateHomes:]_block_invoke.24
- ___48-[ANHomeManager accessoryDidUpdateControllable:]_block_invoke
- ___48-[ANHomeManager accessoryDidUpdateControllable:]_block_invoke.53
- ___49-[ANAccessorySettingsCache settingsForAccessory:]_block_invoke
- ___49-[ANAnnouncementManager _loadStoredAnnouncements]_block_invoke.28
- ___50-[ANHomeManager accessoryDidUpdateSupportsDropIn:]_block_invoke
- ___50-[ANHomeManager accessoryDidUpdateSupportsDropIn:]_block_invoke.62
- ___52-[ANHomeManager home:didUpdateAccessControlForUser:]_block_invoke
- ___52-[ANHomeManager home:didUpdateAccessControlForUser:]_block_invoke.37
- ___52-[ANHomeManager home:didUpdateAccessControlForUser:]_block_invoke_2
- ___57-[ANAnnouncementCoordinator _handleReceivedAnnouncement:]_block_invoke.19
- ___57-[ANHomeManager accessoryDidUpdateSupportsAudioAnalysis:]_block_invoke
- ___57-[ANHomeManager accessoryDidUpdateSupportsAudioAnalysis:]_block_invoke.59
- ___58-[ANHomeManager homeDidUpdateAccessControlForCurrentUser:]_block_invoke
- ___58-[ANHomeManager homeDidUpdateAccessControlForCurrentUser:]_block_invoke.34
- ___59-[ANAnnouncementManager addAnnouncement:completionHandler:]_block_invoke.6
- ___61-[ANPlaybackManager updatePlaybackForAnnouncementID:options:]_block_invoke
- ___64-[ANAccessorySettingsCache _fetchSettingsForAccessory:useCache:]_block_invoke
- ___64-[ANAccessorySettingsCache _fetchSettingsForAccessory:useCache:]_block_invoke.10
- ___64-[ANAccessorySettingsCache _fetchSettingsForAccessory:useCache:]_block_invoke.13
- ___64-[ANAccessorySettingsCache _fetchSettingsForAccessory:useCache:]_block_invoke.9
- ___64-[ANAccessorySettingsCache _fetchSettingsForAccessory:useCache:]_block_invoke.cold.1
- ___64-[HMAccessory(Announce) an_announceSettingFromAccessorySettings]_block_invoke
- ___64-[HMAccessory(Announce) an_announceSettingFromAccessorySettings]_block_invoke.8
- ___66-[HMHome(Announce) _usersWithAnnounceEnabledIncludingCurrentUser:]_block_invoke
- ___71-[ANPlaybackSessionServiceListener listener:shouldAcceptNewConnection:]_block_invoke.24
- ___84-[ANAnnouncementCoordinator(Playback) setPlaybackStartedForAnnouncement:endpointID:]_block_invoke
- ___84-[ANAnnouncementCoordinator(Playback) setPlaybackStoppedForAnnouncement:endpointID:]_block_invoke
- ___96-[ANPlaybackSessionServiceListener _updateConnectionForReceivedAnnouncement:groupID:endpointID:]_block_invoke.78
- ___ANLogHandleAccessory_Announce_block_invoke
- ___ANLogHandleHomeManager_block_invoke
- ___ANLogHandleHome_Announce_block_invoke
- ___block_descriptor_32_e28_B16?0"HMAccessorySetting"8l
- ___block_descriptor_32_e33_B16?0"HMAccessorySettingGroup"8l
- ___block_descriptor_40_e8_32s_e16_B16?0"HMUser"8ls32l8
- ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
- ___block_descriptor_40_e8_32s_e33_v16?0"<ANHomeManagerDelegate>"8ls32l8
- ___block_descriptor_48_e8_32s40s_e33_v16?0"<ANHomeManagerDelegate>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
- ___block_descriptor_56_e8_32s40r48w_e5_v8?0lw48l8r40l8s32l8
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
- ___block_descriptor_64_e8_32s40s48r56w_e5_v8?0lw56l8s32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8s40l8s48l8w56l8
- ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8s40l8w56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8r64l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64r72w_e29_v24?0"NSError"8"NSArray"16lw72l8s32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
- ___block_literal_global.11
- ___block_literal_global.143
- ___block_literal_global.15
- ___block_literal_global.30
- ___block_literal_global.33
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_fetchSettingsForAccessory:useCache:
- _objc_msgSend$_notifyManagerLoadedHomes:
- _objc_msgSend$_refreshBeforeDate:completionHandler:
- _objc_msgSend$_updatePlaybackInfoForAnnouncementID:options:player:
- _objc_msgSend$_updateSettings:forAccessoryWithIdentifier:
- _objc_msgSend$_usersWithAnnounceEnabledIncludingCurrentUser:
- _objc_msgSend$accessoryDidUpdateControllable:
- _objc_msgSend$accessoryDidUpdateName:
- _objc_msgSend$accessoryDidUpdateSupportedCapabilities:
- _objc_msgSend$accessorySettingsDataSource
- _objc_msgSend$an_homesSupportingAnnounce
- _objc_msgSend$bundleForLocationAuthorization
- _objc_msgSend$bundleWithPath:
- _objc_msgSend$cachedAccessorySettings
- _objc_msgSend$caseInsensitiveCompare:
- _objc_msgSend$createAccessorySettingsDataSource
- _objc_msgSend$defaultHomeOptions
- _objc_msgSend$didAddHome:
- _objc_msgSend$didRemoveHome:
- _objc_msgSend$didUpdateHomes:
- _objc_msgSend$fetchAccessorySettingsWithHomeIdentifier:accessoryIdentifier:keyPaths:completionHandler:
- _objc_msgSend$fetchCachedAccessorySettingsWithHomeIdentifier:accessoryIdentifier:keyPaths:completionHandler:
- _objc_msgSend$groups
- _objc_msgSend$hmu_accessoriesExcludingCurrentAccessoryFromAccessories:
- _objc_msgSend$hmu_accessoriesFromAccessories:excludingStereoCompanionForAccessory:
- _objc_msgSend$home:didAddAccessory:
- _objc_msgSend$home:didAddUser:
- _objc_msgSend$home:didRemoveAccessory:
- _objc_msgSend$home:didRemoveUser:
- _objc_msgSend$home:didUpdateAccessControlForUser:
- _objc_msgSend$homeAccessControlForUser:
- _objc_msgSend$homeDidUpdateAccessControlForCurrentUser:
- _objc_msgSend$homeManager
- _objc_msgSend$homesLoadedCompletionHandlers
- _objc_msgSend$identifiers
- _objc_msgSend$initWithAccessorySettingsDataSource:
- _objc_msgSend$initWithBundle:
- _objc_msgSend$initWithCaching:
- _objc_msgSend$initWithCaching:homeOptions:
- _objc_msgSend$initWithOptions:cachePolicy:
- _objc_msgSend$isAnnounceAccessAllowed
- _objc_msgSend$isAnnounceSupported
- _objc_msgSend$keyPath
- _objc_msgSend$lastAccessorySettingsFetch
- _objc_msgSend$lastAnnoucementIndex
- _objc_msgSend$loadHomes:
- _objc_msgSend$loadHomesStart
- _objc_msgSend$numberWithUnsignedInt:
- _objc_msgSend$playedAnnouncements
- _objc_msgSend$rootGroup
- _objc_msgSend$setDiscretionary:
- _objc_msgSend$setHomesLoaded:
- _objc_msgSend$setInactiveUpdatingLevel:
- _objc_msgSend$setLastAnnoucementIndex:
- _objc_msgSend$setLocationAuthorization:
- _objc_msgSend$setPlaybackStartedForAnnouncement:endpointID:
- _objc_msgSend$setPlaybackStoppedForAnnouncement:endpointID:
- _objc_msgSend$settingsQueue
- _objc_msgSend$supportsAudioAnalysis
- _objc_msgSend$supportsDropIn
- _objc_msgSend$unplayedAnnouncements
- _objc_msgSend$updatePlaybackForAnnouncementID:options:
- _objc_msgSend$usersWithAnnounceEnabled
- _objc_msgSend$value
- _objc_retain_x9
- _shared.manager
- _swift_dynamicCastObjCClass
- _symbolic Si
CStrings:
+ "@\"<ANAnnouncementManagerDelegate>\""
+ "@\"<ANAnnouncementStorage>\""
+ "@\"<ANUserNotificationControlling>\""
+ "@\"NSArray\"24@0:8@\"NSUUID\"16"
+ "ANAnnouncementManagerDelegate"
+ "ANAnnouncementStorage"
+ "ANUserNotificationControlling"
+ "B24@0:8@\"NSString\"16"
+ "B32@0:8@\"ANAnnouncement\"16@\"HMHome\"24"
+ "T@\"<ANAnnouncementManagerDelegate>\",W,N,V_delegate"
+ "T@\"<ANAnnouncementStorage>\",R,N,V_storageManager"
+ "T@\"<ANUserNotificationControlling>\",R,N,V_notificationController"
+ "Tq,N,V_lastAnnouncementIndex"
+ "_lastAnnouncementIndex"
+ "_notificationController"
+ "_storageManager"
+ "_updatePlaybackInfoForAnnouncementID:options:player:clientIdentifier:userInitiated:"
+ "an_identifiers"
+ "an_playedAnnouncements"
+ "an_unplayedAnnouncements"
+ "homesSupportingAnnounceFromHomes:"
+ "initWithEndpointID:storageManager:notificationController:"
+ "lastAnnouncementIndex"
+ "managerWithEndpointID:storageManager:notificationController:"
+ "notificationController"
+ "setLastAnnouncementIndex:"
+ "setPlaybackStartedForAnnouncement:endpointID:clientIdentifier:"
+ "setPlaybackStoppedForAnnouncement:endpointID:clientIdentifier:userInitiated:"
+ "setPlaybackStoppedForAnnouncement:userInitiated:"
+ "storageManager"
+ "updatePlaybackForAnnouncementID:options:clientIdentifier:userInitiated:"
+ "v28@0:8@\"NSString\"16B24"
+ "v32@0:8@\"NSArray\"16@\"NSUUID\"24"
+ "v32@0:8@\"NSString\"16@\"NSUUID\"24"
+ "v40@0:8@\"NSArray\"16@\"HMHome\"24@\"NSString\"32"
+ "v44@0:8@16@24@32B40"
+ "v44@0:8@16Q24@32B40"
+ "v48@0:8@\"ANAnnouncement\"16@\"NSArray\"24@\"HMHome\"32@\"NSString\"40"
+ "v52@0:8@16Q24@32@40B48"
- " (including current user)"
- "%@%lu accessor%s with announce enabled"
- "%@%lu accessor%s with announce enabled.  %ld user%s with announce enabled"
- "%@Access Control Changed for Current User in Home: %@"
- "%@Access Control Changed for User %@ in Home: %@"
- "%@Accessory Controllable Updated: %@, %@"
- "%@Accessory Name Updated: %@, %@"
- "%@Accessory Supports Audio Analysis Updated: %@, %@, Supports Audio Analysis = %d"
- "%@Accessory Supports Drop In Updated: %@, %@, Supports Drop In = %d"
- "%@Added Accessory %@, %@"
- "%@Added Home %@, %@"
- "%@Announce Access Allowed For User (Name = %@, ID = %@): %@"
- "%@Announce is DISABLED For User (Name = %@, ID = %@)"
- "%@Failed to find Announce Setting Group in Accessory Settings %@"
- "%@Home has %ld users%s, %ld have intercom enabled"
- "%@Home manager refresh %@"
- "%@Home manager refresh start (%.2fs timeout)"
- "%@HomeKit Added User %@, %@, %@"
- "%@HomeKit Removed User %@, %@, %@"
- "%@Homes Already Loaded"
- "%@Homes Loaded: %@"
- "%@Load Homes took %f seconds"
- "%@Loaded Homes Synchronous: %@"
- "%@Loaded homes %@"
- "%@Loading Homes"
- "%@No bundle for location authorization"
- "%@Notifying Homes Loaded to %i handlers"
- "%@Notifying delegate homes loaded: %@"
- "%@Removed Accessory %@, %@"
- "%@Removed Home %@, %@"
- "%@[Override] Force Allow Announce For User (Name = %@, ID = %@) Enabled"
- "%@[Override] Setting HomeKit Cache Policy to None. Actual = %lu"
- "%@allHomes timeout waiting for loaded Homes after %d seconds"
- "/System/Library/LocationBundles/HomeKitDaemon.framework"
- "@\"<ANAnnouncementManagerDelegte>\""
- "@\"ANAccessorySettingsCache\""
- "@\"ANAppIntentsConnectionListener\""
- "@\"HMAccessory\"16@0:8"
- "@\"HMAccessorySettingsDataSource\""
- "@\"HMHome\"16@0:8"
- "@\"HMHomeManager\""
- "@20@0:8B16"
- "@28@0:8@16B24"
- "@28@0:8B16Q20"
- "ANAccessorySettingsCache"
- "ANAnalyticsCounter"
- "ANAnalyticsDailyHomesProvider"
- "ANAnnouncementManagerDelegte"
- "ANHomeManager"
- "AccessorySettingsCache"
- "Accessory_Announce"
- "Announce Enabled Setting For Accessory %@: %{bool}d"
- "Announce is DISABLED For Accessory %@"
- "Announce setting not found in accessory settings"
- "Announce setting not found in settings from data source"
- "AnnounceDaemon1"
- "Attempting to use locally-cached settings"
- "B16@?0@\"HMAccessorySetting\"8"
- "B16@?0@\"HMAccessorySettingGroup\"8"
- "B16@?0@\"HMUser\"8"
- "B24@0:8q16"
- "Cached Settings"
- "Current User Announce Notification Mode: %{public}s"
- "Current User is not in Home %@ (Current Home Location Status = %s (%ld). Not posting user notification."
- "DICHomeManagerProviding"
- "Failed to retrieve %{public}@ for Accessory %@, %@: %@"
- "Fetched %{public}@ for Accessory %@, %@: %@"
- "Fetching %{public}@ for Accessory %@, %@"
- "HMAccessoryDelegate"
- "HMAccessoryDelegatePrivate"
- "HMAccessorySettingsDataSourceDelegate"
- "HMHomeDelegate"
- "HMHomeDelegatePrivate"
- "HMHomeManagerDelegate"
- "HMHome_Announce"
- "HomeManager"
- "Home_Announce"
- "Override Home Location Status: %s (%ld), Current Home Location Status: %s (%ld), Home: %@"
- "Received Settings Updates for Accessory Identifier %@: %@"
- "Settings"
- "Settings need refresh for accessory %@, %@"
- "Settings not found in settings from data source"
- "Supports Announce for Accessory %@: %{bool}d"
- "T@\"<ANAnnouncementManagerDelegte>\",W,N,V_delegate"
- "T@\"ANAccessorySettingsCache\",R,N,V_accessorySettingsCache"
- "T@\"ANAppIntentsConnectionListener\",&,N,V_appIntentConnectionListener"
- "T@\"HMAccessory\",R,N"
- "T@\"HMAccessorySettingsDataSource\",R,N,V_accessorySettingsDataSource"
- "T@\"HMHomeManager\",R,N,V_homeManager"
- "T@\"NSArray\",N,R"
- "T@\"NSDate\",R,N,V_loadHomesStart"
- "T@\"NSMutableArray\",R,N,V_homesLoadedCompletionHandlers"
- "T@\"NSMutableDictionary\",R,N,V_cachedAccessorySettings"
- "T@\"NSMutableDictionary\",R,N,V_lastAccessorySettingsFetch"
- "T@\"NSNumber\",R,N"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_settingsQueue"
- "TB,N,V_homesLoaded"
- "TI,N,V_count"
- "TQ,N,V_hexCount"
- "Timed-out waiting for Accessory %{public}@ for %@, %@"
- "Tq,N,V_lastAnnoucementIndex"
- "WARNING: Using cached settings for accessory. Value may be stale. %@, %@"
- "[Override] Force Allow Announce For Accessory %@ Enabled"
- "[Override] Force Announce Notifications Enabled"
- "[Override] Force Announce Supported For Accessory %@ Enabled"
- "_accessorySettingsCache"
- "_accessorySettingsDataSource"
- "_appIntentConnectionListener"
- "_cachedAccessorySettings"
- "_count"
- "_fetchSettingsForAccessory:useCache:"
- "_hexCount"
- "_homeManager"
- "_homesLoaded"
- "_homesLoadedCompletionHandlers"
- "_lastAccessorySettingsFetch"
- "_lastAnnoucementIndex"
- "_loadHomesStart"
- "_notifyManagerLoadedHomes:"
- "_refreshBeforeDate:completionHandler:"
- "_removeSettingsForAccessoryWithIdentifier:"
- "_settingsQueue"
- "_updatePlaybackInfoForAnnouncementID:options:player:"
- "_updateSettings:forAccessoryWithIdentifier:"
- "_usersWithAnnounceEnabledIncludingCurrentUser:"
- "accessory:didAddControlTarget:"
- "accessory:didAddProfile:"
- "accessory:didAddSymptomsHandler:"
- "accessory:didRemoveControlTarget:"
- "accessory:didRemoveProfile:"
- "accessory:didUpdateApplicationDataForService:"
- "accessory:didUpdateAssociatedServiceTypeForService:"
- "accessory:didUpdateBulletinBoardNotificationForService:"
- "accessory:didUpdateBundleID:"
- "accessory:didUpdateConfigurationStateForService:"
- "accessory:didUpdateConfiguredNameForService:"
- "accessory:didUpdateDefaultNameForService:"
- "accessory:didUpdateDevice:"
- "accessory:didUpdateFirmwareUpdateAvailable:"
- "accessory:didUpdateFirmwareVersion:"
- "accessory:didUpdateHH1EOLEnabled:"
- "accessory:didUpdateHasAuthorizationDataForCharacteristic:"
- "accessory:didUpdateLastKnownOperatingStateResponseForService:"
- "accessory:didUpdateLastKnownSleepDiscoveryModeForService:"
- "accessory:didUpdateLoggedInAccount:"
- "accessory:didUpdateNameForService:"
- "accessory:didUpdatePairingIdentity:"
- "accessory:didUpdateServiceSubtypeForService:"
- "accessory:didUpdateSettings:"
- "accessory:didUpdateSoftwareVersion:"
- "accessory:didUpdateStoreID:"
- "accessory:didUpdateSupportsUWBUnlock:"
- "accessory:didUpdateSupportsWalletKey:"
- "accessory:didUpdateWifiNetworkInfo:"
- "accessory:service:didUpdateValueForCharacteristic:"
- "accessoryDidRemoveSymptomsHandler:"
- "accessoryDidSetHasOnboardedForAdaptiveTemperatureAutomations:"
- "accessoryDidSetHasOnboardedForCleanEnergyAutomation:"
- "accessoryDidSetHasOnboardedForNaturalLighting:"
- "accessoryDidUpdateAdditionalSetupRequired:"
- "accessoryDidUpdateApplicationData:"
- "accessoryDidUpdateAudioDestination:"
- "accessoryDidUpdateAudioDestinationController:"
- "accessoryDidUpdateAudioReturnChannelSupport:"
- "accessoryDidUpdateCalibrationStatus:"
- "accessoryDidUpdateDiagnosticsTransferSupport:"
- "accessoryDidUpdateHomeLevelLocationServiceSettingSupport:"
- "accessoryDidUpdateMultiUserSupport:"
- "accessoryDidUpdatePairingIdentity:"
- "accessoryDidUpdatePendingConfigurationIdentifier:"
- "accessoryDidUpdatePreferredMediaUser:"
- "accessoryDidUpdateReachability:"
- "accessoryDidUpdateReachableTransports:"
- "accessoryDidUpdateServices:"
- "accessoryDidUpdateSupportsAnnounce:"
- "accessoryDidUpdateSupportsAudioAnalysis:"
- "accessoryDidUpdateSupportsCompanionInitiatedObliterate:"
- "accessoryDidUpdateSupportsCompanionInitiatedRestart:"
- "accessoryDidUpdateSupportsDoorbellChime:"
- "accessoryDidUpdateSupportsDropIn:"
- "accessoryDidUpdateSupportsJustSiri:"
- "accessoryDidUpdateSupportsMediaActions:"
- "accessoryDidUpdateSupportsMediaContentProfile:"
- "accessoryDidUpdateSupportsMusicAlarm:"
- "accessoryDidUpdateSupportsPreferredMediaUser:"
- "accessoryDidUpdateSupportsRMVonAppleTV:"
- "accessoryDidUpdateSupportsThirdPartyMusic:"
- "accessoryDidUpdateSupportsUserMediaSettings:"
- "accessoryDidUpdateTargetControlSupport:"
- "accessorySettingsCache"
- "accessorySettingsDataSource"
- "accessorySettingsDataSource:didReceiveSettingsUpdatesForAccessoryWithIdentifier:settings:"
- "an_announceSettingFromAccessorySettings"
- "an_homesSupportingAnnounce"
- "an_isAppleAnnounceAccessory"
- "an_isAppleAnnounceHostAccessory"
- "appIntentConnectionListener"
- "appleAnnounceAccessoriesFromAccessories:"
- "bundleForLocationAuthorization"
- "bundleWithPath:"
- "cachedAccessorySettings"
- "caseInsensitiveCompare:"
- "com.apple.announce.homeManager"
- "com.apple.announce.settingsCache"
- "createAccessorySettingsDataSource"
- "defaultHomeOptions"
- "fetchAccessorySettingsWithHomeIdentifier:accessoryIdentifier:keyPaths:completionHandler:"
- "fetchCachedAccessorySettingsWithHomeIdentifier:accessoryIdentifier:keyPaths:completionHandler:"
- "groups"
- "hmu_accessoriesExcludingCurrentAccessoryFromAccessories:"
- "hmu_accessoriesFromAccessories:excludingStereoCompanionForAccessory:"
- "home:didAddAccessoryNetworkProtectionGroup:"
- "home:didAddActionSet:"
- "home:didAddMediaSystem:"
- "home:didAddResidentDevice:"
- "home:didAddRoom:"
- "home:didAddRoom:toZone:"
- "home:didAddService:toServiceGroup:"
- "home:didAddServiceGroup:"
- "home:didAddTrigger:"
- "home:didAddZone:"
- "home:didEncounterError:forAccessory:"
- "home:didFailAccessorySetupWithError:"
- "home:didRemoveAccessoryNetworkProtectionGroup:"
- "home:didRemoveActionSet:"
- "home:didRemoveMediaSystem:"
- "home:didRemoveResidentDevice:"
- "home:didRemoveRoom:"
- "home:didRemoveRoom:fromZone:"
- "home:didRemoveService:fromServiceGroup:"
- "home:didRemoveServiceGroup:"
- "home:didRemoveTrigger:"
- "home:didRemoveZone:"
- "home:didUnblockAccessory:"
- "home:didUpdateAccesoryInvitationsForUser:"
- "home:didUpdateAccessoryNetworkProtectionGroup:"
- "home:didUpdateActionSet:isExecuting:"
- "home:didUpdateActionsForActionSet:"
- "home:didUpdateApplicationDataForActionSet:"
- "home:didUpdateApplicationDataForRoom:"
- "home:didUpdateApplicationDataForServiceGroup:"
- "home:didUpdateAreBulletinNotificationsSupported:"
- "home:didUpdateAudioAnalysisClassifierOptions:"
- "home:didUpdateAutomaticSoftwareUpdateEnabled:"
- "home:didUpdateAutomaticThirdPartyAccessorySoftwareUpdateEnabled:"
- "home:didUpdateDismissedWalletKeyUWBUnlockOnboarding:"
- "home:didUpdateEventLogDuration:"
- "home:didUpdateEventLogEnabled:"
- "home:didUpdateHasOnboardedForWalletKey:"
- "home:didUpdateHomeActivityState:isActivityStateHoldActive:activityStateHoldEndDate:transitionalStateEndDate:"
- "home:didUpdateHomeActivityStateSchedule:"
- "home:didUpdateHomeHubState:"
- "home:didUpdateLastExecutionDateForActionSet:"
- "home:didUpdateLocation:"
- "home:didUpdateMediaPassword:"
- "home:didUpdateMediaPeerToPeerEnabled:"
- "home:didUpdateMinimumMediaUserPrivilege:"
- "home:didUpdateNameForActionSet:"
- "home:didUpdateNameForRoom:"
- "home:didUpdateNameForServiceGroup:"
- "home:didUpdateNameForTrigger:"
- "home:didUpdateNameForZone:"
- "home:didUpdateOnboardAudioAnalysis:"
- "home:didUpdatePersonManagerSettings:"
- "home:didUpdateReprovisionStateForAccessory:"
- "home:didUpdateRoom:forAccessory:"
- "home:didUpdateSiriPhraseOptions:"
- "home:didUpdateStateForOutgoingInvitations:"
- "home:didUpdateSupportsResidentActionSetStateEvaluation:"
- "home:didUpdateTimeZone:"
- "home:didUpdateTrigger:"
- "homeAccessControlForUser:"
- "homeDidAddWalletKey:"
- "homeDidEnableLocationServices:"
- "homeDidEnableMultiUser:"
- "homeDidOnboardLocationServices:"
- "homeDidRemoveWalletKey:"
- "homeDidSetEnableDoorbellChime:"
- "homeDidSetHasAnyUserAcknowledgedCameraRecordingOnboarding:"
- "homeDidSetHasOnboardedForAccessCode:"
- "homeDidUpdateApplicationData:"
- "homeDidUpdateAssistantIdentifiers:"
- "homeDidUpdateAutoSelectedPreferredResident:"
- "homeDidUpdateHomeLocationStatus:"
- "homeDidUpdateName:"
- "homeDidUpdateNetworkRouterSupport:"
- "homeDidUpdateOnboardedEventLog:"
- "homeDidUpdatePrimaryResidentNetworkInfo:"
- "homeDidUpdateProtectionMode:"
- "homeDidUpdateSoundCheck:"
- "homeDidUpdateSupportedFeatures:"
- "homeDidUpdateSupportsResidentSelection:"
- "homeDidUpdateToROAR:"
- "homeDidUpdateUserSelectedPreferredResident:"
- "homeManager"
- "homeManager:didAddHome:"
- "homeManager:didReceiveAddAccessoryRequest:"
- "homeManager:didRemoveHome:"
- "homeManager:didUpdateAuthorizationStatus:"
- "homeManagerDidUpdateHomes:"
- "homeManagerDidUpdatePrimaryHome:"
- "homesLoadedCompletionHandlers"
- "homesWithRoomNames:"
- "homesWithZoneNames:"
- "identifiers"
- "ies"
- "initWithAccessorySettingsDataSource:"
- "initWithBundle:"
- "initWithCaching:"
- "initWithCaching:homeOptions:"
- "initWithOptions:cachePolicy:"
- "isAnnounceAccessAllowed"
- "isAnnounceAvailable"
- "isAnnounceSupported"
- "keyPath"
- "lastAccessorySettingsFetch"
- "lastAnnoucementIndex"
- "lastPlayedAnnouncementInfo:"
- "loadHomes:"
- "loadHomesStart"
- "numberWithUnsignedInt:"
- "playedAnnouncements"
- "root.announce"
- "root.announce.enabled"
- "rootGroup"
- "s"
- "setAppIntentConnectionListener:"
- "setCount:"
- "setDiscretionary:"
- "setHexCount:"
- "setHomesLoaded:"
- "setInactiveUpdatingLevel:"
- "setLastAnnoucementIndex:"
- "setLocationAuthorization:"
- "setPlaybackStartedForAnnouncement:endpointID:"
- "setPlaybackStoppedForAnnouncement:"
- "setPlaybackStoppedForAnnouncement:endpointID:"
- "settingsForAccessory:"
- "settingsQueue"
- "supportsAudioAnalysis"
- "supportsDropIn"
- "unplayedAnnouncements"
- "updatePlaybackForAnnouncementID:options:"
- "usersWithAnnounceEnabled"
- "v16@?0@\"<ANHomeManagerDelegate>\"8"
- "v24@0:8@\"HMHomeManager\"16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@?0@\"NSError\"8@\"NSArray\"16"
- "v28@0:8@\"HMAccessory\"16B24"
- "v28@0:8@\"HMHome\"16B24"
- "v32@0:8@\"<DICHomeManagerDelegate>\"16@\"NSObject<OS_dispatch_queue>\"24"
- "v32@0:8@\"HMAccessory\"16@\"ACAccount\"24"
- "v32@0:8@\"HMAccessory\"16@\"HMAccessory\"24"
- "v32@0:8@\"HMAccessory\"16@\"HMAccessoryProfile\"24"
- "v32@0:8@\"HMAccessory\"16@\"HMAccessorySettings\"24"
- "v32@0:8@\"HMAccessory\"16@\"HMCharacteristic\"24"
- "v32@0:8@\"HMAccessory\"16@\"HMDevice\"24"
- "v32@0:8@\"HMAccessory\"16@\"HMFPairingIdentity\"24"
- "v32@0:8@\"HMAccessory\"16@\"HMFSoftwareVersion\"24"
- "v32@0:8@\"HMAccessory\"16@\"HMFWiFiNetworkInfo\"24"
- "v32@0:8@\"HMAccessory\"16@\"HMService\"24"
- "v32@0:8@\"HMAccessory\"16@\"HMSymptomsHandler\"24"
- "v32@0:8@\"HMAccessory\"16@\"NSString\"24"
- "v32@0:8@\"HMHome\"16@\"CLLocation\"24"
- "v32@0:8@\"HMHome\"16@\"HMAccessoryNetworkProtectionGroup\"24"
- "v32@0:8@\"HMHome\"16@\"HMActionSet\"24"
- "v32@0:8@\"HMHome\"16@\"HMHomeActivityStateSchedule\"24"
- "v32@0:8@\"HMHome\"16@\"HMHomePersonManagerSettings\"24"
- "v32@0:8@\"HMHome\"16@\"HMMediaSystem\"24"
- "v32@0:8@\"HMHome\"16@\"HMResidentDevice\"24"
- "v32@0:8@\"HMHome\"16@\"HMRoom\"24"
- "v32@0:8@\"HMHome\"16@\"HMServiceGroup\"24"
- "v32@0:8@\"HMHome\"16@\"HMTrigger\"24"
- "v32@0:8@\"HMHome\"16@\"HMZone\"24"
- "v32@0:8@\"HMHome\"16@\"NSArray\"24"
- "v32@0:8@\"HMHome\"16@\"NSError\"24"
- "v32@0:8@\"HMHome\"16@\"NSString\"24"
- "v32@0:8@\"HMHome\"16@\"NSTimeZone\"24"
- "v32@0:8@\"HMHome\"16Q24"
- "v32@0:8@\"HMHome\"16q24"
- "v32@0:8@\"HMHomeManager\"16@\"HMAddAccessoryRequest\"24"
- "v32@0:8@\"HMHomeManager\"16@\"HMHome\"24"
- "v32@0:8@\"HMHomeManager\"16Q24"
- "v32@0:8@16q24"
- "v36@0:8@\"HMHome\"16@\"HMActionSet\"24B32"
- "v36@0:8@16@24B32"
- "v40@0:8@\"HMAccessory\"16@\"HMService\"24@\"HMCharacteristic\"32"
- "v40@0:8@\"HMAccessorySettingsDataSource\"16@\"NSUUID\"24@\"NSArray\"32"
- "v40@0:8@\"HMHome\"16@\"HMRoom\"24@\"HMAccessory\"32"
- "v40@0:8@\"HMHome\"16@\"HMRoom\"24@\"HMZone\"32"
- "v40@0:8@\"HMHome\"16@\"HMService\"24@\"HMServiceGroup\"32"
- "v40@0:8@\"HMHome\"16@\"NSError\"24@\"HMAccessory\"32"
- "v52@0:8@\"HMHome\"16Q24B32@\"NSDate\"36@\"NSDate\"44"
- "v52@0:8@16Q24B32@36@44"
- "value"
- "y"

```
