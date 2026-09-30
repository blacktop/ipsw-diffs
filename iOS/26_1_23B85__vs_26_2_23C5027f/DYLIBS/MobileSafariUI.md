## MobileSafariUI

> `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-622.2.11.10.8
-  __TEXT.__text: 0x2533e0
-  __TEXT.__auth_stubs: 0x3520
-  __TEXT.__objc_methlist: 0x22cc4
-  __TEXT.__const: 0x1a28
-  __TEXT.__gcc_except_tab: 0x1c350
-  __TEXT.__cstring: 0x10e02
+623.1.12.10.4
+  __TEXT.__text: 0x253cc4
+  __TEXT.__auth_stubs: 0x3870
+  __TEXT.__objc_methlist: 0x22bbc
+  __TEXT.__const: 0x1b88
+  __TEXT.__gcc_except_tab: 0x1c3c8
+  __TEXT.__cstring: 0x10f22
   __TEXT.__dlopen_cstrs: 0x83a
-  __TEXT.__oslogstring: 0x9328
-  __TEXT.__ustring: 0x10e8
-  __TEXT.__constg_swiftt: 0xbac
-  __TEXT.__swift5_typeref: 0x1532
+  __TEXT.__oslogstring: 0x9648
+  __TEXT.__ustring: 0x113a
+  __TEXT.__constg_swiftt: 0xd38
+  __TEXT.__swift5_typeref: 0x15d4
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0x748
-  __TEXT.__swift5_fieldmd: 0x61c
+  __TEXT.__swift5_reflstr: 0x848
+  __TEXT.__swift5_fieldmd: 0x6e4
   __TEXT.__swift5_assocty: 0x198
-  __TEXT.__swift5_proto: 0xb4
-  __TEXT.__swift5_types: 0x84
-  __TEXT.__swift5_capture: 0x181c
+  __TEXT.__swift5_proto: 0xc0
+  __TEXT.__swift5_types: 0x94
+  __TEXT.__swift5_capture: 0x186c
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x38
-  __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0xda40
-  __TEXT.__eh_frame: 0xd38
-  __TEXT.__objc_classname: 0x3f6a
-  __TEXT.__objc_methname: 0x6bf77
-  __TEXT.__objc_methtype: 0x150f4
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__unwind_info: 0xda00
+  __TEXT.__eh_frame: 0xd70
+  __TEXT.__objc_classname: 0x3f1f
+  __TEXT.__objc_methname: 0x6bf0c
+  __TEXT.__objc_methtype: 0x14f33
   __TEXT.__objc_stubs: 0x46a00
-  __DATA_CONST.__got: 0x2c90
-  __DATA_CONST.__const: 0x8b48
+  __DATA_CONST.__got: 0x2c88
+  __DATA_CONST.__const: 0x8b58
   __DATA_CONST.__objc_classlist: 0x958
   __DATA_CONST.__objc_catlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0xac8
+  __DATA_CONST.__objc_protolist: 0xab8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16b08
-  __DATA_CONST.__objc_protorefs: 0x158
-  __DATA_CONST.__objc_superrefs: 0x6a8
+  __DATA_CONST.__objc_selrefs: 0x16ac8
+  __DATA_CONST.__objc_protorefs: 0x150
+  __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x340
-  __AUTH_CONST.__auth_got: 0x1aa8
-  __AUTH_CONST.__const: 0x6200
-  __AUTH_CONST.__cfstring: 0xc900
-  __AUTH_CONST.__objc_const: 0x307a0
-  __AUTH_CONST.__objc_intobj: 0x480
+  __AUTH_CONST.__auth_got: 0x1c50
+  __AUTH_CONST.__const: 0x5c48
+  __AUTH_CONST.__cfstring: 0xc9e0
+  __AUTH_CONST.__objc_const: 0x306f0
+  __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x2ff8
-  __AUTH.__data: 0x1b0
-  __DATA.__objc_ivar: 0x20c8
-  __DATA.__data: 0x8140
-  __DATA.__bss: 0x15d0
-  __DATA.__common: 0x21
-  __DATA_DIRTY.__objc_data: 0x3da8
-  __DATA_DIRTY.__data: 0x800
-  __DATA_DIRTY.__bss: 0x8f0
+  __AUTH.__objc_data: 0x3010
+  __AUTH.__data: 0x430
+  __DATA.__objc_ivar: 0x20b0
+  __DATA.__data: 0x80e0
+  __DATA.__bss: 0x1560
+  __DATA.__common: 0x39
+  __DATA_DIRTY.__objc_data: 0x3d08
+  __DATA_DIRTY.__data: 0x820
+  __DATA_DIRTY.__bss: 0x740
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D666B8C0-972C-3867-B633-5448369CD60F
-  Functions: 13599
-  Symbols:   44456
-  CStrings:  22173
+  UUID: CF129BEB-33BF-3666-A603-DDEF37D3EA66
+  Functions: 13479
+  Symbols:   44035
+  CStrings:  22132
 
Symbols:
+ +[BrowserController _sendAutoFillDrivenByUIProcessFlagToProcessPool:]
+ +[BrowserController _sendIsReaderViewInSeparateProcessEnabledFlagToProcessPool:]
+ +[CompletionGroupListing shouldMoveSuggestionFromSearchProvider:toTopOfSectionForUserTypedQuery:]
+ +[SearchQueryBuilder searchQueryBuilderWithQuery:forPrivateBrowsing:richSearchSuggestionEntityIDURLParameter:]
+ -[Application _getCloudHistoryWithCompletionHandler:]
+ -[Application _resyncHistoryWithProfileID:]
+ -[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]
+ -[Application quickWebsiteSearchJavaScriptInjectionController:receivedDetectedSearchURLString:fromWebView:inFrame:]
+ -[Application quickWebsiteSearchJavaScriptInjectionController:receivedOpenSearchSchemaURL:fromWebView:]
+ -[Application resyncHistoryWithProfileID:]
+ -[BookmarkImporter ensureBookmarksNotMarkedAsReadingListItems]
+ -[BookmarksBarLabelButton _cancelFaviconRequest]
+ -[BookmarksBarLabelButton dealloc]
+ -[BrowserController _doSearch:richSearchSuggestionEntityIDURLParameter:]
+ -[BrowserController _logWindowAndTabCounts:]
+ -[BrowserController catalogViewController:didSelectSearch:richSearchSuggestionEntityIDURLParameter:]
+ -[CapsuleNavigationBarViewController _fastAddFolderTitle]
+ -[CatalogViewController _updateSearchSuggestionCompletionItemSelectionForQueryString:]
+ -[CatalogViewController beginDefaultSearchEngineOnboardingForStartPageViewController:completionHandler:]
+ -[CatalogViewController dismissSearchEngineSelectionTableViewAndPresentConfirmationSheet:]
+ -[CatalogViewController isShowingSearchEngineOnboardingCard]
+ -[CatalogViewController search:richSearchSuggestionEntityIDURLParameter:]
+ -[CompletionGroupListing _setPositionsOfSearchSuggestions]
+ -[CompletionList _addRecentSearchesToListing:]
+ -[CompletionList _completionsByMergingRecentSearches:withSuggestions:userTypedString:queryID:topHits:forPrivateBrowsing:]
+ -[CompletionList _swipeActionForRecentSearches:atIndexPath:]
+ -[CompletionList clearSearchCaches]
+ -[CompletionList indexPathOfAutocompletedSuggestion]
+ -[CompletionList shouldAutocompleteTopSuggestionFromSearchProvider]
+ -[History historyStoreDidFailDatabaseIntegrityCheck:error:databaseURLs:]
+ -[SafariClearBrowsingDataController clearDataWithRequest:]
+ -[SafariClearBrowsingDataController clearHistoryViewController:clearDataWithRequest:]
+ -[SearchQueryBuilder initWithQueryString:forPrivateBrowsing:richSearchSuggestionEntityIDURLParameter:]
+ -[SearchQueryBuilder initWithSearchEngineInfo:queryString:richSearchSuggestionEntityIDURLParameter:]
+ -[SearchSuggestion _configureImageForTableViewCellIfNeeded:completionList:usingBottomCapsule:]
+ -[SearchSuggestion _configureSubtitleLabelForTableViewCellIfNeeded:]
+ -[SearchSuggestion _configureTitleLabelForTableViewCell:]
+ -[SearchSuggestion _updateSubtitle:forTableViewCell:]
+ -[SearchSuggestion copyRichSearchSuggestionItemFromSuggestion:]
+ -[SearchSuggestion initWithSearchEngineSuggestion:richSearchSuggestion:postFixString:userQuery:forPrivateBrowsing:isOfflineSearchSuggestion:]
+ -[SearchSuggestion position]
+ -[SearchSuggestion richSearchSuggestion]
+ -[SearchSuggestion setPosition:]
+ -[SearchSuggestion setShouldAutocomplete:]
+ -[SearchSuggestion shouldAutocomplete]
+ -[SearchSuggestionTableViewCell hidesSubtitleLabel]
+ -[SearchSuggestionTableViewCell setHidesSubtitleLabel:]
+ -[SearchSuggestionTableViewCell setSubtitleLabel:]
+ -[StartPageController _updateMetadataForCardProxy:withURL:title:cardProxiesToMetadataTokens:]
+ -[TabController receivedTouchDownOutsideOfTabBar]
+ -[TabDocument _loadSearchResultForQuery:richSearchSuggestionEntityIDURLParameter:]
+ -[TabDocument _loadUserTypedAddress:richSearchSuggestionEntityIDURLParameter:]
+ -[TabDocument _processOpenSearchSchemaURL:]
+ -[TabDocument _webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:]
+ -[TabDocument didCommitToSpeculativeLoad]
+ -[TabDocument extractedArticleText]
+ -[TabDocument quickWebsiteSearchJavaScriptInjectionController:receivedDetectedSearchURLString:fromWebView:inFrame:]
+ -[TabDocument quickWebsiteSearchJavaScriptInjectionController:receivedOpenSearchSchemaURL:fromWebView:]
+ -[TabDocument setExtractedArticleText:]
+ -[TabSwitcherViewController didChangeShowSwipeToTabOverviewTip:]
+ -[UnifiedField canUpdateReflectedItemForTopSuggestionText:]
+ -[WBSPageTestController(MobileSafari) _setupBrowserControllerForTestingWithPageTestController:completionHandler:]
+ -[WBSPageTestController(MobileSafari) pageTestControllerEncounteredError:completionHandler:]
+ GCC_except_table1009
+ GCC_except_table1018
+ GCC_except_table1036
+ GCC_except_table1046
+ GCC_except_table1047
+ GCC_except_table1057
+ GCC_except_table1059
+ GCC_except_table1060
+ GCC_except_table1065
+ GCC_except_table1068
+ GCC_except_table1069
+ GCC_except_table1070
+ GCC_except_table1072
+ GCC_except_table1075
+ GCC_except_table1081
+ GCC_except_table1099
+ GCC_except_table1104
+ GCC_except_table1106
+ GCC_except_table1114
+ GCC_except_table1127
+ GCC_except_table1129
+ GCC_except_table1135
+ GCC_except_table1137
+ GCC_except_table1141
+ GCC_except_table1148
+ GCC_except_table1149
+ GCC_except_table1163
+ GCC_except_table1164
+ GCC_except_table1170
+ GCC_except_table1175
+ GCC_except_table1185
+ GCC_except_table1186
+ GCC_except_table1193
+ GCC_except_table1205
+ GCC_except_table1206
+ GCC_except_table1209
+ GCC_except_table1211
+ GCC_except_table1214
+ GCC_except_table1216
+ GCC_except_table1217
+ GCC_except_table1242
+ GCC_except_table1245
+ GCC_except_table1247
+ GCC_except_table1248
+ GCC_except_table1250
+ GCC_except_table1253
+ GCC_except_table1254
+ GCC_except_table1255
+ GCC_except_table1326
+ GCC_except_table1332
+ GCC_except_table138
+ GCC_except_table164
+ GCC_except_table369
+ GCC_except_table371
+ GCC_except_table384
+ GCC_except_table398
+ GCC_except_table411
+ GCC_except_table424
+ GCC_except_table428
+ GCC_except_table431
+ GCC_except_table433
+ GCC_except_table482
+ GCC_except_table489
+ GCC_except_table522
+ GCC_except_table545
+ GCC_except_table547
+ GCC_except_table549
+ GCC_except_table554
+ GCC_except_table603
+ GCC_except_table632
+ GCC_except_table685
+ GCC_except_table730
+ GCC_except_table742
+ GCC_except_table752
+ GCC_except_table761
+ GCC_except_table790
+ GCC_except_table791
+ GCC_except_table795
+ GCC_except_table798
+ GCC_except_table814
+ GCC_except_table833
+ GCC_except_table840
+ GCC_except_table842
+ GCC_except_table846
+ GCC_except_table852
+ GCC_except_table853
+ GCC_except_table859
+ GCC_except_table869
+ GCC_except_table872
+ GCC_except_table877
+ GCC_except_table881
+ GCC_except_table885
+ GCC_except_table904
+ GCC_except_table906
+ GCC_except_table913
+ GCC_except_table926
+ GCC_except_table945
+ GCC_except_table964
+ GCC_except_table972
+ GCC_except_table973
+ GCC_except_table985
+ GCC_except_table990
+ GCC_except_table992
+ _OBJC_CLASS_$_SFSwipeToTabOverviewTipCoordinator
+ _OBJC_CLASS_$_SFTestConsoleLogRecorder
+ _OBJC_CLASS_$_WBSOpenSearchSchemaFetcher
+ _OBJC_CLASS_$_WBSQuickWebsiteSearchJavaScriptInjectionController
+ _OBJC_CLASS_$__SFSearchEngineSelectionViewController
+ _OBJC_IVAR_$_Application._cloudHistoryStatus
+ _OBJC_IVAR_$_CatalogViewController._searchEngineSelectionViewController
+ _OBJC_IVAR_$_SearchQueryBuilder.richSearchSuggestionEntityIDURLParameter
+ _OBJC_IVAR_$_SearchSuggestion._position
+ _OBJC_IVAR_$_SearchSuggestion._richSearchSuggestion
+ _OBJC_IVAR_$_SearchSuggestion._shouldAutocomplete
+ _OBJC_IVAR_$_SearchSuggestionTableViewCell._hidesSubtitleLabel
+ _OBJC_IVAR_$_StartPageController._cloudTabProxiesToMetadataTokens
+ _OBJC_IVAR_$_TabDocument._deferredProcessingOpenSearchSchemaURL
+ _OBJC_IVAR_$_TabDocument._didAttemptInvalidAppLoadPreviously
+ _OBJC_IVAR_$_TabDocument._extractedArticleText
+ _OBJC_IVAR_$_TabDocument._needsSendTelemetryForLoadComplete
+ _SFDefaultSearchEngineOnboardingCardIsDeferredKey
+ _WBSAppWasLaunchedAfterMajorOrMinorOSUpgrade
+ _WBSAutomaticTabClosingIntervalAccessibilityIdentifier
+ _WBSLastOSVersionSafariWasLaunchedOnPreferenceKey
+ _WBSOSLogAppReviewPrompt
+ _WBSOSLogAutoFillAuthentication
+ _WBSOSLogBookmarks
+ _WBSOSLogBrowsingAssistant
+ _WBSOSLogCloudBookmarks
+ _WBSOSLogCloudHistory
+ _WBSOSLogCloudSettings
+ _WBSOSLogCloudTabs
+ _WBSOSLogContentBlockers
+ _WBSOSLogContinuity
+ _WBSOSLogCycler
+ _WBSOSLogDataMigration
+ _WBSOSLogDownloads
+ _WBSOSLogExtensions
+ _WBSOSLogHistory
+ _WBSOSLogHistoryViewController
+ _WBSOSLogInterstellar
+ _WBSOSLogLayout
+ _WBSOSLogLoweredTabBar
+ _WBSOSLogMediaCapture
+ _WBSOSLogOther
+ _WBSOSLogPLT
+ _WBSOSLogPageLoading
+ _WBSOSLogParsec
+ _WBSOSLogPerformanceTest
+ _WBSOSLogPrinting
+ _WBSOSLogPrivateBrowsing
+ _WBSOSLogProfiles
+ _WBSOSLogPush
+ _WBSOSLogReadingList
+ _WBSOSLogSignposts
+ _WBSOSLogSiriIntelligence
+ _WBSOSLogSiriLink
+ _WBSOSLogSiriReadThis
+ _WBSOSLogSiriSuggestedSites
+ _WBSOSLogStartPage
+ _WBSOSLogSystemNoteTaking
+ _WBSOSLogTabGroup
+ _WBSOSLogTabSnapshots
+ _WBSOSLogTabView
+ _WBSOSLogTabs
+ _WBSOSLogTest
+ _WBSOSLogURLAutocomplete
+ _WBSOSLogUserInteraction
+ _WBSOSLogUserInterface
+ _WBSOSLogWebClips
+ _WBSOSLogWebDriver
+ _WBSOSLogWebExtensions
+ _WBSOSLogWebsiteData
+ _WBSOSLogWidgets
+ _WBSStartPageOnboardingResumeDatePreferenceKey
+ _WBSWebProcessPlugInAutoFillDrivenByUIProcessKey
+ _WBSWebProcessPlugInReaderViewInSeparateProcessEnabledKey
+ __DATA__TtC14MobileSafariUI25BookmarksSaveStateManager
+ __DATA__TtCC14MobileSafariUI25BookmarksSaveStateManager9SaveState
+ __DATA__TtCC14MobileSafariUI25BookmarksSaveStateManagerP33_51D94BDDBAB9292D73E7E973E3879C7126DefaultCurrentDateProvider
+ __IVARS_SaveForLaterUIActivity
+ __IVARS__TtC14MobileSafariUI25BookmarksSaveStateManager
+ __IVARS__TtCC14MobileSafariUI25BookmarksSaveStateManager9SaveState
+ __METACLASS_DATA__TtC14MobileSafariUI25BookmarksSaveStateManager
+ __METACLASS_DATA__TtCC14MobileSafariUI25BookmarksSaveStateManager9SaveState
+ __METACLASS_DATA__TtCC14MobileSafariUI25BookmarksSaveStateManagerP33_51D94BDDBAB9292D73E7E973E3879C7126DefaultCurrentDateProvider
+ __OBJC_$_CLASS_METHODS_CompletionGroupListing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__SFNavigationBarCommon
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WBSQuickWebsiteSearchJavaScriptInjectionControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFSearchEngineSelectionViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WBSQuickWebsiteSearchJavaScriptInjectionControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFSearchEngineSelectionViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_WBSQuickWebsiteSearchJavaScriptInjectionControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_WBSQuickWebsiteSearchJavaScriptInjectionControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$__SFSearchEngineSelectionViewControllerDelegate
+ __OBJC_PROTOCOL_$_WBSQuickWebsiteSearchJavaScriptInjectionControllerDelegate
+ __OBJC_PROTOCOL_$__SFSearchEngineSelectionViewControllerDelegate
+ __ZNSt3__120__shared_ptr_emplaceIZ100-[TabDocument _webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:]E23CompletionHandlerCallerNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIZ100-[TabDocument _webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:]E23CompletionHandlerCallerNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIZ100-[TabDocument _webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:]E23CompletionHandlerCallerNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIZ100-[TabDocument _webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:]E23CompletionHandlerCallerNS_9allocatorIS1_EEED1Ev
+ __ZTVNSt3__120__shared_ptr_emplaceIZ100-[TabDocument _webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:]E23CompletionHandlerCallerNS_9allocatorIS1_EEEE
+ ___100-[TabDocument _webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:]_block_invoke
+ ___113-[WBSPageTestController(MobileSafari) _setupBrowserControllerForTestingWithPageTestController:completionHandler:]_block_invoke
+ ___113-[WBSPageTestController(MobileSafari) _setupBrowserControllerForTestingWithPageTestController:completionHandler:]_block_invoke_2
+ ___114-[BrowserRootViewController capsuleNavigationBarViewController:selectedItemWillChangeToState:options:coordinator:]_block_invoke.286
+ ___116-[URLCompletionDatabase enumerateMatchDataForTypedStringHint:filterResultsUsingProfileIdentifier:options:withBlock:]_block_invoke.289
+ ___116-[URLCompletionDatabase enumerateMatchDataForTypedStringHint:filterResultsUsingProfileIdentifier:options:withBlock:]_block_invoke_2.291
+ ___121-[CompletionList _completionsByMergingRecentSearches:withSuggestions:userTypedString:queryID:topHits:forPrivateBrowsing:]_block_invoke
+ ___121-[CompletionList _completionsByMergingRecentSearches:withSuggestions:userTypedString:queryID:topHits:forPrivateBrowsing:]_block_invoke_2
+ ___32-[BrowserController closeWindow]_block_invoke.963
+ ___32-[BrowserController closeWindow]_block_invoke.963.cold.1
+ ___34-[TabDocument _showDownload:path:]_block_invoke.323
+ ___34-[TabDocument _showDownload:path:]_block_invoke.330
+ ___34-[TabDocument _showDownload:path:]_block_invoke.330.cold.1
+ ___34-[TabDocument _showDownload:path:]_block_invoke.331
+ ___39-[BrowserController didEnterBackground]_block_invoke.78
+ ___41-[StartPageController _highlightsSection]_block_invoke.322
+ ___41-[StartPageController _highlightsSection]_block_invoke_2.327
+ ___41-[StartPageController _highlightsSection]_block_invoke_3.328
+ ___41-[StartPageController _highlightsSection]_block_invoke_4.330
+ ___41-[StartPageController _highlightsSection]_block_invoke_5.331
+ ___41-[TabSwitcherViewController _makeContent]_block_invoke.58
+ ___42-[Application resyncHistoryWithProfileID:]_block_invoke
+ ___43-[Application _resyncHistoryWithProfileID:]_block_invoke
+ ___43-[Application _resyncHistoryWithProfileID:]_block_invoke_2
+ ___43-[Application _resyncHistoryWithProfileID:]_block_invoke_2.cold.1
+ ___44-[URLCompletionProvider setQueryToComplete:]_block_invoke.218
+ ___45-[Application saveChangesToCloudHistoryStore]_block_invoke_2
+ ___45-[Application saveChangesToCloudHistoryStore]_block_invoke_2.cold.1
+ ___46-[BrowserRootViewController _layOutTopBanners]_block_invoke.185
+ ___47-[CatalogViewController _reloadCompletionTable]_block_invoke
+ ___47-[CatalogViewController resumeSearchWithQuery:]_block_invoke
+ ___50-[CatalogViewController completionsViewController]_block_invoke
+ ___53-[Application _getCloudHistoryWithCompletionHandler:]_block_invoke
+ ___53-[Application _getCloudHistoryWithCompletionHandler:]_block_invoke_2
+ ___55-[Application pdfDataForTabWithUUID:completionHandler:]_block_invoke.409
+ ___55-[Application pdfDataForTabWithUUID:completionHandler:]_block_invoke.409.cold.1
+ ___56-[Application prewarmAndRemoveOrphanedProfileDataStores]_block_invoke.267
+ ___56-[Application prewarmAndRemoveOrphanedProfileDataStores]_block_invoke.267.cold.1
+ ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1159
+ ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1160
+ ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1161
+ ___58-[SafariClearBrowsingDataController clearDataWithRequest:]_block_invoke
+ ___58-[SafariClearBrowsingDataController clearDataWithRequest:]_block_invoke_2
+ ___60-[Application _saveFrequentlyVisitedListsToDatabaseIfNeeded]_block_invoke.99
+ ___67-[CatalogViewController completionListDidRestoreCachedCompletions:]_block_invoke
+ ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke
+ ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke.361
+ ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke_2
+ ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke_2.363
+ ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke_2.363.cold.1
+ ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke_2.cold.1
+ ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke_3
+ ___68-[Application _updateCloudFeatureAvailabilityWithCompletionHandler:]_block_invoke_3.cold.1
+ ___71-[BrowserController _extractTextFromReaderWebViewOfTab:withCompletion:]_block_invoke.1125
+ ___71-[BrowserController _extractTextFromReaderWebViewOfTab:withCompletion:]_block_invoke.1125.cold.1
+ ___72-[BrowserController _sendPDFRepresentationForScreenshotWithTabDocument:]_block_invoke.1185
+ ___73-[TabDocument _presentTranslationConsentAlertWithType:completionHandler:]_block_invoke.743
+ ___74-[BrowserController toggleBookmarksPresentationWithCollection:completion:]_block_invoke.1049
+ ___74-[TabController(Persistence) persistTabs:inTabGroupWithUUID:inBackground:]_block_invoke_2.cold.1
+ ___75-[BrowserController addBookmarkNavController:didFinishWithResult:bookmark:]_block_invoke.1021
+ ___77-[TabDocument _showFinanceKitOrderPreviewControllerWithURL:dismissalHandler:]_block_invoke.314
+ ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke.182
+ ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke_2.183
+ ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke_3.184
+ ___83-[TabDocument webView:decidePolicyForNavigationAction:preferences:decisionHandler:]_block_invoke.528
+ ___90-[StartPageController startPageCustomizationViewController:didCustomizeItems:withVariant:]_block_invoke.361
+ ___91-[StartPageController startPageCustomizationViewController:didSelectCustomBackgroundImage:]_block_invoke.373
+ ___91-[StartPageController startPageCustomizationViewController:didSelectCustomBackgroundImage:]_block_invoke.373.cold.1
+ ___91-[StartPageController startPageCustomizationViewController:didSelectCustomBackgroundImage:]_block_invoke.374
+ ___92-[TabDocument _internalWebView:decidePolicyForNavigationAction:preferences:decisionHandler:]_block_invoke.539
+ ___92-[TabDocument _internalWebView:decidePolicyForNavigationAction:preferences:decisionHandler:]_block_invoke_2.540
+ ___92-[TabDocument _internalWebView:decidePolicyForNavigationAction:preferences:decisionHandler:]_block_invoke_3.553
+ ___93-[StartPageController _updateMetadataForCardProxy:withURL:title:cardProxiesToMetadataTokens:]_block_invoke
+ ___96-[BrowserController catalogViewController:presentViewControllerWithinPopover:completionHandler:]_block_invoke.214
+ ___97-[CatalogViewController dismissCompletionDetailWindowAndResumeEditingIfNeeded:completionHandler:]_block_invoke.128
+ ___98-[CapsuleNavigationBarViewController capsuleCollectionView:createSupplementaryViewWithIdentifier:]_block_invoke_5
+ ___Block_byref_object_copy_.740
+ ___Block_byref_object_dispose_.741
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96bs104r_e23_v16?0"UIAlertAction"8ls32l8r104l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_32_e42_v16?0"<WBSCloudHistoryServiceProtocol>"8l
+ ___block_descriptor_40_e8_32s_e42_v16?0"<WBSCloudHistoryServiceProtocol>"8ls32l8
+ ___block_descriptor_40_ea8_32s_e51_v24?0"<WBSStartPageCardProxy>"8"WBSRecentItem"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e54_v24?0"<WBSCloudHistoryServiceProtocol>"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_ea8_32c114_ZTSKZ100-[TabDocument _webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:]E3$_1_e5_v8?0l
+ ___block_descriptor_48_ea8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48w_e33_v16?0"WBSSiteMetadataResponse"8lw48l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40bs48w_e26_v16?0"_WKFrameTreeNode"8lw48l8s40l8s32l8
+ ___block_descriptor_65_ea8_32s40s48bs56w_e33_v24?0q8"WKWebpagePreferences"16lw56l8s48l8s32l8s40l8
+ ___block_descriptor_89_ea8_32s40s48s56s64s_e16_v16?0"NSData"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_97_ea8_32s40s48s56s64s72bs_e8_v12?0B8ls32l8s40l8s72l8s48l8s56l8s64l8
+ ___block_descriptor_98_ea8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s72l8s48l8s56l8s64l8
+ ___block_literal_global.1012
+ ___block_literal_global.102
+ ___block_literal_global.1048
+ ___block_literal_global.1053
+ ___block_literal_global.1065
+ ___block_literal_global.1091
+ ___block_literal_global.1096
+ ___block_literal_global.1116
+ ___block_literal_global.1121
+ ___block_literal_global.1122
+ ___block_literal_global.1124
+ ___block_literal_global.1126
+ ___block_literal_global.1128
+ ___block_literal_global.113
+ ___block_literal_global.1130
+ ___block_literal_global.1133
+ ___block_literal_global.1140
+ ___block_literal_global.1148
+ ___block_literal_global.1152
+ ___block_literal_global.1158
+ ___block_literal_global.1172
+ ___block_literal_global.152
+ ___block_literal_global.161
+ ___block_literal_global.192
+ ___block_literal_global.195
+ ___block_literal_global.199
+ ___block_literal_global.201
+ ___block_literal_global.203
+ ___block_literal_global.205
+ ___block_literal_global.215
+ ___block_literal_global.225
+ ___block_literal_global.228
+ ___block_literal_global.230
+ ___block_literal_global.234
+ ___block_literal_global.270
+ ___block_literal_global.271
+ ___block_literal_global.288
+ ___block_literal_global.2916
+ ___block_literal_global.297
+ ___block_literal_global.318
+ ___block_literal_global.323
+ ___block_literal_global.332
+ ___block_literal_global.334
+ ___block_literal_global.339
+ ___block_literal_global.341
+ ___block_literal_global.355
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.368
+ ___block_literal_global.376
+ ___block_literal_global.381
+ ___block_literal_global.389
+ ___block_literal_global.399
+ ___block_literal_global.403
+ ___block_literal_global.407
+ ___block_literal_global.414
+ ___block_literal_global.416
+ ___block_literal_global.432
+ ___block_literal_global.436
+ ___block_literal_global.520
+ ___block_literal_global.525
+ ___block_literal_global.578
+ ___block_literal_global.611
+ ___block_literal_global.66
+ ___block_literal_global.668
+ ___block_literal_global.736
+ ___block_literal_global.755
+ ___block_literal_global.784
+ ___block_literal_global.797
+ ___block_literal_global.81
+ ___block_literal_global.847
+ ___block_literal_global.891
+ ___block_literal_global.917
+ ___block_literal_global.92
+ ___block_literal_global.966
+ ___copy_helper_block_ea8_32c114_ZTSKZ100-[TabDocument _webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:]E3$_1
+ ___destroy_helper_block_ea8_32c114_ZTSKZ100-[TabDocument _webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:]E3$_1
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_memcpy5_4
+ ___swift_mutable_project_boxed_opaque_existential_1
+ _block_copy_helper.171
+ _block_copy_helper.199
+ _block_copy_helper.205
+ _block_copy_helper.211
+ _block_copy_helper.70
+ _block_copy_helper.76
+ _block_descriptor.173
+ _block_descriptor.201
+ _block_descriptor.207
+ _block_descriptor.213
+ _block_descriptor.72
+ _block_descriptor.78
+ _block_destroy_helper.172
+ _block_destroy_helper.200
+ _block_destroy_helper.206
+ _block_destroy_helper.212
+ _block_destroy_helper.71
+ _block_destroy_helper.77
+ _objc_msgSend$_addRecentSearchesToListing:
+ _objc_msgSend$_cancelFaviconRequest
+ _objc_msgSend$_completionsByMergingRecentSearches:withSuggestions:userTypedString:queryID:topHits:forPrivateBrowsing:
+ _objc_msgSend$_configureImageForTableViewCellIfNeeded:completionList:usingBottomCapsule:
+ _objc_msgSend$_configureSubtitleLabelForTableViewCellIfNeeded:
+ _objc_msgSend$_configureTitleLabelForTableViewCell:
+ _objc_msgSend$_fastAddFolderTitle
+ _objc_msgSend$_getCloudHistoryWithCompletionHandler:
+ _objc_msgSend$_resyncHistoryWithProfileID:
+ _objc_msgSend$_setupBrowserControllerForTestingWithPageTestController:completionHandler:
+ _objc_msgSend$_swipeActionForRecentSearches:atIndexPath:
+ _objc_msgSend$_updateCloudFeatureAvailabilityWithCompletionHandler:
+ _objc_msgSend$_updateMetadataForCardProxy:withURL:title:cardProxiesToMetadataTokens:
+ _objc_msgSend$_updateSearchSuggestionCompletionItemSelectionForQueryString:
+ _objc_msgSend$_updateSubtitle:forTableViewCell:
+ _objc_msgSend$afterDate
+ _objc_msgSend$autocompleteToFirstSuggestion
+ _objc_msgSend$canUpdateReflectedItemForTopSuggestionText:
+ _objc_msgSend$catalogViewController:didSelectSearch:richSearchSuggestionEntityIDURLParameter:
+ _objc_msgSend$clearAllProfiles
+ _objc_msgSend$clearDataWithRequest:
+ _objc_msgSend$clearDistractionControlSettings
+ _objc_msgSend$clearSearchCaches
+ _objc_msgSend$closeAllTabs
+ _objc_msgSend$copyRichSearchSuggestionItemFromSuggestion:
+ _objc_msgSend$databaseID
+ _objc_msgSend$defaultSuggestedFolderDestinations
+ _objc_msgSend$didCommitToSpeculativeLoad
+ _objc_msgSend$didDecideNavigationPolicyForFrame:
+ _objc_msgSend$didEnterTabOverviewFromSwipeGesture
+ _objc_msgSend$didUpdateShouldShowNotification
+ _objc_msgSend$donateTextInWebView:extractedReaderText:canDonateFullPageText:profileIdentifier:personalizationData:
+ _objc_msgSend$ensureBookmarksNotMarkedAsReadingListItems
+ _objc_msgSend$entityIDURLParameter
+ _objc_msgSend$extractedArticleText
+ _objc_msgSend$fetchOpenSearchDescriptionWithURL:
+ _objc_msgSend$filterOutUnlikelyMatchesBeforeTopHitPromotionFromMatches:forQuery:
+ _objc_msgSend$filterOutUnlikelyMatchesFromTopHits:forQuery:
+ _objc_msgSend$indexPathOfAutocompletedSuggestion
+ _objc_msgSend$initWithHitTestResult:forCurrentURL:modifierFlags:
+ _objc_msgSend$initWithImage:forPersona:
+ _objc_msgSend$initWithLinkPresentationMetadataProvider:
+ _objc_msgSend$initWithQueryString:forPrivateBrowsing:richSearchSuggestionEntityIDURLParameter:
+ _objc_msgSend$initWithSearchEngineInfo:queryString:richSearchSuggestionEntityIDURLParameter:
+ _objc_msgSend$initWithSearchEngineSuggestion:richSearchSuggestion:postFixString:userQuery:forPrivateBrowsing:isOfflineSearchSuggestion:
+ _objc_msgSend$isReaderViewInSeparateProcessEnabled
+ _objc_msgSend$isShowingSearchEngineOnboardingCard
+ _objc_msgSend$isSpecialFolder
+ _objc_msgSend$makeTrailingButtonWithManager:folderTitleProvider:sizeUpdateHandler:menuPresentationHandler:
+ _objc_msgSend$migrateBookmarksMarkedAsReadingListItemsIfNeeded
+ _objc_msgSend$navigationIntentWithSearchText:richSearchSuggestionEntityIDURLParameter:
+ _objc_msgSend$needsToBeNotifiedOfNavigationPolicyDecision
+ _objc_msgSend$originPage
+ _objc_msgSend$position
+ _objc_msgSend$quickWebsiteSearchJavaScriptInjectionController:receivedDetectedSearchURLString:fromWebView:inFrame:
+ _objc_msgSend$quickWebsiteSearchJavaScriptInjectionController:receivedOpenSearchSchemaURL:fromWebView:
+ _objc_msgSend$receivedTouchDownOutsideOfTabBar
+ _objc_msgSend$recentAndSuggestedCompletionStringsByMergingRecentSearches:withSuggestions:userTypedString:userTypedStringHasMultipleCorrespondingRichSuggestions:
+ _objc_msgSend$recordConsoleLogIfRunningTest:
+ _objc_msgSend$resyncHistoryWithProfileID:
+ _objc_msgSend$resyncHistoryWithProfileID:completionHandler:
+ _objc_msgSend$richSearchSuggestion
+ _objc_msgSend$richSearchSuggestionEntityIDURLParameter
+ _objc_msgSend$richSearchSuggestionsForSearchString:
+ _objc_msgSend$richSearchSuggestionsResult
+ _objc_msgSend$safari_createUserContentController
+ _objc_msgSend$safari_defaultProfileUserContentController
+ _objc_msgSend$safari_getFrameTreeNodeForFrameWithHandle:completionHandler:
+ _objc_msgSend$saveFaviconImageData:usingWebView:iconURL:pageURL:originalPageURL:size:isPrivate:completionHandler:
+ _objc_msgSend$search:richSearchSuggestionEntityIDURLParameter:
+ _objc_msgSend$searchEngineOnboardingProviderForStartPageFromProviders:
+ _objc_msgSend$searchQueryBuilderWithQuery:forPrivateBrowsing:richSearchSuggestionEntityIDURLParameter:
+ _objc_msgSend$searchURLForUserTypedString:richSearchSuggestionEntityIDURLParameter:
+ _objc_msgSend$setCompletionHandler:
+ _objc_msgSend$setExtractedArticleText:
+ _objc_msgSend$setHidesSubtitleLabel:
+ _objc_msgSend$setOpenSearchDescriptionURLString:forSourcePageURLString:
+ _objc_msgSend$setShouldAutocomplete:
+ _objc_msgSend$setShowsSwipeToTabOverviewTip:
+ _objc_msgSend$setSubtitleLabel:
+ _objc_msgSend$sharedFetcher
+ _objc_msgSend$shouldAutocomplete
+ _objc_msgSend$shouldAutocompleteTopSuggestionFromSearchProvider
+ _objc_msgSend$shouldMoveSuggestionFromSearchProvider:toTopOfSectionForUserTypedQuery:
+ _objc_msgSend$shouldShowTip
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$userDidEngageWithCompletionListItem:method:
+ _objc_msgSend$userDidEngageWithCompletionListItem:method:doesMatchSiriSuggestion:voiceSearchQueryID:
+ _objc_msgSend$willSubmitFormValues:frameInfo:userObject:submissionHandler:
+ _objectdestroy.188Tm
+ _objectdestroy.35Tm
+ _objectdestroy.39Tm
+ _objectdestroy.6Tm
+ _swift_makeBoxUnique
+ _symbolic $s14MobileSafariUI25BookmarksSaveStateManagerC19CurrentDateProviderP
+ _symbolic SSyc
+ _symbolic SaySDySSypGG
+ _symbolic Say_____G 14MobileSafariUI25BookmarksSaveStateManagerC10FolderInfoV
+ _symbolic So8NSStringCIeyBa_
+ _symbolic _____ 14MobileSafariUI25BookmarksSaveStateManagerC
+ _symbolic _____ 14MobileSafariUI25BookmarksSaveStateManagerC0eF0C
+ _symbolic _____ 14MobileSafariUI25BookmarksSaveStateManagerC10FolderInfoV
+ _symbolic _____ 14MobileSafariUI25BookmarksSaveStateManagerC26DefaultCurrentDateProvider33_51D94BDDBAB9292D73E7E973E3879C71LLC
+ _symbolic _____Sg 12CoreGraphics7CGFloatV
+ _symbolic _____Sg_ABt 10Foundation9IndexPathV
+ _symbolic ______p 14MobileSafariUI25BookmarksSaveStateManagerC19CurrentDateProviderP
+ _symbolic _____ySDySSypGG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 14MobileSafariUI25BookmarksSaveStateManagerC10FolderInfoV
+ _type_layout_string 14MobileSafariUI25BookmarksSaveStateManagerC10FolderInfoV
+ _type_layout_string So23BookmarksCollectionTypea
- +[CompletionList _completionsByMergingRecentSearches:withSuggestions:andLiteralSearch:queryID:topHits:forPrivateBrowsing:]
- +[SearchQueryBuilder searchQueryBuilderWithQuery:forPrivateBrowsing:]
- -[ActivityItemConfiguration .cxx_destruct]
- -[ActivityItemConfiguration activityItemsConfigurationMetadataForItemAtIndex:key:]
- -[ActivityItemConfiguration activityItemsConfigurationMetadataForKey:]
- -[ActivityItemConfiguration activityItemsConfigurationPreviewForItemAtIndex:intent:suggestedSize:]
- -[ActivityItemConfiguration activityItemsConfigurationSupportsInteraction:]
- -[ActivityItemConfiguration applicationActivitiesForActivityItemsConfiguration]
- -[ActivityItemConfiguration initWithInnerItemConfigurationProvider:additionalItemProviders:]
- -[ActivityItemConfiguration itemProvidersForActivityItemsConfiguration]
- -[BookmarksBarView setShowsSeparator:]
- -[BookmarksBarView showsSeparator]
- -[BrowserController _doSearch:]
- -[BrowserController _showDefaultBrowserSheetIfNecessary]
- -[BrowserController browserViewController:didCreateNavigationBar:]
- -[BrowserController catalogViewController:didSelectSearch:]
- -[BrowserController configureMenuAndAdoptButton:]
- -[BrowserController currentContentUUIDForNavigationBar:]
- -[BrowserController dataOwnerForNavigationBar:]
- -[BrowserController extractedArticleText]
- -[BrowserController itemProviderForNavigationBar:]
- -[BrowserController navigationBar:didCreateLeadingToolbar:trailingToolbar:]
- -[BrowserController navigationBar:didProduceNavigationIntent:]
- -[BrowserController navigationBarDidLayoutSubviews:]
- -[BrowserController navigationBarURLForSharing:]
- -[BrowserRootViewController _showWelcomeBrowsingExplanationSheet]
- -[BrowserRootViewController dismissDefaultBrowserSheetForOtherWindows]
- -[BrowserRootViewController dismissDefaultBrowserSheet]
- -[BrowserRootViewController isShowingDefaultBrowserSheet]
- -[BrowserRootViewController navigationBar]
- -[BrowserRootViewController showDefaultBrowserSheetWithDisplayHandler:]
- -[CatalogViewController _logQueryEngagement]
- -[CatalogViewController search:]
- -[CatalogViewController tableViewDidFinishReload:]
- -[CatalogViewController unifiedField:didEngageWithQuerySuggestion:forQueryString:]
- -[CatalogViewController updateQuerySuggestionsFromResponse:]
- -[CompletionList clearCachedSearches]
- -[NavigationBar newTextField]
- -[NavigationBar placeholderHorizontalInset]
- -[NavigationBar setExpanded:textFieldSelectionRange:]
- -[NavigationBar setTextFieldPlaceHolderColor:]
- -[NavigationBar textField]
- -[SafariClearBrowsingDataController clearDataAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeTabs:]
- -[SafariClearBrowsingDataController clearHistoryViewController:clearHistoryVisitsAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeAllTabs:]
- -[SearchQueryBuilder initWithQueryString:forPrivateBrowsing:]
- -[SearchQueryBuilder initWithSearchEngineInfo:queryString:]
- -[SearchSuggestion _configureHistoryLastAccessedLabelForTableViewCellIfNeeded:]
- -[SearchSuggestion initWithSearchEngineSuggestion:postFixString:userQuery:forPrivateBrowsing:isOfflineSearchSuggestion:]
- -[SearchSuggestionTableViewCell _isLabelPreviousSearchesInCompletionListEnabled]
- -[SearchSuggestionTableViewCell hidesHistoryLastAccessedLabel]
- -[SearchSuggestionTableViewCell setHidesHistoryLastAccessedLabel:]
- -[SearchSuggestionTableViewCell setHistoryLastAccessedLabel:]
- -[StartPageController _recentCloudTabItemsDidReceiveMetadata:]
- -[SystemNoteTakingController _isSystemNoteTakingEnabledForSafari]
- -[TabDocument _loadSearchResultForQuery:]
- -[TabDocument _loadUserTypedAddress:]
- -[TabDocument _webView:willSubmitFormValues:userObject:submissionHandler:]
- -[TabDocument didAutoDetectSiteSpecificSearchProviderWithOriginatingURL:searchURLTemplate:]
- -[UnifiedField contextCompleter]
- -[UnifiedField hasSelectedQuerySuggestion]
- -[UnifiedField insertTextSuggestion:]
- -[UnifiedField lastInputWasQuerySuggestion]
- -[UnifiedField querySuggestions]
- -[UnifiedField setContextCompleter:]
- GCC_except_table1003
- GCC_except_table1019
- GCC_except_table1025
- GCC_except_table1030
- GCC_except_table1034
- GCC_except_table1041
- GCC_except_table1043
- GCC_except_table1048
- GCC_except_table1052
- GCC_except_table1053
- GCC_except_table1055
- GCC_except_table1064
- GCC_except_table1080
- GCC_except_table1082
- GCC_except_table1087
- GCC_except_table1089
- GCC_except_table1093
- GCC_except_table1101
- GCC_except_table1112
- GCC_except_table1120
- GCC_except_table1124
- GCC_except_table1130
- GCC_except_table1131
- GCC_except_table1132
- GCC_except_table1134
- GCC_except_table1146
- GCC_except_table1152
- GCC_except_table1153
- GCC_except_table1155
- GCC_except_table1158
- GCC_except_table1171
- GCC_except_table1176
- GCC_except_table1180
- GCC_except_table1192
- GCC_except_table1194
- GCC_except_table1196
- GCC_except_table1199
- GCC_except_table1200
- GCC_except_table1208
- GCC_except_table1228
- GCC_except_table1231
- GCC_except_table1233
- GCC_except_table1234
- GCC_except_table1236
- GCC_except_table1237
- GCC_except_table1238
- GCC_except_table1244
- GCC_except_table1256
- GCC_except_table1257
- GCC_except_table1258
- GCC_except_table1259
- GCC_except_table1260
- GCC_except_table1262
- GCC_except_table1263
- GCC_except_table1264
- GCC_except_table1265
- GCC_except_table1266
- GCC_except_table1267
- GCC_except_table1269
- GCC_except_table1270
- GCC_except_table1271
- GCC_except_table1272
- GCC_except_table133
- GCC_except_table1344
- GCC_except_table1350
- GCC_except_table139
- GCC_except_table162
- GCC_except_table167
- GCC_except_table368
- GCC_except_table370
- GCC_except_table372
- GCC_except_table383
- GCC_except_table396
- GCC_except_table409
- GCC_except_table427
- GCC_except_table430
- GCC_except_table470
- GCC_except_table487
- GCC_except_table490
- GCC_except_table521
- GCC_except_table530
- GCC_except_table539
- GCC_except_table546
- GCC_except_table553
- GCC_except_table602
- GCC_except_table615
- GCC_except_table654
- GCC_except_table659
- GCC_except_table666
- GCC_except_table674
- GCC_except_table681
- GCC_except_table684
- GCC_except_table689
- GCC_except_table691
- GCC_except_table707
- GCC_except_table715
- GCC_except_table728
- GCC_except_table776
- GCC_except_table777
- GCC_except_table785
- GCC_except_table799
- GCC_except_table800
- GCC_except_table826
- GCC_except_table830
- GCC_except_table835
- GCC_except_table836
- GCC_except_table837
- GCC_except_table838
- GCC_except_table855
- GCC_except_table856
- GCC_except_table866
- GCC_except_table891
- GCC_except_table911
- GCC_except_table935
- GCC_except_table943
- GCC_except_table949
- GCC_except_table970
- GCC_except_table975
- GCC_except_table977
- GCC_except_table994
- GCC_except_table997
- _CGSizeMake
- _OBJC_CLASS_$_ActivityItemConfiguration
- _OBJC_CLASS_$_NavigationBar
- _OBJC_CLASS_$_SFDefaultBrowserPromptController
- _OBJC_CLASS_$_SFDefaultBrowserViewController
- _OBJC_CLASS_$_SFSearchSuggestion
- _OBJC_CLASS_$_SFSuggestionEngagementFeedback
- _OBJC_CLASS_$_SystemNoteTakingController
- _OBJC_CLASS_$_WBSAutoFillJavaScriptInjectionController
- _OBJC_CLASS_$_WBSQuerySuggestion
- _OBJC_CLASS_$__SFNavigationBar
- _OBJC_IVAR_$_ActivityItemConfiguration._additionalItemProviders
- _OBJC_IVAR_$_ActivityItemConfiguration._innerProvider
- _OBJC_IVAR_$_ActivityItemConfiguration._innerProviderItemCount
- _OBJC_IVAR_$_BookmarksBarView._separator
- _OBJC_IVAR_$_BrowserController._extractedArticleText
- _OBJC_IVAR_$_BrowserRootViewController._defaultBrowserSheet
- _OBJC_IVAR_$_BrowserRootViewController._defaultBrowserViewController
- _OBJC_IVAR_$_BrowserRootViewController._navigationBar
- _OBJC_IVAR_$_CatalogViewController._completionTableIsReloading
- _OBJC_IVAR_$_SearchSuggestionTableViewCell._accessoryContainerStackView
- _OBJC_IVAR_$_SearchSuggestionTableViewCell._accessoryContainerView
- _OBJC_IVAR_$_SearchSuggestionTableViewCell._hidesHistoryLastAccessedLabel
- _OBJC_IVAR_$_StartPageController._coalescedRecentCloudTabsSectionUpdateTimer
- _OBJC_IVAR_$_TabDocument._siteSpecificSearchEventListenerInterface
- _OBJC_IVAR_$_UnifiedField._contextCompleter
- _OBJC_IVAR_$_UnifiedField._hasSelectedQuerySuggestion
- _OBJC_IVAR_$_UnifiedField._lastInputWasQuerySuggestion
- _OBJC_IVAR_$_UnifiedField._querySuggestions
- _OBJC_METACLASS_$_ActivityItemConfiguration
- _OBJC_METACLASS_$_NavigationBar
- _OBJC_METACLASS_$_SystemNoteTakingController
- _OBJC_METACLASS_$_WBSSystemNoteTakingController
- _OBJC_METACLASS_$__SFNavigationBar
- _UIWindowLevelStatusBar
- _WBSRecentsStoreDidUpdateRecentItemsWithMetadataNotification
- _WBS_LOG_CHANNEL_PREFIXAppReviewPrompt
- _WBS_LOG_CHANNEL_PREFIXAppReviewPrompt.cold.1
- _WBS_LOG_CHANNEL_PREFIXAppReviewPrompt.log
- _WBS_LOG_CHANNEL_PREFIXAppReviewPrompt.onceToken
- _WBS_LOG_CHANNEL_PREFIXAutoFillAuthentication
- _WBS_LOG_CHANNEL_PREFIXAutoFillAuthentication.cold.1
- _WBS_LOG_CHANNEL_PREFIXAutoFillAuthentication.log
- _WBS_LOG_CHANNEL_PREFIXAutoFillAuthentication.onceToken
- _WBS_LOG_CHANNEL_PREFIXBookmarks
- _WBS_LOG_CHANNEL_PREFIXBookmarks.cold.1
- _WBS_LOG_CHANNEL_PREFIXBookmarks.log
- _WBS_LOG_CHANNEL_PREFIXBookmarks.onceToken
- _WBS_LOG_CHANNEL_PREFIXBrowsingAssistant
- _WBS_LOG_CHANNEL_PREFIXBrowsingAssistant.cold.1
- _WBS_LOG_CHANNEL_PREFIXBrowsingAssistant.log
- _WBS_LOG_CHANNEL_PREFIXBrowsingAssistant.onceToken
- _WBS_LOG_CHANNEL_PREFIXCloudBookmarks
- _WBS_LOG_CHANNEL_PREFIXCloudBookmarks.cold.1
- _WBS_LOG_CHANNEL_PREFIXCloudBookmarks.log
- _WBS_LOG_CHANNEL_PREFIXCloudBookmarks.onceToken
- _WBS_LOG_CHANNEL_PREFIXCloudHistory
- _WBS_LOG_CHANNEL_PREFIXCloudHistory.cold.1
- _WBS_LOG_CHANNEL_PREFIXCloudHistory.log
- _WBS_LOG_CHANNEL_PREFIXCloudHistory.onceToken
- _WBS_LOG_CHANNEL_PREFIXCloudSettings
- _WBS_LOG_CHANNEL_PREFIXCloudSettings.cold.1
- _WBS_LOG_CHANNEL_PREFIXCloudSettings.log
- _WBS_LOG_CHANNEL_PREFIXCloudSettings.onceToken
- _WBS_LOG_CHANNEL_PREFIXCloudTabs
- _WBS_LOG_CHANNEL_PREFIXCloudTabs.cold.1
- _WBS_LOG_CHANNEL_PREFIXCloudTabs.log
- _WBS_LOG_CHANNEL_PREFIXCloudTabs.onceToken
- _WBS_LOG_CHANNEL_PREFIXContentBlockers
- _WBS_LOG_CHANNEL_PREFIXContentBlockers.cold.1
- _WBS_LOG_CHANNEL_PREFIXContentBlockers.log
- _WBS_LOG_CHANNEL_PREFIXContentBlockers.onceToken
- _WBS_LOG_CHANNEL_PREFIXContinuity
- _WBS_LOG_CHANNEL_PREFIXContinuity.cold.1
- _WBS_LOG_CHANNEL_PREFIXContinuity.log
- _WBS_LOG_CHANNEL_PREFIXContinuity.onceToken
- _WBS_LOG_CHANNEL_PREFIXCycler
- _WBS_LOG_CHANNEL_PREFIXCycler.cold.1
- _WBS_LOG_CHANNEL_PREFIXCycler.log
- _WBS_LOG_CHANNEL_PREFIXCycler.onceToken
- _WBS_LOG_CHANNEL_PREFIXDataMigration
- _WBS_LOG_CHANNEL_PREFIXDataMigration.cold.1
- _WBS_LOG_CHANNEL_PREFIXDataMigration.log
- _WBS_LOG_CHANNEL_PREFIXDataMigration.onceToken
- _WBS_LOG_CHANNEL_PREFIXDownloads
- _WBS_LOG_CHANNEL_PREFIXDownloads.cold.1
- _WBS_LOG_CHANNEL_PREFIXDownloads.log
- _WBS_LOG_CHANNEL_PREFIXDownloads.onceToken
- _WBS_LOG_CHANNEL_PREFIXExtensions
- _WBS_LOG_CHANNEL_PREFIXExtensions.cold.1
- _WBS_LOG_CHANNEL_PREFIXExtensions.log
- _WBS_LOG_CHANNEL_PREFIXExtensions.onceToken
- _WBS_LOG_CHANNEL_PREFIXHistory
- _WBS_LOG_CHANNEL_PREFIXHistory.cold.1
- _WBS_LOG_CHANNEL_PREFIXHistory.log
- _WBS_LOG_CHANNEL_PREFIXHistory.onceToken
- _WBS_LOG_CHANNEL_PREFIXHistoryViewController
- _WBS_LOG_CHANNEL_PREFIXHistoryViewController.cold.1
- _WBS_LOG_CHANNEL_PREFIXHistoryViewController.log
- _WBS_LOG_CHANNEL_PREFIXHistoryViewController.onceToken
- _WBS_LOG_CHANNEL_PREFIXInterstellar
- _WBS_LOG_CHANNEL_PREFIXInterstellar.cold.1
- _WBS_LOG_CHANNEL_PREFIXInterstellar.log
- _WBS_LOG_CHANNEL_PREFIXInterstellar.onceToken
- _WBS_LOG_CHANNEL_PREFIXLayout
- _WBS_LOG_CHANNEL_PREFIXLayout.cold.1
- _WBS_LOG_CHANNEL_PREFIXLayout.log
- _WBS_LOG_CHANNEL_PREFIXLayout.onceToken
- _WBS_LOG_CHANNEL_PREFIXLoweredTabBar
- _WBS_LOG_CHANNEL_PREFIXLoweredTabBar.cold.1
- _WBS_LOG_CHANNEL_PREFIXLoweredTabBar.log
- _WBS_LOG_CHANNEL_PREFIXLoweredTabBar.onceToken
- _WBS_LOG_CHANNEL_PREFIXMediaCapture
- _WBS_LOG_CHANNEL_PREFIXMediaCapture.cold.1
- _WBS_LOG_CHANNEL_PREFIXMediaCapture.log
- _WBS_LOG_CHANNEL_PREFIXMediaCapture.onceToken
- _WBS_LOG_CHANNEL_PREFIXOther
- _WBS_LOG_CHANNEL_PREFIXOther.cold.1
- _WBS_LOG_CHANNEL_PREFIXOther.log
- _WBS_LOG_CHANNEL_PREFIXOther.onceToken
- _WBS_LOG_CHANNEL_PREFIXPLT
- _WBS_LOG_CHANNEL_PREFIXPLT.cold.1
- _WBS_LOG_CHANNEL_PREFIXPLT.log
- _WBS_LOG_CHANNEL_PREFIXPLT.onceToken
- _WBS_LOG_CHANNEL_PREFIXPageLoading
- _WBS_LOG_CHANNEL_PREFIXPageLoading.cold.1
- _WBS_LOG_CHANNEL_PREFIXPageLoading.log
- _WBS_LOG_CHANNEL_PREFIXPageLoading.onceToken
- _WBS_LOG_CHANNEL_PREFIXParsec
- _WBS_LOG_CHANNEL_PREFIXParsec.cold.1
- _WBS_LOG_CHANNEL_PREFIXParsec.log
- _WBS_LOG_CHANNEL_PREFIXParsec.onceToken
- _WBS_LOG_CHANNEL_PREFIXPerformanceTest
- _WBS_LOG_CHANNEL_PREFIXPerformanceTest.cold.1
- _WBS_LOG_CHANNEL_PREFIXPerformanceTest.log
- _WBS_LOG_CHANNEL_PREFIXPerformanceTest.onceToken
- _WBS_LOG_CHANNEL_PREFIXPrinting
- _WBS_LOG_CHANNEL_PREFIXPrinting.cold.1
- _WBS_LOG_CHANNEL_PREFIXPrinting.log
- _WBS_LOG_CHANNEL_PREFIXPrinting.onceToken
- _WBS_LOG_CHANNEL_PREFIXPrivateBrowsing
- _WBS_LOG_CHANNEL_PREFIXPrivateBrowsing.cold.1
- _WBS_LOG_CHANNEL_PREFIXPrivateBrowsing.log
- _WBS_LOG_CHANNEL_PREFIXPrivateBrowsing.onceToken
- _WBS_LOG_CHANNEL_PREFIXProfiles
- _WBS_LOG_CHANNEL_PREFIXProfiles.cold.1
- _WBS_LOG_CHANNEL_PREFIXProfiles.log
- _WBS_LOG_CHANNEL_PREFIXProfiles.onceToken
- _WBS_LOG_CHANNEL_PREFIXPush
- _WBS_LOG_CHANNEL_PREFIXPush.cold.1
- _WBS_LOG_CHANNEL_PREFIXPush.log
- _WBS_LOG_CHANNEL_PREFIXPush.onceToken
- _WBS_LOG_CHANNEL_PREFIXReadingList
- _WBS_LOG_CHANNEL_PREFIXReadingList.cold.1
- _WBS_LOG_CHANNEL_PREFIXReadingList.log
- _WBS_LOG_CHANNEL_PREFIXReadingList.onceToken
- _WBS_LOG_CHANNEL_PREFIXSignposts
- _WBS_LOG_CHANNEL_PREFIXSignposts.cold.1
- _WBS_LOG_CHANNEL_PREFIXSignposts.log
- _WBS_LOG_CHANNEL_PREFIXSignposts.onceToken
- _WBS_LOG_CHANNEL_PREFIXSiriIntelligence
- _WBS_LOG_CHANNEL_PREFIXSiriIntelligence.cold.1
- _WBS_LOG_CHANNEL_PREFIXSiriIntelligence.log
- _WBS_LOG_CHANNEL_PREFIXSiriIntelligence.onceToken
- _WBS_LOG_CHANNEL_PREFIXSiriLink
- _WBS_LOG_CHANNEL_PREFIXSiriLink.cold.1
- _WBS_LOG_CHANNEL_PREFIXSiriLink.log
- _WBS_LOG_CHANNEL_PREFIXSiriLink.onceToken
- _WBS_LOG_CHANNEL_PREFIXSiriReadThis
- _WBS_LOG_CHANNEL_PREFIXSiriReadThis.cold.1
- _WBS_LOG_CHANNEL_PREFIXSiriReadThis.log
- _WBS_LOG_CHANNEL_PREFIXSiriReadThis.onceToken
- _WBS_LOG_CHANNEL_PREFIXSiriSuggestedSites
- _WBS_LOG_CHANNEL_PREFIXSiriSuggestedSites.cold.1
- _WBS_LOG_CHANNEL_PREFIXSiriSuggestedSites.log
- _WBS_LOG_CHANNEL_PREFIXSiriSuggestedSites.onceToken
- _WBS_LOG_CHANNEL_PREFIXStartPage
- _WBS_LOG_CHANNEL_PREFIXStartPage.cold.1
- _WBS_LOG_CHANNEL_PREFIXStartPage.log
- _WBS_LOG_CHANNEL_PREFIXStartPage.onceToken
- _WBS_LOG_CHANNEL_PREFIXSystemNoteTaking
- _WBS_LOG_CHANNEL_PREFIXSystemNoteTaking.cold.1
- _WBS_LOG_CHANNEL_PREFIXSystemNoteTaking.log
- _WBS_LOG_CHANNEL_PREFIXSystemNoteTaking.onceToken
- _WBS_LOG_CHANNEL_PREFIXTabGroup
- _WBS_LOG_CHANNEL_PREFIXTabGroup.cold.1
- _WBS_LOG_CHANNEL_PREFIXTabGroup.log
- _WBS_LOG_CHANNEL_PREFIXTabGroup.onceToken
- _WBS_LOG_CHANNEL_PREFIXTabSnapshots
- _WBS_LOG_CHANNEL_PREFIXTabSnapshots.cold.1
- _WBS_LOG_CHANNEL_PREFIXTabSnapshots.log
- _WBS_LOG_CHANNEL_PREFIXTabSnapshots.onceToken
- _WBS_LOG_CHANNEL_PREFIXTabView
- _WBS_LOG_CHANNEL_PREFIXTabView.cold.1
- _WBS_LOG_CHANNEL_PREFIXTabView.log
- _WBS_LOG_CHANNEL_PREFIXTabView.onceToken
- _WBS_LOG_CHANNEL_PREFIXTabs
- _WBS_LOG_CHANNEL_PREFIXTabs.cold.1
- _WBS_LOG_CHANNEL_PREFIXTabs.log
- _WBS_LOG_CHANNEL_PREFIXTabs.onceToken
- _WBS_LOG_CHANNEL_PREFIXTest
- _WBS_LOG_CHANNEL_PREFIXTest.cold.1
- _WBS_LOG_CHANNEL_PREFIXTest.log
- _WBS_LOG_CHANNEL_PREFIXTest.onceToken
- _WBS_LOG_CHANNEL_PREFIXURLAutocomplete
- _WBS_LOG_CHANNEL_PREFIXURLAutocomplete.cold.1
- _WBS_LOG_CHANNEL_PREFIXURLAutocomplete.log
- _WBS_LOG_CHANNEL_PREFIXURLAutocomplete.onceToken
- _WBS_LOG_CHANNEL_PREFIXUserInteraction
- _WBS_LOG_CHANNEL_PREFIXUserInteraction.cold.1
- _WBS_LOG_CHANNEL_PREFIXUserInteraction.log
- _WBS_LOG_CHANNEL_PREFIXUserInteraction.onceToken
- _WBS_LOG_CHANNEL_PREFIXUserInterface
- _WBS_LOG_CHANNEL_PREFIXUserInterface.cold.1
- _WBS_LOG_CHANNEL_PREFIXUserInterface.log
- _WBS_LOG_CHANNEL_PREFIXUserInterface.onceToken
- _WBS_LOG_CHANNEL_PREFIXWebClips
- _WBS_LOG_CHANNEL_PREFIXWebClips.cold.1
- _WBS_LOG_CHANNEL_PREFIXWebClips.log
- _WBS_LOG_CHANNEL_PREFIXWebClips.onceToken
- _WBS_LOG_CHANNEL_PREFIXWebDriver
- _WBS_LOG_CHANNEL_PREFIXWebDriver.cold.1
- _WBS_LOG_CHANNEL_PREFIXWebDriver.log
- _WBS_LOG_CHANNEL_PREFIXWebDriver.onceToken
- _WBS_LOG_CHANNEL_PREFIXWebExtensions
- _WBS_LOG_CHANNEL_PREFIXWebExtensions.cold.1
- _WBS_LOG_CHANNEL_PREFIXWebExtensions.log
- _WBS_LOG_CHANNEL_PREFIXWebExtensions.onceToken
- _WBS_LOG_CHANNEL_PREFIXWebsiteData
- _WBS_LOG_CHANNEL_PREFIXWebsiteData.cold.1
- _WBS_LOG_CHANNEL_PREFIXWebsiteData.log
- _WBS_LOG_CHANNEL_PREFIXWebsiteData.onceToken
- _WBS_LOG_CHANNEL_PREFIXWidgets
- _WBS_LOG_CHANNEL_PREFIXWidgets.cold.1
- _WBS_LOG_CHANNEL_PREFIXWidgets.log
- _WBS_LOG_CHANNEL_PREFIXWidgets.onceToken
- __OBJC_$_INSTANCE_METHODS_ActivityItemConfiguration
- __OBJC_$_INSTANCE_METHODS_NavigationBar
- __OBJC_$_INSTANCE_METHODS_SystemNoteTakingController
- __OBJC_$_INSTANCE_VARIABLES_ActivityItemConfiguration
- __OBJC_$_PROP_LIST_ActivityItemConfiguration
- __OBJC_$_PROP_LIST_NavigationBar
- __OBJC_$_PROP_LIST_UIActivityItemsConfigurationReading
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIActivityItemsConfigurationReading
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__SFNavigationBarDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_QuickWebsiteSearchEventListener
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFMenuConfiguring
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIActivityItemsConfigurationReading
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFNavigationBarDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_QuickWebsiteSearchEventListener
- __OBJC_$_PROTOCOL_METHOD_TYPES_SFMenuConfiguring
- __OBJC_$_PROTOCOL_METHOD_TYPES_UIActivityItemsConfigurationReading
- __OBJC_$_PROTOCOL_METHOD_TYPES__SFNavigationBarDelegate
- __OBJC_$_PROTOCOL_REFS_QuickWebsiteSearchEventListener
- __OBJC_$_PROTOCOL_REFS_SFMenuConfiguring
- __OBJC_$_PROTOCOL_REFS_UIActivityItemsConfigurationReading
- __OBJC_$_PROTOCOL_REFS__SFNavigationBarDelegate
- __OBJC_CLASS_PROTOCOLS_$_ActivityItemConfiguration
- __OBJC_CLASS_RO_$_ActivityItemConfiguration
- __OBJC_CLASS_RO_$_NavigationBar
- __OBJC_CLASS_RO_$_SystemNoteTakingController
- __OBJC_LABEL_PROTOCOL_$_QuickWebsiteSearchEventListener
- __OBJC_LABEL_PROTOCOL_$_SFMenuConfiguring
- __OBJC_LABEL_PROTOCOL_$_UIActivityItemsConfigurationReading
- __OBJC_LABEL_PROTOCOL_$__SFNavigationBarDelegate
- __OBJC_METACLASS_RO_$_ActivityItemConfiguration
- __OBJC_METACLASS_RO_$_NavigationBar
- __OBJC_METACLASS_RO_$_SystemNoteTakingController
- __OBJC_PROTOCOL_$_QuickWebsiteSearchEventListener
- __OBJC_PROTOCOL_$_SFMenuConfiguring
- __OBJC_PROTOCOL_$_UIActivityItemsConfigurationReading
- __OBJC_PROTOCOL_$__SFNavigationBarDelegate
- __OBJC_PROTOCOL_REFERENCE_$_QuickWebsiteSearchEventListener
- __SFLinkHoverFrameKey
- __SFLinkHoverTargetFrameKey
- __SFLinkHoverURLKey
- __ZNSt3__120__shared_ptr_emplaceIZ74-[TabDocument _webView:willSubmitFormValues:userObject:submissionHandler:]E23CompletionHandlerCallerNS_9allocatorIS1_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceIZ74-[TabDocument _webView:willSubmitFormValues:userObject:submissionHandler:]E23CompletionHandlerCallerNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceIZ74-[TabDocument _webView:willSubmitFormValues:userObject:submissionHandler:]E23CompletionHandlerCallerNS_9allocatorIS1_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceIZ74-[TabDocument _webView:willSubmitFormValues:userObject:submissionHandler:]E23CompletionHandlerCallerNS_9allocatorIS1_EEED1Ev
- __ZTVNSt3__120__shared_ptr_emplaceIZ74-[TabDocument _webView:willSubmitFormValues:userObject:submissionHandler:]E23CompletionHandlerCallerNS_9allocatorIS1_EEEE
- ___114-[BrowserRootViewController capsuleNavigationBarViewController:selectedItemWillChangeToState:options:coordinator:]_block_invoke.289
- ___116-[URLCompletionDatabase enumerateMatchDataForTypedStringHint:filterResultsUsingProfileIdentifier:options:withBlock:]_block_invoke.285
- ___116-[URLCompletionDatabase enumerateMatchDataForTypedStringHint:filterResultsUsingProfileIdentifier:options:withBlock:]_block_invoke_2.287
- ___117-[SafariClearBrowsingDataController clearDataAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeTabs:]_block_invoke
- ___117-[SafariClearBrowsingDataController clearDataAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeTabs:]_block_invoke_2
- ___122+[CompletionList _completionsByMergingRecentSearches:withSuggestions:andLiteralSearch:queryID:topHits:forPrivateBrowsing:]_block_invoke
- ___122+[CompletionList _completionsByMergingRecentSearches:withSuggestions:andLiteralSearch:queryID:topHits:forPrivateBrowsing:]_block_invoke_2
- ___32-[BrowserController closeWindow]_block_invoke.958
- ___32-[BrowserController closeWindow]_block_invoke.958.cold.1
- ___34-[TabDocument _showDownload:path:]_block_invoke.287
- ___34-[TabDocument _showDownload:path:]_block_invoke.294
- ___34-[TabDocument _showDownload:path:]_block_invoke.294.cold.1
- ___34-[TabDocument _showDownload:path:]_block_invoke.295
- ___37-[UnifiedField insertTextSuggestion:]_block_invoke
- ___39-[BrowserController didEnterBackground]_block_invoke.75
- ___41-[StartPageController _highlightsSection]_block_invoke.328
- ___41-[StartPageController _highlightsSection]_block_invoke_2.333
- ___41-[StartPageController _highlightsSection]_block_invoke_3.334
- ___41-[StartPageController _highlightsSection]_block_invoke_4.336
- ___41-[StartPageController _highlightsSection]_block_invoke_5.337
- ___41-[TabSwitcherViewController _makeContent]_block_invoke.54
- ___44-[URLCompletionProvider setQueryToComplete:]_block_invoke.214
- ___45-[Application saveChangesToCloudHistoryStore]_block_invoke.cold.1
- ___46-[Application _updateCloudFeatureAvailability]_block_invoke.356
- ___46-[Application _updateCloudFeatureAvailability]_block_invoke_2
- ___46-[Application _updateCloudFeatureAvailability]_block_invoke_2.358
- ___46-[Application _updateCloudFeatureAvailability]_block_invoke_2.358.cold.1
- ___46-[Application _updateCloudFeatureAvailability]_block_invoke_2.cold.1
- ___46-[Application _updateCloudFeatureAvailability]_block_invoke_3
- ___46-[Application _updateCloudFeatureAvailability]_block_invoke_3.cold.1
- ___46-[BrowserRootViewController _layOutTopBanners]_block_invoke.187
- ___47-[SearchSuggestionProvider setQueryToComplete:]_block_invoke_2
- ___53-[CatalogViewController textFieldShouldBeginEditing:]_block_invoke
- ___53-[CatalogViewController textFieldShouldBeginEditing:]_block_invoke_2
- ___55-[Application pdfDataForTabWithUUID:completionHandler:]_block_invoke.406
- ___55-[Application pdfDataForTabWithUUID:completionHandler:]_block_invoke.406.cold.1
- ___56-[Application prewarmAndRemoveOrphanedProfileDataStores]_block_invoke.263
- ___56-[Application prewarmAndRemoveOrphanedProfileDataStores]_block_invoke.263.cold.1
- ___56-[BrowserController _showDefaultBrowserSheetIfNecessary]_block_invoke
- ___56-[BrowserController _showDefaultBrowserSheetIfNecessary]_block_invoke_2
- ___56-[BrowserController _showDefaultBrowserSheetIfNecessary]_block_invoke_3
- ___56-[BrowserController _showDefaultBrowserSheetIfNecessary]_block_invoke_4
- ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1162
- ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1163
- ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1164
- ___58-[BrowserRootViewController _updateTopBarAllowingRemoval:]_block_invoke_2
- ___60-[Application _saveFrequentlyVisitedListsToDatabaseIfNeeded]_block_invoke.97
- ___60-[TabDocument _donateTextAllowingDonationWithoutReaderText:]_block_invoke
- ___62-[StartPageController _recentCloudTabItemsDidReceiveMetadata:]_block_invoke
- ___65-[BrowserRootViewController _showWelcomeBrowsingExplanationSheet]_block_invoke
- ___71-[BrowserController _extractTextFromReaderWebViewOfTab:withCompletion:]_block_invoke.1127
- ___71-[BrowserController _extractTextFromReaderWebViewOfTab:withCompletion:]_block_invoke.1127.cold.1
- ___71-[BrowserRootViewController showDefaultBrowserSheetWithDisplayHandler:]_block_invoke
- ___71-[BrowserRootViewController showDefaultBrowserSheetWithDisplayHandler:]_block_invoke_2
- ___72-[BrowserController _sendPDFRepresentationForScreenshotWithTabDocument:]_block_invoke.1188
- ___73-[TabDocument _presentTranslationConsentAlertWithType:completionHandler:]_block_invoke.710
- ___74-[BrowserController toggleBookmarksPresentationWithCollection:completion:]_block_invoke.1050
- ___74-[TabDocument _webView:willSubmitFormValues:userObject:submissionHandler:]_block_invoke
- ___75-[BrowserController addBookmarkNavController:didFinishWithResult:bookmark:]_block_invoke.1022
- ___77-[TabDocument _showFinanceKitOrderPreviewControllerWithURL:dismissalHandler:]_block_invoke.278
- ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke.177
- ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke_14
- ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke_15
- ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke_16
- ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke_2.178
- ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke_3.179
- ___84-[CatalogViewController _textFieldEditingChangedForUpdatingCompletionListOnRestore:]_block_invoke
- ___88-[BrowserController _requestQueryResultsOnTabDocument:forText:contentType:pageMetadata:]_block_invoke
- ___88-[BrowserController _requestQueryResultsOnTabDocument:forText:contentType:pageMetadata:]_block_invoke_2
- ___89-[WBSPageTestController(MobileSafari) pageTestControllerInitializeApp:completionHandler:]_block_invoke
- ___89-[WBSPageTestController(MobileSafari) pageTestControllerInitializeApp:completionHandler:]_block_invoke_2
- ___90-[StartPageController startPageCustomizationViewController:didCustomizeItems:withVariant:]_block_invoke.367
- ___91-[StartPageController startPageCustomizationViewController:didSelectCustomBackgroundImage:]_block_invoke.379
- ___91-[StartPageController startPageCustomizationViewController:didSelectCustomBackgroundImage:]_block_invoke.379.cold.1
- ___91-[StartPageController startPageCustomizationViewController:didSelectCustomBackgroundImage:]_block_invoke.380
- ___92-[TabDocument _internalWebView:decidePolicyForNavigationAction:preferences:decisionHandler:]_block_invoke.504
- ___92-[TabDocument _internalWebView:decidePolicyForNavigationAction:preferences:decisionHandler:]_block_invoke_2.505
- ___92-[TabDocument _internalWebView:decidePolicyForNavigationAction:preferences:decisionHandler:]_block_invoke_3.518
- ___96-[BrowserController catalogViewController:presentViewControllerWithinPopover:completionHandler:]_block_invoke.209
- ___97-[CatalogViewController dismissCompletionDetailWindowAndResumeEditingIfNeeded:completionHandler:]_block_invoke.131
- ___Block_byref_object_copy_.707
- ___Block_byref_object_dispose_.708
- ___WBS_LOG_CHANNEL_PREFIXAppReviewPrompt_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXAutoFillAuthentication_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXBookmarks_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXBrowsingAssistant_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXCloudBookmarks_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXCloudHistory_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXCloudSettings_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXCloudTabs_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXContentBlockers_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXContinuity_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXCycler_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXDataMigration_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXDownloads_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXExtensions_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXHistoryViewController_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXHistory_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXInterstellar_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXLayout_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXLoweredTabBar_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXMediaCapture_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXOther_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXPLT_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXPageLoading_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXParsec_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXPerformanceTest_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXPrinting_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXPrivateBrowsing_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXProfiles_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXPush_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXReadingList_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXSignposts_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXSiriIntelligence_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXSiriLink_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXSiriReadThis_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXSiriSuggestedSites_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXStartPage_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXSystemNoteTaking_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXTabGroup_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXTabSnapshots_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXTabView_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXTabs_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXTest_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXURLAutocomplete_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXUserInteraction_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXUserInterface_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXWebClips_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXWebDriver_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXWebExtensions_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXWebsiteData_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXWidgets_block_invoke
- ___block_descriptor_113_e8_32s40s48s56s64s72s80s88bs96r_e23_v16?0"UIAlertAction"8ls32l8r96l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_32_e28_v24?0"NSString"8"NSURL"16l
- ___block_descriptor_32_e45_"WBSQuerySuggestion"16?0"CKContextResult"8l
- ___block_descriptor_32_e51_v24?0"<WBSStartPageCardProxy>"8"WBSRecentItem"16l
- ___block_descriptor_40_e8_32s_e54_v24?0"<WBSCloudHistoryServiceProtocol>"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32w_e27_v16?0"CKContextResponse"8lw32l8
- ___block_descriptor_48_ea8_32c87_ZTSKZ74-[TabDocument _webView:willSubmitFormValues:userObject:submissionHandler:]E3$_1_e5_v8?0l
- ___block_descriptor_48_ea8_32s40s_e31_v24?0"NSString"8"NSString"16ls32l8s40l8
- ___block_descriptor_49_e8_32s40s_e36_"SearchSuggestion"16?0"NSString"8ls32l8s40l8
- ___block_descriptor_56_ea8_32s40w48w_e5_v8?0ls32l8w40l8w48l8
- ___block_descriptor_57_ea8_32s40bs48w_e33_v24?0q8"WKWebpagePreferences"16lw48l8s32l8s40l8
- ___block_descriptor_81_ea8_32s40s48s56s_e16_v16?0"NSData"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_89_ea8_32s40s48s56s64bs_e8_v12?0B8ls32l8s40l8s64l8s48l8s56l8
- ___block_descriptor_90_ea8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
- ___block_literal_global.100
- ___block_literal_global.1013
- ___block_literal_global.1049
- ___block_literal_global.1055
- ___block_literal_global.1067
- ___block_literal_global.1093
- ___block_literal_global.1098
- ___block_literal_global.1101
- ___block_literal_global.1107
- ___block_literal_global.1109
- ___block_literal_global.1111
- ___block_literal_global.1113
- ___block_literal_global.1115
- ___block_literal_global.112
- ___block_literal_global.1123
- ___block_literal_global.1135
- ___block_literal_global.1143
- ___block_literal_global.1151
- ___block_literal_global.1155
- ___block_literal_global.1161
- ___block_literal_global.1175
- ___block_literal_global.121
- ___block_literal_global.127
- ___block_literal_global.13
- ___block_literal_global.133
- ___block_literal_global.136
- ___block_literal_global.142
- ___block_literal_global.145
- ___block_literal_global.146
- ___block_literal_global.151
- ___block_literal_global.158
- ___block_literal_global.160
- ___block_literal_global.163
- ___block_literal_global.169
- ___block_literal_global.175
- ___block_literal_global.178
- ___block_literal_global.181
- ___block_literal_global.184
- ___block_literal_global.187
- ___block_literal_global.194
- ___block_literal_global.196
- ___block_literal_global.197
- ___block_literal_global.198
- ___block_literal_global.200
- ___block_literal_global.202
- ___block_literal_global.216
- ___block_literal_global.22
- ___block_literal_global.226
- ___block_literal_global.231
- ___block_literal_global.233
- ___block_literal_global.247
- ___block_literal_global.25
- ___block_literal_global.256
- ___block_literal_global.263
- ___block_literal_global.274
- ___block_literal_global.28
- ___block_literal_global.289
- ___block_literal_global.291
- ___block_literal_global.294
- ___block_literal_global.2945
- ___block_literal_global.31
- ___block_literal_global.315
- ___block_literal_global.319
- ___block_literal_global.320
- ___block_literal_global.330
- ___block_literal_global.340
- ___block_literal_global.350
- ___block_literal_global.351
- ___block_literal_global.358
- ___block_literal_global.363
- ___block_literal_global.365
- ___block_literal_global.370
- ___block_literal_global.384
- ___block_literal_global.386
- ___block_literal_global.393
- ___block_literal_global.400
- ___block_literal_global.404
- ___block_literal_global.411
- ___block_literal_global.413
- ___block_literal_global.426
- ___block_literal_global.433
- ___block_literal_global.487
- ___block_literal_global.492
- ___block_literal_global.543
- ___block_literal_global.553
- ___block_literal_global.579
- ___block_literal_global.61
- ___block_literal_global.636
- ___block_literal_global.64
- ___block_literal_global.67
- ___block_literal_global.703
- ___block_literal_global.722
- ___block_literal_global.73
- ___block_literal_global.773
- ___block_literal_global.798
- ___block_literal_global.802
- ___block_literal_global.83
- ___block_literal_global.842
- ___block_literal_global.88
- ___block_literal_global.886
- ___block_literal_global.91
- ___block_literal_global.912
- ___block_literal_global.94
- ___block_literal_global.961
- ___copy_helper_block_ea8_32c87_ZTSKZ74-[TabDocument _webView:willSubmitFormValues:userObject:submissionHandler:]E3$_1
- ___destroy_helper_block_ea8_32c87_ZTSKZ74-[TabDocument _webView:willSubmitFormValues:userObject:submissionHandler:]E3$_1
- _block_copy_helper.161
- _block_copy_helper.189
- _block_copy_helper.195
- _block_copy_helper.201
- _block_copy_helper.213
- _block_descriptor.163
- _block_descriptor.191
- _block_descriptor.197
- _block_descriptor.203
- _block_descriptor.215
- _block_destroy_helper.162
- _block_destroy_helper.190
- _block_destroy_helper.196
- _block_destroy_helper.202
- _block_destroy_helper.214
- _objc_msgSend$_completionsByMergingRecentSearches:withSuggestions:andLiteralSearch:queryID:topHits:forPrivateBrowsing:
- _objc_msgSend$_configureHistoryLastAccessedLabelForTableViewCellIfNeeded:
- _objc_msgSend$_controlsAlpha
- _objc_msgSend$_isLabelPreviousSearchesInCompletionListEnabled
- _objc_msgSend$_logQueryEngagement
- _objc_msgSend$_overrideLayoutParametersWithMinimumLayoutSize:maximumUnobscuredSizeOverride:
- _objc_msgSend$_showWelcomeBrowsingExplanationSheet
- _objc_msgSend$activityItemsConfigurationMetadataForItemAtIndex:key:
- _objc_msgSend$activityItemsConfigurationMetadataForKey:
- _objc_msgSend$activityItemsConfigurationPreviewForItemAtIndex:intent:suggestedSize:
- _objc_msgSend$activityItemsConfigurationSupportsInteraction:
- _objc_msgSend$applicationActivitiesForActivityItemsConfiguration
- _objc_msgSend$bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:
- _objc_msgSend$browserIconReplacementAlertController:browserLocalizedName:completionHandler:
- _objc_msgSend$browserViewController:didCreateNavigationBar:
- _objc_msgSend$catalogViewController:didSelectSearch:
- _objc_msgSend$clearCachedSearches
- _objc_msgSend$clearDataAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeTabs:
- _objc_msgSend$configureMenuAndAdoptButton:
- _objc_msgSend$contextCompleter
- _objc_msgSend$determineIfBrowserIconSwapAlertNeedsDisplayWithCompletionHandler:
- _objc_msgSend$determineIfBrowserSheetNeedsDisplayWithCompletionHandler:
- _objc_msgSend$didCompleteBrowserSheet
- _objc_msgSend$discard
- _objc_msgSend$dismissDefaultBrowserSheet
- _objc_msgSend$dismissDefaultBrowserSheetForOtherWindows
- _objc_msgSend$donateTextInWebView:extractedReaderText:canDonateFullPageText:profileIdentifier:personalizationData:extractInnerText:
- _objc_msgSend$fetchMetadata
- _objc_msgSend$filterOutUnlikelyMatchesBeforeTopHitPromotionFromMatches:forQuery:searchProvider:
- _objc_msgSend$filterOutUnlikelyMatchesFromTopHits:forQuery:searchProvider:
- _objc_msgSend$frameForBarItem:inCoordinateSpace:
- _objc_msgSend$hasSelectedQuerySuggestion
- _objc_msgSend$hasToolbar
- _objc_msgSend$initWithHoveredLinkURL:forCurrentURL:modifierFlags:frame:targetFrame:
- _objc_msgSend$initWithIdentifier:suggestion:query:score:type:
- _objc_msgSend$initWithImage:forInputMode:
- _objc_msgSend$initWithInnerItemConfigurationProvider:additionalItemProviders:
- _objc_msgSend$initWithQueryString:forPrivateBrowsing:
- _objc_msgSend$initWithSearchEngineInfo:queryString:
- _objc_msgSend$initWithSearchEngineSuggestion:postFixString:userQuery:forPrivateBrowsing:isOfflineSearchSuggestion:
- _objc_msgSend$initWithSuggestion:
- _objc_msgSend$initWithTitle:identifier:type:tag:
- _objc_msgSend$initWithViewDidBecomeReady:completion:
- _objc_msgSend$inputText
- _objc_msgSend$isCloudKitBookmarksAvailable
- _objc_msgSend$isLockedPrivateBrowsingEnabled
- _objc_msgSend$isSafariProfilesEnabled
- _objc_msgSend$isSendingBarMetricsChangeNotification
- _objc_msgSend$isShowingDefaultBrowserSheet
- _objc_msgSend$itemProvidersForActivityItemsConfiguration
- _objc_msgSend$lastInputWasQuerySuggestion
- _objc_msgSend$liveCompletionList
- _objc_msgSend$logTransactionSuccessfulForInput:
- _objc_msgSend$makeTrailingButtonWithManager:sizeUpdateHandler:menuPresentationHandler:
- _objc_msgSend$minimumHeight
- _objc_msgSend$navigationIntentWithSearchText:
- _objc_msgSend$placeholderHorizontalInset
- _objc_msgSend$queryItems
- _objc_msgSend$querySuggestions
- _objc_msgSend$recentAndSuggestedCompletionStringsByMergingRecentSearches:withSuggestions:literalSearch:
- _objc_msgSend$registerToolbar:withLayout:persona:
- _objc_msgSend$safari_URLForKey:
- _objc_msgSend$safari_userContentController
- _objc_msgSend$saveFaviconImageData:iconURL:pageURL:originalPageURL:size:isPrivate:completionHandler:
- _objc_msgSend$search:
- _objc_msgSend$searchQueryBuilderWithQuery:forPrivateBrowsing:
- _objc_msgSend$setBackdropGroupDisabled:
- _objc_msgSend$setContextCompleter:
- _objc_msgSend$setExpanded:completionHandler:
- _objc_msgSend$setExpanded:textFieldSelectionRange:completionHandler:
- _objc_msgSend$setHasToolbar:
- _objc_msgSend$setHidesHistoryLastAccessedLabel:
- _objc_msgSend$setHistoryLastAccessedLabel:
- _objc_msgSend$setMaximumHeight:
- _objc_msgSend$setMenuButtonConfigurator:
- _objc_msgSend$setModalInPresentation:
- _objc_msgSend$setPlaceholderColor:
- _objc_msgSend$setQueryItems:
- _objc_msgSend$setQuerySuggestions:
- _objc_msgSend$setUnifiedFieldShowsProgressView:
- _objc_msgSend$setUpScriptInjectionWithUserContentController:
- _objc_msgSend$sf_tabSeparatorColor
- _objc_msgSend$shouldPerformPromptCheck
- _objc_msgSend$showDefaultBrowserSheetWithDisplayHandler:
- _objc_msgSend$suggestedFolderDestinations
- _objc_msgSend$unifiedField:didEngageWithQuerySuggestion:forQueryString:
- _objc_msgSend$updateQuerySuggestionsFromResponse:
- _objc_msgSend$userDidEngageWithCompletionListItem:onActionButton:method:
- _objc_msgSend$userDidEngageWithCompletionListItem:onActionButton:method:doesMatchSiriSuggestion:voiceSearchQueryID:
- _objc_msgSend$willSubmitFormValues:userObject:submissionHandler:
- _objectdestroy.178Tm
- _objectdestroy.28Tm
- _os_log_create
- _symbolic SaySo16UIViewControllerCG
- _symbolic _____y_____G s23_ContiguousArrayStorageC So10BookmarkIDa
- _type_layout_string So18UIActionIdentifiera
CStrings:
+ "; should autocomplete = %@"
+ "<%@: %p; string = %@; goes to URL: %@; private = %@"
+ "@\"WBSRichSearchSuggestion\""
+ "@\"WBSRichSearchSuggestion\"16@0:8"
+ "@\"WBSSystemNoteTakingController\""
+ "@\"_SFSearchEngineSelectionViewController\""
+ "@48@0:8@16@?24@?32@?40"
+ "@56@0:8@16@24@32@40B48B52"
+ "AddToReadingListButtonContextMenu"
+ "All (Reading List)"
+ "App lifecycle %{public}@: %zu windows, %zu total tabs across all windows, this window: %zu normal + %zu private = %zu tabs"
+ "Closing %zu tabs while updating tab group."
+ "CompactViewModeMenuItem"
+ "CopySearchTermMenuItem"
+ "Failed to resync profile with identifier %@: %{public}@"
+ "FirstLoadToComplete"
+ "Hide %@ History"
+ "Inserting %zu tabs while updating tab group."
+ "LargeViewModeMenuItem"
+ "No WBTabs found in %{public}@ - inserting placeholder tab."
+ "Persisting %zu tabs in tab group with UUID: %{public}@, inBackground: %d"
+ "ReadingListFilterSegmentedControl"
+ "Rich Suggestion"
+ "Rich Suggestion With Subtitle"
+ "RichSearchSuggestion"
+ "SegmentedControlSection"
+ "Show %@ History"
+ "T@\"NSNumber\",&,N,V_position"
+ "T@\"NSString\",C,N,V_extractedArticleText"
+ "T@\"UISegmentedControl\",N,&,VselectedCollectionControl"
+ "T@\"UITextField\",?,R,N"
+ "T@\"WBSRichSearchSuggestion\",?,R,N"
+ "T@\"WBSRichSearchSuggestion\",R,N,V_richSearchSuggestion"
+ "T@\"WBSSystemNoteTakingController\",R,N"
+ "TB,N,V_hidesSubtitleLabel"
+ "TB,N,V_shouldAutocomplete"
+ "TabController didUpdateTabsInTabGroupWithUUID: %{public}@ - tabGroup has %zu tabs"
+ "WBSQuickWebsiteSearchJavaScriptInjectionControllerDelegate"
+ "_SFSearchEngineSelectionViewControllerDelegate"
+ "_TtC14MobileSafariUI25BookmarksSaveStateManager"
+ "_TtCC14MobileSafariUI25BookmarksSaveStateManager9SaveState"
+ "_TtCC14MobileSafariUI25BookmarksSaveStateManagerP33_51D94BDDBAB9292D73E7E973E3879C7126DefaultCurrentDateProvider"
+ "_addRecentSearchesToListing:"
+ "_cancelFaviconRequest"
+ "_cloudHistoryStatus"
+ "_cloudTabProxiesToMetadataTokens"
+ "_completionsByMergingRecentSearches:withSuggestions:userTypedString:queryID:topHits:forPrivateBrowsing:"
+ "_configureImageForTableViewCellIfNeeded:completionList:usingBottomCapsule:"
+ "_configureSubtitleLabelForTableViewCellIfNeeded:"
+ "_configureTitleLabelForTableViewCell:"
+ "_deferredProcessingOpenSearchSchemaURL"
+ "_didAttemptInvalidAppLoadPreviously"
+ "_fastAddFolderTitle"
+ "_getCloudHistoryWithCompletionHandler:"
+ "_hidesSubtitleLabel"
+ "_needsSendTelemetryForLoadComplete"
+ "_position"
+ "_resyncHistoryWithProfileID:"
+ "_richSearchSuggestion"
+ "_searchEngineSelectionViewController"
+ "_setupBrowserControllerForTestingWithPageTestController:completionHandler:"
+ "_shouldAutocomplete"
+ "_swipeActionForRecentSearches:atIndexPath:"
+ "_updateCloudFeatureAvailabilityWithCompletionHandler:"
+ "_updateMetadataForCardProxy:withURL:title:cardProxiesToMetadataTokens:"
+ "_updateSearchSuggestionCompletionItemSelectionForQueryString:"
+ "_updateSubtitle:forTableViewCell:"
+ "_webView:didReceiveConsoleLogForTesting:"
+ "_webView:startXRSessionWithFeatures:colorFormat:depthFormat:completionHandler:"
+ "_webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:"
+ "afterDate"
+ "autocompleteToFirstSuggestion"
+ "beginDefaultSearchEngineOnboardingForStartPageViewController:completionHandler:"
+ "canUpdateReflectedItemForTopSuggestionText:"
+ "catalogViewController:didSelectSearch:richSearchSuggestionEntityIDURLParameter:"
+ "clearAllProfiles"
+ "clearDataWithRequest:"
+ "clearDistractionControlSettings"
+ "clearHistoryViewController:clearDataWithRequest:"
+ "clearSearchCaches"
+ "closeAllTabs"
+ "collectionViewControllers"
+ "completedLoad=NO enableTelemetry=YES "
+ "completedLoad=YES enableTelemetry=YES "
+ "copyRichSearchSuggestionItemFromSuggestion:"
+ "currentCollectionContentOffset"
+ "currentCollectionIndexPath"
+ "databaseID"
+ "dateProvider"
+ "defaultSuggestedFolderDestinations"
+ "didChangeShowSwipeToTabOverviewTip:"
+ "didCommitToSpeculativeLoad"
+ "didDecideNavigationPolicyForFrame:"
+ "didEnterTabOverviewFromMoreMenu"
+ "didEnterTabOverviewFromSwipeGesture"
+ "didUpdateShouldShowNotification"
+ "dismissSearchEngineSelectionTableViewAndPresentConfirmationSheet:"
+ "donateTextInWebView:extractedReaderText:canDonateFullPageText:profileIdentifier:personalizationData:"
+ "ensureBookmarksNotMarkedAsReadingListItems"
+ "entityIDURLParameter"
+ "fetchOpenSearchDescriptionWithURL:"
+ "filterOutUnlikelyMatchesBeforeTopHitPromotionFromMatches:forQuery:"
+ "filterOutUnlikelyMatchesFromTopHits:forQuery:"
+ "folderTitleProvider"
+ "hidesSubtitleLabel"
+ "historyStoreDidFailDatabaseIntegrityCheck:error:databaseURLs:"
+ "indexPathOfAutocompletedSuggestion"
+ "initWithHitTestResult:forCurrentURL:modifierFlags:"
+ "initWithImage:forPersona:"
+ "initWithLinkPresentationMetadataProvider:"
+ "initWithQueryString:forPrivateBrowsing:richSearchSuggestionEntityIDURLParameter:"
+ "initWithSearchEngineInfo:queryString:richSearchSuggestionEntityIDURLParameter:"
+ "initWithSearchEngineSuggestion:richSearchSuggestion:postFixString:userQuery:forPrivateBrowsing:isOfflineSearchSuggestion:"
+ "isReaderViewInSeparateProcessEnabled"
+ "isShowingSearchEngineOnboardingCard"
+ "isSpecialFolder"
+ "makeTrailingButtonWithManager:folderTitleProvider:sizeUpdateHandler:menuPresentationHandler:"
+ "migrateBookmarksMarkedAsReadingListItemsIfNeeded"
+ "navigationIntentWithSearchText:richSearchSuggestionEntityIDURLParameter:"
+ "navigationStack"
+ "needsToBeNotifiedOfNavigationPolicyDecision"
+ "originPage"
+ "pageTestControllerEncounteredError:completionHandler:"
+ "persistAllCurrentTabsInBackground: usesGlobalPinnedTabs=%d, unpinnedTabs=%zu, currentTabs=%zu, tabsToPersist=%zu"
+ "position"
+ "quickWebsiteSearchJavaScriptInjectionController:receivedDetectedSearchURLString:fromWebView:inFrame:"
+ "quickWebsiteSearchJavaScriptInjectionController:receivedOpenSearchSchemaURL:fromWebView:"
+ "receivedTouchDownOutsideOfTabBar"
+ "recentAndSuggestedCompletionStringsByMergingRecentSearches:withSuggestions:userTypedString:userTypedStringHasMultipleCorrespondingRichSuggestions:"
+ "recordConsoleLogIfRunningTest:"
+ "resyncHistoryWithProfileID:"
+ "resyncHistoryWithProfileID:completionHandler:"
+ "richSearchSuggestion"
+ "richSearchSuggestionEntityIDURLParameter"
+ "richSearchSuggestionsForSearchString:"
+ "richSearchSuggestionsResult"
+ "safari_createUserContentController"
+ "safari_defaultProfileUserContentController"
+ "safari_getFrameTreeNodeForFrameWithHandle:completionHandler:"
+ "saveFaviconImageData:usingWebView:iconURL:pageURL:originalPageURL:size:isPrivate:completionHandler:"
+ "saveStateInBackground called: inBackground=%d, needsValidate=%d, activeTabGroup=%{public}@"
+ "saveStateManager"
+ "search:richSearchSuggestionEntityIDURLParameter:"
+ "searchEngineOnboardingProviderForStartPageFromProviders:"
+ "searchQueryBuilderWithQuery:forPrivateBrowsing:richSearchSuggestionEntityIDURLParameter:"
+ "searchURLForUserTypedString:richSearchSuggestionEntityIDURLParameter:"
+ "selectedCollectionControl"
+ "setBackButtonDisplayMode:"
+ "setCompletionHandler:"
+ "setExtractedArticleText:"
+ "setHidesSubtitleLabel:"
+ "setOpenSearchDescriptionURLString:forSourcePageURLString:"
+ "setSelectedCollectionControl:"
+ "setShouldAutocomplete:"
+ "setShowsSwipeToTabOverviewTip:"
+ "sharedFetcher"
+ "shouldAutocomplete"
+ "shouldAutocompleteTopSuggestionFromSearchProvider"
+ "shouldMoveSuggestionFromSearchProvider:toTopOfSectionForUserTypedQuery:"
+ "shouldShowTip"
+ "timeIntervalSince1970"
+ "unsignedIntValue"
+ "updateSelectedCollectionControlIfNecessary"
+ "userDefaults"
+ "userDidEngageWithCompletionListItem:method:"
+ "userDidEngageWithCompletionListItem:method:doesMatchSiriSuggestion:voiceSearchQueryID:"
+ "v16@?0@\"<WBSCloudHistoryServiceProtocol>\"8"
+ "v16@?0@\"_WKFrameTreeNode\"8"
+ "v32@0:8@\"SFClearHistoryViewController\"16@\"SFBrowsingDataDeletionRequest\"24"
+ "v32@0:8@\"SFStartPageViewController\"16@?<v@?>24"
+ "v32@0:8@\"WKWebView\"16@\"NSString\"24"
+ "v40@0:8@\"CatalogViewController\"16@\"NSString\"24@\"NSString\"32"
+ "v40@0:8@\"WBSQuickWebsiteSearchJavaScriptInjectionController\"16@\"NSURL\"24@\"WKWebView\"32"
+ "v48@0:8@\"WBSQuickWebsiteSearchJavaScriptInjectionController\"16@\"NSString\"24@\"WKWebView\"32@\"WKFrameInfo\"40"
+ "v56@0:8@\"WKWebView\"16Q24Q32Q40@?<v@?@@\"UIViewController\">48"
+ "v56@0:8@16Q24Q32Q40@?48"
+ "v64@0:8@\"WKWebView\"16@\"NSDictionary\"24@\"WKFrameInfo\"32@\"WKFrameInfo\"40@\"NSObject<NSSecureCoding>\"48@?<v@?>56"
+ "wbTab should not be nil when trying to persist."
+ "willSubmitFormValues:frameInfo:userObject:submissionHandler:"
+ "withoutReloadingCount"
+ "\x94"
+ "\xf0!\xf0\xf0\x91\xc1\xf0\xf0\xf0\x81\xf0q\x82\xf0\x81"
+ "\xf0\xf0\xf0q"
- "$__lazy_storage_$_dismissButton"
- "<%@: %p; string = %@; goes to URL: %d; private = %@>"
- "@\"<UIActivityItemsConfigurationReading>\""
- "@\"NSItemProvider\"24@0:8@\"_SFNavigationBar\"16"
- "@\"NSItemProvider\"48@0:8q16@\"NSString\"24{CGSize=dd}32"
- "@\"NSURL\"24@0:8@\"_SFNavigationBar\"16"
- "@\"NSUUID\"24@0:8@\"_SFNavigationBar\"16"
- "@\"NavigationBar\""
- "@\"SFDefaultBrowserViewController\""
- "@\"SystemNoteTakingController\""
- "@\"WBSQuerySuggestion\"16@?0@\"CKContextResult\"8"
- "@\"WKWebView\"24@0:8@\"WBSPageContextDataFetcher\"16"
- "@24@0:8@\"NSString\"16"
- "@32@0:8q16@\"NSString\"24"
- "@40@0:8@16@?24@?32"
- "@48@0:8@16@24@32B40B44"
- "@48@0:8q16@24{CGSize=dd}32"
- "ActivityItemConfiguration"
- "AppReviewPrompt"
- "AutoFillAuthentication"
- "B24@0:8@\"WBSPageContextDataFetcher\"16"
- "BookmarkFolderId"
- "BrowsingAssistant"
- "Closing %zu tabs"
- "CloudBookmarks"
- "CloudHistory"
- "CloudSettings"
- "CloudTabs"
- "ContentBlockers"
- "Continuity"
- "CopySearchTermsButton"
- "Cycler"
- "DataMigration"
- "Extensions"
- "HistoryViewController"
- "Inserting %zu tabs"
- "Interstellar"
- "JavaScriptConsoleOutputPath"
- "JavaScriptConsoleOutputURLBookmarkData"
- "Layout"
- "LoweredTabBar"
- "MediaCapture"
- "NavigationBar"
- "Other"
- "PageLoading"
- "Parsec"
- "PerformanceTest"
- "Printing"
- "PrivateBrowsing"
- "Profiles"
- "Push"
- "QuickWebsiteSearchEventListener"
- "ReadingList"
- "SFMenuConfiguring"
- "Signposts"
- "SiriIntelligence"
- "SiriLink"
- "SiriReadThis"
- "SiriSuggestedSites"
- "StartPage"
- "SystemNoteTaking"
- "SystemNoteTakingController"
- "T@\"CKContextCompleter\",&,N,V_contextCompleter"
- "T@\"NSArray\",?,R,C,N"
- "T@\"NSArray\",R,N,V_querySuggestions"
- "T@\"NSDictionary\",N,C"
- "T@\"NSString\",R,C,N,V_extractedArticleText"
- "T@\"NavigationBar\",R,N,V_navigationBar"
- "T@\"SystemNoteTakingController\",R,N"
- "T@\"UITextField\",R,N"
- "TB,N,V_hidesHistoryLastAccessedLabel"
- "TB,R,N,GisShowingDefaultBrowserSheet"
- "TB,R,N,V_hasSelectedQuerySuggestion"
- "TB,R,N,V_lastInputWasQuerySuggestion"
- "TabGroup"
- "TabSnapshots"
- "TabView"
- "Test"
- "UIActivityItemsConfigurationReading"
- "URLAutocomplete"
- "UserInteraction"
- "UserInterface"
- "WebClips"
- "WebDriver"
- "WebExtensions"
- "WebsiteData"
- "Widgets"
- "_SFNavigationBarDelegate"
- "_accessoryContainerStackView"
- "_accessoryContainerView"
- "_additionalItemProviders"
- "_coalescedRecentCloudTabsSectionUpdateTimer"
- "_completionTableIsReloading"
- "_completionsByMergingRecentSearches:withSuggestions:andLiteralSearch:queryID:topHits:forPrivateBrowsing:"
- "_configureHistoryLastAccessedLabelForTableViewCellIfNeeded:"
- "_controlsAlpha"
- "_defaultBrowserSheet"
- "_defaultBrowserViewController"
- "_hasSelectedQuerySuggestion"
- "_hidesHistoryLastAccessedLabel"
- "_innerProvider"
- "_innerProviderItemCount"
- "_isSystemNoteTakingEnabledForSafari"
- "_lastInputWasQuerySuggestion"
- "_logQueryEngagement"
- "_overrideLayoutParametersWithMinimumLayoutSize:maximumUnobscuredSizeOverride:"
- "_querySuggestions"
- "_recentCloudTabItemsDidReceiveMetadata:"
- "_showWelcomeBrowsingExplanationSheet"
- "_siteSpecificSearchEventListenerInterface"
- "_webView:decideWebApplicationCacheQuotaForSecurityOrigin:currentQuota:totalBytesNeeded:decisionHandler:"
- "_webView:startXRSessionWithFeatures:completionHandler:"
- "activityItemsConfigurationMetadataForItemAtIndex:key:"
- "activityItemsConfigurationMetadataForKey:"
- "activityItemsConfigurationPreviewForItemAtIndex:intent:suggestedSize:"
- "activityItemsConfigurationSupportsInteraction:"
- "applicationActivitiesForActivityItemsConfiguration"
- "bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:"
- "browserIconReplacementAlertController:browserLocalizedName:completionHandler:"
- "browserViewController:didCreateNavigationBar:"
- "catalogViewController:didSelectSearch:"
- "clearCachedSearches"
- "clearDataAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeTabs:"
- "clearHistoryViewController:clearHistoryVisitsAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeAllTabs:"
- "configureMenuAndAdoptButton:"
- "contextCompleter"
- "currentContentUUIDForNavigationBar:"
- "dataOwnerForNavigationBar:"
- "destinationFolderTitle"
- "determineIfBrowserIconSwapAlertNeedsDisplayWithCompletionHandler:"
- "determineIfBrowserSheetNeedsDisplayWithCompletionHandler:"
- "didAutoDetectSiteSpecificSearchProviderWithOriginatingURL:searchURLTemplate:"
- "didCompleteBrowserSheet"
- "discard"
- "dismissDefaultBrowserSheet"
- "dismissDefaultBrowserSheetForOtherWindows"
- "donateTextInWebView:extractedReaderText:canDonateFullPageText:profileIdentifier:personalizationData:extractInnerText:"
- "fetchMetadata"
- "filterOutUnlikelyMatchesBeforeTopHitPromotionFromMatches:forQuery:searchProvider:"
- "filterOutUnlikelyMatchesFromTopHits:forQuery:searchProvider:"
- "frameForBarItem:inCoordinateSpace:"
- "hasSelectedQuerySuggestion"
- "hasToolbar"
- "hidesHistoryLastAccessedLabel"
- "initWithHoveredLinkURL:forCurrentURL:modifierFlags:frame:targetFrame:"
- "initWithIdentifier:suggestion:query:score:type:"
- "initWithImage:forInputMode:"
- "initWithInnerItemConfigurationProvider:additionalItemProviders:"
- "initWithQueryString:forPrivateBrowsing:"
- "initWithSearchEngineInfo:queryString:"
- "initWithSearchEngineSuggestion:postFixString:userQuery:forPrivateBrowsing:isOfflineSearchSuggestion:"
- "initWithSuggestion:"
- "initWithTitle:identifier:type:tag:"
- "initWithViewDidBecomeReady:completion:"
- "inputText"
- "isCloudKitBookmarksAvailable"
- "isLockedPrivateBrowsingEnabled"
- "isSafariProfilesEnabled"
- "isSendingBarMetricsChangeNotification"
- "isShowingDefaultBrowserSheet"
- "itemProviderForNavigationBar:"
- "itemProvidersForActivityItemsConfiguration"
- "lastInputWasQuerySuggestion"
- "liveCompletionList"
- "logTransactionSuccessfulForInput:"
- "makeTrailingButtonWithManager:sizeUpdateHandler:menuPresentationHandler:"
- "minimumHeight"
- "navigationBar:didCreateBar:trailingBar:"
- "navigationBar:didCreateLeadingToolbar:trailingToolbar:"
- "navigationBar:didProduceNavigationIntent:"
- "navigationBarDidLayoutSubviews:"
- "navigationBarDoneButtonWasTapped:"
- "navigationBarURLForSharing:"
- "navigationIntentWithSearchText:"
- "newTextField"
- "pageContextDataFetcherDidFetchTextSamples:forURL:"
- "pageContextDataFetcherShouldFetchTextSamples:"
- "q24@0:8@\"_SFNavigationBar\"16"
- "queryItems"
- "querySuggestions"
- "recentAndSuggestedCompletionStringsByMergingRecentSearches:withSuggestions:literalSearch:"
- "registerToolbar:withLayout:persona:"
- "safari_URLForKey:"
- "safari_userContentController"
- "saveFaviconImageData:iconURL:pageURL:originalPageURL:size:isPrivate:completionHandler:"
- "search:"
- "searchQueryBuilderWithQuery:forPrivateBrowsing:"
- "setBackdropGroupDisabled:"
- "setContextCompleter:"
- "setDismissButton:"
- "setExpanded:completionHandler:"
- "setExpanded:textFieldSelectionRange:"
- "setExpanded:textFieldSelectionRange:completionHandler:"
- "setHasToolbar:"
- "setHidesHistoryLastAccessedLabel:"
- "setHistoryLastAccessedLabel:"
- "setMaximumHeight:"
- "setMenuButtonConfigurator:"
- "setModalInPresentation:"
- "setQueryItems:"
- "setQuerySuggestions:"
- "setSavedState:"
- "setTextFieldPlaceHolderColor:"
- "setUnifiedFieldShowsProgressView:"
- "setUpScriptInjectionWithUserContentController:"
- "sf_tabSeparatorColor"
- "shouldPerformPromptCheck"
- "showDefaultBrowserSheetWithDisplayHandler:"
- "showingDefaultBrowserSheet"
- "unifiedField:didEngageWithQuerySuggestion:forQueryString:"
- "updateQuerySuggestionsFromResponse:"
- "userDidEngageWithCompletionListItem:onActionButton:method:"
- "userDidEngageWithCompletionListItem:onActionButton:method:doesMatchSiriSuggestion:voiceSearchQueryID:"
- "v24@0:8@\"UIButton\"16"
- "v24@0:8@\"_SFNavigationBar\"16"
- "v24@?0@\"NSString\"8@\"NSURL\"16"
- "v32@0:8@\"BrowserRootViewController\"16@\"NavigationBar\"24"
- "v32@0:8@\"NSString\"16@\"NSURL\"24"
- "v32@0:8@\"NSURL\"16@\"NSString\"24"
- "v32@0:8@\"_SFNavigationBar\"16@\"_SFNavigationIntent\"24"
- "v36@0:8B16{_NSRange=QQ}20"
- "v40@0:8@\"UnifiedField\"16@\"CKContextResult\"24@\"NSString\"32"
- "v40@0:8@\"WKWebView\"16Q24@?<v@?@@\"UIViewController\">32"
- "v40@0:8@\"_SFNavigationBar\"16@\"<SFBarRepresentable>\"24@\"<SFBarRepresentable>\"32"
- "v40@0:8@\"_SFNavigationBar\"16@\"UIToolbar\"24@\"UIToolbar\"32"
- "v48@0:8@16@24@32B40B44"
- "v56@0:8@\"SFClearHistoryViewController\"16@\"NSDate\"24@\"NSDate\"32@\"NSString\"40B48B52"
- "v56@0:8@\"WKWebView\"16@\"WKSecurityOrigin\"24Q32Q40@?<v@?Q>48"
- "v56@0:8@16@24@32@40B48B52"
- "v56@0:8@16@24Q32Q40@?48"
- "webViewForPageContextDataFetcher:"
- "willSubmitFormValues:userObject:submissionHandler:"
- "\xb4"
- "\xf01\xf0\xf0\x91\xc1\xf0\xf0\xf0a\xf0q\x82\xf0q"
- "\xf0\xf0\xf0a"

```
