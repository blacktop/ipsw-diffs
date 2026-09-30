## TipsCore

> `/System/Library/PrivateFrameworks/TipsCore.framework/Versions/A/TipsCore`

```diff

-772.1.0.0.0
-  __TEXT.__text: 0xa1364
-  __TEXT.__auth_stubs: 0x19f0
-  __TEXT.__objc_methlist: 0x8488
-  __TEXT.__const: 0x1620
-  __TEXT.__cstring: 0x5fa3
-  __TEXT.__oslogstring: 0x1204
-  __TEXT.__gcc_except_tab: 0x10b4
+778.4.3.0.0
+  __TEXT.__text: 0x9b2b0
+  __TEXT.__auth_stubs: 0x1a00
+  __TEXT.__objc_methlist: 0x80f4
+  __TEXT.__const: 0x1678
+  __TEXT.__cstring: 0x5663
+  __TEXT.__oslogstring: 0x1205
+  __TEXT.__gcc_except_tab: 0x1080
   __TEXT.__ustring: 0x118
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__constg_swiftt: 0xf90
-  __TEXT.__swift5_typeref: 0xb42
-  __TEXT.__swift5_reflstr: 0xcf2
-  __TEXT.__swift5_fieldmd: 0xab0
+  __TEXT.__constg_swiftt: 0xf30
+  __TEXT.__swift5_typeref: 0xb40
+  __TEXT.__swift5_reflstr: 0xbb2
+  __TEXT.__swift5_fieldmd: 0xa20
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0xd0

   __TEXT.__swift5_capture: 0x500
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2df8
-  __TEXT.__eh_frame: 0xf90
-  __TEXT.__objc_classname: 0xec6
-  __TEXT.__objc_methname: 0xf944
-  __TEXT.__objc_methtype: 0x1a08
-  __TEXT.__objc_stubs: 0x9ba0
-  __DATA_CONST.__got: 0x8a8
-  __DATA_CONST.__const: 0x1388
-  __DATA_CONST.__objc_classlist: 0x4c8
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__unwind_info: 0x2d78
+  __TEXT.__eh_frame: 0x1180
+  __TEXT.__objc_classname: 0xda2
+  __TEXT.__objc_methname: 0xeca1
+  __TEXT.__objc_methtype: 0x184a
+  __TEXT.__objc_stubs: 0x9600
+  __DATA_CONST.__got: 0x890
+  __DATA_CONST.__const: 0x1318
+  __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ad8
-  __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x360
+  __DATA_CONST.__objc_selrefs: 0x3980
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0xd08
-  __AUTH_CONST.__const: 0x3980
-  __AUTH_CONST.__cfstring: 0x5780
-  __AUTH_CONST.__objc_const: 0xea08
-  __AUTH_CONST.__objc_intobj: 0x3d8
+  __AUTH_CONST.__auth_got: 0xd10
+  __AUTH_CONST.__const: 0x36b0
+  __AUTH_CONST.__cfstring: 0x53c0
+  __AUTH_CONST.__objc_const: 0xd318
+  __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x3da0
+  __AUTH.__objc_data: 0x3a20
   __AUTH.__data: 0x920
-  __DATA.__objc_ivar: 0x838
-  __DATA.__data: 0x12d0
-  __DATA.__bss: 0x1d30
+  __DATA.__objc_ivar: 0x7a4
+  __DATA.__data: 0x11a0
+  __DATA.__bss: 0x1d20
   __DATA.__common: 0x38
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 675E53DF-B942-35D0-8E51-355BD4E0764F
-  Functions: 4715
-  Symbols:   7322
-  CStrings:  5129
+  UUID: F53DDB81-12BB-3C22-9042-E94AB7E12BCB
+  Functions: 4537
+  Symbols:   6992
+  CStrings:  4896
 
Symbols:
+ +[TPSAnalyticsCommonDefines ineligibleReasonStringForReason:].cold.2
+ +[TPSAnalyticsEventAppLaunched _currentSessionEvents].cold.1
+ +[TPSAnalyticsEventController sharedInstance].cold.1
+ +[TPSAnalyticsEventSearchResultSelected eventWithSearchID:searchTerm:topicID:bookID:bookSlug:]
+ +[TPSAppController sharedInstance].cold.1
+ +[TPSAssetCacheController sharedInstance].cold.1
+ +[TPSCloudController sharedInstance].cold.1
+ +[TPSCommonDefines deviceClass].cold.1
+ +[TPSCommonDefines isGreenTeaDevice].cold.1
+ +[TPSCommonDefines isSeniorUser].cold.1
+ +[TPSCommonDefines mainBundleIdentifier].cold.1
+ +[TPSCommonDefines osBuild].cold.1
+ +[TPSCommonDefines sharedInstance].cold.1
+ +[TPSContentURLController _uiTestLocalBaseURL].cold.1
+ +[TPSDataCacheController sharedInstance].cold.1
+ +[TPSEventsProviderManager defaultManager].cold.1
+ +[TPSFeatureFlags allowsDE].cold.1
+ +[TPSFeatureFlags allowsTipsSharing].cold.1
+ +[TPSJSONCacheController sharedInstance].cold.1
+ +[TPSSecureArchivingUtilities syncQueue].cold.1
+ +[TPSStringCacheController sharedInstance].cold.1
+ +[TPSURLActionComponents _actionTypeForString:].cold.1
+ +[TPSURLSessionACAuthContext defaultContext].cold.1
+ +[TPSURLSessionACAuthHandler canAuthenticateWithURLResponse:].cold.1
+ +[TPSURLSessionHandler sharedInstance].cold.1
+ +[TPSURLSessionManager defaultManager].cold.1
+ -[TPSAnalyticsEventController analyticsQueue].cold.1
+ -[TPSAnalyticsEventSearchResultSelected _initWithSearchID:searchTerm:topic_id:book_id:book_slug:]
+ -[TPSAnalyticsEventSearchResultSelected bookID]
+ -[TPSAnalyticsEventSearchResultSelected bookSlug]
+ -[TPSAnalyticsEventSearchResultSelected setBookID:]
+ -[TPSAnalyticsEventSearchResultSelected setBookSlug:]
+ -[TPSAnalyticsEventSearchResultSelected setTopicID:]
+ -[TPSAnalyticsEventSearchResultSelected topicID]
+ -[TPSCommonDefines userType].cold.1
+ -[TPSTipStatus isHintIneligible]
+ -[TPSTipStatusController hintIneligibleReasonForIdentifier:]
+ -[TPSTipStatusController isHintIneligibleForIdentifier:]
+ -[TPSTipStatusController isHintIneligibleForReason:identifier:]
+ -[TPSTipStatusController updateHintIneligibleForIdentifier:value:]
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table62
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table72
+ GCC_except_table74
+ OBJC_IVAR_$_TPSAnalyticsEventSearchResultSelected._bookID
+ OBJC_IVAR_$_TPSAnalyticsEventSearchResultSelected._bookSlug
+ OBJC_IVAR_$_TPSAnalyticsEventSearchResultSelected._topicID
+ __22+[TPSSize na_identity]_block_invoke.cold.1
+ __23+[TPSSizes na_identity]_block_invoke.cold.1
+ __24+[TPSAssets na_identity]_block_invoke.cold.1
+ __25+[TPSContent na_identity]_block_invoke.cold.1
+ __26+[TPSDocument na_identity]_block_invoke.cold.1
+ __26+[TPSGradient na_identity]_block_invoke.cold.1
+ __30+[TPSGradientStop na_identity]_block_invoke.cold.1
+ __30+[TPSNotification na_identity]_block_invoke.cold.1
+ __31+[TPSAssetFileInfo na_identity]_block_invoke.cold.1
+ __38+[TPSAssetFileInfoManager na_identity]_block_invoke.cold.1
+ __OBJC_$_INSTANCE_METHODS_TPSAppController(TPSAppController)
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ _objc_msgSend$_initWithSearchID:searchTerm:topic_id:book_id:book_slug:
+ _objc_msgSend$isHintIneligible
+ _objc_msgSend$updateHintIneligibleForIdentifier:value:
+ _swift_allocBox
+ _symbolic SS3key_yp5valuet
- +[TPSAnalyticsEventContentEligibilityMet eventWithContentID:bundleID:eligibleContext:displayType:usageFlags:date:]
- +[TPSAnalyticsEventContentEligibilityMet supportsSecureCoding]
- +[TPSAnalyticsEventTipDismissed eventWithTipID:correlationID:bundleID:context:dismissType:timeToDismissal:date:]
- +[TPSAnalyticsEventTipDismissed supportsSecureCoding]
- +[TPSAnalyticsEventTipReadyToBeDisplayed eventWithTipID:correlationID:]
- +[TPSAnalyticsEventTipReadyToBeDisplayed eventWithTipID:correlationID:bundleID:context:displayType:]
- +[TPSAnalyticsEventTipReadyToBeDisplayed supportsSecureCoding]
- +[TPSAnalyticsEventTipTapped eventWithTipID:correlationID:]
- +[TPSAnalyticsEventTipTapped eventWithTipID:correlationID:bundleID:context:]
- +[TPSAnalyticsEventTipTapped supportsSecureCoding]
- +[TPSContextualPortraitEvent supportsSecureCoding]
- +[TPSDiscoverabilityTip supportsSecureCoding]
- +[TPSFeatureFlags allowsPersistentSiri]
- +[TPSMiniTipMetadata supportsSecureCoding]
- +[TPSMonitoringEvents supportsSecureCoding]
- -[TPSAnalyticsDataProvider bundleIDForIdentifier:]
- -[TPSAnalyticsEventContentEligibilityMet .cxx_destruct]
- -[TPSAnalyticsEventContentEligibilityMet _initWithContentID:bundleID:eligibleContext:displayType:usageFlags:date:]
- -[TPSAnalyticsEventContentEligibilityMet bundleID]
- -[TPSAnalyticsEventContentEligibilityMet contentID]
- -[TPSAnalyticsEventContentEligibilityMet displayType]
- -[TPSAnalyticsEventContentEligibilityMet eligibleContext]
- -[TPSAnalyticsEventContentEligibilityMet encodeWithCoder:]
- -[TPSAnalyticsEventContentEligibilityMet eventName]
- -[TPSAnalyticsEventContentEligibilityMet initWithCoder:]
- -[TPSAnalyticsEventContentEligibilityMet mutableAnalyticsEventRepresentation]
- -[TPSAnalyticsEventContentEligibilityMet usageFlags]
- -[TPSAnalyticsEventTipDismissed .cxx_destruct]
- -[TPSAnalyticsEventTipDismissed _initWithTipID:correlationID:bundleID:context:dismissType:timeToDismissal:date:]
- -[TPSAnalyticsEventTipDismissed bundleID]
- -[TPSAnalyticsEventTipDismissed context]
- -[TPSAnalyticsEventTipDismissed correlationID]
- -[TPSAnalyticsEventTipDismissed dismissType]
- -[TPSAnalyticsEventTipDismissed displayCount]
- -[TPSAnalyticsEventTipDismissed encodeWithCoder:]
- -[TPSAnalyticsEventTipDismissed eventName]
- -[TPSAnalyticsEventTipDismissed initWithCoder:]
- -[TPSAnalyticsEventTipDismissed mutableAnalyticsEventRepresentation]
- -[TPSAnalyticsEventTipDismissed setDataProvider:]
- -[TPSAnalyticsEventTipDismissed setDisplayCount:]
- -[TPSAnalyticsEventTipDismissed setTimeToDismissal:]
- -[TPSAnalyticsEventTipDismissed timeToDismissal]
- -[TPSAnalyticsEventTipDismissed tipID]
- -[TPSAnalyticsEventTipReadyToBeDisplayed .cxx_destruct]
- -[TPSAnalyticsEventTipReadyToBeDisplayed _initWithTipID:correlationID:]
- -[TPSAnalyticsEventTipReadyToBeDisplayed _initWithTipID:correlationID:bundleID:context:displayType:]
- -[TPSAnalyticsEventTipReadyToBeDisplayed bundleID]
- -[TPSAnalyticsEventTipReadyToBeDisplayed context]
- -[TPSAnalyticsEventTipReadyToBeDisplayed correlationID]
- -[TPSAnalyticsEventTipReadyToBeDisplayed displayType]
- -[TPSAnalyticsEventTipReadyToBeDisplayed encodeWithCoder:]
- -[TPSAnalyticsEventTipReadyToBeDisplayed eventName]
- -[TPSAnalyticsEventTipReadyToBeDisplayed initWithCoder:]
- -[TPSAnalyticsEventTipReadyToBeDisplayed mutableAnalyticsEventRepresentation]
- -[TPSAnalyticsEventTipReadyToBeDisplayed setBundleID:]
- -[TPSAnalyticsEventTipReadyToBeDisplayed setContext:]
- -[TPSAnalyticsEventTipReadyToBeDisplayed setCorrelationID:]
- -[TPSAnalyticsEventTipReadyToBeDisplayed setDataProvider:]
- -[TPSAnalyticsEventTipReadyToBeDisplayed setDisplayType:]
- -[TPSAnalyticsEventTipReadyToBeDisplayed setTipID:]
- -[TPSAnalyticsEventTipReadyToBeDisplayed tipID]
- -[TPSAnalyticsEventTipTapped .cxx_destruct]
- -[TPSAnalyticsEventTipTapped _initWithTipID:correlationID:]
- -[TPSAnalyticsEventTipTapped _initWithTipID:correlationID:bundleID:context:]
- -[TPSAnalyticsEventTipTapped bundleID]
- -[TPSAnalyticsEventTipTapped context]
- -[TPSAnalyticsEventTipTapped correlationID]
- -[TPSAnalyticsEventTipTapped displayType]
- -[TPSAnalyticsEventTipTapped encodeWithCoder:]
- -[TPSAnalyticsEventTipTapped eventName]
- -[TPSAnalyticsEventTipTapped initWithCoder:]
- -[TPSAnalyticsEventTipTapped mutableAnalyticsEventRepresentation]
- -[TPSAnalyticsEventTipTapped setBundleID:]
- -[TPSAnalyticsEventTipTapped setContext:]
- -[TPSAnalyticsEventTipTapped setCorrelationID:]
- -[TPSAnalyticsEventTipTapped setDataProvider:]
- -[TPSAnalyticsEventTipTapped setTipID:]
- -[TPSAnalyticsEventTipTapped tipID]
- -[TPSContextualPortraitEvent .cxx_destruct]
- -[TPSContextualPortraitEvent confidenceThreshold]
- -[TPSContextualPortraitEvent copyWithZone:]
- -[TPSContextualPortraitEvent debugDescription]
- -[TPSContextualPortraitEvent encodeWithCoder:]
- -[TPSContextualPortraitEvent initWithCoder:]
- -[TPSContextualPortraitEvent initWithDictionary:]
- -[TPSContextualPortraitEvent minObservationCount]
- -[TPSContextualPortraitEvent setConfidenceThreshold:]
- -[TPSContextualPortraitEvent setTopicID:]
- -[TPSContextualPortraitEvent topicID]
- -[TPSDiscoverabilityTip .cxx_destruct]
- -[TPSDiscoverabilityTip attributedString]
- -[TPSDiscoverabilityTip copyWithZone:]
- -[TPSDiscoverabilityTip debugDescription]
- -[TPSDiscoverabilityTip encodeWithCoder:]
- -[TPSDiscoverabilityTip initWithCoder:]
- -[TPSDiscoverabilityTip isLocalContent]
- -[TPSDiscoverabilityTip preconditions]
- -[TPSDiscoverabilityTip setAttributedString:]
- -[TPSDiscoverabilityTip setLocalContent:]
- -[TPSDiscoverabilityTip setPreconditions:]
- -[TPSMiniTipContentManager .cxx_destruct]
- -[TPSMiniTipContentManager _actionCompletionOnClientQueue:]
- -[TPSMiniTipContentManager _contentWithContentIDCompletionOnClientQueue:]
- -[TPSMiniTipContentManager _performSyncWithProxyHandler:errorHandler:]
- -[TPSMiniTipContentManager _performWithProxyHandler:errorHandler:]
- -[TPSMiniTipContentManager clientQueue]
- -[TPSMiniTipContentManager contentWithContentIdentifiers:bundleID:context:completionHandler:]
- -[TPSMiniTipContentManager hintDismissedForIdentifier:bundleID:context:reason:]
- -[TPSMiniTipContentManager hintDisplayedForIdentifier:correlationID:context:]
- -[TPSMiniTipContentManager init]
- -[TPSMiniTipContentManager invalidate]
- -[TPSMiniTipContentManager personalizationFailedForContentID:bundleID:context:]
- -[TPSMiniTipContentManager restartTrackingForContentIdentifiers:]
- -[TPSMiniTipContentManager serviceProxy]
- -[TPSMiniTipContentManager setClientQueue:]
- -[TPSMiniTipContentManager setServiceProxy:]
- -[TPSMiniTipContentManager validateAndPrepareContentForDisplay:bundleID:context:synchronous:skipUsageCheck:completionHandler:]
- -[TPSMiniTipMetadata .cxx_destruct]
- -[TPSMiniTipMetadata content]
- -[TPSMiniTipMetadata copyWithZone:]
- -[TPSMiniTipMetadata customizationID]
- -[TPSMiniTipMetadata debugDescription]
- -[TPSMiniTipMetadata description]
- -[TPSMiniTipMetadata encodeWithCoder:]
- -[TPSMiniTipMetadata error]
- -[TPSMiniTipMetadata identifier]
- -[TPSMiniTipMetadata initWithCoder:]
- -[TPSMiniTipMetadata initWithContent:]
- -[TPSMiniTipMetadata monitoringEvents]
- -[TPSMiniTipMetadata setContent:]
- -[TPSMiniTipMetadata setCustomizationID:]
- -[TPSMiniTipMetadata setError:]
- -[TPSMiniTipMetadata setMonitoringEvents:]
- -[TPSMiniTipMetadata setUserInfo:]
- -[TPSMiniTipMetadata userInfo]
- -[TPSMonitoringEvents .cxx_destruct]
- -[TPSMonitoringEvents autoDismissEvents]
- -[TPSMonitoringEvents clientContextEventsForMap:]
- -[TPSMonitoringEvents clientContextKeysForEventOptions:]
- -[TPSMonitoringEvents clientContextKeysForMap:]
- -[TPSMonitoringEvents copyWithZone:]
- -[TPSMonitoringEvents debugDescription]
- -[TPSMonitoringEvents desiredOutcomeEventMap]
- -[TPSMonitoringEvents dismissalEventMap]
- -[TPSMonitoringEvents displayEventMap]
- -[TPSMonitoringEvents encodeWithCoder:]
- -[TPSMonitoringEvents eventMapFromMonitoringEventsDictionary:]
- -[TPSMonitoringEvents eventOptionsForEventIdentifier:]
- -[TPSMonitoringEvents hasClientContextKeysForEventOptions:]
- -[TPSMonitoringEvents hasEvents]
- -[TPSMonitoringEvents hasRegistrableContextualEventsForEventOptions:]
- -[TPSMonitoringEvents initWithCoder:]
- -[TPSMonitoringEvents initWithDictionary:desiredOutcomeDictionary:]
- -[TPSMonitoringEvents initialDisplayEventMap]
- -[TPSMonitoringEvents registrableContextualEventsForEventOptions:type:]
- -[TPSMonitoringEvents registrableContextualEventsForMap:type:]
- -[TPSMonitoringEvents restartTrackingDisplayEventMap]
- -[TPSMonitoringEvents restartTrackingTriggerEventMap]
- -[TPSMonitoringEvents setDesiredOutcomeEventMap:]
- -[TPSMonitoringEvents setDismissalEventMap:]
- -[TPSMonitoringEvents setDisplayEventMap:]
- -[TPSMonitoringEvents setInitialDisplayEventMap:]
- -[TPSMonitoringEvents setRestartTrackingDisplayEventMap:]
- -[TPSMonitoringEvents setRestartTrackingTriggerEventMap:]
- -[TPSTipStatus isHintInelgibile]
- -[TPSTipStatusController hintInelgibileReasonForIdentifier:]
- -[TPSTipStatusController isHintInelgibileForIdentifier:]
- -[TPSTipStatusController isHintInelgibileForReason:identifier:]
- -[TPSTipStatusController isHintMaxDurationExcceededForIdentifier:]
- -[TPSTipStatusController updateHintInelgibileForIdentifier:value:]
- GCC_except_table29
- GCC_except_table36
- GCC_except_table38
- GCC_except_table40
- GCC_except_table42
- GCC_except_table44
- GCC_except_table46
- GCC_except_table49
- GCC_except_table51
- GCC_except_table53
- GCC_except_table56
- GCC_except_table58
- GCC_except_table63
- GCC_except_table69
- GCC_except_table73
- GCC_except_table75
- GCC_except_table84
- OBJC_IVAR_$_TPSAnalyticsEventContentEligibilityMet._bundleID
- OBJC_IVAR_$_TPSAnalyticsEventContentEligibilityMet._contentID
- OBJC_IVAR_$_TPSAnalyticsEventContentEligibilityMet._displayType
- OBJC_IVAR_$_TPSAnalyticsEventContentEligibilityMet._eligibleContext
- OBJC_IVAR_$_TPSAnalyticsEventContentEligibilityMet._usageFlags
- OBJC_IVAR_$_TPSAnalyticsEventTipDismissed._bundleID
- OBJC_IVAR_$_TPSAnalyticsEventTipDismissed._context
- OBJC_IVAR_$_TPSAnalyticsEventTipDismissed._correlationID
- OBJC_IVAR_$_TPSAnalyticsEventTipDismissed._dismissType
- OBJC_IVAR_$_TPSAnalyticsEventTipDismissed._displayCount
- OBJC_IVAR_$_TPSAnalyticsEventTipDismissed._timeToDismissal
- OBJC_IVAR_$_TPSAnalyticsEventTipDismissed._tipID
- OBJC_IVAR_$_TPSAnalyticsEventTipReadyToBeDisplayed._bundleID
- OBJC_IVAR_$_TPSAnalyticsEventTipReadyToBeDisplayed._context
- OBJC_IVAR_$_TPSAnalyticsEventTipReadyToBeDisplayed._correlationID
- OBJC_IVAR_$_TPSAnalyticsEventTipReadyToBeDisplayed._displayType
- OBJC_IVAR_$_TPSAnalyticsEventTipReadyToBeDisplayed._tipID
- OBJC_IVAR_$_TPSAnalyticsEventTipTapped._bundleID
- OBJC_IVAR_$_TPSAnalyticsEventTipTapped._context
- OBJC_IVAR_$_TPSAnalyticsEventTipTapped._correlationID
- OBJC_IVAR_$_TPSAnalyticsEventTipTapped._displayType
- OBJC_IVAR_$_TPSAnalyticsEventTipTapped._tipID
- OBJC_IVAR_$_TPSContextualPortraitEvent._confidenceThreshold
- OBJC_IVAR_$_TPSContextualPortraitEvent._topicID
- OBJC_IVAR_$_TPSDiscoverabilityTip._attributedString
- OBJC_IVAR_$_TPSDiscoverabilityTip._localContent
- OBJC_IVAR_$_TPSDiscoverabilityTip._preconditions
- OBJC_IVAR_$_TPSMiniTipContentManager._clientQueue
- OBJC_IVAR_$_TPSMiniTipContentManager._serviceProxy
- OBJC_IVAR_$_TPSMiniTipMetadata._content
- OBJC_IVAR_$_TPSMiniTipMetadata._customizationID
- OBJC_IVAR_$_TPSMiniTipMetadata._error
- OBJC_IVAR_$_TPSMiniTipMetadata._monitoringEvents
- OBJC_IVAR_$_TPSMiniTipMetadata._userInfo
- OBJC_IVAR_$_TPSMonitoringEvents._desiredOutcomeEventMap
- OBJC_IVAR_$_TPSMonitoringEvents._dismissalEventMap
- OBJC_IVAR_$_TPSMonitoringEvents._displayEventMap
- OBJC_IVAR_$_TPSMonitoringEvents._initialDisplayEventMap
- OBJC_IVAR_$_TPSMonitoringEvents._restartTrackingDisplayEventMap
- OBJC_IVAR_$_TPSMonitoringEvents._restartTrackingTriggerEventMap
- _OBJC_CLASS_$_TPSAnalyticsEventContentEligibilityMet
- _OBJC_CLASS_$_TPSAnalyticsEventTipDismissed
- _OBJC_CLASS_$_TPSAnalyticsEventTipReadyToBeDisplayed
- _OBJC_CLASS_$_TPSAnalyticsEventTipTapped
- _OBJC_CLASS_$_TPSContextualPortraitEvent
- _OBJC_CLASS_$_TPSDiscoverabilityTip
- _OBJC_CLASS_$_TPSMiniTipContentManager
- _OBJC_CLASS_$_TPSMiniTipMetadata
- _OBJC_CLASS_$_TPSMonitoringEvents
- _OBJC_METACLASS_$_TPSAnalyticsEventContentEligibilityMet
- _OBJC_METACLASS_$_TPSAnalyticsEventTipDismissed
- _OBJC_METACLASS_$_TPSAnalyticsEventTipReadyToBeDisplayed
- _OBJC_METACLASS_$_TPSAnalyticsEventTipTapped
- _OBJC_METACLASS_$_TPSContextualPortraitEvent
- _OBJC_METACLASS_$_TPSDiscoverabilityTip
- _OBJC_METACLASS_$_TPSMiniTipContentManager
- _OBJC_METACLASS_$_TPSMiniTipMetadata
- _OBJC_METACLASS_$_TPSMonitoringEvents
- _OUTLINED_FUNCTION_3
- _TPSAnalyticsDismissTypeByClient
- _TPSAnalyticsDismissTypeByUser
- _TPSAnalyticsDismissTypeDesiredOutcome
- _TPSAnalyticsDismissTypeDismissalEventOccurred
- _TPSAnalyticsDismissTypeHintMaxDisplayedCountExceeded
- _TPSAnalyticsDismissTypeHintMaxDurationExceeded
- _TPSAnalyticsDismissTypeRestartTrackingDisplayEventOccurred
- _TPSAnalyticsDismissTypeUnknown
- _TPSMiniTipContentManagerServiceInterfaceServerInterface
- _TPSMonitoringEventsKey
- _TPSTipStatusControllerHintMaxDurationTimeInterval
- _TPSWidgetAssertionCreated
- __126-[TPSMiniTipContentManager validateAndPrepareContentForDisplay:bundleID:context:synchronous:skipUsageCheck:completionHandler:]_block_invoke.6
- __126-[TPSMiniTipContentManager validateAndPrepareContentForDisplay:bundleID:context:synchronous:skipUsageCheck:completionHandler:]_block_invoke.9
- __126-[TPSMiniTipContentManager validateAndPrepareContentForDisplay:bundleID:context:synchronous:skipUsageCheck:completionHandler:]_block_invoke_2.10
- __65-[TPSMiniTipContentManager restartTrackingForContentIdentifiers:]_block_invoke.20
- __79-[TPSMiniTipContentManager hintDismissedForIdentifier:bundleID:context:reason:]_block_invoke.16
- __79-[TPSMiniTipContentManager personalizationFailedForContentID:bundleID:context:]_block_invoke.11
- __93-[TPSMiniTipContentManager contentWithContentIdentifiers:bundleID:context:completionHandler:]_block_invoke.2
- __OBJC_$_CLASS_METHODS_TPSAnalyticsEventContentEligibilityMet
- __OBJC_$_CLASS_METHODS_TPSAnalyticsEventTipDismissed
- __OBJC_$_CLASS_METHODS_TPSAnalyticsEventTipReadyToBeDisplayed
- __OBJC_$_CLASS_METHODS_TPSAnalyticsEventTipTapped
- __OBJC_$_CLASS_METHODS_TPSContextualPortraitEvent
- __OBJC_$_CLASS_METHODS_TPSDiscoverabilityTip
- __OBJC_$_CLASS_METHODS_TPSMiniTipMetadata
- __OBJC_$_CLASS_METHODS_TPSMonitoringEvents
- __OBJC_$_CLASS_PROP_LIST_TPSMiniTipMetadata
- __OBJC_$_INSTANCE_METHODS_TPSAnalyticsEventContentEligibilityMet
- __OBJC_$_INSTANCE_METHODS_TPSAnalyticsEventTipDismissed
- __OBJC_$_INSTANCE_METHODS_TPSAnalyticsEventTipReadyToBeDisplayed
- __OBJC_$_INSTANCE_METHODS_TPSAnalyticsEventTipTapped
- __OBJC_$_INSTANCE_METHODS_TPSAppController(TipsCore)
- __OBJC_$_INSTANCE_METHODS_TPSContextualPortraitEvent
- __OBJC_$_INSTANCE_METHODS_TPSDiscoverabilityTip
- __OBJC_$_INSTANCE_METHODS_TPSMiniTipContentManager
- __OBJC_$_INSTANCE_METHODS_TPSMiniTipMetadata
- __OBJC_$_INSTANCE_METHODS_TPSMonitoringEvents
- __OBJC_$_INSTANCE_VARIABLES_TPSAnalyticsEventContentEligibilityMet
- __OBJC_$_INSTANCE_VARIABLES_TPSAnalyticsEventTipDismissed
- __OBJC_$_INSTANCE_VARIABLES_TPSAnalyticsEventTipReadyToBeDisplayed
- __OBJC_$_INSTANCE_VARIABLES_TPSAnalyticsEventTipTapped
- __OBJC_$_INSTANCE_VARIABLES_TPSContextualPortraitEvent
- __OBJC_$_INSTANCE_VARIABLES_TPSDiscoverabilityTip
- __OBJC_$_INSTANCE_VARIABLES_TPSMiniTipContentManager
- __OBJC_$_INSTANCE_VARIABLES_TPSMiniTipMetadata
- __OBJC_$_INSTANCE_VARIABLES_TPSMonitoringEvents
- __OBJC_$_PROP_LIST_TPSAnalyticsEventContentEligibilityMet
- __OBJC_$_PROP_LIST_TPSAnalyticsEventTipDismissed
- __OBJC_$_PROP_LIST_TPSAnalyticsEventTipReadyToBeDisplayed
- __OBJC_$_PROP_LIST_TPSAnalyticsEventTipTapped
- __OBJC_$_PROP_LIST_TPSContextualPortraitEvent
- __OBJC_$_PROP_LIST_TPSDiscoverabilityTip
- __OBJC_$_PROP_LIST_TPSMiniTipContentManager
- __OBJC_$_PROP_LIST_TPSMiniTipMetadata
- __OBJC_$_PROP_LIST_TPSMonitoringEvents
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TPSMiniTipContentManagerServiceInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_TPSMiniTipContentManagerServiceInterface
- __OBJC_$_PROTOCOL_REFS_TPSMiniTipContentManagerServiceInterface
- __OBJC_CLASS_PROTOCOLS_$_TPSMiniTipMetadata
- __OBJC_CLASS_RO_$_TPSAnalyticsEventContentEligibilityMet
- __OBJC_CLASS_RO_$_TPSAnalyticsEventTipDismissed
- __OBJC_CLASS_RO_$_TPSAnalyticsEventTipReadyToBeDisplayed
- __OBJC_CLASS_RO_$_TPSAnalyticsEventTipTapped
- __OBJC_CLASS_RO_$_TPSContextualPortraitEvent
- __OBJC_CLASS_RO_$_TPSDiscoverabilityTip
- __OBJC_CLASS_RO_$_TPSMiniTipContentManager
- __OBJC_CLASS_RO_$_TPSMiniTipMetadata
- __OBJC_CLASS_RO_$_TPSMonitoringEvents
- __OBJC_LABEL_PROTOCOL_$_TPSMiniTipContentManagerServiceInterface
- __OBJC_METACLASS_RO_$_TPSAnalyticsEventContentEligibilityMet
- __OBJC_METACLASS_RO_$_TPSAnalyticsEventTipDismissed
- __OBJC_METACLASS_RO_$_TPSAnalyticsEventTipReadyToBeDisplayed
- __OBJC_METACLASS_RO_$_TPSAnalyticsEventTipTapped
- __OBJC_METACLASS_RO_$_TPSContextualPortraitEvent
- __OBJC_METACLASS_RO_$_TPSDiscoverabilityTip
- __OBJC_METACLASS_RO_$_TPSMiniTipContentManager
- __OBJC_METACLASS_RO_$_TPSMiniTipMetadata
- __OBJC_METACLASS_RO_$_TPSMonitoringEvents
- __OBJC_PROTOCOL_$_TPSMiniTipContentManagerServiceInterface
- __OBJC_PROTOCOL_REFERENCE_$_TPSMiniTipContentManagerServiceInterface
- ___126-[TPSMiniTipContentManager validateAndPrepareContentForDisplay:bundleID:context:synchronous:skipUsageCheck:completionHandler:]_block_invoke
- ___126-[TPSMiniTipContentManager validateAndPrepareContentForDisplay:bundleID:context:synchronous:skipUsageCheck:completionHandler:]_block_invoke_2
- ___126-[TPSMiniTipContentManager validateAndPrepareContentForDisplay:bundleID:context:synchronous:skipUsageCheck:completionHandler:]_block_invoke_3
- ___39+[TPSFeatureFlags allowsPersistentSiri]_block_invoke
- ___59-[TPSMiniTipContentManager _actionCompletionOnClientQueue:]_block_invoke
- ___59-[TPSMiniTipContentManager _actionCompletionOnClientQueue:]_block_invoke_2
- ___65-[TPSMiniTipContentManager restartTrackingForContentIdentifiers:]_block_invoke
- ___73-[TPSMiniTipContentManager _contentWithContentIDCompletionOnClientQueue:]_block_invoke
- ___73-[TPSMiniTipContentManager _contentWithContentIDCompletionOnClientQueue:]_block_invoke_2
- ___77-[TPSMiniTipContentManager hintDisplayedForIdentifier:correlationID:context:]_block_invoke
- ___77-[TPSMiniTipContentManager hintDisplayedForIdentifier:correlationID:context:]_block_invoke_2
- ___79-[TPSMiniTipContentManager hintDismissedForIdentifier:bundleID:context:reason:]_block_invoke
- ___79-[TPSMiniTipContentManager personalizationFailedForContentID:bundleID:context:]_block_invoke
- ___93-[TPSMiniTipContentManager contentWithContentIdentifiers:bundleID:context:completionHandler:]_block_invoke
- ___block_descriptor_40_e8_32bs_e52_v16?0"<TPSMiniTipContentManagerServiceInterface>"8l
- ___block_descriptor_40_e8_32s_e52_v16?0"<TPSMiniTipContentManagerServiceInterface>"8l
- ___block_descriptor_48_e8_32s40bs_e23_v28?0B812"NSError"20l
- ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48s_e52_v16?0"<TPSMiniTipContentManagerServiceInterface>"8l
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0l
- ___block_descriptor_64_e8_32s40s48s56bs_e52_v16?0"<TPSMiniTipContentManagerServiceInterface>"8l
- ___block_descriptor_64_e8_32s40s48s_e52_v16?0"<TPSMiniTipContentManagerServiceInterface>"8l
- ___block_descriptor_65_e8_32s40s48s56bs_e52_v16?0"<TPSMiniTipContentManagerServiceInterface>"8l
- __block_literal_global.18
- _kTPSMiniTipContentManagerServiceInterfaceErrorDomain
- _kTipsAnalyticsDisplayTypeMiniHintString
- _kTipsEventHintReadyToBeDisplayed
- _kTipsMiniTipTappedKey
- _kTipsTipDismissedKey
- _objc_msgSend$_contentWithContentIDCompletionOnClientQueue:
- _objc_msgSend$_initWithContentID:bundleID:eligibleContext:displayType:usageFlags:date:
- _objc_msgSend$_initWithTipID:correlationID:
- _objc_msgSend$_initWithTipID:correlationID:bundleID:context:
- _objc_msgSend$_initWithTipID:correlationID:bundleID:context:dismissType:timeToDismissal:date:
- _objc_msgSend$_initWithTipID:correlationID:bundleID:context:displayType:
- _objc_msgSend$_performSyncWithProxyHandler:errorHandler:
- _objc_msgSend$bundleIDForIdentifier:
- _objc_msgSend$clientContextKeys
- _objc_msgSend$clientContextKeysForEventOptions:
- _objc_msgSend$clientContextKeysForMap:
- _objc_msgSend$content
- _objc_msgSend$contentWithContentIdentifiers:bundleID:context:completionHandler:
- _objc_msgSend$customizationID
- _objc_msgSend$desiredOutcomeEventMap
- _objc_msgSend$dismissalEventMap
- _objc_msgSend$displayEventMap
- _objc_msgSend$eventMapFromMonitoringEventsDictionary:
- _objc_msgSend$eventsForConditionDictionary:
- _objc_msgSend$hasEvents
- _objc_msgSend$hintDismissedForIdentifier:bundleID:context:reason:
- _objc_msgSend$hintDisplayedForIdentifier:correlationID:context:
- _objc_msgSend$hintMaxDurationTimeInterval
- _objc_msgSend$initialDisplayEventMap
- _objc_msgSend$isHintInelgibile
- _objc_msgSend$monitoringEvents
- _objc_msgSend$personalizationFailedForContentID:bundleID:context:
- _objc_msgSend$registrableContextualEventsForEventOptions:type:
- _objc_msgSend$registrableContextualEventsForMap:type:
- _objc_msgSend$restartTrackingDisplayEventMap
- _objc_msgSend$restartTrackingForContentIdentifiers:
- _objc_msgSend$restartTrackingTriggerEventMap
- _objc_msgSend$setConfidenceThreshold:
- _objc_msgSend$setContent:
- _objc_msgSend$setCustomizationID:
- _objc_msgSend$setDesiredOutcomeEventMap:
- _objc_msgSend$setDismissalEventMap:
- _objc_msgSend$setDisplayEventMap:
- _objc_msgSend$setError:
- _objc_msgSend$setInitialDisplayEventMap:
- _objc_msgSend$setLocalContent:
- _objc_msgSend$setMonitoringEvents:
- _objc_msgSend$setPreconditions:
- _objc_msgSend$setRestartTrackingDisplayEventMap:
- _objc_msgSend$setRestartTrackingTriggerEventMap:
- _objc_msgSend$setTopicID:
- _objc_msgSend$updateHintInelgibileForIdentifier:value:
- _objc_msgSend$validateAndPrepareContentForDisplay:bundleID:context:skipUsageCheck:completionHandler:
- _swift_arrayDestroy
- _symbolic SS3key_yp5valuetSg
- allowsPersistentSiri.allowFeature
- allowsPersistentSiri.predicate
CStrings:
+ "Add observerIdentifier %@ to map %@ for event identifier %@"
+ "T@\"NSString\",C,N,V_bookID"
+ "T@\"NSString\",C,N,V_bookSlug"
+ "TB,R,N,GisHintIneligible"
+ "__swift_objectForKeyedSubscript:"
+ "_bookID"
+ "_bookSlug"
+ "_initWithSearchID:searchTerm:topic_id:book_id:book_slug:"
+ "bookID"
+ "bookSlug"
+ "book_id"
+ "book_slug"
+ "eventWithSearchID:searchTerm:topicID:bookID:bookSlug:"
+ "hintIneligible"
+ "hintIneligibleReasonForIdentifier:"
+ "isHintIneligible"
+ "isHintIneligibleForIdentifier:"
+ "isHintIneligibleForReason:identifier:"
+ "setBookID:"
+ "setBookSlug:"
+ "topic_id"
+ "updateHintIneligibleForIdentifier:value:"
- "%@ = %lf\n"
- "@\"NSAttributedString\""
- "@\"TPSMonitoringEvents\""
- "@32@0:8Q16q24"
- "@64@0:8@16@24@32Q40Q48@56"
- "@72@0:8@16@24@32@40@48d56@64"
- "Add observerIdentifer %@ to map %@ for event identifier %@"
- "B24@0:8Q16"
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "SiriUI"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"NSArray\",R,N,V_eligibleContext"
- "T@\"NSAttributedString\",&,N,V_attributedString"
- "T@\"NSDictionary\",C,N,V_desiredOutcomeEventMap"
- "T@\"NSDictionary\",C,N,V_dismissalEventMap"
- "T@\"NSDictionary\",C,N,V_displayEventMap"
- "T@\"NSDictionary\",C,N,V_initialDisplayEventMap"
- "T@\"NSDictionary\",C,N,V_preconditions"
- "T@\"NSDictionary\",C,N,V_restartTrackingDisplayEventMap"
- "T@\"NSDictionary\",C,N,V_restartTrackingTriggerEventMap"
- "T@\"NSDictionary\",C,N,V_userInfo"
- "T@\"NSString\",R,N,V_dismissType"
- "T@\"TPSDocument\",C,N,V_content"
- "T@\"TPSMonitoringEvents\",C,N,V_monitoringEvents"
- "TB,N,GisLocalContent,V_localContent"
- "TB,R,N,GisHintInelgibile"
- "TPSAnalyticsEventContentEligibilityMet"
- "TPSAnalyticsEventTipDismissed"
- "TPSAnalyticsEventTipReadyToBeDisplayed"
- "TPSAnalyticsEventTipTapped"
- "TPSContentCheckInternalOverride"
- "TPSContextualPortraitEvent"
- "TPSDiscoverabilityOverrideHintMaxDisplayedCount"
- "TPSDiscoverabilityTip"
- "TPSHintMaxDurationTimeIntervalOverride"
- "TPSMiniTipContentManager"
- "TPSMiniTipContentManagerServiceInterface"
- "TPSMiniTipMetadata"
- "TPSMonitoringEvents"
- "TPSOverrideMinVersionForSpatialAudio"
- "TPSWidgetAssertionCreated"
- "Td,N,V_confidenceThreshold"
- "Td,N,V_timeToDismissal"
- "TipKitMonitoringEvents"
- "TipKitOverrideAlwaysDisplayContentForContext"
- "TipKitOverrideHintActionText"
- "TipKitOverrideHintActionURL"
- "TipKitOverrideHintBody"
- "TipKitOverrideHintCustomizationID"
- "TipKitOverrideHintTitle"
- "TipKitSuppressContent"
- "Tq,N,V_customizationID"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "Vv40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
- "Vv40@0:8@16@24@32"
- "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32q40"
- "Vv48@0:8@16@24@32q40"
- "_actionCompletionOnClientQueue:"
- "_attributedString"
- "_confidenceThreshold"
- "_content"
- "_contentWithContentIDCompletionOnClientQueue:"
- "_customizationID"
- "_desiredOutcomeEventMap"
- "_dismissType"
- "_dismissalEventMap"
- "_displayEventMap"
- "_eligibleContext"
- "_initWithContentID:bundleID:eligibleContext:displayType:usageFlags:date:"
- "_initWithTipID:correlationID:"
- "_initWithTipID:correlationID:bundleID:context:"
- "_initWithTipID:correlationID:bundleID:context:dismissType:timeToDismissal:date:"
- "_initWithTipID:correlationID:bundleID:context:displayType:"
- "_initialDisplayEventMap"
- "_localContent"
- "_monitoringEvents"
- "_performSyncWithProxyHandler:errorHandler:"
- "_preconditions"
- "_restartTrackingDisplayEventMap"
- "_restartTrackingTriggerEventMap"
- "_timeToDismissal"
- "allowsPersistentSiri"
- "attributedString"
- "autoDismissEvents"
- "bundleIDForIdentifier:"
- "clientContextEventsForMap:"
- "clientContextKeysForEventOptions:"
- "clientContextKeysForMap:"
- "com.apple.tips.TPSMiniTipContentManager"
- "com.apple.tipsd.xpc.discoverability"
- "confidenceThreshold"
- "contentWithContentIdentifiers:bundleID:context:completionHandler:"
- "content_eligible"
- "customizationID"
- "desiredOutcome"
- "desiredOutcomeEventMap"
- "discoverabilityOverrideMaxDisplayCount"
- "discoverabilitySuppressionInterval"
- "dismissType"
- "dismissalEventMap"
- "dismissalEventOccurred"
- "dismissalEvents"
- "dismissedByClient"
- "dismissedByUser"
- "displayContentForContext"
- "displayEventMap"
- "displayEvents"
- "eligibleContext"
- "eventMapFromMonitoringEventsDictionary:"
- "eventOptionsForEventIdentifier:"
- "eventWithContentID:bundleID:eligibleContext:displayType:usageFlags:date:"
- "eventWithTipID:correlationID:"
- "eventWithTipID:correlationID:bundleID:context:"
- "eventWithTipID:correlationID:bundleID:context:dismissType:timeToDismissal:date:"
- "eventWithTipID:correlationID:bundleID:context:displayType:"
- "hasClientContextKeysForEventOptions:"
- "hasEvents"
- "hasRegistrableContextualEventsForEventOptions:"
- "hintActionText"
- "hintActionURL"
- "hintBody"
- "hintCustomizationID"
- "hintDismissedForIdentifier:bundleID:context:reason:"
- "hintDisplayedForIdentifier:correlationID:context:"
- "hintInelgibile"
- "hintInelgibileReasonForIdentifier:"
- "hintMaxDurationTimeInterval"
- "hintMonitoringEvents"
- "hintTitle"
- "inAppHint"
- "initWithContent:"
- "initWithDictionary:desiredOutcomeDictionary:"
- "initialDisplayEventMap"
- "initialDisplayEvents"
- "invalid Collection: less than 'count' elements in collection"
- "invalidConfiguration"
- "isHintInelgibile"
- "isHintInelgibileForIdentifier:"
- "isHintInelgibileForReason:identifier:"
- "isHintMaxDurationExcceededForIdentifier:"
- "isLocalContent"
- "languageCodeMismatched"
- "localContent"
- "maxDisplayedCountExceeded"
- "maxDurationExceeded"
- "minVersionForSpatialAudio"
- "monitoringEvents"
- "persistent_siri"
- "personalizationFailed"
- "personalizationFailedForContentID:bundleID:context:"
- "preconditions"
- "registrableContextualEventsForEventOptions:type:"
- "registrableContextualEventsForMap:type:"
- "restartTrackingDisplayEventMap"
- "restartTrackingDisplayEventOccurred"
- "restartTrackingDisplayEvents"
- "restartTrackingForContentIdentifiers:"
- "restartTrackingTriggerEventMap"
- "restartTrackingTriggerEvents"
- "setAttributedString:"
- "setConfidenceThreshold:"
- "setContent:"
- "setCustomizationID:"
- "setDesiredOutcomeEventMap:"
- "setDismissalEventMap:"
- "setDisplayEventMap:"
- "setInitialDisplayEventMap:"
- "setLocalContent:"
- "setMonitoringEvents:"
- "setPreconditions:"
- "setRestartTrackingDisplayEventMap:"
- "setRestartTrackingTriggerEventMap:"
- "setTimeToDismissal:"
- "suppressTipKitContent"
- "timeToDismissal"
- "tip_dismissed"
- "tip_ready_to_be_displayed"
- "tip_tapped"
- "tipsAppDeleted"
- "updateHintInelgibileForIdentifier:value:"
- "v16@?0@\"<TPSMiniTipContentManagerServiceInterface>\"8"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v28@?0B8@12@\"NSError\"20"
- "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v48@0:8@16@24@32q40"
- "v52@0:8@16@\"NSString\"24@\"NSString\"32B40@?<v@?B@@\"NSError\">44"
- "v56@0:8@16@24@32B40B44@?48"
- "validateAndPrepareContentForDisplay:bundleID:context:skipUsageCheck:completionHandler:"
- "validateAndPrepareContentForDisplay:bundleID:context:synchronous:skipUsageCheck:completionHandler:"

```
