## InputAnalytics

> `/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics`

```diff

-111.3.104.2.0
-  __TEXT.__text: 0x1eaf8
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x257c
-  __TEXT.__const: 0x322
-  __TEXT.__cstring: 0x4cd2
-  __TEXT.__oslogstring: 0x28e0
-  __TEXT.__gcc_except_tab: 0x42c
+111.4.3.0.0
+  __TEXT.__text: 0x20c40
+  __TEXT.__auth_stubs: 0x8b0
+  __TEXT.__objc_methlist: 0x25dc
+  __TEXT.__const: 0x32a
+  __TEXT.__gcc_except_tab: 0x48c
+  __TEXT.__cstring: 0x4db2
+  __TEXT.__oslogstring: 0x296c
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x8c
-  __TEXT.__swift5_capture: 0x98
+  __TEXT.__swift5_typeref: 0x8b
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_capture: 0x98
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x898
+  __TEXT.__unwind_info: 0x9f8
   __TEXT.__eh_frame: 0x310
-  __TEXT.__objc_classname: 0x704
-  __TEXT.__objc_methname: 0x4b48
-  __TEXT.__objc_methtype: 0xa50
-  __TEXT.__objc_stubs: 0x2fc0
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x1918
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __TEXT.__objc_classname: 0x74d
+  __TEXT.__objc_methname: 0x4cae
+  __TEXT.__objc_methtype: 0xadd
+  __TEXT.__objc_stubs: 0x3240
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__const: 0x1a40
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1198
+  __DATA_CONST.__objc_selrefs: 0x11e0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf8
-  __DATA_CONST.__objc_arraydata: 0xdb0
-  __AUTH_CONST.__auth_got: 0x448
-  __AUTH_CONST.__const: 0x5a8
-  __AUTH_CONST.__cfstring: 0x7a00
-  __AUTH_CONST.__objc_const: 0x3f90
+  __DATA_CONST.__objc_arraydata: 0xea0
+  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__const: 0x608
+  __AUTH_CONST.__cfstring: 0x7f00
+  __AUTH_CONST.__objc_const: 0x40c0
   __AUTH_CONST.__objc_intobj: 0xc30
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x930
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH.__objc_data: 0x9d0
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x224
   __DATA.__data: 0x300
-  __DATA.__common: 0x8
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x780
-  __DATA_DIRTY.__bss: 0xd8
-  __DATA_DIRTY.__common: 0x10
+  __DATA_DIRTY.__bss: 0xf0
+  __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/Categories.framework/Categories
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
   - /System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: BF4E23CA-A0AA-3CD6-8AE8-1A4B94079CD6
-  Functions: 980
-  Symbols:   839
-  CStrings:  3159
+  UUID: 4E69CD9F-3410-370F-B257-D3B169758D87
+  Functions: 1037
+  Symbols:   4174
+  CStrings:  3253
 
Symbols:
+ +[IADataStoreBoolean type]
+ +[IADataStoreCounter type]
+ +[IADataStoreDaterange type]
+ +[IADataStoreObject type]
+ +[IADataStoreObject type].cold.1
+ +[IAEventDispatcher dispatchEvent:payload:]
+ +[IAEventDispatcher sharedInstance]
+ +[IAGenmojiAnalytics genmojiCreationFailReasonToEnumMap]
+ +[IAGenmojiAnalytics genmojiCreationFailReasonToEnumMap].cold.1
+ +[IAGenmojiAnalytics genmojiCreationSignalToEnumMap]
+ +[IAGenmojiAnalytics genmojiCreationSignalToEnumMap].cold.1
+ +[IAGenmojiAnalytics genmojiSourceToEnumMap]
+ +[IAGenmojiAnalytics genmojiSourceToEnumMap].cold.1
+ +[IAImageGenerationAnalytics imageCreationFeatureToEnumMap]
+ +[IAImageGenerationAnalytics imageCreationFeatureToEnumMap].cold.1
+ +[IAImageGenerationAnalytics imageCreationSignalToEnumMap]
+ +[IAImageGenerationAnalytics imageCreationSignalToEnumMap].cold.1
+ +[IAKeyboardDetection keyboardIsPresent]
+ +[IAKeyboardDetection keyboardIsPresent].cold.1
+ +[IAKeyboardDetection prewarm]
+ +[IASAnalyzer periodic24HourEvents]
+ +[IASAnalyzerErrors consolidatedErrorStringFromErrors:]
+ +[IASDailyGarbageCollectionStateMachineAnalyzer stringForState:]
+ +[IASTextInputActionsAnalyzer analyzerWithName:]
+ +[IASTextInputActionsAnalyzer getOrInitializeArrayFromArray:forKey:initCapacity:]
+ +[IASTextInputActionsAnalyzer getOrInitializeArrayFromArray:forKey:initCapacity:].cold.1
+ +[IASTextInputActionsAnalyzer getOrInitializeArrayFromArray:forKey:initCapacity:].cold.2
+ +[IASTextInputActionsAnalyzer getOrInitializeArrayFromArray:forKey:initCapacity:].cold.3
+ +[IASTextInputActionsAnalyzer getOrInitializeArrayFromDictionary:forKey:initCapacity:]
+ +[IASTextInputActionsAnalyzer getOrInitializeArrayFromDictionary:forKey:initCapacity:].cold.1
+ +[IASTextInputActionsAnalyzer getOrInitializeDictionaryFrom:forKey:initCapacity:]
+ +[IASTextInputActionsAnalyzer getOrInitializeDictionaryFrom:forKey:initCapacity:].cold.1
+ +[IASTextInputActionsAnalyzerEntry generateAnalyzerEntryFromAction:]
+ +[IASTextInputActionsErrorChecking validateLanguage:]
+ +[IASTextInputActionsErrorChecking validateLanguage:].cold.1
+ +[IASTextInputActionsErrorChecking validateLanguageHelper:]
+ +[IASTextInputActionsErrorChecking validateLanguageHelper:].cold.1
+ +[IASTextInputActionsErrorChecking validateRegion:]
+ +[IASTextInputActionsErrorChecking validateRegion:].cold.1
+ +[IASTextInputActionsErrorChecking validateRegionHelper:]
+ +[IASTextInputActionsErrorChecking validateRegionHelper:].cold.1
+ +[IAServerStats logShutdown]
+ +[IAServerStats logStart]
+ +[IAServerStats reportConnectionStatusSuccessful:]
+ +[IAServerStats reportDailyStats]
+ +[IASignalAnalytics actionQueue]
+ +[IASignalAnalytics actionQueue].cold.1
+ +[IASignalAnalytics asyncSendSignal:toChannel:withNullableSessionID:withPayload:]
+ +[IASignalAnalytics asyncSendSignal:toChannel:withNullableUniqueStringID:withPayload:]
+ +[IASignalAnalytics sendSignal:toChannel:withNullableSessionID:withPayload:]
+ +[IASignalAnalytics sendSignal:toChannel:withNullableSessionID:withPayload:].cold.1
+ +[IASignalAnalytics sendSignal:toChannel:withNullableUniqueStringID:withPayload:]
+ +[IASignalAnalytics sendSignal:toChannel:withNullableUniqueStringID:withPayload:].cold.1
+ +[IASignalAnalytics sendSignal:toChannel:withPayload:]
+ +[IASignalAnalytics sendSignal:toChannel:withPayload:].cold.1
+ +[IASignalAnalytics sendSignal:toChannel:withSessionID:withPayload:]
+ +[IASignalAnalytics sendSignal:toChannel:withUniqueStringID:withPayload:]
+ +[IASignalAnalyticsObject(NSSecureCoding) supportsSecureCoding]
+ +[IASmartRepliesAnalytics smartRepliesSignalToEnumMap]
+ +[IASmartRepliesAnalytics smartRepliesSignalToEnumMap].cold.1
+ +[IAStringDetails emojiCountForText:]
+ +[IAStringDetails getDetailsForString:]
+ +[IAStringDetails normalizedTextLength:]
+ +[IAStringDetails punctuationCountForText:]
+ +[IAStringDetails sharedPunctuationCharacterSet]
+ +[IAStringDetails sharedPunctuationCharacterSet].cold.1
+ +[IATextInputActionsInputMode supportsSecureCoding]
+ +[IATextInputActionsSessionAction shouldSeparatelyTrackKeystrokesForSource:type:]
+ +[IATextInputActionsSessionAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsSessionDeletionAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsSessionDictationBeganAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsSessionEndAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsSessionGlomojiTapAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsSessionInsertionAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsSessionKBMenuAppearAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsSessionKBMenuDismissAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsSessionKBMenuInteractionAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsSessionKeyboardDockItemButtonPressAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsSessionReplaceTextAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsSessionReplaceWithCandidateAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsSessionSelectionAction(NSSecureCoding) supportsSecureCoding]
+ +[IATextInputActionsUtils isEmojiSearchSetInFlagOptions:]
+ +[IATextInputActionsUtils isMarkedTextSetInFlagOptions:]
+ +[IATextInputActionsUtils isWebSetInFlagOptions:]
+ +[IATextInputActionsUtils log10IntegerForInt:]
+ +[IATextInputActionsUtils log10WholeNumberForUnsignedInt:]
+ +[IATextInputActionsUtils sessionActionsEnumFromSource:]
+ +[IATextInputActionsUtils sessionActionsEnumFromSource:type:]
+ +[IATextInputActionsUtils setBool:forField:inFlagOptions:]
+ +[IATextInputActionsUtils setEmojiSearch:inFlagOptions:]
+ +[IATextInputActionsUtils setMarkedText:inFlagOptions:]
+ +[IATextInputActionsUtils setWeb:inFlagOptions:]
+ +[IATextInputActionsUtils stringForKeyboardDockItemButtonPressResult:]
+ +[IATextInputActionsUtils stringForKeyboardDockItemButtonType:]
+ +[IATextInputActionsUtils stringForReplaceWithCandidateType:]
+ +[IATextInputActionsUtils stringForSessionActionsEnum:]
+ +[IATextInputActionsUtils stringForSource:]
+ +[IATextInputActionsUtils stringForType:]
+ +[IAUtility _CTCategoryForBundleId:timeout:]
+ +[IAUtility _CTCategoryForBundleId:timeout:].cold.1
+ +[IAUtility _CTCategoryForBundleId:timeout:].cold.2
+ +[IAUtility _lookupAppBundle:useCTCategoryFallback:timeout:]
+ +[IAUtility _lookupAppBundle:useCTCategoryFallback:timeout:].cold.1
+ +[IAUtility getSPIVersion]
+ +[IAUtility lookupAppBundle:]
+ +[IAUtility lookupAppBundle:useCTCategoryFallback:]
+ +[IAUtility xpcEnabled]
+ +[IAUtility xpcEnabled].cold.1
+ +[IAXPCObject supportsSecureCoding]
+ +[IAXPCSPIObject invalidateConnection]
+ +[IAXPCSPIObject syncQueue]
+ +[IAXPCSPIObject syncQueue].cold.1
+ +[IAXPCSPIObject xpcClient]
+ -[IADataStoreBoolean destroy]
+ -[IADataStoreBoolean destroy].cold.1
+ -[IADataStoreBoolean destroy].cold.2
+ -[IADataStoreBoolean initWithDatastoreHandle:andName:shouldBeCreated:]
+ -[IADataStoreBoolean initWithDatastoreHandle:andName:shouldBeCreated:].cold.1
+ -[IADataStoreBoolean isTrue]
+ -[IADataStoreBoolean negate]
+ -[IADataStoreBoolean persist]
+ -[IADataStoreBoolean persist].cold.1
+ -[IADataStoreBoolean persist].cold.2
+ -[IADataStoreBoolean setFalse]
+ -[IADataStoreBoolean setToValue:]
+ -[IADataStoreBoolean setTrue]
+ -[IADataStoreCounter count]
+ -[IADataStoreCounter decrement]
+ -[IADataStoreCounter decrement].cold.1
+ -[IADataStoreCounter destroy]
+ -[IADataStoreCounter destroy].cold.1
+ -[IADataStoreCounter destroy].cold.2
+ -[IADataStoreCounter increment]
+ -[IADataStoreCounter initWithDatastoreHandle:andName:shouldBeCreated:]
+ -[IADataStoreCounter initWithDatastoreHandle:andName:shouldBeCreated:].cold.1
+ -[IADataStoreCounter persist]
+ -[IADataStoreCounter persist].cold.1
+ -[IADataStoreCounter persist].cold.2
+ -[IADataStoreCounter updateWithCount:]
+ -[IADataStoreDaterange .cxx_destruct]
+ -[IADataStoreDaterange _clearWithMask:]
+ -[IADataStoreDaterange _clearWithMask:].cold.1
+ -[IADataStoreDaterange _updateStartDate]
+ -[IADataStoreDaterange _updateStartDate].cold.1
+ -[IADataStoreDaterange bitfield]
+ -[IADataStoreDaterange bitmaskForDayRangeFrom:to:]
+ -[IADataStoreDaterange bitmaskForLessThanDayN:]
+ -[IADataStoreDaterange clearAllUsage]
+ -[IADataStoreDaterange clearHistoricalUsage]
+ -[IADataStoreDaterange clearMonthlyUsage]
+ -[IADataStoreDaterange destroy]
+ -[IADataStoreDaterange destroy].cold.1
+ -[IADataStoreDaterange destroy].cold.2
+ -[IADataStoreDaterange everUsed]
+ -[IADataStoreDaterange initWithDatastoreHandle:andName:shouldBeCreated:]
+ -[IADataStoreDaterange initWithDatastoreHandle:andName:shouldBeCreated:].cold.1
+ -[IADataStoreDaterange markToday]
+ -[IADataStoreDaterange markToday].cold.1
+ -[IADataStoreDaterange originDate]
+ -[IADataStoreDaterange persist]
+ -[IADataStoreDaterange persist].cold.1
+ -[IADataStoreDaterange persist].cold.2
+ -[IADataStoreDaterange setBitfield:]
+ -[IADataStoreDaterange setOriginDate:]
+ -[IADataStoreDaterange setStartDate:]
+ -[IADataStoreDaterange startDate]
+ -[IADataStoreDaterange timesUsedInDayRangeFrom:to:]
+ -[IADataStoreDaterange timesUsedInDayRangeFrom:to:].cold.1
+ -[IADataStoreDaterange timesUsedInLastNDays:]
+ -[IADataStoreDaterange usageFrequency]
+ -[IADataStoreDaterange usageFrequency].cold.1
+ -[IADataStoreDaterange usageFrequency].cold.2
+ -[IADataStoreDaterange usageFrequency].cold.3
+ -[IADataStoreDaterange usedInDayRangeFrom:to:]
+ -[IADataStoreDaterange usedInLastDay]
+ -[IADataStoreDaterange usedInLastMonth]
+ -[IADataStoreDaterange usedInLastNDays:]
+ -[IADataStoreDaterange usedInLastWeek]
+ -[IADataStoreObject .cxx_destruct]
+ -[IADataStoreObject datastoreHandle]
+ -[IADataStoreObject destroy]
+ -[IADataStoreObject destroy].cold.1
+ -[IADataStoreObject destroy].cold.2
+ -[IADataStoreObject destroyed]
+ -[IADataStoreObject initWithDatastoreHandle:andName:shouldBeCreated:]
+ -[IADataStoreObject initWithDatastoreHandle:andName:shouldBeCreated:].cold.1
+ -[IADataStoreObject lastModified]
+ -[IADataStoreObject name]
+ -[IADataStoreObject persist]
+ -[IADataStoreObject persist].cold.1
+ -[IADataStoreObject persist].cold.2
+ -[IADataStoreObject version]
+ -[IADefaultsDataStore .cxx_destruct]
+ -[IADefaultsDataStore _createErrorWithDescription:code:error:]
+ -[IADefaultsDataStore _validName:]
+ -[IADefaultsDataStore createDataStoreObjectWithName:withType:withError:]
+ -[IADefaultsDataStore createDataStoreObjectWithName:withType:withError:].cold.1
+ -[IADefaultsDataStore createDataStoreObjectWithName:withType:withError:].cold.2
+ -[IADefaultsDataStore createDataStoreObjectWithName:withType:withError:].cold.3
+ -[IADefaultsDataStore createDataStoreObjectWithName:withType:withError:].cold.4
+ -[IADefaultsDataStore datastoreName]
+ -[IADefaultsDataStore defaultsHandle]
+ -[IADefaultsDataStore deleteDataStoreObject:withError:]
+ -[IADefaultsDataStore deleteDataStoreObject:withError:].cold.1
+ -[IADefaultsDataStore deleteDataStoreObject:withError:].cold.2
+ -[IADefaultsDataStore getObjectWithName:withType:withError:]
+ -[IADefaultsDataStore getObjectWithName:withType:withError:].cold.1
+ -[IADefaultsDataStore getObjectWithName:withType:withError:].cold.2
+ -[IADefaultsDataStore getObjectWithName:withType:withError:].cold.3
+ -[IADefaultsDataStore initWithName:]
+ -[IADefaultsDataStore initWithName:].cold.1
+ -[IADefaultsDataStore objectExistsWithName:andType:withError:]
+ -[IADefaultsDataStore objectExistsWithName:andType:withError:].cold.1
+ -[IAEventDispatcher .cxx_destruct]
+ -[IAEventDispatcher dispatchEvent:payload:]
+ -[IAEventDispatcher init]
+ -[IAEventDispatcher isUnitTest]
+ -[IAEventDispatcher payloadsObservedForTesting]
+ -[IAEventDispatcher setIsUnitTest:]
+ -[IAEventDispatcher setPayloadsObservedForTesting:]
+ -[IASAnalyzer .cxx_destruct]
+ -[IASAnalyzer analyzerSessionId]
+ -[IASAnalyzer consumeAction:]
+ -[IASAnalyzer createTimerWithDelay:handler:]
+ -[IASAnalyzer createTimerWithDelay:handler:].cold.1
+ -[IASAnalyzer depthRange]
+ -[IASAnalyzer enumerateAnalytics]
+ -[IASAnalyzer eventHandler]
+ -[IASAnalyzer initWithAnalyzerSessionId:sessionManagerDelegate:queue:]
+ -[IASAnalyzer initWithAnalyzerSessionId:sessionManagerDelegate:queue:eventHandler:]
+ -[IASAnalyzer queue]
+ -[IASAnalyzer sessionErrors]
+ -[IASAnalyzer sessionManagerDelegate]
+ -[IASAnalyzer setAnalyzerSessionId:]
+ -[IASAnalyzer setEventHandler:]
+ -[IASAnalyzer setQueue:]
+ -[IASAnalyzer setSessionErrors:]
+ -[IASAnalyzer setSessionManagerDelegate:]
+ -[IASAnalyzer shouldBeGarbageCollected]
+ -[IASAnalyzerErrors .cxx_destruct]
+ -[IASAnalyzerErrors clear]
+ -[IASAnalyzerErrors errorString]
+ -[IASAnalyzerErrors errors]
+ -[IASAnalyzerErrors init]
+ -[IASAnalyzerErrors logErrorCodeIfNotNil:]
+ -[IASAnalyzerErrors logErrorCodeIfNotNil:].cold.1
+ -[IASAnalyzerErrors setErrors:]
+ -[IASDailyGarbageCollectionAnalyzer .cxx_destruct]
+ -[IASDailyGarbageCollectionAnalyzer asynchronousSignalIsConsistent:]
+ -[IASDailyGarbageCollectionAnalyzer consumeAction:]
+ -[IASDailyGarbageCollectionAnalyzer dateOfLastAction]
+ -[IASDailyGarbageCollectionAnalyzer initWithAnalyzerSessionId:sessionManagerDelegate:queue:]
+ -[IASDailyGarbageCollectionAnalyzer initWithAnalyzerSessionId:sessionManagerDelegate:queue:eventHandler:]
+ -[IASDailyGarbageCollectionAnalyzer lastConsumedSignalTimestamp]
+ -[IASDailyGarbageCollectionAnalyzer setDateOfLastAction:]
+ -[IASDailyGarbageCollectionAnalyzer setLastConsumedSignalTimestamp:]
+ -[IASDailyGarbageCollectionAnalyzer shouldBeGarbageCollected]
+ -[IASDailyGarbageCollectionStateMachineAnalyzer setState:]
+ -[IASDailyGarbageCollectionStateMachineAnalyzer state]
+ -[IASDailyGarbageCollectionStateMachineAnalyzer stringForState:]
+ -[IASTextInputActionsAnalyzer .cxx_destruct]
+ -[IASTextInputActionsAnalyzer computeSessionActionsStringOnSession:]
+ -[IASTextInputActionsAnalyzer consumeAction:]
+ -[IASTextInputActionsAnalyzer consumeAction:].cold.1
+ -[IASTextInputActionsAnalyzer consumeAction:].cold.2
+ -[IASTextInputActionsAnalyzer consumeAction:].cold.3
+ -[IASTextInputActionsAnalyzer consumeAction:].cold.4
+ -[IASTextInputActionsAnalyzer description]
+ -[IASTextInputActionsAnalyzer enumerateAnalytics]
+ -[IASTextInputActionsAnalyzer enumerateTextInputActionsAnalytics:]
+ -[IASTextInputActionsAnalyzer enumerateTextInputActionsAnalytics:].cold.1
+ -[IASTextInputActionsAnalyzer enumerateTextInputActionsAnalytics:].cold.2
+ -[IASTextInputActionsAnalyzer increaseCountForAppBundleId:forSource:forActionType:forFlagOptions:forInputModeKey:byAnalyzerEntry:]
+ -[IASTextInputActionsAnalyzer increaseCountForAppBundleId:forSource:forActionType:forFlagOptions:forInputModeKey:byAnalyzerEntry:].cold.1
+ -[IASTextInputActionsAnalyzer initWithAnalyzerSessionId:sessionManagerDelegate:queue:]
+ -[IASTextInputActionsAnalyzer initWithAnalyzerSessionId:sessionManagerDelegate:queue:].cold.1
+ -[IASTextInputActionsAnalyzer initWithAnalyzerSessionId:sessionManagerDelegate:queue:eventHandler:]
+ -[IASTextInputActionsAnalyzer initWithAnalyzerSessionId:sessionManagerDelegate:queue:eventHandler:].cold.1
+ -[IASTextInputActionsAnalyzer keyboardTrialParameters]
+ -[IASTextInputActionsAnalyzer reset]
+ -[IASTextInputActionsAnalyzer reset].cold.1
+ -[IASTextInputActionsAnalyzer setKeyboardTrialParameters:]
+ -[IASTextInputActionsAnalyzer shouldBeGarbageCollected]
+ -[IASTextInputActionsAnalyzerEntry increaseWithEntry:]
+ -[IASTextInputActionsAnalyzerEntry inputActions]
+ -[IASTextInputActionsAnalyzerEntry isAllZeroes]
+ -[IASTextInputActionsAnalyzerEntry netCharacters]
+ -[IASTextInputActionsAnalyzerEntry netEmojiCharacters]
+ -[IASTextInputActionsAnalyzerEntry setInputActions:]
+ -[IASTextInputActionsAnalyzerEntry setNetCharacters:]
+ -[IASTextInputActionsAnalyzerEntry setNetEmojiCharacters:]
+ -[IASTextInputActionsAnalyzerEntry setUserRemovedCharacters:]
+ -[IASTextInputActionsAnalyzerEntry setUserRemovedEmojiCharacters:]
+ -[IASTextInputActionsAnalyzerEntry userRemovedCharacters]
+ -[IASTextInputActionsAnalyzerEntry userRemovedEmojiCharacters]
+ -[IASTextInputActionsEvent .cxx_destruct]
+ -[IASTextInputActionsEvent bundleId]
+ -[IASTextInputActionsEvent dispatchEvent:]
+ -[IASTextInputActionsEvent dispatchEvent]
+ -[IASTextInputActionsEvent initWithbundleId:]
+ -[IASTextInputActionsEvent inputActionCount]
+ -[IASTextInputActionsEvent inputModeIdentifier]
+ -[IASTextInputActionsEvent isDispatchable]
+ -[IASTextInputActionsEvent isEmojiSearch]
+ -[IASTextInputActionsEvent isMarkedText]
+ -[IASTextInputActionsEvent keyboardLayout]
+ -[IASTextInputActionsEvent keyboardType]
+ -[IASTextInputActionsEvent keyboardVariant]
+ -[IASTextInputActionsEvent language]
+ -[IASTextInputActionsEvent netCharacters]
+ -[IASTextInputActionsEvent netEmojiCharacters]
+ -[IASTextInputActionsEvent region]
+ -[IASTextInputActionsEvent resetMeasures]
+ -[IASTextInputActionsEvent sessionActions]
+ -[IASTextInputActionsEvent sessionIsModeless]
+ -[IASTextInputActionsEvent setBundleId:]
+ -[IASTextInputActionsEvent setInputActionCount:]
+ -[IASTextInputActionsEvent setInputModeIdentifier:]
+ -[IASTextInputActionsEvent setIsEmojiSearch:]
+ -[IASTextInputActionsEvent setIsMarkedText:]
+ -[IASTextInputActionsEvent setKeyboardLayout:]
+ -[IASTextInputActionsEvent setKeyboardType:]
+ -[IASTextInputActionsEvent setKeyboardVariant:]
+ -[IASTextInputActionsEvent setLanguage:]
+ -[IASTextInputActionsEvent setNetCharacters:]
+ -[IASTextInputActionsEvent setNetEmojiCharacters:]
+ -[IASTextInputActionsEvent setRegion:]
+ -[IASTextInputActionsEvent setSessionActions:]
+ -[IASTextInputActionsEvent setSessionIsModeless:]
+ -[IASTextInputActionsEvent setSource:]
+ -[IASTextInputActionsEvent setType:]
+ -[IASTextInputActionsEvent setUserRemovedCharacters:]
+ -[IASTextInputActionsEvent setUserRemovedEmojiCharacters:]
+ -[IASTextInputActionsEvent source]
+ -[IASTextInputActionsEvent type]
+ -[IASTextInputActionsEvent userRemovedCharacters]
+ -[IASTextInputActionsEvent userRemovedEmojiCharacters]
+ -[IASignalAnalyticsObject .cxx_destruct]
+ -[IASignalAnalyticsObject analyticsSessionIdString]
+ -[IASignalAnalyticsObject channelName]
+ -[IASignalAnalyticsObject description]
+ -[IASignalAnalyticsObject initWithChannel:signal:sessionIdString:creationTimestamp:payload:]
+ -[IASignalAnalyticsObject initWithChannel:signal:sessionIdString:payload:]
+ -[IASignalAnalyticsObject obtainPayloadValueSafelyForKey:expectedClass:]
+ -[IASignalAnalyticsObject payload]
+ -[IASignalAnalyticsObject setAnalyticsSessionIdString:]
+ -[IASignalAnalyticsObject setChannelName:]
+ -[IASignalAnalyticsObject setPayload:]
+ -[IASignalAnalyticsObject setSignalName:]
+ -[IASignalAnalyticsObject signalName]
+ -[IASignalAnalyticsObject(NSSecureCoding) encodeWithCoder:]
+ -[IASignalAnalyticsObject(NSSecureCoding) initWithCoder:]
+ -[IAStringDetails characters]
+ -[IAStringDetails emojiCharacters]
+ -[IAStringDetails punctuationCharacters]
+ -[IAStringDetails setCharacters:]
+ -[IAStringDetails setEmojiCharacters:]
+ -[IAStringDetails setPunctuationCharacters:]
+ -[IAStringDetails setTextIsTooLong:]
+ -[IAStringDetails textIsTooLong]
+ -[IATextInputActionsAnalytics .cxx_destruct]
+ -[IATextInputActionsAnalytics _didDeleteBackwardAction:]
+ -[IATextInputActionsAnalytics _didDeleteBackwardCount:withType:shouldOverrideInputActionCountToZero:withInputMode:forceNotMarkedText:]
+ -[IATextInputActionsAnalytics _didDeleteBackwardCount:withType:shouldOverrideInputActionCountToZero:withInputMode:forceNotMarkedText:].cold.1
+ -[IATextInputActionsAnalytics _didDeleteBackwardText:withType:shouldOverrideInputActionCountToZero:withInputMode:forceNotMarkedText:]
+ -[IATextInputActionsAnalytics _didDeleteBackwardText:withType:shouldOverrideInputActionCountToZero:withInputMode:forceNotMarkedText:].cold.1
+ -[IATextInputActionsAnalytics _didDeleteBackwardTextDetails:withType:shouldOverrideInputActionCountToZero:withInputMode:forceNotMarkedText:]
+ -[IATextInputActionsAnalytics _didDeleteBackwardTextDetails:withType:shouldOverrideInputActionCountToZero:withInputMode:forceNotMarkedText:].cold.1
+ -[IATextInputActionsAnalytics _didDeletionKeyPressOfKey:withType:]
+ -[IATextInputActionsAnalytics _didInsertTextAction:]
+ -[IATextInputActionsAnalytics _didInsertionKeyPressOfKey:withType:]
+ -[IATextInputActionsAnalytics _didReplacementForText:withText:allowNilText:allowEmptyText:allowNilReplacement:withSource:withType:withInputActionCount:]
+ -[IATextInputActionsAnalytics _didReplacementForText:withText:allowNilText:allowEmptyText:allowNilReplacement:withSource:withType:withInputActionCount:].cold.1
+ -[IATextInputActionsAnalytics _didReplacementForText:withText:allowNilText:allowEmptyText:allowNilReplacement:withSource:withType:withInputActionCount:].cold.2
+ -[IATextInputActionsAnalytics _didReplacementForText:withText:allowNilText:allowEmptyText:allowNilReplacement:withSource:withType:withInputActionCount:].cold.3
+ -[IATextInputActionsAnalytics _instanceOfActionClass:]
+ -[IATextInputActionsAnalytics _instanceOfActionClass:].cold.1
+ -[IATextInputActionsAnalytics analyticsDelegate]
+ -[IATextInputActionsAnalytics didAutocorrectReplacementForText:withText:]
+ -[IATextInputActionsAnalytics didAutocorrectReplacementForText:withText:].cold.1
+ -[IATextInputActionsAnalytics didAutocorrectTapOnCompletionReplacementForText:withText:]
+ -[IATextInputActionsAnalytics didAutocorrectTapOnCompletionReplacementForText:withText:].cold.1
+ -[IATextInputActionsAnalytics didCalloutBarReplacementForText:withText:]
+ -[IATextInputActionsAnalytics didCalloutBarReplacementForText:withText:].cold.1
+ -[IATextInputActionsAnalytics didCandidateBarAction]
+ -[IATextInputActionsAnalytics didCandidateBarReplacementForText:withText:]
+ -[IATextInputActionsAnalytics didCandidateBarReplacementForText:withText:].cold.1
+ -[IATextInputActionsAnalytics didChangeToSelection:relativeRangeBefore:]
+ -[IATextInputActionsAnalytics didCommitText:]
+ -[IATextInputActionsAnalytics didCommitText:].cold.1
+ -[IATextInputActionsAnalytics didCommitText:].cold.2
+ -[IATextInputActionsAnalytics didCompositionReplacementForText:withText:]
+ -[IATextInputActionsAnalytics didCompositionReplacementForText:withText:].cold.1
+ -[IATextInputActionsAnalytics didConversionForMarkedText:withText:]
+ -[IATextInputActionsAnalytics didConversionForMarkedText:withText:].cold.1
+ -[IATextInputActionsAnalytics didConversionForMarkedText:withText:].cold.2
+ -[IATextInputActionsAnalytics didConversionForMarkedText:withText:].cold.3
+ -[IATextInputActionsAnalytics didConversionForMarkedText:withText:].cold.4
+ -[IATextInputActionsAnalytics didCopy:]
+ -[IATextInputActionsAnalytics didCopy:].cold.1
+ -[IATextInputActionsAnalytics didCut:]
+ -[IATextInputActionsAnalytics didCut:].cold.1
+ -[IATextInputActionsAnalytics didDecompositionReplacementForText:withText:]
+ -[IATextInputActionsAnalytics didDecompositionReplacementForText:withText:].cold.1
+ -[IATextInputActionsAnalytics didDeleteBackwardCount:withType:]
+ -[IATextInputActionsAnalytics didDeleteBackwardText:]
+ -[IATextInputActionsAnalytics didDeleteBackwardText:].cold.1
+ -[IATextInputActionsAnalytics didDeleteBackwardText:withType:]
+ -[IATextInputActionsAnalytics didDeleteBackwardText:withType:].cold.1
+ -[IATextInputActionsAnalytics didDeleteBackwardText:withType:withInputMode:]
+ -[IATextInputActionsAnalytics didDeletionKeyPressOfKey:withType:]
+ -[IATextInputActionsAnalytics didDeletionKeyPressOfKey:withType:].cold.1
+ -[IATextInputActionsAnalytics didDeletionKeyPress]
+ -[IATextInputActionsAnalytics didDeletionKeyPress].cold.1
+ -[IATextInputActionsAnalytics didDictationBegin:usesMultiModalDictation:]
+ -[IATextInputActionsAnalytics didDictationBegin:usesMultiModalDictation:].cold.1
+ -[IATextInputActionsAnalytics didDictationEnd]
+ -[IATextInputActionsAnalytics didDictationEnd].cold.1
+ -[IATextInputActionsAnalytics didGlomojiTap:newInputMode:]
+ -[IATextInputActionsAnalytics didGlomojiTap:newInputMode:].cold.1
+ -[IATextInputActionsAnalytics didGlomojiTap:originalInputMode:newInputMode:]
+ -[IATextInputActionsAnalytics didGlomojiTap:originalInputMode:newInputMode:].cold.1
+ -[IATextInputActionsAnalytics didInlineCompletionReplacementForText:withText:]
+ -[IATextInputActionsAnalytics didInlineCompletionReplacementForText:withText:].cold.1
+ -[IATextInputActionsAnalytics didInlineCompletionTapOnCompletionReplacementForText:withText:]
+ -[IATextInputActionsAnalytics didInlineCompletionTapOnCompletionReplacementForText:withText:].cold.1
+ -[IATextInputActionsAnalytics didInsertText:withType:]
+ -[IATextInputActionsAnalytics didInsertText:withType:relativeRangeBefore:withNumAlternatives:selectedTextBefore:withInputMode:]
+ -[IATextInputActionsAnalytics didInsertText:withType:relativeRangeBefore:withNumAlternatives:selectedTextBefore:withInputMode:].cold.1
+ -[IATextInputActionsAnalytics didInsertText:withType:selectedTextBefore:]
+ -[IATextInputActionsAnalytics didInsertText:withType:selectedTextBefore:withInputMode:]
+ -[IATextInputActionsAnalytics didInsertText:withType:withInputMode:]
+ -[IATextInputActionsAnalytics didInsertionKeyPressOfKey:withType:]
+ -[IATextInputActionsAnalytics didInsertionKeyPressOfKey:withType:].cold.1
+ -[IATextInputActionsAnalytics didInsertionKeyPress]
+ -[IATextInputActionsAnalytics didInsertionKeyPress].cold.1
+ -[IATextInputActionsAnalytics didKBMenuAppear:]
+ -[IATextInputActionsAnalytics didKBMenuAppear:].cold.1
+ -[IATextInputActionsAnalytics didKBMenuAppear:originalInputMode:]
+ -[IATextInputActionsAnalytics didKBMenuAppear:originalInputMode:].cold.1
+ -[IATextInputActionsAnalytics didKBMenuDismiss:]
+ -[IATextInputActionsAnalytics didKBMenuDismiss:].cold.1
+ -[IATextInputActionsAnalytics didKBMenuInteraction:selectedAction:newInputMode:]
+ -[IATextInputActionsAnalytics didKBMenuInteraction:selectedAction:newInputMode:].cold.1
+ -[IATextInputActionsAnalytics didKeyboardDockItemButtonPress:buttonType:buttonSize:touchDown:touchUp:touchDuration:inputSource:inputType:uiInterfaceOrientation:]
+ -[IATextInputActionsAnalytics didOther]
+ -[IATextInputActionsAnalytics didOther].cold.1
+ -[IATextInputActionsAnalytics didPaste:]
+ -[IATextInputActionsAnalytics didPaste:].cold.1
+ -[IATextInputActionsAnalytics didRedo]
+ -[IATextInputActionsAnalytics didRedo].cold.1
+ -[IATextInputActionsAnalytics didReplaceWithCandidate:]
+ -[IATextInputActionsAnalytics didReplaceWithCandidate:].cold.1
+ -[IATextInputActionsAnalytics didRevisionBubbleReplacementForText:withText:]
+ -[IATextInputActionsAnalytics didRevisionBubbleReplacementForText:withText:].cold.1
+ -[IATextInputActionsAnalytics didRevisionBubbleTap]
+ -[IATextInputActionsAnalytics didRevisionBubbleTap].cold.1
+ -[IATextInputActionsAnalytics didSessionBegin]
+ -[IATextInputActionsAnalytics didSessionBegin].cold.1
+ -[IATextInputActionsAnalytics didSessionEnd]
+ -[IATextInputActionsAnalytics didSessionEnd].cold.1
+ -[IATextInputActionsAnalytics didUndo]
+ -[IATextInputActionsAnalytics didUndo].cold.1
+ -[IATextInputActionsAnalytics flushAndSetLastAction:]
+ -[IATextInputActionsAnalytics initWithAnalyticsDelegate:]
+ -[IATextInputActionsAnalytics initWithAnalyticsMetadataObserver:]
+ -[IATextInputActionsAnalytics mergeOrConsumeAction:]
+ -[IATextInputActionsAnalytics mergeOrConsumeAction:].cold.1
+ -[IATextInputActionsAnalytics populateActionInputMode:withInputMode:]
+ -[IATextInputActionsAnalytics queue]
+ -[IATextInputActionsAnalytics sessionIdentifier]
+ -[IATextInputActionsAnalytics setAnalyticsDelegate:]
+ -[IATextInputActionsAnalytics setQueue:]
+ -[IATextInputActionsAnalytics setSessionIdentifier:]
+ -[IATextInputActionsAnalytics(TestingSupport) dispatchToAnalyticsQueue:]
+ -[IATextInputActionsAnalytics(TestingSupport) initWithAnalyticsMetadataObserver:withEventHandler:]
+ -[IATextInputActionsAnalytics(TestingSupport) initWithAnalyticsMetadataObserver:withServiceName:]
+ -[IATextInputActionsAnalytics(TestingSupport) lastAction]
+ -[IATextInputActionsAnalytics(TestingSupport) server]
+ -[IATextInputActionsInputMode .cxx_destruct]
+ -[IATextInputActionsInputMode copyWithZone:]
+ -[IATextInputActionsInputMode description]
+ -[IATextInputActionsInputMode encodeWithCoder:]
+ -[IATextInputActionsInputMode initFromDictionary:]
+ -[IATextInputActionsInputMode initWithCoder:]
+ -[IATextInputActionsInputMode initWithLanguage:region:keyboardVariant:keyboardLayout:keyboardType:inputModeIdentifier:]
+ -[IATextInputActionsInputMode inputModeIdentifier]
+ -[IATextInputActionsInputMode inputModeUniqueString]
+ -[IATextInputActionsInputMode isEmpty]
+ -[IATextInputActionsInputMode isEqual:]
+ -[IATextInputActionsInputMode keyboardLayout]
+ -[IATextInputActionsInputMode keyboardType]
+ -[IATextInputActionsInputMode keyboardVariant]
+ -[IATextInputActionsInputMode language]
+ -[IATextInputActionsInputMode region]
+ -[IATextInputActionsInputMode setInputModeIdentifier:]
+ -[IATextInputActionsInputMode setKeyboardLayout:]
+ -[IATextInputActionsInputMode setKeyboardType:]
+ -[IATextInputActionsInputMode setKeyboardVariant:]
+ -[IATextInputActionsInputMode setLanguage:]
+ -[IATextInputActionsInputMode setRegion:]
+ -[IATextInputActionsInputMode toDictionary]
+ -[IATextInputActionsServer .cxx_destruct]
+ -[IATextInputActionsServer analyzer]
+ -[IATextInputActionsServer consumeAction:]
+ -[IATextInputActionsServer dispatchEventToCoreAnalytics]
+ -[IATextInputActionsServer enumerateTextInputActionsAnalytics]
+ -[IATextInputActionsServer initWithQueue:eventHandler:]
+ -[IATextInputActionsServer q_flushRecentActions]
+ -[IATextInputActionsServer queue]
+ -[IATextInputActionsServer recentActions]
+ -[IATextInputActionsServer setAnalyzer:]
+ -[IATextInputActionsServer setKeyboardTrialParameters:]
+ -[IATextInputActionsServer setQueue:]
+ -[IATextInputActionsServer setRecentActions:]
+ -[IATextInputActionsServer setTestingDelegate:]
+ -[IATextInputActionsServer testingDelegate]
+ -[IATextInputActionsSessionAction .cxx_destruct]
+ -[IATextInputActionsSessionAction asBegan]
+ -[IATextInputActionsSessionAction asCommitText]
+ -[IATextInputActionsSessionAction asCopy]
+ -[IATextInputActionsSessionAction asCut]
+ -[IATextInputActionsSessionAction asDeletion]
+ -[IATextInputActionsSessionAction asDictationBegan]
+ -[IATextInputActionsSessionAction asDictationEnded]
+ -[IATextInputActionsSessionAction asEnd]
+ -[IATextInputActionsSessionAction asGlomojiTap]
+ -[IATextInputActionsSessionAction asInsertion]
+ -[IATextInputActionsSessionAction asKBMenuAppear]
+ -[IATextInputActionsSessionAction asKBMenuDismiss]
+ -[IATextInputActionsSessionAction asKBMenuInteraction]
+ -[IATextInputActionsSessionAction asKeyboardDockItemButtonPress]
+ -[IATextInputActionsSessionAction asPaste]
+ -[IATextInputActionsSessionAction asRedo]
+ -[IATextInputActionsSessionAction asReplaceText]
+ -[IATextInputActionsSessionAction asReplaceWithCandidate]
+ -[IATextInputActionsSessionAction asSelection]
+ -[IATextInputActionsSessionAction asUndo]
+ -[IATextInputActionsSessionAction changedContent]
+ -[IATextInputActionsSessionAction clientSideSessionErrors]
+ -[IATextInputActionsSessionAction description]
+ -[IATextInputActionsSessionAction flagOptions]
+ -[IATextInputActionsSessionAction inputActionCountFromMergedActions]
+ -[IATextInputActionsSessionAction inputActionCount]
+ -[IATextInputActionsSessionAction inputMode]
+ -[IATextInputActionsSessionAction insertedEmojiCount]
+ -[IATextInputActionsSessionAction insertedPunctuationCount]
+ -[IATextInputActionsSessionAction insertedTextLength]
+ -[IATextInputActionsSessionAction isCapableOfTextInsertion]
+ -[IATextInputActionsSessionAction isMergeableWith:]
+ -[IATextInputActionsSessionAction largestSingleDeletionLength]
+ -[IATextInputActionsSessionAction largestSingleInsertionLength]
+ -[IATextInputActionsSessionAction mergeActionIfPossible:]
+ -[IATextInputActionsSessionAction netCharacterCount]
+ -[IATextInputActionsSessionAction processBundleId]
+ -[IATextInputActionsSessionAction relativeRangeBefore]
+ -[IATextInputActionsSessionAction removedEmojiCount]
+ -[IATextInputActionsSessionAction removedPunctuationCount]
+ -[IATextInputActionsSessionAction removedTextLength]
+ -[IATextInputActionsSessionAction setClientSideSessionErrors:]
+ -[IATextInputActionsSessionAction setFlagOptions:]
+ -[IATextInputActionsSessionAction setInputActionCountFromMergedActions:]
+ -[IATextInputActionsSessionAction setInputMode:]
+ -[IATextInputActionsSessionAction setInsertedEmojiCount:]
+ -[IATextInputActionsSessionAction setInsertedEmojiCount:].cold.1
+ -[IATextInputActionsSessionAction setInsertedPunctuationCount:]
+ -[IATextInputActionsSessionAction setInsertedPunctuationCount:].cold.1
+ -[IATextInputActionsSessionAction setInsertedTextLength:]
+ -[IATextInputActionsSessionAction setInsertedTextLength:].cold.1
+ -[IATextInputActionsSessionAction setInsertedTextLengthWithoutTracking:]
+ -[IATextInputActionsSessionAction setInsertedTextLengthWithoutTracking:].cold.1
+ -[IATextInputActionsSessionAction setLargestSingleDeletionLength:]
+ -[IATextInputActionsSessionAction setLargestSingleInsertionLength:]
+ -[IATextInputActionsSessionAction setProcessBundleId:]
+ -[IATextInputActionsSessionAction setRelativeRangeBefore:]
+ -[IATextInputActionsSessionAction setRemovedEmojiCount:]
+ -[IATextInputActionsSessionAction setRemovedEmojiCount:].cold.1
+ -[IATextInputActionsSessionAction setRemovedPunctuationCount:]
+ -[IATextInputActionsSessionAction setRemovedPunctuationCount:].cold.1
+ -[IATextInputActionsSessionAction setRemovedTextLength:]
+ -[IATextInputActionsSessionAction setRemovedTextLength:].cold.1
+ -[IATextInputActionsSessionAction setRemovedTextLengthWithoutTracking:]
+ -[IATextInputActionsSessionAction setRemovedTextLengthWithoutTracking:].cold.1
+ -[IATextInputActionsSessionAction setSource:]
+ -[IATextInputActionsSessionAction setTextInputActionsType:]
+ -[IATextInputActionsSessionAction source]
+ -[IATextInputActionsSessionAction textInputActionsType]
+ -[IATextInputActionsSessionAction(ConvertToDictionary) initFromDictionary:]
+ -[IATextInputActionsSessionAction(ConvertToDictionary) toDictionary]
+ -[IATextInputActionsSessionAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionActionInformation .cxx_destruct]
+ -[IATextInputActionsSessionActionInformation sessionActionsString]
+ -[IATextInputActionsSessionActionInformation sessionHasDictation]
+ -[IATextInputActionsSessionActionInformation sessionHasOnlyPrimaryInput]
+ -[IATextInputActionsSessionActionInformation setSessionActionsString:]
+ -[IATextInputActionsSessionActionInformation setSessionHasDictation:]
+ -[IATextInputActionsSessionActionInformation setSessionHasOnlyPrimaryInput:]
+ -[IATextInputActionsSessionBeganAction inputActionCount]
+ -[IATextInputActionsSessionCommitTextAction changedContent]
+ -[IATextInputActionsSessionCommitTextAction inputActionCount]
+ -[IATextInputActionsSessionCommitTextAction textInputActionsType]
+ -[IATextInputActionsSessionCopyAction changedContent]
+ -[IATextInputActionsSessionCutAction changedContent]
+ -[IATextInputActionsSessionDeletionAction changedContent]
+ -[IATextInputActionsSessionDeletionAction description]
+ -[IATextInputActionsSessionDeletionAction inputActionCount]
+ -[IATextInputActionsSessionDeletionAction mergeActionIfPossible:]
+ -[IATextInputActionsSessionDeletionAction options]
+ -[IATextInputActionsSessionDeletionAction setOptions:]
+ -[IATextInputActionsSessionDeletionAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionDeletionAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionDeletionAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionDeletionAction(NSSecureCoding) toDictionary]
+ -[IATextInputActionsSessionDictationBeganAction description]
+ -[IATextInputActionsSessionDictationBeganAction dictationBeganCount]
+ -[IATextInputActionsSessionDictationBeganAction inputActionCount]
+ -[IATextInputActionsSessionDictationBeganAction mergeActionIfPossible:]
+ -[IATextInputActionsSessionDictationBeganAction modelessUsedAtLeastOnceCount]
+ -[IATextInputActionsSessionDictationBeganAction multiModalDictationBeganCount]
+ -[IATextInputActionsSessionDictationBeganAction setDictationBeganCount:]
+ -[IATextInputActionsSessionDictationBeganAction setModelessUsedAtLeastOnceCount:]
+ -[IATextInputActionsSessionDictationBeganAction setMultiModalDictationBeganCount:]
+ -[IATextInputActionsSessionDictationBeganAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionDictationBeganAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionDictationBeganAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionDictationBeganAction(NSSecureCoding) toDictionary]
+ -[IATextInputActionsSessionDictationEndedAction inputActionCount]
+ -[IATextInputActionsSessionEndAction .cxx_destruct]
+ -[IATextInputActionsSessionEndAction description]
+ -[IATextInputActionsSessionEndAction inputActionCount]
+ -[IATextInputActionsSessionEndAction keyboardTrialParameters]
+ -[IATextInputActionsSessionEndAction setKeyboardTrialParameters:]
+ -[IATextInputActionsSessionEndAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionEndAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionEndAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionEndAction(NSSecureCoding) toDictionary]
+ -[IATextInputActionsSessionGlomojiTapAction .cxx_destruct]
+ -[IATextInputActionsSessionGlomojiTapAction glomojiType]
+ -[IATextInputActionsSessionGlomojiTapAction init]
+ -[IATextInputActionsSessionGlomojiTapAction inputActionCount]
+ -[IATextInputActionsSessionGlomojiTapAction mergeActionIfPossible:]
+ -[IATextInputActionsSessionGlomojiTapAction mergedActionsCount]
+ -[IATextInputActionsSessionGlomojiTapAction originalInputMode]
+ -[IATextInputActionsSessionGlomojiTapAction setGlomojiType:]
+ -[IATextInputActionsSessionGlomojiTapAction setMergedActionsCount:]
+ -[IATextInputActionsSessionGlomojiTapAction setOriginalInputMode:]
+ -[IATextInputActionsSessionGlomojiTapAction setUpdatedInputMode:]
+ -[IATextInputActionsSessionGlomojiTapAction updatedInputMode]
+ -[IATextInputActionsSessionGlomojiTapAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionGlomojiTapAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionGlomojiTapAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionGlomojiTapAction(NSSecureCoding) toDictionary]
+ -[IATextInputActionsSessionInsertionAction changedContent]
+ -[IATextInputActionsSessionInsertionAction description]
+ -[IATextInputActionsSessionInsertionAction inputActionCount]
+ -[IATextInputActionsSessionInsertionAction isCapableOfTextInsertion]
+ -[IATextInputActionsSessionInsertionAction mergeActionIfPossible:]
+ -[IATextInputActionsSessionInsertionAction options]
+ -[IATextInputActionsSessionInsertionAction setOptions:]
+ -[IATextInputActionsSessionInsertionAction setWithAlternativesCount:]
+ -[IATextInputActionsSessionInsertionAction withAlternativesCount]
+ -[IATextInputActionsSessionInsertionAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionInsertionAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionInsertionAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionInsertionAction(NSSecureCoding) toDictionary]
+ -[IATextInputActionsSessionKBMenuAppearAction .cxx_destruct]
+ -[IATextInputActionsSessionKBMenuAppearAction glomojiType]
+ -[IATextInputActionsSessionKBMenuAppearAction inputActionCount]
+ -[IATextInputActionsSessionKBMenuAppearAction originalInputMode]
+ -[IATextInputActionsSessionKBMenuAppearAction setGlomojiType:]
+ -[IATextInputActionsSessionKBMenuAppearAction setOriginalInputMode:]
+ -[IATextInputActionsSessionKBMenuAppearAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionKBMenuAppearAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionKBMenuAppearAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionKBMenuAppearAction(NSSecureCoding) toDictionary]
+ -[IATextInputActionsSessionKBMenuDismissAction KBMenuDismissSource]
+ -[IATextInputActionsSessionKBMenuDismissAction inputActionCount]
+ -[IATextInputActionsSessionKBMenuDismissAction setKBMenuDismissSource:]
+ -[IATextInputActionsSessionKBMenuDismissAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionKBMenuDismissAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionKBMenuDismissAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionKBMenuDismissAction(NSSecureCoding) toDictionary]
+ -[IATextInputActionsSessionKBMenuInteractionAction .cxx_destruct]
+ -[IATextInputActionsSessionKBMenuInteractionAction KBMenuInteractionSource]
+ -[IATextInputActionsSessionKBMenuInteractionAction KBMenuSelectedAction]
+ -[IATextInputActionsSessionKBMenuInteractionAction inputActionCount]
+ -[IATextInputActionsSessionKBMenuInteractionAction setKBMenuInteractionSource:]
+ -[IATextInputActionsSessionKBMenuInteractionAction setKBMenuSelectedAction:]
+ -[IATextInputActionsSessionKBMenuInteractionAction setUpdatedInputMode:]
+ -[IATextInputActionsSessionKBMenuInteractionAction updatedInputMode]
+ -[IATextInputActionsSessionKBMenuInteractionAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionKBMenuInteractionAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionKBMenuInteractionAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionKBMenuInteractionAction(NSSecureCoding) toDictionary]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction buttonPressResult]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction buttonSize]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction buttonType]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction description]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction inputActionCount]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction setButtonPressResult:]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction setButtonSize:]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction setButtonType:]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction setTouchDownPoint:]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction setTouchDuration:]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction setTouchUpPoint:]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction setUiOrientation:]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction touchDownPoint]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction touchDuration]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction touchUpPoint]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction uiOrientation]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionKeyboardDockItemButtonPressAction(NSSecureCoding) toDictionary]
+ -[IATextInputActionsSessionPasteAction changedContent]
+ -[IATextInputActionsSessionPasteAction isCapableOfTextInsertion]
+ -[IATextInputActionsSessionRedoAction changedContent]
+ -[IATextInputActionsSessionRedoAction isCapableOfTextInsertion]
+ -[IATextInputActionsSessionReplaceTextAction changedContent]
+ -[IATextInputActionsSessionReplaceTextAction isCapableOfTextInsertion]
+ -[IATextInputActionsSessionReplaceTextAction mergeActionIfPossible:]
+ -[IATextInputActionsSessionReplaceTextAction options]
+ -[IATextInputActionsSessionReplaceTextAction setOptions:]
+ -[IATextInputActionsSessionReplaceTextAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionReplaceTextAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionReplaceTextAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionReplaceTextAction(NSSecureCoding) toDictionary]
+ -[IATextInputActionsSessionReplaceWithCandidateAction changedContent]
+ -[IATextInputActionsSessionReplaceWithCandidateAction isCapableOfTextInsertion]
+ -[IATextInputActionsSessionReplaceWithCandidateAction replaceWithCandidateType]
+ -[IATextInputActionsSessionReplaceWithCandidateAction setReplaceWithCandidateType:]
+ -[IATextInputActionsSessionReplaceWithCandidateAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionReplaceWithCandidateAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionReplaceWithCandidateAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionReplaceWithCandidateAction(NSSecureCoding) toDictionary]
+ -[IATextInputActionsSessionSelectionAction description]
+ -[IATextInputActionsSessionSelectionAction mergeActionIfPossible:]
+ -[IATextInputActionsSessionSelectionAction rangeAfter]
+ -[IATextInputActionsSessionSelectionAction setRangeAfter:]
+ -[IATextInputActionsSessionSelectionAction textInputActionsType]
+ -[IATextInputActionsSessionSelectionAction(NSSecureCoding) encodeWithCoder:]
+ -[IATextInputActionsSessionSelectionAction(NSSecureCoding) initFromDictionary:]
+ -[IATextInputActionsSessionSelectionAction(NSSecureCoding) initWithCoder:]
+ -[IATextInputActionsSessionSelectionAction(NSSecureCoding) toDictionary]
+ -[IATextInputActionsSessionUndoAction changedContent]
+ -[IATextInputActionsSessionUndoAction isCapableOfTextInsertion]
+ -[IATextInputUserPreferenceAnalytics initWithEventHandler:]
+ -[IATextInputUserPreferenceAnalytics init]
+ -[IATextInputUserPreferenceAnalytics reportStateForUserPreference:]
+ -[IATextInputUserPreferenceAnalytics reportStateForUserPreference:].cold.1
+ -[IATextInputUserPreferenceAnalytics reportStateForUserPreferences:]
+ -[IATextInputUserPreferenceAnalytics reportStateForUserPreferences:].cold.1
+ -[IAXPCClient .cxx_destruct]
+ -[IAXPCClient dealloc]
+ -[IAXPCClient initWithServiceName:]
+ -[IAXPCClient init]
+ -[IAXPCClient invalidateConnection]
+ -[IAXPCClient logMessage:]
+ -[IAXPCClient logMessage:].cold.1
+ -[IAXPCClient server]
+ -[IAXPCClient server].cold.1
+ -[IAXPCObject .cxx_destruct]
+ -[IAXPCObject appBundleId]
+ -[IAXPCObject appSessionId]
+ -[IAXPCObject creationTimestampWithFallback]
+ -[IAXPCObject creationTimestamp]
+ -[IAXPCObject description]
+ -[IAXPCObject encodeWithCoder:]
+ -[IAXPCObject initWithCoder:]
+ -[IAXPCObject initWithTimestamp:]
+ -[IAXPCObject init]
+ -[IAXPCObject isEqual:]
+ -[IAXPCObject setAppBundleId:]
+ -[IAXPCObject setAppSessionId:]
+ -[IAXPCObject setCreationTimestamp:]
+ -[IAXPCObject setTextInputSessionId:]
+ -[IAXPCObject setTimestamp:]
+ -[IAXPCObject textInputSessionId]
+ -[IAXPCObject timestamp]
+ -[IAXPCProtocolObject didAction:]
+ -[IAXPCProtocolObject didAction:].cold.1
+ -[IAXPCProtocolObject didSessionBeginWithSessionMetadata:]
+ -[IAXPCProtocolObject didSessionBeginWithSessionMetadata:].cold.1
+ -[IAXPCProtocolObject didSessionEndWithSessionMetadata:]
+ -[IAXPCProtocolObject didSessionEndWithSessionMetadata:].cold.1
+ -[IAXPCProtocolObject getDateWithReply:]
+ -[IAXPCProtocolObject getDateWithReply:].cold.1
+ -[IAXPCProtocolObject logMessage:]
+ -[IAXPCProtocolObject logMessage:].cold.1
+ -[IAXPCProtocolObject reportStatus]
+ -[IAXPCProtocolObject reportStatus].cold.1
+ -[NSMutableDictionary(SetObjectIfNotNil) setObjectIfNotNil:forKey:]
+ <redacted>
+ GCC_except_table0
+ GCC_except_table1
+ GCC_except_table10
+ GCC_except_table19
+ GCC_except_table2
+ GCC_except_table27
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table4
+ GCC_except_table5
+ GCC_except_table7
+ GCC_except_table8
+ _$s14InputAnalytics13createSubject33_EDC78993CADAEE7778F038DFDC42D66ELL15originalContent09generatedK013featureDomain9modelInfo15FeedbackService14FBKSEvaluationC0D0OSS_SSAH15FBKSInteractionC07FeatureN0OSSSgtF
+ _$s15FeedbackService14FBKSEvaluationC6ActionO10thumbsDownyA2EmFWC
+ _$s15FeedbackService14FBKSEvaluationC6ActionO13reportConcernyA2EmFWC
+ _$s15FeedbackService14FBKSEvaluationC6ActionO8thumbsUpyA2EmFWC
+ _$s15FeedbackService14FBKSEvaluationC6ActionOMa
+ _$s15FeedbackService14FBKSEvaluationC7SubjectO11interactionyAeA15FBKSInteractionCcAEmFWC
+ _$s15FeedbackService14FBKSEvaluationC7SubjectO15_remoteEvaluate6action04showA4FormyAC6ActionO_SbtYaKF
+ _$s15FeedbackService14FBKSEvaluationC7SubjectO15_remoteEvaluate6action04showA4FormyAC6ActionO_SbtYaKFTu
+ _$s15FeedbackService14FBKSEvaluationC7SubjectO9presentedyyYaKF
+ _$s15FeedbackService14FBKSEvaluationC7SubjectO9presentedyyYaKFTu
+ _$s15FeedbackService14FBKSEvaluationC7SubjectOMa
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainO12smartRepliesyA2EmFWC
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainO12writingToolsyA2EmFWC
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainOMa
+ _$s15FeedbackService15FBKSInteractionC13featureDomain8bundleID16prefillQuestions24originalAnnotatedContent09generatedkL005extraL012modelVersion11diagnostics16auxiliaryMetrics14isHighPriorityA2C07FeatureE0O_SSSgSDyAA8FBKSFormC8QuestionOSaySSGGSgAC0kL0VSgAZSayAYGA2PSDySSSiGSgSbtcfc
+ _$s15FeedbackService15FBKSInteractionC16AnnotatedContentV7payload11displayName11description04fileH05group8iconType14additionalInfoAeC0E0O_S4SSgAE04IconM0OSgSDyS2SGSgtcfC
+ _$s15FeedbackService15FBKSInteractionC16AnnotatedContentV8IconTypeOMa
+ _$s15FeedbackService15FBKSInteractionC16AnnotatedContentV8IconTypeOMn
+ _$s15FeedbackService15FBKSInteractionC16AnnotatedContentV8IconTypeOSgMR
+ _$s15FeedbackService15FBKSInteractionC16AnnotatedContentV8IconTypeOSgMd
+ _$s15FeedbackService15FBKSInteractionC16AnnotatedContentVMa
+ _$s15FeedbackService15FBKSInteractionC16AnnotatedContentVMn
+ _$s15FeedbackService15FBKSInteractionC16AnnotatedContentVSgMR
+ _$s15FeedbackService15FBKSInteractionC16AnnotatedContentVSgMd
+ _$s15FeedbackService15FBKSInteractionC16AnnotatedContentVSgWOb
+ _$s15FeedbackService15FBKSInteractionC7ContentO4textyAESScAEmFWC
+ _$s15FeedbackService15FBKSInteractionC7ContentOMa
+ _$s15FeedbackService15FBKSInteractionCMa
+ _$s2os32getNullTerminatedUTF8PointerImpl_21storingStringOwnersInSVSS_SpyypGSgztF
+ _$s2os6LoggerV9logObjectSo03OS_a1_C0Cvg
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _$s2os6LoggerVMa
+ _$sBi64_WV
+ _$sIeAgH_ytIeAgHr_TR
+ _$sIeAgH_ytIeAgHr_TRTA
+ _$sIeAgH_ytIeAgHr_TRTA.39
+ _$sIeAgH_ytIeAgHr_TRTA.39TQ0_
+ _$sIeAgH_ytIeAgHr_TRTA.39Tu
+ _$sIeAgH_ytIeAgHr_TRTATQ0_
+ _$sIeAgH_ytIeAgHr_TRTATu
+ _$sIeAgH_ytIeAgHr_TRTQ0_
+ _$sIeAgH_ytIeAgHr_TRTu
+ _$sIeghH_IeAgH_TR
+ _$sIeghH_IeAgH_TRTA
+ _$sIeghH_IeAgH_TRTA.34
+ _$sIeghH_IeAgH_TRTA.34TQ0_
+ _$sIeghH_IeAgH_TRTA.34Tu
+ _$sIeghH_IeAgH_TRTATQ0_
+ _$sIeghH_IeAgH_TRTATu
+ _$sIeghH_IeAgH_TRTQ0_
+ _$sIeghH_IeAgH_TRTu
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSS10describingSSx_tclufC
+ _$sSS11utf8CStrings15ContiguousArrayVys4Int8VGvg
+ _$sSS8UTF8ViewV13_foreignCountSiyF
+ _$sSa6append10contentsOfyqd__n_t7ElementQyd__RszSTRd__lFs5UInt8V_SayAFGTgq5
+ _$sScA15unownedExecutorScevgTj
+ _$sScP8rawValues5UInt8Vvg
+ _$sScPMa
+ _$sScPSgMR
+ _$sScPSgMd
+ _$sScPSgWOcTm
+ _$sScTss5NeverORs_rlE4name8priority9operationScTyxABGSSSg_ScPSgxyYaYAcntcfCyt_Tt2gq5
+ _$sSo13os_log_type_ta0A0E4infoABvgZ
+ _$sSo13os_log_type_ta0A0E5errorABvgZ
+ _$sSo22IAFBKSEvaluationActionVMB
+ _$sSo22IAFBKSEvaluationActionVML
+ _$sSo22IAFBKSEvaluationActionVMa
+ _$sSo22IAFBKSEvaluationActionVMf
+ _$sSo22IAFBKSEvaluationActionVMn
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE13featureDomain6action15originalContent09generatedK09modelInfoABSo024IAFBKSInteractionFeatureH0V_So22IAFBKSEvaluationActionVSSSgA2MtcfC
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE13featureDomain6action15originalContent09generatedK09modelInfoABSo024IAFBKSInteractionFeatureH0V_So22IAFBKSEvaluationActionVSSSgA2Mtcfc
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE13featureDomain6action15originalContent09generatedK09modelInfoABSo024IAFBKSInteractionFeatureH0V_So22IAFBKSEvaluationActionVSSSgA2MtcfcTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE13featureDomainSo024IAFBKSInteractionFeatureH0Vvg
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE13featureDomainSo024IAFBKSInteractionFeatureH0VvgTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE13featureDomainSo024IAFBKSInteractionFeatureH0VvpABTK
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE13featureDomainSo024IAFBKSInteractionFeatureH0VvpABTk
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE13featureDomainSo024IAFBKSInteractionFeatureH0VvpMV
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE13featureDomainSo024IAFBKSInteractionFeatureH0VvpWvd
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE13featureDomainSo024IAFBKSInteractionFeatureH0Vvs
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE13featureDomainSo024IAFBKSInteractionFeatureH0VvsTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaF
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaFTQ1_
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaFTY0_
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaFTY2_
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaFTY3_
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaFTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaFTu
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaFyyYacfU_To
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaFyyYacfU_ToTA
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaFyyYacfU_ToTATQ0_
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaFyyYacfU_ToTATu
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaFyyYacfU_ToTQ0_
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE14launchFeedbackyyYaFyyYacfU_ToTu
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15originalContentSSvg
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15originalContentSSvgTm
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15originalContentSSvgTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15originalContentSSvgToTm
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15originalContentSSvpABTK
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15originalContentSSvpABTk
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15originalContentSSvpMV
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15originalContentSSvpWvd
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15originalContentSSvs
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15originalContentSSvsTm
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15originalContentSSvsTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15originalContentSSvsToTm
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaF
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaFTQ1_
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaFTY0_
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaFTY2_
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaFTY3_
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaFTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaFTu
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaFyyYacfU_To
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaFyyYacfU_ToTA
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaFyyYacfU_ToTATQ0_
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaFyyYacfU_ToTATu
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaFyyYacfU_ToTQ0_
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE15reportPresentedyyYaFyyYacfU_ToTu
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE16generatedContentSSvg
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE16generatedContentSSvgTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE16generatedContentSSvpABTK
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE16generatedContentSSvpABTk
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE16generatedContentSSvpMV
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE16generatedContentSSvpWvd
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE16generatedContentSSvs
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE16generatedContentSSvsTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE6actionSo22IAFBKSEvaluationActionVvg
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE6actionSo22IAFBKSEvaluationActionVvgTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE6actionSo22IAFBKSEvaluationActionVvpABTK
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE6actionSo22IAFBKSEvaluationActionVvpABTk
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE6actionSo22IAFBKSEvaluationActionVvpMV
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE6actionSo22IAFBKSEvaluationActionVvpWvd
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE6actionSo22IAFBKSEvaluationActionVvs
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE6actionSo22IAFBKSEvaluationActionVvsTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE6logger33_EDC78993CADAEE7778F038DFDC42D66ELL2os6LoggerVvpZ
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE6logger33_EDC78993CADAEE7778F038DFDC42D66ELL_WZ
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE6logger33_EDC78993CADAEE7778F038DFDC42D66ELL_Wz
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE9modelInfoSSSgvg
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE9modelInfoSSSgvgTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE9modelInfoSSSgvpABTK
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE9modelInfoSSSgvpABTk
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE9modelInfoSSSgvpMV
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE9modelInfoSSSgvpWvd
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE9modelInfoSSSgvs
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsE9modelInfoSSSgvsTo
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsEABycfC
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsEABycfc
+ _$sSo28IAFeedbackServiceSwiftBridgeC14InputAnalyticsEABycfcTo
+ _$sSo28IAFeedbackServiceSwiftBridgeCML
+ _$sSo28IAFeedbackServiceSwiftBridgeCMa
+ _$sSo28IAFeedbackServiceSwiftBridgeCfETo
+ _$sSo30IAFBKSInteractionFeatureDomainVMB
+ _$sSo30IAFBKSInteractionFeatureDomainVML
+ _$sSo30IAFBKSInteractionFeatureDomainVMa
+ _$sSo30IAFBKSInteractionFeatureDomainVMaTm
+ _$sSo30IAFBKSInteractionFeatureDomainVMf
+ _$sSo30IAFBKSInteractionFeatureDomainVMn
+ _$sSo8NSObjectCSgMR
+ _$sSo8NSObjectCSgMd
+ _$sSo8NSObjectCSgWOhTm
+ _$sSoMXM
+ _$ss11_StringGutsV16_deconstructUTF87scratchyXlSg5owner_xSi6lengthSb11usesScratchSb15allocatedMemorytSwSg_ts8_PointerRzlFSV_Tgq5
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss11_StringGutsV23_allocateForDeconstructyXl5owner_SVSi6lengthtyF
+ _$ss11_StringGutsV23_allocateForDeconstructyXl5owner_SVSi6lengthtyFTv_r
+ _$ss11_StringGutsVN
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFs5UInt8V_Tgq5
+ _$ss13_StringObjectV10sharedUTF8SRys5UInt8VGvg
+ _$ss20__StaticArrayStorageCN
+ _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tt1gq5
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss23_ContiguousArrayStorageCys5UInt8VGMR
+ _$ss23_ContiguousArrayStorageCys5UInt8VGMd
+ _$ss32_copyCollectionToContiguousArrayys0dE0Vy7ElementQzGxSlRzlFSS8UTF8ViewV_Tgq5
+ _$ss5UInt8VMn
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.21
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.21TQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TA.21Tu
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TATQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TATu
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5TQ0_
+ _$sxIeAgHr_xs5Error_pIegHrzo_s8SendableRzs5NeverORs_r0_lTRyt_Tgq5Tu
+ _$sypN
+ _$sypWOc
+ _$sytN
+ _IAChannelMissingKeyboard
+ _IADefaultsDataStoreLog
+ _IADefaultsDataStoreLog.__instance
+ _IADefaultsDataStoreLog.cold.1
+ _IADefaultsDataStoreLog.onceToken
+ _IAEventDispatcherLog
+ _IAEventDispatcherLog.__instance
+ _IAEventDispatcherLog.cold.1
+ _IAEventDispatcherLog.onceToken
+ _IAGlomojiLog
+ _IAGlomojiLog.__instance
+ _IAGlomojiLog.cold.1
+ _IAGlomojiLog.onceToken
+ _IAKeyboardDetectionLog
+ _IAKeyboardDetectionLog.__instance
+ _IAKeyboardDetectionLog.cold.1
+ _IAKeyboardDetectionLog.onceToken
+ _IAPayloadKeyImageGenerationAppInfo
+ _IAPayloadKeyMissingKeyboardInputMode
+ _IAPayloadKeyMissingKeyboardIsWebKitView
+ _IAPayloadKeyMissingKeyboardOrientation
+ _IAPayloadKeyMissingKeyboardSceneId
+ _IAPayloadValueMissingKeyboardOrientationLandscapeLeft
+ _IAPayloadValueMissingKeyboardOrientationLandscapeRight
+ _IAPayloadValueMissingKeyboardOrientationLandscapeUnknown
+ _IAPayloadValueMissingKeyboardOrientationPortrait
+ _IAPayloadValueMissingKeyboardOrientationPortraitUpsideDown
+ _IASAnalyzerErrorsLog
+ _IASAnalyzerErrorsLog.__instance
+ _IASAnalyzerErrorsLog.cold.1
+ _IASAnalyzerErrorsLog.onceToken
+ _IASErrorAsynchronousSignalInconsistency
+ _IASErrorGarbageCollected
+ _IASErrorInvalidLanguage
+ _IASErrorInvalidRegion
+ _IASTextInputActionsLog
+ _IASTextInputActionsLog.__instance
+ _IASTextInputActionsLog.cold.1
+ _IASTextInputActionsLog.onceToken
+ _IAServerStatsLog
+ _IAServerStatsLog.__instance
+ _IAServerStatsLog.cold.1
+ _IAServerStatsLog.onceToken
+ _IASignalAnalyticsLog
+ _IASignalAnalyticsLog.__instance
+ _IASignalAnalyticsLog.cold.1
+ _IASignalAnalyticsLog.onceToken
+ _IASignalMissingKeyboardAppBackgrounded
+ _IASignalMissingKeyboardAppForegrounded
+ _IASignalMissingKeyboardInputModeDidChange
+ _IASignalMissingKeyboardKeyboardDismissed
+ _IASignalMissingKeyboardKeyboardRequested
+ _IASignalMissingKeyboardOrientationWillChange
+ _IATextInputActionsAnalyticsEventFullName
+ _IATextInputActionsBundleIdKey
+ _IATextInputActionsErrorsKey
+ _IATextInputActionsInitialUsrRmCharsKey
+ _IATextInputActionsInitialUsrRmEmojisKey
+ _IATextInputActionsInputActionCountKey
+ _IATextInputActionsInternalProcessBundleIdKey
+ _IATextInputActionsIsEmojiSearchKey
+ _IATextInputActionsIsMarkedTextKey
+ _IATextInputActionsKeyboardConfigurationKey
+ _IATextInputActionsKeyboardLayoutKey
+ _IATextInputActionsKeyboardTypeKey
+ _IATextInputActionsKeyboardVariantKey
+ _IATextInputActionsLanguageKey
+ _IATextInputActionsLargestSessionDeletionKey
+ _IATextInputActionsLargestSessionInsertionKey
+ _IATextInputActionsLog
+ _IATextInputActionsLog.__instance
+ _IATextInputActionsLog.cold.1
+ _IATextInputActionsLog.onceToken
+ _IATextInputActionsNetCharactersKey
+ _IATextInputActionsNetEmojiCharactersKey
+ _IATextInputActionsRegionKey
+ _IATextInputActionsSessionActionsKey
+ _IATextInputActionsSessionHasDictationKey
+ _IATextInputActionsSessionHasPrimaryInputKey
+ _IATextInputActionsSessionIsModelessKey
+ _IATextInputActionsSessionNetCharsKey
+ _IATextInputActionsSessionStartedWithDeletionKey
+ _IATextInputActionsSourceKey
+ _IATextInputActionsTypeKey
+ _IATextInputActionsUserRemovedCharactersKey
+ _IATextInputActionsUserRemovedEmojiCharactersKey
+ _IATextInputUserPreferenceAnalyticsLog
+ _IATextInputUserPreferenceAnalyticsLog.__instance
+ _IATextInputUserPreferenceAnalyticsLog.cold.1
+ _IATextInputUserPreferenceAnalyticsLog.onceToken
+ _IAUtilityLog
+ _IAUtilityLog.__instance
+ _IAUtilityLog.cold.1
+ _IAUtilityLog.onceToken
+ _IAXPCClientLog
+ _IAXPCClientLog.__instance
+ _IAXPCClientLog.cold.1
+ _IAXPCClientLog.onceToken
+ _InputAnalyticsVersionNumber
+ _InputAnalyticsVersionString
+ _OBJC_CLASS_$_CTCategories
+ _OBJC_CLASS_$_IAKeyboardDetection
+ _OBJC_CLASS_$_IASAnalyzer
+ _OBJC_CLASS_$_IASAnalyzerErrors
+ _OBJC_CLASS_$_IASDailyGarbageCollectionAnalyzer
+ _OBJC_CLASS_$_IASDailyGarbageCollectionStateMachineAnalyzer
+ _OBJC_CLASS_$_IASTextInputActionsAnalyzer
+ _OBJC_CLASS_$_IASTextInputActionsAnalyzerEntry
+ _OBJC_CLASS_$_IASTextInputActionsErrorChecking
+ _OBJC_CLASS_$_IASTextInputActionsEvent
+ _OBJC_CLASS_$_IAStringDetails
+ _OBJC_CLASS_$_IATextInputActionsServer
+ _OBJC_CLASS_$_IATextInputActionsSessionActionInformation
+ _OBJC_CLASS_$_IAXPCSPIObject
+ _OBJC_IVAR_$_IADataStoreBoolean._isTrue
+ _OBJC_IVAR_$_IADataStoreCounter._count
+ _OBJC_IVAR_$_IADataStoreDaterange._bitfield
+ _OBJC_IVAR_$_IADataStoreDaterange._originDate
+ _OBJC_IVAR_$_IADataStoreDaterange._startDate
+ _OBJC_IVAR_$_IADataStoreObject._datastoreHandle
+ _OBJC_IVAR_$_IADataStoreObject._destroyed
+ _OBJC_IVAR_$_IADataStoreObject._lastModified
+ _OBJC_IVAR_$_IADataStoreObject._name
+ _OBJC_IVAR_$_IADataStoreObject._version
+ _OBJC_IVAR_$_IADefaultsDataStore._datastoreName
+ _OBJC_IVAR_$_IADefaultsDataStore._defaultsHandle
+ _OBJC_IVAR_$_IAEventDispatcher._isUnitTest
+ _OBJC_IVAR_$_IAEventDispatcher._payloadsObservedForTesting
+ _OBJC_IVAR_$_IASAnalyzer.analyzerSessionId
+ _OBJC_IVAR_$_IASAnalyzer.depthRange
+ _OBJC_IVAR_$_IASAnalyzer.eventHandler
+ _OBJC_IVAR_$_IASAnalyzer.queue
+ _OBJC_IVAR_$_IASAnalyzer.sessionErrors
+ _OBJC_IVAR_$_IASAnalyzer.sessionManagerDelegate
+ _OBJC_IVAR_$_IASAnalyzerErrors._errors
+ _OBJC_IVAR_$_IASDailyGarbageCollectionAnalyzer._dateOfLastAction
+ _OBJC_IVAR_$_IASDailyGarbageCollectionAnalyzer._lastConsumedSignalTimestamp
+ _OBJC_IVAR_$_IASDailyGarbageCollectionStateMachineAnalyzer._state
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzer._charsRemovedBeforeFirstInsertionCount
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzer._emojisRemovedBeforeFirstInsertionCount
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzer._entries
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzer._insertionObservedInSession
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzer._keyboardTrialParameters
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzer._largestSessionDeletionLength
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzer._largestSessionInsertionLength
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzer._mostRecentAppBundleId
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzer._mostRecentProcessId
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzer._name
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzer._sessionIsModeless
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzer._sessionNetCharacters
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzerEntry._inputActions
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzerEntry._netCharacters
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzerEntry._netEmojiCharacters
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzerEntry._userRemovedCharacters
+ _OBJC_IVAR_$_IASTextInputActionsAnalyzerEntry._userRemovedEmojiCharacters
+ _OBJC_IVAR_$_IASTextInputActionsEvent._bundleId
+ _OBJC_IVAR_$_IASTextInputActionsEvent._inputActionCount
+ _OBJC_IVAR_$_IASTextInputActionsEvent._inputModeIdentifier
+ _OBJC_IVAR_$_IASTextInputActionsEvent._isEmojiSearch
+ _OBJC_IVAR_$_IASTextInputActionsEvent._isMarkedText
+ _OBJC_IVAR_$_IASTextInputActionsEvent._keyboardLayout
+ _OBJC_IVAR_$_IASTextInputActionsEvent._keyboardType
+ _OBJC_IVAR_$_IASTextInputActionsEvent._keyboardVariant
+ _OBJC_IVAR_$_IASTextInputActionsEvent._language
+ _OBJC_IVAR_$_IASTextInputActionsEvent._netCharacters
+ _OBJC_IVAR_$_IASTextInputActionsEvent._netEmojiCharacters
+ _OBJC_IVAR_$_IASTextInputActionsEvent._region
+ _OBJC_IVAR_$_IASTextInputActionsEvent._sessionActions
+ _OBJC_IVAR_$_IASTextInputActionsEvent._sessionIsModeless
+ _OBJC_IVAR_$_IASTextInputActionsEvent._source
+ _OBJC_IVAR_$_IASTextInputActionsEvent._type
+ _OBJC_IVAR_$_IASTextInputActionsEvent._userRemovedCharacters
+ _OBJC_IVAR_$_IASTextInputActionsEvent._userRemovedEmojiCharacters
+ _OBJC_IVAR_$_IASignalAnalyticsObject._analyticsSessionIdString
+ _OBJC_IVAR_$_IASignalAnalyticsObject._channelName
+ _OBJC_IVAR_$_IASignalAnalyticsObject._payload
+ _OBJC_IVAR_$_IASignalAnalyticsObject._signalName
+ _OBJC_IVAR_$_IAStringDetails._characters
+ _OBJC_IVAR_$_IAStringDetails._emojiCharacters
+ _OBJC_IVAR_$_IAStringDetails._punctuationCharacters
+ _OBJC_IVAR_$_IAStringDetails._textIsTooLong
+ _OBJC_IVAR_$_IATextInputActionsAnalytics._analyticsDelegate
+ _OBJC_IVAR_$_IATextInputActionsAnalytics._lastAction
+ _OBJC_IVAR_$_IATextInputActionsAnalytics._localServer
+ _OBJC_IVAR_$_IATextInputActionsAnalytics._queue
+ _OBJC_IVAR_$_IATextInputActionsAnalytics._sessionIdentifier
+ _OBJC_IVAR_$_IATextInputActionsAnalytics._useAnalyticsDaemon
+ _OBJC_IVAR_$_IATextInputActionsAnalytics._useLocalAnalytics
+ _OBJC_IVAR_$_IATextInputActionsInputMode._inputModeIdentifier
+ _OBJC_IVAR_$_IATextInputActionsInputMode._keyboardLayout
+ _OBJC_IVAR_$_IATextInputActionsInputMode._keyboardType
+ _OBJC_IVAR_$_IATextInputActionsInputMode._keyboardVariant
+ _OBJC_IVAR_$_IATextInputActionsInputMode._language
+ _OBJC_IVAR_$_IATextInputActionsInputMode._region
+ _OBJC_IVAR_$_IATextInputActionsServer._analyzer
+ _OBJC_IVAR_$_IATextInputActionsServer._queue
+ _OBJC_IVAR_$_IATextInputActionsServer._recentActions
+ _OBJC_IVAR_$_IATextInputActionsServer._testingDelegate
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._clientSideSessionErrors
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._flagOptions
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._inputActionCountFromMergedActions
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._inputMode
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._insertedEmojiCount
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._insertedPunctuationCount
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._insertedTextLength
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._largestSingleDeletionLength
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._largestSingleInsertionLength
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._processBundleId
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._relativeRangeBefore
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._removedEmojiCount
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._removedPunctuationCount
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._removedTextLength
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._source
+ _OBJC_IVAR_$_IATextInputActionsSessionAction._textInputActionsType
+ _OBJC_IVAR_$_IATextInputActionsSessionActionInformation._sessionActionsString
+ _OBJC_IVAR_$_IATextInputActionsSessionActionInformation._sessionHasDictation
+ _OBJC_IVAR_$_IATextInputActionsSessionActionInformation._sessionHasOnlyPrimaryInput
+ _OBJC_IVAR_$_IATextInputActionsSessionDeletionAction._options
+ _OBJC_IVAR_$_IATextInputActionsSessionDictationBeganAction._dictationBeganCount
+ _OBJC_IVAR_$_IATextInputActionsSessionDictationBeganAction._modelessUsedAtLeastOnceCount
+ _OBJC_IVAR_$_IATextInputActionsSessionDictationBeganAction._multiModalDictationBeganCount
+ _OBJC_IVAR_$_IATextInputActionsSessionEndAction._keyboardTrialParameters
+ _OBJC_IVAR_$_IATextInputActionsSessionGlomojiTapAction._glomojiType
+ _OBJC_IVAR_$_IATextInputActionsSessionGlomojiTapAction._mergedActionsCount
+ _OBJC_IVAR_$_IATextInputActionsSessionGlomojiTapAction._originalInputMode
+ _OBJC_IVAR_$_IATextInputActionsSessionGlomojiTapAction._updatedInputMode
+ _OBJC_IVAR_$_IATextInputActionsSessionInsertionAction._options
+ _OBJC_IVAR_$_IATextInputActionsSessionInsertionAction._withAlternativesCount
+ _OBJC_IVAR_$_IATextInputActionsSessionKBMenuAppearAction._glomojiType
+ _OBJC_IVAR_$_IATextInputActionsSessionKBMenuAppearAction._originalInputMode
+ _OBJC_IVAR_$_IATextInputActionsSessionKBMenuDismissAction._KBMenuDismissSource
+ _OBJC_IVAR_$_IATextInputActionsSessionKBMenuInteractionAction._KBMenuInteractionSource
+ _OBJC_IVAR_$_IATextInputActionsSessionKBMenuInteractionAction._KBMenuSelectedAction
+ _OBJC_IVAR_$_IATextInputActionsSessionKBMenuInteractionAction._updatedInputMode
+ _OBJC_IVAR_$_IATextInputActionsSessionKeyboardDockItemButtonPressAction._buttonPressResult
+ _OBJC_IVAR_$_IATextInputActionsSessionKeyboardDockItemButtonPressAction._buttonSize
+ _OBJC_IVAR_$_IATextInputActionsSessionKeyboardDockItemButtonPressAction._buttonType
+ _OBJC_IVAR_$_IATextInputActionsSessionKeyboardDockItemButtonPressAction._touchDownPoint
+ _OBJC_IVAR_$_IATextInputActionsSessionKeyboardDockItemButtonPressAction._touchDuration
+ _OBJC_IVAR_$_IATextInputActionsSessionKeyboardDockItemButtonPressAction._touchUpPoint
+ _OBJC_IVAR_$_IATextInputActionsSessionKeyboardDockItemButtonPressAction._uiOrientation
+ _OBJC_IVAR_$_IATextInputActionsSessionReplaceTextAction._options
+ _OBJC_IVAR_$_IATextInputActionsSessionReplaceWithCandidateAction._replaceWithCandidateType
+ _OBJC_IVAR_$_IATextInputActionsSessionSelectionAction._rangeAfter
+ _OBJC_IVAR_$_IAXPCClient._connection
+ _OBJC_IVAR_$_IAXPCClient._serverInstance
+ _OBJC_IVAR_$_IAXPCObject.appBundleId
+ _OBJC_IVAR_$_IAXPCObject.appSessionId
+ _OBJC_IVAR_$_IAXPCObject.creationTimestamp
+ _OBJC_IVAR_$_IAXPCObject.textInputSessionId
+ _OBJC_IVAR_$_IAXPCObject.timestamp
+ _OBJC_METACLASS_$_IAKeyboardDetection
+ _OBJC_METACLASS_$_IASAnalyzer
+ _OBJC_METACLASS_$_IASAnalyzerErrors
+ _OBJC_METACLASS_$_IASDailyGarbageCollectionAnalyzer
+ _OBJC_METACLASS_$_IASDailyGarbageCollectionStateMachineAnalyzer
+ _OBJC_METACLASS_$_IASTextInputActionsAnalyzer
+ _OBJC_METACLASS_$_IASTextInputActionsAnalyzerEntry
+ _OBJC_METACLASS_$_IASTextInputActionsErrorChecking
+ _OBJC_METACLASS_$_IASTextInputActionsEvent
+ _OBJC_METACLASS_$_IAStringDetails
+ _OBJC_METACLASS_$_IATextInputActionsServer
+ _OBJC_METACLASS_$_IATextInputActionsSessionActionInformation
+ _OBJC_METACLASS_$_IAXPCSPIObject
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __CTCategoryForBundleId:timeout:.categoryLookup
+ __CTCategoryForBundleId:timeout:.onceToken
+ __DATA_IAFeedbackServiceSwiftBridge
+ __INSTANCE_METHODS_IAFeedbackServiceSwiftBridge
+ __IVARS_IAFeedbackServiceSwiftBridge
+ __METACLASS_DATA_IAFeedbackServiceSwiftBridge
+ __OBJC_$_CATEGORY_NSMutableDictionary_$_SetObjectIfNotNil
+ __OBJC_$_CLASS_METHODS_IADataStoreBoolean
+ __OBJC_$_CLASS_METHODS_IADataStoreCounter
+ __OBJC_$_CLASS_METHODS_IADataStoreDaterange
+ __OBJC_$_CLASS_METHODS_IADataStoreObject
+ __OBJC_$_CLASS_METHODS_IAEventDispatcher
+ __OBJC_$_CLASS_METHODS_IAGenmojiAnalytics
+ __OBJC_$_CLASS_METHODS_IAImageGenerationAnalytics
+ __OBJC_$_CLASS_METHODS_IAKeyboardDetection
+ __OBJC_$_CLASS_METHODS_IASAnalyzer
+ __OBJC_$_CLASS_METHODS_IASAnalyzerErrors
+ __OBJC_$_CLASS_METHODS_IASDailyGarbageCollectionStateMachineAnalyzer
+ __OBJC_$_CLASS_METHODS_IASTextInputActionsAnalyzer
+ __OBJC_$_CLASS_METHODS_IASTextInputActionsAnalyzerEntry
+ __OBJC_$_CLASS_METHODS_IASTextInputActionsErrorChecking
+ __OBJC_$_CLASS_METHODS_IAServerStats
+ __OBJC_$_CLASS_METHODS_IASignalAnalytics
+ __OBJC_$_CLASS_METHODS_IASignalAnalyticsObject(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IASmartRepliesAnalytics
+ __OBJC_$_CLASS_METHODS_IAStringDetails
+ __OBJC_$_CLASS_METHODS_IATextInputActionsInputMode
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionAction(NSSecureCoding|ConvertToDictionary)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionDeletionAction(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionDictationBeganAction(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionEndAction(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionGlomojiTapAction(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionInsertionAction(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionKBMenuAppearAction(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionKBMenuDismissAction(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionKBMenuInteractionAction(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionKeyboardDockItemButtonPressAction(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionReplaceTextAction(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionReplaceWithCandidateAction(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsSessionSelectionAction(NSSecureCoding)
+ __OBJC_$_CLASS_METHODS_IATextInputActionsUtils
+ __OBJC_$_CLASS_METHODS_IAUtility
+ __OBJC_$_CLASS_METHODS_IAXPCObject
+ __OBJC_$_CLASS_METHODS_IAXPCSPIObject
+ __OBJC_$_CLASS_PROP_LIST_IATextInputActionsInputMode
+ __OBJC_$_CLASS_PROP_LIST_IAXPCObject
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_IADataStoreBoolean
+ __OBJC_$_INSTANCE_METHODS_IADataStoreCounter
+ __OBJC_$_INSTANCE_METHODS_IADataStoreDaterange
+ __OBJC_$_INSTANCE_METHODS_IADataStoreObject
+ __OBJC_$_INSTANCE_METHODS_IADefaultsDataStore
+ __OBJC_$_INSTANCE_METHODS_IAEventDispatcher
+ __OBJC_$_INSTANCE_METHODS_IASAnalyzer
+ __OBJC_$_INSTANCE_METHODS_IASAnalyzerErrors
+ __OBJC_$_INSTANCE_METHODS_IASDailyGarbageCollectionAnalyzer
+ __OBJC_$_INSTANCE_METHODS_IASDailyGarbageCollectionStateMachineAnalyzer
+ __OBJC_$_INSTANCE_METHODS_IASTextInputActionsAnalyzer
+ __OBJC_$_INSTANCE_METHODS_IASTextInputActionsAnalyzerEntry
+ __OBJC_$_INSTANCE_METHODS_IASTextInputActionsEvent
+ __OBJC_$_INSTANCE_METHODS_IASignalAnalyticsObject(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IAStringDetails
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsAnalytics(TestingSupport)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsInputMode
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsServer
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionAction(NSSecureCoding|ConvertToDictionary)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionActionInformation
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionBeganAction
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionCommitTextAction
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionCopyAction
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionCutAction
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionDeletionAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionDictationBeganAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionDictationEndedAction
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionEndAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionGlomojiTapAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionInsertionAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionKBMenuAppearAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionKBMenuDismissAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionKBMenuInteractionAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionKeyboardDockItemButtonPressAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionPasteAction
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionRedoAction
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionReplaceTextAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionReplaceWithCandidateAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionSelectionAction(NSSecureCoding)
+ __OBJC_$_INSTANCE_METHODS_IATextInputActionsSessionUndoAction
+ __OBJC_$_INSTANCE_METHODS_IATextInputUserPreferenceAnalytics
+ __OBJC_$_INSTANCE_METHODS_IAXPCClient
+ __OBJC_$_INSTANCE_METHODS_IAXPCObject
+ __OBJC_$_INSTANCE_METHODS_IAXPCProtocolObject
+ __OBJC_$_INSTANCE_METHODS_NSMutableDictionary(SetObjectIfNotNil|SetObjectIfNotNil)
+ __OBJC_$_INSTANCE_VARIABLES_IADataStoreBoolean
+ __OBJC_$_INSTANCE_VARIABLES_IADataStoreCounter
+ __OBJC_$_INSTANCE_VARIABLES_IADataStoreDaterange
+ __OBJC_$_INSTANCE_VARIABLES_IADataStoreObject
+ __OBJC_$_INSTANCE_VARIABLES_IADefaultsDataStore
+ __OBJC_$_INSTANCE_VARIABLES_IAEventDispatcher
+ __OBJC_$_INSTANCE_VARIABLES_IASAnalyzer
+ __OBJC_$_INSTANCE_VARIABLES_IASAnalyzerErrors
+ __OBJC_$_INSTANCE_VARIABLES_IASDailyGarbageCollectionAnalyzer
+ __OBJC_$_INSTANCE_VARIABLES_IASDailyGarbageCollectionStateMachineAnalyzer
+ __OBJC_$_INSTANCE_VARIABLES_IASTextInputActionsAnalyzer
+ __OBJC_$_INSTANCE_VARIABLES_IASTextInputActionsAnalyzerEntry
+ __OBJC_$_INSTANCE_VARIABLES_IASTextInputActionsEvent
+ __OBJC_$_INSTANCE_VARIABLES_IASignalAnalyticsObject
+ __OBJC_$_INSTANCE_VARIABLES_IAStringDetails
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsInputMode
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsServer
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionAction
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionActionInformation
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionDeletionAction
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionDictationBeganAction
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionEndAction
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionGlomojiTapAction
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionInsertionAction
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionKBMenuAppearAction
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionKBMenuDismissAction
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionKBMenuInteractionAction
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionKeyboardDockItemButtonPressAction
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionReplaceTextAction
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionReplaceWithCandidateAction
+ __OBJC_$_INSTANCE_VARIABLES_IATextInputActionsSessionSelectionAction
+ __OBJC_$_INSTANCE_VARIABLES_IAXPCClient
+ __OBJC_$_INSTANCE_VARIABLES_IAXPCObject
+ __OBJC_$_PROP_LIST_IADataStoreBoolean
+ __OBJC_$_PROP_LIST_IADataStoreCounter
+ __OBJC_$_PROP_LIST_IADataStoreDaterange
+ __OBJC_$_PROP_LIST_IADataStoreObject
+ __OBJC_$_PROP_LIST_IADefaultsDataStore
+ __OBJC_$_PROP_LIST_IAEventDispatcher
+ __OBJC_$_PROP_LIST_IASAnalyzer
+ __OBJC_$_PROP_LIST_IASAnalyzerErrors
+ __OBJC_$_PROP_LIST_IASAnalyzerProtocol
+ __OBJC_$_PROP_LIST_IASDailyGarbageCollectionAnalyzer
+ __OBJC_$_PROP_LIST_IASDailyGarbageCollectionStateMachineAnalyzer
+ __OBJC_$_PROP_LIST_IASTextInputActionsAnalyzer
+ __OBJC_$_PROP_LIST_IASTextInputActionsAnalyzerEntry
+ __OBJC_$_PROP_LIST_IASTextInputActionsEvent
+ __OBJC_$_PROP_LIST_IASessionMetadataProtocol
+ __OBJC_$_PROP_LIST_IASignalAnalyticsObject
+ __OBJC_$_PROP_LIST_IAStringDetails
+ __OBJC_$_PROP_LIST_IATextInputActionsAnalytics
+ __OBJC_$_PROP_LIST_IATextInputActionsInputMode
+ __OBJC_$_PROP_LIST_IATextInputActionsServer
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionActionInformation
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionDeletionAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionDictationBeganAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionEndAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionGlomojiTapAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionInsertionAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionKBMenuAppearAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionKBMenuDismissAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionKBMenuInteractionAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionKeyboardDockItemButtonPressAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionReplaceTextAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionReplaceWithCandidateAction
+ __OBJC_$_PROP_LIST_IATextInputActionsSessionSelectionAction
+ __OBJC_$_PROP_LIST_IAXPCClient
+ __OBJC_$_PROP_LIST_IAXPCObject
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_CLASS_METHODS_IASAnalyzerProtocol
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_IASAnalyzerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_IASessionMetadataProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_IATelemetryEvent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_IXAXPCProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_IASAnalyzerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_IASessionMetadataProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_IATelemetryEvent
+ __OBJC_$_PROTOCOL_METHOD_TYPES_IXAXPCProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_IASAnalyzerProtocol
+ __OBJC_$_PROTOCOL_REFS_IASessionMetadataProtocol
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_IASAnalyzer
+ __OBJC_CLASS_PROTOCOLS_$_IASTextInputActionsEvent
+ __OBJC_CLASS_PROTOCOLS_$_IATextInputActionsInputMode
+ __OBJC_CLASS_PROTOCOLS_$_IAXPCObject
+ __OBJC_CLASS_PROTOCOLS_$_IAXPCProtocolObject
+ __OBJC_CLASS_RO_$_IADataStoreBoolean
+ __OBJC_CLASS_RO_$_IADataStoreCounter
+ __OBJC_CLASS_RO_$_IADataStoreDaterange
+ __OBJC_CLASS_RO_$_IADataStoreObject
+ __OBJC_CLASS_RO_$_IADefaultsDataStore
+ __OBJC_CLASS_RO_$_IAEventDispatcher
+ __OBJC_CLASS_RO_$_IAGenmojiAnalytics
+ __OBJC_CLASS_RO_$_IAImageGenerationAnalytics
+ __OBJC_CLASS_RO_$_IAKeyboardDetection
+ __OBJC_CLASS_RO_$_IASAnalyzer
+ __OBJC_CLASS_RO_$_IASAnalyzerErrors
+ __OBJC_CLASS_RO_$_IASDailyGarbageCollectionAnalyzer
+ __OBJC_CLASS_RO_$_IASDailyGarbageCollectionStateMachineAnalyzer
+ __OBJC_CLASS_RO_$_IASTextInputActionsAnalyzer
+ __OBJC_CLASS_RO_$_IASTextInputActionsAnalyzerEntry
+ __OBJC_CLASS_RO_$_IASTextInputActionsErrorChecking
+ __OBJC_CLASS_RO_$_IASTextInputActionsEvent
+ __OBJC_CLASS_RO_$_IAServerStats
+ __OBJC_CLASS_RO_$_IASignalAnalytics
+ __OBJC_CLASS_RO_$_IASignalAnalyticsObject
+ __OBJC_CLASS_RO_$_IASmartRepliesAnalytics
+ __OBJC_CLASS_RO_$_IAStringDetails
+ __OBJC_CLASS_RO_$_IATextInputActionsAnalytics
+ __OBJC_CLASS_RO_$_IATextInputActionsInputMode
+ __OBJC_CLASS_RO_$_IATextInputActionsServer
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionActionInformation
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionBeganAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionCommitTextAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionCopyAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionCutAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionDeletionAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionDictationBeganAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionDictationEndedAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionEndAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionGlomojiTapAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionInsertionAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionKBMenuAppearAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionKBMenuDismissAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionKBMenuInteractionAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionKeyboardDockItemButtonPressAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionPasteAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionRedoAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionReplaceTextAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionReplaceWithCandidateAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionSelectionAction
+ __OBJC_CLASS_RO_$_IATextInputActionsSessionUndoAction
+ __OBJC_CLASS_RO_$_IATextInputActionsUtils
+ __OBJC_CLASS_RO_$_IATextInputUserPreferenceAnalytics
+ __OBJC_CLASS_RO_$_IAUtility
+ __OBJC_CLASS_RO_$_IAXPCClient
+ __OBJC_CLASS_RO_$_IAXPCObject
+ __OBJC_CLASS_RO_$_IAXPCProtocolObject
+ __OBJC_CLASS_RO_$_IAXPCSPIObject
+ __OBJC_LABEL_PROTOCOL_$_IASAnalyzerProtocol
+ __OBJC_LABEL_PROTOCOL_$_IASessionMetadataProtocol
+ __OBJC_LABEL_PROTOCOL_$_IATelemetryEvent
+ __OBJC_LABEL_PROTOCOL_$_IXAXPCProtocol
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_IADataStoreBoolean
+ __OBJC_METACLASS_RO_$_IADataStoreCounter
+ __OBJC_METACLASS_RO_$_IADataStoreDaterange
+ __OBJC_METACLASS_RO_$_IADataStoreObject
+ __OBJC_METACLASS_RO_$_IADefaultsDataStore
+ __OBJC_METACLASS_RO_$_IAEventDispatcher
+ __OBJC_METACLASS_RO_$_IAGenmojiAnalytics
+ __OBJC_METACLASS_RO_$_IAImageGenerationAnalytics
+ __OBJC_METACLASS_RO_$_IAKeyboardDetection
+ __OBJC_METACLASS_RO_$_IASAnalyzer
+ __OBJC_METACLASS_RO_$_IASAnalyzerErrors
+ __OBJC_METACLASS_RO_$_IASDailyGarbageCollectionAnalyzer
+ __OBJC_METACLASS_RO_$_IASDailyGarbageCollectionStateMachineAnalyzer
+ __OBJC_METACLASS_RO_$_IASTextInputActionsAnalyzer
+ __OBJC_METACLASS_RO_$_IASTextInputActionsAnalyzerEntry
+ __OBJC_METACLASS_RO_$_IASTextInputActionsErrorChecking
+ __OBJC_METACLASS_RO_$_IASTextInputActionsEvent
+ __OBJC_METACLASS_RO_$_IAServerStats
+ __OBJC_METACLASS_RO_$_IASignalAnalytics
+ __OBJC_METACLASS_RO_$_IASignalAnalyticsObject
+ __OBJC_METACLASS_RO_$_IASmartRepliesAnalytics
+ __OBJC_METACLASS_RO_$_IAStringDetails
+ __OBJC_METACLASS_RO_$_IATextInputActionsAnalytics
+ __OBJC_METACLASS_RO_$_IATextInputActionsInputMode
+ __OBJC_METACLASS_RO_$_IATextInputActionsServer
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionActionInformation
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionBeganAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionCommitTextAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionCopyAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionCutAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionDeletionAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionDictationBeganAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionDictationEndedAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionEndAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionGlomojiTapAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionInsertionAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionKBMenuAppearAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionKBMenuDismissAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionKBMenuInteractionAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionKeyboardDockItemButtonPressAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionPasteAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionRedoAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionReplaceTextAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionReplaceWithCandidateAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionSelectionAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsSessionUndoAction
+ __OBJC_METACLASS_RO_$_IATextInputActionsUtils
+ __OBJC_METACLASS_RO_$_IATextInputUserPreferenceAnalytics
+ __OBJC_METACLASS_RO_$_IAUtility
+ __OBJC_METACLASS_RO_$_IAXPCClient
+ __OBJC_METACLASS_RO_$_IAXPCObject
+ __OBJC_METACLASS_RO_$_IAXPCProtocolObject
+ __OBJC_METACLASS_RO_$_IAXPCSPIObject
+ __OBJC_PROTOCOL_$_IASAnalyzerProtocol
+ __OBJC_PROTOCOL_$_IASessionMetadataProtocol
+ __OBJC_PROTOCOL_$_IATelemetryEvent
+ __OBJC_PROTOCOL_$_IXAXPCProtocol
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_REFERENCE_$_IXAXPCProtocol
+ __PROPERTIES_IAFeedbackServiceSwiftBridge
+ ___152-[IATextInputActionsAnalytics _didReplacementForText:withText:allowNilText:allowEmptyText:allowNilReplacement:withSource:withType:withInputActionCount:]_block_invoke
+ ___161-[IATextInputActionsAnalytics didKeyboardDockItemButtonPress:buttonType:buttonSize:touchDown:touchUp:touchDuration:inputSource:inputType:uiInterfaceOrientation:]_block_invoke
+ ___21-[IAXPCClient server]_block_invoke
+ ___21-[IAXPCClient server]_block_invoke.cold.1
+ ___23+[IAUtility xpcEnabled]_block_invoke
+ ___27+[IAXPCSPIObject syncQueue]_block_invoke
+ ___27+[IAXPCSPIObject xpcClient]_block_invoke
+ ___32+[IASignalAnalytics actionQueue]_block_invoke
+ ___35+[IAEventDispatcher sharedInstance]_block_invoke
+ ___35-[IAXPCClient initWithServiceName:]_block_invoke
+ ___35-[IAXPCClient initWithServiceName:]_block_invoke.17
+ ___35-[IAXPCClient initWithServiceName:]_block_invoke.17.cold.1
+ ___35-[IAXPCClient initWithServiceName:]_block_invoke.21
+ ___35-[IAXPCClient initWithServiceName:]_block_invoke.21.cold.1
+ ___35-[IAXPCClient initWithServiceName:]_block_invoke.cold.1
+ ___35-[IAXPCClient invalidateConnection]_block_invoke
+ ___37+[IAStringDetails emojiCountForText:]_block_invoke
+ ___38+[IAXPCSPIObject invalidateConnection]_block_invoke
+ ___38-[IATextInputActionsAnalytics didCut:]_block_invoke
+ ___38-[IATextInputActionsAnalytics didRedo]_block_invoke
+ ___38-[IATextInputActionsAnalytics didUndo]_block_invoke
+ ___39-[IATextInputActionsAnalytics didCopy:]_block_invoke
+ ___40+[IAKeyboardDetection keyboardIsPresent]_block_invoke
+ ___40-[IATextInputActionsAnalytics didPaste:]_block_invoke
+ ___41-[IASTextInputActionsEvent dispatchEvent]_block_invoke
+ ___43-[IAEventDispatcher dispatchEvent:payload:]_block_invoke
+ ___44+[IAGenmojiAnalytics genmojiSourceToEnumMap]_block_invoke
+ ___44+[IAUtility _CTCategoryForBundleId:timeout:]_block_invoke
+ ___44+[IAUtility _CTCategoryForBundleId:timeout:]_block_invoke.734
+ ___44+[IAUtility _CTCategoryForBundleId:timeout:]_block_invoke.cold.1
+ ___44-[IATextInputActionsAnalytics didSessionEnd]_block_invoke
+ ___45-[IASTextInputActionsAnalyzer consumeAction:]_block_invoke
+ ___45-[IATextInputActionsAnalytics didCommitText:]_block_invoke
+ ___46-[IATextInputActionsAnalytics didDictationEnd]_block_invoke
+ ___46-[IATextInputActionsAnalytics didSessionBegin]_block_invoke
+ ___47-[IATextInputActionsAnalytics didKBMenuAppear:]_block_invoke
+ ___48+[IAStringDetails sharedPunctuationCharacterSet]_block_invoke
+ ___48-[IATextInputActionsAnalytics didKBMenuDismiss:]_block_invoke
+ ___49-[IATextInputActionsSessionEndAction description]_block_invoke
+ ___50+[IAServerStats reportConnectionStatusSuccessful:]_block_invoke
+ ___51+[IASTextInputActionsErrorChecking validateRegion:]_block_invoke
+ ___52+[IAGenmojiAnalytics genmojiCreationSignalToEnumMap]_block_invoke
+ ___52-[IATextInputActionsAnalytics _didInsertTextAction:]_block_invoke
+ ___52-[IATextInputActionsAnalytics didCandidateBarAction]_block_invoke
+ ___53+[IASTextInputActionsErrorChecking validateLanguage:]_block_invoke
+ ___54+[IASmartRepliesAnalytics smartRepliesSignalToEnumMap]_block_invoke
+ ___55-[IATextInputActionsAnalytics didReplaceWithCandidate:]_block_invoke
+ ___55-[IATextInputActionsServer setKeyboardTrialParameters:]_block_invoke
+ ___56+[IAGenmojiAnalytics genmojiCreationFailReasonToEnumMap]_block_invoke
+ ___56-[IATextInputActionsAnalytics _didDeleteBackwardAction:]_block_invoke
+ ___57+[IASTextInputActionsErrorChecking validateRegionHelper:]_block_invoke
+ ___58+[IAImageGenerationAnalytics imageCreationSignalToEnumMap]_block_invoke
+ ___58-[IATextInputActionsAnalytics didGlomojiTap:newInputMode:]_block_invoke
+ ___59+[IAImageGenerationAnalytics imageCreationFeatureToEnumMap]_block_invoke
+ ___59+[IASTextInputActionsErrorChecking validateLanguageHelper:]_block_invoke
+ ___60+[IAUtility _lookupAppBundle:useCTCategoryFallback:timeout:]_block_invoke
+ ___62-[IADefaultsDataStore objectExistsWithName:andType:withError:]_block_invoke
+ ___62-[IATextInputActionsServer enumerateTextInputActionsAnalytics]_block_invoke
+ ___65-[IATextInputActionsAnalytics didKBMenuAppear:originalInputMode:]_block_invoke
+ ___65-[IATextInputActionsAnalytics initWithAnalyticsMetadataObserver:]_block_invoke
+ ___66-[IASTextInputActionsAnalyzer enumerateTextInputActionsAnalytics:]_block_invoke
+ ___66-[IASTextInputActionsAnalyzer enumerateTextInputActionsAnalytics:]_block_invoke_2
+ ___66-[IASTextInputActionsAnalyzer enumerateTextInputActionsAnalytics:]_block_invoke_3
+ ___66-[IASTextInputActionsAnalyzer enumerateTextInputActionsAnalytics:]_block_invoke_4
+ ___66-[IASTextInputActionsAnalyzer enumerateTextInputActionsAnalytics:]_block_invoke_5
+ ___67-[IATextInputActionsAnalytics didConversionForMarkedText:withText:]_block_invoke
+ ___68-[IASTextInputActionsAnalyzer computeSessionActionsStringOnSession:]_block_invoke
+ ___68-[IASTextInputActionsAnalyzer computeSessionActionsStringOnSession:]_block_invoke_2
+ ___68-[IASTextInputActionsAnalyzer computeSessionActionsStringOnSession:]_block_invoke_2.cold.1
+ ___68-[IASTextInputActionsAnalyzer computeSessionActionsStringOnSession:]_block_invoke_3
+ ___72-[IATextInputActionsAnalytics didChangeToSelection:relativeRangeBefore:]_block_invoke
+ ___72-[IATextInputActionsAnalytics(TestingSupport) dispatchToAnalyticsQueue:]_block_invoke
+ ___73-[IATextInputActionsAnalytics didDictationBegin:usesMultiModalDictation:]_block_invoke
+ ___76-[IATextInputActionsAnalytics didGlomojiTap:originalInputMode:newInputMode:]_block_invoke
+ ___80-[IATextInputActionsAnalytics didKBMenuInteraction:selectedAction:newInputMode:]_block_invoke
+ ___81+[IASignalAnalytics asyncSendSignal:toChannel:withNullableSessionID:withPayload:]_block_invoke
+ ___81+[IASignalAnalytics asyncSendSignal:toChannel:withNullableSessionID:withPayload:]_block_invoke.cold.1
+ ___86+[IASignalAnalytics asyncSendSignal:toChannel:withNullableUniqueStringID:withPayload:]_block_invoke
+ ___86+[IASignalAnalytics asyncSendSignal:toChannel:withNullableUniqueStringID:withPayload:]_block_invoke.cold.1
+ ___86-[IASTextInputActionsAnalyzer initWithAnalyzerSessionId:sessionManagerDelegate:queue:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___IADefaultsDataStoreLog_block_invoke
+ ___IAEventDispatcherLog_block_invoke
+ ___IAGlomojiLog_block_invoke
+ ___IAKeyboardDetectionLog_block_invoke
+ ___IASAnalyzerErrorsLog_block_invoke
+ ___IASTextInputActionsLog_block_invoke
+ ___IAServerStatsLog_block_invoke
+ ___IASignalAnalyticsLog_block_invoke
+ ___IATextInputActionsLog_block_invoke
+ ___IATextInputUserPreferenceAnalyticsLog_block_invoke
+ ___IAUtilityLog_block_invoke
+ ___IAXPCClientLog_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56bs64r72r_e59_v32?0"NSString"8"IASTextInputActionsAnalyzerEntry"16^B24ls32l8s40l8s48l8r64l8r72l8s56l8
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e22_v16?0"NSDictionary"8l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_33_e5_v8?0l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32r_e42_v40?0"EMFEmojiToken"8{_NSRange=QQ}16^B32lr32l8
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e25_v32?0"NSNumber"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40r_e32_v24?0"CTCategory"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e8_v16?0Q8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_50_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s_e31_v32?0"NSMutableArray"8Q16^B24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e41_v32?0"NSString"8"NSMutableArray"16^B24ls32l8r48l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40s48r_e31_v32?0"NSMutableArray"8Q16^B24lr48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e31_v32?0"NSMutableArray"8Q16^B24ls32l8s40l8s48l8r64l8r72l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56bs64r72r_e31_v32?0"NSMutableArray"8Q16^B24ls32l8s40l8s48l8r64l8r72l8s56l8
+ ___block_descriptor_96_e8_32s40s48s56bs64r72r_e36_v32?0"NSMutableDictionary"8Q16^B24ls32l8s40l8s48l8r64l8r72l8s56l8
+ ___block_literal_global
+ ___block_literal_global.10
+ ___block_literal_global.13
+ ___block_literal_global.15
+ ___block_literal_global.16
+ ___block_literal_global.19
+ ___block_literal_global.20
+ ___block_literal_global.22
+ ___block_literal_global.25
+ ___block_literal_global.346
+ ___block_literal_global.4
+ ___block_literal_global.663
+ ___block_literal_global.665
+ ___block_literal_global.7
+ ___block_literal_global.736
+ ___block_literal_global.811
+ ___swift_allocate_value_buffer
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __actionQueue
+ __lookupAppBundle:useCTCategoryFallback:timeout:.categoryLookup
+ __lookupAppBundle:useCTCategoryFallback:timeout:.onceToken
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_InputAnalytics
+ __swift_FORCE_LOAD_$_swiftDispatch_$_InputAnalytics
+ __swift_FORCE_LOAD_$_swiftFoundation_$_InputAnalytics
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_InputAnalytics
+ __swift_FORCE_LOAD_$_swiftXPC_$_InputAnalytics
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_InputAnalytics
+ __swift_FORCE_LOAD_$_swiftos_$_InputAnalytics
+ __swift_stdlib_malloc_size
+ __syncQueue
+ __xpcClient
+ _actionQueue.onceToken
+ _defaultsDataStoreVersion
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _genmojiCreationFailReasonToEnumMap.mapping
+ _genmojiCreationFailReasonToEnumMap.onceToken
+ _genmojiCreationSignalToEnumMap.mapping
+ _genmojiCreationSignalToEnumMap.onceToken
+ _genmojiSourceToEnumMap.mapping
+ _genmojiSourceToEnumMap.onceToken
+ _imageCreationFeatureToEnumMap.mapping
+ _imageCreationFeatureToEnumMap.onceToken
+ _imageCreationSignalToEnumMap.mapping
+ _imageCreationSignalToEnumMap.onceToken
+ _keypath_get_selector_action
+ _keypath_get_selector_featureDomain
+ _keypath_get_selector_generatedContent
+ _keypath_get_selector_modelInfo
+ _keypath_get_selector_originalContent
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_CTCategoryForBundleId:timeout:
+ _objc_msgSend$_clearWithMask:
+ _objc_msgSend$_containsEmoji
+ _objc_msgSend$_createErrorWithDescription:code:error:
+ _objc_msgSend$_didDeleteBackwardAction:
+ _objc_msgSend$_didDeleteBackwardCount:withType:shouldOverrideInputActionCountToZero:withInputMode:forceNotMarkedText:
+ _objc_msgSend$_didDeleteBackwardText:withType:shouldOverrideInputActionCountToZero:withInputMode:forceNotMarkedText:
+ _objc_msgSend$_didDeleteBackwardTextDetails:withType:shouldOverrideInputActionCountToZero:withInputMode:forceNotMarkedText:
+ _objc_msgSend$_didDeletionKeyPressOfKey:withType:
+ _objc_msgSend$_didInsertTextAction:
+ _objc_msgSend$_didInsertionKeyPressOfKey:withType:
+ _objc_msgSend$_didReplacementForText:withText:allowNilText:allowEmptyText:allowNilReplacement:withSource:withType:withInputActionCount:
+ _objc_msgSend$_enumerateEmojiTokensInRange:block:
+ _objc_msgSend$_instanceOfActionClass:
+ _objc_msgSend$_lookupAppBundle:useCTCategoryFallback:timeout:
+ _objc_msgSend$_removeCharactersFromSet:
+ _objc_msgSend$_updateStartDate
+ _objc_msgSend$_validName:
+ _objc_msgSend$action
+ _objc_msgSend$actionQueue
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addObject:
+ _objc_msgSend$allKeys
+ _objc_msgSend$analyticsDelegate
+ _objc_msgSend$analyticsSessionIdString
+ _objc_msgSend$analyzer
+ _objc_msgSend$analyzerSessionId
+ _objc_msgSend$appBundleId
+ _objc_msgSend$appSessionId
+ _objc_msgSend$appendString:
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$asBegan
+ _objc_msgSend$asCommitText
+ _objc_msgSend$asCopy
+ _objc_msgSend$asCut
+ _objc_msgSend$asDeletion
+ _objc_msgSend$asDictationBegan
+ _objc_msgSend$asDictationEnded
+ _objc_msgSend$asEnd
+ _objc_msgSend$asGlomojiTap
+ _objc_msgSend$asInsertion
+ _objc_msgSend$asKBMenuAppear
+ _objc_msgSend$asKBMenuDismiss
+ _objc_msgSend$asKBMenuInteraction
+ _objc_msgSend$asKeyboardDockItemButtonPress
+ _objc_msgSend$asPaste
+ _objc_msgSend$asRedo
+ _objc_msgSend$asReplaceText
+ _objc_msgSend$asReplaceWithCandidate
+ _objc_msgSend$asSelection
+ _objc_msgSend$asUndo
+ _objc_msgSend$bitfield
+ _objc_msgSend$bitmaskForDayRangeFrom:to:
+ _objc_msgSend$bitmaskForLessThanDayN:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$boolValue
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$buttonPressResult
+ _objc_msgSend$buttonType
+ _objc_msgSend$categoryForBundleID:completionHandler:
+ _objc_msgSend$changedContent
+ _objc_msgSend$channelName
+ _objc_msgSend$characters
+ _objc_msgSend$clear
+ _objc_msgSend$clientSideSessionErrors
+ _objc_msgSend$compare:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$computeSessionActionsStringOnSession:
+ _objc_msgSend$consumeAction:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$containsString:
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createDataStoreObjectWithName:withType:withError:
+ _objc_msgSend$creationTimestamp
+ _objc_msgSend$creationTimestampWithFallback
+ _objc_msgSend$currentHandler
+ _objc_msgSend$datastoreHandle
+ _objc_msgSend$date
+ _objc_msgSend$dateOfLastAction
+ _objc_msgSend$dateWithTimeInterval:sinceDate:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$defaultsHandle
+ _objc_msgSend$description
+ _objc_msgSend$destroy
+ _objc_msgSend$destroyed
+ _objc_msgSend$dictationBeganCount
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$didAction:
+ _objc_msgSend$didDeleteBackwardText:withType:
+ _objc_msgSend$didEndEnumeratingAnalytics
+ _objc_msgSend$didInsertText:withType:relativeRangeBefore:withNumAlternatives:selectedTextBefore:withInputMode:
+ _objc_msgSend$didInsertText:withType:selectedTextBefore:withInputMode:
+ _objc_msgSend$dispatchEvent:
+ _objc_msgSend$dispatchEvent:payload:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$emojiCharacters
+ _objc_msgSend$emojiCountForText:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$enumerateAnalytics
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$enumerateSubstringsInRange:options:usingBlock:
+ _objc_msgSend$enumerateTextInputActionsAnalytics
+ _objc_msgSend$enumerateTextInputActionsAnalytics:
+ _objc_msgSend$errorString
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$errors
+ _objc_msgSend$eventHandler
+ _objc_msgSend$featureDomain
+ _objc_msgSend$flagOptions
+ _objc_msgSend$flushAndSetLastAction:
+ _objc_msgSend$generateAnalyzerEntryFromAction:
+ _objc_msgSend$generatedContent
+ _objc_msgSend$getDetailsForString:
+ _objc_msgSend$getOrInitializeArrayFromArray:forKey:initCapacity:
+ _objc_msgSend$getOrInitializeArrayFromDictionary:forKey:initCapacity:
+ _objc_msgSend$getOrInitializeDictionaryFrom:forKey:initCapacity:
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$identifier
+ _objc_msgSend$increaseCountForAppBundleId:forSource:forActionType:forFlagOptions:forInputModeKey:byAnalyzerEntry:
+ _objc_msgSend$increaseWithEntry:
+ _objc_msgSend$init
+ _objc_msgSend$initFromDictionary:
+ _objc_msgSend$initWithAnalyticsMetadataObserver:withEventHandler:
+ _objc_msgSend$initWithAnalyticsMetadataObserver:withServiceName:
+ _objc_msgSend$initWithAnalyzerSessionId:sessionManagerDelegate:queue:eventHandler:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithChannel:signal:sessionIdString:creationTimestamp:payload:
+ _objc_msgSend$initWithChannel:signal:sessionIdString:payload:
+ _objc_msgSend$initWithDatastoreHandle:andName:shouldBeCreated:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithFeatureDomain:action:originalContent:generatedContent:modelInfo:
+ _objc_msgSend$initWithKey:ascending:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$initWithQueue:eventHandler:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$inputActionCount
+ _objc_msgSend$inputActionCountFromMergedActions
+ _objc_msgSend$inputActions
+ _objc_msgSend$inputMode
+ _objc_msgSend$inputModeIdentifier
+ _objc_msgSend$inputModeUniqueString
+ _objc_msgSend$insertedEmojiCount
+ _objc_msgSend$insertedPunctuationCount
+ _objc_msgSend$insertedTextLength
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$invalidateConnection
+ _objc_msgSend$isAllZeroes
+ _objc_msgSend$isCapableOfTextInsertion
+ _objc_msgSend$isDispatchable
+ _objc_msgSend$isEmojiSearchSetInFlagOptions:
+ _objc_msgSend$isEmpty
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isMarkedTextSetInFlagOptions:
+ _objc_msgSend$isMergeableWith:
+ _objc_msgSend$isSubclassOfClass:
+ _objc_msgSend$isTrue
+ _objc_msgSend$isUnitTest
+ _objc_msgSend$isWebSetInFlagOptions:
+ _objc_msgSend$keyboardIsPresentWithReply:
+ _objc_msgSend$keyboardLayout
+ _objc_msgSend$keyboardTrialParameters
+ _objc_msgSend$keyboardType
+ _objc_msgSend$keyboardVariant
+ _objc_msgSend$language
+ _objc_msgSend$largestSingleDeletionLength
+ _objc_msgSend$largestSingleInsertionLength
+ _objc_msgSend$lastConsumedSignalTimestamp
+ _objc_msgSend$lastModified
+ _objc_msgSend$length
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$localizedFailureReason
+ _objc_msgSend$log10IntegerForInt:
+ _objc_msgSend$log10WholeNumberForUnsignedInt:
+ _objc_msgSend$logErrorCodeIfNotNil:
+ _objc_msgSend$logMessage:
+ _objc_msgSend$longValue
+ _objc_msgSend$lookupAppBundle:
+ _objc_msgSend$lookupAppBundle:useCTCategoryFallback:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$mergeActionIfPossible:
+ _objc_msgSend$mergeOrConsumeAction:
+ _objc_msgSend$mergedActionsCount
+ _objc_msgSend$modelInfo
+ _objc_msgSend$modelessUsedAtLeastOnceCount
+ _objc_msgSend$multiModalDictationBeganCount
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$name
+ _objc_msgSend$netCharacterCount
+ _objc_msgSend$netCharacters
+ _objc_msgSend$netEmojiCharacters
+ _objc_msgSend$normalizedTextLength:
+ _objc_msgSend$now
+ _objc_msgSend$null
+ _objc_msgSend$numberOfMatchesInString:options:range:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectExistsWithName:andType:withError:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$options
+ _objc_msgSend$originDate
+ _objc_msgSend$originalContent
+ _objc_msgSend$originalInputMode
+ _objc_msgSend$payload
+ _objc_msgSend$payloadsObservedForTesting
+ _objc_msgSend$persist
+ _objc_msgSend$populateActionInputMode:withInputMode:
+ _objc_msgSend$prewarm
+ _objc_msgSend$processBundleId
+ _objc_msgSend$punctuationCharacterSet
+ _objc_msgSend$punctuationCountForText:
+ _objc_msgSend$q_flushRecentActions
+ _objc_msgSend$queue
+ _objc_msgSend$rangeAfter
+ _objc_msgSend$region
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$relativeRangeBefore
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removedEmojiCount
+ _objc_msgSend$removedPunctuationCount
+ _objc_msgSend$removedTextLength
+ _objc_msgSend$reportConnectionStatusSuccessful:
+ _objc_msgSend$reset
+ _objc_msgSend$resume
+ _objc_msgSend$sendSignal:toChannel:withNullableSessionID:withPayload:
+ _objc_msgSend$sendSignal:toChannel:withNullableUniqueStringID:withPayload:
+ _objc_msgSend$server
+ _objc_msgSend$sessionActionsEnumFromSource:
+ _objc_msgSend$sessionActionsEnumFromSource:type:
+ _objc_msgSend$sessionActionsString
+ _objc_msgSend$sessionErrors
+ _objc_msgSend$sessionHasDictation
+ _objc_msgSend$sessionHasOnlyPrimaryInput
+ _objc_msgSend$sessionIdentifier
+ _objc_msgSend$setAction:
+ _objc_msgSend$setAnalyticsSessionIdString:
+ _objc_msgSend$setAnalyzerSessionId:
+ _objc_msgSend$setAppBundleId:
+ _objc_msgSend$setBool:forField:inFlagOptions:
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setButtonPressResult:
+ _objc_msgSend$setButtonSize:
+ _objc_msgSend$setButtonType:
+ _objc_msgSend$setChannelName:
+ _objc_msgSend$setCharacters:
+ _objc_msgSend$setClientSideSessionErrors:
+ _objc_msgSend$setCreationTimestamp:
+ _objc_msgSend$setDateOfLastAction:
+ _objc_msgSend$setDictationBeganCount:
+ _objc_msgSend$setEmojiCharacters:
+ _objc_msgSend$setErrors:
+ _objc_msgSend$setEventHandler:
+ _objc_msgSend$setFeatureDomain:
+ _objc_msgSend$setFlagOptions:
+ _objc_msgSend$setGeneratedContent:
+ _objc_msgSend$setGlomojiType:
+ _objc_msgSend$setInputActionCountFromMergedActions:
+ _objc_msgSend$setInputActions:
+ _objc_msgSend$setInputMode:
+ _objc_msgSend$setInputModeIdentifier:
+ _objc_msgSend$setInsertedEmojiCount:
+ _objc_msgSend$setInsertedPunctuationCount:
+ _objc_msgSend$setInsertedTextLength:
+ _objc_msgSend$setInsertedTextLengthWithoutTracking:
+ _objc_msgSend$setInteger:forKey:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setKBMenuDismissSource:
+ _objc_msgSend$setKBMenuInteractionSource:
+ _objc_msgSend$setKBMenuSelectedAction:
+ _objc_msgSend$setKeyboardLayout:
+ _objc_msgSend$setKeyboardTrialParameters:
+ _objc_msgSend$setKeyboardType:
+ _objc_msgSend$setKeyboardVariant:
+ _objc_msgSend$setLanguage:
+ _objc_msgSend$setLargestSingleDeletionLength:
+ _objc_msgSend$setLargestSingleInsertionLength:
+ _objc_msgSend$setLastConsumedSignalTimestamp:
+ _objc_msgSend$setMergedActionsCount:
+ _objc_msgSend$setModelInfo:
+ _objc_msgSend$setModelessUsedAtLeastOnceCount:
+ _objc_msgSend$setMultiModalDictationBeganCount:
+ _objc_msgSend$setNetCharacters:
+ _objc_msgSend$setNetEmojiCharacters:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setObjectIfNotNil:forKey:
+ _objc_msgSend$setOptions:
+ _objc_msgSend$setOriginalContent:
+ _objc_msgSend$setOriginalInputMode:
+ _objc_msgSend$setPayload:
+ _objc_msgSend$setPayloadsObservedForTesting:
+ _objc_msgSend$setProcessBundleId:
+ _objc_msgSend$setPunctuationCharacters:
+ _objc_msgSend$setQueue:
+ _objc_msgSend$setRangeAfter:
+ _objc_msgSend$setRegion:
+ _objc_msgSend$setRelativeRangeBefore:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setRemovedEmojiCount:
+ _objc_msgSend$setRemovedTextLength:
+ _objc_msgSend$setRemovedTextLengthWithoutTracking:
+ _objc_msgSend$setReplaceWithCandidateType:
+ _objc_msgSend$setSessionActionsString:
+ _objc_msgSend$setSessionErrors:
+ _objc_msgSend$setSessionHasDictation:
+ _objc_msgSend$setSessionHasOnlyPrimaryInput:
+ _objc_msgSend$setSessionIdentifier:
+ _objc_msgSend$setSessionManagerDelegate:
+ _objc_msgSend$setSignalName:
+ _objc_msgSend$setSource:
+ _objc_msgSend$setTextInputActionsType:
+ _objc_msgSend$setTextInputSessionId:
+ _objc_msgSend$setTextIsTooLong:
+ _objc_msgSend$setTimestamp:
+ _objc_msgSend$setTouchDownPoint:
+ _objc_msgSend$setTouchDuration:
+ _objc_msgSend$setTouchUpPoint:
+ _objc_msgSend$setUiOrientation:
+ _objc_msgSend$setUpdatedInputMode:
+ _objc_msgSend$setUserRemovedCharacters:
+ _objc_msgSend$setUserRemovedEmojiCharacters:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$setWithAlternativesCount:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$sharedCategories
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$sharedPunctuationCharacterSet
+ _objc_msgSend$shouldSeparatelyTrackKeystrokesForSource:type:
+ _objc_msgSend$signalName
+ _objc_msgSend$sortedArrayUsingDescriptors:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$source
+ _objc_msgSend$startDate
+ _objc_msgSend$string
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$stringForKeyboardDockItemButtonPressResult:
+ _objc_msgSend$stringForKeyboardDockItemButtonType:
+ _objc_msgSend$stringForReplaceWithCandidateType:
+ _objc_msgSend$stringForSessionActionsEnum:
+ _objc_msgSend$stringForSource:
+ _objc_msgSend$stringForState:
+ _objc_msgSend$stringForType:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$syncQueue
+ _objc_msgSend$testingDelegate
+ _objc_msgSend$textInputActionsType
+ _objc_msgSend$textInputSessionId
+ _objc_msgSend$textIsTooLong
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$timesUsedInDayRangeFrom:to:
+ _objc_msgSend$timestamp
+ _objc_msgSend$toDictionary
+ _objc_msgSend$type
+ _objc_msgSend$uiOrientation
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$updatedInputMode
+ _objc_msgSend$usedInDayRangeFrom:to:
+ _objc_msgSend$usedInLastNDays:
+ _objc_msgSend$userRemovedCharacters
+ _objc_msgSend$userRemovedEmojiCharacters
+ _objc_msgSend$validateLanguage:
+ _objc_msgSend$validateLanguageHelper:
+ _objc_msgSend$validateRegion:
+ _objc_msgSend$validateRegionHelper:
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$version
+ _objc_msgSend$withAlternativesCount
+ _objc_msgSend$xpcClient
+ _objc_msgSend$xpcEnabled
+ _objc_retain_x26
+ _objc_retain_x28
+ _objectExistsWithName:andType:withError:.onceToken
+ _objectExistsWithName:andType:withError:.validTypes
+ _objectdestroy.7Tm
+ _objectdestroyTm
+ _reportConnectionStatusSuccessful:.onceToken
+ _sharedInstance.onceToken
+ _sharedInstance.sharedInstance
+ _sharedPunctuationCharacterSet.onceToken
+ _sharedPunctuationCharacterSet.punctuationSet
+ _smartRepliesSignalToEnumMap.mapping
+ _smartRepliesSignalToEnumMap.onceToken
+ _swift_beginAccess
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic IeyB_Sg
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic So28IAFeedbackServiceSwiftBridgeC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ So22IAFBKSEvaluationActionV
+ _symbolic _____ So30IAFBKSInteractionFeatureDomainV
+ _symbolic _____Sg 15FeedbackService15FBKSInteractionC16AnnotatedContentV
+ _symbolic _____Sg 15FeedbackService15FBKSInteractionC16AnnotatedContentV8IconTypeO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic ytIeAgHr_
+ _syncQueue.onceToken
+ _validateLanguage:.onceToken
+ _validateLanguage:.seenLanguages
+ _validateLanguageHelper:.onceToken
+ _validateLanguageHelper:.regex
+ _validateRegion:.onceToken
+ _validateRegion:.seenRegions
+ _validateRegionHelper:.onceToken
+ _validateRegionHelper:.regex
+ _xpcEnabled.onceToken
+ _xpcEnabled.shouldXPC
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
CStrings:
+ "%@: ...returning xpcClient 0x%lx"
+ "%@: fetching xpcClient..."
+ "@28@0:8@16B24"
+ "@28@0:8@16f24"
+ "@32@0:8@16B24f28"
+ "AppBackgrounded"
+ "AppForegrounded"
+ "AppInfo"
+ "CTCategories reported error: %@"
+ "CT_%@"
+ "Creativity"
+ "DH0011"
+ "DH0012"
+ "DH0013"
+ "DH1001"
+ "DH1002"
+ "DH1003"
+ "DH1004"
+ "DH1005"
+ "DH1006"
+ "DH1007"
+ "DH1008"
+ "DH1009"
+ "DH1011"
+ "DH1012"
+ "DH1013"
+ "Error"
+ "Event dispatched: '%{private}@' with payload: %{private}@"
+ "Health & Fitness"
+ "IAKeyboardDetection"
+ "IAXPCSPIObject"
+ "Information & Reading"
+ "InputModeDidChange"
+ "KeyboardDismissed"
+ "KeyboardRequested"
+ "LandscapeLeft"
+ "LandscapeRight"
+ "MissingKeyboard"
+ "OrientationWillChange"
+ "Portrait"
+ "PortraitUpsideDown"
+ "Productivity & Finance"
+ "Shopping & Food"
+ "Social"
+ "System"
+ "Timed out waiting for CTCategories."
+ "Travel"
+ "_CTCategoryForBundleId:timeout:"
+ "_lookupAppBundle:useCTCategoryFallback:timeout:"
+ "categoryForBundleID:completionHandler:"
+ "identifier"
+ "isWebKitView"
+ "keyboardIsPresent"
+ "keyboardIsPresent timed out waiting for XPC reply"
+ "keyboardIsPresentWithReply:"
+ "lookupAppBundle:useCTCategoryFallback:"
+ "orientation"
+ "prewarm"
+ "sceneId"
+ "sharedCategories"
+ "userStudiesMode"
+ "v16@?0Q8"
+ "v24@0:8@?<v@?Q>16"
+ "v24@?0@\"CTCategory\"8@\"NSError\"16"
- "IASignalAnalytics: ...returning xpcClient 0x%lx"
- "IASignalAnalytics: fetching xpcClient..."

```
