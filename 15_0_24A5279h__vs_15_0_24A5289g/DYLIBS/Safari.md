## Safari

> `/System/Library/PrivateFrameworks/Safari.framework/Versions/A/Safari`

```diff

-619.1.18.11.1
-  __TEXT.__text: 0x6a1414
+619.1.20.11.1
+  __TEXT.__text: 0x6a3020
   __TEXT.__auth_stubs: 0x47e0
-  __TEXT.__objc_methlist: 0x49d94
-  __TEXT.__gcc_except_tab: 0xc3064
-  __TEXT.__const: 0x4410
+  __TEXT.__objc_methlist: 0x49e64
+  __TEXT.__gcc_except_tab: 0xc2ff8
+  __TEXT.__const: 0x43d0
   __TEXT.__ustring: 0xfd02
-  __TEXT.__cstring: 0x3a7b5
-  __TEXT.__oslogstring: 0x1daf3
+  __TEXT.__cstring: 0x3a9f0
+  __TEXT.__oslogstring: 0x1dc9d
   __TEXT.__dlopen_cstrs: 0x461
-  __TEXT.__unwind_info: 0x37280
-  __TEXT.__objc_classname: 0xb482
-  __TEXT.__objc_methname: 0xf4b12
-  __TEXT.__objc_methtype: 0x214ff
-  __TEXT.__objc_stubs: 0x93600
-  __DATA_CONST.__got: 0x3448
-  __DATA_CONST.__const: 0x3fb0
-  __DATA_CONST.__objc_classlist: 0x1f50
+  __TEXT.__unwind_info: 0x37288
+  __TEXT.__objc_classname: 0xb499
+  __TEXT.__objc_methname: 0xf5785
+  __TEXT.__objc_methtype: 0x215d9
+  __TEXT.__objc_stubs: 0x93e40
+  __DATA_CONST.__got: 0x3488
+  __DATA_CONST.__const: 0x4050
+  __DATA_CONST.__objc_classlist: 0x1f40
   __DATA_CONST.__objc_catlist: 0x300
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1008
+  __DATA_CONST.__objc_protolist: 0x1010
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d7d8
+  __DATA_CONST.__objc_selrefs: 0x2d9c8
   __DATA_CONST.__objc_protorefs: 0x1d0
-  __DATA_CONST.__objc_superrefs: 0x1838
+  __DATA_CONST.__objc_superrefs: 0x1828
   __DATA_CONST.__objc_arraydata: 0xae8
   __AUTH_CONST.__auth_got: 0x2408
-  __AUTH_CONST.__const: 0x195e8
-  __AUTH_CONST.__cfstring: 0x32ca0
-  __AUTH_CONST.__objc_const: 0x8c418
-  __AUTH_CONST.__objc_intobj: 0x1260
+  __AUTH_CONST.__const: 0x19828
+  __AUTH_CONST.__cfstring: 0x32d40
+  __AUTH_CONST.__objc_const: 0x8cb78
+  __AUTH_CONST.__objc_intobj: 0x1248
   __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH_CONST.__objc_arrayobj: 0x510
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0xe858
-  __DATA.__objc_ivar: 0x5d54
-  __DATA.__data: 0xc3d8
-  __DATA.__bss: 0x1a58
+  __AUTH.__objc_data: 0xe7e0
+  __DATA.__objc_ivar: 0x5da8
+  __DATA.__data: 0xc438
+  __DATA.__bss: 0x1a48
   __DATA.__common: 0x1
-  __DATA_DIRTY.__objc_data: 0x50c8
+  __DATA_DIRTY.__objc_data: 0x50a0
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__crash_info: 0x40
   __DATA_DIRTY.__bss: 0x981

   - /usr/lib/libspindump.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysmon.dylib
-  Functions: 33806
-  Symbols:   91322
-  CStrings:  7203
+  Functions: 33847
+  Symbols:   91459
+  CStrings:  7213
 
Symbols:
+ +[StartPageCollectionSectionTitleConfiguration configurationWithValues:]
+ +[StartPageCollectionViewLayoutSupplementaryItem headerSupplementaryItemWithKind:height:]
+ +[StartPagePopoverTogglesDataSource backgroundImageDataWithRowIndex:]
+ +[StartPagePopoverTogglesDataSource numberOfBackgroundImageRows]
+ +[StartPagePopoverTogglesDataSource numberOfSuggestionsRows]
+ +[StartPagePopoverTogglesDataSource suggestionsDataWithRowIndex:]
+ +[WebKitPreferencesManager _userContentControllerForBrowsingMode:profileIdentifier:]
+ -[AppController sectionManagerForProfileWithIdentifier:]
+ -[AssistantPopoverPageMenuItem _setUIElementsToStandardColors]
+ -[AssistantPopoverPageMenuItem mouseEntered:]
+ -[AssistantPopoverPageMenuItem mouseExited:]
+ -[AssistantPopoverPageMenuItem viewWillAppear]
+ -[AssistantPopoverPageMenuItem viewWillDisappear]
+ -[AssistantPopoverResult setSummaryDisclamer:]
+ -[AssistantPopoverResult summaryDisclamer]
+ -[AssistantPopoverResultCollectionViewCell _setupSummaryDisclaimerTextField]
+ -[AssistantPopoverResultCollectionViewCell setSummaryDisclaimer:]
+ -[AssistantPopoverResultCollectionViewCell summaryDisclaimer]
+ -[AssistantPopoverViewController _computeAndUpdateResultSectionsWithAnimation:]
+ -[AssistantPopoverViewController _summaryDisclamerTextFromSearchResult:]
+ -[AssistantPopoverViewController _summaryDisclamerTextFromSearchResult:].cold.1
+ -[AssistantPopoverViewController addDefaultPageMenuItems]
+ -[AssistantPopoverViewController readerVisibilityHasBeenDetermined]
+ -[AssistantPopoverViewController viewWillAppear]
+ -[BrowserNavigationDelegate _loadURLSoon:isReissuingLoadWithUserAndPasswordRemoved:]
+ -[BrowserWindowController _presentAssistantPopover]
+ -[BrowserWindowController currentOrExpectedURL]
+ -[CombinedFavoritesController _associateHistoryItemToFrequentlyVisitedSite:]
+ -[CombinedFavoritesController providerSectionIdentifier]
+ -[DevelopMenuController _updateWebExtensionBackgroundPagesMenuMenuItems].cold.1
+ -[LibrarySidebarNavigationViewController updateTabGroupTabs:inParentTabGroup:]
+ -[LibraryViewController updateTabGroupTabs:inParentTabGroup:]
+ -[RolloverTrackingButton _supportsLongPress]
+ -[SafariSettingsSyncEngineAccessMac _updateStartPageCloudTabsConsent:].cold.1
+ -[StartPageCloudTabsSectionProvider _cloudTabsConsentStateDidChange:]
+ -[StartPageCloudTabsSectionProvider didCollapse:section:]
+ -[StartPageCloudTabsSectionProvider goBackInSection:]
+ -[StartPageCloudTabsSectionProvider titleConfigurationForSection:]
+ -[StartPageCollectionSectionTitleConfiguration .cxx_destruct]
+ -[StartPageCollectionSectionTitleConfiguration _copy]
+ -[StartPageCollectionSectionTitleConfiguration accessibilityLabel]
+ -[StartPageCollectionSectionTitleConfiguration canCollapseSection]
+ -[StartPageCollectionSectionTitleConfiguration canGoBack]
+ -[StartPageCollectionSectionTitleConfiguration configurationByModifyingValues:]
+ -[StartPageCollectionSectionTitleConfiguration copyWithZone:]
+ -[StartPageCollectionSectionTitleConfiguration hash]
+ -[StartPageCollectionSectionTitleConfiguration isEqual:]
+ -[StartPageCollectionSectionTitleConfiguration isSectionCollapsed]
+ -[StartPageCollectionSectionTitleConfiguration makeSecondaryTrailingAccessoryView]
+ -[StartPageCollectionSectionTitleConfiguration makeTrailingAccessoryView]
+ -[StartPageCollectionSectionTitleConfiguration popUpAction]
+ -[StartPageCollectionSectionTitleConfiguration secondaryTrailingAccessoryViewProvider]
+ -[StartPageCollectionSectionTitleConfiguration setAccessibilityLabel:]
+ -[StartPageCollectionSectionTitleConfiguration setCanCollapseSection:]
+ -[StartPageCollectionSectionTitleConfiguration setCanGoBack:]
+ -[StartPageCollectionSectionTitleConfiguration setIsSectionCollapsed:]
+ -[StartPageCollectionSectionTitleConfiguration setPopUpAction:]
+ -[StartPageCollectionSectionTitleConfiguration setSecondaryTrailingAccessoryViewProvider:]
+ -[StartPageCollectionSectionTitleConfiguration setShowsProfileIcon:]
+ -[StartPageCollectionSectionTitleConfiguration setTitle:]
+ -[StartPageCollectionSectionTitleConfiguration setTrailingAccessoryViewProvider:]
+ -[StartPageCollectionSectionTitleConfiguration setUsesCustomShowMore:]
+ -[StartPageCollectionSectionTitleConfiguration showsProfileIcon]
+ -[StartPageCollectionSectionTitleConfiguration title]
+ -[StartPageCollectionSectionTitleConfiguration trailingAccessoryViewProvider]
+ -[StartPageCollectionSectionTitleConfiguration usesCustomShowMore]
+ -[StartPageCollectionSectionTitleView _applyConfiguration]
+ -[StartPageCollectionSectionTitleView configuration]
+ -[StartPageCollectionSectionTitleView controlTintColor]
+ -[StartPageCollectionSectionTitleView setConfiguration:]
+ -[StartPageCollectionSectionTitleView setControlTintColor:]
+ -[StartPageCollectionViewController _didUpdateBackgroundAppearance]
+ -[StartPageCollectionViewController _indexForSectionTitleView:]
+ -[StartPageCollectionViewController _section:didHighlight:forProvider:]
+ -[StartPageCollectionViewController _setUpSectionTitleView:inSection:forProvider:]
+ -[StartPageCollectionViewController _titleViewForSection:]
+ -[StartPageCollectionViewController _updateCustomizationPopupButtonVisibility]
+ -[StartPageCollectionViewController goBackForStartPageCollectionSectionTitleView:]
+ -[StartPageCollectionViewController startPageCollectionSectionProvider:titleConfigurationDidUpdateInSection:]
+ -[StartPageCollectionViewController startPageCollectionSectionTitleView:collapseSection:]
+ -[StartPageCollectionViewControllerAnimator startPageCollectionSectionProvider:titleConfigurationDidUpdateInSection:]
+ -[StartPageEmptyTabGroupFavoritesItem appearance]
+ -[StartPageEmptyTabGroupFavoritesItem setAppearance:]
+ -[StartPageFallbackImageManager displayableImageForImage:withRequiredImageSize:]
+ -[StartPageFavoritesSectionProvider _titleView]
+ -[StartPageFavoritesSectionProvider backgroundAppearance]
+ -[StartPageFavoritesSectionProvider goBackInSection:]
+ -[StartPageFavoritesSectionProvider setBackgroundAppearance:]
+ -[StartPageFavoritesSectionProvider titleConfigurationForSection:]
+ -[StartPageHeadingSectionProvider appearance]
+ -[StartPageHeadingSectionProvider setAppearance:]
+ -[StartPageHeadingViewItem setAppearance:]
+ -[StartPageHighlightViewItem _constrainChinViews]
+ -[StartPageHighlightViewItem relativeDateString]
+ -[StartPageHighlightViewItem setRelativeDateString:]
+ -[StartPageHighlightsSectionProvider titleConfigurationForSection:]
+ -[StartPagePopoverTogglesDataSource initTitleDataSourceWithTitle:]
+ -[StartPagePopoverTogglesDataSource isTitle]
+ -[StartPagePopoverViewController _loadBackgroundImageTogglesData]
+ -[StartPagePopoverViewController _loadSuggestionsTogglesData]
+ -[StartPagePopoverViewController _reloadSuggestionsDataSourceVisibility]
+ -[StartPagePopoverViewController _sectionIndexForSectionType:]
+ -[StartPagePrivacyReportRedesignViewItem populateLabelsWithCachedPrivacyReportMetrics:usesPrivateBrowsing:]
+ -[StartPagePrivacyReportSectionProvider _cachedPrivacyReportData]
+ -[StartPagePrivacyReportSectionProvider _setCachedPrivacyReportData]
+ -[StartPagePrivacyReportSectionProvider titleConfigurationForSection:]
+ -[StartPageReadingListSectionProvider titleConfigurationForSection:]
+ -[StartPageRecentlyClosedTabsSectionProvider _makeClearAllRecentlyClosedTabsButton]
+ -[StartPageRecentlyClosedTabsSectionProvider _makeShowHistoryButtonIfNeeded]
+ -[StartPageRecentlyClosedTabsSectionProvider titleConfigurationForSection:]
+ -[StartPageSiriSuggestionsSectionProvider titleConfigurationForSection:]
+ -[StartPageTouchIconSectionProvider titleConfigurationForSection:]
+ -[TitleRowItem .cxx_destruct]
+ -[TitleRowItem loadView]
+ -[TitleRowItem setTitleText:]
+ -[TitleRowItem titleText]
+ -[TopSite historyItem]
+ -[TopSite setHistoryItem:]
+ -[UnifiedField _pageMenuLongPressAction]
+ -[UnifiedField _updateAssistantButtonImageToShowContentOption:]
+ -[UnifiedField rolloverTrackingButton:didMouseUp:]
+ -[UnifiedField rolloverTrackingButton:mouseEntered:]
+ -[UnifiedField rolloverTrackingButtonDidLongPress:]
+ -[UnifiedField shouldAllowLongPressInRolloverTrackingButton:]
+ GCC_except_table1014
+ GCC_except_table1046
+ GCC_except_table1069
+ GCC_except_table1098
+ GCC_except_table1128
+ GCC_except_table1136
+ GCC_except_table1161
+ GCC_except_table1209
+ GCC_except_table1210
+ GCC_except_table1211
+ GCC_except_table1228
+ GCC_except_table1234
+ GCC_except_table1241
+ GCC_except_table1260
+ GCC_except_table1261
+ GCC_except_table1268
+ GCC_except_table1274
+ GCC_except_table1275
+ GCC_except_table1276
+ GCC_except_table1287
+ GCC_except_table1288
+ GCC_except_table1289
+ GCC_except_table1290
+ GCC_except_table1296
+ GCC_except_table1297
+ GCC_except_table1302
+ GCC_except_table1304
+ GCC_except_table1305
+ GCC_except_table1307
+ GCC_except_table1315
+ GCC_except_table1317
+ GCC_except_table1324
+ GCC_except_table1336
+ GCC_except_table1338
+ GCC_except_table1343
+ GCC_except_table1348
+ GCC_except_table1350
+ GCC_except_table1359
+ GCC_except_table1364
+ GCC_except_table1367
+ GCC_except_table1375
+ GCC_except_table1376
+ GCC_except_table1377
+ GCC_except_table1378
+ GCC_except_table1388
+ GCC_except_table1393
+ GCC_except_table1394
+ GCC_except_table1415
+ GCC_except_table1420
+ GCC_except_table1425
+ GCC_except_table1433
+ GCC_except_table1435
+ GCC_except_table1440
+ GCC_except_table1441
+ GCC_except_table1442
+ GCC_except_table1450
+ GCC_except_table1453
+ GCC_except_table1456
+ GCC_except_table1463
+ GCC_except_table1465
+ GCC_except_table1474
+ GCC_except_table1490
+ GCC_except_table1492
+ GCC_except_table1493
+ GCC_except_table1502
+ GCC_except_table1521
+ GCC_except_table1522
+ GCC_except_table1523
+ GCC_except_table1555
+ GCC_except_table1556
+ GCC_except_table1557
+ GCC_except_table1566
+ GCC_except_table1567
+ GCC_except_table1569
+ GCC_except_table1577
+ GCC_except_table1578
+ GCC_except_table1579
+ GCC_except_table1580
+ GCC_except_table469
+ GCC_except_table469
+ GCC_except_table551
+ GCC_except_table556
+ GCC_except_table579
+ GCC_except_table592
+ GCC_except_table630
+ GCC_except_table746
+ GCC_except_table757
+ GCC_except_table775
+ GCC_except_table775
+ GCC_except_table781
+ GCC_except_table804
+ GCC_except_table825
+ GCC_except_table837
+ GCC_except_table848
+ GCC_except_table849
+ GCC_except_table861
+ GCC_except_table869
+ GCC_except_table888
+ GCC_except_table894
+ GCC_except_table933
+ GCC_except_table980
+ OBJC_IVAR_$_AssistantPopoverPageMenuItem._backgroundView
+ OBJC_IVAR_$_AssistantPopoverPageMenuItem._trackingArea
+ OBJC_IVAR_$_AssistantPopoverResult._summaryDisclamer
+ OBJC_IVAR_$_AssistantPopoverResultCollectionViewCell._summaryDisclaimer
+ OBJC_IVAR_$_AssistantPopoverResultCollectionViewCell._summaryDisclaimerTextField
+ OBJC_IVAR_$_BrowserNavigationDelegate._isReissuingLoadWithUserAndPasswordRemoved
+ OBJC_IVAR_$_BrowserWindowController._assistantPresentationTimer
+ OBJC_IVAR_$_RolloverTrackingButton._mouseDownTimer
+ OBJC_IVAR_$_RolloverTrackingButton._performedLongPress
+ OBJC_IVAR_$_StartPageCollectionSectionTitleConfiguration._accessibilityLabel
+ OBJC_IVAR_$_StartPageCollectionSectionTitleConfiguration._canCollapseSection
+ OBJC_IVAR_$_StartPageCollectionSectionTitleConfiguration._canGoBack
+ OBJC_IVAR_$_StartPageCollectionSectionTitleConfiguration._isSectionCollapsed
+ OBJC_IVAR_$_StartPageCollectionSectionTitleConfiguration._popUpAction
+ OBJC_IVAR_$_StartPageCollectionSectionTitleConfiguration._secondaryTrailingAccessoryViewProvider
+ OBJC_IVAR_$_StartPageCollectionSectionTitleConfiguration._showsProfileIcon
+ OBJC_IVAR_$_StartPageCollectionSectionTitleConfiguration._title
+ OBJC_IVAR_$_StartPageCollectionSectionTitleConfiguration._trailingAccessoryViewProvider
+ OBJC_IVAR_$_StartPageCollectionSectionTitleConfiguration._usesCustomShowMore
+ OBJC_IVAR_$_StartPageCollectionSectionTitleView._configuration
+ OBJC_IVAR_$_StartPageCollectionSectionTitleView._controlTintColor
+ OBJC_IVAR_$_StartPageCollectionViewController._backgroundAppearance
+ OBJC_IVAR_$_StartPageCollectionViewController._hasBackgroundImage
+ OBJC_IVAR_$_StartPageEmptyTabGroupFavoritesItem._appearance
+ OBJC_IVAR_$_StartPageFavoritesSectionProvider._backgroundAppearance
+ OBJC_IVAR_$_StartPageHeadingSectionProvider._appearance
+ OBJC_IVAR_$_StartPageHeadingViewItem._appearance
+ OBJC_IVAR_$_StartPageHighlightViewItem._relativeDateString
+ OBJC_IVAR_$_StartPageHighlightViewItem._relativeDateTextField
+ OBJC_IVAR_$_StartPageHighlightsSectionProvider._relativeDateFormatter
+ OBJC_IVAR_$_StartPagePopoverTogglesDataSource._isTitle
+ OBJC_IVAR_$_StartPagePopoverViewController._backgroundImageTogglesData
+ OBJC_IVAR_$_StartPagePopoverViewController._shouldShowSuggestionsSections
+ OBJC_IVAR_$_StartPagePopoverViewController._suggestionsTogglesData
+ OBJC_IVAR_$_StartPagePopoverViewController._togglesViewHeightConstraint
+ OBJC_IVAR_$_StartPagePrivacyReportRedesignViewItem._cachedMetrics
+ OBJC_IVAR_$_TitleRowItem._textField
+ OBJC_IVAR_$_TitleRowItem._titleText
+ OBJC_IVAR_$_TopSite._historyItem
+ _NSFontTextStyleCaption2
+ _OBJC_CLASS_$_LPImage
+ _OBJC_CLASS_$_NSRelativeDateTimeFormatter
+ _OBJC_CLASS_$_RFReferenceFootnoteCardSection
+ _OBJC_CLASS_$_StartPageCollectionSectionTitleConfiguration
+ _OBJC_CLASS_$_TitleRowItem
+ _OBJC_CLASS_$_WBSPrivacyReportMetrics
+ _OBJC_METACLASS_$_StartPageCollectionSectionTitleConfiguration
+ _OBJC_METACLASS_$_TitleRowItem
+ _WBSCloudBookmarkListRecordNameTopBookmark
+ _WBSSafariBookmarksSyncAgentCloudTabsConsentWasUpdatedNotificationName
+ __101-[StartPageHighlightsSectionProvider didPerformContextMenuShowingEventForItem:socialMenuItems:event:]_block_invoke.60
+ __101-[StartPageHighlightsSectionProvider didPerformContextMenuShowingEventForItem:socialMenuItems:event:]_block_invoke.64
+ __108-[StartPageCollectionViewController collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:]_block_invoke.306
+ __116-[StartPageCollectionViewController startPageCollectionSectionProvider:updateVisibilityOfSectionsWithDataAvailable:]_block_invoke.287
+ __130-[StartPageCollectionViewController startPageCollectionSectionProvider:hideAllItemsInSections:withBatchUpdates:completionHandler:]_block_invoke.282
+ __33-[UnifiedField _showTransientUI:]_block_invoke.175
+ __38-[UnifiedField setSecurityAnnotation:]_block_invoke.146
+ __40-[UnifiedField showPopUpWindowBlockedUI]_block_invoke.178
+ __48-[StartPageCollectionViewController viewDidLoad]_block_invoke.81
+ __49-[StartPageFavoritesSectionProvider _openFolder:]_block_invoke.83
+ __50-[BrowserWindowController unifiedFieldReaderMenu:]_block_invoke.1031
+ __53-[BrowserWindowController _updateUnifiedFieldIconNow]_block_invoke.1193
+ __53-[StartPageSiriSuggestionsSectionProvider reloadData]_block_invoke.112
+ __55-[StartPageCollectionViewController _appendExtraItems:]_block_invoke.191
+ __58-[BrowserWindowController _updateTabTitlesAsynchronously:]_block_invoke.309
+ __58-[BrowserWindowController _updateTabTitlesAsynchronously:]_block_invoke.311
+ __58-[BrowserWindowController audioMenuForBrowserTabViewItem:]_block_invoke.1332
+ __58-[BrowserWindowController audioMenuForBrowserTabViewItem:]_block_invoke.1341
+ __58-[BrowserWindowController audioMenuForBrowserTabViewItem:]_block_invoke.1342
+ __58-[BrowserWindowController audioMenuForBrowserTabViewItem:]_block_invoke_2.1343
+ __60-[BrowserWindowController tabInfosForUnifiedFieldCompletion]_block_invoke.1364
+ __60-[StartPageCloudTabsSectionProvider _changeSelectedTabItem:]_block_invoke.51
+ __61-[StartPageCloudTabsSectionProvider _contextMenuForCloudTab:]_block_invoke.65
+ __61-[StartPageCloudTabsSectionProvider _contextMenuForCloudTab:]_block_invoke.68
+ __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke.102
+ __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke.106
+ __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke.98
+ __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke_2.103
+ __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke_2.107
+ __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke_3.104
+ __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke_3.108
+ __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke_4.109
+ __61-[StartPageHighlightsSectionProvider _contextMenuForFrecent:]_block_invoke.36
+ __61-[StartPageHighlightsSectionProvider _contextMenuForFrecent:]_block_invoke.37
+ __63-[BrowserWindowController unifiedFieldReloadMenu:isInMoreMenu:]_block_invoke.1049
+ __63-[BrowserWindowController unifiedFieldReloadMenu:isInMoreMenu:]_block_invoke.1061
+ __64-[StartPageCollectionViewController _reloadHistoryBasedSections]_block_invoke.147
+ __72-[BrowserWindowController _moveToTabGroupMenuItemForBrowserTabViewItem:]_block_invoke.383
+ __72-[BrowserWindowController _setAssistantCalloutPopoverForContentOptions:]_block_invoke.1092
+ __73-[StartPageRecentlyClosedTabsSectionProvider _contextMenuForTabGroupTab:]_block_invoke.59
+ __73-[StartPageRecentlyClosedTabsSectionProvider _contextMenuForTabGroupTab:]_block_invoke.61
+ __74-[StartPagePopoverViewController _configureDefaultItem:atIndexPath:index:]_block_invoke.370
+ __75-[BrowserWindowController tabGroupManager:didUpdateTabsInTabGroupWithUUID:]_block_invoke.1461
+ __75-[BrowserWindowController tabGroupManager:didUpdateTabsInTabGroupWithUUID:]_block_invoke.1465
+ __75-[StartPageRecentlyClosedTabsSectionProvider titleConfigurationForSection:]_block_invoke.80
+ __76-[StartPageCloudTabsSectionProvider _cloudDevicesDidChange:previousDevices:]_block_invoke.34
+ __76-[StartPageCloudTabsSectionProvider _cloudDevicesDidChange:previousDevices:]_block_invoke.38
+ __76-[StartPagePopoverViewController collectionView:didSelectItemsAtIndexPaths:]_block_invoke.380
+ __77-[BrowserWindowController _goToUnifiedFieldURLWithWindowPolicy:httpReferrer:]_block_invoke.1285
+ __78-[BrowserWindowController closeTabsAutomaticallyIfNecessaryEnsuringOcclusion:]_block_invoke.1206
+ __80-[BrowserWindowController selectTabGroupWithUUID:withOptions:completionHandler:]_block_invoke.1441
+ __80-[BrowserWindowController selectTabGroupWithUUID:withOptions:completionHandler:]_block_invoke.1447
+ __80-[BrowserWindowController selectTabGroupWithUUID:withOptions:completionHandler:]_block_invoke_2.1442
+ __84-[BrowserWindowController mediaAndDisplayCaptureIndicatorMenuForBrowserTabViewItem:]_block_invoke.1351
+ __84-[BrowserWindowController mediaAndDisplayCaptureIndicatorMenuForBrowserTabViewItem:]_block_invoke.1354
+ __84-[BrowserWindowController mediaAndDisplayCaptureIndicatorMenuForBrowserTabViewItem:]_block_invoke_2.1355
+ __84-[BrowserWindowController replaceTabsWithStates:options:allowGoBack:selectTabIndex:]_block_invoke.648
+ __89-[StartPageHighlightsSectionProvider collectionView:itemForRepresentedObjectAtIndexPath:]_block_invoke.27
+ __91-[BrowserWindowController switchToTabWithUUID:inTabGroupWithUUID:closePreviousTabIfNeeded:]_block_invoke.1370
+ __93-[UnifiedField _showAssistantToastsforContentOptionString:forUnifiedToast:forContentOptions:]_block_invoke.174
+ __97-[StartPageReadingListSectionProvider startPageFullDescriptionViewItem:showContextMenuWithEvent:]_block_invoke.54
+ __97-[StartPageReadingListSectionProvider startPageFullDescriptionViewItem:showContextMenuWithEvent:]_block_invoke.55
+ __97-[StartPageReadingListSectionProvider startPageFullDescriptionViewItem:showContextMenuWithEvent:]_block_invoke_2.56
+ __98-[StartPageCollectionViewController collectionView:viewForSupplementaryElementOfKind:atIndexPath:]_block_invoke.297
+ __OBJC_$_CLASS_METHODS_StartPageCollectionSectionTitleConfiguration
+ __OBJC_$_INSTANCE_METHODS_StartPageCollectionSectionTitleConfiguration
+ __OBJC_$_INSTANCE_METHODS_TitleRowItem
+ __OBJC_$_INSTANCE_VARIABLES_StartPageCollectionSectionTitleConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_TitleRowItem
+ __OBJC_$_PROP_LIST_StartPageCollectionSectionTitleConfiguration
+ __OBJC_$_PROP_LIST_StartPageCollectionSectionTitleMutableConfiguration
+ __OBJC_$_PROP_LIST_TitleRowItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_StartPageCollectionSectionTitleMutableConfiguration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_StartPageCollectionSectionTitleMutableConfiguration
+ __OBJC_$_PROTOCOL_REFS_StartPageCollectionSectionTitleMutableConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_StartPageCollectionSectionTitleConfiguration
+ __OBJC_CLASS_RO_$_StartPageCollectionSectionTitleConfiguration
+ __OBJC_CLASS_RO_$_TitleRowItem
+ __OBJC_LABEL_PROTOCOL_$_StartPageCollectionSectionTitleMutableConfiguration
+ __OBJC_METACLASS_RO_$_StartPageCollectionSectionTitleConfiguration
+ __OBJC_METACLASS_RO_$_TitleRowItem
+ __OBJC_PROTOCOL_$_StartPageCollectionSectionTitleMutableConfiguration
+ __WKMenuItemIdentifierToggleVideoViewer
+ __WKMenuItemIdentifierWritingTools
+ __ZL43configureStartPageHighlightViewItemMetadataP26StartPageHighlightViewItemP14LPLinkMetadataP11SLHighlightP17SLAttributionViewP8NSString
+ __ZN6Safari27BrowserBundlePageFormClient13resetForFrameERKNS_2WK11BundleFrameE
+ __ZN6SafariL25frameOrChildContainsFrameERKNS_2WK11BundleFrameES3_
+ ___36-[RolloverTrackingButton mouseDown:]_block_invoke
+ ___54-[BrowserWindowController unifiedFieldToggleAssistant]_block_invoke
+ ___61-[StartPageFavoritesSectionProvider setBackgroundAppearance:]_block_invoke
+ ___63-[StartPageCollectionViewController _indexForSectionTitleView:]_block_invoke
+ ___66-[SafariLocationManagerDelegate locationManager:didFailWithError:]_block_invoke
+ ___66-[StartPageCloudTabsSectionProvider titleConfigurationForSection:]_block_invoke
+ ___66-[StartPageFavoritesSectionProvider titleConfigurationForSection:]_block_invoke
+ ___66-[StartPageTouchIconSectionProvider titleConfigurationForSection:]_block_invoke
+ ___67-[StartPageHighlightsSectionProvider titleConfigurationForSection:]_block_invoke
+ ___68-[StartPageReadingListSectionProvider titleConfigurationForSection:]_block_invoke
+ ___70-[BrowserWindowController _updateTabTitleForTabViewItems:useFastPath:]_block_invoke
+ ___70-[StartPagePrivacyReportSectionProvider titleConfigurationForSection:]_block_invoke
+ ___71-[SafariLocationManagerDelegate locationManagerDidChangeAuthorization:]_block_invoke
+ ___72-[AssistantPopoverViewController _summaryDisclamerTextFromSearchResult:]_block_invoke
+ ___72-[StartPagePopoverViewController _reloadSuggestionsDataSourceVisibility]_block_invoke
+ ___72-[StartPageSiriSuggestionsSectionProvider titleConfigurationForSection:]_block_invoke
+ ___75-[StartPageRecentlyClosedTabsSectionProvider titleConfigurationForSection:]_block_invoke
+ ___75-[StartPageRecentlyClosedTabsSectionProvider titleConfigurationForSection:]_block_invoke_2
+ ___82-[SafariLocationManagerDelegate locationManager:didUpdateToLocation:fromLocation:]_block_invoke
+ ___82-[StartPageCollectionViewController _setUpSectionTitleView:inSection:forProvider:]_block_invoke
+ ___82-[StartPageCollectionViewController goBackForStartPageCollectionSectionTitleView:]_block_invoke
+ ___84-[BrowserNavigationDelegate _loadURLSoon:isReissuingLoadWithUserAndPasswordRemoved:]_block_invoke
+ ___89-[StartPageCollectionViewController startPageCollectionSectionTitleView:collapseSection:]_block_invoke
+ ___ZL24updateImageFromIndexPathP11NSIndexPathP16NSCollectionViewP6NSViewP5NSURLP8NSStringb_block_invoke.678
+ ___ZL24updateImageFromIndexPathP11NSIndexPathP16NSCollectionViewP6NSViewP5NSURLP8NSStringb_block_invoke.681
+ ___ZL24updateImageFromIndexPathP11NSIndexPathP16NSCollectionViewP6NSViewP5NSURLP8NSStringb_block_invoke_2.682
+ ___block_descriptor_32_e23_B16?0"SFCardSection"8l
+ ___block_descriptor_32_e63_v16?0"<StartPageCollectionSectionTitleMutableConfiguration>"8l
+ ___block_descriptor_40_e46_16?0"<StartPageCollectionSectionProvider>"8l
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSTimer"8l
+ ___block_descriptor_40_ea8_32s_e56_v32?0"StartPageTouchIconViewItem"8"NSIndexPath"16^B24l
+ ___block_descriptor_40_ea8_32s_e63_v16?0"<StartPageCollectionSectionTitleMutableConfiguration>"8l
+ ___block_descriptor_40_ea8_32w_e13_"NSView"8?0l
+ ___block_descriptor_48_ea8_32s40s_e25_B24?0"NSIndexPath"8^B16l
+ ___block_descriptor_48_ea8_32s_e63_v16?0"<StartPageCollectionSectionTitleMutableConfiguration>"8l
+ ___block_descriptor_56_ea8_32s40s48s_e46_16?0"<StartPageCollectionSectionProvider>"8l
+ ___block_descriptor_57_ea8_32s40s_e46_16?0"<StartPageCollectionSectionProvider>"8l
+ ___block_descriptor_57_ea8_32s40w48w_e5_v8?0l
+ ___block_descriptor_64_e5_v8?0l
+ ___block_descriptor_73_ea8_32s40s48s56s64s_e24_v16?0"LPLinkMetadata"8l
+ __block_literal_global.1165
+ __block_literal_global.1179
+ __block_literal_global.1184
+ __block_literal_global.1196
+ __block_literal_global.1201
+ __block_literal_global.1216
+ __block_literal_global.1219
+ __block_literal_global.1225
+ __block_literal_global.1226
+ __block_literal_global.123
+ __block_literal_global.123
+ __block_literal_global.1248
+ __block_literal_global.1260
+ __block_literal_global.1288
+ __block_literal_global.133
+ __block_literal_global.135
+ __block_literal_global.1399
+ __block_literal_global.1437
+ __block_literal_global.1440
+ __block_literal_global.1444
+ __block_literal_global.1451
+ __block_literal_global.1455
+ __block_literal_global.181
+ __block_literal_global.2550
+ __block_literal_global.266
+ __block_literal_global.308
+ __block_literal_global.351
+ __block_literal_global.352
+ __block_literal_global.353
+ __block_literal_global.363
+ __block_literal_global.3701
+ __block_literal_global.394
+ __block_literal_global.402
+ __block_literal_global.408
+ __block_literal_global.445
+ __block_literal_global.578
+ __block_literal_global.628
+ __block_literal_global.632
+ __block_literal_global.634
+ __block_literal_global.638
+ __block_literal_global.657
+ __block_literal_global.688
+ __block_literal_global.779
+ __block_literal_global.781
+ __block_literal_global.976
+ __block_literal_global.983
+ __block_literal_global.988
+ _objc_msgSend$_applyConfiguration
+ _objc_msgSend$_associateHistoryItemToFrequentlyVisitedSite:
+ _objc_msgSend$_cachedPrivacyReportData
+ _objc_msgSend$_computeAndUpdateResultSectionsWithAnimation:
+ _objc_msgSend$_constrainChinViews
+ _objc_msgSend$_copy
+ _objc_msgSend$_didUpdateBackgroundAppearance
+ _objc_msgSend$_indexForSectionTitleView:
+ _objc_msgSend$_intent
+ _objc_msgSend$_loadBackgroundImageTogglesData
+ _objc_msgSend$_loadSuggestionsTogglesData
+ _objc_msgSend$_loadURLSoon:isReissuingLoadWithUserAndPasswordRemoved:
+ _objc_msgSend$_makeClearAllRecentlyClosedTabsButton
+ _objc_msgSend$_makeShowHistoryButtonIfNeeded
+ _objc_msgSend$_overrideBackgroundColor
+ _objc_msgSend$_pageMenuLongPressAction
+ _objc_msgSend$_presentAssistantPopover
+ _objc_msgSend$_reloadSuggestionsDataSourceVisibility
+ _objc_msgSend$_section:didHighlight:forProvider:
+ _objc_msgSend$_sectionIndexForSectionType:
+ _objc_msgSend$_setCachedPrivacyReportData
+ _objc_msgSend$_setUIElementsToStandardColors
+ _objc_msgSend$_setUpSectionTitleView:inSection:forProvider:
+ _objc_msgSend$_setupSummaryDisclaimerTextField
+ _objc_msgSend$_summaryDisclamerTextFromSearchResult:
+ _objc_msgSend$_supportsLongPress
+ _objc_msgSend$_titleViewForSection:
+ _objc_msgSend$_toggleReader:
+ _objc_msgSend$_toggleVideoViewerForAssistant:
+ _objc_msgSend$_updateAssistantButtonImageToShowContentOption:
+ _objc_msgSend$_updateCustomizationPopupButtonVisibility
+ _objc_msgSend$_userContentControllerForBrowsingMode:profileIdentifier:
+ _objc_msgSend$addDefaultPageMenuItems
+ _objc_msgSend$backgroundImageDataWithRowIndex:
+ _objc_msgSend$cachedPrivacyReportDataOnStartPageForProfileWithIdentifier:
+ _objc_msgSend$canCollapseSection
+ _objc_msgSend$configurationByModifyingValues:
+ _objc_msgSend$configurationWithValues:
+ _objc_msgSend$currentOrExpectedURL
+ _objc_msgSend$didCollapse:section:
+ _objc_msgSend$didEnableTheaterModeSBA
+ _objc_msgSend$didEncounterHiddenIgnoredSiriSuggestedSite:
+ _objc_msgSend$didTogglePIPFromTheaterMode
+ _objc_msgSend$displayableImageForImage:withRequiredImageSize:
+ _objc_msgSend$dominantColor
+ _objc_msgSend$goBackInSection:
+ _objc_msgSend$headerSupplementaryItemWithKind:height:
+ _objc_msgSend$indexPathsForVisibleSupplementaryElementsOfKind:
+ _objc_msgSend$initTitleDataSourceWithTitle:
+ _objc_msgSend$initWithEffectiveBundlePath:delegate:onQueue:
+ _objc_msgSend$initWithPlatformImage:
+ _objc_msgSend$isSectionCollapsed
+ _objc_msgSend$isTitle
+ _objc_msgSend$lastVisitedDate
+ _objc_msgSend$makeSecondaryTrailingAccessoryView
+ _objc_msgSend$makeTrailingAccessoryView
+ _objc_msgSend$mostSeenKnownTrackerDomain
+ _objc_msgSend$mostSeenKnownTrackerFirstParties
+ _objc_msgSend$numberOfBackgroundImageRows
+ _objc_msgSend$numberOfSuggestionsRows
+ _objc_msgSend$numberOfTrackers
+ _objc_msgSend$popUpAction
+ _objc_msgSend$populateLabelsWithCachedPrivacyReportMetrics:usesPrivateBrowsing:
+ _objc_msgSend$properties
+ _objc_msgSend$readerVisibilityHasBeenDetermined
+ _objc_msgSend$rolloverTrackingButtonDidLongPress:
+ _objc_msgSend$safari_suggestionsLocalizedStringRelativeToNowForDate:
+ _objc_msgSend$safari_suggestionsRelativeDateTimeFormatter
+ _objc_msgSend$setBackgroundAppearance:
+ _objc_msgSend$setCachedPrivacyReportDataOnStartPage:forProfileWithIdentifier:
+ _objc_msgSend$setControlTintColor:
+ _objc_msgSend$setLineBreakStrategy:
+ _objc_msgSend$setMostSeenKnownTrackerDomain:
+ _objc_msgSend$setMostSeenKnownTrackerFirstParties:
+ _objc_msgSend$setNumberOfTrackers:
+ _objc_msgSend$setPopUpAction:
+ _objc_msgSend$setRatioOfTrackedFirstPartiesToAllVisited:
+ _objc_msgSend$setRelativeDateString:
+ _objc_msgSend$setSecondaryTrailingAccessoryViewProvider:
+ _objc_msgSend$setShowsProfileIcon:
+ _objc_msgSend$setSummaryDisclaimer:
+ _objc_msgSend$setSummaryDisclamer:
+ _objc_msgSend$setTrailingAccessoryViewProvider:
+ _objc_msgSend$setUsesCustomShowMore:
+ _objc_msgSend$shouldAllowLongPressInRolloverTrackingButton:
+ _objc_msgSend$showsProfileIcon
+ _objc_msgSend$startPageCollectionSectionProvider:titleConfigurationDidUpdateInSection:
+ _objc_msgSend$subscribeToAssistantAssetIfNeeded
+ _objc_msgSend$suggestionsDataWithRowIndex:
+ _objc_msgSend$summaryDisclamer
+ _objc_msgSend$titleConfigurationForSection:
+ _objc_msgSend$updateTabGroupTabs:inParentTabGroup:
+ _objc_msgSend$usesCustomShowMore
- +[SnippetEditor reopen]
- +[SnippetEditor sharedSnippetEditor]
- +[StartPagePopoverTogglesDataSource sectionManagerForProfileWithIdentifier:]
- -[AssistantPopoverResultCollectionViewCellActionButton setBackgroundColor:]
- -[AssistantPopoverViewController _computeAndUpdateResultSections:]
- -[BrowserNavigationDelegate _loadURLSoon:]
- -[PasswordGenerationMenuItem .cxx_destruct]
- -[PasswordGenerationMenuItem _buildView]
- -[PasswordGenerationMenuItem actionBlock]
- -[PasswordGenerationMenuItem configureWithAppIcon:badge:]
- -[PasswordGenerationMenuItem initWithTitle:subtitle:icon:handler:]
- -[PasswordGenerationMenuItem setActionBlock:]
- -[PasswordGenerationMenuItem setImage:]
- -[PasswordGenerationMenuItem setSubtitle:]
- -[PasswordGenerationMenuItem subtitle]
- -[SnippetEditor .cxx_destruct]
- -[SnippetEditor splitView:constrainMaxCoordinate:ofSubviewAt:]
- -[SnippetEditor splitView:constrainMinCoordinate:ofSubviewAt:]
- -[SnippetEditor textDidChange:]
- -[SnippetEditor updateNow:]
- -[SnippetEditor updatePreview]
- -[SnippetEditor windowDidLoad]
- -[SnippetEditor windowNibName]
- -[SnippetEditorDelegate _webView:getContextMenuFromProposedMenu:forElement:userInfo:completionHandler:]
- -[SnippetEditorDelegate webView:decidePolicyForNavigationAction:decisionHandler:]
- -[SnippetEditorWKWebView .cxx_destruct]
- -[SnippetEditorWKWebView initWithFrame:]
- -[StartPageCloudTabsSectionProvider _appearanceForSupplementaryTitleView]
- -[StartPageCloudTabsSectionProvider _titleViewForSectionAtIndex:]
- -[StartPageCloudTabsSectionProvider appearanceForStartPageCollectionSectionTitleView:]
- -[StartPageCloudTabsSectionProvider collectionView:viewForSupplementaryElementOfKind:atIndexPath:]
- -[StartPageCloudTabsSectionProvider goBackForStartPageCollectionSectionTitleView:]
- -[StartPageCloudTabsSectionProvider highlightSectionAtIndex:]
- -[StartPageCloudTabsSectionProvider startPageCollectionSectionTitleView:collapseSection:]
- -[StartPageCloudTabsSectionProvider unhighlightSectionAtIndex:]
- -[StartPageCloudTabsSectionProvider viewDidLayoutWithFirstSectionIndex:]
- -[StartPageCollectionSectionTitleView _backgroundImageDidChange]
- -[StartPageCollectionSectionTitleView bottomAccessoryViewContainer]
- -[StartPageCollectionSectionTitleView setBottomAccessoryViewContainer:]
- -[StartPageFavoritesSectionProvider _appearanceForSupplementaryTitleView]
- -[StartPageFavoritesSectionProvider _canCollapse]
- -[StartPageFavoritesSectionProvider _updateBackButton]
- -[StartPageFavoritesSectionProvider _updateTitle]
- -[StartPageFavoritesSectionProvider appearanceForStartPageCollectionSectionTitleView:]
- -[StartPageFavoritesSectionProvider appearanceForTitleOfItem:]
- -[StartPageFavoritesSectionProvider collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:]
- -[StartPageFavoritesSectionProvider goBackForStartPageCollectionSectionTitleView:]
- -[StartPageHighlightViewItem _constrainAttributionView]
- -[StartPageHighlightsSectionProvider _appearanceForSupplementaryTitleView]
- -[StartPageHighlightsSectionProvider _canCollapse]
- -[StartPageHighlightsSectionProvider _isCollapsed]
- -[StartPageHighlightsSectionProvider _sectionIndex]
- -[StartPageHighlightsSectionProvider _titleViewForSectionAtIndex:]
- -[StartPageHighlightsSectionProvider appearanceForStartPageCollectionSectionTitleView:]
- -[StartPageHighlightsSectionProvider collectionView:viewForSupplementaryElementOfKind:atIndexPath:]
- -[StartPageHighlightsSectionProvider highlightSectionAtIndex:]
- -[StartPageHighlightsSectionProvider startPageCollectionSectionTitleView:collapseSection:]
- -[StartPageHighlightsSectionProvider unhighlightSectionAtIndex:]
- -[StartPageHighlightsSectionProvider viewDidLayoutWithFirstSectionIndex:]
- -[StartPagePrivacyReportRedesignViewItem populateLabelsWithNumberOfTrackers:usesPrivateBrowsing:]
- -[StartPagePrivacyReportSectionProvider _appearanceForSupplementaryTitleView]
- -[StartPagePrivacyReportSectionProvider appearanceForStartPageCollectionSectionTitleView:]
- -[StartPagePrivacyReportSectionProvider collectionView:viewForSupplementaryElementOfKind:atIndexPath:]
- -[StartPageReadingListSectionProvider _appearanceForSupplementaryTitleView]
- -[StartPageReadingListSectionProvider _canCollapse]
- -[StartPageReadingListSectionProvider _isCollapsed]
- -[StartPageReadingListSectionProvider _sectionIndex]
- -[StartPageReadingListSectionProvider _titleViewForSectionAtIndex:]
- -[StartPageReadingListSectionProvider appearanceForStartPageCollectionSectionTitleView:]
- -[StartPageReadingListSectionProvider collectionView:viewForSupplementaryElementOfKind:atIndexPath:]
- -[StartPageReadingListSectionProvider highlightSectionAtIndex:]
- -[StartPageReadingListSectionProvider startPageCollectionSectionTitleView:collapseSection:]
- -[StartPageReadingListSectionProvider unhighlightSectionAtIndex:]
- -[StartPageReadingListSectionProvider viewDidLayoutWithFirstSectionIndex:]
- -[StartPageRecentlyClosedTabsSectionProvider _appearanceForSupplementaryTitleView]
- -[StartPageRecentlyClosedTabsSectionProvider _createClearAllRecentlyClosedTabsButton]
- -[StartPageRecentlyClosedTabsSectionProvider _createShowHistoryButtonIfNeeded]
- -[StartPageRecentlyClosedTabsSectionProvider _titleViewForSectionAtIndex:]
- -[StartPageRecentlyClosedTabsSectionProvider _updateTitleViewIfNeeded]
- -[StartPageRecentlyClosedTabsSectionProvider appearanceForStartPageCollectionSectionTitleView:]
- -[StartPageRecentlyClosedTabsSectionProvider collectionView:viewForSupplementaryElementOfKind:atIndexPath:]
- -[StartPageRecentlyClosedTabsSectionProvider highlightSectionAtIndex:]
- -[StartPageRecentlyClosedTabsSectionProvider startPageCollectionSectionTitleView:collapseSection:]
- -[StartPageRecentlyClosedTabsSectionProvider unhighlightSectionAtIndex:]
- -[StartPageSiriSuggestionsSectionProvider _appearanceForSupplementaryTitleView]
- -[StartPageSiriSuggestionsSectionProvider _titleViewForSectionAtIndex:]
- -[StartPageSiriSuggestionsSectionProvider appearanceForStartPageCollectionSectionTitleView:]
- -[StartPageSiriSuggestionsSectionProvider highlightSectionAtIndex:]
- -[StartPageSiriSuggestionsSectionProvider startPageCollectionSectionTitleView:collapseSection:]
- -[StartPageSiriSuggestionsSectionProvider unhighlightSectionAtIndex:]
- -[StartPageSiriSuggestionsSectionProvider viewDidLayoutWithFirstSectionIndex:]
- -[StartPageTouchIconSectionProvider _appearanceForSupplementaryTitleView]
- -[StartPageTouchIconSectionProvider _canCollapse]
- -[StartPageTouchIconSectionProvider _isCollapsed]
- -[StartPageTouchIconSectionProvider _titleViewForSectionAtIndex:]
- -[StartPageTouchIconSectionProvider _titleView]
- -[StartPageTouchIconSectionProvider appearanceForStartPageCollectionSectionTitleView:]
- -[StartPageTouchIconSectionProvider collectionView:didEndDisplayingSupplementaryView:forElementOfKind:atIndexPath:]
- -[StartPageTouchIconSectionProvider collectionView:viewForSupplementaryElementOfKind:atIndexPath:]
- -[StartPageTouchIconSectionProvider collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:]
- -[StartPageTouchIconSectionProvider highlightSectionAtIndex:]
- -[StartPageTouchIconSectionProvider startPageCollectionSectionTitleView:collapseSection:]
- -[StartPageTouchIconSectionProvider unhighlightSectionAtIndex:]
- -[StartPageTouchIconSectionProvider viewDidLayoutWithFirstSectionIndex:]
- -[StartPageTouchIconViewItem _backgroundAppearanceDidChange:]
- GCC_except_table1003
- GCC_except_table1005
- GCC_except_table1018
- GCC_except_table1023
- GCC_except_table1030
- GCC_except_table1038
- GCC_except_table1056
- GCC_except_table1061
- GCC_except_table1073
- GCC_except_table1108
- GCC_except_table1137
- GCC_except_table1140
- GCC_except_table1173
- GCC_except_table1198
- GCC_except_table1203
- GCC_except_table1213
- GCC_except_table1215
- GCC_except_table1218
- GCC_except_table1224
- GCC_except_table1233
- GCC_except_table1247
- GCC_except_table1264
- GCC_except_table1266
- GCC_except_table1269
- GCC_except_table1272
- GCC_except_table1278
- GCC_except_table1279
- GCC_except_table1280
- GCC_except_table1292
- GCC_except_table1293
- GCC_except_table1295
- GCC_except_table1298
- GCC_except_table1300
- GCC_except_table1301
- GCC_except_table1309
- GCC_except_table1310
- GCC_except_table1311
- GCC_except_table1312
- GCC_except_table1323
- GCC_except_table1328
- GCC_except_table1344
- GCC_except_table1346
- GCC_except_table1347
- GCC_except_table1353
- GCC_except_table1358
- GCC_except_table1360
- GCC_except_table1363
- GCC_except_table1371
- GCC_except_table1372
- GCC_except_table1379
- GCC_except_table1380
- GCC_except_table1381
- GCC_except_table1382
- GCC_except_table1396
- GCC_except_table1398
- GCC_except_table1401
- GCC_except_table1423
- GCC_except_table1428
- GCC_except_table1429
- GCC_except_table1437
- GCC_except_table1439
- GCC_except_table1444
- GCC_except_table1445
- GCC_except_table1446
- GCC_except_table1454
- GCC_except_table1460
- GCC_except_table1461
- GCC_except_table1469
- GCC_except_table1480
- GCC_except_table1494
- GCC_except_table1501
- GCC_except_table1510
- GCC_except_table1525
- GCC_except_table1527
- GCC_except_table1547
- GCC_except_table1559
- GCC_except_table1561
- GCC_except_table1568
- GCC_except_table1573
- GCC_except_table1574
- GCC_except_table1575
- GCC_except_table369
- GCC_except_table426
- GCC_except_table426
- GCC_except_table552
- GCC_except_table555
- GCC_except_table568
- GCC_except_table580
- GCC_except_table600
- GCC_except_table635
- GCC_except_table635
- GCC_except_table702
- GCC_except_table783
- GCC_except_table786
- GCC_except_table801
- GCC_except_table805
- GCC_except_table828
- GCC_except_table881
- GCC_except_table893
- GCC_except_table920
- GCC_except_table930
- GCC_except_table947
- OBJC_IVAR_$_AssistantPopoverViewController._isEditingPegasusResults
- OBJC_IVAR_$_BrowserViewController._assistantContentOptionsForURL
- OBJC_IVAR_$_PasswordGenerationMenuItem._actionBlock
- OBJC_IVAR_$_PasswordGenerationMenuItem._imageContainerView
- OBJC_IVAR_$_PasswordGenerationMenuItem._imageView
- OBJC_IVAR_$_PasswordGenerationMenuItem._labelContainer
- OBJC_IVAR_$_PasswordGenerationMenuItem._subtitle
- OBJC_IVAR_$_PasswordGenerationMenuItem._subtitleTextField
- OBJC_IVAR_$_PasswordGenerationMenuItem._titleTextField
- OBJC_IVAR_$_SnippetEditor._textView
- OBJC_IVAR_$_SnippetEditor._updateAfterTypingCheckBox
- OBJC_IVAR_$_SnippetEditor._webView
- OBJC_IVAR_$_SnippetEditorWKWebView._delegate
- OBJC_IVAR_$_StartPageCollectionSectionTitleView._bottomAccessoryViewContainer
- OBJC_IVAR_$_StartPagePrivacyReportRedesignViewItem._cachedNumberOfTrackers
- OBJC_IVAR_$_StartPageRecentlyClosedTabsSectionProvider._clearAllRecentlyClosedTabsButton
- OBJC_IVAR_$_StartPageRecentlyClosedTabsSectionProvider._showHistoryButton
- OBJC_IVAR_$_StartPageTouchIconSectionProvider._titleView
- _OBJC_CLASS_$_PasswordGenerationMenuItem
- _OBJC_CLASS_$_SnippetEditor
- _OBJC_CLASS_$_SnippetEditorDelegate
- _OBJC_CLASS_$_SnippetEditorWKWebView
- _OBJC_METACLASS_$_PasswordGenerationMenuItem
- _OBJC_METACLASS_$_SnippetEditor
- _OBJC_METACLASS_$_SnippetEditorDelegate
- _OBJC_METACLASS_$_SnippetEditorWKWebView
- _ZN3WTF10makeStringIJycNS_6StringEEEES1_DpT_.cold.1
- _ZN6Safari32PageLoadTestBundlePageLoadClient23didReachLayoutMilestoneEj.cold.1
- __101-[StartPageHighlightsSectionProvider didPerformContextMenuShowingEventForItem:socialMenuItems:event:]_block_invoke.62
- __101-[StartPageHighlightsSectionProvider didPerformContextMenuShowingEventForItem:socialMenuItems:event:]_block_invoke.66
- __108-[StartPageCollectionViewController collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:]_block_invoke.295
- __116-[StartPageCollectionViewController startPageCollectionSectionProvider:updateVisibilityOfSectionsWithDataAvailable:]_block_invoke.275
- __130-[StartPageCollectionViewController startPageCollectionSectionProvider:hideAllItemsInSections:withBatchUpdates:completionHandler:]_block_invoke.270
- __33-[UnifiedField _showTransientUI:]_block_invoke.174
- __38-[UnifiedField setSecurityAnnotation:]_block_invoke.145
- __40-[ToolbarController toolbarWillAddItem:]_block_invoke.415
- __40-[UnifiedField showPopUpWindowBlockedUI]_block_invoke.177
- __48-[StartPageCollectionViewController viewDidLoad]_block_invoke.78
- __49-[StartPageFavoritesSectionProvider _openFolder:]_block_invoke.85
- __50-[BrowserWindowController unifiedFieldReaderMenu:]_block_invoke.1028
- __53-[BrowserWindowController _updateUnifiedFieldIconNow]_block_invoke.1188
- __53-[StartPageSiriSuggestionsSectionProvider reloadData]_block_invoke.113
- __55-[StartPageCollectionViewController _appendExtraItems:]_block_invoke.192
- __58-[BrowserWindowController _updateTabTitlesAsynchronously:]_block_invoke.306
- __58-[BrowserWindowController _updateTabTitlesAsynchronously:]_block_invoke.308
- __58-[BrowserWindowController audioMenuForBrowserTabViewItem:]_block_invoke.1327
- __58-[BrowserWindowController audioMenuForBrowserTabViewItem:]_block_invoke.1336
- __58-[BrowserWindowController audioMenuForBrowserTabViewItem:]_block_invoke.1337
- __58-[BrowserWindowController audioMenuForBrowserTabViewItem:]_block_invoke_2.1338
- __60-[BrowserWindowController tabInfosForUnifiedFieldCompletion]_block_invoke.1359
- __60-[StartPageCloudTabsSectionProvider _changeSelectedTabItem:]_block_invoke.57
- __61-[StartPageCloudTabsSectionProvider _contextMenuForCloudTab:]_block_invoke.71
- __61-[StartPageCloudTabsSectionProvider _contextMenuForCloudTab:]_block_invoke.74
- __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke.103
- __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke.107
- __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke.99
- __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke_2.104
- __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke_2.108
- __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke_3.105
- __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke_3.109
- __61-[StartPageFavoritesSectionProvider _contextMenuForBookmark:]_block_invoke_4.110
- __61-[StartPageHighlightsSectionProvider _contextMenuForFrecent:]_block_invoke.32
- __61-[StartPageHighlightsSectionProvider _contextMenuForFrecent:]_block_invoke.33
- __63-[BrowserWindowController unifiedFieldReloadMenu:isInMoreMenu:]_block_invoke.1046
- __63-[BrowserWindowController unifiedFieldReloadMenu:isInMoreMenu:]_block_invoke.1055
- __64-[StartPageCollectionViewController _reloadHistoryBasedSections]_block_invoke.148
- __72-[BrowserWindowController _moveToTabGroupMenuItemForBrowserTabViewItem:]_block_invoke.380
- __72-[BrowserWindowController _setAssistantCalloutPopoverForContentOptions:]_block_invoke.1088
- __73-[StartPageRecentlyClosedTabsSectionProvider _contextMenuForTabGroupTab:]_block_invoke.64
- __73-[StartPageRecentlyClosedTabsSectionProvider _contextMenuForTabGroupTab:]_block_invoke.66
- __74-[StartPagePopoverViewController _configureDefaultItem:atIndexPath:index:]_block_invoke.351
- __75-[BrowserWindowController tabGroupManager:didUpdateTabsInTabGroupWithUUID:]_block_invoke.1456
- __75-[BrowserWindowController tabGroupManager:didUpdateTabsInTabGroupWithUUID:]_block_invoke.1460
- __76-[StartPageCloudTabsSectionProvider _cloudDevicesDidChange:previousDevices:]_block_invoke.40
- __76-[StartPageCloudTabsSectionProvider _cloudDevicesDidChange:previousDevices:]_block_invoke.44
- __76-[StartPagePopoverViewController collectionView:didSelectItemsAtIndexPaths:]_block_invoke.361
- __77-[BrowserWindowController _goToUnifiedFieldURLWithWindowPolicy:httpReferrer:]_block_invoke.1280
- __78-[BrowserWindowController closeTabsAutomaticallyIfNecessaryEnsuringOcclusion:]_block_invoke.1201
- __80-[BrowserWindowController selectTabGroupWithUUID:withOptions:completionHandler:]_block_invoke.1436
- __80-[BrowserWindowController selectTabGroupWithUUID:withOptions:completionHandler:]_block_invoke.1442
- __80-[BrowserWindowController selectTabGroupWithUUID:withOptions:completionHandler:]_block_invoke_2.1437
- __84-[BrowserWindowController mediaAndDisplayCaptureIndicatorMenuForBrowserTabViewItem:]_block_invoke.1346
- __84-[BrowserWindowController mediaAndDisplayCaptureIndicatorMenuForBrowserTabViewItem:]_block_invoke.1349
- __84-[BrowserWindowController mediaAndDisplayCaptureIndicatorMenuForBrowserTabViewItem:]_block_invoke_2.1350
- __84-[BrowserWindowController replaceTabsWithStates:options:allowGoBack:selectTabIndex:]_block_invoke.645
- __89-[StartPageHighlightsSectionProvider collectionView:itemForRepresentedObjectAtIndexPath:]_block_invoke.26
- __91-[BrowserWindowController switchToTabWithUUID:inTabGroupWithUUID:closePreviousTabIfNeeded:]_block_invoke.1365
- __93-[UnifiedField _showAssistantToastsforContentOptionString:forUnifiedToast:forContentOptions:]_block_invoke.173
- __97-[StartPageReadingListSectionProvider startPageFullDescriptionViewItem:showContextMenuWithEvent:]_block_invoke.56
- __97-[StartPageReadingListSectionProvider startPageFullDescriptionViewItem:showContextMenuWithEvent:]_block_invoke.57
- __97-[StartPageReadingListSectionProvider startPageFullDescriptionViewItem:showContextMenuWithEvent:]_block_invoke_2.58
- __OBJC_$_CLASS_METHODS_SnippetEditor
- __OBJC_$_INSTANCE_METHODS_PasswordGenerationMenuItem
- __OBJC_$_INSTANCE_METHODS_SnippetEditor
- __OBJC_$_INSTANCE_METHODS_SnippetEditorDelegate
- __OBJC_$_INSTANCE_METHODS_SnippetEditorWKWebView
- __OBJC_$_INSTANCE_VARIABLES_PasswordGenerationMenuItem
- __OBJC_$_INSTANCE_VARIABLES_SnippetEditor
- __OBJC_$_INSTANCE_VARIABLES_SnippetEditorWKWebView
- __OBJC_$_PROP_LIST_PasswordGenerationMenuItem
- __OBJC_$_PROP_LIST_SnippetEditor
- __OBJC_$_PROP_LIST_SnippetEditorDelegate
- __OBJC_CLASS_PROTOCOLS_$_PasswordGenerationMenuItem
- __OBJC_CLASS_PROTOCOLS_$_SnippetEditor
- __OBJC_CLASS_PROTOCOLS_$_SnippetEditorDelegate
- __OBJC_CLASS_RO_$_PasswordGenerationMenuItem
- __OBJC_CLASS_RO_$_SnippetEditor
- __OBJC_CLASS_RO_$_SnippetEditorDelegate
- __OBJC_CLASS_RO_$_SnippetEditorWKWebView
- __OBJC_METACLASS_RO_$_PasswordGenerationMenuItem
- __OBJC_METACLASS_RO_$_SnippetEditor
- __OBJC_METACLASS_RO_$_SnippetEditorDelegate
- __OBJC_METACLASS_RO_$_SnippetEditorWKWebView
- __WKMenuItemIdentifierSwapCharacters
- __ZGVZ36+[SnippetEditor sharedSnippetEditor]E13snippetEditor
- __ZL43configureStartPageHighlightViewItemMetadataP26StartPageHighlightViewItemP14LPLinkMetadataP11SLHighlightP17SLAttributionView
- __ZN3WTF9HashTableINS_6StringENS_12KeyValuePairIS1_NSt3__15tupleIJS1_N6Safari15SnapshotPayloadEyEEEEENS_24KeyValuePairKeyExtractorIS8_EENS_11DefaultHashIS1_EENS_7HashMapIS1_S7_SC_NS_10HashTraitsIS1_EENSE_IS7_EENS_15HashTableTraitsEE18KeyValuePairTraitsESF_E8reinsertEOS8_
- __ZN6SafariL34canAppendSeparatorToCompletionListERN3WTF6VectorINS0_6RefPtrINS_18CompletionListItemENS0_12RawPtrTraitsIS3_EENS0_21DefaultRefDerefTraitsIS3_EEEELm0ENS0_15CrashOnOverflowELm16ENS0_10FastMallocEEE
- __ZNSt3__112__tuple_leafILm0EN3WTF6StringELb0EED2Ev
- __ZZ36+[SnippetEditor sharedSnippetEditor]E13snippetEditor
- ___42-[BrowserNavigationDelegate _loadURLSoon:]_block_invoke
- ___ZL24updateImageFromIndexPathP11NSIndexPathP16NSCollectionViewP6NSViewP5NSURLP8NSStringb_block_invoke.651
- ___ZL24updateImageFromIndexPathP11NSIndexPathP16NSCollectionViewP6NSViewP5NSURLP8NSStringb_block_invoke.654
- ___ZL24updateImageFromIndexPathP11NSIndexPathP16NSCollectionViewP6NSViewP5NSURLP8NSStringb_block_invoke_2.655
- ___block_descriptor_40_ea8_32s_e30_v32?0"NSToolbarItem"8Q16^B24l
- ___block_descriptor_65_ea8_32s40s48s56s_e24_v16?0"LPLinkMetadata"8l
- __block_literal_global.1163
- __block_literal_global.1177
- __block_literal_global.1182
- __block_literal_global.1194
- __block_literal_global.1199
- __block_literal_global.1209
- __block_literal_global.1211
- __block_literal_global.1212
- __block_literal_global.1220
- __block_literal_global.1224
- __block_literal_global.1243
- __block_literal_global.126
- __block_literal_global.1283
- __block_literal_global.134
- __block_literal_global.138
- __block_literal_global.1394
- __block_literal_global.1432
- __block_literal_global.1435
- __block_literal_global.1439
- __block_literal_global.1446
- __block_literal_global.1450
- __block_literal_global.174
- __block_literal_global.215
- __block_literal_global.222
- __block_literal_global.2547
- __block_literal_global.274
- __block_literal_global.332
- __block_literal_global.334
- __block_literal_global.349
- __block_literal_global.364
- __block_literal_global.3702
- __block_literal_global.392
- __block_literal_global.395
- __block_literal_global.400
- __block_literal_global.409
- __block_literal_global.432
- __block_literal_global.575
- __block_literal_global.625
- __block_literal_global.629
- __block_literal_global.631
- __block_literal_global.635
- __block_literal_global.651
- __block_literal_global.661
- __block_literal_global.783
- __block_literal_global.785
- __block_literal_global.973
- __block_literal_global.980
- __block_literal_global.985
- _objc_msgSend$_appearanceForSupplementaryTitleView
- _objc_msgSend$_canCollapse
- _objc_msgSend$_computeAndUpdateResultSections:
- _objc_msgSend$_constrainAttributionView
- _objc_msgSend$_createClearAllRecentlyClosedTabsButton
- _objc_msgSend$_createShowHistoryButtonIfNeeded
- _objc_msgSend$_isCollapsed
- _objc_msgSend$_loadURLSoon:
- _objc_msgSend$_sectionTitleForSelectedTabDevice
- _objc_msgSend$_setViewIsDrawingOnly:
- _objc_msgSend$_titleViewForSectionAtIndex:
- _objc_msgSend$_updateBackButton
- _objc_msgSend$appearanceForStartPageCollectionSectionTitleView:
- _objc_msgSend$appearanceForTitleOfItem:
- _objc_msgSend$bottomAccessoryViewContainer
- _objc_msgSend$didToggleTheaterModeSBA
- _objc_msgSend$highlightSectionAtIndex:
- _objc_msgSend$isEnhancedPrivateBrowsingEnabled
- _objc_msgSend$isProfileStartPageCustomizationEnabled
- _objc_msgSend$keyColorForIcon:
- _objc_msgSend$leadingIconImageForStartPageFavoritesSectionProvider:
- _objc_msgSend$loadHTMLString:baseURL:
- _objc_msgSend$sharedSnippetEditor
- _objc_msgSend$subscribeToAssistantAssetDownload
- _objc_msgSend$unhighlightSectionAtIndex:
- _objc_msgSend$updatePreview
- _objc_msgSend$userFixedPitchFontOfSize:
CStrings:
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/Autocomplete/AutoFillPageTest.mm"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/BrowserMiscellany/NetworkConfigurationController.mm"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/Debug/DebugUtilities.mm"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/History/HistoryItem.mm"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/Reader/ArticleFinderJSController.mm"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/Reader/ReaderController.mm"
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/Reader/ReaderPageTest.mm"
+ "@\"NSView\"8@?0"
+ "B16@?0@\"SFCardSection\"8"
+ "B24@?0@\"NSIndexPath\"8^B16"
+ "Drag to Reorder"
+ "Show in Suggestions"
+ "StartPageCustomizationMenu"
+ "StartPageSiriSuggestionsWelcomeViewElementKind"
+ "Zoom (assistant popover)"
+ "checked, Shared with You, checkbox"
+ "com.apple.Safari.GeolocationController.%!p(MISSING).m_locationManagerQueue"
+ "const slackRedirectPageObserver = new MutationObserver((mutationsList, observer) => {     const childMutation = mutationsList.find(mutation => mutation.type === 'childList');     if (childMutation !== undefined) {          bypassSlackRedirectPage();     }});function bypassSlackRedirectPage() {     const links = document.querySelectorAll('a');     const firstMessageLink = [...links].find(function(link) {        var href = link.href;        if (!href) {            return false;        }        var url = new URL(href);        return url.host === window.location.host && url.pathname.startsWith('/messages/');     });     if (firstMessageLink) {          firstMessageLink.click();          slackRedirectPageObserver.disconnect();     }};slackRedirectPageObserver.observe(document.body, {     childList: true,     subtree: true,});"
+ "customizationTitleIdentifier"
+ "titleItem"
+ "toggle Shared with You section"
+ "unchecked, Shared with You, checkbox"
+ "v16@?0@\"<StartPageCollectionSectionTitleMutableConfiguration>\"8"
+ "v32@?0@\"StartPageTouchIconViewItem\"8@\"NSIndexPath\"16^B24"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/Autocomplete/AutoFillPageTest.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/BrowserMiscellany/NetworkConfigurationController.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/Debug/DebugUtilities.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/History/HistoryItem.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/Reader/ArticleFinderJSController.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/Reader/ReaderController.mm"
- "/AppleInternal/Library/BuildRoots/c9bccf69-2ccc-11ef-98ec-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Safari/Mac/Safari/Reader/ReaderPageTest.mm"
- "Group Name"
- "Show features for web developers"
- "Snippet Editor"
- "SnippetEditor"
- "Text Size"
- "chevron.right"
- "const slackRedirectPageObserver = new MutationObserver((mutationsList, observer) => {     for (const mutation of mutationsList) {          if (mutation.type == 'childList') {               bypassSlackRedirectPage();               return;          }     }});function bypassSlackRedirectPage() {     const links = document.querySelectorAll('a');     const firstMessageLink = [...links].find(link => link.getAttribute('href') && link.getAttribute('href').startsWith('/messages/'));     if (firstMessageLink) {          firstMessageLink.click();          slackRedirectPageObserver.disconnect();     }};slackRedirectPageObserver.observe(document.body, {     childList: true,     subtree: true,});"

```
