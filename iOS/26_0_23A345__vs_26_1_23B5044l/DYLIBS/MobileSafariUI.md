## MobileSafariUI

> `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-622.1.22.10.9
-  __TEXT.__text: 0x24d1d8
-  __TEXT.__auth_stubs: 0x35e0
-  __TEXT.__objc_methlist: 0x227bc
+622.2.5.10.3
+  __TEXT.__text: 0x24f6ac
+  __TEXT.__auth_stubs: 0x3610
+  __TEXT.__objc_methlist: 0x229f4
   __TEXT.__const: 0x1548
-  __TEXT.__gcc_except_tab: 0x1c134
-  __TEXT.__cstring: 0x10654
+  __TEXT.__gcc_except_tab: 0x1c36c
+  __TEXT.__cstring: 0x109b4
   __TEXT.__dlopen_cstrs: 0x774
-  __TEXT.__oslogstring: 0x92a8
+  __TEXT.__oslogstring: 0x91c8
   __TEXT.__ustring: 0x10e8
-  __TEXT.__constg_swiftt: 0xb2c
+  __TEXT.__constg_swiftt: 0xb38
   __TEXT.__swift5_typeref: 0x143c
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_reflstr: 0x698

   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0x9c
   __TEXT.__swift5_types: 0x7c
-  __TEXT.__swift5_capture: 0x1798
+  __TEXT.__swift5_capture: 0x17b8
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xd858
+  __TEXT.__unwind_info: 0xd930
   __TEXT.__eh_frame: 0xd38
-  __TEXT.__objc_classname: 0x3f13
-  __TEXT.__objc_methname: 0x6b326
-  __TEXT.__objc_methtype: 0x14fa2
-  __TEXT.__objc_stubs: 0x46120
-  __DATA_CONST.__got: 0x2c60
-  __DATA_CONST.__const: 0x89f0
-  __DATA_CONST.__objc_classlist: 0x938
+  __TEXT.__objc_classname: 0x3f4d
+  __TEXT.__objc_methname: 0x6b906
+  __TEXT.__objc_methtype: 0x15035
+  __TEXT.__objc_stubs: 0x466a0
+  __DATA_CONST.__got: 0x2cb0
+  __DATA_CONST.__const: 0x8b10
+  __DATA_CONST.__objc_classlist: 0x948
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0xac8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16858
+  __DATA_CONST.__objc_selrefs: 0x169b8
   __DATA_CONST.__objc_protorefs: 0x158
-  __DATA_CONST.__objc_superrefs: 0x690
+  __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__auth_got: 0x1b08
-  __AUTH_CONST.__const: 0x6070
-  __AUTH_CONST.__cfstring: 0xc240
-  __AUTH_CONST.__objc_const: 0x2fe98
+  __AUTH_CONST.__auth_got: 0x1b20
+  __AUTH_CONST.__const: 0x60b0
+  __AUTH_CONST.__cfstring: 0xc4e0
+  __AUTH_CONST.__objc_const: 0x30270
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x2e40
+  __AUTH.__objc_data: 0x2ee0
   __AUTH.__data: 0x188
-  __DATA.__objc_ivar: 0x2088
-  __DATA.__data: 0x7f50
+  __DATA.__objc_ivar: 0x20b4
+  __DATA.__data: 0x7fc0
   __DATA.__bss: 0x1330
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x3d80
-  __DATA_DIRTY.__data: 0x9d8
+  __DATA_DIRTY.__data: 0x9e8
   __DATA_DIRTY.__bss: 0x8d0
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5DCD767C-1BD7-337C-9A93-6A6B3B64BC22
-  Functions: 13430
-  Symbols:   44072
-  CStrings:  21917
+  UUID: 88B89F79-F2B1-3448-86A0-F6916A00E813
+  Functions: 13484
+  Symbols:   44264
+  CStrings:  22022
 
Symbols:
+ +[HistoryController sharedController]
+ +[HistoryController sharedController].cold.1
+ -[BrowserController _pressedNewTabKeyWithOptions:isKeyboardShortcut:]
+ -[BrowserController effectiveNewDocumentShortcutBehavior]
+ -[BrowserController imageForNewDefaultWindowCommand]
+ -[BrowserController openNewNormalTab:]
+ -[BrowserController openNewTabOrWindow:]
+ -[BrowserController titleForNewDefaultWindowCommand]
+ -[BrowserControllerDefaultUIDelegate browserControllerIsFullscreen:]
+ -[BrowserRootViewController tabOverviewDidChangePerformingReducedMotionTransition:]
+ -[CalculationResultCompletionItem tableItemEqualityInfo]
+ -[CapsuleNavigationBarViewController _updateTabDocumentsAnimated:reloadingTab:]
+ -[CatalogViewControllerState debugDescription]
+ -[CompletionGroup groupIdentifier]
+ -[CompletionGroup initWithTitle:groupIdentifier:completions:maximumNumberOfCompletions:]
+ -[CompletionGroup initWithTitle:groupIdentifier:completions:query:maximumNumberOfCompletions:]
+ -[CompletionGroup initWithTitle:groupIdentifier:completions:query:maximumNumberOfCompletions:].cold.1
+ -[CompletionGroupListing _groupWithTitle:identifier:completions:]
+ -[CompletionGroupListing _groupWithTitle:identifier:completions:maximumCompletions:]
+ -[CompletionList identifierForGroupAtIndex:]
+ -[CompletionListTableItem .cxx_destruct]
+ -[CompletionListTableItem completionItem]
+ -[CompletionListTableItem description]
+ -[CompletionListTableItem hash]
+ -[CompletionListTableItem initWithCompletionItem:]
+ -[CompletionListTableItem isEqual:]
+ -[CompletionListTableViewController dataSource]
+ -[CompletionListTableViewDataSource .cxx_destruct]
+ -[CompletionListTableViewDataSource actionHandler]
+ -[CompletionListTableViewDataSource buildSnapshot]
+ -[CompletionListTableViewDataSource completionItemAtIndexPath:]
+ -[CompletionListTableViewDataSource initWithTableView:]
+ -[CompletionListTableViewDataSource reloadVisibleRows]
+ -[CompletionListTableViewDataSource setActionHandler:]
+ -[CompletionListTableViewDataSource tableView:cellForItem:atIndexPath:]
+ -[CompletionListTableViewDataSource updateTableViewWithCompletionList:animated:completion:]
+ -[CompletionListTableViewDataSource updateTableViewWithCompletionList:rowAnimation:completion:]
+ -[FindOnPageCompletionItem tableItemEqualityInfo]
+ -[HistoryController _init]
+ -[PencilInputCompletionItem tableItemEqualityInfo]
+ -[QuickWebsiteSearchCompletionItem tableItemEqualityInfo]
+ -[SFHistoryViewController didMoveToParentViewController:]
+ -[SFHistoryViewController resetSearchText]
+ -[SFSearchResult(CompletionItem) tableItemEqualityInfo]
+ -[SearchQueryRestorationCompletionItem tableItemEqualityInfo]
+ -[SearchSuggestion tableItemEqualityInfo]
+ -[TabController closeWBTabs:action:]
+ -[TabController tabGroupManagerDidDeletedAllLocalTabs:]
+ -[TabDocument webViewWillChangeSize]
+ -[TabSwitcherViewController _closeItems:action:]
+ -[WBSBrowserTabCompletionMatch(SafariCompletionItem) tableItemEqualityInfo]
+ -[WBSURLCompletionMatch(SafariCompletionItem) tableItemEqualityInfo]
+ GCC_except_table1003
+ GCC_except_table1006
+ GCC_except_table1012
+ GCC_except_table1023
+ GCC_except_table1030
+ GCC_except_table1034
+ GCC_except_table1036
+ GCC_except_table1040
+ GCC_except_table1051
+ GCC_except_table1052
+ GCC_except_table1053
+ GCC_except_table1054
+ GCC_except_table1062
+ GCC_except_table1063
+ GCC_except_table1066
+ GCC_except_table1075
+ GCC_except_table1091
+ GCC_except_table1093
+ GCC_except_table1100
+ GCC_except_table1104
+ GCC_except_table1108
+ GCC_except_table1112
+ GCC_except_table1121
+ GCC_except_table1123
+ GCC_except_table1129
+ GCC_except_table1131
+ GCC_except_table1135
+ GCC_except_table1141
+ GCC_except_table1142
+ GCC_except_table1143
+ GCC_except_table1145
+ GCC_except_table1157
+ GCC_except_table1158
+ GCC_except_table1164
+ GCC_except_table1166
+ GCC_except_table1179
+ GCC_except_table1180
+ GCC_except_table1182
+ GCC_except_table1183
+ GCC_except_table1191
+ GCC_except_table1199
+ GCC_except_table1200
+ GCC_except_table1203
+ GCC_except_table1207
+ GCC_except_table1211
+ GCC_except_table1219
+ GCC_except_table1236
+ GCC_except_table1239
+ GCC_except_table1242
+ GCC_except_table1245
+ GCC_except_table1248
+ GCC_except_table1255
+ GCC_except_table1262
+ GCC_except_table1268
+ GCC_except_table1269
+ GCC_except_table1270
+ GCC_except_table1271
+ GCC_except_table1343
+ GCC_except_table1349
+ GCC_except_table519
+ GCC_except_table528
+ GCC_except_table532
+ GCC_except_table541
+ GCC_except_table546
+ GCC_except_table551
+ GCC_except_table552
+ GCC_except_table577
+ GCC_except_table588
+ GCC_except_table595
+ GCC_except_table597
+ GCC_except_table602
+ GCC_except_table624
+ GCC_except_table646
+ GCC_except_table658
+ GCC_except_table678
+ GCC_except_table688
+ GCC_except_table704
+ GCC_except_table712
+ GCC_except_table713
+ GCC_except_table726
+ GCC_except_table746
+ GCC_except_table748
+ GCC_except_table751
+ GCC_except_table774
+ GCC_except_table776
+ GCC_except_table782
+ GCC_except_table787
+ GCC_except_table794
+ GCC_except_table810
+ GCC_except_table822
+ GCC_except_table837
+ GCC_except_table838
+ GCC_except_table839
+ GCC_except_table848
+ GCC_except_table855
+ GCC_except_table856
+ GCC_except_table867
+ GCC_except_table874
+ GCC_except_table876
+ GCC_except_table883
+ GCC_except_table884
+ GCC_except_table897
+ GCC_except_table902
+ GCC_except_table909
+ GCC_except_table922
+ GCC_except_table939
+ GCC_except_table945
+ GCC_except_table966
+ GCC_except_table967
+ GCC_except_table979
+ GCC_except_table986
+ _CompletionGroupIdentifierBookmarksAndHistory
+ _CompletionGroupIdentifierCalculationResult
+ _CompletionGroupIdentifierFindOnPage
+ _CompletionGroupIdentifierMergedSources
+ _CompletionGroupIdentifierPegasusResults
+ _CompletionGroupIdentifierPencilScribble
+ _CompletionGroupIdentifierQuickWebsiteSearch
+ _CompletionGroupIdentifierSearchSuggestions
+ _CompletionGroupIdentifierSuggestedSites
+ _CompletionGroupIdentifierSwitchToTab
+ _CompletionGroupIdentifierSwitchToTabGroup
+ _CompletionGroupIdentifierTopHit
+ _CompletionListTableItemEqualityInfo
+ _OBJC_CLASS_$_CompletionListTableItem
+ _OBJC_CLASS_$_CompletionListTableViewDataSource
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_UIPreviewTarget
+ _OBJC_CLASS_$_UITableViewDiffableDataSource
+ _OBJC_CLASS_$_WBSInternalFeedbackRadar
+ _OBJC_CLASS_$_WBSInternalFeedbackRadarComponent
+ _OBJC_IVAR_$_BrowserRootViewController._sizeForCurrentViewSizeTransition
+ _OBJC_IVAR_$_CapsuleNavigationBarViewController._cachedHighlightPreview
+ _OBJC_IVAR_$_CompletionGroup._groupIdentifier
+ _OBJC_IVAR_$_CompletionListTableItem._completionItem
+ _OBJC_IVAR_$_CompletionListTableItem._equivalenceHash
+ _OBJC_IVAR_$_CompletionListTableItem._tableItemEqualityInfo
+ _OBJC_IVAR_$_CompletionListTableViewController._dataSource
+ _OBJC_IVAR_$_CompletionListTableViewDataSource._actionHandler
+ _OBJC_IVAR_$_CompletionListTableViewDataSource._completionList
+ _OBJC_IVAR_$_CompletionListTableViewDataSource._dataSource
+ _OBJC_IVAR_$_CompletionListTableViewDataSource._tableView
+ _OBJC_IVAR_$_TabController._isClosingWBTabsWithAction
+ _OBJC_IVAR_$_TabController._requestedFilingRadarForTabLoss
+ _OBJC_METACLASS_$_CompletionListTableItem
+ _OBJC_METACLASS_$_CompletionListTableViewDataSource
+ _WBSAboutSrcdocString
+ __OBJC_$_CLASS_METHODS_HistoryController
+ __OBJC_$_CLASS_PROP_LIST_HistoryController
+ __OBJC_$_INSTANCE_METHODS_CompletionListTableItem
+ __OBJC_$_INSTANCE_METHODS_CompletionListTableViewDataSource
+ __OBJC_$_INSTANCE_VARIABLES_CompletionListTableItem
+ __OBJC_$_INSTANCE_VARIABLES_CompletionListTableViewDataSource
+ __OBJC_$_PROP_LIST_CompletionListTableItem
+ __OBJC_$_PROP_LIST_CompletionListTableViewDataSource
+ __OBJC_CLASS_RO_$_CompletionListTableItem
+ __OBJC_CLASS_RO_$_CompletionListTableViewDataSource
+ __OBJC_METACLASS_RO_$_CompletionListTableItem
+ __OBJC_METACLASS_RO_$_CompletionListTableViewDataSource
+ ___116-[URLCompletionDatabase enumerateMatchDataForTypedStringHint:filterResultsUsingProfileIdentifier:options:withBlock:]_block_invoke.280
+ ___116-[URLCompletionDatabase enumerateMatchDataForTypedStringHint:filterResultsUsingProfileIdentifier:options:withBlock:]_block_invoke_2.282
+ ___120-[BrowserController _presentModalViewController:fromPopoverSource:useAdaptivePresentationInCompact:animated:completion:]_block_invoke
+ ___140-[TabController tabGroupsMenuElementsWithOptions:newTabGroupName:hostTitle:descendantCount:movingSelectedTabs:actionHandler:dismissHandler:]_block_invoke_4
+ ___32-[BrowserController closeWindow]_block_invoke.955
+ ___32-[BrowserController closeWindow]_block_invoke.955.cold.1
+ ___36-[TabController closeWBTabs:action:]_block_invoke
+ ___36-[TabController closeWBTabs:action:]_block_invoke_2
+ ___36-[TabController closeWBTabs:action:]_block_invoke_3
+ ___36-[TabController closeWBTabs:action:]_block_invoke_4
+ ___36-[TabController closeWBTabs:action:]_block_invoke_5
+ ___36-[TabController closeWBTabs:action:]_block_invoke_6
+ ___36-[TabController closeWBTabs:action:]_block_invoke_7
+ ___36-[TabController closeWBTabs:action:]_block_invoke_8
+ ___37+[HistoryController sharedController]_block_invoke
+ ___38-[TabController closeTabWithURL:UUID:]_block_invoke.104
+ ___40-[TabController _updateTabsForTabGroup:]_block_invoke.492
+ ___40-[TabController _updateTabsForTabGroup:]_block_invoke.493
+ ___40-[TabSwitcherViewController viewDidLoad]_block_invoke_32
+ ___44-[URLCompletionProvider setQueryToComplete:]_block_invoke.209
+ ___50-[CompletionListTableViewDataSource buildSnapshot]_block_invoke
+ ___50-[TabController closeTabsAutomaticallyIfNecessary]_block_invoke.41
+ ___54-[CompletionListTableViewDataSource reloadVisibleRows]_block_invoke
+ ___55-[CompletionListTableViewDataSource initWithTableView:]_block_invoke
+ ___55-[TabController tabGroupManagerDidDeletedAllLocalTabs:]_block_invoke
+ ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1159
+ ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1160
+ ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1161
+ ___57-[TabController openNewTabWithOptions:completionHandler:]_block_invoke.102
+ ___57-[TabController openNewTabWithOptions:completionHandler:]_block_invoke.102.cold.1
+ ___69-[BrowserController _pressedNewTabKeyWithOptions:isKeyboardShortcut:]_block_invoke
+ ___69-[BrowserController _pressedNewTabKeyWithOptions:isKeyboardShortcut:]_block_invoke_2
+ ___71-[BrowserController _extractTextFromReaderWebViewOfTab:withCompletion:]_block_invoke.1124
+ ___71-[BrowserController _extractTextFromReaderWebViewOfTab:withCompletion:]_block_invoke.1124.cold.1
+ ___71-[CompletionListTableViewDataSource tableView:cellForItem:atIndexPath:]_block_invoke
+ ___72-[BrowserController _sendPDFRepresentationForScreenshotWithTabDocument:]_block_invoke.1185
+ ___74-[BrowserController toggleBookmarksPresentationWithCollection:completion:]_block_invoke.1049
+ ___75-[BrowserController addBookmarkNavController:didFinishWithResult:bookmark:]_block_invoke.1019
+ ___79-[CapsuleNavigationBarViewController _updateTabDocumentsAnimated:reloadingTab:]_block_invoke
+ ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke.177
+ ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke_2.178
+ ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke_3.179
+ ___96-[BrowserController catalogViewController:presentViewControllerWithinPopover:completionHandler:]_block_invoke.209
+ ___97-[CatalogViewController dismissCompletionDetailWindowAndResumeEditingIfNeeded:completionHandler:]_block_invoke.130
+ ___block_descriptor_32_e51_"CompletionListTableItem"16?0"<CompletionItem>"8l
+ ___block_descriptor_40_e8_32s_e46_"CompletionListTableItem"16?0"NSIndexPath"8ls32l8
+ ___block_descriptor_40_e8_32w_e28_v24?0"NSSet"8"UIAction"16lw32l8
+ ___block_descriptor_40_e8_32w_e82_"UITableViewCell"32?0"UITableView"8"NSIndexPath"16"CompletionListTableItem"24lw32l8
+ ___block_descriptor_40_ea8_32s_e59_"UIView"16?0"UIZoomTransitionSourceViewProviderContext"8ls32l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.101
+ ___block_literal_global.1010
+ ___block_literal_global.1048
+ ___block_literal_global.1054
+ ___block_literal_global.1066
+ ___block_literal_global.1090
+ ___block_literal_global.1095
+ ___block_literal_global.1101
+ ___block_literal_global.1107
+ ___block_literal_global.1109
+ ___block_literal_global.1111
+ ___block_literal_global.1113
+ ___block_literal_global.1120
+ ___block_literal_global.1132
+ ___block_literal_global.1140
+ ___block_literal_global.1148
+ ___block_literal_global.1152
+ ___block_literal_global.1158
+ ___block_literal_global.1172
+ ___block_literal_global.146
+ ___block_literal_global.158
+ ___block_literal_global.194
+ ___block_literal_global.196
+ ___block_literal_global.210
+ ___block_literal_global.216
+ ___block_literal_global.233
+ ___block_literal_global.250
+ ___block_literal_global.263
+ ___block_literal_global.289
+ ___block_literal_global.2941
+ ___block_literal_global.319
+ ___block_literal_global.330
+ ___block_literal_global.354
+ ___block_literal_global.496
+ ___block_literal_global.57
+ ___block_literal_global.599
+ ___block_literal_global.604
+ ___block_literal_global.606
+ ___block_literal_global.608
+ ___block_literal_global.610
+ ___block_literal_global.613
+ ___block_literal_global.615
+ ___block_literal_global.618
+ ___block_literal_global.63
+ ___block_literal_global.68
+ ___block_literal_global.72
+ ___block_literal_global.74
+ ___block_literal_global.76
+ ___block_literal_global.770
+ ___block_literal_global.795
+ ___block_literal_global.802
+ ___block_literal_global.839
+ ___block_literal_global.87
+ ___block_literal_global.883
+ ___block_literal_global.909
+ ___block_literal_global.958
+ _block_copy_helper.107
+ _block_copy_helper.151
+ _block_copy_helper.160
+ _block_copy_helper.167
+ _block_copy_helper.170
+ _block_descriptor.109
+ _block_descriptor.153
+ _block_descriptor.162
+ _block_descriptor.169
+ _block_descriptor.172
+ _block_destroy_helper.108
+ _block_destroy_helper.152
+ _block_destroy_helper.161
+ _block_destroy_helper.168
+ _block_destroy_helper.171
+ _objc_msgSend$_closeItems:action:
+ _objc_msgSend$_init
+ _objc_msgSend$_sf_isFullScreenHeight
+ _objc_msgSend$_updateTabDocumentsAnimated:reloadingTab:
+ _objc_msgSend$applySnapshot:animatingDifferences:completion:
+ _objc_msgSend$browserControllerIsFullscreen:
+ _objc_msgSend$buildSnapshot
+ _objc_msgSend$closeWBTabs:action:
+ _objc_msgSend$completionItem
+ _objc_msgSend$completionItemAtIndexPath:
+ _objc_msgSend$continueInTapToRadarURL
+ _objc_msgSend$defaultRowAnimation
+ _objc_msgSend$existingSharedHistoryController
+ _objc_msgSend$groupIdentifier
+ _objc_msgSend$identifierForGroupAtIndex:
+ _objc_msgSend$initWithCompletionItem:
+ _objc_msgSend$initWithComponent:title:descriptionTemplate:
+ _objc_msgSend$initWithTableView:
+ _objc_msgSend$initWithTableView:cellProvider:
+ _objc_msgSend$initWithTitle:groupIdentifier:completions:query:maximumNumberOfCompletions:
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$null
+ _objc_msgSend$openNewWindowInFrontmostProfile:
+ _objc_msgSend$postFixString
+ _objc_msgSend$preferredNewDocumentShortcutBehavior
+ _objc_msgSend$reloadVisibleRows
+ _objc_msgSend$removeAllCoreSpotlightTabDataDonatedBySafariForProfileWithIdentifier:
+ _objc_msgSend$resetSearchText
+ _objc_msgSend$safariTabsAll
+ _objc_msgSend$safari_URLByNormalizingBlobURL
+ _objc_msgSend$safari_looksLikeAboutSrcdocURL
+ _objc_msgSend$selectedCapsuleFrame
+ _objc_msgSend$separatorEffect
+ _objc_msgSend$setActionHandler:
+ _objc_msgSend$setClassification:
+ _objc_msgSend$setDefaultRowAnimation:
+ _objc_msgSend$setPreferredTransition:
+ _objc_msgSend$setReducedMotionTransitionObserver:
+ _objc_msgSend$setReproducibility:
+ _objc_msgSend$tabOverviewDidChangePerformingReducedMotionTransition:
+ _objc_msgSend$tableItemEqualityInfo
+ _objc_msgSend$tableView:cellForItem:atIndexPath:
+ _objc_msgSend$updateTableViewWithCompletionList:animated:completion:
+ _objc_msgSend$updateTableViewWithCompletionList:rowAnimation:completion:
+ _objc_msgSend$viewForSupplementaryWithIdentifier:
+ _objc_msgSend$webViewWillChangeSize
+ _objc_msgSend$zoomWithOptions:sourceViewProvider:
+ _objectdestroy.149Tm
+ _sharedController.once
- -[BrowserController _pressedNewTabKeySwitchingToPrivateBrowsingIfNeeded:positionOptions:isKeyboardShortcut:]
- -[CatalogViewController numberOfSectionsInTableView:]
- -[CatalogViewController numberOfSectionsInTableView:].cold.1
- -[CatalogViewController tableView:cellForRowAtIndexPath:]
- -[CatalogViewController tableView:cellForRowAtIndexPath:].cold.1
- -[CatalogViewController tableView:numberOfRowsInSection:]
- -[CatalogViewController tableView:numberOfRowsInSection:].cold.1
- -[CompletionGroup initWithTitle:completions:maximumNumberOfCompletions:]
- -[CompletionGroup initWithTitle:completions:query:maximumNumberOfCompletions:]
- -[CompletionGroup initWithTitle:completions:query:maximumNumberOfCompletions:].cold.1
- -[CompletionGroupListing _groupWithTitle:completions:]
- -[CompletionGroupListing _groupWithTitle:completions:maximumCompletions:]
- -[HistoryController init]
- -[TabSwitcherViewController _closeItems:]
- GCC_except_table1008
- GCC_except_table1011
- GCC_except_table1022
- GCC_except_table1028
- GCC_except_table1035
- GCC_except_table1039
- GCC_except_table1046
- GCC_except_table1050
- GCC_except_table1056
- GCC_except_table1057
- GCC_except_table1058
- GCC_except_table1067
- GCC_except_table1068
- GCC_except_table1071
- GCC_except_table1074
- GCC_except_table1080
- GCC_except_table1096
- GCC_except_table1103
- GCC_except_table1105
- GCC_except_table1109
- GCC_except_table1113
- GCC_except_table1117
- GCC_except_table1126
- GCC_except_table1128
- GCC_except_table1134
- GCC_except_table1136
- GCC_except_table1140
- GCC_except_table1146
- GCC_except_table1147
- GCC_except_table1148
- GCC_except_table1150
- GCC_except_table1167
- GCC_except_table1168
- GCC_except_table1171
- GCC_except_table1174
- GCC_except_table1184
- GCC_except_table1185
- GCC_except_table1188
- GCC_except_table1192
- GCC_except_table1196
- GCC_except_table1204
- GCC_except_table1212
- GCC_except_table1213
- GCC_except_table1215
- GCC_except_table1216
- GCC_except_table1229
- GCC_except_table1246
- GCC_except_table1250
- GCC_except_table1252
- GCC_except_table1253
- GCC_except_table1254
- GCC_except_table1260
- GCC_except_table1338
- GCC_except_table1344
- GCC_except_table428
- GCC_except_table538
- GCC_except_table545
- GCC_except_table549
- GCC_except_table559
- GCC_except_table591
- GCC_except_table605
- GCC_except_table614
- GCC_except_table649
- GCC_except_table668
- GCC_except_table685
- GCC_except_table690
- GCC_except_table700
- GCC_except_table717
- GCC_except_table725
- GCC_except_table730
- GCC_except_table750
- GCC_except_table790
- GCC_except_table813
- GCC_except_table833
- GCC_except_table841
- GCC_except_table844
- GCC_except_table851
- GCC_except_table852
- GCC_except_table853
- GCC_except_table868
- GCC_except_table872
- GCC_except_table875
- GCC_except_table878
- GCC_except_table885
- GCC_except_table888
- GCC_except_table889
- GCC_except_table904
- GCC_except_table905
- GCC_except_table907
- GCC_except_table930
- GCC_except_table963
- GCC_except_table971
- GCC_except_table972
- GCC_except_table989
- GCC_except_table991
- _OBJC_IVAR_$_BrowserController._isPerformingRootViewControllerSizeTransition
- _OBJC_IVAR_$_BrowserRootViewController._isPerformingSizeTransition
- _OUTLINED_FUNCTION_101
- _OUTLINED_FUNCTION_102
- ___108-[BrowserController _pressedNewTabKeySwitchingToPrivateBrowsingIfNeeded:positionOptions:isKeyboardShortcut:]_block_invoke
- ___108-[BrowserController _pressedNewTabKeySwitchingToPrivateBrowsingIfNeeded:positionOptions:isKeyboardShortcut:]_block_invoke_2
- ___116-[URLCompletionDatabase enumerateMatchDataForTypedStringHint:filterResultsUsingProfileIdentifier:options:withBlock:]_block_invoke.276
- ___116-[URLCompletionDatabase enumerateMatchDataForTypedStringHint:filterResultsUsingProfileIdentifier:options:withBlock:]_block_invoke_2.278
- ___29-[TabController closeWBTabs:]_block_invoke
- ___29-[TabController closeWBTabs:]_block_invoke_2
- ___29-[TabController closeWBTabs:]_block_invoke_3
- ___29-[TabController closeWBTabs:]_block_invoke_4
- ___29-[TabController closeWBTabs:]_block_invoke_5
- ___29-[TabController closeWBTabs:]_block_invoke_6
- ___29-[TabController closeWBTabs:]_block_invoke_7
- ___29-[TabController closeWBTabs:]_block_invoke_8
- ___32-[BrowserController closeWindow]_block_invoke.940
- ___32-[BrowserController closeWindow]_block_invoke.940.cold.1
- ___38-[TabController closeTabWithURL:UUID:]_block_invoke.68
- ___40-[TabController _updateTabsForTabGroup:]_block_invoke.456
- ___40-[TabController _updateTabsForTabGroup:]_block_invoke.457
- ___44-[URLCompletionProvider setQueryToComplete:]_block_invoke.204
- ___50-[TabController closeTabsAutomaticallyIfNecessary]_block_invoke.5
- ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1142
- ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1143
- ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.1144
- ___57-[CatalogViewController tableView:cellForRowAtIndexPath:]_block_invoke
- ___57-[TabController openNewTabWithOptions:completionHandler:]_block_invoke.66
- ___57-[TabController openNewTabWithOptions:completionHandler:]_block_invoke.66.cold.1
- ___66-[CapsuleNavigationBarViewController _updateTabDocumentsAnimated:]_block_invoke
- ___71-[BrowserController _extractTextFromReaderWebViewOfTab:withCompletion:]_block_invoke.1107
- ___71-[BrowserController _extractTextFromReaderWebViewOfTab:withCompletion:]_block_invoke.1107.cold.1
- ___72-[BrowserController _sendPDFRepresentationForScreenshotWithTabDocument:]_block_invoke.1168
- ___74-[BrowserController toggleBookmarksPresentationWithCollection:completion:]_block_invoke.1032
- ___75-[BrowserController addBookmarkNavController:didFinishWithResult:bookmark:]_block_invoke.1004
- ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke.176
- ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke_2.177
- ___81-[BrowserController setFavoritesState:forVoiceSearch:animated:completionHandler:]_block_invoke_3.178
- ___96-[BrowserController catalogViewController:presentViewControllerWithinPopover:completionHandler:]_block_invoke.208
- ___97-[CatalogViewController dismissCompletionDetailWindowAndResumeEditingIfNeeded:completionHandler:]_block_invoke.143
- ___block_descriptor_40_e8_32w_e15_v16?0"NSSet"8lw32l8
- ___block_literal_global.102
- ___block_literal_global.1031
- ___block_literal_global.1037
- ___block_literal_global.1049
- ___block_literal_global.1073
- ___block_literal_global.1078
- ___block_literal_global.1100
- ___block_literal_global.1103
- ___block_literal_global.1106
- ___block_literal_global.1108
- ___block_literal_global.1110
- ___block_literal_global.1112
- ___block_literal_global.1114
- ___block_literal_global.1123
- ___block_literal_global.1131
- ___block_literal_global.1135
- ___block_literal_global.1141
- ___block_literal_global.1155
- ___block_literal_global.122
- ___block_literal_global.137
- ___block_literal_global.180
- ___block_literal_global.193
- ___block_literal_global.195
- ___block_literal_global.208
- ___block_literal_global.227
- ___block_literal_global.23
- ___block_literal_global.236
- ___block_literal_global.248
- ___block_literal_global.253
- ___block_literal_global.27
- ___block_literal_global.283
- ___block_literal_global.29
- ___block_literal_global.2924
- ___block_literal_global.314
- ___block_literal_global.318
- ___block_literal_global.32
- ___block_literal_global.38
- ___block_literal_global.42
- ___block_literal_global.460
- ___block_literal_global.539
- ___block_literal_global.544
- ___block_literal_global.546
- ___block_literal_global.548
- ___block_literal_global.550
- ___block_literal_global.553
- ___block_literal_global.555
- ___block_literal_global.558
- ___block_literal_global.73
- ___block_literal_global.755
- ___block_literal_global.780
- ___block_literal_global.801
- ___block_literal_global.824
- ___block_literal_global.868
- ___block_literal_global.894
- ___block_literal_global.943
- ___block_literal_global.995
- _block_copy_helper.106
- _block_copy_helper.150
- _block_copy_helper.159
- _block_copy_helper.166
- _block_copy_helper.169
- _block_descriptor.108
- _block_descriptor.152
- _block_descriptor.161
- _block_descriptor.168
- _block_descriptor.171
- _block_destroy_helper.107
- _block_destroy_helper.151
- _block_destroy_helper.160
- _block_destroy_helper.167
- _block_destroy_helper.170
- _objc_msgSend$_closeItems:
- _objc_msgSend$initWithTitle:completions:query:maximumNumberOfCompletions:
- _objc_msgSend$reloadRowsAtIndexPaths:withRowAnimation:
- _objectdestroy.148Tm
CStrings:
+ "%p"
+ "<%@: %p; queryString = %@; showingCompletions = %@>"
+ "<%@; %@>"
+ "@\"CompletionListTableItem\"16@?0@\"<CompletionItem>\"8"
+ "@\"CompletionListTableItem\"16@?0@\"NSIndexPath\"8"
+ "@\"CompletionListTableViewDataSource\""
+ "@\"UITableViewCell\"32@?0@\"UITableView\"8@\"NSIndexPath\"16@\"CompletionListTableItem\"24"
+ "@\"UITableViewDiffableDataSource\""
+ "@\"UITargetedPreview\""
+ "@\"UIView\"16@?0@\"UIZoomTransitionSourceViewProviderContext\"8"
+ "@56@0:8@16@24@32@40Q48"
+ "BookmarksAndHistory"
+ "Cancel filing radar for tab loss"
+ "CompletionListTableItem"
+ "CompletionListTableViewDataSource"
+ "Describe what you were doing in Safari before filing the radar."
+ "Duplicate items detected: "
+ "File a radar for tab loss"
+ "If this was unintended, please file a radar to help us investigate."
+ "MergedSources"
+ "New Window (Keyboard)"
+ "Not Applicable"
+ "Open new normal tab"
+ "PegasusResults"
+ "PencilScribble"
+ "SearchSuggestions"
+ "Serious Bug"
+ "SuggestedSites"
+ "SwitchToTabGroup"
+ "T@\"<CompletionItem>\",R,N,V_completionItem"
+ "T@\"<CompletionItemActionHandler>\",W,N,V_actionHandler"
+ "T@\"CompletionListTableViewDataSource\",R,N"
+ "T@\"NSString\",R,C,N,V_groupIdentifier"
+ "TopHit"
+ "[Internal] Safari closed all local tabs in your default profile"
+ "[Tab Loss] All local tabs are lost"
+ "_cachedHighlightPreview"
+ "_closeItems:action:"
+ "_completionItem"
+ "_equivalenceHash"
+ "_groupIdentifier"
+ "_init"
+ "_isClosingWBTabsWithAction"
+ "_requestedFilingRadarForTabLoss"
+ "_sf_isFullScreenHeight"
+ "_sizeForCurrentViewSizeTransition"
+ "_tableItemEqualityInfo"
+ "_updateTabDocumentsAnimated:reloadingTab:"
+ "actionHandler"
+ "applySnapshot:animatingDifferences:completion:"
+ "browserControllerIsFullscreen:"
+ "buildSnapshot"
+ "closeWBTabs:action:"
+ "completionItem"
+ "completionItemAtIndexPath:"
+ "continueInTapToRadarURL"
+ "defaultRowAnimation"
+ "existingSharedHistoryController"
+ "groupIdentifier"
+ "identifierForGroupAtIndex:"
+ "initWithCompletionItem:"
+ "initWithComponent:title:descriptionTemplate:"
+ "initWithTableView:"
+ "initWithTableView:cellProvider:"
+ "initWithTitle:groupIdentifier:completions:maximumNumberOfCompletions:"
+ "initWithTitle:groupIdentifier:completions:query:maximumNumberOfCompletions:"
+ "null"
+ "openNewNormalTab:"
+ "openNewTabOrWindow:"
+ "plus.rectangle"
+ "preferredNewDocumentShortcutBehavior"
+ "reloadVisibleRows"
+ "removeAllCoreSpotlightTabDataDonatedBySafariForProfileWithIdentifier:"
+ "resetSearchText"
+ "safariTabsAll"
+ "safari_URLByNormalizingBlobURL"
+ "safari_looksLikeAboutSrcdocURL"
+ "selectedCapsuleFrame"
+ "separatorEffect"
+ "setActionHandler:"
+ "setClassification:"
+ "setDefaultRowAnimation:"
+ "setReducedMotionTransitionObserver:"
+ "setReproducibility:"
+ "tabGroupManagerDidDeletedAllLocalTabs:"
+ "tabOverviewDidChangePerformingReducedMotionTransition:"
+ "tableItemEqualityInfo"
+ "tableView:cellForItem:atIndexPath:"
+ "updateTableViewWithCompletionList:animated:completion:"
+ "updateTableViewWithCompletionList:rowAnimation:completion:"
+ "v24@?0@\"NSSet\"8@\"UIAction\"16"
+ "v32@0:8@\"NSArray\"16@\"UIAction\"24"
+ "viewForSupplementaryWithIdentifier:"
+ "webViewWillChangeSize"
+ "zoomWithOptions:sourceViewProvider:"
- "New Window"
- "No completion item at index path %{public}@; completion list %{public}@ showing recent searches view"
- "Number of completions for group at index %ld: %ld; completion item class: %{public}@"
- "Number of sections in table view: %ld"
- "TB,R,N,V_isPerformingSizeTransition"
- "_closeItems:"
- "_isPerformingRootViewControllerSizeTransition"
- "_isPerformingSizeTransition"
- "initWithTitle:completions:maximumNumberOfCompletions:"
- "initWithTitle:completions:query:maximumNumberOfCompletions:"
- "reloadRowsAtIndexPaths:withRowAnimation:"

```
