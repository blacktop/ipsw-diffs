## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-850.0.7.0.0
-  __TEXT.__text: 0x5f8e4
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x61dc
+850.10.3.0.0
+  __TEXT.__text: 0x62820
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x643c
   __TEXT.__const: 0x1ac
-  __TEXT.__cstring: 0x7244
-  __TEXT.__oslogstring: 0x53e0
-  __TEXT.__gcc_except_tab: 0xf5c
+  __TEXT.__cstring: 0x760a
+  __TEXT.__oslogstring: 0x5d69
+  __TEXT.__gcc_except_tab: 0x1078
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1b20
-  __TEXT.__objc_classname: 0x1271
-  __TEXT.__objc_methname: 0xed9c
-  __TEXT.__objc_methtype: 0x1b7b
-  __TEXT.__objc_stubs: 0x9280
-  __DATA_CONST.__got: 0x8b0
-  __DATA_CONST.__const: 0x22e0
-  __DATA_CONST.__objc_classlist: 0x538
+  __TEXT.__unwind_info: 0x1bf0
+  __TEXT.__objc_classname: 0x12c7
+  __TEXT.__objc_methname: 0xf3e4
+  __TEXT.__objc_methtype: 0x1bf1
+  __TEXT.__objc_stubs: 0x95e0
+  __DATA_CONST.__got: 0x8c8
+  __DATA_CONST.__const: 0x2450
+  __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3338
+  __DATA_CONST.__objc_selrefs: 0x3448
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x488
+  __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0x600
-  __AUTH_CONST.__auth_got: 0x468
-  __AUTH_CONST.__const: 0xe40
-  __AUTH_CONST.__cfstring: 0x99c0
-  __AUTH_CONST.__objc_const: 0x11fb8
+  __AUTH_CONST.__auth_got: 0x470
+  __AUTH_CONST.__const: 0xe60
+  __AUTH_CONST.__cfstring: 0x9b00
+  __AUTH_CONST.__objc_const: 0x123d0
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x9ac
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x9e0
   __DATA.__data: 0x7a0
-  __DATA.__bss: 0x120
-  __DATA.__common: 0x4
-  __DATA_DIRTY.__objc_data: 0x32a0
+  __DATA.__bss: 0x110
+  __DATA_DIRTY.__objc_data: 0x33e0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x428
-  __DATA_DIRTY.__common: 0x1
+  __DATA_DIRTY.__bss: 0x448
+  __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2496
-  Symbols:   3452
-  CStrings:  4839
+  Functions: 2564
+  Symbols:   3543
+  CStrings:  4947
 
