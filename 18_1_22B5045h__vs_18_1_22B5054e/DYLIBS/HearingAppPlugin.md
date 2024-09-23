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
+ _OBJC_CLASS_$_UIScrollView
+ _HKLocalizedStringForHearingLevelClassification
+ _swift_makeBoxUnique
+ _CGContextSetFillColorWithColor
+ _CGPathCreateWithRoundedRect
+ _OBJC_CLASS_$_HKAudiogramSample
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_METACLASS_$_UIViewController
+ __swift_FORCE_LOAD_$_swiftSceneKit
+ _HKFormatValueAndUnit
+ _HKNumberFormatterWithDecimalPrecision
+ _OBJC_METACLASS_$__TtC18HealthExperienceUI42CompoundDataSourceCollectionViewController
+ _HKIntegerFormatter
+ _HKSampleSortIdentifierEndDate
+ _HKFeatureAvailabilityRequirementIdentifierFeatureIsNotRemotelyDisabled
+ _OBJC_METACLASS_$__TtC18HealthExperienceUI42PDFPageAlignedNumberedPageWithCustomNotice
+ _UIGraphicsPopContext
+ _swift_task_switch
+ _swift_getOpaqueTypeConformance2
+ _HKFeatureAvailabilityContextUsage
+ _HKCurrentLocaleCountryCodeIfUnknown
+ _HKCountryCodeJapan
+ _OBJC_CLASS_$_NSSortDescriptor
+ _HKFeatureIdentifierHearingTest
+ _HKUIJoinStringsForAutomationIdentifier
+ _CGContextRestoreGState
+ _OBJC_CLASS_$_HKCollectionViewLayoutEngineDefaults
+ _OBJC_CLASS_$_HKUnitPreferenceController
+ __HKPrivateMetadataKeyHearingTestTakenWithRightEarNoiseLevel
+ _HKFeatureAvailabilityRequirementIdentifierCountryIsSupportedOnLocalDevice
+ _OBJC_CLASS_$_NSNumberFormatter
+ _UIGraphicsPushContext
+ _HKUIAutomationIdentifierPrefix
+ _OBJC_CLASS_$_HKFeatureStatusManager
+ _HKFeatureAvailabilityContextHearingTestPromptTileVisibility
+ _OBJC_CLASS_$_UIBarButtonItem
+ _HKSampleSortIdentifierStartDate
+ _OBJC_CLASS_$_HKAudiogramSensitivityTest
+ __HKPrivateMetadataKeyHearingTestTakenWithLeftEarNoiseLevel
+ _OBJC_CLASS_$_HKHealthChartFactory
+ _swift_deletedAsyncMethodErrorTu
+ _swift_release_n
+ _swift_getTupleTypeMetadata
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _OBJC_CLASS_$_HKQuery
+ _OBJC_CLASS_$_HKSample
+ _OBJC_CLASS_$_HKQueryDescriptor
+ _objc_retain_x3
+ _HKHearingLevelClassificationForSensitivity
+ __HKPrivateMetadataKeyHearingTestTakenFromFirstParty
+ _CGContextAddPath
+ _HKLocalizedStringForUpperClampedValueAndUnit
+ _OBJC_CLASS_$_NSDateFormatter
+ _objc_release_x10
+ __HKPrivateMetadataKeyHearingTestTakenWithCongestion
+ _HKFeatureAvailabilityRequirementIdentifierSeedIsNotExpired
+ __swift_FORCE_LOAD_$_swiftModelIO
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ _OBJC_CLASS_$_UIButton
+ _CGContextDrawPath
+ _OBJC_CLASS_$_NSTextAttachment
+ __swift_FORCE_LOAD_$_swiftGLKit
+ _swift_getOpaqueTypeMetadata2
+ _OBJC_CLASS_$_HKAudiogramSensitivityPoint
+ __HKPrivateMetadataKeyHearingTestTakenWithRecentLoudNoiseExposure
+ _CGContextSaveGState
+ _HKCountryCodeUnknownCountry
+ _OBJC_CLASS_$_LSApplicationWorkspace
CStrings:
+ "[%!{(MISSING)public}s] Did tap Hearing Features in Settings."
+ "@\"UIViewController\"16@0:8"
+ "HearingAppPlugin-Localizable-Yodel"
+ "URLForResource:withExtension:"
+ "init(nibName:bundle:)"
+ "rescindedState(from:)"
+ "HEARING_TEST_PDF_BUTTON_TITLE"
+ "colorWithAlphaComponent:"
+ "localizedIngestionSource"
+ "HEARING_TEST_PDF_OVERVIEW_DESCRIPTION"
+ "[%!{(MISSING)public}s] Got nil result from classification utility"
+ "SECTION4_LIST_ITEM6"
+ "CGContext"
+ "HEARING_TEST_PDF_PREVIEW_TITLE"
+ "SECTION1_PARAGRAPH2_HEADER"
+ "_TtC16HearingAppPlugin43AudiogramPDFJapanDisclaimerPageNumberedPage"
+ "capturedInitialQueryAnalytics"
+ "hearingTestFeatureStatus"
+ "HEARING_TEST_PDF_METADATA_VALUE_NO"
+ "showViewController:sender:"
+ "square.and.arrow.up"
+ "averageSensitivity"
+ "initWithNibName:bundle:"
+ "$__lazy_storage_$_shareBarButtonItem"
+ "lower upper "
+ "HEARING_TEST_RESCINDED_FEED_ITEM_TITLE"
+ "stringFromNumber:"
+ "[%!{(MISSING)public}s] Unable to determine chart x scale domain"
+ "initWithCollectionViewLayout:"
+ "initWithSampleType:predicate:"
+ "SECTION1_PARAGRAPH6"
+ "rightEarAnnotationIndex"
+ "safeAreaLayoutGuide"
+ "ONBOARDING_SHOULD_KNOW_ITEM_1_TITLE"
+ "_TtC16HearingAppPlugin25AudiogramShowAllComponent"
+ "lowerBound"
+ "$__lazy_storage_$_exportPDFButton"
+ "setDistribution:"
+ "SECTION4_LIST_ITEM5"
+ "_TtC16HearingAppPlugin26HearingTestArticleProvider"
+ "HEARING_TEST_ADD_TEST"
+ "HERTZ_NUMBERLESS_UNIT"
+ "SECTION4_PARAGRAPH2"
+ "AllHearingResultsButton"
+ "SECTION4_LIST_ITEM9"
+ "edgeInsetsForWidthDesignation:"
+ "stringFromDate:"
+ "HEARING_TEST_PDF_FOOTNOTE_JAPAN_DISCLAIMER"
+ "_TtP13HearingTestUI27HearingTestArticleProviding_"
+ "HEARING_TEST_PDF_CONGESTION"
+ "pdfProvider"
+ "setMaximumFractionDigits:"
+ "leftEarAnnotationIndex"
+ "AudiogramAllDataChartView"
+ "systemPinkColor"
+ "HEARING_TEST_PROMOTION_TILE_TITLE"
+ "SECTION4_LIST_ITEM7"
+ "cancellable"
+ "makePromptFeedItem(sourceProfile:featureStatus:)"
+ "remoteDisable"
+ "defaultWorkspace"
+ "makePromotionTileConfiguration(from:)"
+ "[%!{(MISSING)public}s.%!{(MISSING)public}s]: Hearing Test prompt tile requirement was not met for feature status %!{(MISSING)public}s"
+ "automationIdentifierBase"
+ "chartController"
+ "_TtC16HearingAppPlugin37HearingTestPromotionViewActionHandler"
+ "didMoveToParentViewController:"
+ "setBounds:"
+ "JAPAN_SECTION_DESCRIPTION"
+ "ONBOARDING_SHOULD_KNOW_TITLE"
+ "HEARING_TEST_PDF_METADATA_VALUE_YES"
+ "SECTION4_LIST_ITEM1"
+ "size"
+ "HearingTest.prompt.feedItem"
+ "hearingLossArticleViewController"
+ "HEARING_TEST_PDF_FILE_NAME"
+ "unsatisfiedRequirementIdentifiers"
+ "configurationByApplyingConfiguration:"
+ "setDirectionalLayoutMargins:"
+ "hearingLevelSummary"
+ "init(collectionViewLayout:)"
+ "predicateForSamplesWithStartDate:endDate:options:"
+ "regionGated"
+ "AudiogramEducation-Localizable-Yodel"
+ "SECTION3_PARAGRAPH4"
+ "addArrangedSubview:"
+ "analyticsManager"
+ "Hearing Features in Settings has not been implemented yet."
+ "systemImageNamed:"
+ "capHeight"
+ "ONBOARDING_SHOULD_KNOW_ITEM_3_TITLE"
+ "initWithKey:ascending:"
+ "[%!{(MISSING)public}s] PDF Configuration Row not found for row %!{(MISSING)public}ld"
+ "staticAudiogramChartViewControllerWithAudiogramSample:hideEnhancedUI:"
+ "HEARING_TEST_PDF_SHARE_ACTION_TITLE"
+ "SECTION4_LIST_ITEM8"
+ "HearingTest.promotion.feedItem"
+ "setContentHorizontalAlignment:"
+ "shareButtonTapped:"
+ "HEARING_TEST_PDF_CONTEXT_PILL_RIGHT"
+ "averageLeftEarSensitivity"
+ "ear.badge.magnifyingglass"
+ "HEARING_TEST_PDF_FOOTNOTE_"
+ "_PARTY_UPPER_CLAMPING"
+ "_TtC16HearingAppPlugin34HearingTestPromptTileActionHandler"
+ "_PARTY_LOWER_CLAMPING"
+ "startInitialAudiogramPublisherTime"
+ "didTapExportAll:"
+ "rightEarMetrics"
+ "tintColor"
+ "HEARING_TEST_PDF_LONGITUDINAL_CHART_TITLE"
+ "HEARING_TEST_PDF_YEAR_RANGE"
+ "SECTION4_LIST_ITEM2"
+ "[%!s(MISSING)] Failed to encode PromptTileView.ViewModel for Hearing Test Prompt Tile. Failed to create a feed item with error: %!s(MISSING)"
+ "whiteColor"
+ "_TtC16HearingAppPlugin35AudiogramAllDataChartViewController"
+ "audiogramSampleSubject"
+ "HEARING_TEST_RESCINDED_LINK"
+ "textAttachmentWithImage:"
+ "_TtC16HearingAppPlugin25AudiogramAllDataViewModel"
+ "HEARING_TEST_PDF_INGESTION_SOURCE"
+ "averageRightEarSensitivity"
+ "initWithFeatureIdentifier:healthStore:"
+ "HEARING_TEST_ALL_RESULTS_CELL_TEXT_%!@(MISSING)%!@(MISSING)"
+ "metadata"
+ "setAccessibilityIdentifier:"
+ "startDate"
+ "tests"
+ "HEARING_TEST_ALL_RESULTS_DECIBEL_TEXT_%!@(MISSING)"
+ "HearingAppPlugin.AudiogramAllDataChartViewController"
+ "HearingAppPlugin/AudiogramAllDataViewController.swift"
+ "debounceForSelectedItemInSeconds"
+ "openSensitiveURL:withOptions:"
+ "yodel"
+ "setNumberStyle:"
+ "view"
+ "_TtC16HearingAppPlugin30AudiogramAllDataViewController"
+ "showPromotionTile(from:)"
+ "SECTION3_PARAGRAPH3"
+ "SECTION4_LIST_ITEM4"
+ "isRequirementSatisfiedWithIdentifier:"
+ "HEARING_TEST_PDF_SENSITIVITY_POINT_VALUE_UPPER_CLAMPING"
+ "removeFromSuperview"
+ "appendAttributedString:"
+ "HEARING_TEST_PROMOTION_TILE_BUTTON"
+ "endDate"
+ "ONBOARDING_SHOULD_KNOW_ITEM_2_TITLE"
+ "[%!s(MISSING).%!s(MISSING)]: Returning remoteDisable state from unavailability %!s(MISSING)"
+ "[%!s(MISSING).%!s(MISSING)]: Feed item created with state %!s(MISSING)"
+ "upperBound"
+ "HEARING_TEST_PDF_AUDIOGRAM_TITLE"
+ "HEARING_TEST_PDF_DBHL"
+ "v32@0:8@16@?24"
+ "HearingTest.rescinded.feedItem"
+ "scrollViewContainer"
+ "CGColor"
+ "HearingAppPlugin.AudiogramAllDataViewController"
+ "SECTION1_PARAGRAPH5_HEADER"
+ "[%!s(MISSING).%!s(MISSING)]: Feed item will be marked for deletion given no unavailability reasons"
+ "v32@0:8@\"_TtC13HearingTestUI29HearingTestMainViewController\"16@?<v@?@\"HKAudiogramSample\">24"
+ "SECTION4_PARAGRAPH1_LEARN_MORE"
+ "_TtC16HearingAppPlugin35AudiogramPDFOverviewSectionProvider"
+ "containSensitivityPointsIsMasked:forSide:"
+ "%!{(MISSING)public}s: Failed to create frequency formatter"
+ "audiogramAllDataViewModel"
+ "setRightBarButtonItem:"
+ ".AudiogramLongitudinalPDFChartView"
+ "AudiogramAllData"
+ "HEARING_TEST_PDF_RECENT_LOUD_NOISE_EXPOSURE"
+ "[[%!{(MISSING)public}s] Cannot open hearing test with path components: %!{(MISSING)public}s"
+ "setTimeStyle:"
+ "userInterfaceLayoutDirectionForSemanticContentAttribute:"
+ "Failed to encode userData: %!s(MISSING)"
+ "KILOHERTZ_NUMBERLESS_UNIT"
+ "addChildViewController:"
+ "AudiogramShowAllComponent"
+ "HEARING_TEST_PDF_CONTEXT_PILL_LEFT"
+ "ShowAllAudiogramsSampleSampleDetails"
+ "hk_hearingHealthAudiogramLeftEarLineColor"
+ "HEARING_TEST_PROMOTION_TILE_DETAIL"
+ "[%!{(MISSING)public}s] Presenting Hearing Test."
+ "_TtC16HearingAppPlugin36AudiogramPDFAudiogramSectionProvider"
+ "hearing_aid_article_background"
+ "[%!s(MISSING)] Failed to encode PromptTileView.ViewModel for Hearing Test Rescinded Tile. Failed to create a feed item with error: %!s(MISSING)"
+ "[%!{(MISSING)public}s] Hearing Test not available due to error: %!{(MISSING)public}@"
+ "none"
+ "selectedConfiguration"
+ "HEARING_TEST_ALL_RESULTS_BUTTON_TITLE"
+ "audiogramSample"
+ "masked"
+ "HEARING_FEATURES_IN_SETTINGS_PROMOTION_TILE_TITLE"
+ "HearingAppPlugin/AudiogramAllDataChartViewController.swift"
+ "_TtC16HearingAppPlugin39AudiogramPDFLongitudinalChartDataSource"
+ "requestType"
+ "shareButtonBehavior"
+ "HearingAppPlugin1"
+ "[%!{(MISSING)public}s.%!{(MISSING)public}s]: Hearing Test promotion tile requirement was not met for feature status %!{(MISSING)public}s"
+ "sampleType"
+ "[%!s(MISSING)]: Opening %!s(MISSING), success: %!s(MISSING)"
+ "leftEarMetrics"
+ "makeFeedItem(sourceProfile:state:)"
+ "setDelegate:"
+ "[%!s(MISSING).%!s(MISSING)]: Non-primary source"
+ "hk_hearingHealthAudiogramRightEarLineColor"
+ "footerProvider"
+ "headerProvider"
+ "HEARING_TEST_ABOUT_BUTTON_TITLE"
+ "HearingAidsEducation-Localizable-Yodel"
+ "scrollView"
+ "_TtP13HearingTestUI39HearingTestAudiogramImportFlowProviding_"
+ "[%!{(MISSING)public}s.%!{(MISSING)public}s]: Creating promo tile action handler user data object"
+ "chartModel"
+ "configurationWithPointSize:"
+ "HEARING_TEST_PDF_LEFT_EAR_NOISE_LEVEL"
+ "[%!s(MISSING).%!s(MISSING)]: Feed item will not be created given onboarding and feature enabled status"
+ "HEARING_TEST_PDF_RIGHT_EAR_NOISE_LEVEL"
+ "navigationItem"
+ "[%!s(MISSING).%!s(MISSING)]: Returning regionGated state from unavailability %!s(MISSING)"
+ "makeActionHandlerUserDataObject(context:)"
+ "[%!{(MISSING)public}s.%!{(MISSING)public}s]: Creating prompt tile configuration for feature status %!{(MISSING)public}s"
+ "hk_appTintColor"
+ "seedExpiry"
+ "HEARING_TEST_PDF_SELECTION_ALL"
+ "HearingTestTileFeedItemFactory"
+ "_TtC16HearingAppPlugin26AudiogramPDFAudiogramChart"
+ "HEARING_TEST_ALL_RESULTS_TITLE"
+ "HEARING_TEST_PDF_SENSITIVITY_POINT_VALUE_LOWER_CLAMPING"
+ "sensitivity"
+ "_TtC16HearingAppPlugin40AudiogramPDFAsyncConfigurationDataSource"
+ "setModalPresentationStyle:"
+ "setShowsHorizontalScrollIndicator:"
+ "HEARING_TEST_RESCINDED_FEED_ITEM_ACTION"
+ "didTapImportAudiogramLinkIn:completion:"
+ "HearingTestRescinded"
+ "initWithImage:options:"
+ "isAverageSensitivityUpperClampedForSide:"
+ "AudiogramPDFItem"
+ "characteristicsProvider"
+ "arrangedSubviews"
+ "clampedSensitivity"
+ "constraintEqualToAnchor:constant:"
+ "SECTION2_PARAGRAPH2_LEARN_MORE"
+ "init(dataSource:)"
+ "_TtC16HearingAppPlugin20AudiogramPDFProvider"
+ "clearColor"
+ "com.apple.health.Education.HearingAids"
+ "[%!{(MISSING)public}s] Error fetching db changes: %!{(MISSING)public}s"
+ "doubleValueForUnit:"
+ "HEARING_TEST_PDF_OVERVIEW_TITLE"
+ "systemBlueColor"
+ "unitTest_didPublishAudiograms"
+ "HEARING_TEST_ALL_RESULTS_EXPORT_PDF"
+ "PDF page is too small to render all elements. Elements will be clipped."
+ "[%!{(MISSING)public}s] PDF Configuration cannot determine first date of ten years ago"
+ "addTarget:action:forControlEvents:"
+ "localizedDisplayNameForUnit:value:"
+ "HEARING_TEST_PDF_SHARE_ACTION_BUTTON_TITLE"
+ "HearingTestRescindedFeedItemFactory"
+ "_TtC16HearingAppPlugin55HearingFeaturesInSettingsPromotionTileViewActionHandler"
+ "configurationWithHierarchicalColor:"
+ "setLayoutMarginsRelativeArrangement:"
+ "HearingAidsHelpMoreThanYourHearing"
+ "frequency"
+ "setDateStyle:"
+ "[%!{(MISSING)public}s] Failed to format filter value for type: %!s(MISSING)"
+ "buttonWithType:"
+ "_TtC16HearingAppPlugin37HearingTestRescindedTileActionHandler"
+ "HEARING_TEST_DATATYPE_ROOM_TITLE"
+ "SECTION4_LIST_ITEM3"
+ "_TtC16HearingAppPlugin51HearingFeaturesInSettingsPromotionGeneratorPipeline"
+ "attributedStringWithAttachment:"
+ "HearingHealthEducation-Localizable-Yodel"
+ "_TtC16HearingAppPlugin29AudiogramPDFLongitudinalChart"
+ "clampingRange"
+ "HEARING_TEST_PDF_SHARE_ACTION_DESCRIPTION"
+ "HEARING_TEST_RESCINDED_FEED_ITEM_BODY"
+ "[%!{(MISSING)public}s] Error fetching sample counts: %!{(MISSING)public}s"
+ "bottomPadding"
+ "HEARING_TEST_PREVIEW_PDF_MOST_RECENT"
+ "showPromptTile(from:)"
+ "audiogram_ear_message_image"
+ "sensitivityPoints"
+ "SECTION2_PARAGRAPH4"
+ "Error fetching audiogram samples: %!{(MISSING)public}s"
+ "HEARING_TEST_ALL_RESULTS_CLASSIFICATION_DECIBEL_TEXT_%!@(MISSING)%!@(MISSING)"
+ "HEARING_TEST_PDF_THINGS_YOU_SHOULD_KNOW_NUMBERED_LIST_JOINER"
+ "item cellType "
+ "_TtC16HearingAppPlugin27AudiogramPDFChartDataSource"
+ " options caption accessibilityDescription playVisibilityPercentage "
+ "[%!s(MISSING).%!s(MISSING)]: Returning seedExpiry state from unavailability %!s(MISSING)"
+ "[%!{(MISSING)public}s.%!{(MISSING)public}s]: Creating promo tile configuration for feature status %!{(MISSING)public}s"
+ "areAllRequirementsSatisfied"
+ "dataSource"
+ "@32@0:8@16@24"
+ "hertzUnit"
+ "side"
- "SECTION1_PARAGRAPH3_LEARN_MORE"

```
