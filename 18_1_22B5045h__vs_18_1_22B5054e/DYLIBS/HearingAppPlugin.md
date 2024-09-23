## HearingAppPlugin

> `/System/Library/Health/FeedItemPlugins/HearingAppPlugin.healthplugin/HearingAppPlugin`

```diff

-5200.1.7.0.0
-  __TEXT.__text: 0x3e280
-  __TEXT.__auth_stubs: 0x1b80
-  __TEXT.__objc_methlist: 0x130
-  __TEXT.__const: 0x2044
-  __TEXT.__cstring: 0x2b50
-  __TEXT.__constg_swiftt: 0x1574
-  __TEXT.__swift5_typeref: 0x98c
-  __TEXT.__swift5_reflstr: 0x9c4
-  __TEXT.__swift5_fieldmd: 0x948
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__oslogstring: 0xdd5
-  __TEXT.__swift5_capture: 0x2d0
-  __TEXT.__swift5_proto: 0x188
-  __TEXT.__swift5_types: 0xcc
-  __TEXT.__swift5_protos: 0x30
-  __TEXT.__unwind_info: 0xd88
-  __TEXT.__eh_frame: 0x538
+5200.1.9.1.2
+  __TEXT.__text: 0x89ad4
+  __TEXT.__auth_stubs: 0x3690
+  __TEXT.__objc_methlist: 0x198
+  __TEXT.__const: 0x4174
+  __TEXT.__cstring: 0x46e0
+  __TEXT.__constg_swiftt: 0x2198
+  __TEXT.__swift5_typeref: 0x14bc
+  __TEXT.__swift5_reflstr: 0x13c4
+  __TEXT.__swift5_fieldmd: 0x1268
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_assocty: 0x230
+  __TEXT.__oslogstring: 0x1673
+  __TEXT.__swift5_capture: 0x4e8
+  __TEXT.__swift5_proto: 0x308
+  __TEXT.__swift5_types: 0x1a8
+  __TEXT.__swift5_protos: 0x34
+  __TEXT.__unwind_info: 0x1c20
+  __TEXT.__eh_frame: 0xed0
   __TEXT.__objc_classname: 0x4b
-  __TEXT.__objc_methname: 0x126f
+  __TEXT.__objc_methname: 0x1ade
   __TEXT.__objc_methtype: 0xd6
-  __DATA_CONST.__got: 0x690
-  __DATA_CONST.__const: 0x130
-  __DATA_CONST.__objc_classlist: 0x90
+  __TEXT.__objc_stubs: 0x20
+  __DATA_CONST.__got: 0xe20
+  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist2: 0x8
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x540
-  __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0xdc0
-  __AUTH_CONST.__auth_ptr: 0x750
-  __AUTH_CONST.__const: 0x1158
-  __AUTH_CONST.__objc_const: 0x1778
-  __AUTH.__objc_data: 0xd90
-  __AUTH.__data: 0x960
-  __DATA.__data: 0x7a8
-  __DATA.__objc_stublist: 0x58
-  __DATA.__common: 0xb8
-  __DATA.__bss: 0x1340
+  __DATA_CONST.__objc_selrefs: 0x830
+  __DATA_CONST.__objc_protorefs: 0x28
+  __AUTH_CONST.__auth_got: 0x1b50
+  __AUTH_CONST.__auth_ptr: 0xd60
+  __AUTH_CONST.__const: 0x21d8
+  __AUTH_CONST.__objc_const: 0x25e8
+  __AUTH.__objc_data: 0x1398
+  __AUTH.__data: 0x1870
+  __DATA.__data: 0x16a0
+  __DATA.__objc_stublist: 0x78
+  __DATA.__common: 0x218
+  __DATA.__bss: 0x3da0
   __DATA_DIRTY.__objc_data: 0x3e0
-  __DATA_DIRTY.__data: 0xb38
-  __DATA_DIRTY.__bss: 0x1100
+  __DATA_DIRTY.__data: 0xb78
+  __DATA_DIRTY.__bss: 0x1580
   __DATA_DIRTY.__common: 0xf0
   - /System/Library/Frameworks/Charts.framework/Charts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/HealthPlatformCore.framework/HealthPlatformCore
   - /System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox
   - /System/Library/PrivateFrameworks/HealthUI.framework/HealthUI
+  - /System/Library/PrivateFrameworks/HearingTestUI.framework/HearingTestUI
   - /System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences

   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib
+  - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSceneKit.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1182
-  Symbols:   252
-  CStrings:  525
+  Functions: 2449
+  Symbols:   320
+  CStrings:  821
 
Symbols:
+ _HKLocalizedStringForHearingLevelClassification
+ _OBJC_CLASS_$_UIScrollView
+ _HKFeatureAvailabilityContextHearingTestPromptTileVisibility
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _swift_getTupleTypeMetadata
+ _HKFeatureAvailabilityRequirementIdentifierCountryIsSupportedOnLocalDevice
+ _HKUIJoinStringsForAutomationIdentifier
+ __HKPrivateMetadataKeyHearingTestTakenWithRecentLoudNoiseExposure
+ _OBJC_CLASS_$_HKUnitPreferenceController
+ _HKIntegerFormatter
+ __swift_FORCE_LOAD_$_swiftGLKit
+ _swift_task_switch
+ _CGContextDrawPath
+ _OBJC_CLASS_$_HKCollectionViewLayoutEngineDefaults
+ _swift_release_n
+ _CGContextAddPath
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_CLASS_$_NSDateFormatter
+ __HKPrivateMetadataKeyHearingTestTakenFromFirstParty
+ _OBJC_METACLASS_$__TtC18HealthExperienceUI42CompoundDataSourceCollectionViewController
+ __swift_FORCE_LOAD_$_swiftModelIO
+ _OBJC_CLASS_$_HKQuery
+ _HKNumberFormatterWithDecimalPrecision
+ _OBJC_CLASS_$_NSTextAttachment
+ _OBJC_CLASS_$_NSNumberFormatter
+ _objc_release_x10
+ _HKFeatureAvailabilityContextUsage
+ _OBJC_CLASS_$_UIBarButtonItem
+ _HKLocalizedStringForUpperClampedValueAndUnit
+ _OBJC_CLASS_$_HKSample
+ __swift_FORCE_LOAD_$_swiftSceneKit
+ _swift_getOpaqueTypeMetadata2
+ _OBJC_CLASS_$_HKFeatureStatusManager
+ _OBJC_METACLASS_$__TtC18HealthExperienceUI42PDFPageAlignedNumberedPageWithCustomNotice
+ __HKPrivateMetadataKeyHearingTestTakenWithCongestion
+ _HKFeatureAvailabilityRequirementIdentifierSeedIsNotExpired
+ _HKCountryCodeJapan
+ _HKFormatValueAndUnit
+ _OBJC_CLASS_$_HKQueryDescriptor
+ _swift_deletedAsyncMethodErrorTu
+ _OBJC_CLASS_$_HKAudiogramSample
+ _OBJC_CLASS_$_HKAudiogramSensitivityTest
+ _HKCountryCodeUnknownCountry
+ _CGPathCreateWithRoundedRect
+ _OBJC_CLASS_$_HKAudiogramSensitivityPoint
+ _OBJC_METACLASS_$_UIViewController
+ _HKSampleSortIdentifierEndDate
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _HKFeatureAvailabilityRequirementIdentifierFeatureIsNotRemotelyDisabled
+ _swift_getOpaqueTypeConformance2
+ _CGContextSaveGState
+ _HKHearingLevelClassificationForSensitivity
+ _HKFeatureIdentifierHearingTest
+ _CGContextRestoreGState
+ _CGContextSetFillColorWithColor
+ _HKCurrentLocaleCountryCodeIfUnknown
+ _UIGraphicsPushContext
+ _objc_retain_x3
+ _OBJC_CLASS_$_UIButton
+ _UIGraphicsPopContext
+ __HKPrivateMetadataKeyHearingTestTakenWithLeftEarNoiseLevel
+ _HKSampleSortIdentifierStartDate
+ _HKUIAutomationIdentifierPrefix
+ __HKPrivateMetadataKeyHearingTestTakenWithRightEarNoiseLevel
+ _swift_makeBoxUnique
+ _OBJC_CLASS_$_HKHealthChartFactory
+ __swift_FORCE_LOAD_$_swiftMetalKit
CStrings:
+ "HEARING_TEST_PDF_METADATA_VALUE_NO"
+ "HearingAppPlugin-Localizable-Yodel"
+ "systemImageNamed:"
+ "ShowAllAudiogramsSampleSampleDetails"
+ "_TtC16HearingAppPlugin20AudiogramPDFProvider"
+ "_TtP13HearingTestUI27HearingTestArticleProviding_"
+ "systemBlueColor"
+ "HEARING_TEST_RESCINDED_LINK"
+ "HERTZ_NUMBERLESS_UNIT"
+ "SECTION4_LIST_ITEM2"
+ "SECTION4_PARAGRAPH1_LEARN_MORE"
+ "_TtC16HearingAppPlugin27AudiogramPDFChartDataSource"
+ "averageLeftEarSensitivity"
+ "HEARING_TEST_PDF_OVERVIEW_TITLE"
+ "arrangedSubviews"
+ "openSensitiveURL:withOptions:"
+ "HEARING_TEST_PDF_YEAR_RANGE"
+ "_TtC16HearingAppPlugin40AudiogramPDFAsyncConfigurationDataSource"
+ "addChildViewController:"
+ "[%!s(MISSING)] Failed to encode PromptTileView.ViewModel for Hearing Test Prompt Tile. Failed to create a feed item with error: %!s(MISSING)"
+ "makePromotionTileConfiguration(from:)"
+ "whiteColor"
+ "AudiogramEducation-Localizable-Yodel"
+ "_TtC16HearingAppPlugin36AudiogramPDFAudiogramSectionProvider"
+ "hk_hearingHealthAudiogramRightEarLineColor"
+ "HearingAppPlugin/AudiogramAllDataChartViewController.swift"
+ "_TtC16HearingAppPlugin26AudiogramPDFAudiogramChart"
+ "buttonWithType:"
+ "HEARING_TEST_DATATYPE_ROOM_TITLE"
+ "HEARING_TEST_ALL_RESULTS_TITLE"
+ "averageRightEarSensitivity"
+ "HEARING_TEST_ABOUT_BUTTON_TITLE"
+ "HearingAidsHelpMoreThanYourHearing"
+ "SECTION4_LIST_ITEM6"
+ "HEARING_TEST_PDF_SELECTION_ALL"
+ "HEARING_TEST_PDF_SHARE_ACTION_BUTTON_TITLE"
+ "[%!{(MISSING)public}s.%!{(MISSING)public}s]: Creating promo tile configuration for feature status %!{(MISSING)public}s"
+ "setDelegate:"
+ "setLayoutMarginsRelativeArrangement:"
+ "initWithNibName:bundle:"
+ "[%!{(MISSING)public}s] PDF Configuration Row not found for row %!{(MISSING)public}ld"
+ "shareButtonTapped:"
+ "analyticsManager"
+ "AudiogramPDFItem"
+ "metadata"
+ "clampedSensitivity"
+ "edgeInsetsForWidthDesignation:"
+ "defaultWorkspace"
+ "setAccessibilityIdentifier:"
+ "cancellable"
+ "$__lazy_storage_$_exportPDFButton"
+ "v32@0:8@\"_TtC13HearingTestUI29HearingTestMainViewController\"16@?<v@?@\"HKAudiogramSample\">24"
+ "HEARING_TEST_PDF_CONTEXT_PILL_LEFT"
+ "shareButtonBehavior"
+ "CGContext"
+ "HEARING_TEST_PDF_THINGS_YOU_SHOULD_KNOW_NUMBERED_LIST_JOINER"
+ "SECTION1_PARAGRAPH2_HEADER"
+ "bottomPadding"
+ "initWithFeatureIdentifier:healthStore:"
+ "requestType"
+ "userInterfaceLayoutDirectionForSemanticContentAttribute:"
+ "$__lazy_storage_$_shareBarButtonItem"
+ "Error fetching audiogram samples: %!{(MISSING)public}s"
+ "HEARING_TEST_RESCINDED_FEED_ITEM_TITLE"
+ "appendAttributedString:"
+ "HearingTest.prompt.feedItem"
+ "ONBOARDING_SHOULD_KNOW_TITLE"
+ "hearingLevelSummary"
+ "_TtC16HearingAppPlugin51HearingFeaturesInSettingsPromotionGeneratorPipeline"
+ "remoteDisable"
+ "[%!{(MISSING)public}s] Unable to determine chart x scale domain"
+ "debounceForSelectedItemInSeconds"
+ "HearingAppPlugin/AudiogramAllDataViewController.swift"
+ "hk_appTintColor"
+ "predicateForSamplesWithStartDate:endDate:options:"
+ "HEARING_TEST_ADD_TEST"
+ "[%!s(MISSING).%!s(MISSING)]: Feed item will not be created given onboarding and feature enabled status"
+ "_TtC16HearingAppPlugin26HearingTestArticleProvider"
+ "sampleType"
+ "size"
+ "unitTest_didPublishAudiograms"
+ "HEARING_TEST_PDF_AUDIOGRAM_TITLE"
+ "chartModel"
+ "safeAreaLayoutGuide"
+ "Hearing Features in Settings has not been implemented yet."
+ "SECTION2_PARAGRAPH4"
+ "lower upper "
+ "makePromptFeedItem(sourceProfile:featureStatus:)"
+ "upperBound"
+ "HEARING_TEST_PDF_FOOTNOTE_JAPAN_DISCLAIMER"
+ "localizedIngestionSource"
+ "HEARING_TEST_PDF_SHARE_ACTION_DESCRIPTION"
+ "initWithCollectionViewLayout:"
+ "HEARING_TEST_ALL_RESULTS_DECIBEL_TEXT_%!@(MISSING)"
+ "_TtC16HearingAppPlugin37HearingTestRescindedTileActionHandler"
+ "leftEarAnnotationIndex"
+ "tintColor"
+ "HearingHealthEducation-Localizable-Yodel"
+ "[%!s(MISSING).%!s(MISSING)]: Returning regionGated state from unavailability %!s(MISSING)"
+ "[%!{(MISSING)public}s.%!{(MISSING)public}s]: Creating prompt tile configuration for feature status %!{(MISSING)public}s"
+ "_TtC16HearingAppPlugin35AudiogramAllDataChartViewController"
+ "tests"
+ "AudiogramShowAllComponent"
+ "SECTION1_PARAGRAPH6"
+ "HearingTest.promotion.feedItem"
+ "endDate"
+ "showPromptTile(from:)"
+ "[%!{(MISSING)public}s] Got nil result from classification utility"
+ "doubleValueForUnit:"
+ "initWithSampleType:predicate:"
+ "setModalPresentationStyle:"
+ "_TtC16HearingAppPlugin25AudiogramShowAllComponent"
+ "_TtP13HearingTestUI39HearingTestAudiogramImportFlowProviding_"
+ "setRightBarButtonItem:"
+ "seedExpiry"
+ "areAllRequirementsSatisfied"
+ "AudiogramAllData"
+ "[%!s(MISSING).%!s(MISSING)]: Returning remoteDisable state from unavailability %!s(MISSING)"
+ "showPromotionTile(from:)"
+ "colorWithAlphaComponent:"
+ "URLForResource:withExtension:"
+ "attributedStringWithAttachment:"
+ "regionGated"
+ "headerProvider"
+ "side"
+ "sensitivity"
+ "hertzUnit"
+ "HEARING_TEST_PDF_SENSITIVITY_POINT_VALUE_LOWER_CLAMPING"
+ "HEARING_TEST_PDF_SHARE_ACTION_TITLE"
+ "HEARING_TEST_PROMOTION_TILE_BUTTON"
+ "HearingTestRescinded"
+ "containSensitivityPointsIsMasked:forSide:"
+ "makeActionHandlerUserDataObject(context:)"
+ "clampingRange"
+ ".AudiogramLongitudinalPDFChartView"
+ "SECTION4_LIST_ITEM5"
+ "constraintEqualToAnchor:constant:"
+ "sensitivityPoints"
+ "configurationWithHierarchicalColor:"
+ "startDate"
+ "lowerBound"
+ "HearingTestRescindedFeedItemFactory"
+ "init(nibName:bundle:)"
+ "KILOHERTZ_NUMBERLESS_UNIT"
+ "setDistribution:"
+ "HEARING_TEST_ALL_RESULTS_BUTTON_TITLE"
+ "HEARING_TEST_PDF_PREVIEW_TITLE"
+ "showViewController:sender:"
+ "HEARING_TEST_PREVIEW_PDF_MOST_RECENT"
+ "setShowsHorizontalScrollIndicator:"
+ "[%!s(MISSING).%!s(MISSING)]: Feed item will be marked for deletion given no unavailability reasons"
+ "didMoveToParentViewController:"
+ "init(dataSource:)"
+ "setMaximumFractionDigits:"
+ "HearingAppPlugin.AudiogramAllDataViewController"
+ "frequency"
+ "SECTION4_LIST_ITEM9"
+ "ear.badge.magnifyingglass"
+ "HEARING_TEST_RESCINDED_FEED_ITEM_ACTION"
+ "SECTION4_LIST_ITEM3"
+ "HearingTestTileFeedItemFactory"
+ "makeFeedItem(sourceProfile:state:)"
+ "selectedConfiguration"
+ "HearingAppPlugin.AudiogramAllDataChartViewController"
+ "SECTION4_PARAGRAPH2"
+ "clearColor"
+ "stringFromNumber:"
+ "JAPAN_SECTION_DESCRIPTION"
+ "[[%!{(MISSING)public}s] Cannot open hearing test with path components: %!{(MISSING)public}s"
+ "_PARTY_LOWER_CLAMPING"
+ "HEARING_TEST_ALL_RESULTS_CLASSIFICATION_DECIBEL_TEXT_%!@(MISSING)%!@(MISSING)"
+ "HEARING_TEST_PDF_LEFT_EAR_NOISE_LEVEL"
+ "SECTION1_PARAGRAPH5_HEADER"
+ "[%!s(MISSING).%!s(MISSING)]: Non-primary source"
+ "[%!s(MISSING)] Failed to encode PromptTileView.ViewModel for Hearing Test Rescinded Tile. Failed to create a feed item with error: %!s(MISSING)"
+ "yodel"
+ "HEARING_TEST_PDF_FILE_NAME"
+ "[%!{(MISSING)public}s] Error fetching sample counts: %!{(MISSING)public}s"
+ "navigationItem"
+ "_TtC16HearingAppPlugin55HearingFeaturesInSettingsPromotionTileViewActionHandler"
+ "capturedInitialQueryAnalytics"
+ "setDateStyle:"
+ "HEARING_TEST_PDF_OVERVIEW_DESCRIPTION"
+ "[%!{(MISSING)public}s] Hearing Test not available due to error: %!{(MISSING)public}@"
+ "capHeight"
+ "view"
+ "HEARING_TEST_PROMOTION_TILE_DETAIL"
+ "PDF page is too small to render all elements. Elements will be clipped."
+ "configurationWithPointSize:"
+ "item cellType "
+ "@32@0:8@16@24"
+ "AllHearingResultsButton"
+ "HEARING_TEST_PDF_RIGHT_EAR_NOISE_LEVEL"
+ "[%!{(MISSING)public}s] Failed to format filter value for type: %!s(MISSING)"
+ "addTarget:action:forControlEvents:"
+ "@\"UIViewController\"16@0:8"
+ "HEARING_TEST_PROMOTION_TILE_TITLE"
+ "[%!{(MISSING)public}s] Did tap Hearing Features in Settings."
+ "scrollView"
+ "HEARING_TEST_ALL_RESULTS_CELL_TEXT_%!@(MISSING)%!@(MISSING)"
+ "com.apple.health.Education.HearingAids"
+ "removeFromSuperview"
+ "AudiogramAllDataChartView"
+ "footerProvider"
+ "HEARING_TEST_PDF_BUTTON_TITLE"
+ "HEARING_TEST_PDF_FOOTNOTE_"
+ "ONBOARDING_SHOULD_KNOW_ITEM_2_TITLE"
+ "[%!{(MISSING)public}s] Presenting Hearing Test."
+ "HEARING_TEST_PDF_METADATA_VALUE_YES"
+ "HearingAidsEducation-Localizable-Yodel"
+ "SECTION4_LIST_ITEM4"
+ "localizedDisplayNameForUnit:value:"
+ "[%!{(MISSING)public}s] PDF Configuration cannot determine first date of ten years ago"
+ "setContentHorizontalAlignment:"
+ "textAttachmentWithImage:"
+ "CGColor"
+ "HEARING_TEST_ALL_RESULTS_EXPORT_PDF"
+ "HEARING_TEST_PDF_DBHL"
+ "HearingAppPlugin1"
+ "_TtC16HearingAppPlugin30AudiogramAllDataViewController"
+ "audiogramAllDataViewModel"
+ "HEARING_TEST_PDF_INGESTION_SOURCE"
+ "SECTION2_PARAGRAPH2_LEARN_MORE"
+ "rightEarAnnotationIndex"
+ "HEARING_TEST_PDF_CONGESTION"
+ "SECTION4_LIST_ITEM8"
+ "[%!{(MISSING)public}s.%!{(MISSING)public}s]: Hearing Test promotion tile requirement was not met for feature status %!{(MISSING)public}s"
+ "hearingLossArticleViewController"
+ "configurationByApplyingConfiguration:"
+ "initWithImage:options:"
+ "unsatisfiedRequirementIdentifiers"
+ "_PARTY_UPPER_CLAMPING"
+ "scrollViewContainer"
+ "%!{(MISSING)public}s: Failed to create frequency formatter"
+ "Failed to encode userData: %!s(MISSING)"
+ "isAverageSensitivityUpperClampedForSide:"
+ "[%!s(MISSING).%!s(MISSING)]: Returning seedExpiry state from unavailability %!s(MISSING)"
+ "rightEarMetrics"
+ "SECTION4_LIST_ITEM1"
+ "didTapImportAudiogramLinkIn:completion:"
+ "setTimeStyle:"
+ "[%!{(MISSING)public}s.%!{(MISSING)public}s]: Hearing Test prompt tile requirement was not met for feature status %!{(MISSING)public}s"
+ "_TtC16HearingAppPlugin37HearingTestPromotionViewActionHandler"
+ "addArrangedSubview:"
+ "averageSensitivity"
+ "didTapExportAll:"
+ "SECTION4_LIST_ITEM7"
+ "pdfProvider"
+ "staticAudiogramChartViewControllerWithAudiogramSample:hideEnhancedUI:"
+ " options caption accessibilityDescription playVisibilityPercentage "
+ "HEARING_TEST_RESCINDED_FEED_ITEM_BODY"
+ "audiogramSampleSubject"
+ "dataSource"
+ "_TtC16HearingAppPlugin35AudiogramPDFOverviewSectionProvider"
+ "stringFromDate:"
+ "hearingTestFeatureStatus"
+ "audiogramSample"
+ "init(collectionViewLayout:)"
+ "HEARING_TEST_PDF_CONTEXT_PILL_RIGHT"
+ "_TtC16HearingAppPlugin29AudiogramPDFLongitudinalChart"
+ "initWithKey:ascending:"
+ "_TtC16HearingAppPlugin43AudiogramPDFJapanDisclaimerPageNumberedPage"
+ "isRequirementSatisfiedWithIdentifier:"
+ "setNumberStyle:"
+ "setBounds:"
+ "HEARING_TEST_PDF_RECENT_LOUD_NOISE_EXPOSURE"
+ "HEARING_TEST_PDF_SENSITIVITY_POINT_VALUE_UPPER_CLAMPING"
+ "ONBOARDING_SHOULD_KNOW_ITEM_1_TITLE"
+ "ONBOARDING_SHOULD_KNOW_ITEM_3_TITLE"
+ "SECTION3_PARAGRAPH3"
+ "setDirectionalLayoutMargins:"
+ "audiogram_ear_message_image"
+ "square.and.arrow.up"
+ "[%!s(MISSING).%!s(MISSING)]: Feed item created with state %!s(MISSING)"
+ "[%!{(MISSING)public}s.%!{(MISSING)public}s]: Creating promo tile action handler user data object"
+ "leftEarMetrics"
+ "_TtC16HearingAppPlugin25AudiogramAllDataViewModel"
+ "automationIdentifierBase"
+ "characteristicsProvider"
+ "hearing_aid_article_background"
+ "SECTION3_PARAGRAPH4"
+ "[%!{(MISSING)public}s] Error fetching db changes: %!{(MISSING)public}s"
+ "_TtC16HearingAppPlugin34HearingTestPromptTileActionHandler"
+ "_TtC16HearingAppPlugin39AudiogramPDFLongitudinalChartDataSource"
+ "masked"
+ "HEARING_FEATURES_IN_SETTINGS_PROMOTION_TILE_TITLE"
+ "HearingTest.rescinded.feedItem"
+ "[%!s(MISSING)]: Opening %!s(MISSING), success: %!s(MISSING)"
+ "none"
+ "startInitialAudiogramPublisherTime"
+ "rescindedState(from:)"
+ "systemPinkColor"
+ "HEARING_TEST_PDF_LONGITUDINAL_CHART_TITLE"
+ "chartController"
+ "hk_hearingHealthAudiogramLeftEarLineColor"
+ "v32@0:8@16@?24"
- "SECTION1_PARAGRAPH3_LEARN_MORE"

```
