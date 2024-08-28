## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-850.10.3.0.0
-  __TEXT.__text: 0x62820
-  __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x643c
+850.10.7.0.0
+  __TEXT.__text: 0x63b74
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x658c
   __TEXT.__const: 0x1ac
-  __TEXT.__cstring: 0x760a
-  __TEXT.__oslogstring: 0x5d69
-  __TEXT.__gcc_except_tab: 0x1078
+  __TEXT.__cstring: 0x7669
+  __TEXT.__oslogstring: 0x5d29
+  __TEXT.__gcc_except_tab: 0x10d8
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1bf0
-  __TEXT.__objc_classname: 0x12c7
-  __TEXT.__objc_methname: 0xf3e4
-  __TEXT.__objc_methtype: 0x1bf1
-  __TEXT.__objc_stubs: 0x95e0
-  __DATA_CONST.__got: 0x8c8
-  __DATA_CONST.__const: 0x2450
-  __DATA_CONST.__objc_classlist: 0x550
+  __TEXT.__unwind_info: 0x1c40
+  __TEXT.__objc_classname: 0x12e9
+  __TEXT.__objc_methname: 0xf8ab
+  __TEXT.__objc_methtype: 0x1c5d
+  __TEXT.__objc_stubs: 0x9780
+  __DATA_CONST.__got: 0x8d0
+  __DATA_CONST.__const: 0x24a8
+  __DATA_CONST.__objc_classlist: 0x558
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3448
+  __DATA_CONST.__objc_selrefs: 0x3500
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x498
+  __DATA_CONST.__objc_superrefs: 0x4a0
   __DATA_CONST.__objc_arraydata: 0x600
-  __AUTH_CONST.__auth_got: 0x470
+  __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0xe60
-  __AUTH_CONST.__cfstring: 0x9b00
-  __AUTH_CONST.__objc_const: 0x123d0
+  __AUTH_CONST.__cfstring: 0x9ae0
+  __AUTH_CONST.__objc_const: 0x125f0
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x9e0
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x9fc
   __DATA.__data: 0x7a0
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x33e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2564
-  Symbols:   3543
-  CStrings:  4947
+  Functions: 2596
+  Symbols:   3576
+  CStrings:  4996
 
