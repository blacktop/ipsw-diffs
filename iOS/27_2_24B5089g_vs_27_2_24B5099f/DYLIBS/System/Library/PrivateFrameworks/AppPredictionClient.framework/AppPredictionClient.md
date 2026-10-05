## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-675.0.2.0.0
-  __TEXT.__text: 0x1855ac
-  __TEXT.__objc_methlist: 0x18f7c
+677.0.2.0.0
+  __TEXT.__text: 0x188f0c
+  __TEXT.__objc_methlist: 0x190bc
   __TEXT.__const: 0x710
-  __TEXT.__cstring: 0x1c4ba
-  __TEXT.__oslogstring: 0x17c32
-  __TEXT.__gcc_except_tab: 0x2038
+  __TEXT.__cstring: 0x1c96f
+  __TEXT.__oslogstring: 0x180dc
+  __TEXT.__gcc_except_tab: 0x20ac
   __TEXT.__dlopen_cstrs: 0x491
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x85b8
+  __TEXT.__unwind_info: 0x8670
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x63f0
+  __DATA_CONST.__const: 0x6490
   __DATA_CONST.__objc_classlist: 0xe40
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa120
+  __DATA_CONST.__objc_selrefs: 0xa200
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0xc48
-  __DATA_CONST.__objc_arraydata: 0xb28
-  __DATA_CONST.__got: 0x1718
-  __AUTH_CONST.__const: 0x2b00
-  __AUTH_CONST.__cfstring: 0x155c0
-  __AUTH_CONST.__objc_const: 0x461d8
+  __DATA_CONST.__objc_arraydata: 0xb48
+  __DATA_CONST.__got: 0x1730
+  __AUTH_CONST.__const: 0x2ba0
+  __AUTH_CONST.__cfstring: 0x15680
+  __AUTH_CONST.__objc_const: 0x462b0
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_arrayobj: 0x708
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_dictobj: 0x168
+  __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__auth_got: 0x790
   __AUTH.__objc_data: 0x4740
-  __DATA.__objc_ivar: 0x1ca4
+  __DATA.__objc_ivar: 0x1cb8
   __DATA.__data: 0x1cf0
   __DATA_DIRTY.__objc_data: 0x4740
   __DATA_DIRTY.__data: 0x88

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10927
-  Symbols:   16833
-  CStrings:  4841
+  Functions: 10980
+  Symbols:   16896
+  CStrings:  4876
 
