## SafariSharedUI

> `/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI`

```diff

-616.2.9.10.13
-  __TEXT.__text: 0x16effc
-  __TEXT.__auth_stubs: 0x1430
-  __TEXT.__objc_methlist: 0xc81c
-  __TEXT.__gcc_except_tab: 0x1ebd0
+617.1.17.10.9
+  __TEXT.__text: 0x16f048
+  __TEXT.__auth_stubs: 0x1440
+  __TEXT.__objc_methlist: 0xc7a4
+  __TEXT.__gcc_except_tab: 0x1ea60
   __TEXT.__const: 0xd70
-  __TEXT.__cstring: 0x18207
-  __TEXT.__oslogstring: 0xae31
+  __TEXT.__cstring: 0x18267
+  __TEXT.__oslogstring: 0xaf81
   __TEXT.__ustring: 0x1f00
   __TEXT.__dlopen_cstrs: 0x3f8
-  __TEXT.__unwind_info: 0x9cf8
+  __TEXT.__unwind_info: 0x9c84
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x27f6
-  __TEXT.__objc_methname: 0x30eed
-  __TEXT.__objc_methtype: 0x79c0
-  __TEXT.__objc_stubs: 0x1c4c0
-  __DATA_CONST.__got: 0x7d0
-  __DATA_CONST.__const: 0x7258
-  __DATA_CONST.__objc_classlist: 0x7c0
-  __DATA_CONST.__objc_catlist: 0xe8
+  __TEXT.__objc_classname: 0x27ae
+  __TEXT.__objc_methname: 0x310d7
+  __TEXT.__objc_methtype: 0x77c2
+  __TEXT.__objc_stubs: 0x1c640
+  __DATA_CONST.__got: 0x7c8
+  __DATA_CONST.__const: 0x7430
+  __DATA_CONST.__objc_classlist: 0x7a8
+  __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x18d80
-  __DATA_CONST.__objc_selrefs: 0x8bb0
-  __DATA_CONST.__objc_arraydata: 0x2160
-  __AUTH_CONST.__objc_const: 0x61d0
-  __AUTH_CONST.__cfstring: 0x176e0
-  __AUTH_CONST.__const: 0x3c08
-  __AUTH_CONST.__objc_intobj: 0xc18
+  __DATA_CONST.__objc_const: 0x189f0
+  __DATA_CONST.__objc_selrefs: 0x8c30
+  __DATA_CONST.__objc_arraydata: 0x2150
+  __AUTH_CONST.__objc_const: 0x60b8
+  __AUTH_CONST.__cfstring: 0x17580
+  __AUTH_CONST.__const: 0x3a48
+  __AUTH_CONST.__objc_intobj: 0xc48
   __AUTH_CONST.__objc_arrayobj: 0x888
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x370
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xa30
-  __AUTH.__objc_data: 0x49c0
+  __AUTH_CONST.__auth_got: 0xa38
+  __AUTH.__objc_data: 0x48d0
   __AUTH.__data: 0x70
   __DATA.__got_weak: 0xd0
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0xca0
-  __DATA.__objc_superrefs: 0x590
-  __DATA.__objc_ivar: 0x1384
-  __DATA.__data: 0x1f68
-  __DATA.__bss: 0x1040
+  __DATA.__objc_protorefs: 0x28
+  __DATA.__objc_classrefs: 0xc78
+  __DATA.__objc_superrefs: 0x578
+  __DATA.__objc_ivar: 0x1364
+  __DATA.__data: 0x1f78
+  __DATA.__bss: 0x1050
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x29

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7535
-  Symbols:   27015
-  CStrings:  11746
+  Functions: 7528
+  Symbols:   26982
+  CStrings:  11749
 
Symbols:
+ +[UIImage(SafariSharedExtras) safari_largestSizedBitmapImageOrSVGFromImages:]
+ +[WBSApplicationManifestFetcher _longestEdgeForIcon:]
+ +[WBSApplicationManifestFetcher _preferredPurposeForIcons:]
+ +[WBSApplicationManifestFetcher _primaryPurposeForPurposes:]
+ +[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]
+ +[WBSTouchIconRequest requestWithTitle:url:minimumIconSize:maximumIconSize:monogramConfiguration:options:]
+ +[_WKApplicationManifest(SafariSharedUIExtras) _manifestWithInfoDictionary:withSynthesizedProperties:]
+ +[_WKApplicationManifest(SafariSharedUIExtras) _manifestWithInfoDictionary:withSynthesizedProperties:].cold.1
+ +[_WKApplicationManifest(SafariSharedUIExtras) safari_manifestWithInfoDictionary:]
+ -[NSString(SafariSharedUIExtras) safari_stringHasLeadingEmoji:]
+ -[SFSearchResult(SafariSharedExtras) uuidString]
+ -[UIImage(SafariSharedExtras) safari_longestEdgeInPixels]
+ -[UIImage(SafariSharedExtras) safari_setThemeColor:]
+ -[UIImage(SafariSharedExtras) safari_themeColor]
+ -[WBSAction accessibilityIdentifier]
+ -[WBSAction setAccessibilityIdentifier:]
+ -[WBSParsecDSession _didReceiveResponse:error:forTask:query:].cold.2
+ -[WBSParsecSearchResult imageURL]
+ -[WBSSVGImageRenderingFetchOperation _didRenderImage:]
+ -[WBSSVGImageRenderingFetchOperation _takeSnapshotAndFinish]
+ -[WBSSVGImageRenderingFetchOperation didFinishNavigation]
+ -[WBSSafariExtension dealloc]
+ -[WBSStartPageBackgroundManager normalizeImage:properties:]
+ -[WBSStartPageSection icon]
+ -[WBSStartPageSection setIcon:]
+ -[WBSTouchIconRequest initWithTitle:url:minimumIconSize:maximumIconSize:monogramConfiguration:options:]
+ -[WBSTouchIconRequest monogramConfiguration]
+ -[WBSWKDataTaskDelegate .cxx_destruct]
+ -[WBSWKDataTaskDelegate dataTask:didCompleteWithError:]
+ -[WBSWKDataTaskDelegate dataTask:didReceiveData:]
+ -[WBSWKDataTaskDelegate didCompleteWithError]
+ -[WBSWKDataTaskDelegate didReceiveData]
+ -[WBSWKDataTaskDelegate setDidCompleteWithError:]
+ -[WBSWKDataTaskDelegate setDidReceiveData:]
+ -[WBSWebExtensionInjectedContentData removeWKUserScriptsFromUserContentController:]
+ -[WBSWebExtensionInjectedContentData removeWKUserStyleSheetsFromUserContentController:]
+ -[WBSWebProcessPlugIn abGroupIdentifier]
+ -[WBSWebProcessPlugIn isABTestingEnabled]
+ -[WBSWebViewMetadataFetchOperation didFinishNavigation]
+ -[WBSWebViewMetadataFetchOperation webView:didFinishNavigation:]
+ -[WBSWebViewMetadataFetchOperation webViewWebContentProcessDidTerminate:]
+ -[_WKApplicationManifest(SafariSharedUIExtras) safari_dictionaryRepresentation].cold.1
+ -[_WKApplicationManifest(SafariSharedUIExtras) safari_iconKind]
+ -[_WKApplicationManifest(SafariSharedUIExtras) safari_scope]
+ -[_WKApplicationManifest(SafariSharedUIExtras) safari_setIconKind:]
+ GCC_except_table208
+ GCC_except_table216
+ GCC_except_table223
+ GCC_except_table246
+ GCC_except_table250
+ GCC_except_table302
+ GCC_except_table339
+ GCC_except_table385
+ GCC_except_table386
+ GCC_except_table391
+ GCC_except_table393
+ GCC_except_table394
+ GCC_except_table400
+ GCC_except_table406
+ GCC_except_table407
+ GCC_except_table413
+ _CGDataProviderRelease
+ _CTLineCreateWithString
+ _CTRunGetStringRange
+ _OBJC_CLASS_$_WBSCGImage
+ _OBJC_CLASS_$_WBSWKDataTaskDelegate
+ _OBJC_IVAR_$_WBSAction._accessibilityIdentifier
+ _OBJC_IVAR_$_WBSParsecSearchResult._imageURL
+ _OBJC_IVAR_$_WBSStartPageSection._icon
+ _OBJC_IVAR_$_WBSTouchIconRequest._monogramConfiguration
+ _OBJC_IVAR_$_WBSWKDataTaskDelegate._didCompleteWithError
+ _OBJC_IVAR_$_WBSWKDataTaskDelegate._didReceiveData
+ _OBJC_METACLASS_$_WBSWKDataTaskDelegate
+ _WBSWKApplicationManifestIconKindCustomIcon
+ _WBSWKApplicationManifestIconKindFavicon
+ _WBSWKApplicationManifestIconKindManifestIcon
+ _WBSWKApplicationManifestIconKindMonogram
+ _WBSWKApplicationManifestIconKindRootLevelKey
+ _WBSWKApplicationManifestIconKindTouchIcon
+ _WBSWKApplicationManifestLegacyIsSynthesizedRootLevelKey
+ _WBSWKApplicationManifestURLRootLevelKey
+ _WBSWebProcessPlugInABGroupIdentifierKey
+ _WBSWebProcessPlugInABTestingEnabledKey
+ __OBJC_$_CLASS_METHODS_WBSApplicationManifestFetcher
+ __OBJC_$_INSTANCE_METHODS_WBSWKDataTaskDelegate
+ __OBJC_$_INSTANCE_VARIABLES_WBSWKDataTaskDelegate
+ __OBJC_$_PROP_LIST_WBSParsecSearchResult.225
+ __OBJC_$_PROP_LIST_WBSParsecSearchSimpleResult.83
+ __OBJC_$_PROP_LIST_WBSWKDataTaskDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__WKDataTaskDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__WKDataTaskDelegate
+ __OBJC_$_PROTOCOL_REFS__WKDataTaskDelegate
+ __OBJC_CLASS_PROTOCOLS_$_WBSWKDataTaskDelegate
+ __OBJC_CLASS_RO_$_WBSWKDataTaskDelegate
+ __OBJC_LABEL_PROTOCOL_$__WKDataTaskDelegate
+ __OBJC_METACLASS_RO_$_WBSWKDataTaskDelegate
+ __OBJC_PROTOCOL_$__WKDataTaskDelegate
+ __ZGVZL33parsedShortcutForManifestShortcutP8NSStringE28upperCaseEnglishCharacterSet
+ __ZL13themeColorKey
+ __ZZL33parsedShortcutForManifestShortcutP8NSStringE28upperCaseEnglishCharacterSet
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.469.cold.1
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.470.cold.1
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.471
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.472
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke_2.476
+ ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke_2.476.cold.1
+ ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke
+ ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke.76
+ ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke.98
+ ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke_2
+ ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke_2.78
+ ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke_3
+ ___113+[WBSApplicationManifestFetcher downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:]_block_invoke_3.80
+ ___113-[WBSWebExtensionDeclarativeNetRequestRule _webKitRuleWithWebKitActionType:chromeActionType:chromeResourceTypes:]_block_invoke_3
+ ___50-[WBSWebExtensionData _loadBackgroundPageWithURL:]_block_invoke.567
+ ___60-[WBSParsecDSession _setCurrentQuery:withKeyboardInputType:]_block_invoke.30
+ ___60-[WBSSVGImageRenderingFetchOperation _takeSnapshotAndFinish]_block_invoke
+ ___60-[WBSSVGImageRenderingFetchOperation _takeSnapshotAndFinish]_block_invoke.26
+ ___60-[WBSSVGImageRenderingFetchOperation _takeSnapshotAndFinish]_block_invoke.26.cold.1
+ ___60-[WBSSVGImageRenderingFetchOperation _takeSnapshotAndFinish]_block_invoke.cold.1
+ ___60-[WBSSVGImageRenderingFetchOperation _takeSnapshotAndFinish]_block_invoke.cold.2
+ ___65-[WBSPrivacyReportData _loadDataForWebViewWithCompletionHandler:]_block_invoke_2
+ ___66-[WBSReaderFont(SafariSharedUI) isInstalledWithCompletionHandler:]_block_invoke_2
+ ___69-[WBSTranslationContext _updateProgressWithTranslatedParagraphCount:]_block_invoke.119
+ ___69-[WBSTranslationContext _updateProgressWithTranslatedParagraphCount:]_block_invoke.119.cold.1
+ ___75-[WBSTranslationContext _setState:usingLock:validatingTransitionIsAllowed:]_block_invoke.87
+ ___75-[WBSTranslationContext _setState:usingLock:validatingTransitionIsAllowed:]_block_invoke.88
+ ___76-[WBSTranslationContext _updateProgressForFinishingInitialContentExtraction]_block_invoke.120
+ ___77+[WBSParsecDSession _updateAutoFillTLDsIfNeededForSession:completionHandler:]_block_invoke.51
+ ___77+[WBSParsecDSession _updateAutoFillTLDsIfNeededForSession:completionHandler:]_block_invoke.51.cold.1
+ ___77+[WBSParsecDSession _updateAutoFillTLDsIfNeededForSession:completionHandler:]_block_invoke.51.cold.2
+ ___77-[WBSWebExtensionsController postMessage:fromPortWithID:fromExtensionWithID:]_block_invoke.296
+ ___78-[WBSExtensionsController writeExtensionsStateToStorageWithCompletionHandler:]_block_invoke.30
+ ___79-[WBSWebExtensionsController _deleteStorageForExtensionWithComposedIdentifier:]_block_invoke.169
+ ___80-[WBSParsecDSession _startUpdatingAutoFillDataInBackgroundIfPossibleForSession:]_block_invoke.46
+ ___80-[WBSParsecDSession _startUpdatingAutoFillDataInBackgroundIfPossibleForSession:]_block_invoke.46.cold.1
+ ___80-[WBSParsecDSession _startUpdatingAutoFillDataInBackgroundIfPossibleForSession:]_block_invoke.47
+ ___80-[WBSParsecDSession _startUpdatingAutoFillDataInBackgroundIfPossibleForSession:]_block_invoke_2.48
+ ___82-[WBSStartPageBackgroundManager _setImageOnAnyQueue:withAppearance:forIdentifier:]_block_invoke_3
+ ___84-[WBSTranslationContext _promptIfNeededToConsentToTranslationWithCompletionHandler:]_block_invoke.93
+ ___84-[WBSWebExtensionData loadRegisteredContentScriptsFromStorageWithCompletionHandler:]_block_invoke.485
+ ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke.417
+ ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke.421
+ ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke.421.cold.1
+ ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke_2.418
+ ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke_2.418.cold.1
+ ___87+[WBSParsecDSession _updateAutoFillCorrectionSetsIfNeededForSession:completionHandler:]_block_invoke.53
+ ___87+[WBSParsecDSession _updateAutoFillCorrectionSetsIfNeededForSession:completionHandler:]_block_invoke.53.cold.1
+ ___87+[WBSParsecDSession _updateAutoFillCorrectionSetsIfNeededForSession:completionHandler:]_block_invoke.53.cold.2
+ ___87+[WBSParsecDSession _updateAutoFillCorrectionSetsIfNeededForSession:completionHandler:]_block_invoke.53.cold.3
+ ___87-[WBSExtensionsController setExtension:isEnabled:dueToUserGesture:skipSavingToStorage:]_block_invoke.35
+ ___89-[WBSStartPageBackgroundManager _prefetchImage:luminance:completion:withNanoSecondDelay:]_block_invoke_2
+ ___91-[WBSWebExtensionsController _loadPermissionsFromStorageForWebExtension:completionHandler:]_block_invoke.300
+ ____ZL25_analyzeImageTransparencyP7CGImage_block_invoke_4
+ ___block_descriptor_176_ea8_32s40s48s56bs_e20_v16?0^{CGContext=}8ls32l8s56l8s40l8s48l8
+ ___block_descriptor_40_e36_B16?0"_WKApplicationManifestIcon"8l
+ ___block_descriptor_40_e8_32r_e32_v24?0"_WKDataTask"8"NSData"16lr32l8
+ ___block_descriptor_40_e8_32w_e29_v24?0"UIImage"8"NSError"16lw32l8
+ ___block_descriptor_40_ea8_32s_e45_v32?0"NSNumber"8?<v?"WBSCGImage"B>16^B24ls32l8
+ ___block_descriptor_48_e8_32s40w_e20_v24?08"NSError"16lw40l8s32l8
+ ___block_descriptor_52_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e37_v28?0"NSURL"8"NSMutableArray"16B24ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e21_v16?0"_WKDataTask"8ls32l8s40l8s48l8
+ ___block_descriptor_57_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56r_e33_v24?0"_WKDataTask"8"NSError"16lr56l8s32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_74_ea8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.109
+ ___block_literal_global.123
+ ___block_literal_global.152
+ ___block_literal_global.198
+ ___block_literal_global.209
+ ___block_literal_global.240
+ ___block_literal_global.256
+ ___block_literal_global.293
+ ___block_literal_global.298
+ ___block_literal_global.305
+ ___block_literal_global.338
+ ___block_literal_global.352
+ ___block_literal_global.449
+ ___block_literal_global.484
+ ___block_literal_global.487
+ ___block_literal_global.495
+ ___block_literal_global.506
+ ___block_literal_global.509
+ ___block_literal_global.521
+ ___block_literal_global.542
+ ___block_literal_global.560
+ ___block_literal_global.66
+ ___block_literal_global.770
+ ___block_literal_global.86
+ __unnamed_array_storage.130
+ __unnamed_array_storage.1359
+ __unnamed_array_storage.1494
+ __unnamed_array_storage.26
+ __unnamed_array_storage.306
+ __unnamed_array_storage.360
+ __unnamed_array_storage.361
+ __unnamed_array_storage.364
+ __unnamed_array_storage.376
+ __unnamed_array_storage.409
+ __unnamed_array_storage.412
+ __unnamed_array_storage.413
+ __unnamed_array_storage.423
+ __unnamed_array_storage.426
+ __unnamed_array_storage.429
+ __unnamed_array_storage.765
+ __unnamed_array_storage.93
+ _objc_msgSend$_dataTaskWithRequest:completionHandler:
+ _objc_msgSend$_didRenderImage:
+ _objc_msgSend$_isSingleEmoji
+ _objc_msgSend$_longestEdgeForIcon:
+ _objc_msgSend$_manifestWithInfoDictionary:withSynthesizedProperties:
+ _objc_msgSend$_preferredPurposeForIcons:
+ _objc_msgSend$_primaryPurposeForPurposes:
+ _objc_msgSend$_setHiddenPageDOMTimerThrottlingEnabled:
+ _objc_msgSend$_setUsesTransparentBackground:
+ _objc_msgSend$_takeSnapshotAndFinish
+ _objc_msgSend$_webViewWebProcessDidCrash:
+ _objc_msgSend$appendData:
+ _objc_msgSend$characterSetWithRange:
+ _objc_msgSend$didFinishNavigation
+ _objc_msgSend$evaluateJavaScript:completionHandler:
+ _objc_msgSend$iconType
+ _objc_msgSend$imageByAdoptingCGImage:
+ _objc_msgSend$initWithTitle:url:minimumIconSize:maximumIconSize:monogramConfiguration:options:
+ _objc_msgSend$isDefaultScope
+ _objc_msgSend$isSearchEvaluationLoggingEnabled
+ _objc_msgSend$isSpeculative
+ _objc_msgSend$normalizeImage:properties:
+ _objc_msgSend$preferredFormat
+ _objc_msgSend$rawJSON
+ _objc_msgSend$removeWKUserScriptsFromUserContentController:
+ _objc_msgSend$removeWKUserStyleSheetsFromUserContentController:
+ _objc_msgSend$safari_hostDomainsEnumerator
+ _objc_msgSend$safari_isSVGImage
+ _objc_msgSend$safari_largestSizedBitmapImageOrSVGFromImages:
+ _objc_msgSend$safari_longestEdgeInPixels
+ _objc_msgSend$safari_scope
+ _objc_msgSend$safari_setIconKind:
+ _objc_msgSend$safari_setImages:
+ _objc_msgSend$safari_setThemeColor:
+ _objc_msgSend$safari_themeColor
+ _objc_msgSend$safari_urlHashesOfComponents
+ _objc_msgSend$setDidCompleteWithError:
+ _objc_msgSend$setDidReceiveData:
+ _objc_msgSend$setInactiveSchedulingPolicy:
+ _objc_msgSend$uuidString
+ _resolvedDisplayModeForURL
+ _safariIconKindKey
+ _safariScopeKey
- +[WBSParsecSearchSportsResult _specializedSchema]
- -[SFSearchResult(SafariSharedExtras) safari_loggingDescription]
- -[WBSParsecSearchMapsResult .cxx_destruct]
- -[WBSParsecSearchMapsResult initWithDictionary:]
- -[WBSParsecSearchMapsResult mapsFeedbackSender]
- -[WBSParsecSearchMapsResult parsecSearchSession]
- -[WBSParsecSearchMapsResult setMapsFeedbackSender:]
- -[WBSParsecSearchMapsResult setParsecSearchSession:]
- -[WBSParsecSearchMoviesResult .cxx_destruct]
- -[WBSParsecSearchMoviesResult descriptionLeadInText]
- -[WBSParsecSearchMoviesResult initWithDictionary:]
- -[WBSParsecSearchMoviesResult postersWithSession:]
- -[WBSParsecSearchResult descriptionLeadInText]
- -[WBSParsecSearchResult descriptionMaximumNumberOfLines]
- -[WBSParsecSearchResult descriptionTextCanWrap]
- -[WBSParsecSearchResult hasSingleLineDescriptionAndTitle]
- -[WBSParsecSearchResult titleGlyphWithSession:]
- -[WBSParsecSearchResult titleMaximumNumberOfLines]
- -[WBSParsecSearchSimpleResult descriptionLeadInText]
- -[WBSParsecSearchSimpleResult descriptionMaximumNumberOfLines]
- -[WBSParsecSearchSimpleResult descriptionTextCanWrap]
- -[WBSParsecSearchSimpleResult hasSingleLineDescriptionAndTitle]
- -[WBSParsecSearchSimpleResult titleGlyphWithSession:]
- -[WBSParsecSearchSimpleResult titleMaximumNumberOfLines]
- -[WBSParsecSearchSportsResult .cxx_destruct]
- -[WBSParsecSearchSportsResult extraCompletionItem]
- -[WBSParsecSearchSportsResult images]
- -[WBSParsecSearchSportsResult individualScores]
- -[WBSParsecSearchSportsResult initWithDictionary:]
- -[WBSParsecSearchSportsResult subtitle]
- -[WBSSVGImageRenderingFetchOperation didCreateWebView]
- -[WBSSVGImageRenderingFetchOperation didRenderImage:]
- -[WBSSVGImageRenderingWebProcessPlugInPageController .cxx_destruct]
- -[WBSSVGImageRenderingWebProcessPlugInPageController svgImageRenderingObserver]
- -[WBSSVGImageRenderingWebProcessPlugInPageController webProcessPlugInBrowserContextController:didFinishLoadForFrame:]
- -[WBSSafariExtension .cxx_construct]
- -[WBSStartPageBackgroundImagesDataSource .cxx_construct]
- -[WBSStartPageBackgroundManager .cxx_construct]
- -[WBSStartPageBackgroundManager normalizeImage:imageSource:properties:]
- -[WBSStartPageSection setSymbolImageName:]
- -[WBSStartPageSection symbolImageName]
- -[WBSWebExtensionInjectedContentData removeWKUserScripts]
- -[WBSWebExtensionInjectedContentData removeWKUserStyleSheets]
- -[WBSWebProcessPlugIn isParsecABTestingEnabled]
- -[WBSWebProcessPlugIn parsecABGroupIdentifier]
- -[_WKApplicationManifest(SafariSharedUIExtras) _resolvedScopeURLString:usingStartURLString:]
- -[_WKApplicationManifest(SafariSharedUIExtras) safari_isSynthesized]
- -[_WKApplicationManifest(SafariSharedUIExtras) safari_setIsSynthesized:]
- -[_WKApplicationManifestIcon(SafariSharedUIExtras) safari_dictionaryRepresentation]
- GCC_except_table214
- GCC_except_table220
- GCC_except_table240
- GCC_except_table247
- GCC_except_table270
- GCC_except_table274
- GCC_except_table298
- GCC_except_table335
- GCC_except_table381
- GCC_except_table382
- GCC_except_table387
- GCC_except_table389
- GCC_except_table390
- GCC_except_table392
- GCC_except_table402
- GCC_except_table403
- GCC_except_table408
- GCC_except_table410
- GCC_except_table411
- GCC_except_table412
- GCC_except_table414
- GCC_except_table418
- GCC_except_table419
- _CFErrorCreate
- _OBJC_CLASS_$_WBSParsecSearchMapsResult
- _OBJC_CLASS_$_WBSParsecSearchMoviesResult
- _OBJC_CLASS_$_WBSParsecSearchSportsResult
- _OBJC_CLASS_$_WBSSVGImageRenderingWebProcessPlugInPageController
- _OBJC_CLASS_$_WKWebProcessPlugInNodeHandle
- _OBJC_CLASS_$__WKApplicationManifestIcon
- _OBJC_IVAR_$_WBSParsecSearchMapsResult._mapsFeedbackSender
- _OBJC_IVAR_$_WBSParsecSearchMapsResult._parsecSearchSession
- _OBJC_IVAR_$_WBSParsecSearchMoviesResult._descriptionLeadInText
- _OBJC_IVAR_$_WBSParsecSearchMoviesResult._posterRepresentations
- _OBJC_IVAR_$_WBSParsecSearchSimpleResult._descriptionLeadInText
- _OBJC_IVAR_$_WBSParsecSearchSimpleResult._descriptionMaximumNumberOfLines
- _OBJC_IVAR_$_WBSParsecSearchSimpleResult._descriptionTextCanWrap
- _OBJC_IVAR_$_WBSParsecSearchSimpleResult._hasSingleLineDescriptionAndTitle
- _OBJC_IVAR_$_WBSParsecSearchSimpleResult._titleMaximumNumberOfLines
- _OBJC_IVAR_$_WBSParsecSearchSportsResult._extraCompletionItem
- _OBJC_IVAR_$_WBSParsecSearchSportsResult._scoreSummary
- _OBJC_IVAR_$_WBSSVGImageRenderingFetchOperation._svgImageRenderingObserverInterface
- _OBJC_IVAR_$_WBSSVGImageRenderingWebProcessPlugInPageController._svgImageRenderingObserver
- _OBJC_IVAR_$_WBSStartPageSection._symbolImageName
- _OBJC_METACLASS_$_WBSParsecSearchMapsResult
- _OBJC_METACLASS_$_WBSParsecSearchMoviesResult
- _OBJC_METACLASS_$_WBSParsecSearchSportsResult
- _OBJC_METACLASS_$_WBSSVGImageRenderingWebProcessPlugInPageController
- _WBSChromeExtensionURLScheme
- _WBSParsecDSessionDidLoadBagNotification
- _WBSSVGImageRenderingWebViewConfigurationGroupIdentifier
- _WBSWKManifestIsSynthesizedRootLevelKey
- _WBSWebProcessPlugInParsecABGroupIdentifierKey
- _WBSWebProcessPlugInParsecABTestingEnabledKey
- __CFHostIsDomainTopLevel
- __OBJC_$_CATEGORY__WKApplicationManifestIcon_$_SafariSharedUIExtras
- __OBJC_$_CLASS_METHODS_WBSParsecSearchSportsResult
- __OBJC_$_INSTANCE_METHODS_WBSParsecSearchMapsResult
- __OBJC_$_INSTANCE_METHODS_WBSParsecSearchMoviesResult
- __OBJC_$_INSTANCE_METHODS_WBSParsecSearchSportsResult
- __OBJC_$_INSTANCE_METHODS_WBSSVGImageRenderingWebProcessPlugInPageController
- __OBJC_$_INSTANCE_METHODS__WKApplicationManifestIcon(SafariSharedUIExtras)
- __OBJC_$_INSTANCE_VARIABLES_WBSParsecSearchMapsResult
- __OBJC_$_INSTANCE_VARIABLES_WBSParsecSearchMoviesResult
- __OBJC_$_INSTANCE_VARIABLES_WBSParsecSearchSportsResult
- __OBJC_$_INSTANCE_VARIABLES_WBSSVGImageRenderingWebProcessPlugInPageController
- __OBJC_$_PROP_LIST_WBSParsecSearchMapsResult
- __OBJC_$_PROP_LIST_WBSParsecSearchMoviesResult
- __OBJC_$_PROP_LIST_WBSParsecSearchResult.233
- __OBJC_$_PROP_LIST_WBSParsecSearchSimpleResult.125
- __OBJC_$_PROP_LIST_WBSParsecSearchSportsResult.25
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_WBSSVGImageRenderingObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_WBSSVGImageRenderingObserver
- __OBJC_$_PROTOCOL_REFS_WBSSVGImageRenderingObserver
- __OBJC_CLASS_PROTOCOLS_$_WBSParsecSearchMapsResult
- __OBJC_CLASS_PROTOCOLS_$_WBSParsecSearchSportsResult
- __OBJC_CLASS_PROTOCOLS_$_WBSSVGImageRenderingFetchOperation
- __OBJC_CLASS_RO_$_WBSParsecSearchMapsResult
- __OBJC_CLASS_RO_$_WBSParsecSearchMoviesResult
- __OBJC_CLASS_RO_$_WBSParsecSearchSportsResult
- __OBJC_CLASS_RO_$_WBSSVGImageRenderingWebProcessPlugInPageController
- __OBJC_LABEL_PROTOCOL_$_WBSSVGImageRenderingObserver
- __OBJC_METACLASS_RO_$_WBSParsecSearchMapsResult
- __OBJC_METACLASS_RO_$_WBSParsecSearchMoviesResult
- __OBJC_METACLASS_RO_$_WBSParsecSearchSportsResult
- __OBJC_METACLASS_RO_$_WBSSVGImageRenderingWebProcessPlugInPageController
- __OBJC_PROTOCOL_$_WBSSVGImageRenderingObserver
- __OBJC_PROTOCOL_REFERENCE_$_WBSSVGImageRenderingObserver
- __ZN3WTF17dynamic_objc_castI12NSDictionaryEEPT_P11objc_object
- __ZN3WTF17dynamic_objc_castI17NSHTTPURLResponseEEPT_P11objc_object
- __ZN3WTF17dynamic_objc_castI19WBSWebExtensionDataEEPT_P11objc_object
- __ZN3WTF17dynamic_objc_castI27WBSWebExtensionMatchPatternEEPT_P11objc_object
- __ZN3WTF17dynamic_objc_castI38WBSSavePermissionsToStorageInformationEEPT_P11objc_object
- __ZN3WTF17dynamic_objc_castI6NSDataEEPT_P11objc_object
- __ZN3WTF17dynamic_objc_castI7JSValueEEPT_P11objc_object
- __ZN3WTF17dynamic_objc_castI7NSArrayEEPT_P11objc_object
- __ZN3WTF17dynamic_objc_castI8NSNumberEEPT_P11objc_object
- __ZN3WTF17dynamic_objc_castI8NSStringEEPT_P11objc_object
- __ZN3WTF6VectorINS_9RetainPtrIP7CGImageEELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE15reserveCapacityILNS_13FailureActionE0EEEbm
- __ZN3WTF6VectorINS_9RetainPtrIP7CGImageEELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEED2Ev
- ___102-[WBSPhishingURLClassifierCrowdsourcedFeedbackAllowListAdapter classifyURL:options:completionHandler:]_block_invoke_4
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.467
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.467.cold.1
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.468
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke.468.cold.1
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke_2.474
- ___109-[WBSWebExtensionData _updateDeclarativeNetRequestRulesInStorage:byRemovingRules:addRules:completionHandler:]_block_invoke_2.474.cold.1
- ___49+[WBSParsecSearchSportsResult _specializedSchema]_block_invoke
- ___50-[WBSParsecSearchMoviesResult postersWithSession:]_block_invoke
- ___50-[WBSWebExtensionData _loadBackgroundPageWithURL:]_block_invoke.565
- ___60-[WBSParsecDSession _setCurrentQuery:withKeyboardInputType:]_block_invoke.33
- ___69-[WBSTranslationContext _updateProgressWithTranslatedParagraphCount:]_block_invoke.128
- ___69-[WBSTranslationContext _updateProgressWithTranslatedParagraphCount:]_block_invoke.128.cold.1
- ___75-[WBSTranslationContext _setState:usingLock:validatingTransitionIsAllowed:]_block_invoke.96
- ___75-[WBSTranslationContext _setState:usingLock:validatingTransitionIsAllowed:]_block_invoke.97
- ___76-[WBSTranslationContext _updateProgressForFinishingInitialContentExtraction]_block_invoke.129
- ___77+[WBSParsecDSession _updateAutoFillTLDsIfNeededForSession:completionHandler:]_block_invoke.49
- ___77+[WBSParsecDSession _updateAutoFillTLDsIfNeededForSession:completionHandler:]_block_invoke.49.cold.1
- ___77+[WBSParsecDSession _updateAutoFillTLDsIfNeededForSession:completionHandler:]_block_invoke.49.cold.2
- ___77-[WBSTranslationContext _dominantLocaleForTextSamples:url:completionHandler:]_block_invoke
- ___77-[WBSWebExtensionsController postMessage:fromPortWithID:fromExtensionWithID:]_block_invoke.295
- ___78-[WBSExtensionsController writeExtensionsStateToStorageWithCompletionHandler:]_block_invoke.29
- ___79-[WBSWebExtensionsController _deleteStorageForExtensionWithComposedIdentifier:]_block_invoke.168
- ___80-[WBSParsecDSession _startUpdatingAutoFillDataInBackgroundIfPossibleForSession:]_block_invoke.42
- ___80-[WBSParsecDSession _startUpdatingAutoFillDataInBackgroundIfPossibleForSession:]_block_invoke.43
- ___80-[WBSParsecDSession _startUpdatingAutoFillDataInBackgroundIfPossibleForSession:]_block_invoke.44.cold.1
- ___80-[WBSParsecDSession _startUpdatingAutoFillDataInBackgroundIfPossibleForSession:]_block_invoke_2.46
- ___82-[WBSStartPageBackgroundManager _setImageOnAnyQueue:withAppearance:forIdentifier:]_block_invoke.101
- ___84-[WBSTranslationContext _promptIfNeededToConsentToTranslationWithCompletionHandler:]_block_invoke.102
- ___84-[WBSWebExtensionData loadRegisteredContentScriptsFromStorageWithCompletionHandler:]_block_invoke.483
- ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke.419
- ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke.419.cold.1
- ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke_3
- ___86-[WBSWebExtensionData loadDeclarativeNetRequestRulesetsIfNeededWithCompletionHandler:]_block_invoke_3.cold.1
- ___87+[WBSParsecDSession _updateAutoFillCorrectionSetsIfNeededForSession:completionHandler:]_block_invoke.51
- ___87+[WBSParsecDSession _updateAutoFillCorrectionSetsIfNeededForSession:completionHandler:]_block_invoke.51.cold.1
- ___87+[WBSParsecDSession _updateAutoFillCorrectionSetsIfNeededForSession:completionHandler:]_block_invoke.51.cold.2
- ___87+[WBSParsecDSession _updateAutoFillCorrectionSetsIfNeededForSession:completionHandler:]_block_invoke.51.cold.3
- ___87-[WBSExtensionsController setExtension:isEnabled:dueToUserGesture:skipSavingToStorage:]_block_invoke.34
- ___91-[WBSWebExtensionsController _loadPermissionsFromStorageForWebExtension:completionHandler:]_block_invoke.299
- ___92-[_WKApplicationManifest(SafariSharedUIExtras) _resolvedScopeURLString:usingStartURLString:]_block_invoke
- ___block_descriptor_176_ea8_32s40bs112c31_ZTSN3WTF9RetainPtrIP7CGImageEE168c31_ZTSN3WTF9RetainPtrIP7CGImageEE_e20_v16?0^{CGContext=}8l
- ___block_descriptor_40_e8_32s_e17_B16?0"WBSPair"8ls32l8
- ___block_descriptor_40_ea8_32s_e57_v32?0"NSNumber"8?<v?{RetainPtr<CGImage *>=^v}B>16^B24ls32l8
- ___block_descriptor_48_ea8_32s40c31_ZTSN3WTF9RetainPtrIP7CGImageEE_e5_v8?0l
- ___block_descriptor_52_ea8_32s40c31_ZTSN3WTF9RetainPtrIP7CGImageEE_e5_v8?0l
- ___block_descriptor_56_e8_32s40s48s_e5_B8?0ls32l8s40l8s48l8
- ___block_descriptor_56_ea8_32s40s48c31_ZTSN3WTF9RetainPtrIP7CGImageEE_e5_v8?0l
- ___block_descriptor_57_ea8_32s40s48c37_ZTSN3WTF9RetainPtrI13CGImageSourceEE_e5_v8?0l
- ___block_descriptor_64_ea8_32s40bs56c31_ZTSN3WTF9RetainPtrIP7CGImageEE_e5_v8?0l
- ___block_descriptor_64_ea8_32s40s48c37_ZTSN3WTF9RetainPtrI13CGImageSourceEE_e5_v8?0l
- ___block_descriptor_72_e8_32s40s48s56bs64r_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_74_ea8_32s40s48bs56c31_ZTSN3WTF9RetainPtrIP7CGImageEE_e5_v8?0l
- ___block_literal_global.110
- ___block_literal_global.124
- ___block_literal_global.151
- ___block_literal_global.197
- ___block_literal_global.239
- ___block_literal_global.255
- ___block_literal_global.291
- ___block_literal_global.297
- ___block_literal_global.304
- ___block_literal_global.350
- ___block_literal_global.353
- ___block_literal_global.458
- ___block_literal_global.482
- ___block_literal_global.485
- ___block_literal_global.493
- ___block_literal_global.504
- ___block_literal_global.507
- ___block_literal_global.517
- ___block_literal_global.540
- ___block_literal_global.558
- ___block_literal_global.65
- ___block_literal_global.766
- ___block_literal_global.85
- ___copy_helper_block_ea8_112c31_ZTSN3WTF9RetainPtrIP7CGImageEE168c31_ZTSN3WTF9RetainPtrIP7CGImageEE
- ___copy_helper_block_ea8_40c31_ZTSN3WTF9RetainPtrIP7CGImageEE
- ___copy_helper_block_ea8_48c31_ZTSN3WTF9RetainPtrIP7CGImageEE
- ___copy_helper_block_ea8_48c37_ZTSN3WTF9RetainPtrI13CGImageSourceEE
- ___copy_helper_block_ea8_56c31_ZTSN3WTF9RetainPtrIP7CGImageEE
- ___destroy_helper_block_ea8_112c31_ZTSN3WTF9RetainPtrIP7CGImageEE168c31_ZTSN3WTF9RetainPtrIP7CGImageEE
- ___destroy_helper_block_ea8_40c31_ZTSN3WTF9RetainPtrIP7CGImageEE
- ___destroy_helper_block_ea8_48c31_ZTSN3WTF9RetainPtrIP7CGImageEE
- ___destroy_helper_block_ea8_48c37_ZTSN3WTF9RetainPtrI13CGImageSourceEE
- ___destroy_helper_block_ea8_56c31_ZTSN3WTF9RetainPtrIP7CGImageEE
- __unnamed_array_storage.119
- __unnamed_array_storage.1357
- __unnamed_array_storage.1492
- __unnamed_array_storage.29
- __unnamed_array_storage.321
- __unnamed_array_storage.355
- __unnamed_array_storage.356
- __unnamed_array_storage.370
- __unnamed_array_storage.371
- __unnamed_array_storage.408
- __unnamed_array_storage.427
- __unnamed_array_storage.435
- __unnamed_array_storage.438
- __unnamed_array_storage.441
- __unnamed_array_storage.763
- __unnamed_array_storage.92
- _objc_msgSend$_resolvedScopeURLString:usingStartURLString:
- _objc_msgSend$_simpleResult
- _objc_msgSend$applicationDescription
- _objc_msgSend$completedQuery
- _objc_msgSend$defaultFormat
- _objc_msgSend$descriptionLeadInText
- _objc_msgSend$descriptionMaximumNumberOfLines
- _objc_msgSend$descriptionTextCanWrap
- _objc_msgSend$didRenderImage:
- _objc_msgSend$firstElementForSelector:
- _objc_msgSend$hasProperty:
- _objc_msgSend$hasSingleLineDescriptionAndTitle
- _objc_msgSend$intendedQuery
- _objc_msgSend$manifestId
- _objc_msgSend$nodeHandleWithJSValue:inContext:
- _objc_msgSend$normalizeImage:imageSource:properties:
- _objc_msgSend$removeLastObject
- _objc_msgSend$removeWKUserScripts
- _objc_msgSend$removeWKUserStyleSheets
- _objc_msgSend$renderedImageWithOptions:
- _objc_msgSend$safari_reverseEnumerateComponents:usingBlock:
- _objc_msgSend$safari_setIsSynthesized:
- _objc_msgSend$scores
- _objc_msgSend$svgImageRenderingObserver
- _objc_msgSend$titleGlyphWithSession:
- _objc_msgSend$titleMaximumNumberOfLines
- _objc_msgSend$uppercaseLetterCharacterSet
- _objc_msgSend$userInput
- _safariIsSynthesizedKey
CStrings:
+ "\x01\x17'\x11"
+ "\x05\x11\x11\x14"
+ " %@ <%@>,"
+ "8617.1.17.10.9"
+ "<html><head>%@%@</head><body>%@</body></html>"
+ "<script>window.didEncounterRenderingError = function() {    let elem = document.querySelector(\".image\");    return !elem || elem.hasAttribute(\"error\");}</script>"
+ "@\"WBSCGImage\""
+ "@\"WBSTemplateIconMonogramConfiguration\""
+ "@32@0:8@16^{CGImageSource=}24"
+ "@36@0:8@16^{CGImageSource=}24B32"
+ "@48@0:8^{CGImage=}16d24d32d40"
+ "@56@0:8^{CGImage=}16^{CGImage=}24d32^q40^d48"
+ "@80@0:8@16@24{CGSize=dd}32{CGSize=dd}48@64Q72"
+ "B16@?0@\"_WKApplicationManifestIcon\"8"
+ "Check for successful SVG rendering failed with error: %{public}@"
+ "Custom"
+ "Favicon"
+ "Invalid error message passed to %{public}@.get() for extension %{private}@. Expected NSString, was %{public}@."
+ "Monogram"
+ "Parsec Results: [%{public}@]"
+ "Q36@0:8@16^{CGImageSource=}24B32"
+ "SVG rendering failed with unexpected result: %{public}@"
+ "Snapshotting SVG content failed with error: %{public}@"
+ "T@\"NSString\",&,N,Ssafari_setIconKind:"
+ "T@\"NSString\",C,N,V_accessibilityIdentifier"
+ "T@\"NSString\",R,N,V_imageURL"
+ "T@\"UIColor\",&,N,Ssafari_setThemeColor:"
+ "T@\"UIImage\",&,N,V_icon"
+ "T@\"WBSCGImage\",R,N,V_image"
+ "T@\"WBSTemplateIconMonogramConfiguration\",R,N,V_monogramConfiguration"
+ "T@?,C,N,V_didCompleteWithError"
+ "T@?,C,N,V_didReceiveData"
+ "TB,R,N,GisABTestingEnabled"
+ "T^{__SecCode=},N,V_bundleCodeRef"
+ "Touch"
+ "Unable to read manifest."
+ "Unable to serialize manifest with %{public}@"
+ "Unknown error occurred in %@.get()."
+ "WBSWKDataTaskDelegate"
+ "WKManifestIconKind"
+ "WKManifestURL"
+ "^{__SecCode=}"
+ "^{__SecCode=}16@0:8"
+ "_WKDataTaskDelegate"
+ "_accessibilityIdentifier"
+ "_dataTaskWithRequest:completionHandler:"
+ "_didCompleteWithError"
+ "_didReceiveData"
+ "_didRenderImage:"
+ "_isSingleEmoji"
+ "_longestEdgeForIcon:"
+ "_manifestWithInfoDictionary:withSynthesizedProperties:"
+ "_preferredPurposeForIcons:"
+ "_primaryPurposeForPurposes:"
+ "_setHiddenPageDOMTimerThrottlingEnabled:"
+ "_setUsesTransparentBackground:"
+ "_takeSnapshotAndFinish"
+ "abGroupIdentifier"
+ "abTestingEnabled"
+ "accessibilityIdentifier"
+ "appendData:"
+ "characterSetWithRange:"
+ "com.apple.Safari.SectionToggleExpanded"
+ "dataTask:didCompleteWithError:"
+ "dataTask:didReceiveAuthenticationChallenge:completionHandler:"
+ "dataTask:didReceiveData:"
+ "dataTask:didReceiveResponse:decisionHandler:"
+ "dataTask:willPerformHTTPRedirection:newRequest:decisionHandler:"
+ "didCompleteWithError"
+ "didFinishNavigation"
+ "didReceiveData"
+ "downloadImagesForManifest:linkIconParameters:usingWebView:withCompletionHandler:"
+ "evaluateJavaScript:completionHandler:"
+ "iconType"
+ "imageByAdoptingCGImage:"
+ "initWithTitle:url:minimumIconSize:maximumIconSize:monogramConfiguration:options:"
+ "isABTestingEnabled"
+ "isDefaultScope"
+ "isSearchEvaluationLoggingEnabled"
+ "isSpeculative"
+ "mask"
+ "normalizeImage:properties:"
+ "preferredFormat"
+ "rawJSON"
+ "removeWKUserScriptsFromUserContentController:"
+ "removeWKUserStyleSheetsFromUserContentController:"
+ "requestWithTitle:url:minimumIconSize:maximumIconSize:monogramConfiguration:options:"
+ "safari_hostDomainsEnumerator"
+ "safari_iconKind"
+ "safari_largestSizedBitmapImageOrSVGFromImages:"
+ "safari_longestEdgeInPixels"
+ "safari_manifestWithInfoDictionary:"
+ "safari_scope"
+ "safari_setIconKind:"
+ "safari_setThemeColor:"
+ "safari_stringHasLeadingEmoji:"
+ "safari_themeColor"
+ "safari_urlHashesOfComponents"
+ "setDidCompleteWithError:"
+ "setDidReceiveData:"
+ "setInactiveSchedulingPolicy:"
+ "uuidString"
+ "v16@?0@\"_WKDataTask\"8"
+ "v24@0:8^{__SecCode=}16"
+ "v24@?0@\"_WKDataTask\"8@\"NSData\"16"
+ "v24@?0@\"_WKDataTask\"8@\"NSError\"16"
+ "v28@?0@\"NSURL\"8@\"NSMutableArray\"16B24"
+ "v32@0:8@\"_WKDataTask\"16@\"NSData\"24"
+ "v32@0:8@\"_WKDataTask\"16@\"NSError\"24"
+ "v32@?0@\"NSNumber\"8@?<v@?@\"WBSCGImage\"B>16^B24"
+ "v36@0:8^{CGImageSource=}16@24B32"
+ "v40@0:8@\"_WKDataTask\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v40@0:8@\"_WKDataTask\"16@\"NSURLResponse\"24@?<v@?q>32"
+ "v48@0:8@\"_WKDataTask\"16@\"NSHTTPURLResponse\"24@\"NSURLRequest\"32@?<v@?q>40"
+ "v64@0:8@16q24d32@40B48B52@?56"
+ "window.didEncounterRenderingError()"
- "\x01\x16(\x11"
- "\x02\x12\x113"
- "\x02\x16"
- "\x05!"
- "%@%@"
- ".image"
- "8616.2.9.10.13"
- "<html><head>%@</head><body>%@</body></html>"
- "@\"<WBSSVGImageRenderingObserver>\""
- "@\"WBSParsecSearchSportsAttributionExtraCompletionItem\""
- "@\"WBSParsecSportsScoreSummary\""
- "B16@?0@\"WBSPair\"8"
- "Q36@0:8@16{RetainPtr<CGImageSource>=^v}24B32"
- "SFSearchResult: identifier=%@, userInput=%@, intendedQuery=%@, completedQuery=%@,"
- "SVGImageRendering"
- "T@\"NSNumber\",R,N,V_descriptionMaximumNumberOfLines"
- "T@\"NSNumber\",R,N,V_titleMaximumNumberOfLines"
- "T@\"NSString\",C,N,V_symbolImageName"
- "T@\"NSString\",R,N,V_descriptionLeadInText"
- "T@\"WBSParsecSearchSportsAttributionExtraCompletionItem\",R,N,V_extraCompletionItem"
- "TB,N,Ssafari_setIsSynthesized:"
- "TB,R,N,GisParsecABTestingEnabled"
- "TB,R,N,V_descriptionTextCanWrap"
- "TB,R,N,V_hasSingleLineDescriptionAndTitle"
- "Treating website as %{public}@ due to quirks list"
- "T{RetainPtr<CGImage *>=^v},R,N,V_image"
- "T{RetainPtr<const __SecCode *>=^v},N,V_bundleCodeRef"
- "WBSParsecDSessionDidLoadBag"
- "WBSParsecSearchMoviesResult"
- "WBSSVGImageRenderingObserver"
- "WBSSVGImageRenderingWebProcessPlugInPageController"
- "_descriptionLeadInText"
- "_descriptionMaximumNumberOfLines"
- "_descriptionTextCanWrap"
- "_extraCompletionItem"
- "_hasSingleLineDescriptionAndTitle"
- "_posterRepresentations"
- "_resolvedScopeURLString:usingStartURLString:"
- "_scoreSummary"
- "_svgImageRenderingObserver"
- "_svgImageRenderingObserverInterface"
- "_symbolImageName"
- "_titleMaximumNumberOfLines"
- "any"
- "applicationDescription"
- "com.apple.safari.SectionToggleExpanded"
- "completedQuery"
- "defaultFormat"
- "descriptionLeadInText"
- "descriptionMaximumNumberOfLines"
- "descriptionTextCanWrap"
- "description_follows_title"
- "description_lead_in"
- "description_maxlines"
- "description_nowrap"
- "didRenderImage:"
- "hasProperty:"
- "hasSingleLineDescriptionAndTitle"
- "intendedQuery"
- "isParsecABTestingEnabled"
- "manifestId"
- "maps_result_type"
- "maskable"
- "monochrome"
- "movie_list"
- "nodeHandleWithJSValue:inContext:"
- "normalizeImage:imageSource:properties:"
- "parsecABGroupIdentifier"
- "parsecABTestingEnabled"
- "posters"
- "postersWithSession:"
- "q24@0:8{RetainPtr<CGImage *>=^v}16"
- "removeLastObject"
- "removeWKUserScripts"
- "removeWKUserStyleSheets"
- "renderedImageWithOptions:"
- "safari_isSynthesized"
- "safari_loggingDescription"
- "safari_reverseEnumerateComponents:usingBlock:"
- "safari_setIsSynthesized:"
- "setSymbolImageName:"
- "sports_summary"
- "svgImageRenderingObserver"
- "symbolImageName"
- "titleGlyphWithSession:"
- "titleMaximumNumberOfLines"
- "tmall.com"
- "twitter"
- "uppercaseLetterCharacterSet"
- "userInput"
- "v24@0:8@\"UIImage\"16"
- "v24@0:8{RetainPtr<const __SecCode *>=^v}16"
- "v32@?0@\"NSNumber\"8@?<v@?{RetainPtr<CGImage *>=^v}B>16^B24"
- "v36@0:8{RetainPtr<CGImageSource>=^v}16@24B32"
- "v40@0:8{RetainPtr<CGImage *>=^v}16q24@32"
- "v64@0:8{RetainPtr<CGImage *>=^v}16q24d32@40B48B52@?56"
- "x"
- "{RetainPtr<CGImage *>=\"m_ptr\"^v}"
- "{RetainPtr<CGImage *>=^v}16@0:8"
- "{RetainPtr<CGImage *>=^v}24@0:8@16"
- "{RetainPtr<CGImage *>=^v}32@0:8@16@24"
- "{RetainPtr<CGImage *>=^v}32@0:8@16{RetainPtr<CGImageSource *>=^v}24"
- "{RetainPtr<CGImage *>=^v}32@0:8{RetainPtr<CGImage *>=^v}16{RetainPtr<CGImage *>=^v}24"
- "{RetainPtr<CGImage *>=^v}36@0:8@16{RetainPtr<CGImageSource>=^v}24B32"
- "{RetainPtr<CGImage *>=^v}40@0:8{RetainPtr<CGImage *>=^v}16{RetainPtr<CGImageSource>=^v}24@32"
- "{RetainPtr<CGImage *>=^v}48@0:8^{CGImage=}16d24d32d40"
- "{RetainPtr<CGImage *>=^v}56@0:8^{CGImage=}16^{CGImage=}24d32^q40^d48"
- "{RetainPtr<const __SecCode *>=\"m_ptr\"^v}"
- "{RetainPtr<const __SecCode *>=^v}16@0:8"
- "{Vector<WTF::RetainPtr<CGImage *>, 0UL, WTF::CrashOnOverflow, 16UL, WTF::FastMalloc>=\"m_buffer\"^v\"m_capacity\"I\"m_size\"I}"

```
