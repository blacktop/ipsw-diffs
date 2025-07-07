## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-613.0.1.0.0
-  __TEXT.__text: 0x18b220
+615.0.2.0.0
+  __TEXT.__text: 0x18c0d0
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x189ec
+  __TEXT.__objc_methlist: 0x18a64
   __TEXT.__const: 0x6f8
-  __TEXT.__cstring: 0x1b6a7
-  __TEXT.__oslogstring: 0x1728e
+  __TEXT.__cstring: 0x1b74f
+  __TEXT.__oslogstring: 0x1746f
   __TEXT.__gcc_except_tab: 0x22e0
   __TEXT.__dlopen_cstrs: 0x3d0
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x65e0
+  __TEXT.__unwind_info: 0x66a0
   __TEXT.__objc_classname: 0x3be3
-  __TEXT.__objc_methname: 0x33f8a
-  __TEXT.__objc_methtype: 0x6773
-  __TEXT.__objc_stubs: 0x1c9e0
+  __TEXT.__objc_methname: 0x340ac
+  __TEXT.__objc_methtype: 0x676d
+  __TEXT.__objc_stubs: 0x1cae0
   __DATA_CONST.__got: 0x16f0
-  __DATA_CONST.__const: 0x6308
+  __DATA_CONST.__const: 0x6358
   __DATA_CONST.__objc_classlist: 0xe48
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e58
+  __DATA_CONST.__objc_selrefs: 0x9e90
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0xc50
   __DATA_CONST.__objc_arraydata: 0xaf8
   __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__const: 0x2a60
-  __AUTH_CONST.__cfstring: 0x150a0
+  __AUTH_CONST.__cfstring: 0x15160
   __AUTH_CONST.__objc_const: 0x45ce0
   __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_arrayobj: 0x6d8

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 86CAF497-126E-3DF7-965C-3600D9BE3064
-  Functions: 10636
-  Symbols:   35015
-  CStrings:  15956
+  UUID: D67788CE-64FD-39FC-919E-A146623EF02C
+  Functions: 10646
+  Symbols:   35045
+  CStrings:  15981
 
