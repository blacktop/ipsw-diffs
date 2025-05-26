## TipsCore

> `/System/Library/PrivateFrameworks/TipsCore.framework/TipsCore`

```diff

-720.1.0.0.0
-  __TEXT.__text: 0x8fc58
-  __TEXT.__auth_stubs: 0x1910
-  __TEXT.__objc_methlist: 0x8bb8
-  __TEXT.__const: 0x1268
-  __TEXT.__cstring: 0x51c6
-  __TEXT.__oslogstring: 0x19ee
+725.16.0.0.0
+  __TEXT.__text: 0x92084
+  __TEXT.__auth_stubs: 0x1920
+  __TEXT.__objc_methlist: 0x8cf8
+  __TEXT.__const: 0x1328
+  __TEXT.__cstring: 0x5d56
+  __TEXT.__oslogstring: 0x1987
   __TEXT.__gcc_except_tab: 0x10e4
   __TEXT.__ustring: 0x118
   __TEXT.__dlopen_cstrs: 0x209
-  __TEXT.__swift5_typeref: 0x89b
-  __TEXT.__constg_swiftt: 0xa90
-  __TEXT.__swift5_reflstr: 0x631
-  __TEXT.__swift5_fieldmd: 0x6a4
+  __TEXT.__constg_swiftt: 0xca0
+  __TEXT.__swift5_typeref: 0x8bd
+  __TEXT.__swift5_reflstr: 0xb51
+  __TEXT.__swift5_fieldmd: 0x928
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_proto: 0xb4
-  __TEXT.__swift5_types: 0x88
+  __TEXT.__swift5_assocty: 0x138
+  __TEXT.__swift5_proto: 0xc0
+  __TEXT.__swift5_types: 0x90
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x360
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x36c4
+  __TEXT.__unwind_info: 0x36c0
   __TEXT.__eh_frame: 0xa98
-  __TEXT.__objc_classname: 0x10d1
-  __TEXT.__objc_methname: 0x1114a
-  __TEXT.__objc_methtype: 0x1cae
-  __TEXT.__objc_stubs: 0xb3a0
+  __TEXT.__objc_classname: 0x10d9
+  __TEXT.__objc_methname: 0x1134c
+  __TEXT.__objc_methtype: 0x1cf9
+  __TEXT.__objc_stubs: 0xb380
   __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0x2408
+  __DATA_CONST.__const: 0x2438
   __DATA_CONST.__objc_classlist: 0x520
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa8c8
-  __DATA_CONST.__objc_selrefs: 0x3ee0
+  __DATA_CONST.__objc_const: 0xacf8
+  __DATA_CONST.__objc_selrefs: 0x3f38
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x630
+  __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x138
-  __AUTH_CONST.__cfstring: 0x5e60
+  __AUTH_CONST.__cfstring: 0x5960
   __AUTH_CONST.__objc_const: 0x4d58
-  __AUTH_CONST.__const: 0x21c0
+  __AUTH_CONST.__const: 0x22d0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__auth_got: 0xc98
-  __AUTH.__objc_data: 0x1320
-  __AUTH.__data: 0x620
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x628
-  __DATA.__objc_superrefs: 0x380
-  __DATA.__objc_ivar: 0x8ac
-  __DATA.__data: 0x1280
-  __DATA.__bss: 0x13e0
+  __AUTH_CONST.__auth_ptr: 0x88
+  __AUTH_CONST.__auth_got: 0xca0
+  __AUTH.__objc_data: 0x12c8
+  __AUTH.__data: 0x408
+  __DATA.__objc_ivar: 0x8c4
+  __DATA.__data: 0x1860
+  __DATA.__bss: 0x1560
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2848
-  __DATA_DIRTY.__data: 0x358
+  __DATA_DIRTY.__objc_data: 0x2ab8
+  __DATA_DIRTY.__data: 0x640
   __DATA_DIRTY.__bss: 0x2c8
   __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4461
-  Symbols:   11035
-  CStrings:  4614
+  Functions: 4619
+  Symbols:   10985
+  CStrings:  4717
 
Symbols:
+ +[TPSAnalyticsEventSharedTipDisplayed eventWithTipID:correlationID:collectionID:variantID:message:isEligible:]
+ +[TPSAnalyticsEventSharedTipDisplayed supportsSecureCoding]
+ +[TPSCommonDefines isChecklistCollectionWithIdentifier:]
+ +[TPSConstellationContentUtilities contentContainsInlineIcon:]
+ +[TPSFeatureFlags allowTipsSharing]
+ -[TPSAnalyticsEventSharedTipDisplayed .cxx_destruct]
+ -[TPSAnalyticsEventSharedTipDisplayed _initWithTipID:correlationID:collectionID:variantID:eligibility:message:]
+ -[TPSAnalyticsEventSharedTipDisplayed collectionID]
+ -[TPSAnalyticsEventSharedTipDisplayed correlationID]
+ -[TPSAnalyticsEventSharedTipDisplayed eligibility]
+ -[TPSAnalyticsEventSharedTipDisplayed encodeWithCoder:]
+ -[TPSAnalyticsEventSharedTipDisplayed eventName]
+ -[TPSAnalyticsEventSharedTipDisplayed initWithCoder:]
+ -[TPSAnalyticsEventSharedTipDisplayed message]
+ -[TPSAnalyticsEventSharedTipDisplayed mutableAnalyticsEventRepresentation]
+ -[TPSAnalyticsEventSharedTipDisplayed setCollectionID:]
+ -[TPSAnalyticsEventSharedTipDisplayed setCorrelationID:]
+ -[TPSAnalyticsEventSharedTipDisplayed setEligibility:]
+ -[TPSAnalyticsEventSharedTipDisplayed setMessage:]
+ -[TPSAnalyticsEventSharedTipDisplayed setTipID:]
+ -[TPSAnalyticsEventSharedTipDisplayed setVariantID:]
+ -[TPSAnalyticsEventSharedTipDisplayed tipID]
+ -[TPSAnalyticsEventSharedTipDisplayed variantID]
+ -[TPSAppController contentForVariant:completionHandler:]
+ -[TPSAppController tipForCorrelationIdentifier:]
+ -[TPSAppController tipForVariantIdentifier:]
+ -[TPSCollection containsOutroTip]
+ -[TPSCollection countExcludingBookends]
+ -[TPSCollection setContainsOutroTip:]
+ -[TPSDocument availabilityMessage]
+ -[TPSDocument setAvailabilityMessage:]
+ -[TPSFullTipContentManager contentForVariant:completionHandler:]
+ GCC_except_table41
+ GCC_except_table56
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_TPSAnalyticsEventSharedTipDisplayed
+ _OBJC_IVAR_$_TPSAnalyticsEventSharedTipDisplayed._collectionID
+ _OBJC_IVAR_$_TPSAnalyticsEventSharedTipDisplayed._correlationID
+ _OBJC_IVAR_$_TPSAnalyticsEventSharedTipDisplayed._eligibility
+ _OBJC_IVAR_$_TPSAnalyticsEventSharedTipDisplayed._message
+ _OBJC_IVAR_$_TPSAnalyticsEventSharedTipDisplayed._tipID
+ _OBJC_IVAR_$_TPSAnalyticsEventSharedTipDisplayed._variantID
+ _OBJC_IVAR_$_TPSCollection._containsOutroTip
+ _OBJC_IVAR_$_TPSDocument._availabilityMessage
+ _OBJC_METACLASS_$_TPSAnalyticsEventSharedTipDisplayed
+ _TPSAnalyticsLaunchTypeSharedTipLocal
+ _TPSAnalyticsLaunchTypeSharedTipModal
+ _TPSAnalyticsLaunchTypeSharedTipSecondLaunch
+ _TPSConstellationContentUtilitiesAttributeHrefKey
+ _TPSConstellationContentUtilitiesMarkTypeLinkKey
+ __CLASS_PROPERTIES_TPSDefaultsManager
+ __DATA_TPSDefaultsManager
+ __METACLASS_DATA_TPSDefaultsManager
+ __OBJC_$_CLASS_METHODS_TPSAnalyticsEventSharedTipDisplayed
+ __OBJC_$_CLASS_METHODS_TPSAppController(TipsCore)
+ __OBJC_$_INSTANCE_METHODS_TPSAnalyticsEventSharedTipDisplayed
+ __OBJC_$_INSTANCE_METHODS_TPSAppController(TipsCore)
+ __OBJC_$_INSTANCE_METHODS_TPSDefaultsManager
+ __OBJC_$_INSTANCE_VARIABLES_TPSAnalyticsEventSharedTipDisplayed
+ __OBJC_$_PROP_LIST_TPSAnalyticsEventSharedTipDisplayed
+ __OBJC_CLASS_RO_$_TPSAnalyticsEventSharedTipDisplayed
+ __OBJC_METACLASS_RO_$_TPSAnalyticsEventSharedTipDisplayed
+ ___26+[TPSDocument na_identity]_block_invoke_15
+ ___35+[TPSFeatureFlags allowTipsSharing]_block_invoke
+ ___64-[TPSFullTipContentManager contentForVariant:completionHandler:]_block_invoke
+ ___64-[TPSFullTipContentManager contentForVariant:completionHandler:]_block_invoke_2
+ ___block_literal_global.109
+ ___block_literal_global.116
+ ___block_literal_global.118
+ ___block_literal_global.120
+ ___block_literal_global.122
+ ___block_literal_global.133
+ ___block_literal_global.141
+ ___block_literal_global.144
+ ___block_literal_global.94
+ _allowTipsSharing.allowFeature
+ _allowTipsSharing.predicate
+ _associated conformance 8TipsCore0A15DefaultsManagerC3Key026_FE6E458ED1144E0DACA4F0D75I5BC1A5LLOSHAASQ
+ _block_copy_helper.17
+ _block_copy_helper.32
+ _block_copy_helper.40
+ _block_copy_helper.48
+ _block_copy_helper.56
+ _block_descriptor.19
+ _block_descriptor.34
+ _block_descriptor.42
+ _block_descriptor.50
+ _block_descriptor.58
+ _block_destroy_helper.18
+ _block_destroy_helper.33
+ _block_destroy_helper.41
+ _block_destroy_helper.49
+ _block_destroy_helper.57
+ _kTipsAnalyticsVariantIDKey
+ _objc_msgSend$_initWithTipID:correlationID:collectionID:variantID:eligibility:message:
+ _objc_msgSend$availabilityMessage
+ _objc_msgSend$containsOutroTip
+ _objc_msgSend$contentForVariant:completionHandler:
+ _objc_msgSend$countExcludingBookends
+ _objc_msgSend$eligibility
+ _objc_msgSend$message
+ _objc_msgSend$setAvailabilityMessage:
+ _objectdestroy.30Tm
+ _swift_unknownObjectRetain_n
+ _symbolic _____ 8TipsCore0A15DefaultsManagerC
+ _symbolic _____ 8TipsCore0A15DefaultsManagerC3Key026_FE6E458ED1144E0DACA4F0D75I5BC1A5LLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s12StaticStringV
- +[TPSDefaultsManager allowsHardwareWelcomeNotification]
- +[TPSDefaultsManager assetRatioIdentifier]
- +[TPSDefaultsManager assetRequestHostURL]
- +[TPSDefaultsManager assetURL]
- +[TPSDefaultsManager boolDefaultsForKey:]
- +[TPSDefaultsManager boolDefaultsForKey:].cold.1
- +[TPSDefaultsManager checkOfflineContentOnLaunch]
- +[TPSDefaultsManager contextualEventDaysSinceLastMajorUpdateInSeconds]
- +[TPSDefaultsManager contextualEventLookBackDaysInSeconds]
- +[TPSDefaultsManager crunchingIntervalInDays]
- +[TPSDefaultsManager debugActiveIAPs]
- +[TPSDefaultsManager deviceModel]
- +[TPSDefaultsManager discoverabilityOverrideMaxDisplayCount]
- +[TPSDefaultsManager discoverabilitySuppressionInterval]
- +[TPSDefaultsManager displayContentForContext]
- +[TPSDefaultsManager featuredCollection]
- +[TPSDefaultsManager hintActionText]
- +[TPSDefaultsManager hintActionURL]
- +[TPSDefaultsManager hintBody]
- +[TPSDefaultsManager hintCustomizationID]
- +[TPSDefaultsManager hintMaxDurationTimeInterval]
- +[TPSDefaultsManager hintMonitoringEvents]
- +[TPSDefaultsManager hintTitle]
- +[TPSDefaultsManager holdoutGroup]
- +[TPSDefaultsManager ignoreCloud]
- +[TPSDefaultsManager ignoreTargetingValidator]
- +[TPSDefaultsManager integerDefaultsForKey:]
- +[TPSDefaultsManager integerDefaultsForKey:].cold.1
- +[TPSDefaultsManager isInternalDevice]
- +[TPSDefaultsManager lastMajorVersionUpdateDate]
- +[TPSDefaultsManager matchedClientConditionTargeting]
- +[TPSDefaultsManager matchedClientConditions]
- +[TPSDefaultsManager minVersionForSpatialAudio]
- +[TPSDefaultsManager notificationDocument]
- +[TPSDefaultsManager objectDefaultsForKey:]
- +[TPSDefaultsManager objectDefaultsForKey:].cold.1
- +[TPSDefaultsManager platform]
- +[TPSDefaultsManager releaseType]
- +[TPSDefaultsManager requestHostURL]
- +[TPSDefaultsManager requestInterval]
- +[TPSDefaultsManager requestLanguage]
- +[TPSDefaultsManager requestModel]
- +[TPSDefaultsManager requestPlatform]
- +[TPSDefaultsManager requestURL]
- +[TPSDefaultsManager requestVersion]
- +[TPSDefaultsManager resetDaemonData]
- +[TPSDefaultsManager resetDataCache]
- +[TPSDefaultsManager sessionTimeoutIntervalInSeconds]
- +[TPSDefaultsManager showAllCollections]
- +[TPSDefaultsManager showCollectionIntro]
- +[TPSDefaultsManager showPagingLabelOnLongPress]
- +[TPSDefaultsManager standardNotificationInterval]
- +[TPSDefaultsManager suppressNotifications]
- +[TPSDefaultsManager suppressTipKitContent]
- +[TPSDefaultsManager timeIntervalDefaultsForKey:]
- +[TPSDefaultsManager triggerMinObservationCount]
- +[TPSDefaultsManager welcomeNotificationDelay]
- +[TPSDefaultsManager welcomeNotificationGracePeriod]
- +[TPSDefaultsManager widgetDocument]
- +[TPSTuple tupleWithFirst:second:]
- -[TPSTuple .cxx_destruct]
- -[TPSTuple description]
- -[TPSTuple first]
- -[TPSTuple initWithFirst:second:]
- -[TPSTuple second]
- GCC_except_table53
- GCC_except_table55
- _OBJC_CLASS_$_TPSTuple
- _OBJC_IVAR_$_TPSTuple._first
- _OBJC_IVAR_$_TPSTuple._second
- _OBJC_METACLASS_$_TPSTuple
- __OBJC_$_CLASS_METHODS_TPSAppController
- __OBJC_$_CLASS_METHODS_TPSTuple
- __OBJC_$_INSTANCE_METHODS_TPSAppController
- __OBJC_$_INSTANCE_METHODS_TPSTuple
- __OBJC_$_INSTANCE_VARIABLES_TPSTuple
- __OBJC_$_PROP_LIST_TPSTuple
- __OBJC_CLASS_RO_$_TPSDefaultsManager
- __OBJC_CLASS_RO_$_TPSTuple
- __OBJC_METACLASS_RO_$_TPSDefaultsManager
- __OBJC_METACLASS_RO_$_TPSTuple
- ___38+[TPSDefaultsManager isInternalDevice]_block_invoke
- ___38+[TPSDefaultsManager isInternalDevice]_block_invoke.cold.1
- ___block_literal_global.106
- ___block_literal_global.113
- ___block_literal_global.115
- ___block_literal_global.117
- ___block_literal_global.119
- ___block_literal_global.121
- ___block_literal_global.132
- ___block_literal_global.91
- _block_copy_helper.18
- _block_copy_helper.33
- _block_copy_helper.41
- _block_copy_helper.49
- _block_copy_helper.57
- _block_descriptor.20
- _block_descriptor.35
- _block_descriptor.43
- _block_descriptor.51
- _block_descriptor.59
- _block_destroy_helper.19
- _block_destroy_helper.34
- _block_destroy_helper.42
- _block_destroy_helper.50
- _block_destroy_helper.58
- _isInternalDevice._isInternal
- _isInternalDevice.onceToken
- _objc_msgSend$boolDefaultsForKey:
- _objc_msgSend$boolForKey:
- _objc_msgSend$cStringUsingEncoding:
- _objc_msgSend$first
- _objc_msgSend$initWithFirst:second:
- _objc_msgSend$integerDefaultsForKey:
- _objc_msgSend$objectDefaultsForKey:
- _objc_msgSend$second
- _objc_msgSend$timeIntervalDefaultsForKey:
- _objc_retain_x10
- _objectdestroy.31Tm
- _swift_setDeallocating
CStrings:
+ "\x1c"
+ " override with value "
+ "@60@0:8@16@24@32@40@48B56"
+ "Can't construct Array with count < 0"
+ "Default TPSInternalDevice override with value "
+ "Division by zero"
+ "Division results in an overflow"
+ "Insufficient space allocated to copy string contents"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSDate\",N,R"
+ "T@\"NSNumber\",N,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_availabilityMessage"
+ "T@\"NSString\",C,N,V_eligibility"
+ "T@\"NSString\",C,N,V_message"
+ "TB,N"
+ "TB,N,V_containsOutroTip"
+ "TPSAnalyticsEventSharedTipDisplayed"
+ "Td,N,R"
+ "This feature may not be available on your device."
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_availabilityMessage"
+ "_containsOutroTip"
+ "_eligibility"
+ "_initWithTipID:correlationID:collectionID:variantID:eligibility:message:"
+ "_message"
+ "allowTipsSharing"
+ "availabilityMessage"
+ "containsOutroTip"
+ "contentContainsInlineIcon:"
+ "contentForVariant:completionHandler:"
+ "countExcludingBookends"
+ "eligibility"
+ "eligible"
+ "eventWithTipID:correlationID:collectionID:variantID:message:isEligible:"
+ "hasLocalVariant:"
+ "ineligible"
+ "ineligible - with correlating tip"
+ "invalid Collection: less than 'count' elements in collection"
+ "isChecklistCollectionWithIdentifier:"
+ "logSharedTipDisplayed:isEligible:"
+ "message"
+ "n/a"
+ "numberFromString:"
+ "setAvailabilityMessage:"
+ "setContainsOutroTip:"
+ "setEligibility:"
+ "setIsInternalDevice:"
+ "setMessage:"
+ "shared_tip_local"
+ "shared_tip_modal"
+ "shared_tip_second_launch"
+ "sharing"
+ "tipForCorrelationIdentifier:"
+ "tipForVariantIdentifier:"
+ "tip_shared"
+ "tip_variant_ID"
+ "v32@0:8@\"NSString\"16@?<v@?@\"TPSTip\"@\"NSError\">24"
- "\x1b"
- "<%@: %p; first = %@, second = %@>"
- "Default %@ override with value %@"
- "Default %@ override with value %d"
- "Default %@ override with value %ld"
- "T@,R,N,V_first"
- "T@,R,N,V_second"
- "TPSCheckOfflineContentOnLaunch"
- "TPSTuple"
- "_first"
- "_second"
- "boolDefaultsForKey:"
- "cStringUsingEncoding:"
- "checkOfflineContentOnLaunch"
- "first"
- "initWithFirst:second:"
- "integerDefaultsForKey:"
- "objectDefaultsForKey:"
- "second"
- "timeIntervalDefaultsForKey:"
- "tupleWithFirst:second:"

```
