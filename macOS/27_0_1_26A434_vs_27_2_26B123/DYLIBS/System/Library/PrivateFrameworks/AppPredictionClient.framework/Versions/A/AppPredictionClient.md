## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/Versions/A/AppPredictionClient`

```diff

-671.0.1.0.1
-  __TEXT.__text: 0x19fa20
-  __TEXT.__objc_methlist: 0x18a2c
-  __TEXT.__const: 0x700
-  __TEXT.__cstring: 0x1bdfc
-  __TEXT.__oslogstring: 0x1719a
-  __TEXT.__gcc_except_tab: 0x1c34
+678.0.1.0.0
+  __TEXT.__text: 0x1a445c
+  __TEXT.__objc_methlist: 0x18b9c
+  __TEXT.__const: 0x708
+  __TEXT.__cstring: 0x1c2a2
+  __TEXT.__oslogstring: 0x178ab
+  __TEXT.__gcc_except_tab: 0x1cac
   __TEXT.__dlopen_cstrs: 0x2cc
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x66e8
+  __TEXT.__unwind_info: 0x6768
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9f60
+  __DATA_CONST.__objc_selrefs: 0xa060
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0xbf0
-  __DATA_CONST.__objc_arraydata: 0xb10
-  __DATA_CONST.__got: 0x16c8
-  __AUTH_CONST.__const: 0x6440
-  __AUTH_CONST.__cfstring: 0x15460
-  __AUTH_CONST.__objc_const: 0x44770
+  __DATA_CONST.__objc_arraydata: 0xb30
+  __DATA_CONST.__got: 0x16d8
+  __AUTH_CONST.__const: 0x6550
+  __AUTH_CONST.__cfstring: 0x15560
+  __AUTH_CONST.__objc_const: 0x448a8
   __AUTH_CONST.__objc_intobj: 0xa98
   __AUTH_CONST.__objc_arrayobj: 0x6d8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_dictobj: 0x168
+  __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__auth_got: 0x690
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x33e0
-  __DATA.__objc_ivar: 0x1c30
+  __DATA.__objc_ivar: 0x1c50
   __DATA.__data: 0x1aa0
-  __DATA.__bss: 0x310
+  __DATA.__bss: 0x320
   __DATA_DIRTY.__objc_data: 0x55f0
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x320
+  __DATA_DIRTY.__bss: 0x330
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10873
-  Symbols:   20584
-  CStrings:  4773
+  Functions: 10927
+  Symbols:   20678
+  CStrings:  4825
 
Symbols:
+ +[ATXDefaultHomeScreenItemManager _widgetIdentifiersNotAllowedForClient:]
+ +[ATXDefaultHomeScreenItemManager _widgetIdentifiersNotAllowedOnTvOS]
+ +[ATXDefaultHomeScreenItemProducerUtilities remoteWidgetsFromPairedDeviceRanking:size:personalityToDescriptorDictionary:]
+ +[ATXDefaultHomeScreenItemProducerUtilities similarThirdPartyWidgetsForPosition:assets:]
+ +[ATXDefaultHomeScreenItemProducerUtilities widgetsByInterleavingWidgets:withWidgets:limit:usedPersonalities:usedAppBundleIds:]
+ -[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:]
+ -[ATXAppLaunches rawLaunchCountAndDistinctDaysLaunchedForAllAppsOverLastDays:]
+ -[ATXDefaultHomeScreenItemManager _pairedDeviceRankedWidgetsForClientIdentity:]
+ -[ATXDefaultHomeScreenItemManagerTransfer _deviceIdentifierForRelationshipIdentifier:]
+ -[ATXDefaultHomeScreenItemManagerTransfer _hasPairedDeviceImportForVariant:]
+ -[ATXDefaultHomeScreenItemManagerTransfer _pairedDevicePathForVariant:sourceDeviceIdentifier:]
+ -[ATXDefaultHomeScreenItemManagerTransfer importedWidgetSmartStacksByPathForVariant:]
+ -[ATXDefaultHomeScreenItemManagerTransfer pairedDeviceWidgetSmartStackForVariant:relationshipIdentifier:maximumAge:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _blendedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _dayZeroStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _firstWidgetThatIsntUsedYet:usedPersonalities:size:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _generatedStacksWithRequest:includeRequiredWidgets:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _pairedDeviceRemoteWidgetsForSize:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _stacksByFillingWithPairedDeviceThirdPartyWidgets:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _tvOSRequiredWidgetsKeyForOnboarding:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer pairedDeviceRankedWidgets]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer setPairedDeviceRankedWidgets:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer usageRankedStacksWithRequest:]
+ -[ATXDefaultHomeScreenItemProducer _computeNewlyInstalledThresholdsIfNeeded]
+ -[ATXDefaultHomeScreenItemProducer _onboardingStacksProducerForSmartStackRequest:]
+ -[ATXDefaultHomeScreenItemProducer pairedDeviceRankedWidgets]
+ -[ATXDefaultHomeScreenItemProducer setPairedDeviceRankedWidgets:]
+ -[ATXDefaultHomeScreenItemProducer usageRankedStacksWithRequest:]
+ -[ATXDefaultWidgetSuggesterClient fetchWidgetSmartStackForPairedTvOSDeviceWithRequest:completionHandler:]
+ -[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]
+ -[ATXInformationStore fetchAllDistinctWidgetsIgnoringIntentWithTimelineDonations]
+ -[ATXWidgetSmartStackResponse setSourceDeviceIdentifier:]
+ -[ATXWidgetSmartStackResponse sourceDeviceIdentifier]
+ ATXCanonicalContainerBundleIdForWidgetDedup
+ ATXCanonicalContainerBundleIdForWidgetDedup.aliases
+ ATXCanonicalContainerBundleIdForWidgetDedup.onceToken
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
+ OBJC_IVAR_$_ATXDefaultHomeScreenItemManagerTransfer._pairedDevicePathPrefix
+ OBJC_IVAR_$_ATXDefaultHomeScreenItemManagerTransfer._widgetSuggesterClient
+ OBJC_IVAR_$_ATXDefaultHomeScreenItemOnboardingStacksProducer._pairedDeviceRankedWidgets
+ OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._newInstallThreshold
+ OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._pairedDeviceRankedWidgets
+ OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._widgetInstallDateThreshold
+ OBJC_IVAR_$_ATXHomeScreenConfigCache._usesDefaultRootPath
+ OBJC_IVAR_$_ATXWidgetSmartStackResponse._sourceDeviceIdentifier
+ _ATXCanonicalContainerBundleIdForWidgetDedup
+ _OBJC_CLASS_$_CHSRemoteDeviceService
+ _OBJC_CLASS_$_NSOrderedSet
+ __103-[ATXDefaultHomeScreenItemOnboardingStacksProducer _generatedStacksWithRequest:includeRequiredWidgets:]_block_invoke
+ __105-[ATXDefaultWidgetSuggesterClient fetchWidgetSmartStackForPairedTvOSDeviceWithRequest:completionHandler:]_block_invoke
+ __153-[ATXDefaultHomeScreenItemOnboardingStacksProducer _dayZeroStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]_block_invoke
+ __196-[ATXDefaultHomeScreenItemOnboardingStacksProducer _blendedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]_block_invoke
+ __78-[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]_block_invoke_3
+ __80-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:]_block_invoke
+ __86-[ATXDefaultHomeScreenItemManagerTransfer _deviceIdentifierForRelationshipIdentifier:]_block_invoke
+ ___103-[ATXDefaultHomeScreenItemOnboardingStacksProducer _generatedStacksWithRequest:includeRequiredWidgets:]_block_invoke
+ ___105-[ATXDefaultWidgetSuggesterClient fetchWidgetSmartStackForPairedTvOSDeviceWithRequest:completionHandler:]_block_invoke
+ ___107-[ATXDefaultHomeScreenItemOnboardingStacksProducer _pairedDeviceRemoteWidgetsForSize:denyListOfExtensions:]_block_invoke
+ ___153-[ATXDefaultHomeScreenItemOnboardingStacksProducer _dayZeroStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]_block_invoke
+ ___196-[ATXDefaultHomeScreenItemOnboardingStacksProducer _blendedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]_block_invoke
+ ___55-[ATXDefaultHomeScreenItemProducer _personalizedUpdate]_block_invoke
+ ___78-[ATXAppLaunches rawLaunchCountAndDistinctDaysLaunchedForAllAppsOverLastDays:]_block_invoke
+ ___78-[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]_block_invoke
+ ___78-[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]_block_invoke_2
+ ___78-[ATXInformationStore _fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:]_block_invoke_3
+ ___80-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:]_block_invoke
+ ___80-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:]_block_invoke_2
+ ___86-[ATXDefaultHomeScreenItemManagerTransfer _deviceIdentifierForRelationshipIdentifier:]_block_invoke
+ ___88+[ATXDefaultHomeScreenItemProducerUtilities similarThirdPartyWidgetsForPosition:assets:]_block_invoke
+ ___ATXCanonicalContainerBundleIdForWidgetDedup_block_invoke
+ ___block_descriptor_48_e8_32s40r_e29_v16?0"NSMutableDictionary"8l
+ ___block_descriptor_48_e8_32s40s_e29_v16?0"NSMutableDictionary"8l
+ ___block_descriptor_48_e8_32s_e30_B16?0"ATXWidgetPersonality"8l
+ ___pairedDeviceIdentifiersByRelationship_block_invoke
+ _cachePath
+ _canonicalDeviceIdentifier
+ _isNilOrArrayOfWidgets
+ _isWellFormedSmartStackResponse
+ _kATXAppLaunchesSmartStackLookbackDays
+ _kATXPairedDeviceWidgetRankingMaximumAge
+ _objc_msgSend$_blendedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:
+ _objc_msgSend$_computeNewlyInstalledThresholdsIfNeeded
+ _objc_msgSend$_dayZeroStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:
+ _objc_msgSend$_deviceIdentifierForRelationshipIdentifier:
+ _objc_msgSend$_fetchDistinctWidgetsIgnoringIntentWithQuery:sinceDate:
+ _objc_msgSend$_firstWidgetThatIsntUsedYet:usedPersonalities:size:
+ _objc_msgSend$_generatedStacksWithRequest:includeRequiredWidgets:
+ _objc_msgSend$_hasPairedDeviceImportForVariant:
+ _objc_msgSend$_onboardingStacksProducerForSmartStackRequest:
+ _objc_msgSend$_pairedDevicePathForVariant:sourceDeviceIdentifier:
+ _objc_msgSend$_pairedDeviceRankedWidgetsForClientIdentity:
+ _objc_msgSend$_pairedDeviceRemoteWidgetsForSize:denyListOfExtensions:
+ _objc_msgSend$_rawLaunchCountAndDistinctDaysLaunchedOverLastDays:withFilter:
+ _objc_msgSend$_stacksByFillingWithPairedDeviceThirdPartyWidgets:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:
+ _objc_msgSend$_tvOSRequiredWidgetsKeyForOnboarding:
+ _objc_msgSend$_widgetIdentifiersNotAllowedForClient:
+ _objc_msgSend$allPairedDevices
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$fetchWidgetSmartStackForPairedTvOSDeviceWithRequest:completionHandler:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$orderedSetWithObjects:
+ _objc_msgSend$pairedDeviceRankedWidgets
+ _objc_msgSend$rawLaunchCountAndDistinctDaysLaunchedForAllAppsOverLastDays:
+ _objc_msgSend$relationshipID
+ _objc_msgSend$remoteWidgetsFromPairedDeviceRanking:size:personalityToDescriptorDictionary:
+ _objc_msgSend$setPairedDeviceRankedWidgets:
+ _objc_msgSend$similarThirdPartyWidgetsForPosition:assets:
+ _objc_msgSend$sourceDeviceIdentifier
+ _objc_msgSend$usageRankedStacksWithRequest:
+ _objc_msgSend$widgetsByInterleavingWidgets:withWidgets:limit:usedPersonalities:usedAppBundleIds:
+ _pairedDeviceIdentifiersByRelationship
+ pairedDeviceIdentifiersByRelationship
+ pairedDeviceIdentifiersByRelationship.lock
+ pairedDeviceIdentifiersByRelationship.onceToken
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
- __79-[ATXDefaultHomeScreenItemOnboardingStacksProducer generatedStacksWithRequest:]_block_invoke
- __81-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:]_block_invoke
- ___67-[ATXInformationStore fetchDistinctWidgetsIgnoringIntentSinceDate:]_block_invoke
- ___67-[ATXInformationStore fetchDistinctWidgetsIgnoringIntentSinceDate:]_block_invoke_2
- ___67-[ATXInformationStore fetchDistinctWidgetsIgnoringIntentSinceDate:]_block_invoke_3
- ___71-[ATXWidgetDescriptorCache _queue_fetchAllDescriptorMetadataWithError:]_block_invoke
- ___79-[ATXAppLaunches rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysForAllApps]_block_invoke
- ___79-[ATXDefaultHomeScreenItemOnboardingStacksProducer generatedStacksWithRequest:]_block_invoke
- ___81+[ATXDefaultHomeScreenItemProducerUtilities similarThirdPartyWidgetsForPosition:]_block_invoke
- ___81-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:]_block_invoke
- ___81-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:]_block_invoke_2
- ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke_2
- _objc_msgSend$_firstWidgetThatIsntUsedYet:usedPersonalities:
- _objc_msgSend$_rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:
- _objc_msgSend$similarThirdPartyWidgetsForPosition:
CStrings:
+ "%s: %lu third-party widgets available from the paired device's ranking"
+ "%s: Couldn't read import at %@: %@"
+ "%s: Importing %lu smart stacks from source device %@"
+ "%s: No descriptor available for required personalities %{public}@"
+ "%s: No paired device for relationship %@"
+ "%s: No usable stacks from paired device %@ (error: %@)"
+ "%s: Not importing malformed smart stacks"
+ "%s: Number of Stacks being requested %lu, including required widgets: %{BOOL}d"
+ "%s: Skipping descriptor disfavored for tvOS: %@"
+ "%s: Skipping descriptor that does not support systemSmall: %@"
+ "%s: Skipping remote widget %{public}@:%{public}@ because a local version exists for %{public}@:%{public}@"
+ "%s: blending %lu of the paired device's %lu ranked widgets"
+ "%s: blending %lu of the paired device's %lu ranked widgets into gallery widgets"
+ "%s: built day zero default stack with %lu widgets"
+ "%s: descriptor metadata unavailable (%{public}@), continuing with %lu descriptors because this is a day zero request"
+ "%s: generating usage ranked stacks for Client. numDescriptors:%lu, descriptorCacheSize:%lu, appsWithLaunches:%lu"
+ "%s: not adding default widget %{public}@ because it is already used"
+ "%s: not adding default widget %{public}@ because it is in the client's deny list"
+ "%s: not adding widget %{public}@ because it does not support stack layout size %lu"
+ "%s: stack has %lu of %lu widgets; the paired device has no more third-party widgets to fill it"
+ "(unstamped)"
+ ","
+ "-[ATXDefaultHomeScreenItemManagerTransfer importWidgetSmartStackWithRequest:response:completionHandler:]"
+ "-[ATXDefaultHomeScreenItemManagerTransfer importedWidgetSmartStacksByPathForVariant:]"
+ "-[ATXDefaultHomeScreenItemManagerTransfer pairedDeviceWidgetSmartStackForVariant:relationshipIdentifier:maximumAge:]"
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _blendedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]"
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _dayZeroStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]"
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _firstWidgetThatIsntUsedYet:usedPersonalities:size:]"
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _generatedStacksWithRequest:includeRequiredWidgets:]"
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _stacksByFillingWithPairedDeviceThirdPartyWidgets:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]"
+ "-[ATXDefaultHomeScreenItemProducer usageRankedStacksWithRequest:]"
+ "ATXDefaultWidgetSuggesterClient: XPC error; could not generate smart stacks for paired tvOS device via duetexpertd: %@"
+ "SELECT DISTINCT extensionBundleId, containerBundleIdentifier, widgetKind, widgetFamily FROM timelineDonations;"
+ "SELECT timestamp, score, duration, suggestionId, suggestionMappingReason FROM timelineDonations WHERE extensionBundleId = :extensionBundleId AND widgetKind = :widgetKind AND containerBundleIdentifier IS :containerBundleIdentifier AND suggestionMappingReason IS NOT NULL ORDER BY timestamp"
+ "Smart stacks to import are malformed"
+ "apps:%lu"
+ "com.apple.mobilecal"
+ "dayZero:%{BOOL}d pairedDevice:%{BOOL}d"
+ "denyListWidgetsTvOS"
+ "descriptors:%lu"
+ "metadata:%lu"
+ "onboardingDefaultStackTvOS"
+ "smartStackAppLaunchHistory"
+ "smartStackDenyListAssetLookup"
+ "smartStackDescriptorCacheAccess"
+ "smartStackFetchAndFilterDescriptors"
+ "smartStackFetchDescriptorMetadata"
+ "smartStackGenerateStacks"
+ "smartStackPairedDeviceRanking"
+ "smartStackProducerInit"
+ "smartStackProtectedAppsLookup"
+ "smartStackRequest"
+ "sourceDeviceIdentifier"
+ "stacks:%lu"
+ "stacks:0"
+ "v16@?0@\"NSMutableDictionary\"8"
+ "widgets:%lu"
- "%s: Number of Stacks being requested %lu"
- "%s: Skipping remote widget because local version exists for %@:%@"
- "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _firstWidgetThatIsntUsedYet:usedPersonalities:]"
- "-[ATXDefaultHomeScreenItemOnboardingStacksProducer generatedStacksWithRequest:]"
- "SELECT timestamp, score, duration, suggestionId, suggestionMappingReason FROM timelineDonations WHERE extensionBundleId = :extensionBundleId AND widgetKind = :widgetKind AND containerBundleIdentifier = :containerBundleIdentifier AND suggestionMappingReason IS NOT NULL ORDER BY timestamp"
```