Symbols:
+ _OBJC_CLASS_$_WLKPostPlayAutoPlayCache
+ _OBJC_CLASS_$_WLKPostPlayAutoPlayCacheResult
+ _OBJC_CLASS_$_WLKPostPlayAutoPlayManager
+ _OBJC_METACLASS_$_WLKPostPlayAutoPlayCache
+ _OBJC_METACLASS_$_WLKPostPlayAutoPlayCacheResult
+ _OBJC_METACLASS_$_WLKPostPlayAutoPlayManager
+ _WLKAutoPlayNextEpisodeCacheStatusKey
+ _WLKAutoPlayNextEpisodeCacheStatusLastModifiedDateKey
+ _WLKAutoPlayRecommendedItemsCacheStatusKey
+ _WLKAutoPlayRecommendedItemsCacheStatusLastModifiedDateKey
+ _WLKPostPlayAutoPlayCheckHasActiveAccount
+ _WLKPostPlayAutoPlayErrorDomain
+ _WLKPostPlayAutoPlayNextEpisodeSettingChangedNotification
+ _WLKPostPlayAutoPlayRecommendedItemsSettingChangedNotification
+ _WLKPostPlayAutoPlaySettingChangedNotificationErrorKey
+ _WLKPostPlayAutoPlaySettingChangedNotificationStatusKey
+ __WLKPostPlayAutoPlayNextEpisodeStatusChangedCrossProcessNotification
+ __WLKPostPlayAutoPlayRecommendedItemsStatusChangedCrossProcessNotification
+ _objc_retain_x6
CStrings:
+ "\x01!"
+ "+[WLKPostPlayAutoPlayManager _postLocalNotificationForType:status:error:]"
+ "-[WLKPostPlayAutoPlayManager _performUserSettingsAction:setPostPlayAutoPlayEnabled:types:overrideLastModifiedDate:completion:]_block_invoke"
+ "-[WLKPostPlayAutoPlayManager isEnabledForType:]"
+ "@\"WLKPostPlayAutoPlayCache\""
+ "@28@0:8B16Q20"
+ "T@\"NSDate\",&,N,V_lastModifiedDate"
+ "T@\"WLKPostPlayAutoPlayCache\",&,N,V_cache"
+ "TB,N,GisEnabled,V_enabled"
+ "TB,N,V_initWithPostPlayAutoPlaySetting"
+ "TB,N,V_isMigrationInProgress"
+ "TB,R,N,V_nextEpisodeAutoPlayEnabled"
+ "TB,R,N,V_postPlayAutoPlayRecommendedItemsEnabled"
+ "TQ,N,V_postPlayAutoPlayType"
+ "TQ,N,V_type"
+ "WLKPostPlayAutoPlay - Error while migrating the user preference for post-play auto play: %!@(MISSING)"
+ "WLKPostPlayAutoPlay - Firing local post play auto-play status changed notification for type: %!@(MISSING)"
+ "WLKPostPlayAutoPlay - Invalidate cache due to _handleAccountDidChange"
+ "WLKPostPlayAutoPlay - Migrating post play auto-play from WLKSettingsStore"
+ "WLKPostPlayAutoPlay - Migrating post play auto-play from WLKSystemPreferencesStore"
+ "WLKPostPlayAutoPlay - Migration is in progress, ignoring this call _migrateFromSystemPreferencesStoreOrSettingsStore."
+ "WLKPostPlayAutoPlay - No cache result for type: %!@(MISSING), default to YES"
+ "WLKPostPlayAutoPlay - Post play auto-play (user settings) action failed -- %!@(MISSING). Request -- %!l(MISSING)u"
+ "WLKPostPlayAutoPlay - Post play auto-play (user settings) action succeeded -- %!@(MISSING). Request -- %!l(MISSING)u"
+ "WLKPostPlayAutoPlay - Post play auto-play (user settings) action will not be executed -- empty userSettings parameter."
+ "WLKPostPlayAutoPlay - Received post play auto-play next episode status changed notification, fetching cache"
+ "WLKPostPlayAutoPlay - Received post play auto-play recommended items status changed notification, fetching cache"
+ "WLKPostPlayAutoPlay - Set cache based on migration preference value: %!@(MISSING), types: %!@(MISSING)"
+ "WLKPostPlayAutoPlay - Settings: Error fetch post play auto-play status: %!@(MISSING)"
+ "WLKPostPlayAutoPlay - Settings: Fetch post play auto-play status completed. isEnabled:%!i(MISSING), error=%!@(MISSING)"
+ "WLKPostPlayAutoPlay - Settings: Fetch post play auto-play status timed out."
+ "WLKPostPlayAutoPlay - User is not signed in, returning early with error %!@(MISSING)"
+ "WLKPostPlayAutoPlay - cached post play auto-play state: %!d(MISSING), lastModified: %!@(MISSING)"
+ "WLKPostPlayAutoPlay - fetchStatus replied with cached state because there is ongoing migration: %!d(MISSING), lastModified: %!@(MISSING)"
+ "WLKPostPlayAutoPlay - fetchStatus replied with fresh state: %!d(MISSING), lastModified: %!@(MISSING), error: %!@(MISSING)"
+ "WLKPostPlayAutoPlay - fetchStatusForType: %!@(MISSING)"
+ "WLKPostPlayAutoPlay - getStatusForType replied with cached state: %!d(MISSING), lastModified: %!@(MISSING)"
+ "WLKPostPlayAutoPlay - getStatusForType: %!@(MISSING), no cache found."
+ "WLKPostPlayAutoPlay - posting (cross process) notification %!s(MISSING)"
+ "WLKPostPlayAutoPlay - returning cached value for post play auto-play state: %!d(MISSING)"
+ "WLKPostPlayAutoPlay - returning new value for post play auto-play type: %!@(MISSING), state: %!d(MISSING)"
+ "WLKPostPlayAutoPlay - setStatus: %!@(MISSING), types: %!@(MISSING)"
+ "WLKPostPlayAutoPlay - setting cache for post play auto-play state: %!d(MISSING)"
+ "WLKPostPlayAutoPlay - setting cache for post play auto-play state: %!d(MISSING), type: %!@(MISSING)"
+ "WLKPostPlayAutoPlayCache"
+ "WLKPostPlayAutoPlayCacheResult"
+ "WLKPostPlayAutoPlayErrorDomain"
+ "WLKPostPlayAutoPlayManager"
+ "WLKPostPlayAutoPlayManager.m"
+ "WLKPostPlayAutoPlayManagerPersistentCacheQueue"
+ "WLKPostPlayAutoPlayNextEpisodeSettingChangedNotification"
+ "WLKPostPlayAutoPlaySettingChangedNotificationErrorKey"
+ "WLKPostPlayAutoPlaySettingChangedNotificationStatusKey"
+ "_cacheKeyForType:"
+ "_handleAccountDidChange:"
+ "_initWithPostPlayAutoPlaySetting"
+ "_isMigrationInProgress"
+ "_lastModifiedDate"
+ "_lastModifiedDateCacheKeyForType:"
+ "_migrateFromSystemPreferencesStoreOrSettingsStore"
+ "_nextEpisodeAutoPlayEnabled"
+ "_performUserSettingsAction:setPostPlayAutoPlayEnabled:types:overrideLastModifiedDate:completion:"
+ "_postLocalNotificationForType:status:error:"
+ "_postPlayAutoPlayNextEpisodeSettingChangedNotificationToken"
+ "_postPlayAutoPlayRecommendedItemsEnabled"
+ "_postPlayAutoPlayRecommendedItemsSettingChangedNotificationToken"
+ "_postPlayAutoPlayType"
+ "auto-play-next-episode-status"
+ "auto-play-next-video-status-last-modified-date"
+ "auto-play-recommended-items-status"
+ "auto-play-recommended-items-status-last-modified-date"
+ "cache"
+ "cacheResult != nil"
+ "cacheResultForType:"
+ "cacheResultsForTypes:"
+ "com.apple.WatchListKit.WLKPostPlayAutoPlayNextEpisodeStatusChangedNotification"
+ "com.apple.WatchListKit.WLKPostPlayAutoPlayRecommendedItemsStatusChangedNotification"
+ "fetchStatusForType:withCompletion:"
+ "getStatusForType:withCompletion:"
+ "hasCacheForType:"
+ "hasPostPlayAutoPlayNextVideoPreferences"
+ "initWithPostPlayAutoPlayEnabled:types:"
+ "initWithPostPlayAutoPlaySetting"
+ "isEnabled"
+ "isEnabledForType:"
+ "isMigrationInProgress"
+ "lastModifiedDate"
+ "nextEpisodeAutoPlayEnabled"
+ "nextEpisodeAutoPlayEnabled"
+ "notificationName != nil"
+ "postPlayAutoPlayEnabled"
+ "postPlayAutoPlayNextEpisodeEnabled"
+ "postPlayAutoPlayRecommendedItemsEnabled"
+ "postPlayAutoPlayType"
+ "removePostPlayAutoPlayNextVideoPreferences"
+ "setCache:"
+ "setEnabled:type:overrideLastModifiedDate:"
+ "setEnabled:types:overrideLastModifiedDate:"
+ "setInitWithPostPlayAutoPlaySetting:"
+ "setIsMigrationInProgress:"
+ "setLastModifiedDate:"
+ "setPostPlayAutoPlayNextEpisodeEnabled:"
+ "setPostPlayAutoPlayType:"
+ "setStatus:types:completion:"
+ "setType:"
+ "type != WLKPostPlayAutoPlayTypeNone"
+ "v32@0:8B16Q20B28"
+ "v36@0:8B16Q20@?28"
+ "v36@0:8Q16B24@28"
+ "v48@0:8Q16B24Q28B36@?40"
- "KettleTCC"
- "UserNotifications"

```