Symbols:
+ +[ATXDefaultHomeScreenItemManager _widgetIdentifiersNotAllowedForClient:]
+ +[ATXDefaultHomeScreenItemManager _widgetIdentifiersNotAllowedOnTvOS]
+ +[ATXDefaultHomeScreenItemProducerUtilities remoteWidgetsFromPairedDeviceRanking:size:personalityToDescriptorDictionary:]
+ +[ATXDefaultHomeScreenItemProducerUtilities widgetsByInterleavingWidgets:withWidgets:limit:usedPersonalities:usedAppBundleIds:]
+ -[ATXDefaultHomeScreenItemManager _pairedDeviceRankedWidgetsForClientIdentity:]
+ -[ATXDefaultHomeScreenItemManagerTransfer _deviceIdentifierForRelationshipIdentifier:]
+ -[ATXDefaultHomeScreenItemManagerTransfer _fetchWidgetSmartStackForPairedTvOSDeviceWithRequest:completionHandler:]
+ -[ATXDefaultHomeScreenItemManagerTransfer _hasPairedDeviceImportForVariant:]
+ -[ATXDefaultHomeScreenItemManagerTransfer _pairedDevicePathForVariant:sourceDeviceIdentifier:]
+ -[ATXDefaultHomeScreenItemManagerTransfer importedWidgetSmartStacksByPathForVariant:]
+ -[ATXDefaultHomeScreenItemManagerTransfer pairedDeviceWidgetSmartStackForVariant:relationshipIdentifier:maximumAge:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _blendedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _generatedStacksWithRequest:includeRequiredWidgets:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _pairedDeviceRemoteWidgetsForSize:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _stacksByFillingWithPairedDeviceThirdPartyWidgets:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _tvOSRequiredWidgetsKeyForOnboarding:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer pairedDeviceRankedWidgets]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer setPairedDeviceRankedWidgets:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer usageRankedStacksWithRequest:]
+ -[ATXDefaultHomeScreenItemProducer _onboardingStacksProducerForSmartStackRequest:]
+ -[ATXDefaultHomeScreenItemProducer pairedDeviceRankedWidgets]
+ -[ATXDefaultHomeScreenItemProducer setPairedDeviceRankedWidgets:]
+ -[ATXDefaultHomeScreenItemProducer usageRankedStacksWithRequest:]
+ -[ATXDefaultWidgetSuggesterClient fetchWidgetSmartStackForPairedTvOSDeviceWithRequest:completionHandler:]
+ -[ATXWidgetSmartStackResponse setSourceDeviceIdentifier:]
+ -[ATXWidgetSmartStackResponse sourceDeviceIdentifier]
+ _ATXCanonicalContainerBundleIdForWidgetDedup
+ _ATXCanonicalContainerBundleIdForWidgetDedup.aliases
+ _ATXCanonicalContainerBundleIdForWidgetDedup.onceToken
+ _OBJC_CLASS_$_CHSRemoteDeviceService
+ _OBJC_CLASS_$_NSOrderedSet
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemManagerTransfer._pairedDevicePathPrefix
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemManagerTransfer._widgetSuggesterClient
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemOnboardingStacksProducer._pairedDeviceRankedWidgets
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemProducer._pairedDeviceRankedWidgets
+ _OBJC_IVAR_$_ATXWidgetSmartStackResponse._sourceDeviceIdentifier
+ ___103-[ATXDefaultHomeScreenItemOnboardingStacksProducer _generatedStacksWithRequest:includeRequiredWidgets:]_block_invoke
+ ___105-[ATXDefaultWidgetSuggesterClient fetchWidgetSmartStackForPairedTvOSDeviceWithRequest:completionHandler:]_block_invoke
+ ___107-[ATXDefaultHomeScreenItemOnboardingStacksProducer _pairedDeviceRemoteWidgetsForSize:denyListOfExtensions:]_block_invoke
+ ___114-[ATXDefaultHomeScreenItemManagerTransfer _fetchWidgetSmartStackForPairedTvOSDeviceWithRequest:completionHandler:]_block_invoke
+ ___153-[ATXDefaultHomeScreenItemOnboardingStacksProducer _dayZeroStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]_block_invoke
+ ___153-[ATXDefaultHomeScreenItemOnboardingStacksProducer _dayZeroStacksFromRequiredPersonalitiesPerStack:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]_block_invoke_2
+ ___196-[ATXDefaultHomeScreenItemOnboardingStacksProducer _blendedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]_block_invoke
+ ___196-[ATXDefaultHomeScreenItemOnboardingStacksProducer _blendedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]_block_invoke_2
+ ___55-[ATXDefaultHomeScreenItemProducer _personalizedUpdate]_block_invoke
+ ___86-[ATXDefaultHomeScreenItemManagerTransfer _deviceIdentifierForRelationshipIdentifier:]_block_invoke
+ ___86-[ATXDefaultHomeScreenItemManagerTransfer _deviceIdentifierForRelationshipIdentifier:]_block_invoke_2
+ ___ATXCanonicalContainerBundleIdForWidgetDedup_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e49_v24?0"ATXWidgetSmartStackResponse"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e29_v16?0"NSMutableDictionary"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e29_v16?0"NSMutableDictionary"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e30_B16?0"ATXWidgetPersonality"8ls32l8
+ ___pairedDeviceIdentifiersByRelationship_block_invoke
+ ___sharedWidgetSuggesterClient_block_invoke
+ _cachePath
+ _canonicalDeviceIdentifier
+ _isNilOrArrayOfWidgets
+ _isWellFormedSmartStackResponse
+ _kATXPairedDeviceWidgetRankingMaximumAge
+ _pairedDeviceIdentifiersByRelationship
+ _pairedDeviceIdentifiersByRelationship.lock
+ _pairedDeviceIdentifiersByRelationship.onceToken
+ _sharedWidgetSuggesterClient.client
+ _sharedWidgetSuggesterClient.onceToken
- ___79-[ATXDefaultHomeScreenItemOnboardingStacksProducer generatedStacksWithRequest:]_block_invoke
CStrings:
+ "%s: %lu third-party widgets available from the paired device's ranking"
+ "%s: Couldn't reach duetexpertd (%@), generating smart stacks in process"
+ "%s: Couldn't read import at %@: %@"
+ "%s: Importing %lu smart stacks from source device %@"
+ "%s: No descriptor available for required personalities %{public}@"
+ "%s: No paired device for relationship %@"
+ "%s: No usable stacks from paired device %@ (error: %@)"
+ "%s: Not importing malformed smart stacks"
+ "%s: Number of Stacks being requested %lu, including required widgets: %{BOOL}d"
+ "%s: Requesting smart stacks from duetexpertd for Client: %@"
+ "%s: Skipping remote widget %{public}@:%{public}@ because a local version exists for %{public}@:%{public}@"
+ "%s: blending %lu of the paired device's %lu ranked widgets"
+ "%s: blending %lu of the paired device's %lu ranked widgets into gallery widgets"
+ "%s: generating usage ranked stacks for Client. numDescriptors:%lu, descriptorCacheSize:%lu, appsWithLaunches:%lu"
+ "%s: stack has %lu of %lu widgets; the paired device has no more third-party widgets to fill it"
+ "(unstamped)"
+ "-[ATXDefaultHomeScreenItemManagerTransfer _fetchWidgetSmartStackForPairedTvOSDeviceWithRequest:completionHandler:]"
+ "-[ATXDefaultHomeScreenItemManagerTransfer _fetchWidgetSmartStackForPairedTvOSDeviceWithRequest:completionHandler:]_block_invoke"
+ "-[ATXDefaultHomeScreenItemManagerTransfer importWidgetSmartStackWithRequest:response:completionHandler:]"
+ "-[ATXDefaultHomeScreenItemManagerTransfer importedWidgetSmartStacksByPathForVariant:]"
+ "-[ATXDefaultHomeScreenItemManagerTransfer pairedDeviceWidgetSmartStackForVariant:relationshipIdentifier:maximumAge:]"
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _blendedStacksForSize:requiredWidgetPersonalitiesPerStack:rankedWidgets:usedWidgetPersonalities:maxNumberOfWidgetsPerStack:denyListOfExtensions:]"
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _generatedStacksWithRequest:includeRequiredWidgets:]"
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _stacksByFillingWithPairedDeviceThirdPartyWidgets:size:maxNumberOfWidgetsPerStack:denyListOfExtensions:]"
+ "-[ATXDefaultHomeScreenItemProducer usageRankedStacksWithRequest:]"
+ "ATXDefaultWidgetSuggesterClient: XPC error; could not generate smart stacks for paired tvOS device via duetexpertd: %@"
+ "Smart stacks to import are malformed"
+ "com.apple.iCal"
+ "dayZero:%{BOOL}d pairedDevice:%{BOOL}d"
+ "denyListWidgetsTvOS"
+ "onboardingDefaultStackTvOS"
+ "smartStackDenyListAssetLookup"
+ "smartStackDescriptorCacheAccess"
+ "smartStackPairedDeviceRanking"
+ "smartStackProtectedAppsLookup"
+ "sourceDeviceIdentifier"
+ "v16@?0@\"NSMutableDictionary\"8"
+ "v24@?0@\"ATXWidgetSmartStackResponse\"8@\"NSError\"16"
+ "widgets:%lu"
- "%s: Number of Stacks being requested %lu"
- "%s: Skipping remote widget because local version exists for %@:%@"
- "-[ATXDefaultHomeScreenItemOnboardingStacksProducer generatedStacksWithRequest:]"
- "dayZero:%{BOOL}d"
```
