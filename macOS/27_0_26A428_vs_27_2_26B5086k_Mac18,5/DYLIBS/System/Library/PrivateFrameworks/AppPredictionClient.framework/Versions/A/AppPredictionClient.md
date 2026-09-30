## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/Versions/A/AppPredictionClient`

```diff

-671.0.1.0.1
-  __TEXT.__text: 0x197c30
-  __TEXT.__objc_methlist: 0x18a2c
-  __TEXT.__const: 0x700
-  __TEXT.__cstring: 0x1bdfc
-  __TEXT.__oslogstring: 0x1719a
-  __TEXT.__gcc_except_tab: 0x1c34
+674.0.1.0.0
+  __TEXT.__text: 0x198c3c
+  __TEXT.__objc_methlist: 0x18a64
+  __TEXT.__const: 0x708
+  __TEXT.__cstring: 0x1bf0d
+  __TEXT.__oslogstring: 0x17410
+  __TEXT.__gcc_except_tab: 0x1c38
   __TEXT.__dlopen_cstrs: 0x2cc
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x83d8
+  __TEXT.__unwind_info: 0x83e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9f60
+  __DATA_CONST.__objc_selrefs: 0x9f88
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0xbf0
   __DATA_CONST.__objc_arraydata: 0xb10
   __DATA_CONST.__got: 0x16c8
   __AUTH_CONST.__const: 0x6440
-  __AUTH_CONST.__cfstring: 0x15460
-  __AUTH_CONST.__objc_const: 0x44770
+  __AUTH_CONST.__cfstring: 0x154a0
+  __AUTH_CONST.__objc_const: 0x447d0
   __AUTH_CONST.__objc_intobj: 0xa98
   __AUTH_CONST.__objc_arrayobj: 0x6d8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__auth_got: 0x690
   __AUTH.__objc_data: 0x33e0
-  __DATA.__objc_ivar: 0x1c30
+  __DATA.__objc_ivar: 0x1c3c
   __DATA.__data: 0x1aa0
   __DATA_DIRTY.__objc_data: 0x55f0
   __DATA_DIRTY.__data: 0x88

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10873
-  Symbols:   20584
-  CStrings:  4773
+  Functions: 10880
+  Symbols:   20595
+  CStrings:  4794
 
Symbols:
+ +[ATXDefaultHomeScreenItemProducerUtilities similarThirdPartyWidgetsForPosition:assets:]
+ -[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:]
+ -[ATXAppLaunches rawLaunchCountAndDistinctDaysLaunchedForAllAppsOverLastDays:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _dayZeroStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _firstWidgetThatIsntUsedYet:usedPersonalities:size:]
+ -[ATXDefaultHomeScreenItemProducer _computeNewlyInstalledThresholdsIfNeeded]
+ -[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]
+ -[ATXInformationStore fetchAllDistinctWidgetsIgnoringIntentWithTimelineDonations]
+ GCC_except_table258
+ GCC_except_table262
+ GCC_except_table266
+ GCC_except_table270
+ GCC_except_table274
+ GCC_except_table277
+ GCC_except_table281
+ GCC_except_table284
+ GCC_except_table288
+ GCC_except_table297
+ GCC_except_table302
+ GCC_except_table306
+ GCC_except_table310
+ GCC_except_table313
+ GCC_except_table316
+ GCC_except_table320
+ GCC_except_table324
+ GCC_except_table327
+ OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._newInstallThreshold
+ OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._widgetInstallDateThreshold
+ OBJC_IVAR_$_ATXHomeScreenConfigCache._usesDefaultRootPath
+ __78-[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]_block_invoke_3
+ __80-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:]_block_invoke
+ ___78-[ATXAppLaunches rawLaunchCountAndDistinctDaysLaunchedForAllAppsOverLastDays:]_block_invoke
+ ___78-[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]_block_invoke
+ ___78-[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]_block_invoke_2
+ ___78-[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]_block_invoke_3
+ ___80-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:]_block_invoke
+ ___80-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:]_block_invoke_2
+ ___88+[ATXDefaultHomeScreenItemProducerUtilities similarThirdPartyWidgetsForPosition:assets:]_block_invoke
+ _kATXAppLaunchesSmartStackLookbackDays
+ _objc_msgSend$_computeNewlyInstalledThresholdsIfNeeded
+ _objc_msgSend$_dayZeroStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:
+ _objc_msgSend$_fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:
+ _objc_msgSend$_firstWidgetThatIsntUsedYet:usedPersonalities:size:
+ _objc_msgSend$_rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:
+ _objc_msgSend$rawLaunchCountAndDistinctDaysLaunchedForAllAppsOverLastDays:
+ _objc_msgSend$similarThirdPartyWidgetsForPosition:assets:
- +[ATXDefaultHomeScreenItemProducerUtilities similarThirdPartyWidgetsForPosition:]
- -[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:]
- -[ATXDefaultHomeScreenItemOnboardingStacksProducer _firstWidgetThatIsntUsedYet:usedPersonalities:]
- GCC_except_table256
- GCC_except_table260
- GCC_except_table264
- GCC_except_table268
- GCC_except_table272
- GCC_except_table275
- GCC_except_table279
- GCC_except_table282
- GCC_except_table286
- GCC_except_table295
- GCC_except_table300
- GCC_except_table304
- GCC_except_table308
- GCC_except_table311
- GCC_except_table314
- GCC_except_table318
- GCC_except_table322
- GCC_except_table325
- __67-[ATXInformationStore fetchDistinctWidgetsIgnoringIntentSinceDate:]_block_invoke_3
- __81-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:]_block_invoke
- ___67-[ATXInformationStore fetchDistinctWidgetsIgnoringIntentSinceDate:]_block_invoke
- ___67-[ATXInformationStore fetchDistinctWidgetsIgnoringIntentSinceDate:]_block_invoke_2
- ___67-[ATXInformationStore fetchDistinctWidgetsIgnoringIntentSinceDate:]_block_invoke_3
- ___71-[ATXWidgetDescriptorCache _queue_fetchAllDescriptorMetadataWithError:]_block_invoke
- ___79-[ATXAppLaunches rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysForAllApps]_block_invoke
- ___81+[ATXDefaultHomeScreenItemProducerUtilities similarThirdPartyWidgetsForPosition:]_block_invoke
- ___81-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:]_block_invoke
- ___81-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:]_block_invoke_2
- ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke_2
- _objc_msgSend$_firstWidgetThatIsntUsedYet:usedPersonalities:
- _objc_msgSend$_rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:
- _objc_msgSend$similarThirdPartyWidgetsForPosition:
CStrings:
+ "%s: Skipping descriptor disfavored for tvOS: %@"
+ "%s: Skipping descriptor that does not support systemSmall: %@"
+ "%s: built day zero default stack with %lu widgets"
+ "%s: not adding default widget %{public}@ because it is already used"
+ "%s: not adding default widget %{public}@ because it is in the client's deny list"
+ "%s: not adding widget %{public}@ because it does not support stack layout size %lu"
+ ","
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _dayZeroStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]"
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _firstWidgetThatIsntUsedYet:usedPersonalities:size:]"
+ "SELECT DISTINCT extensionBundleId, containerBundleIdentifier, widgetKind, widgetFamily FROM timelineDonations;"
+ "SELECT timestamp, score, duration, suggestionId, suggestionMappingReason FROM timelineDonations WHERE extensionBundleId = :extensionBundleId AND widgetKind = :widgetKind AND containerBundleIdentifier IS :containerBundleIdentifier AND suggestionMappingReason IS NOT NULL ORDER BY timestamp"
+ "apps:%lu"
+ "dayZero:%{BOOL}d"
+ "descriptors:%lu"
+ "metadata:%lu"
+ "smartStackAppLaunchHistory"
+ "smartStackFetchAndFilterDescriptors"
+ "smartStackFetchDescriptorMetadata"
+ "smartStackGenerateStacks"
+ "smartStackProducerInit"
+ "smartStackRequest"
+ "stacks:%lu"
+ "stacks:0"
- "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _firstWidgetThatIsntUsedYet:usedPersonalities:]"
- "SELECT timestamp, score, duration, suggestionId, suggestionMappingReason FROM timelineDonations WHERE extensionBundleId = :extensionBundleId AND widgetKind = :widgetKind AND containerBundleIdentifier = :containerBundleIdentifier AND suggestionMappingReason IS NOT NULL ORDER BY timestamp"
```