Symbols:
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_CLASS_$_WLKPostPlayAutoPlayToggleInterface
+ _OBJC_CLASS_$_WLKPostPlayAutoPlaySettings
+ _OBJC_METACLASS_$_WLKPostPlayAutoPlayToggleInterface
+ _OBJC_METACLASS_$_WLKPostPlayAutoPlaySettings
- _WLKAutoPlayRecommendedItemsCacheStatusLastModifiedDateKey
- _OBJC_METACLASS_$_WLKPostPlayAutoPlayCacheResult
- _objc_retain_x6
- _OBJC_CLASS_$_WLKPostPlayAutoPlayCacheResult
- _WLKAutoPlayNextEpisodeCacheStatusLastModifiedDateKey
CStrings:
+ "\x02\x12\x11\x12\x14"
+ "WLKPostPlayAutoPlayToggleInterface - isRecommendedItemsSettingEnabled returns %!@(MISSING)"
+ "WLKPostPlayAutoPlay - _migrateStatus: %!@(MISSING)"
+ "WLKPostPlayAutoPlay - There is ongoing operation."
+ "v16@?0@\"NSURLSessionDataTask\"8"
+ "WLKPostPlayAutoPlay - setSettings: %!@(MISSING)"
+ "\x02\x12"
+ "WLKPostPlayAutoPlaySettings"
+ "_recommendedItemsBouncer"
+ "_recommendedItemsAutoPlayEnabled"
+ "T@\"WLKUserSettingsRequestOperation\",&,N,V_ongoingUpdateOperation"
+ "recommendedItemsBouncer"
+ "WLKPostPlayAutoPlay - cached post play auto-play type: %!@(MISSING), state: %!d(MISSING)"
+ "WLKPostPlayAutoPlay - fetchStatus replied with cached state because there is ongoing migration: %!d(MISSING)"
+ "WLKPostPlayAutoPlay - Nothing to update since settings has no values set"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "_migrateStatus:completion:"
+ "isEqualToSettings:"
+ "recommendedItemsAutoPlayEnabled"
+ "setIsRecommendedItemsSettingEnabled:"
+ "setSettings:completion:"
+ "_cacheResultForType:"
+ "WLKPostPlayAutoPlay - fetchStatusForAllTypes"
+ "recommendedItemsSettingValue"
+ "task"
+ "T@\"NSNumber\",&,N,V_nextEpisodeSettingValue"
+ "v24@?0@\"WLKPostPlayAutoPlaySettings\"8@\"NSError\"16"
+ "WLKPostPlayAutoPlay - New settings: %!@(MISSING)"
+ "currentSettingForType:"
+ "v16@?0@\"NSTimer\"8"
+ "_isRecommendedItemsSettingEnabled"
+ "nextEpisodeSettingDidChange"
+ "_newSettingsMergedWithPreviousSettings:"
+ "T@\"<WLKPostPlayAutoPlayToggleInterfaceDelegate>\",W,N,V_delegate"
+ "T@\"NSNumber\",&,N,V_isRecommendedItemsSettingEnabled"
+ "nextEpisodeBouncer"
+ "v40@0:8Q16@24@?32"
+ "T@\"NSNumber\",&,N,V_recommendedItemsSettingValue"
+ "@\"<WLKPostPlayAutoPlayToggleInterfaceDelegate>\""
+ "currentSettings"
+ "newSettings != nil"
+ "createDataTaskWithRequest:activity:dataTaskCreationCompletionHandler:requestCompletionHandler:"
+ "@\"WLKUserSettingsRequestOperation\""
+ "_performUserSettingsAction:settings:completion:"
+ "initWithPostPlayAutoPlaySettings:"
+ "recommendedItemsSettingDidChange"
+ "postPlayAutoPlaySettings"
+ "_hasValues"
+ "isNextEpisodeSettingEnabled"
+ "T@\"NSURLSessionDataTask\",&,N,V_task"
+ "_postPlayAutoPlaySettings"
+ "WLKPostPlayAutoPlayToggleInterface"
+ "setTask:"
+ "_setEnabled:type:"
+ "_fetchStatusForType:withCompletion:"
+ "_autoPlayRecommendedItemsSettingDidChange:"
+ "v28@0:8B16Q20"
+ "WLKPostPlayAutoPlay - update cache for post play auto-play settings: %!@(MISSING)"
+ "TB,R,N,V_recommendedItemsAutoPlayEnabled"
+ "updateWithSettings:"
+ "T@\"NSTimer\",&,N,V_nextEpisodeBouncer"
+ "setRecommendedItemsSettingValue:"
+ "_nextEpisodeSettingValue"
+ "T@\"NSTimer\",&,N,V_recommendedItemsBouncer"
+ "T@\"NSNumber\",&,N,V_isNextEpisodeSettingEnabled"
+ "WLKPostPlayAutoPlayCache.m"
+ "WLKPostPlayAutoPlay - getStatusForType replied with cached state: %!d(MISSING)"
+ "_task"
+ "@\"NSURLSessionDataTask\""
+ "fetchStatusForAllTypesWithCompletion:"
+ "isRecommendedItemsSettingEnabled"
+ "T@\"WLKPostPlayAutoPlaySettings\",&,N,V_postPlayAutoPlaySettings"
+ "_isNextEpisodeSettingEnabled"
+ "_nextEpisodeBouncer"
+ "setRecommendedItemsBouncer:"
+ "@\"WLKPostPlayAutoPlaySettings\""
+ "@\"NSTimer\""
+ "_autoPlayNextEpisodeSettingDidChange:"
+ "_ongoingUpdateOperation"
+ "WLKPostPlayAutoPlay - fetchStatus replied with fresh state: %!d(MISSING), error: %!@(MISSING)"
+ "setPostPlayAutoPlaySettings:"
+ "ongoingUpdateOperation"
+ "setOngoingUpdateOperation:"
+ "+[WLKPostPlayAutoPlayCache _postLocalNotificationForType:status:error:]"
+ "initWithDelegate:"
+ "setIsNextEpisodeSettingEnabled:"
+ "setNextEpisodeBouncer:"
+ "-[WLKPostPlayAutoPlayCache _setEnabled:type:]"
+ "_recommendedItemsSettingValue"
+ "WLKPostPlayAutoPlay - The ongoing operation has the same settings, skipping the latest one."
+ "setNextEpisodeSettingValue:"
+ "WLKPostPlayAutoPlayToggleInterface - isNextEpisodeSettingEnabled returns %!@(MISSING)"
+ "-[WLKPostPlayAutoPlayManager _performUserSettingsAction:settings:completion:]_block_invoke"
+ "nextEpisodeSettingValue"
+ "WLKPostPlayAutoPlay - The ongoing operation has different settings, cancel the ongoing operation."
+ "<WLKPostPlayAutoPlaySettings: %!p(MISSING)>, nextEpisode = %!@(MISSING), recommendedItems = %!@(MISSING)"
- "v36@0:8B16Q20@?28"
- "cacheResult != nil"
- "WLKPostPlayAutoPlay - fetchStatus replied with fresh state: %!d(MISSING), lastModified: %!@(MISSING), error: %!@(MISSING)"
- "WLKPostPlayAutoPlay - returning cached value for post play auto-play state: %!d(MISSING)"
- "TB,R,N,V_postPlayAutoPlayRecommendedItemsEnabled"
- "v32@0:8B16Q20B28"
- "WLKPostPlayAutoPlay - fetchStatus replied with cached state because there is ongoing migration: %!d(MISSING), lastModified: %!@(MISSING)"
- "-[WLKPostPlayAutoPlayManager _performUserSettingsAction:setPostPlayAutoPlayEnabled:types:overrideLastModifiedDate:completion:]_block_invoke"
- "setLastModifiedDate:"
- "WLKPostPlayAutoPlay - Settings: Fetch post play auto-play status completed. isEnabled:%!i(MISSING), error=%!@(MISSING)"
- "WLKPostPlayAutoPlay - setting cache for post play auto-play state: %!d(MISSING)"
- "WLKPostPlayAutoPlay - cached post play auto-play state: %!d(MISSING), lastModified: %!@(MISSING)"
- "setEnabled:type:overrideLastModifiedDate:"
- "WLKPostPlayAutoPlay - Settings: Error fetch post play auto-play status: %!@(MISSING)"
- "_lastModifiedDateCacheKeyForType:"
- "\x01!"
- "v48@0:8Q16B24Q28B36@?40"
- "_lastModifiedDate"
- "WLKPostPlayAutoPlay - getStatusForType replied with cached state: %!d(MISSING), lastModified: %!@(MISSING)"
- "isEnabled"
- "setStatus:types:completion:"
- "@28@0:8B16Q20"
- "WLKPostPlayAutoPlay - Settings: Fetch post play auto-play status timed out."
- "auto-play-recommended-items-status-last-modified-date"
- "cacheResultsForTypes:"
- "setPostPlayAutoPlayNextEpisodeEnabled:"
- "auto-play-next-video-status-last-modified-date"
- "TQ,N,V_type"
- "cacheResultForType:"
- "WLKPostPlayAutoPlay - returning new value for post play auto-play type: %!@(MISSING), state: %!d(MISSING)"
- "invalidateAndCancel"
- "setType:"
- "TB,N,GisEnabled,V_enabled"
- "fetchStatusForType:withCompletion:"
- "+[WLKPostPlayAutoPlayManager _postLocalNotificationForType:status:error:]"
- "WLKPostPlayAutoPlay - Set cache based on migration preference value: %!@(MISSING), types: %!@(MISSING)"
- "WLKPostPlayAutoPlay - Error while migrating the user preference for post-play auto play: %!@(MISSING)"
- "lastModifiedDate"
- "postPlayAutoPlayNextEpisodeEnabled"
- "initWithPostPlayAutoPlayEnabled:types:"
- "WLKPostPlayAutoPlayCacheResult"
- "setEnabled:types:overrideLastModifiedDate:"
- "postPlayAutoPlayRecommendedItemsEnabled"
- "_performUserSettingsAction:setPostPlayAutoPlayEnabled:types:overrideLastModifiedDate:completion:"
- "_postPlayAutoPlayRecommendedItemsEnabled"
- "\x02\x12\x11\x12\x13"
- "T@\"NSDate\",&,N,V_lastModifiedDate"
- "WLKPostPlayAutoPlay - setStatus: %!@(MISSING), types: %!@(MISSING)"

```