Symbols:
+ +[ATXAppDirectoryResponse _canUseSuggestedApp:includeRemoteApps:]
+ +[ATXDefaultHomeScreenItemProducerUtilities bundleIdentifierFromWidgetKey:]
+ +[ATXDefaultHomeScreenItemProducerUtilities eligibleThirdPartyWidgetFromSimilarWidgets:launchCounts:]
+ +[ATXDefaultHomeScreenItemProducerUtilities personalitiesFromAssetsWithKey:launchCounts:]
+ +[ATXDefaultHomeScreenItemProducerUtilities shouldConsiderSimilarThirdPartyWidgetsForPosition:]
+ +[ATXDefaultHomeScreenItemProducerUtilities similarThirdPartyWidgetsForPosition:]
+ +[ATXDefaultHomeScreenItemProducerUtilities widgetExtensionAndKindFromKey:]
+ +[ATXIntentStream generateParameterCombitionsForKeys:]
+ -[ATXAppDirectoryClient getDirectoryResponseFromCacheWithMaxNumberOfAppsToPredict:].cold.2
+ -[ATXAppDirectoryResponse _minuteZeroResponse]
+ -[ATXDefaultHomeScreenItemUpdater _updateAllDefaultsOnQueueWithReason:updateCarPlayDefaults:]
+ -[ATXDefaultHomeScreenItemUpdater updateDefaultsWithSystemDescriptors:updateCarPlayDefaults:installDatesCache:reason:]
+ GCC_except_table53
+ GCC_except_table59
+ GCC_except_table62
+ GCC_except_table66
+ __OBJC_$_CLASS_METHODS_ATXAppDirectoryResponse
+ __OBJC_$_CLASS_METHODS_ATXIntentStream
+ ___118-[ATXDefaultHomeScreenItemUpdater updateDefaultsWithSystemDescriptors:updateCarPlayDefaults:installDatesCache:reason:]_block_invoke
+ ___133-[ATXAppDirectoryResponse initWithSuggestionLayout:includeRemoteApps:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:]_block_invoke
+ ___18-[ATXAction proto]_block_invoke.124
+ ___36-[ATXClient notifySpotlightInvoked:]_block_invoke.cold.1
+ ___46-[ATXAppDirectoryResponse _minuteZeroResponse]_block_invoke
+ ___81+[ATXDefaultHomeScreenItemProducerUtilities similarThirdPartyWidgetsForPosition:]_block_invoke
+ ___block_descriptor_32_e22_16?0"NSDictionary"8l
+ ___block_descriptor_40_e8_B16?08l
+ ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.127
+ ___block_literal_global.573
+ ___block_literal_global.61
+ _kATXAppDirectoryRecentsCacheBundleIdKey
+ _kATXAppDirectoryRecentsCacheInstallDateKey
+ _objc_msgSend$_canUseSuggestedApp:includeRemoteApps:
+ _objc_msgSend$_updateAllDefaultsOnQueueWithReason:updateCarPlayDefaults:
+ _objc_msgSend$bundleIdentifierFromWidgetKey:
+ _objc_msgSend$eligibleThirdPartyWidgetFromSimilarWidgets:launchCounts:
+ _objc_msgSend$isGreaterThanOrEqualToData:
+ _objc_msgSend$personalitiesFromAssetsWithKey:launchCounts:
+ _objc_msgSend$shouldConsiderSimilarThirdPartyWidgetsForPosition:
+ _objc_msgSend$similarThirdPartyWidgetsForPosition:
+ _objc_msgSend$updateDefaultsWithSystemDescriptors:updateCarPlayDefaults:installDatesCache:reason:
+ _objc_msgSend$widgetExtensionAndKindFromKey:
- -[ATXAppDirectoryResponse initWithResponse:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:]
- -[ATXAppDirectoryResponse initWithResponse:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:].cold.1
- -[ATXDefaultHomeScreenItemUpdater _updateAllDefaultsOnQueueWithReason:]
- -[ATXDefaultHomeScreenItemUpdater updateDefaultsWithSystemDescriptors:installDatesCache:reason:]
- GCC_except_table54
- GCC_except_table57
- GCC_except_table60
- GCC_except_table63
- GCC_except_table67
- ___107-[ATXAppDirectoryResponse initWithResponse:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:]_block_invoke
- ___18-[ATXAction proto]_block_invoke.121
- ___36-[ATXClient notifySpotlightInvoked:]_block_invoke_2
- ___36-[ATXClient notifySpotlightInvoked:]_block_invoke_2.cold.1
- ___96-[ATXDefaultHomeScreenItemUpdater updateDefaultsWithSystemDescriptors:installDatesCache:reason:]_block_invoke
- ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
- ___block_literal_global.570
- ___block_literal_global.60
- ___block_literal_global.67
- ___block_literal_global.69
- _objc_msgSend$_updateAllDefaultsOnQueueWithReason:
- _objc_msgSend$updateDefaultsWithSystemDescriptors:installDatesCache:reason:
CStrings:
+ "%@-%lu"
+ "%s: filtering out widget descriptor: %@. Reason: Widget's bundle identifier and extension identifier in deny list %@"
+ "%s: filtering out widget descriptor: %@. Reason: Widget's extension identifier and kind identifier in deny list %@"
+ "@16@?0@\"NSDictionary\"8"
+ "ATXAppDirectoryClient: Recent apps cache element does not have expected number of keys: %@"
+ "ATXAppDirectoryClient: Recent apps cache element doesn't have expected bundleId key: '%@'"
+ "ATXAppDirectoryClient: Recent apps cache element doesn't have expected install date key: '%@'"
+ "ATXAppDirectoryClient: Recent apps have unexpected format; resetting"
+ "SpotlightPlusDocumentsDemoModeEnabled"
+ "_canUseSuggestedApp:includeRemoteApps:"
+ "_updateAllDefaultsOnQueueWithReason:updateCarPlayDefaults:"
+ "bundleIdentifierFromWidgetKey:"
+ "carPlayAnyCalendarWidget"
+ "carPlayAnyMedia_MusicBooksPodcast_Widget"
+ "carPlayAnyToDoWidget"
+ "eligibleThirdPartyWidgetFromSimilarWidgets:launchCounts:"
+ "generateParameterCombitionsForKeys:"
+ "nilActionKey"
+ "personalitiesFromAssetsWithKey:launchCounts:"
+ "shouldConsiderSimilarThirdPartyWidgetsForPosition:"
+ "similarThirdPartyWidgetsForPosition:"
+ "updateDefaultsWithSystemDescriptors:updateCarPlayDefaults:installDatesCache:reason:"
+ "v44@0:8@16B24@28@36"
+ "widgetExtensionAndKindFromKey:"
- "%s: filtering out widget descriptor: %@. Reason: Widget's extension identifier in deny list %@"
- "@64@0:8@16@24@32@40Q48@56"
- "_updateAllDefaultsOnQueueWithReason:"
- "initWithResponse:recentApps:hiddenApps:otherAppsOnScreen:numAppsToPredict:error:"
- "updateDefaultsWithSystemDescriptors:installDatesCache:reason:"

```
