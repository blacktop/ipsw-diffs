## MobileSafariUI

> `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-616.1.27.10.16
-  __TEXT.__text: 0x1d77bc
-  __TEXT.__auth_stubs: 0x1a90
-  __TEXT.__objc_methlist: 0x176b8
-  __TEXT.__const: 0x6a8
-  __TEXT.__gcc_except_tab: 0x16fe0
-  __TEXT.__cstring: 0xb85e
+616.2.9.10.10
+  __TEXT.__text: 0x1d8bc4
+  __TEXT.__auth_stubs: 0x1aa0
+  __TEXT.__objc_methlist: 0x177b8
+  __TEXT.__const: 0x6c8
+  __TEXT.__gcc_except_tab: 0x17044
+  __TEXT.__cstring: 0xb872
   __TEXT.__dlopen_cstrs: 0x7a6
-  __TEXT.__oslogstring: 0x79f5
+  __TEXT.__oslogstring: 0x7a1a
   __TEXT.__ustring: 0x10e4
-  __TEXT.__unwind_info: 0xb5a8
+  __TEXT.__unwind_info: 0xb60c
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x41d7
-  __TEXT.__objc_methname: 0x6286d
-  __TEXT.__objc_methtype: 0x13b9e
-  __TEXT.__objc_stubs: 0x40e60
+  __TEXT.__objc_classname: 0x41fc
+  __TEXT.__objc_methname: 0x62c39
+  __TEXT.__objc_methtype: 0x13cb7
+  __TEXT.__objc_stubs: 0x41060
   __DATA_CONST.__got: 0xe90
-  __DATA_CONST.__const: 0x79f8
-  __DATA_CONST.__objc_classlist: 0x980
+  __DATA_CONST.__const: 0x7a70
+  __DATA_CONST.__objc_classlist: 0x988
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x908
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x354c8
-  __DATA_CONST.__objc_selrefs: 0x13680
+  __DATA_CONST.__objc_const: 0x35720
+  __DATA_CONST.__objc_selrefs: 0x13728
   __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__cfstring: 0xb760
-  __AUTH_CONST.__const: 0x2630
-  __AUTH_CONST.__objc_const: 0x69c8
+  __AUTH_CONST.__cfstring: 0xb7a0
+  __AUTH_CONST.__const: 0x2650
+  __AUTH_CONST.__objc_const: 0x6a10
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0xd60
-  __AUTH.__objc_data: 0x2120
+  __AUTH_CONST.__auth_got: 0xd68
+  __AUTH.__objc_data: 0x2170
   __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x1a58
-  __DATA.__objc_superrefs: 0x760
-  __DATA.__objc_ivar: 0x22b0
+  __DATA.__objc_classrefs: 0x1a60
+  __DATA.__objc_superrefs: 0x768
+  __DATA.__objc_ivar: 0x22d4
   __DATA.__data: 0x6df0
   __DATA.__bss: 0x450
   __DATA.__common: 0x2

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10832
-  Symbols:   40929
-  CStrings:  18594
+  Functions: 10864
+  Symbols:   41031
+  CStrings:  18635
 
Symbols:
+ -[BrowserController actionPanelAddTabDocumentToReadingList:activityDidFinish:]
+ -[BrowserController toggleBookmarksPresentationWithCollection:completion:]
+ -[BrowserControllerDefaultUIDelegate tabSnapshotGeneratorDelegateForBrowserController:]
+ -[BrowserRootViewController contentSizeForSnapshotGenerator:]
+ -[BrowserRootViewController topBarsHeightForSnapshotGenerator:]
+ -[CatalogViewController _preselectCompletionItemIfNecessaryForQueryString:]
+ -[CatalogViewController completionList:willGoToURL:fromMultipartWebAnswer:]
+ -[CatalogViewController completionListHasScheduledDismissal:]
+ -[CatalogViewController hasScheduledCompletionListDismissal]
+ -[CatalogViewController reportUnifiedFieldSearchDidCancel]
+ -[CatalogViewController searchUIFeedbackDelegate]
+ -[CatalogViewController setHasScheduledCompletionListDismissal:]
+ -[CatalogViewController tableView:contextMenuConfigurationForRowAtIndexPath:point:]
+ -[CatalogViewController tableView:previewForHighlightingContextMenuWithConfiguration:]
+ -[CatalogViewController tableView:willEndContextMenuInteractionWithConfiguration:animator:]
+ -[CatalogViewController willGoToURLFromMultipartWebAnswer:]
+ -[CompletionList _postFeedback:]
+ -[CompletionList cardViewDidAppear:]
+ -[CompletionList didEngageCardSection:]
+ -[CompletionList didEngageResult:]
+ -[CompletionList didPerformCommand:]
+ -[CompletionList didReportUserResponseFeedback:]
+ -[CompletionList resultsDidBecomeVisible:]
+ -[CompletionList shouldHandleCardSectionEngagement:]
+ -[CompletionListVendorForHistoryService completionList:willGoToURL:fromMultipartWebAnswer:]
+ -[CompletionListVendorForHistoryService completionListHasScheduledDismissal:]
+ -[SFSearchResult(CompletionItem) urlStringForHistoryServiceCompletionList]
+ -[SearchStateItem didOriginateFromMultipartWebAnswer]
+ -[SearchStateItem setDidOriginateFromMultipartWebAnswer:]
+ -[TabOverview _createPreviewContainerForItem:]
+ -[TabOverview _layOutPreviewContainers]
+ -[TabOverviewDataSourceAdaptor tabCollectionView:canCloseItem:]
+ -[TabOverviewItemLayoutInfo setTransform:]
+ -[TabOverviewItemLayoutInfo setZPosition:]
+ -[TabOverviewItemLayoutInfo transform]
+ -[TabOverviewItemLayoutInfo zPosition]
+ -[TabOverviewTargetedPreviewContainer .cxx_destruct]
+ -[TabOverviewTargetedPreviewContainer _didRemoveSubview:]
+ -[TabOverviewTargetedPreviewContainer didRemoveLastSubviewBlock]
+ -[TabOverviewTargetedPreviewContainer hitTest:withEvent:]
+ -[TabOverviewTargetedPreviewContainer initWithFrame:]
+ -[TabOverviewTargetedPreviewContainer setDidRemoveLastSubviewBlock:]
+ -[TabOverviewTargetedPreviewContainer setTabOverviewItem:]
+ -[TabOverviewTargetedPreviewContainer tabOverviewItem]
+ GCC_except_table1003
+ GCC_except_table1009
+ GCC_except_table1024
+ GCC_except_table1025
+ GCC_except_table1029
+ GCC_except_table1030
+ GCC_except_table1036
+ GCC_except_table1046
+ GCC_except_table1047
+ GCC_except_table1050
+ GCC_except_table1054
+ GCC_except_table1062
+ GCC_except_table1067
+ GCC_except_table1068
+ GCC_except_table1071
+ GCC_except_table1078
+ GCC_except_table1091
+ GCC_except_table1094
+ GCC_except_table1097
+ GCC_except_table1100
+ GCC_except_table1105
+ GCC_except_table1111
+ GCC_except_table1118
+ GCC_except_table1122
+ GCC_except_table1123
+ GCC_except_table1189
+ GCC_except_table1195
+ GCC_except_table174
+ GCC_except_table205
+ GCC_except_table282
+ GCC_except_table307
+ GCC_except_table315
+ GCC_except_table333
+ GCC_except_table335
+ GCC_except_table338
+ GCC_except_table343
+ GCC_except_table346
+ GCC_except_table352
+ GCC_except_table359
+ GCC_except_table361
+ GCC_except_table368
+ GCC_except_table371
+ GCC_except_table373
+ GCC_except_table375
+ GCC_except_table380
+ GCC_except_table383
+ GCC_except_table401
+ GCC_except_table415
+ GCC_except_table482
+ GCC_except_table487
+ GCC_except_table489
+ GCC_except_table493
+ GCC_except_table504
+ GCC_except_table534
+ GCC_except_table544
+ GCC_except_table547
+ GCC_except_table575
+ GCC_except_table580
+ GCC_except_table594
+ GCC_except_table596
+ GCC_except_table603
+ GCC_except_table638
+ GCC_except_table653
+ GCC_except_table664
+ GCC_except_table679
+ GCC_except_table721
+ GCC_except_table723
+ GCC_except_table731
+ GCC_except_table734
+ GCC_except_table741
+ GCC_except_table746
+ GCC_except_table750
+ GCC_except_table753
+ GCC_except_table756
+ GCC_except_table759
+ GCC_except_table766
+ GCC_except_table768
+ GCC_except_table770
+ GCC_except_table784
+ GCC_except_table794
+ GCC_except_table802
+ GCC_except_table811
+ GCC_except_table827
+ GCC_except_table831
+ GCC_except_table834
+ GCC_except_table837
+ GCC_except_table840
+ GCC_except_table845
+ GCC_except_table846
+ GCC_except_table859
+ GCC_except_table864
+ GCC_except_table879
+ GCC_except_table884
+ GCC_except_table887
+ GCC_except_table892
+ GCC_except_table899
+ GCC_except_table903
+ GCC_except_table909
+ GCC_except_table910
+ GCC_except_table915
+ GCC_except_table921
+ GCC_except_table922
+ GCC_except_table929
+ GCC_except_table934
+ GCC_except_table935
+ GCC_except_table942
+ GCC_except_table947
+ GCC_except_table968
+ GCC_except_table974
+ GCC_except_table985
+ GCC_except_table986
+ GCC_except_table991
+ GCC_except_table997
+ _CATransform3DEqualToTransform
+ _OBJC_CLASS_$_TabOverviewTargetedPreviewContainer
+ _OBJC_IVAR_$_CatalogViewController._hasScheduledCompletionListDismissal
+ _OBJC_IVAR_$_CompletionList._multipartWebAnswerResult
+ _OBJC_IVAR_$_CompletionList._safariShouldHandleCardSectionEngagement
+ _OBJC_IVAR_$_SearchStateItem._didOriginateFromMultipartWebAnswer
+ _OBJC_IVAR_$_TabOverview._previewContainers
+ _OBJC_IVAR_$_TabOverviewItemLayoutInfo._transform
+ _OBJC_IVAR_$_TabOverviewItemLayoutInfo._zPosition
+ _OBJC_IVAR_$_TabOverviewTargetedPreviewContainer._didRemoveLastSubviewBlock
+ _OBJC_IVAR_$_TabOverviewTargetedPreviewContainer._tabOverviewItem
+ _OBJC_METACLASS_$_TabOverviewTargetedPreviewContainer
+ __OBJC_$_INSTANCE_METHODS_TabOverviewTargetedPreviewContainer
+ __OBJC_$_INSTANCE_VARIABLES_TabOverviewTargetedPreviewContainer
+ __OBJC_$_PROP_LIST_TabOverviewTargetedPreviewContainer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BannerControllerDelegate
+ __OBJC_CLASS_RO_$_TabOverviewTargetedPreviewContainer
+ __OBJC_METACLASS_RO_$_TabOverviewTargetedPreviewContainer
+ ___117-[SafariClearBrowsingDataController clearDataAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeTabs:]_block_invoke
+ ___117-[SafariClearBrowsingDataController clearDataAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeTabs:]_block_invoke_2
+ ___21-[CloudTabStore init]_block_invoke
+ ___44-[BrowserController editBookmarksKeyPressed]_block_invoke
+ ___46-[TabOverview _createPreviewContainerForItem:]_block_invoke
+ ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.901
+ ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.905
+ ___71-[BookmarkImporter _getCarrierBundleBuiltinBookmarkInfoWithCompletion:]_block_invoke.259
+ ___71-[BookmarkImporter _getCarrierBundleBuiltinBookmarkInfoWithCompletion:]_block_invoke.259.cold.1
+ ___74-[BrowserController toggleBookmarksPresentationWithCollection:completion:]_block_invoke
+ ___74-[BrowserController toggleBookmarksPresentationWithCollection:completion:]_block_invoke.820
+ ___74-[BrowserController toggleBookmarksPresentationWithCollection:completion:]_block_invoke_2
+ ___75-[TabOverview _updateIndexesMatchingSearchAndPerformLayout:includingItems:]_block_invoke.133
+ ___78-[BrowserController actionPanelAddTabDocumentToReadingList:activityDidFinish:]_block_invoke
+ ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke_18
+ ___97-[CatalogViewController dismissCompletionDetailWindowAndResumeEditingIfNeeded:completionHandler:]_block_invoke.170
+ ___block_descriptor_112_e8_32s40bs_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8s40l8
+ ___block_descriptor_40_e8_32w_e45_v16?0"TabOverviewTargetedPreviewContainer"8lw32l8
+ ___block_descriptor_57_e8_32s40s48s_e17_v16?0"NSArray"8ls32l8s40l8s48l8
+ ___block_descriptor_57_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_81_ea8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.2514
+ ___block_literal_global.649
+ ___block_literal_global.824
+ ___block_literal_global.836
+ ___block_literal_global.856
+ ___block_literal_global.861
+ ___block_literal_global.881
+ ___block_literal_global.888
+ ___block_literal_global.894
+ ___block_literal_global.896
+ ___block_literal_global.900
+ ___block_literal_global.903
+ ___block_literal_global.910
+ _defaultAutoscrollInsets
+ _objc_msgSend$_preselectCompletionItemIfNecessaryForQueryString:
+ _objc_msgSend$actionPanelAddTabDocumentToReadingList:activityDidFinish:
+ _objc_msgSend$completionList:willGoToURL:fromMultipartWebAnswer:
+ _objc_msgSend$completionListHasScheduledDismissal:
+ _objc_msgSend$contextMenuActionProvider
+ _objc_msgSend$destination
+ _objc_msgSend$didOriginateFromMultipartWebAnswer
+ _objc_msgSend$dismissing
+ _objc_msgSend$domainName
+ _objc_msgSend$prewarm
+ _objc_msgSend$reportUnifiedFieldSearchDidCancel
+ _objc_msgSend$searchUIFeedbackDelegate
+ _objc_msgSend$setAutoscrollInsets:
+ _objc_msgSend$setDidOriginateFromMultipartWebAnswer:
+ _objc_msgSend$setDidRemoveLastSubviewBlock:
+ _objc_msgSend$setHasScheduledCompletionListDismissal:
+ _objc_msgSend$setTabOverviewItem:
+ _objc_msgSend$tabSnapshotGeneratorDelegateForBrowserController:
+ _objc_msgSend$willGoToURLFromMultipartWebAnswer:
- -[BrowserController actionPanelAddTabDocumentToReadingList:completion:]
- -[BrowserController contentSizeForSnapshotGenerator:]
- -[BrowserController toggleBookmarksPresentationWithCollection:]
- -[BrowserController topBarsHeightForSnapshotGenerator:]
- -[CatalogViewController cancelUnifiedFieldSearch]
- -[SFSearchResult _postFeedback:]
- -[SFSearchResult(CompletionItem) cardViewDidAppear:]
- -[SFSearchResult(CompletionItem) didEngageCardSection:]
- -[SFSearchResult(CompletionItem) didEngageResult:]
- -[SFSearchResult(CompletionItem) didPerformCommand:]
- -[SFSearchResult(CompletionItem) resultsDidBecomeVisible:]
- -[TabDocument _pauseListeningToPageIfNeeded]
- -[UniversalSearchCompositeResultCompletionItem _postFeedback:]
- -[UniversalSearchCompositeResultCompletionItem cardViewDidAppear:]
- -[UniversalSearchCompositeResultCompletionItem description]
- -[UniversalSearchCompositeResultCompletionItem didEngageCardSection:]
- -[UniversalSearchCompositeResultCompletionItem didEngageResult:]
- -[UniversalSearchCompositeResultCompletionItem didPerformCommand:]
- -[UniversalSearchCompositeResultCompletionItem resultsDidBecomeVisible:]
- GCC_except_table1001
- GCC_except_table1005
- GCC_except_table1012
- GCC_except_table1015
- GCC_except_table1026
- GCC_except_table1027
- GCC_except_table1032
- GCC_except_table1035
- GCC_except_table1038
- GCC_except_table1048
- GCC_except_table1051
- GCC_except_table1052
- GCC_except_table1060
- GCC_except_table1064
- GCC_except_table1069
- GCC_except_table1070
- GCC_except_table1079
- GCC_except_table1080
- GCC_except_table1093
- GCC_except_table1096
- GCC_except_table1103
- GCC_except_table1107
- GCC_except_table1108
- GCC_except_table1113
- GCC_except_table1120
- GCC_except_table1187
- GCC_except_table1193
- GCC_except_table188
- GCC_except_table274
- GCC_except_table283
- GCC_except_table334
- GCC_except_table337
- GCC_except_table341
- GCC_except_table347
- GCC_except_table360
- GCC_except_table362
- GCC_except_table367
- GCC_except_table369
- GCC_except_table374
- GCC_except_table382
- GCC_except_table384
- GCC_except_table402
- GCC_except_table404
- GCC_except_table414
- GCC_except_table458
- GCC_except_table481
- GCC_except_table486
- GCC_except_table488
- GCC_except_table490
- GCC_except_table503
- GCC_except_table532
- GCC_except_table543
- GCC_except_table546
- GCC_except_table574
- GCC_except_table579
- GCC_except_table593
- GCC_except_table595
- GCC_except_table602
- GCC_except_table637
- GCC_except_table652
- GCC_except_table661
- GCC_except_table678
- GCC_except_table720
- GCC_except_table722
- GCC_except_table729
- GCC_except_table732
- GCC_except_table740
- GCC_except_table745
- GCC_except_table747
- GCC_except_table751
- GCC_except_table755
- GCC_except_table757
- GCC_except_table765
- GCC_except_table767
- GCC_except_table769
- GCC_except_table813
- GCC_except_table829
- GCC_except_table832
- GCC_except_table833
- GCC_except_table836
- GCC_except_table839
- GCC_except_table842
- GCC_except_table847
- GCC_except_table848
- GCC_except_table861
- GCC_except_table868
- GCC_except_table881
- GCC_except_table886
- GCC_except_table889
- GCC_except_table894
- GCC_except_table901
- GCC_except_table907
- GCC_except_table912
- GCC_except_table913
- GCC_except_table917
- GCC_except_table925
- GCC_except_table926
- GCC_except_table931
- GCC_except_table937
- GCC_except_table940
- GCC_except_table944
- GCC_except_table949
- GCC_except_table972
- GCC_except_table976
- GCC_except_table987
- GCC_except_table988
- GCC_except_table993
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BannerControllerDelegate
- ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.900
- ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.903
- ___63-[BrowserController toggleBookmarksPresentationWithCollection:]_block_invoke
- ___66-[BrowserRootViewController _turnOnLockedPrivateBrowsingFromSheet]_block_invoke
- ___71-[BookmarkImporter _getCarrierBundleBuiltinBookmarkInfoWithCompletion:]_block_invoke.253
- ___71-[BookmarkImporter _getCarrierBundleBuiltinBookmarkInfoWithCompletion:]_block_invoke.253.cold.1
- ___71-[BrowserController actionPanelAddTabDocumentToReadingList:completion:]_block_invoke
- ___75-[TabOverview _updateIndexesMatchingSearchAndPerformLayout:includingItems:]_block_invoke.131
- ___97-[CatalogViewController dismissCompletionDetailWindowAndResumeEditingIfNeeded:completionHandler:]_block_invoke.164
- ___block_descriptor_104_e8_32s40bs_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8s40l8
- ___block_descriptor_80_ea8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.111
- ___block_literal_global.134
- ___block_literal_global.143
- ___block_literal_global.18
- ___block_literal_global.2518
- ___block_literal_global.59
- ___block_literal_global.648
- ___block_literal_global.823
- ___block_literal_global.835
- ___block_literal_global.855
- ___block_literal_global.860
- ___block_literal_global.880
- ___block_literal_global.887
- ___block_literal_global.892
- ___block_literal_global.895
- ___block_literal_global.897
- ___block_literal_global.901
- ___block_literal_global.909
- _objc_msgSend$actionPanelAddTabDocumentToReadingList:completion:
- _objc_msgSend$bannerController:didUpdateTopBanners:
- _objc_msgSend$cancelUnifiedFieldSearch
CStrings:
+ "\x011\x115!"
+ "\x04\x17\xd1\x14\"\x12\x11\x14!\xf0\xa2\x11Q!!12\x11C"
+ "\x12\x12\x1b\x16\x11\x11!/\x02"
+ "@\"<SearchUIFeedbackDelegate>\"16@0:8"
+ "@\"<TabSnapshotGeneratorDelegate>\"24@0:8@\"BrowserController\"16"
+ "B24@0:8@\"CompletionList\"16"
+ "Safari requested dismissing playback"
+ "T@\"TabOverviewItem\",W,N,V_tabOverviewItem"
+ "T@?,C,N,V_didRemoveLastSubviewBlock"
+ "TB,N,V_didOriginateFromMultipartWebAnswer"
+ "TB,N,V_hasScheduledCompletionListDismissal"
+ "TabOverviewTargetedPreviewContainer"
+ "_didOriginateFromMultipartWebAnswer"
+ "_didRemoveLastSubviewBlock"
+ "_didRemoveSubview:"
+ "_hasScheduledCompletionListDismissal"
+ "_multipartWebAnswerResult"
+ "_preselectCompletionItemIfNecessaryForQueryString:"
+ "_previewContainers"
+ "_safariShouldHandleCardSectionEngagement"
+ "_transform"
+ "_zPosition"
+ "actionPanelAddTabDocumentToReadingList:activityDidFinish:"
+ "completionList:willGoToURL:fromMultipartWebAnswer:"
+ "completionListHasScheduledDismissal:"
+ "contextMenuActionProvider"
+ "didOriginateFromMultipartWebAnswer"
+ "didRemoveLastSubviewBlock"
+ "dismissing"
+ "domainName"
+ "hasScheduledCompletionListDismissal"
+ "prewarm"
+ "reportUnifiedFieldSearchDidCancel"
+ "searchUIFeedbackDelegate"
+ "setDidOriginateFromMultipartWebAnswer:"
+ "setDidRemoveLastSubviewBlock:"
+ "setHasScheduledCompletionListDismissal:"
+ "setTabOverviewItem:"
+ "tabGroupManager:didFinishSyncForScopedBookmarkList:"
+ "tabSnapshotGeneratorDelegateForBrowserController:"
+ "v16@?0@\"TabOverviewTargetedPreviewContainer\"8"
+ "v24@0:8@\"SFSearchResult\"16"
+ "v28@0:8B16@?<v@?B>20"
+ "v40@0:8@\"CompletionList\"16@\"NSURL\"24@\"SFSearchResult\"32"
+ "visionTitle"
+ "visionURL"
+ "web_answer"
+ "willGoToURLFromMultipartWebAnswer:"
+ "{CATransform3D=\"m11\"d\"m12\"d\"m13\"d\"m14\"d\"m21\"d\"m22\"d\"m23\"d\"m24\"d\"m31\"d\"m32\"d\"m33\"d\"m34\"d\"m41\"d\"m42\"d\"m43\"d\"m44\"d}"
+ "\xf0\xf0\xf0\xf0\xf0\xf0QA"
+ "\xf0\xf1\x12"
- "\x011\x115\x11"
- "\x04\x17\xd1\x13\"\x12\x11\x14!\xf0\xa2\x11Q!!12\x11C"
- "\x12\x12\x1b\x16\x11!/\x02"
- "<%@: %p, title = %@, results = %@, bestSectionHeader = %@>"
- "actionPanelAddTabDocumentToReadingList:completion:"
- "bannerController:didUpdateTopBanners:"
- "cancelUnifiedFieldSearch"
- "v28@0:8B16@?<v@?>20"
- "v32@0:8@\"BannerController\"16@\"NSArray\"24"
- "\xf0\xd1\x12"
- "\xf0\xf0\xf0\xf0\xf0\xf0AA"

```
