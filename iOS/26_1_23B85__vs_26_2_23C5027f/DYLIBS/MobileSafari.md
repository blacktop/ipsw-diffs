## MobileSafari

> `/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari`

```diff

-622.2.11.10.8
-  __TEXT.__text: 0x46eb00
-  __TEXT.__auth_stubs: 0x5de0
-  __TEXT.__objc_methlist: 0x19ce8
-  __TEXT.__const: 0x187f4
-  __TEXT.__cstring: 0x1d37c
-  __TEXT.__gcc_except_tab: 0x72ec
+623.1.12.10.4
+  __TEXT.__text: 0x476590
+  __TEXT.__auth_stubs: 0x5fc0
+  __TEXT.__objc_methlist: 0x19f48
+  __TEXT.__const: 0x18864
+  __TEXT.__cstring: 0x1d9ec
+  __TEXT.__gcc_except_tab: 0x7308
   __TEXT.__oslogstring: 0x3d69
   __TEXT.__ustring: 0x2306
   __TEXT.__dlopen_cstrs: 0x43b
-  __TEXT.__swift5_typeref: 0xb84a
-  __TEXT.__swift5_capture: 0x630c
-  __TEXT.__constg_swiftt: 0x10188
-  __TEXT.__swift5_reflstr: 0xb7c0
-  __TEXT.__swift5_fieldmd: 0x8c74
+  __TEXT.__swift5_typeref: 0xb87c
+  __TEXT.__swift5_capture: 0x632c
+  __TEXT.__constg_swiftt: 0x10328
+  __TEXT.__swift5_reflstr: 0xba70
+  __TEXT.__swift5_fieldmd: 0x8da8
   __TEXT.__swift5_builtin: 0x35c
   __TEXT.__swift5_assocty: 0x14d0
-  __TEXT.__swift5_proto: 0xf04
-  __TEXT.__swift5_types: 0x800
+  __TEXT.__swift5_proto: 0xf08
+  __TEXT.__swift5_types: 0x808
   __TEXT.__swift_as_entry: 0x39c
   __TEXT.__swift_as_ret: 0x270
   __TEXT.__swift5_mpenum: 0x4c
   __TEXT.__swift5_protos: 0xc8
-  __TEXT.__unwind_info: 0x109b0
-  __TEXT.__eh_frame: 0x7b2c
-  __TEXT.__objc_classname: 0x2e40
-  __TEXT.__objc_methname: 0x43f44
-  __TEXT.__objc_methtype: 0xa85b
-  __TEXT.__objc_stubs: 0x25de0
-  __DATA_CONST.__got: 0x2488
-  __DATA_CONST.__const: 0x5ee8
-  __DATA_CONST.__objc_classlist: 0xec8
+  __TEXT.__unwind_info: 0x10ad0
+  __TEXT.__eh_frame: 0x7b64
+  __TEXT.__objc_classname: 0x2e8b
+  __TEXT.__objc_methname: 0x44504
+  __TEXT.__objc_methtype: 0xa8b7
+  __TEXT.__objc_stubs: 0x26020
+  __DATA_CONST.__got: 0x24c8
+  __DATA_CONST.__const: 0x5f40
+  __DATA_CONST.__objc_classlist: 0xee8
   __DATA_CONST.__objc_catlist: 0x178
-  __DATA_CONST.__objc_protolist: 0x6a8
+  __DATA_CONST.__objc_protolist: 0x6b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xed30
+  __DATA_CONST.__objc_selrefs: 0xee68
   __DATA_CONST.__objc_protorefs: 0x208
-  __DATA_CONST.__objc_superrefs: 0x758
+  __DATA_CONST.__objc_superrefs: 0x760
   __DATA_CONST.__objc_arraydata: 0x278
-  __AUTH_CONST.__auth_got: 0x2f08
-  __AUTH_CONST.__const: 0x1c908
-  __AUTH_CONST.__cfstring: 0x9b40
-  __AUTH_CONST.__objc_const: 0x354f0
-  __AUTH_CONST.__objc_intobj: 0x5a0
+  __AUTH_CONST.__auth_got: 0x2ff8
+  __AUTH_CONST.__const: 0x1c770
+  __AUTH_CONST.__cfstring: 0x9bc0
+  __AUTH_CONST.__objc_const: 0x35a50
+  __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_doubleobj: 0x130
   __AUTH_CONST.__objc_arrayobj: 0x210
-  __AUTH.__objc_data: 0xf708
-  __AUTH.__data: 0x7278
-  __DATA.__objc_ivar: 0x1aa0
-  __DATA.__data: 0xc240
+  __AUTH.__objc_data: 0xfab0
+  __AUTH.__data: 0x72e8
+  __DATA.__objc_ivar: 0x1ab4
+  __DATA.__data: 0xc340
   __DATA.__objc_stublist: 0x30
-  __DATA.__bss: 0x1b730
-  __DATA.__common: 0xd41
-  __DATA_DIRTY.__objc_data: 0x39b8
+  __DATA.__bss: 0x1b690
+  __DATA.__common: 0xd59
+  __DATA_DIRTY.__objc_data: 0x3a00
   __DATA_DIRTY.__data: 0x1608
   __DATA_DIRTY.__bss: 0xc0
   __DATA_DIRTY.__common: 0x268

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 225D120E-6051-35CA-8830-23740D3B7441
-  Functions: 23733
-  Symbols:   33816
-  CStrings:  16690
+  UUID: C8B74575-BE0F-302C-A686-FD2CC5D9C681
+  Functions: 23780
+  Symbols:   33773
+  CStrings:  16765
 
Symbols:
+ +[SFFeatureManager _searchEngineOnboardingCardDomainIsEligible]
+ +[SFFeatureManager shouldShowDefaultSearchEngineOnboardingCard]
+ +[SFOnboardingControllerProvider searchEngineOnboardingProviderForStartPageFromProviders:]
+ +[SFTestConsoleLogRecorder recordConsoleLogIfRunningTest:]
+ -[SFBrowsingDataDeletionRequest .cxx_destruct]
+ -[SFBrowsingDataDeletionRequest afterDate]
+ -[SFBrowsingDataDeletionRequest beforeDate]
+ -[SFBrowsingDataDeletionRequest clearAllProfiles]
+ -[SFBrowsingDataDeletionRequest clearDistractionControlSettings]
+ -[SFBrowsingDataDeletionRequest closeAllTabs]
+ -[SFBrowsingDataDeletionRequest profileIdentifier]
+ -[SFBrowsingDataDeletionRequest setAfterDate:]
+ -[SFBrowsingDataDeletionRequest setBeforeDate:]
+ -[SFBrowsingDataDeletionRequest setClearAllProfiles:]
+ -[SFBrowsingDataDeletionRequest setClearDistractionControlSettings:]
+ -[SFBrowsingDataDeletionRequest setCloseAllTabs:]
+ -[SFBrowsingDataDeletionRequest setProfileIdentifier:]
+ -[SFClearHistoryViewController _cellForAdditionalOptionsCloseAllTabsForIndexPath:]
+ -[SFExtensionsProfilesDataSource initWithTabGroupManager:shouldDiscoverExtensions:]
+ -[SFLinkHoverEvent initWithHitTestResult:forCurrentURL:modifierFlags:]
+ -[SFNavigationBarToggleButton initWithImage:forPersona:]
+ -[SFNavigationBarToggleButton initWithImage:forPersona:].cold.1
+ -[SFStartPageCollectionViewController _loadNextOnboardingItemIfNeeded]
+ -[SFStartPageCollectionViewController didDeferOnboardingItem:]
+ -[SFStartPageViewController beginDefaultSearchEngineOnboardingForStartPageCollectionViewController:completionHandler:]
+ -[SFTestConsoleLogRecorder .cxx_destruct]
+ -[SFTestConsoleLogRecorder initWithOutputPath:]
+ -[SFTestConsoleLogRecorder userContentController:didReceiveScriptMessage:]
+ -[SFUnifiedTabBarItemView _widthForPrioritizedAccessoryButtonsIfPresent]
+ -[SFUnifiedTabBarItemView setSquishTransformFactor:]
+ -[_SFNavigationIntent _initWithType:value:policy:richSearchSuggestionEntityIDURLParameter:]
+ -[_SFNavigationIntent richSearchSuggestionEntityIDURLParameter]
+ -[_SFNavigationIntentBuilder _initializeNavigationIntentWithType:value:richSearchSuggestionEntityIDURLParameter:]
+ -[_SFNavigationIntentBuilder navigationIntentWithSearchText:richSearchSuggestionEntityIDURLParameter:]
+ -[_SFTouchIconFetchOperation didFetchTouchIconURLs:fallbackTouchIconURLs:andFaviconURLs:fallbackFaviconURLs:forURL:]
+ GCC_except_table179
+ GCC_except_table183
+ GCC_except_table187
+ _OBJC_CLASS_$_SFBrowsingDataDeletionRequest
+ _OBJC_CLASS_$_SFSwipeToTabOverviewTipCoordinator
+ _OBJC_CLASS_$_SFTestConsoleLogRecorder
+ _OBJC_CLASS_$_WBSDeviceIdentifierManager
+ _OBJC_CLASS_$_WKUserScript
+ _OBJC_CLASS_$__TtC12MobileSafari18TabOverviewTipView
+ _OBJC_IVAR_$_SFBrowsingDataDeletionRequest._afterDate
+ _OBJC_IVAR_$_SFBrowsingDataDeletionRequest._beforeDate
+ _OBJC_IVAR_$_SFBrowsingDataDeletionRequest._clearAllProfiles
+ _OBJC_IVAR_$_SFBrowsingDataDeletionRequest._clearDistractionControlSettings
+ _OBJC_IVAR_$_SFBrowsingDataDeletionRequest._closeAllTabs
+ _OBJC_IVAR_$_SFBrowsingDataDeletionRequest._profileIdentifier
+ _OBJC_IVAR_$_SFExtensionsProfilesDataSource._shouldDiscoverExtensions
+ _OBJC_IVAR_$_SFNavigationBarToggleButton._persona
+ _OBJC_IVAR_$_SFTestConsoleLogRecorder._outputPath
+ _OBJC_IVAR_$__SFNavigationIntent._richSearchSuggestionEntityIDURLParameter
+ _OBJC_METACLASS_$_SFBrowsingDataDeletionRequest
+ _OBJC_METACLASS_$_SFSwipeToTabOverviewTipCoordinator
+ _OBJC_METACLASS_$_SFTestConsoleLogRecorder
+ _OBJC_METACLASS_$__TtC12MobileSafari18TabOverviewTipView
+ _SFDefaultBrowserPromptVersionKey
+ _SFDefaultBrowserSetUpLaterCountKey
+ _SFDefaultSearchEngineOnboardingCardDeferralCountKey
+ _SFDefaultSearchEngineOnboardingCardIsDeferredKey
+ _SFExtraBarSpacingAfterWindowControls
+ _SFSafariViewControllerUsesSoftPocketKey
+ _UIContentSizeCategorySmall
+ _UIFontTextStyleExtraLargeTitle
+ _WBSOSLogBanners
+ _WBSOSLogBookmarkSync
+ _WBSOSLogDownloads
+ _WBSOSLogExport
+ _WBSOSLogItemProvider
+ _WBSOSLogLoweredTabBar
+ _WBSOSLogMediaCapture
+ _WBSOSLogOther
+ _WBSOSLogPencilInput
+ _WBSOSLogProfiles
+ _WBSOSLogSiriReadThis
+ _WBSOSLogSiteMetadata
+ _WBSOSLogStartPage
+ _WBSOSLogStatePersistence
+ _WBSOSLogTabBar
+ _WBSOSLogTabDialogs
+ _WBSOSLogTabGroup
+ _WBSOSLogUserInterface
+ _WBSOSLogViewService
+ _WBSOSLogWebExtensions
+ _WBSOnboardingIdentifierSetDefaultSearchEngine
+ __CLASS_METHODS_SFSwipeToTabOverviewTipCoordinator
+ __CLASS_PROPERTIES_SFSwipeToTabOverviewTipCoordinator
+ __DATA_SFSwipeToTabOverviewTipCoordinator
+ __DATA__TtC12MobileSafari18TabOverviewTipView
+ __INSTANCE_METHODS_SFSwipeToTabOverviewTipCoordinator
+ __INSTANCE_METHODS__TtC12MobileSafari18TabOverviewTipView
+ __IVARS_SFSwipeToTabOverviewTipCoordinator
+ __IVARS__TtC12MobileSafari18TabOverviewTipView
+ __METACLASS_DATA_SFSwipeToTabOverviewTipCoordinator
+ __METACLASS_DATA__TtC12MobileSafari18TabOverviewTipView
+ __OBJC_$_CLASS_METHODS_SFTestConsoleLogRecorder
+ __OBJC_$_INSTANCE_METHODS_SFBrowsingDataDeletionRequest
+ __OBJC_$_INSTANCE_METHODS_SFTestConsoleLogRecorder
+ __OBJC_$_INSTANCE_VARIABLES_SFBrowsingDataDeletionRequest
+ __OBJC_$_INSTANCE_VARIABLES_SFTestConsoleLogRecorder
+ __OBJC_$_PROP_LIST_SFBrowsingDataDeletionRequest
+ __OBJC_$_PROP_LIST_SFTestConsoleLogRecorder
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__SFNavigationBarCommon
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WKScriptMessageHandler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WKScriptMessageHandler
+ __OBJC_$_PROTOCOL_REFS_WKScriptMessageHandler
+ __OBJC_CLASS_PROTOCOLS_$_SFTestConsoleLogRecorder
+ __OBJC_CLASS_RO_$_SFBrowsingDataDeletionRequest
+ __OBJC_CLASS_RO_$_SFTestConsoleLogRecorder
+ __OBJC_LABEL_PROTOCOL_$_WKScriptMessageHandler
+ __OBJC_METACLASS_RO_$_SFBrowsingDataDeletionRequest
+ __OBJC_METACLASS_RO_$_SFTestConsoleLogRecorder
+ __OBJC_PROTOCOL_$_WKScriptMessageHandler
+ __PROPERTIES_SFSwipeToTabOverviewTipCoordinator
+ __PROTOCOLS_SFStartPageOnboardingCellConfiguration.43
+ ___62-[SFStartPageCollectionViewController didStartOnboardingItem:]_block_invoke
+ ___62-[SFStartPageCollectionViewController didStartOnboardingItem:]_block_invoke_2
+ ___63+[SFFeatureManager _searchEngineOnboardingCardDomainIsEligible]_block_invoke
+ ___63+[SFFeatureManager _searchEngineOnboardingCardDomainIsEligible]_block_invoke_2
+ ___63+[SFFeatureManager _searchEngineOnboardingCardDomainIsEligible]_block_invoke_3
+ ___68-[SFStartPageViewController previewViewControllerForItemIdentifier:]_block_invoke.116
+ ___76+[SFDialog userMediaPermissionDialogWithHost:permissions:completionHandler:]_block_invoke
+ ___90+[SFOnboardingControllerProvider searchEngineOnboardingProviderForStartPageFromProviders:]_block_invoke
+ ___block_descriptor_113_e8_32s40s48r56r_e25_v32?0"NSNumber"8Q16^B24ls32l8r48l8r56l8s40l8
+ ___block_descriptor_32_e48_B16?0"SFStartPageOnboardingCellConfiguration"8l
+ ___block_literal_global.13
+ ___block_literal_global.65
+ ___swift_memcpy200_8
+ ___swift_memcpy208_8
+ ___swift_memcpy336_8
+ ___swift_memcpy416_8
+ __searchEngineOnboardingCardDomainIsEligible.isEligible
+ __searchEngineOnboardingCardDomainIsEligible.notifyToken
+ __searchEngineOnboardingCardDomainIsEligible.onceToken
+ __searchEngineOnboardingCardDomainIsEligible.queue
+ _block_copy_helper.109
+ _block_copy_helper.112
+ _block_copy_helper.187
+ _block_copy_helper.191
+ _block_copy_helper.194
+ _block_copy_helper.199
+ _block_copy_helper.209
+ _block_copy_helper.226
+ _block_copy_helper.230
+ _block_copy_helper.243
+ _block_copy_helper.261
+ _block_copy_helper.272
+ _block_copy_helper.274
+ _block_copy_helper.293
+ _block_copy_helper.300
+ _block_copy_helper.305
+ _block_copy_helper.306
+ _block_copy_helper.312
+ _block_copy_helper.331
+ _block_copy_helper.337
+ _block_copy_helper.345
+ _block_copy_helper.351
+ _block_copy_helper.358
+ _block_copy_helper.372
+ _block_copy_helper.378
+ _block_copy_helper.384
+ _block_copy_helper.394
+ _block_copy_helper.398
+ _block_copy_helper.406
+ _block_copy_helper.407
+ _block_copy_helper.409
+ _block_copy_helper.410
+ _block_copy_helper.422
+ _block_copy_helper.425
+ _block_copy_helper.426
+ _block_copy_helper.432
+ _block_copy_helper.435
+ _block_copy_helper.438
+ _block_copy_helper.448
+ _block_copy_helper.451
+ _block_copy_helper.455
+ _block_copy_helper.462
+ _block_copy_helper.464
+ _block_copy_helper.470
+ _block_copy_helper.471
+ _block_copy_helper.473
+ _block_copy_helper.478
+ _block_copy_helper.480
+ _block_copy_helper.483
+ _block_copy_helper.489
+ _block_copy_helper.497
+ _block_copy_helper.500
+ _block_copy_helper.506
+ _block_copy_helper.509
+ _block_copy_helper.513
+ _block_copy_helper.519
+ _block_copy_helper.522
+ _block_copy_helper.526
+ _block_copy_helper.529
+ _block_copy_helper.531
+ _block_copy_helper.538
+ _block_copy_helper.549
+ _block_copy_helper.563
+ _block_copy_helper.565
+ _block_copy_helper.568
+ _block_copy_helper.582
+ _block_copy_helper.594
+ _block_copy_helper.599
+ _block_copy_helper.611
+ _block_copy_helper.623
+ _block_copy_helper.637
+ _block_copy_helper.639
+ _block_copy_helper.657
+ _block_copy_helper.670
+ _block_copy_helper.672
+ _block_copy_helper.678
+ _block_copy_helper.687
+ _block_copy_helper.96
+ _block_copy_helper.99
+ _block_descriptor.101
+ _block_descriptor.111
+ _block_descriptor.114
+ _block_descriptor.189
+ _block_descriptor.193
+ _block_descriptor.196
+ _block_descriptor.201
+ _block_descriptor.211
+ _block_descriptor.228
+ _block_descriptor.232
+ _block_descriptor.245
+ _block_descriptor.263
+ _block_descriptor.274
+ _block_descriptor.276
+ _block_descriptor.295
+ _block_descriptor.302
+ _block_descriptor.307
+ _block_descriptor.308
+ _block_descriptor.314
+ _block_descriptor.333
+ _block_descriptor.339
+ _block_descriptor.347
+ _block_descriptor.353
+ _block_descriptor.360
+ _block_descriptor.374
+ _block_descriptor.380
+ _block_descriptor.386
+ _block_descriptor.396
+ _block_descriptor.400
+ _block_descriptor.408
+ _block_descriptor.409
+ _block_descriptor.411
+ _block_descriptor.412
+ _block_descriptor.424
+ _block_descriptor.427
+ _block_descriptor.428
+ _block_descriptor.434
+ _block_descriptor.437
+ _block_descriptor.440
+ _block_descriptor.450
+ _block_descriptor.453
+ _block_descriptor.457
+ _block_descriptor.464
+ _block_descriptor.466
+ _block_descriptor.472
+ _block_descriptor.473
+ _block_descriptor.475
+ _block_descriptor.480
+ _block_descriptor.482
+ _block_descriptor.485
+ _block_descriptor.491
+ _block_descriptor.499
+ _block_descriptor.502
+ _block_descriptor.508
+ _block_descriptor.511
+ _block_descriptor.515
+ _block_descriptor.521
+ _block_descriptor.524
+ _block_descriptor.528
+ _block_descriptor.531
+ _block_descriptor.533
+ _block_descriptor.540
+ _block_descriptor.551
+ _block_descriptor.565
+ _block_descriptor.567
+ _block_descriptor.570
+ _block_descriptor.584
+ _block_descriptor.596
+ _block_descriptor.601
+ _block_descriptor.613
+ _block_descriptor.625
+ _block_descriptor.639
+ _block_descriptor.641
+ _block_descriptor.659
+ _block_descriptor.672
+ _block_descriptor.674
+ _block_descriptor.680
+ _block_descriptor.689
+ _block_descriptor.98
+ _block_destroy_helper.100
+ _block_destroy_helper.110
+ _block_destroy_helper.113
+ _block_destroy_helper.188
+ _block_destroy_helper.192
+ _block_destroy_helper.195
+ _block_destroy_helper.200
+ _block_destroy_helper.210
+ _block_destroy_helper.227
+ _block_destroy_helper.231
+ _block_destroy_helper.244
+ _block_destroy_helper.262
+ _block_destroy_helper.273
+ _block_destroy_helper.275
+ _block_destroy_helper.294
+ _block_destroy_helper.301
+ _block_destroy_helper.306
+ _block_destroy_helper.307
+ _block_destroy_helper.313
+ _block_destroy_helper.332
+ _block_destroy_helper.338
+ _block_destroy_helper.346
+ _block_destroy_helper.352
+ _block_destroy_helper.359
+ _block_destroy_helper.373
+ _block_destroy_helper.379
+ _block_destroy_helper.385
+ _block_destroy_helper.395
+ _block_destroy_helper.399
+ _block_destroy_helper.407
+ _block_destroy_helper.408
+ _block_destroy_helper.410
+ _block_destroy_helper.411
+ _block_destroy_helper.423
+ _block_destroy_helper.426
+ _block_destroy_helper.427
+ _block_destroy_helper.433
+ _block_destroy_helper.436
+ _block_destroy_helper.439
+ _block_destroy_helper.449
+ _block_destroy_helper.452
+ _block_destroy_helper.456
+ _block_destroy_helper.463
+ _block_destroy_helper.465
+ _block_destroy_helper.471
+ _block_destroy_helper.472
+ _block_destroy_helper.474
+ _block_destroy_helper.479
+ _block_destroy_helper.481
+ _block_destroy_helper.484
+ _block_destroy_helper.490
+ _block_destroy_helper.498
+ _block_destroy_helper.501
+ _block_destroy_helper.507
+ _block_destroy_helper.510
+ _block_destroy_helper.514
+ _block_destroy_helper.520
+ _block_destroy_helper.523
+ _block_destroy_helper.527
+ _block_destroy_helper.530
+ _block_destroy_helper.532
+ _block_destroy_helper.539
+ _block_destroy_helper.550
+ _block_destroy_helper.564
+ _block_destroy_helper.566
+ _block_destroy_helper.569
+ _block_destroy_helper.583
+ _block_destroy_helper.595
+ _block_destroy_helper.600
+ _block_destroy_helper.612
+ _block_destroy_helper.624
+ _block_destroy_helper.638
+ _block_destroy_helper.640
+ _block_destroy_helper.658
+ _block_destroy_helper.671
+ _block_destroy_helper.673
+ _block_destroy_helper.679
+ _block_destroy_helper.688
+ _block_destroy_helper.97
+ _get_witness_table 10Foundation19AttributedStringKeyRzlAA15AttributeScopesO5UIKitE0G10AttributesV015ForegroundColorE0OAaBHPyHC.270
+ _get_witness_table 10Foundation19AttributedStringKeyRzlAA15AttributeScopesO5UIKitE0G10AttributesV04FontE0OAaBHPyHC.264
+ _notify_register_dispatch
+ _objc_msgSend$_cellForAdditionalOptionsCloseAllTabsForIndexPath:
+ _objc_msgSend$_initWithType:value:policy:richSearchSuggestionEntityIDURLParameter:
+ _objc_msgSend$_initializeNavigationIntentWithType:value:richSearchSuggestionEntityIDURLParameter:
+ _objc_msgSend$_loadNextOnboardingItemIfNeeded
+ _objc_msgSend$_searchEngineOnboardingCardDomainIsEligible
+ _objc_msgSend$_widthForPrioritizedAccessoryButtonsIfPresent
+ _objc_msgSend$absoluteLinkURL
+ _objc_msgSend$addScriptMessageHandler:name:
+ _objc_msgSend$addUserScript:
+ _objc_msgSend$beginDefaultSearchEngineOnboardingForStartPageCollectionViewController:completionHandler:
+ _objc_msgSend$beginDefaultSearchEngineOnboardingForStartPageViewController:completionHandler:
+ _objc_msgSend$body
+ _objc_msgSend$clearDeviceIdentifier
+ _objc_msgSend$clearHistoryViewController:clearDataWithRequest:
+ _objc_msgSend$closeAndReturnError:
+ _objc_msgSend$deviceIdentifier
+ _objc_msgSend$didDefer:
+ _objc_msgSend$hideSelectedElementAnimated:
+ _objc_msgSend$initWithImage:forPersona:
+ _objc_msgSend$initWithKey:readOnly:
+ _objc_msgSend$initWithOutputPath:
+ _objc_msgSend$initWithSource:injectionTime:forMainFrameOnly:
+ _objc_msgSend$linkHasTargetFrame
+ _objc_msgSend$linkTargetFrameIsSameAsLinkFrame
+ _objc_msgSend$migrateFromPlistAtURLIfNeeded:
+ _objc_msgSend$recordConsoleLogIfRunningTest:
+ _objc_msgSend$seekToEndReturningOffset:error:
+ _objc_msgSend$setAfterDate:
+ _objc_msgSend$setBeforeDate:
+ _objc_msgSend$setClearAllProfiles:
+ _objc_msgSend$setClearDistractionControlSettings:
+ _objc_msgSend$setCloseAllTabs:
+ _objc_msgSend$setProfileIdentifier:
+ _objc_msgSend$shouldMigrateDeviceIdentifier
+ _objc_msgSend$userContentController
+ _objc_msgSend$writeData:error:
+ _objectdestroy.212Tm
+ _objectdestroy.247Tm
+ _objectdestroy.270Tm
+ _objectdestroy.276Tm
+ _objectdestroy.298Tm
+ _objectdestroy.300Tm
+ _objectdestroy.334Tm
+ _objectdestroy.343Tm
+ _objectdestroy.349Tm
+ _objectdestroy.380Tm
+ _objectdestroy.402Tm
+ _objectdestroy.405Tm
+ _objectdestroy.411Tm
+ _objectdestroy.457Tm
+ _objectdestroy.576Tm
+ _os_eligibility_get_domain_answer
+ _recordConsoleLogIfRunningTest:.controllersWithMessageHandler
+ _symbolic So6UIViewCyc
+ _symbolic _____ 12MobileSafari18TabOverviewTipViewC
+ _symbolic _____ 12MobileSafari18TabOverviewTipViewC7MetricsV
+ _symbolic _____8folderId_Sb17isSyntheticFoldert So10BookmarkIDa
+ _symbolic _____Sg So6UIViewC5UIKitE12LayoutRegionV14AdaptivityAxisO
+ _type_layout_string 12MobileSafari18TabOverviewTipViewC7MetricsV
- -[SFCapsuleCollectionView _didReceivePan:].cold.1
- -[SFLinkHoverEvent initWithHoveredLinkURL:forCurrentURL:modifierFlags:frame:targetFrame:]
- -[SFNavigationBarItem setTemporarilySuppressText:]
- -[SFNavigationBarToggleButton initWithImage:forInputMode:]
- -[SFNavigationBarToggleButton initWithImage:forInputMode:].cold.1
- -[SFStartPageCollectionViewController _didCompleteOnboardingItem:wasClosed:]
- -[SFUnifiedTabBarItem menuButtonConfigurator]
- -[SFUnifiedTabBarItem setMenuButtonConfigurator:]
- -[SFUnifiedTabBarItemView formatMenuButtonConfigurator]
- -[SFUnifiedTabBarItemView setFormatMenuButtonConfigurator:]
- -[SFVoiceSearchManager _kfed]
- -[SFVoiceSearchManager liveCompletionList]
- -[SFVoiceSearchManager queryItems]
- -[_SFNavigationIntentBuilder navigationIntentWithSearchText:]
- -[_SFSiteIconView setUpdateObserver:]
- -[_SFSiteIconView updateObserver]
- -[_SFTouchIconFetchOperation didFetchTouchIconURLs:andFaviconURLs:forURL:]
- GCC_except_table178
- GCC_except_table182
- GCC_except_table395
- GCC_except_table93
- _CGPointMake
- _CGRectMake
- _OBJC_CLASS_$_NSURLQueryItem
- _OBJC_CLASS_$_WBSPerformImageOperationUsingWebViewProvider
- _OBJC_IVAR_$_SFNavigationBarItem._temporarilySuppressText
- _OBJC_IVAR_$_SFNavigationBarToggleButton._inputMode
- _OBJC_IVAR_$_SFUnifiedTabBarItem._menuButtonConfigurator
- _OBJC_IVAR_$_SFUnifiedTabBarItemView._formatMenuButtonConfigurator
- _OBJC_IVAR_$__SFSiteIconView._updateObserver
- _SFVoiceSearchKfedKey
- _SFVoiceSearchLiveCompletionListKey
- _WBS_LOG_CHANNEL_PREFIXBanners
- _WBS_LOG_CHANNEL_PREFIXBanners.cold.1
- _WBS_LOG_CHANNEL_PREFIXBanners.log
- _WBS_LOG_CHANNEL_PREFIXBanners.onceToken
- _WBS_LOG_CHANNEL_PREFIXBookmarkSync
- _WBS_LOG_CHANNEL_PREFIXBookmarkSync.cold.1
- _WBS_LOG_CHANNEL_PREFIXBookmarkSync.log
- _WBS_LOG_CHANNEL_PREFIXBookmarkSync.onceToken
- _WBS_LOG_CHANNEL_PREFIXDownloads
- _WBS_LOG_CHANNEL_PREFIXDownloads.cold.1
- _WBS_LOG_CHANNEL_PREFIXDownloads.log
- _WBS_LOG_CHANNEL_PREFIXDownloads.onceToken
- _WBS_LOG_CHANNEL_PREFIXExport
- _WBS_LOG_CHANNEL_PREFIXExport.cold.1
- _WBS_LOG_CHANNEL_PREFIXExport.log
- _WBS_LOG_CHANNEL_PREFIXExport.onceToken
- _WBS_LOG_CHANNEL_PREFIXItemProvider
- _WBS_LOG_CHANNEL_PREFIXItemProvider.cold.1
- _WBS_LOG_CHANNEL_PREFIXItemProvider.log
- _WBS_LOG_CHANNEL_PREFIXItemProvider.onceToken
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
- _WBS_LOG_CHANNEL_PREFIXPencilInput
- _WBS_LOG_CHANNEL_PREFIXPencilInput.cold.1
- _WBS_LOG_CHANNEL_PREFIXPencilInput.log
- _WBS_LOG_CHANNEL_PREFIXPencilInput.onceToken
- _WBS_LOG_CHANNEL_PREFIXProfiles
- _WBS_LOG_CHANNEL_PREFIXProfiles.cold.1
- _WBS_LOG_CHANNEL_PREFIXProfiles.log
- _WBS_LOG_CHANNEL_PREFIXProfiles.onceToken
- _WBS_LOG_CHANNEL_PREFIXSiriReadThis
- _WBS_LOG_CHANNEL_PREFIXSiriReadThis.cold.1
- _WBS_LOG_CHANNEL_PREFIXSiriReadThis.log
- _WBS_LOG_CHANNEL_PREFIXSiriReadThis.onceToken
- _WBS_LOG_CHANNEL_PREFIXSiteMetadata
- _WBS_LOG_CHANNEL_PREFIXSiteMetadata.cold.1
- _WBS_LOG_CHANNEL_PREFIXSiteMetadata.log
- _WBS_LOG_CHANNEL_PREFIXSiteMetadata.onceToken
- _WBS_LOG_CHANNEL_PREFIXStartPage
- _WBS_LOG_CHANNEL_PREFIXStartPage.cold.1
- _WBS_LOG_CHANNEL_PREFIXStartPage.log
- _WBS_LOG_CHANNEL_PREFIXStartPage.onceToken
- _WBS_LOG_CHANNEL_PREFIXStatePersistence
- _WBS_LOG_CHANNEL_PREFIXStatePersistence.cold.1
- _WBS_LOG_CHANNEL_PREFIXStatePersistence.log
- _WBS_LOG_CHANNEL_PREFIXStatePersistence.onceToken
- _WBS_LOG_CHANNEL_PREFIXTabBar
- _WBS_LOG_CHANNEL_PREFIXTabBar.cold.1
- _WBS_LOG_CHANNEL_PREFIXTabBar.log
- _WBS_LOG_CHANNEL_PREFIXTabBar.onceToken
- _WBS_LOG_CHANNEL_PREFIXTabDialogs
- _WBS_LOG_CHANNEL_PREFIXTabDialogs.cold.1
- _WBS_LOG_CHANNEL_PREFIXTabDialogs.log
- _WBS_LOG_CHANNEL_PREFIXTabDialogs.onceToken
- _WBS_LOG_CHANNEL_PREFIXTabGroup
- _WBS_LOG_CHANNEL_PREFIXTabGroup.cold.1
- _WBS_LOG_CHANNEL_PREFIXTabGroup.log
- _WBS_LOG_CHANNEL_PREFIXTabGroup.onceToken
- _WBS_LOG_CHANNEL_PREFIXUserInterface
- _WBS_LOG_CHANNEL_PREFIXUserInterface.cold.1
- _WBS_LOG_CHANNEL_PREFIXUserInterface.log
- _WBS_LOG_CHANNEL_PREFIXUserInterface.onceToken
- _WBS_LOG_CHANNEL_PREFIXViewService
- _WBS_LOG_CHANNEL_PREFIXViewService.cold.1
- _WBS_LOG_CHANNEL_PREFIXViewService.log
- _WBS_LOG_CHANNEL_PREFIXViewService.onceToken
- _WBS_LOG_CHANNEL_PREFIXWebExtensions
- _WBS_LOG_CHANNEL_PREFIXWebExtensions.cold.1
- _WBS_LOG_CHANNEL_PREFIXWebExtensions.log
- _WBS_LOG_CHANNEL_PREFIXWebExtensions.onceToken
- __PROTOCOLS_SFStartPageOnboardingCellConfiguration.36
- ___60-[_SFSiteIconView _updateSiteIconViewWithTouchIconResponse:]_block_invoke
- ___68-[SFStartPageViewController previewViewControllerForItemIdentifier:]_block_invoke.114
- ___85-[_SFSiteIconView updateSiteIconViewWithLinkMetadata:requiredImageSize:fallbackIcon:]_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXBanners_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXBookmarkSync_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXDownloads_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXExport_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXItemProvider_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXLoweredTabBar_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXMediaCapture_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXOther_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXPencilInput_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXProfiles_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXSiriReadThis_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXSiteMetadata_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXStartPage_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXStatePersistence_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXTabBar_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXTabDialogs_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXTabGroup_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXUserInterface_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXViewService_block_invoke
- ___WBS_LOG_CHANNEL_PREFIXWebExtensions_block_invoke
- ___block_descriptor_121_e8_32s40s48r56r_e25_v32?0"NSNumber"8Q16^B24ls32l8r48l8r56l8s40l8
- ___block_literal_global.16
- ___block_literal_global.19
- ___block_literal_global.28
- ___block_literal_global.43
- ___block_literal_global.49
- ___block_literal_global.52
- ___block_literal_global.61
- ___block_literal_global.76
- ___block_literal_global.82
- ___block_literal_global.84
- ___swift_memcpy192_8
- ___swift_memcpy216_8
- ___swift_memcpy320_8
- ___swift_memcpy400_8
- _block_copy_helper.180
- _block_copy_helper.181
- _block_copy_helper.189
- _block_copy_helper.192
- _block_copy_helper.207
- _block_copy_helper.223
- _block_copy_helper.240
- _block_copy_helper.254
- _block_copy_helper.258
- _block_copy_helper.270
- _block_copy_helper.287
- _block_copy_helper.299
- _block_copy_helper.309
- _block_copy_helper.311
- _block_copy_helper.313
- _block_copy_helper.321
- _block_copy_helper.328
- _block_copy_helper.334
- _block_copy_helper.340
- _block_copy_helper.348
- _block_copy_helper.349
- _block_copy_helper.354
- _block_copy_helper.355
- _block_copy_helper.367
- _block_copy_helper.368
- _block_copy_helper.382
- _block_copy_helper.402
- _block_copy_helper.405
- _block_copy_helper.414
- _block_copy_helper.416
- _block_copy_helper.421
- _block_copy_helper.427
- _block_copy_helper.431
- _block_copy_helper.434
- _block_copy_helper.444
- _block_copy_helper.447
- _block_copy_helper.457
- _block_copy_helper.460
- _block_copy_helper.469
- _block_copy_helper.472
- _block_copy_helper.474
- _block_copy_helper.479
- _block_copy_helper.487
- _block_copy_helper.492
- _block_copy_helper.493
- _block_copy_helper.504
- _block_copy_helper.505
- _block_copy_helper.507
- _block_copy_helper.517
- _block_copy_helper.518
- _block_copy_helper.520
- _block_copy_helper.527
- _block_copy_helper.530
- _block_copy_helper.541
- _block_copy_helper.547
- _block_copy_helper.557
- _block_copy_helper.559
- _block_copy_helper.560
- _block_copy_helper.574
- _block_copy_helper.586
- _block_copy_helper.595
- _block_copy_helper.603
- _block_copy_helper.619
- _block_copy_helper.631
- _block_copy_helper.633
- _block_copy_helper.645
- _block_copy_helper.664
- _block_copy_helper.666
- _block_copy_helper.674
- _block_copy_helper.683
- _block_copy_helper.92
- _block_descriptor.182
- _block_descriptor.183
- _block_descriptor.191
- _block_descriptor.194
- _block_descriptor.209
- _block_descriptor.225
- _block_descriptor.242
- _block_descriptor.256
- _block_descriptor.260
- _block_descriptor.272
- _block_descriptor.289
- _block_descriptor.301
- _block_descriptor.311
- _block_descriptor.313
- _block_descriptor.315
- _block_descriptor.323
- _block_descriptor.330
- _block_descriptor.336
- _block_descriptor.342
- _block_descriptor.350
- _block_descriptor.351
- _block_descriptor.356
- _block_descriptor.357
- _block_descriptor.369
- _block_descriptor.370
- _block_descriptor.384
- _block_descriptor.404
- _block_descriptor.407
- _block_descriptor.416
- _block_descriptor.418
- _block_descriptor.423
- _block_descriptor.429
- _block_descriptor.433
- _block_descriptor.436
- _block_descriptor.446
- _block_descriptor.449
- _block_descriptor.459
- _block_descriptor.462
- _block_descriptor.471
- _block_descriptor.474
- _block_descriptor.476
- _block_descriptor.481
- _block_descriptor.489
- _block_descriptor.494
- _block_descriptor.495
- _block_descriptor.506
- _block_descriptor.507
- _block_descriptor.509
- _block_descriptor.519
- _block_descriptor.520
- _block_descriptor.522
- _block_descriptor.529
- _block_descriptor.532
- _block_descriptor.543
- _block_descriptor.549
- _block_descriptor.559
- _block_descriptor.561
- _block_descriptor.562
- _block_descriptor.576
- _block_descriptor.588
- _block_descriptor.597
- _block_descriptor.605
- _block_descriptor.621
- _block_descriptor.633
- _block_descriptor.635
- _block_descriptor.647
- _block_descriptor.666
- _block_descriptor.668
- _block_descriptor.676
- _block_descriptor.685
- _block_descriptor.94
- _block_destroy_helper.181
- _block_destroy_helper.182
- _block_destroy_helper.190
- _block_destroy_helper.193
- _block_destroy_helper.208
- _block_destroy_helper.224
- _block_destroy_helper.241
- _block_destroy_helper.255
- _block_destroy_helper.259
- _block_destroy_helper.271
- _block_destroy_helper.288
- _block_destroy_helper.300
- _block_destroy_helper.310
- _block_destroy_helper.312
- _block_destroy_helper.314
- _block_destroy_helper.322
- _block_destroy_helper.329
- _block_destroy_helper.335
- _block_destroy_helper.341
- _block_destroy_helper.349
- _block_destroy_helper.350
- _block_destroy_helper.355
- _block_destroy_helper.356
- _block_destroy_helper.368
- _block_destroy_helper.369
- _block_destroy_helper.383
- _block_destroy_helper.403
- _block_destroy_helper.406
- _block_destroy_helper.415
- _block_destroy_helper.417
- _block_destroy_helper.422
- _block_destroy_helper.428
- _block_destroy_helper.432
- _block_destroy_helper.435
- _block_destroy_helper.445
- _block_destroy_helper.448
- _block_destroy_helper.458
- _block_destroy_helper.461
- _block_destroy_helper.470
- _block_destroy_helper.473
- _block_destroy_helper.475
- _block_destroy_helper.480
- _block_destroy_helper.488
- _block_destroy_helper.493
- _block_destroy_helper.494
- _block_destroy_helper.505
- _block_destroy_helper.506
- _block_destroy_helper.508
- _block_destroy_helper.518
- _block_destroy_helper.519
- _block_destroy_helper.521
- _block_destroy_helper.528
- _block_destroy_helper.531
- _block_destroy_helper.542
- _block_destroy_helper.548
- _block_destroy_helper.558
- _block_destroy_helper.560
- _block_destroy_helper.561
- _block_destroy_helper.575
- _block_destroy_helper.587
- _block_destroy_helper.596
- _block_destroy_helper.604
- _block_destroy_helper.620
- _block_destroy_helper.632
- _block_destroy_helper.634
- _block_destroy_helper.646
- _block_destroy_helper.665
- _block_destroy_helper.667
- _block_destroy_helper.675
- _block_destroy_helper.684
- _block_destroy_helper.93
- _get_witness_table 10Foundation19AttributedStringKeyRzlAA15AttributeScopesO5UIKitE0G10AttributesV015ForegroundColorE0OAaBHPyHC.267
- _get_witness_table 10Foundation19AttributedStringKeyRzlAA15AttributeScopesO5UIKitE0G10AttributesV04FontE0OAaBHPyHC.261
- _objc_msgSend$_didCompleteOnboardingItem:wasClosed:
- _objc_msgSend$_kfed
- _objc_msgSend$clearHistoryViewController:clearHistoryVisitsAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeAllTabs:
- _objc_msgSend$configureMenuAndAdoptButton:
- _objc_msgSend$dictionaryWithContentsOfFile:
- _objc_msgSend$frameID
- _objc_msgSend$hideSelectedElement
- _objc_msgSend$initWithImage:forInputMode:
- _objc_msgSend$initWithName:value:
- _objc_msgSend$isAppleAccountBrandingEnabled
- _objc_msgSend$isSafariProfilesEnabled
- _objc_msgSend$isScribbleEnabled
- _objc_msgSend$menuButtonConfigurator
- _objc_msgSend$queryItemWithName:value:
- _objc_msgSend$setFormatMenuButtonConfigurator:
- _objc_msgSend$setTemporarilySuppressText:
- _objc_msgSend$siteIconViewDidUpdate:
- _objc_msgSend$writeToFile:atomically:
- _objectdestroy.209Tm
- _objectdestroy.244Tm
- _objectdestroy.268Tm
- _objectdestroy.274Tm
- _objectdestroy.296Tm
- _objectdestroy.297Tm
- _objectdestroy.332Tm
- _objectdestroy.341Tm
- _objectdestroy.353Tm
- _objectdestroy.376Tm
- _objectdestroy.406Tm
- _objectdestroy.409Tm
- _objectdestroy.455Tm
- _objectdestroy.572Tm
- _objectdestroy.87Tm
- _os_log_create
- _symbolic _____8folderId_t So10BookmarkIDa
CStrings:
+ "$__lazy_storage_$_constraintForDodgingWindowControls"
+ "$__lazy_storage_$_deferButton"
+ "$__lazy_storage_$_doneButtonHeightConstraint"
+ "$__lazy_storage_$_tipView"
+ "%@\n"
+ "%@Content-%@"
+ "26_2"
+ "@40@0:8Q16@24@32"
+ "@48@0:8Q16@24q32@40"
+ "About Your Default Search Engine"
+ "B16@?0@\"SFStartPageOnboardingCellConfiguration\"8"
+ "BrowsingSessionHeaderCell"
+ "Choose Search Engine"
+ "DefaultSearchEngineOnboardingCardDeferralCount"
+ "DefaultSearchEngineOnboardingCardIsDeferred"
+ "Defer Onboarding Card Button (Default Search Engine)"
+ "DeviceUtilitiesUUID"
+ "JavaScriptConsoleOutputPath"
+ "MobileSafari/TabOverviewTipView.swift"
+ "Next selected item index after pan %zd is beyond bounds of %lu items (%lu total)."
+ "Onboarding Button (Default Search Engine)"
+ "Onboarding Text (Default Search Engine)"
+ "PrivacyReportLabel"
+ "Quickly Access All Tabs"
+ "SFBrowsingDataDeletionRequest"
+ "SFDefaultBrowserPromptVersion"
+ "SFDefaultBrowserSetUpLaterCount"
+ "SFDidDismissSwipeToTabOverviewTip"
+ "SFSwipeToTabOverviewTipCoordinator"
+ "SFSwipeToTabOverviewTipCoordinatorDidUpdateShouldShow"
+ "SFTestConsoleLogRecorder"
+ "SafariOnboardingSearchEngineChoice"
+ "SafariViewControllerUsesSoftPocket"
+ "Search (onboarding card image)"
+ "T@\"NSDate\",&,N,V_afterDate"
+ "T@\"NSDate\",&,N,V_beforeDate"
+ "T@\"NSString\",R,N,V_richSearchSuggestionEntityIDURLParameter"
+ "T@\"SFSwipeToTabOverviewTipCoordinator\",N,R"
+ "T@\"UITextField\",?,R,N"
+ "TB,N,V_clearAllProfiles"
+ "TB,N,V_clearDistractionControlSettings"
+ "TB,N,V_closeAllTabs"
+ "WKScriptMessageHandler"
+ "While viewing a web page, you can swipe up from the search field to quickly view all open tabs."
+ "With iOS, you have a choice in your default search engine. You can change it any time in Settings."
+ "_TtC12MobileSafari18TabOverviewTipView"
+ "_afterDate"
+ "_beforeDate"
+ "_bridgedUpdateContentUnavailableConfigurationUsingState:"
+ "_cellForAdditionalOptionsCloseAllTabsForIndexPath:"
+ "_clearAllProfiles"
+ "_clearDistractionControlSettings"
+ "_closeAllTabs"
+ "_initWithType:value:policy:richSearchSuggestionEntityIDURLParameter:"
+ "_initializeNavigationIntentWithType:value:richSearchSuggestionEntityIDURLParameter:"
+ "_loadNextOnboardingItemIfNeeded"
+ "_outputPath"
+ "_richSearchSuggestionEntityIDURLParameter"
+ "_searchEngineOnboardingCardDomainIsEligible"
+ "_shouldDiscoverExtensions"
+ "_widthForPrioritizedAccessoryButtonsIfPresent"
+ "absoluteLinkURL"
+ "addScriptMessageHandler:name:"
+ "addUserScript:"
+ "afterDate"
+ "alwaysHideCloseButton"
+ "beforeDate"
+ "beginDefaultSearchEngineOnboardingForStartPageCollectionViewController:completionHandler:"
+ "beginDefaultSearchEngineOnboardingForStartPageViewController:completionHandler:"
+ "body"
+ "clearAllProfiles"
+ "clearDeviceIdentifier"
+ "clearDistractionControlSettings"
+ "clearHistoryViewController:clearDataWithRequest:"
+ "closeAllTabs"
+ "closeAndReturnError:"
+ "com.apple.Safari.ErbiumEligibilityObserver"
+ "com.apple.os-eligibility-domain.change.erbium"
+ "console.log = message => window.webkit.messageHandlers.consoleLogRecorder.postMessage(message)"
+ "consoleLogRecorder"
+ "contentUnavailableConfigurationToDisplay"
+ "contextMenuIsVisible"
+ "deferButtonTitle"
+ "deviceIdentifier"
+ "didDefer:"
+ "didDeferOnboardingItem:"
+ "didDismissTip"
+ "didEnterTabOverviewFromMoreMenu"
+ "didEnterTabOverviewFromSwipeGesture"
+ "didFetchTouchIconURLs:fallbackTouchIconURLs:andFaviconURLs:fallbackFaviconURLs:forURL:"
+ "didTapDeferButton"
+ "didUpdateShouldShowNotification"
+ "grayColor"
+ "hasAnyBackgroundImage"
+ "hideSelectedElementAnimated:"
+ "initWithHitTestResult:forCurrentURL:modifierFlags:"
+ "initWithImage:forPersona:"
+ "initWithKey:readOnly:"
+ "initWithOutputPath:"
+ "initWithSource:injectionTime:forMainFrameOnly:"
+ "initWithTabGroupManager:shouldDiscoverExtensions:"
+ "insetForWindowControls"
+ "linkHasTargetFrame"
+ "linkTargetFrameIsSameAsLinkFrame"
+ "migrateFromPlistAtURLIfNeeded:"
+ "navigationIntentWithSearchText:richSearchSuggestionEntityIDURLParameter:"
+ "onboardingButton-"
+ "originPage"
+ "readyToShowTip"
+ "recordConsoleLogIfRunningTest:"
+ "reduceTransparencyStatusDidChange"
+ "richSearchSuggestionEntityIDURLParameter"
+ "searchEngineOnboardingProviderForStartPage"
+ "searchEngineOnboardingProviderForStartPageFromProviders:"
+ "seekToEndReturningOffset:error:"
+ "setAfterDate:"
+ "setBackButtonDisplayMode:"
+ "setBackButtonTitle:"
+ "setBeforeDate:"
+ "setClearAllProfiles:"
+ "setClearDistractionControlSettings:"
+ "setCloseAllTabs:"
+ "setNeedsUpdateContentUnavailableConfiguration"
+ "setShowsSwipeToTabOverviewTip:"
+ "shouldMigrateDeviceIdentifier"
+ "shouldShowDefaultSearchEngineOnboardingCard"
+ "shouldShowTip"
+ "showsSwipeToTabOverviewTip"
+ "suppressTipDefaultsKey"
+ "userContentController"
+ "userContentController:didReceiveScriptMessage:"
+ "v32@0:8@\"SFStartPageCollectionViewController\"16@?<v@?>24"
+ "v32@0:8@\"WKUserContentController\"16@\"WKScriptMessage\"24"
+ "v56@0:8@16@24@32@40@48"
+ "writeData:error:"
+ "\xc1"
+ "\xf0\xe1\x81Q"
- "26_1"
- "@\"<SFMenuConfiguring>\""
- "@\"<_SFSiteIconViewUpdateObserver>\""
- "@56@0:8@16@24q32@40@48"
- "Banners"
- "BookmarkSync"
- "DeviceUUID"
- "Downloads"
- "Export"
- "ItemProvider"
- "LiveCompletionList"
- "LoweredTabBar"
- "MediaCapture"
- "Next selected item index after pan %zd is beyond bounds of array of %lu items"
- "Other"
- "PencilInput"
- "Please update your Apple ID to share a Tab Group."
- "Profiles"
- "SiriReadThis"
- "SiteMetadata"
- "StartPage"
- "StatePersistence"
- "T@\"<SFMenuConfiguring>\",W,N,V_formatMenuButtonConfigurator"
- "T@\"<SFMenuConfiguring>\",W,N,V_menuButtonConfigurator"
- "T@\"<_SFSiteIconViewUpdateObserver>\",W,N,V_updateObserver"
- "T@\"UITextField\",R,N"
- "TabBar"
- "TabDialogs"
- "TabGroup"
- "Update Apple ID Settings"
- "UserInterface"
- "ViewService"
- "VoiceSearchKfed"
- "WebExtensions"
- "_didCompleteOnboardingItem:wasClosed:"
- "_formatMenuButtonConfigurator"
- "_inputMode"
- "_kfed"
- "_menuButtonConfigurator"
- "_temporarilySuppressText"
- "_updateObserver"
- "cancelButton"
- "clearHistoryViewController:clearHistoryVisitsAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeAllTabs:"
- "configureMenuAndAdoptButton:"
- "dictionaryWithContentsOfFile:"
- "didFetchTouchIconURLs:andFaviconURLs:forURL:"
- "explanationView"
- "formatMenuButtonConfigurator"
- "frameID"
- "hideSelectedElement"
- "initWithHoveredLinkURL:forCurrentURL:modifierFlags:frame:targetFrame:"
- "initWithImage:forInputMode:"
- "initWithName:value:"
- "isAppleAccountBrandingEnabled"
- "isSafariProfilesEnabled"
- "isScribbleEnabled"
- "kfed-service"
- "liveCompletionList"
- "menuButtonConfigurator"
- "navigationIntentWithSearchText:"
- "qtype"
- "queryItemWithName:value:"
- "queryItems"
- "setFormatMenuButtonConfigurator:"
- "setMenuButtonConfigurator:"
- "setTemporarilySuppressText:"
- "setUpdateObserver:"
- "siteIconViewDidUpdate:"
- "updateObserver"
- "voice_search"
- "writeToFile:atomically:"
- "\xd1"
- "\xf1"

```
