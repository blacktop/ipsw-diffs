## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-671.0.2.0.1
-  __TEXT.__text: 0x184838
-  __TEXT.__objc_methlist: 0x18f44
-  __TEXT.__const: 0x708
-  __TEXT.__cstring: 0x1c3ab
-  __TEXT.__oslogstring: 0x179bc
+674.0.1.0.0
+  __TEXT.__text: 0x1855d0
+  __TEXT.__objc_methlist: 0x18f7c
+  __TEXT.__const: 0x710
+  __TEXT.__cstring: 0x1c4ba
+  __TEXT.__oslogstring: 0x17c32
   __TEXT.__gcc_except_tab: 0x2038
   __TEXT.__dlopen_cstrs: 0x491
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x85a8
+  __TEXT.__unwind_info: 0x85b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa0f8
+  __DATA_CONST.__objc_selrefs: 0xa120
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0xc48
   __DATA_CONST.__objc_arraydata: 0xb28
   __DATA_CONST.__got: 0x1718
   __AUTH_CONST.__const: 0x2b00
-  __AUTH_CONST.__cfstring: 0x155a0
-  __AUTH_CONST.__objc_const: 0x46178
+  __AUTH_CONST.__cfstring: 0x155c0
+  __AUTH_CONST.__objc_const: 0x461d8
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_arrayobj: 0x708
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__auth_got: 0x790
   __AUTH.__objc_data: 0x4740
-  __DATA.__objc_ivar: 0x1c98
+  __DATA.__objc_ivar: 0x1ca4
   __DATA.__data: 0x1cf0
   __DATA_DIRTY.__objc_data: 0x4740
   __DATA_DIRTY.__data: 0x88

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10920
-  Symbols:   20546
-  CStrings:  4821
+  Functions: 10927
+  Symbols:   20556
+  CStrings:  4841
 
Symbols:
+ +[ATXDefaultHomeScreenItemProducerUtilities similarThirdPartyWidgetsForPosition:assets:]
+ -[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:]
+ -[ATXAppLaunches rawLaunchCountAndDistinctDaysLaunchedForAllAppsOverLastDays:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _dayZeroStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _firstWidgetThatIsntUsedYet:usedPersonalities:size:]
+ -[ATXDefaultHomeScreenItemProducer _computeNewlyInstalledThresholdsIfNeeded]
+ -[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]
+ -[ATXInformationStore fetchAllDistinctWidgetsIgnoringIntentWithTimelineDonations]
+ GCC_except_table236
+ GCC_except_table240
+ GCC_except_table244
+ GCC_except_table248
+ GCC_except_table252
+ GCC_except_table255
+ GCC_except_table259
+ GCC_except_table262
+ GCC_except_table266
+ GCC_except_table275
+ GCC_except_table280
+ GCC_except_table284
+ GCC_except_table288
+ GCC_except_table291
+ GCC_except_table294
+ GCC_except_table298
+ GCC_except_table302
+ GCC_except_table305
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._newInstallThreshold
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._widgetInstallDateThreshold
+ _OBJC_IVAR_$_ATXHomeScreenConfigCache._usesDefaultRootPath
+ ___78-[ATXAppLaunches rawLaunchCountAndDistinctDaysLaunchedForAllAppsOverLastDays:]_block_invoke
+ ___78-[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]_block_invoke
+ ___78-[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]_block_invoke_2
+ ___78-[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]_block_invoke_3
+ ___80-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:]_block_invoke
+ ___80-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:]_block_invoke_2
+ ___80-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:]_block_invoke_3
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
- GCC_except_table234
- GCC_except_table238
- GCC_except_table242
- GCC_except_table246
- GCC_except_table250
- GCC_except_table253
- GCC_except_table257
- GCC_except_table260
- GCC_except_table264
- GCC_except_table273
- GCC_except_table278
- GCC_except_table28
- GCC_except_table282
- GCC_except_table286
- GCC_except_table289
- GCC_except_table292
- GCC_except_table296
- GCC_except_table300
- GCC_except_table303
- ___67-[ATXInformationStore fetchDistinctWidgetsIgnoringIntentSinceDate:]_block_invoke
- ___67-[ATXInformationStore fetchDistinctWidgetsIgnoringIntentSinceDate:]_block_invoke_2
- ___67-[ATXInformationStore fetchDistinctWidgetsIgnoringIntentSinceDate:]_block_invoke_3
- ___71-[ATXWidgetDescriptorCache _queue_fetchAllDescriptorMetadataWithError:]_block_invoke
- ___79-[ATXAppLaunches rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysForAllApps]_block_invoke
- ___81+[ATXDefaultHomeScreenItemProducerUtilities similarThirdPartyWidgetsForPosition:]_block_invoke
- ___81-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:]_block_invoke
- ___81-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:]_block_invoke_2
- ___81-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:]_block_invoke_3
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
