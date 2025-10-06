## MobileSafariUI

> `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-616.2.9.10.13
-  __TEXT.__text: 0x1d8bc4
+617.1.17.10.9
+  __TEXT.__text: 0x1db19c
   __TEXT.__auth_stubs: 0x1aa0
-  __TEXT.__objc_methlist: 0x177b8
+  __TEXT.__objc_methlist: 0x17b98
   __TEXT.__const: 0x6c8
-  __TEXT.__gcc_except_tab: 0x17044
-  __TEXT.__cstring: 0xb872
+  __TEXT.__gcc_except_tab: 0x17018
+  __TEXT.__cstring: 0xba39
   __TEXT.__dlopen_cstrs: 0x7a6
-  __TEXT.__oslogstring: 0x7a1a
-  __TEXT.__ustring: 0x10e4
-  __TEXT.__unwind_info: 0xb60c
+  __TEXT.__oslogstring: 0x7b7f
+  __TEXT.__ustring: 0x10f0
+  __TEXT.__unwind_info: 0xb654
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x41fc
-  __TEXT.__objc_methname: 0x62c39
-  __TEXT.__objc_methtype: 0x13cb7
-  __TEXT.__objc_stubs: 0x41060
-  __DATA_CONST.__got: 0xe90
-  __DATA_CONST.__const: 0x7a70
-  __DATA_CONST.__objc_classlist: 0x988
+  __TEXT.__objc_classname: 0x42b5
+  __TEXT.__objc_methname: 0x6382d
+  __TEXT.__objc_methtype: 0x13d4f
+  __TEXT.__objc_stubs: 0x41580
+  __DATA_CONST.__got: 0xe68
+  __DATA_CONST.__const: 0x7aa8
+  __DATA_CONST.__objc_classlist: 0x980
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x908
+  __DATA_CONST.__objc_protolist: 0x928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x35720
-  __DATA_CONST.__objc_selrefs: 0x13728
-  __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__cfstring: 0xb7a0
-  __AUTH_CONST.__const: 0x2650
+  __DATA_CONST.__objc_const: 0x35f88
+  __DATA_CONST.__objc_selrefs: 0x138b8
+  __DATA_CONST.__objc_arraydata: 0x290
+  __AUTH_CONST.__cfstring: 0xb880
+  __AUTH_CONST.__const: 0x25c8
   __AUTH_CONST.__objc_const: 0x6a10
   __AUTH_CONST.__objc_intobj: 0x4c8
-  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0xd68
-  __AUTH.__objc_data: 0x2170
+  __AUTH.__objc_data: 0x2210
   __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x1a60
+  __DATA.__objc_classrefs: 0x1a90
   __DATA.__objc_superrefs: 0x768
-  __DATA.__objc_ivar: 0x22d4
-  __DATA.__data: 0x6df0
-  __DATA.__bss: 0x450
+  __DATA.__objc_ivar: 0x2310
+  __DATA.__data: 0x6f70
+  __DATA.__bss: 0x460
   __DATA.__common: 0x2
-  __DATA_DIRTY.__objc_data: 0x3de0
+  __DATA_DIRTY.__objc_data: 0x3cf0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x4f0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 77500502-BD80-3434-B6CB-8E58AE365EE2
-  Functions: 10864
-  Symbols:   41031
-  CStrings:  20104
+  UUID: 5E05C441-E69F-360B-B1DA-F971D222E4C4
+  Functions: 10955
+  Symbols:   41284
+  CStrings:  20216
 
Symbols:
+ +[SFFluidTabOverviewItemView contentViewClass]
+ +[SFTabOverviewItemContentView initialize]
+ +[TabDocumentDropHandler canAddTabDocument:toSessionWithDragItems:]
+ +[ToolbarItemConfiguration attributedTitleForTabGroup:inProfile:primaryColor:secondaryColor:]
+ -[Application _saveFrequentlyVisitedListsToDatabaseIfNeeded]
+ -[Application focusProfileUpdateIsForInactiveFocusMode]
+ -[Application setFocusProfileUpdateIsForInactiveFocusMode:]
+ -[BookmarksBarView _createAllLabelButtonsIfNeeded]
+ -[BookmarksBarView _didChangeHorizontalSizeClass]
+ -[BookmarksBarView _repositionBookmarksNavigationController]
+ -[BookmarksNavigationController anySizeClassDidChange]
+ -[BookmarksTableViewController contentSizeCategoryDidChange]
+ -[BookmarksTableViewController tableView:heightForHeaderInSection:]
+ -[BookmarksTableViewController updateSeparatorInsetForTraitChange]
+ -[BrowserController _ABGroupIdentifierDidChange:]
+ -[BrowserController _debugAutoFillConsoleLoggingEnabledPreferenceDidChange:]
+ -[BrowserController toggleBookmarksPresentationWithCollection:]
+ -[CatalogViewController horizontalSizeClassDidChange:previousTraitCollection:]
+ -[CompletionGroupListing _buildListIfNeeded].cold.1
+ -[CompletionList currentSearchEngineHostSuffixes]
+ -[PopoverCatalogViewController initWithNibName:bundle:]
+ -[ReadingListTableViewCell _updateMaximumContentSizeCategory]
+ -[ReadingListViewController contentSizeCategoryDidChange]
+ -[ReadingListViewController tableView:heightForHeaderInSection:]
+ -[ReadingListViewController updateColorSchemeForExplanationView]
+ -[SFFluidTabOverviewDragDropHandler .cxx_destruct]
+ -[SFFluidTabOverviewDragDropHandler _dragItemsForItemAtIndexPath:session:]
+ -[SFFluidTabOverviewDragDropHandler fluidCollectionView:canHandleDropSession:]
+ -[SFFluidTabOverviewDragDropHandler fluidCollectionView:itemsForAddingToDragSession:atIndexPath:]
+ -[SFFluidTabOverviewDragDropHandler fluidCollectionView:itemsForBeginningDragSession:atIndexPath:]
+ -[SFFluidTabOverviewDragDropHandler fluidCollectionView:performDropWithCoordinator:]
+ -[SFFluidTabOverviewDragDropHandler fluidTabOverviewViewController]
+ -[SFFluidTabOverviewDragDropHandler initWithMaximumNumberOfTabs:alertPresentationViewController:]
+ -[SFFluidTabOverviewDragDropHandler setFluidTabOverviewViewController:]
+ -[SFFluidTabOverviewGridLayout _effectiveVisibleTopBackdropHeightForSection:]
+ -[SFFluidTabOverviewGridLayoutSectionInfo setVisibleTopBackdropHeight:]
+ -[SFFluidTabOverviewGridLayoutSectionInfo visibleTopBackdropHeight]
+ -[SFFluidTabOverviewItemView _layOutSubviewsDependentOnContentView]
+ -[SFFluidTabOverviewItemView _tabOverviewContentView]
+ -[SFFluidTabOverviewItemView accessibilityIdentifier]
+ -[SFFluidTabOverviewItemView accessibilityLabel]
+ -[SFFluidTabOverviewItemView accessibilityTraits]
+ -[SFFluidTabOverviewItemView contentViewDidLayOutSubviews:]
+ -[SFFluidTabOverviewItemView item]
+ -[SFFluidTabOverviewItemView setItem:]
+ -[SFFluidTabOverviewItemView setSnapshotImage:]
+ -[SFFluidTabOverviewItemView snapshotImage]
+ -[SFFluidTabOverviewItemView tabCollectionItemDidChangeIcon:]
+ -[SFFluidTabOverviewItemView tabCollectionItemDidChangeTitle:]
+ -[SFFluidTabOverviewLayoutAttributes setTitleRevealPercent:]
+ -[SFFluidTabOverviewLayoutAttributes setVisibleTopBackdropHeight:]
+ -[SFFluidTabOverviewLayoutAttributes titleRevealPercent]
+ -[SFFluidTabOverviewLayoutAttributes visibleTopBackdropHeight]
+ -[SFFluidTabOverviewViewController _viewForItemWithIdentifier:]
+ -[SFFluidTabOverviewViewController alternateBottomSafeAreaInset]
+ -[SFFluidTabOverviewViewController dataSource]
+ -[SFFluidTabOverviewViewController fluidCollectionView:didEndDisplayingView:forItemAtIndexPath:]
+ -[SFFluidTabOverviewViewController fluidCollectionView:layout:visibleTopBackdropHeightForItemsInSection:]
+ -[SFFluidTabOverviewViewController fluidCollectionView:layout:visibleTopBackdropHeightForZoomedItemsInSection:]
+ -[SFFluidTabOverviewViewController fluidCollectionView:willDisplayView:forItemAtIndexPath:]
+ -[SFFluidTabOverviewViewController scrollViewDidScroll:]
+ -[SFFluidTabOverviewViewController setAlternateBottomSafeAreaInset:]
+ -[SFFluidTabOverviewViewController tabSnapshotCache:didCacheSnapshotWithIdentifier:]
+ -[SFFluidTabOverviewViewController tabSnapshotCache:didEvictSnapshotWithIdentifier:]
+ -[SFHistoryViewController scrollViewWillEndDragging:withVelocity:targetContentOffset:]
+ -[SFTabOverviewItemContentView .cxx_destruct]
+ -[SFTabOverviewItemContentView _headerBackgroundColor]
+ -[SFTabOverviewItemContentView _updateContentSizeCategory]
+ -[SFTabOverviewItemContentView attachedViewReferenceRect]
+ -[SFTabOverviewItemContentView attachedView]
+ -[SFTabOverviewItemContentView borrowedContentView]
+ -[SFTabOverviewItemContentView canBecomeFocused]
+ -[SFTabOverviewItemContentView closeButton]
+ -[SFTabOverviewItemContentView cornerRadius]
+ -[SFTabOverviewItemContentView delegate]
+ -[SFTabOverviewItemContentView dimmingView]
+ -[SFTabOverviewItemContentView effectiveHeaderMode]
+ -[SFTabOverviewItemContentView enableDelegateLayoutNotification]
+ -[SFTabOverviewItemContentView focusEffect]
+ -[SFTabOverviewItemContentView headerBackgroundView]
+ -[SFTabOverviewItemContentView icon]
+ -[SFTabOverviewItemContentView initWithFrame:]
+ -[SFTabOverviewItemContentView isRecording]
+ -[SFTabOverviewItemContentView isUnread]
+ -[SFTabOverviewItemContentView layoutSubviews]
+ -[SFTabOverviewItemContentView mediaStateIcon]
+ -[SFTabOverviewItemContentView minYMatchesTopBarMaxYWhenZoomed]
+ -[SFTabOverviewItemContentView participantsBackgroundView]
+ -[SFTabOverviewItemContentView placeholderView]
+ -[SFTabOverviewItemContentView pointInside:withEvent:]
+ -[SFTabOverviewItemContentView recordingIndicatorView]
+ -[SFTabOverviewItemContentView setAttachedView:]
+ -[SFTabOverviewItemContentView setAttachedViewReferenceRect:]
+ -[SFTabOverviewItemContentView setBorrowedContentView:]
+ -[SFTabOverviewItemContentView setCornerRadius:]
+ -[SFTabOverviewItemContentView setDelegate:]
+ -[SFTabOverviewItemContentView setDimmingView:]
+ -[SFTabOverviewItemContentView setEnableDelegateLayoutNotification:]
+ -[SFTabOverviewItemContentView setIcon:]
+ -[SFTabOverviewItemContentView setMediaStateIcon:]
+ -[SFTabOverviewItemContentView setMinYMatchesTopBarMaxYWhenZoomed:]
+ -[SFTabOverviewItemContentView setRecording:]
+ -[SFTabOverviewItemContentView setShadowOpacity:]
+ -[SFTabOverviewItemContentView setShareParticipants:]
+ -[SFTabOverviewItemContentView setSnapshotImage:]
+ -[SFTabOverviewItemContentView setSnapshotView:]
+ -[SFTabOverviewItemContentView setTitle:]
+ -[SFTabOverviewItemContentView setTitleRevealPercent:]
+ -[SFTabOverviewItemContentView setTopBarTheme:]
+ -[SFTabOverviewItemContentView setUnread:]
+ -[SFTabOverviewItemContentView setVisibleTopBackdropHeight:]
+ -[SFTabOverviewItemContentView shadowOpacity]
+ -[SFTabOverviewItemContentView shareParticipants]
+ -[SFTabOverviewItemContentView snapshotClipperView]
+ -[SFTabOverviewItemContentView snapshotImage]
+ -[SFTabOverviewItemContentView snapshotView]
+ -[SFTabOverviewItemContentView titleHeight]
+ -[SFTabOverviewItemContentView titlePadding]
+ -[SFTabOverviewItemContentView titleRevealPercent]
+ -[SFTabOverviewItemContentView titleView]
+ -[SFTabOverviewItemContentView title]
+ -[SFTabOverviewItemContentView topBarTheme]
+ -[SFTabOverviewItemContentView visibleTopBackdropHeight]
+ -[SafariClearBrowsingDataController clearHistoryViewController:clearHistoryVisitsAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeAllTabs:]
+ -[SafariClearBrowsingDataController clearHistoryViewController:numberOfTabsToBeClosedForProfilesWithIdentifiers:]
+ -[SafariClearBrowsingDataController setTabGroupProvider:]
+ -[SafariClearBrowsingDataController tabGroupProvider]
+ -[SearchSuggestion initWithSearchEngineSuggestion:userQuery:forPrivateBrowsing:isOfflineSearchSuggestion:]
+ -[SearchSuggestionTableViewCell hidesCompletionArrowView]
+ -[SearchSuggestionTableViewCell preferredContentSizeCategoryDidChange]
+ -[SearchSuggestionTableViewCell setHidesCompletionArrowView:]
+ -[StartPageController profileProviderForCustomizationViewController:]
+ -[StartPageController startPageViewController:didSelectItemWithIdentifier:atGridLocation:]
+ -[TabController _dropTabDocuments:intoCurrentTabDocumentsAtIndex:pinned:closeDocument:transitionToDragStateWithBlock:]
+ -[TabController _insertTabDocument:atIndex:inBackground:animated:updateUI:].cold.1
+ -[TabController dropTabDocuments:intoCurrentTabDocumentsAtIndex:pinned:transitionToDragStateWithBlock:]
+ -[TabController tabCollectionViewItemHeaderHeightIncludedInSnapshot:]
+ -[TabDocument _donateCurrentPageLoad]
+ -[TabDocument _updatePageLoadDonorWithNavigationPolicy:inMainFrameForNavigationAction:]
+ -[TabDocument autoFillController:didCollectFormMetadataForTesting:forURL:]
+ -[TabDocument autoFillControllerShouldCollectFormMetadataForTesting:]
+ -[TabDocument donateSameDocumentNavigationIfNecessary]
+ -[TabDocument isSearchPage]
+ -[TabDocument nextLoadComesFromSearchPage]
+ -[TabDocument setNextLoadComesFromSearchPage:]
+ -[TabDocument test_metadataHandler]
+ -[TabDocument test_setMetadataHandler:]
+ -[TabDocument topBarThemeForTabOverviewShowingThemeColor:]
+ -[TabDocumentCollectionItem addTabCollectionItemObserver:]
+ -[TabDocumentCollectionItem description]
+ -[TabDocumentCollectionItem icon]
+ -[TabDocumentCollectionItem init]
+ -[TabDocumentCollectionItem removeTabCollectionItemObserver:]
+ -[TabDocumentCollectionItem setIcon:]
+ -[TabGroupSwitcherViewController viewDidLayoutSubviews]
+ -[TabIconAndTitleView _preferredContentSizeCategoryDidChange:previousTraitCollection:]
+ -[TabOverview _preferredContentSizeCategoryDidChange]
+ -[TabOverview _setNeedsResizeHeaderItems]
+ -[TabOverview showsLockedPrivateBrowsingView]
+ -[TabOverviewItem cachedTopBarTheme]
+ -[TabOverviewItem setCachedTopBarTheme:]
+ -[TabOverviewItemView _effectiveTransitionProgress]
+ -[TabOverviewItemView _layOutSubviewsDependentOnContentView]
+ -[TabOverviewItemView contentViewDidLayOutSubviews:]
+ -[TabOverviewToolbar _setNeedsResizeItems]
+ -[TabSnapshotCache _enumerateIdentifiersForEntry:respondingToSelector:withBlock:]
+ -[UnifiedField _reflectedItemCompletionString].cold.1
+ -[UnifiedField _setReflectedItem:updateUserTypedPrefix:].cold.1
+ -[WBSAnalyticsLogger(PrivateBrowsingAnalyticsLogger) _performAdvancedPrivacyProtectionPreferenceReport]
+ -[WBSAnalyticsLogger(SettingsAnalyticsLogger) _performNewTabBehaviorReport]
+ -[WBSAnalyticsLogger(SettingsAnalyticsLogger) _settingsAnalyticsLogger_updatePeriodicCoreAnalyticsLastReportTime]
+ -[WBSAnalyticsLogger(SettingsAnalyticsLogger) schedulePeriodicSettingsReport]
+ -[WBSAnalyticsLogger(TabGroupsAnalyticsLogger) _performSyncSuccessesCountReport]
+ GCC_except_table1001
+ GCC_except_table1005
+ GCC_except_table1011
+ GCC_except_table1012
+ GCC_except_table1013
+ GCC_except_table1015
+ GCC_except_table1031
+ GCC_except_table1032
+ GCC_except_table1035
+ GCC_except_table1038
+ GCC_except_table1048
+ GCC_except_table1049
+ GCC_except_table1052
+ GCC_except_table1056
+ GCC_except_table1058
+ GCC_except_table1060
+ GCC_except_table1069
+ GCC_except_table1073
+ GCC_except_table1077
+ GCC_except_table1079
+ GCC_except_table1080
+ GCC_except_table1093
+ GCC_except_table1104
+ GCC_except_table1106
+ GCC_except_table1107
+ GCC_except_table1113
+ GCC_except_table188
+ GCC_except_table198
+ GCC_except_table233
+ GCC_except_table244
+ GCC_except_table274
+ GCC_except_table283
+ GCC_except_table337
+ GCC_except_table341
+ GCC_except_table347
+ GCC_except_table362
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table374
+ GCC_except_table381
+ GCC_except_table384
+ GCC_except_table402
+ GCC_except_table404
+ GCC_except_table414
+ GCC_except_table458
+ GCC_except_table459
+ GCC_except_table481
+ GCC_except_table486
+ GCC_except_table491
+ GCC_except_table492
+ GCC_except_table503
+ GCC_except_table532
+ GCC_except_table533
+ GCC_except_table543
+ GCC_except_table546
+ GCC_except_table574
+ GCC_except_table579
+ GCC_except_table595
+ GCC_except_table602
+ GCC_except_table637
+ GCC_except_table652
+ GCC_except_table661
+ GCC_except_table662
+ GCC_except_table663
+ GCC_except_table678
+ GCC_except_table720
+ GCC_except_table722
+ GCC_except_table732
+ GCC_except_table733
+ GCC_except_table740
+ GCC_except_table751
+ GCC_except_table757
+ GCC_except_table769
+ GCC_except_table813
+ GCC_except_table826
+ GCC_except_table829
+ GCC_except_table830
+ GCC_except_table832
+ GCC_except_table833
+ GCC_except_table836
+ GCC_except_table839
+ GCC_except_table847
+ GCC_except_table848
+ GCC_except_table866
+ GCC_except_table868
+ GCC_except_table886
+ GCC_except_table894
+ GCC_except_table901
+ GCC_except_table905
+ GCC_except_table911
+ GCC_except_table913
+ GCC_except_table917
+ GCC_except_table923
+ GCC_except_table924
+ GCC_except_table925
+ GCC_except_table936
+ GCC_except_table937
+ GCC_except_table938
+ GCC_except_table940
+ GCC_except_table949
+ GCC_except_table970
+ GCC_except_table972
+ GCC_except_table976
+ GCC_except_table987
+ GCC_except_table993
+ GCC_except_table999
+ _OBJC_CLASS_$_SFCombinedCardSection
+ _OBJC_CLASS_$_SFFluidTabOverviewDragDropHandler
+ _OBJC_CLASS_$_SFOpenPunchoutCommand
+ _OBJC_CLASS_$_SFTabOverviewItemContentView
+ _OBJC_CLASS_$_SFTraitUsesSidebarPresentation
+ _OBJC_CLASS_$_SFTraitUsesVibrantAppearance
+ _OBJC_CLASS_$_UITraitHorizontalSizeClass
+ _OBJC_CLASS_$_UITraitPreferredContentSizeCategory
+ _OBJC_CLASS_$_UITraitVerticalSizeClass
+ _OBJC_IVAR_$_Application._focusProfileUpdateIsForInactiveFocusMode
+ _OBJC_IVAR_$_BookmarksBarView._isPerformingLayout
+ _OBJC_IVAR_$_BookmarksBarView._needsRepositionNavigationController
+ _OBJC_IVAR_$_SFFluidTabOverviewDragDropHandler._fluidTabOverviewViewController
+ _OBJC_IVAR_$_SFFluidTabOverviewGridLayoutSectionInfo._visibleTopBackdropHeight
+ _OBJC_IVAR_$_SFFluidTabOverviewItemView._item
+ _OBJC_IVAR_$_SFFluidTabOverviewItemView._shadowView
+ _OBJC_IVAR_$_SFFluidTabOverviewViewController._alternateBottomSafeAreaInset
+ _OBJC_IVAR_$_SFFluidTabOverviewViewController._dragDropHandler
+ _OBJC_IVAR_$_SFFluidTabOverviewViewController._lastVisibleIndexPaths
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._attachedView
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._attachedViewReferenceRect
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._borrowedContentView
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._closeButton
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._contentSizeIsAccessibilityCategory
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._cornerRadius
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._delegate
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._dimmingView
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._enableDelegateLayoutNotification
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._headerBackgroundView
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._mediaStateIcon
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._minYMatchesTopBarMaxYWhenZoomed
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._participantsBackgroundView
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._participantsView
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._placeholderView
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._preferredHeaderMode
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._recording
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._recordingIndicatorView
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._shadowOpacity
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._snapshotClipperView
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._snapshotView
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._titleHeight
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._titleRevealPercent
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._titleView
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._topBarTheme
+ _OBJC_IVAR_$_SFTabOverviewItemContentView._visibleTopBackdropHeight
+ _OBJC_IVAR_$_SafariClearBrowsingDataController._tabGroupProvider
+ _OBJC_IVAR_$_SearchSuggestion._offlineSearchEngineSuggestion
+ _OBJC_IVAR_$_SearchSuggestionTableViewCell._completionArrowView
+ _OBJC_IVAR_$_SearchSuggestionTableViewCell._hidesCompletionArrowView
+ _OBJC_IVAR_$_TabController._shouldUpdateSnapshotsForTabSwitch
+ _OBJC_IVAR_$_TabDocument._nextLoadComesFromSearchPage
+ _OBJC_IVAR_$_TabDocument._shouldDonatePageLoad
+ _OBJC_IVAR_$_TabDocument._test_metadataHandler
+ _OBJC_IVAR_$_TabDocument._wasPageLoadUserInitiated
+ _OBJC_IVAR_$_TabDocumentCollectionItem._icon
+ _OBJC_IVAR_$_TabDocumentCollectionItem._observers
+ _OBJC_IVAR_$_TabGroupSwitcherViewController._lastBottomInset
+ _OBJC_IVAR_$_TabOverviewItem._cachedTopBarTheme
+ _OBJC_METACLASS_$_SFFluidTabOverviewDragDropHandler
+ _OBJC_METACLASS_$_SFTabOverviewItemContentView
+ _SFDeviceSupportsPointerInteractions
+ _SFNewTabBehaviorIsStartPage
+ _TabOverviewCloseButtonMargin
+ _WBSDebugAutoFillConsoleLoggingEnabledPreferenceKey
+ _WBSPeriodicSyncSuccessesCount
+ __OBJC_$_CLASS_METHODS_SFFluidTabOverviewItemView
+ __OBJC_$_CLASS_METHODS_SFTabOverviewItemContentView
+ __OBJC_$_INSTANCE_METHODS_SFFluidTabOverviewDragDropHandler
+ __OBJC_$_INSTANCE_METHODS_SFTabOverviewItemContentView
+ __OBJC_$_INSTANCE_METHODS_WBSAnalyticsLogger(TabGroupsAnalyticsLogger|SettingsAnalyticsLogger|PrivateBrowsingAnalyticsLogger|StandaloneTabBarAnalyticsLogger)
+ __OBJC_$_INSTANCE_VARIABLES_SFFluidTabOverviewDragDropHandler
+ __OBJC_$_INSTANCE_VARIABLES_SFTabOverviewItemContentView
+ __OBJC_$_PROP_LIST_SFFluidTabOverviewDragDropHandler
+ __OBJC_$_PROP_LIST_SFStartPageCustomizationProfileProviding
+ __OBJC_$_PROP_LIST_SFTabOverviewItemContentView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFFluidTabOverviewZoomableGridLayoutDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFTabOverviewItemContentViewDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TabCollectionItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TabCollectionItemObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TabSnapshotCacheObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFStartPageCustomizationProfileProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SFFormAutoFillTestController
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFFluidTabOverviewZoomableGridLayoutDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFStartPageCustomizationProfileProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFTabOverviewItemContentViewDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TabCollectionItemObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SFFormAutoFillTestController
+ __OBJC_$_PROTOCOL_REFS_SFFluidTabOverviewZoomableGridLayoutDelegate
+ __OBJC_$_PROTOCOL_REFS_SFStartPageCustomizationProfileProviding
+ __OBJC_$_PROTOCOL_REFS_SFTabOverviewItemContentViewDelegate
+ __OBJC_$_PROTOCOL_REFS_TabCollectionItemObserving
+ __OBJC_$_PROTOCOL_REFS__SFFormAutoFillTestController
+ __OBJC_CLASS_PROTOCOLS_$_SFFluidTabOverviewDragDropHandler
+ __OBJC_CLASS_PROTOCOLS_$_SFFluidTabOverviewItemView
+ __OBJC_CLASS_PROTOCOLS_$_TabOverviewItemView
+ __OBJC_CLASS_RO_$_SFFluidTabOverviewDragDropHandler
+ __OBJC_CLASS_RO_$_SFTabOverviewItemContentView
+ __OBJC_LABEL_PROTOCOL_$_SFFluidTabOverviewZoomableGridLayoutDelegate
+ __OBJC_LABEL_PROTOCOL_$_SFStartPageCustomizationProfileProviding
+ __OBJC_LABEL_PROTOCOL_$_SFTabOverviewItemContentViewDelegate
+ __OBJC_LABEL_PROTOCOL_$_TabCollectionItemObserving
+ __OBJC_LABEL_PROTOCOL_$__SFFormAutoFillTestController
+ __OBJC_METACLASS_RO_$_SFFluidTabOverviewDragDropHandler
+ __OBJC_METACLASS_RO_$_SFTabOverviewItemContentView
+ __OBJC_PROTOCOL_$_SFFluidTabOverviewZoomableGridLayoutDelegate
+ __OBJC_PROTOCOL_$_SFStartPageCustomizationProfileProviding
+ __OBJC_PROTOCOL_$_SFTabOverviewItemContentViewDelegate
+ __OBJC_PROTOCOL_$_TabCollectionItemObserving
+ __OBJC_PROTOCOL_$__SFFormAutoFillTestController
+ ___108-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestorationIfNeededAfterCloudTabsFinishedSyncing:]_block_invoke.29
+ ___116-[URLCompletionDatabase enumerateMatchDataForTypedStringHint:filterResultsUsingProfileIdentifier:options:withBlock:]_block_invoke.269
+ ___116-[URLCompletionDatabase enumerateMatchDataForTypedStringHint:filterResultsUsingProfileIdentifier:options:withBlock:]_block_invoke_2.272
+ ___118-[TabController _dropTabDocuments:intoCurrentTabDocumentsAtIndex:pinned:closeDocument:transitionToDragStateWithBlock:]_block_invoke
+ ___118-[TabController _dropTabDocuments:intoCurrentTabDocumentsAtIndex:pinned:closeDocument:transitionToDragStateWithBlock:]_block_invoke_2
+ ___118-[TabController _dropTabDocuments:intoCurrentTabDocumentsAtIndex:pinned:closeDocument:transitionToDragStateWithBlock:]_block_invoke_3
+ ___118-[TabController _dropTabDocuments:intoCurrentTabDocumentsAtIndex:pinned:closeDocument:transitionToDragStateWithBlock:]_block_invoke_4
+ ___118-[TabController _dropTabDocuments:intoCurrentTabDocumentsAtIndex:pinned:closeDocument:transitionToDragStateWithBlock:]_block_invoke_5
+ ___29-[TabOverview layoutSubviews]_block_invoke.113
+ ___29-[TabOverview layoutSubviews]_block_invoke_2.114
+ ___29-[TabOverview layoutSubviews]_block_invoke_3.115
+ ___29-[TabOverview layoutSubviews]_block_invoke_4.116
+ ___32-[BrowserController closeWindow]_block_invoke.729
+ ___32-[BrowserController closeWindow]_block_invoke.729.cold.1
+ ___32-[TabDocument _runURLClassifier]_block_invoke.634
+ ___32-[TabDocument _runURLClassifier]_block_invoke.634.cold.1
+ ___34-[TabDocument _showDownload:path:]_block_invoke.281
+ ___34-[TabDocument _showDownload:path:]_block_invoke.288.cold.1
+ ___34-[TabDocument _showDownload:path:]_block_invoke.289
+ ___36-[LibraryViewController viewDidLoad]_block_invoke_6
+ ___41-[StartPageController _highlightsSection]_block_invoke.272
+ ___41-[StartPageController _highlightsSection]_block_invoke_2.277
+ ___41-[StartPageController _highlightsSection]_block_invoke_3.278
+ ___41-[StartPageController _highlightsSection]_block_invoke_4.280
+ ___41-[StartPageController _highlightsSection]_block_invoke_5.281
+ ___42+[SFTabOverviewItemContentView initialize]_block_invoke
+ ___43-[CloudTabStore synchronizeCloudTabDevices]_block_invoke.54
+ ___44-[URLCompletionProvider setQueryToComplete:]_block_invoke.197
+ ___46-[Application _updateCloudFeatureAvailability]_block_invoke.302
+ ___46-[Application _updateCloudFeatureAvailability]_block_invoke_2.304
+ ___46-[Application _updateCloudFeatureAvailability]_block_invoke_2.304.cold.1
+ ___47-[SearchSuggestionProvider setQueryToComplete:]_block_invoke.234
+ ___47-[SearchSuggestionProvider setQueryToComplete:]_block_invoke_2.235
+ ___47-[SearchSuggestionProvider setQueryToComplete:]_block_invoke_3.236
+ ___48-[TabController _updateTabDocumentsForTabGroup:]_block_invoke.430
+ ___48-[TabController _updateTabDocumentsForTabGroup:]_block_invoke.432
+ ___48-[TabController _updateTabDocumentsForTabGroup:]_block_invoke.434
+ ___50-[SFTabOverviewItemContentView setMediaStateIcon:]_block_invoke
+ ___52-[BrowserWindowController windowForSceneID:options:]_block_invoke.45
+ ___53-[SFTabOverviewItemContentView setShareParticipants:]_block_invoke
+ ___56-[Application prewarmAndRemoveOrphanedProfileDataStores]_block_invoke.221
+ ___56-[Application prewarmAndRemoveOrphanedProfileDataStores]_block_invoke.221.cold.1
+ ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.900
+ ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.903
+ ___57-[ReadingListViewController contentSizeCategoryDidChange]_block_invoke
+ ___60-[Application _saveFrequentlyVisitedListsToDatabaseIfNeeded]_block_invoke
+ ___60-[Application _saveFrequentlyVisitedListsToDatabaseIfNeeded]_block_invoke.77
+ ___60-[Application _saveFrequentlyVisitedListsToDatabaseIfNeeded]_block_invoke.cold.1
+ ___60-[Application _saveFrequentlyVisitedListsToDatabaseIfNeeded]_block_invoke_2
+ ___60-[BookmarksBarView _repositionBookmarksNavigationController]_block_invoke
+ ___60-[BookmarksTableViewController contentSizeCategoryDidChange]_block_invoke
+ ___60-[StartPageController _setUpContextMenuForBookmarksSection:]_block_invoke_6
+ ___62-[BrowserWindowController _mergeWindowStates:intoWindowState:]_block_invoke.72
+ ___63-[BrowserController toggleBookmarksPresentationWithCollection:]_block_invoke
+ ___63-[BrowserWindowController updateCloudTabsForEnteringBackground]_block_invoke.23
+ ___63-[TabSnapshotCache _requestNextSnapshotIfNecessaryForDelegate:]_block_invoke.158
+ ___66-[BrowserRootViewController _turnOnLockedPrivateBrowsingFromSheet]_block_invoke
+ ___70-[SFFluidTabOverviewViewController enumerateItemsOrderedByVisibility:]_block_invoke
+ ___71-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestoration:]_block_invoke.35
+ ___73-[TabDocument _presentTranslationConsentAlertWithType:completionHandler:]_block_invoke.633
+ ___75-[BrowserController addBookmarkNavController:didFinishWithResult:bookmark:]_block_invoke.792
+ ___75-[TabOverview _updateIndexesMatchingSearchAndPerformLayout:includingItems:]_block_invoke.137
+ ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.65
+ ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.65.cold.1
+ ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.65.cold.2
+ ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.65.cold.3
+ ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.65.cold.4
+ ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.65.cold.5
+ ___77-[TabDocument _showFinanceKitOrderPreviewControllerWithURL:dismissalHandler:]_block_invoke.272
+ ___77-[TabGroupSwitcherViewController capsuleCollectionView:didSelectItemAtIndex:]_block_invoke_3
+ ___77-[WBSAnalyticsLogger(SettingsAnalyticsLogger) schedulePeriodicSettingsReport]_block_invoke
+ ___84-[SFFluidTabOverviewDragDropHandler fluidCollectionView:performDropWithCoordinator:]_block_invoke
+ ___84-[SFFluidTabOverviewDragDropHandler fluidCollectionView:performDropWithCoordinator:]_block_invoke_2
+ ___84-[SFFluidTabOverviewDragDropHandler fluidCollectionView:performDropWithCoordinator:]_block_invoke_3
+ ___90-[FrequentlyVisitedSitesController saveFrequentlyVisitedSitesToBookmarksDBWithCompletion:]_block_invoke
+ ___91-[StartPageController startPageCustomizationViewController:didSelectCustomBackgroundImage:]_block_invoke.313
+ ___91-[StartPageController startPageCustomizationViewController:didSelectCustomBackgroundImage:]_block_invoke.313.cold.1
+ ___91-[StartPageController startPageCustomizationViewController:didSelectCustomBackgroundImage:]_block_invoke.314
+ ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke.197
+ ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke.198
+ ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke.208
+ ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke.247
+ ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke.251
+ ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke_2.209
+ ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke_2.257
+ ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke_3.228
+ ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke_3.259
+ ___96-[BrowserController catalogViewController:presentViewControllerWithinPopover:completionHandler:]_block_invoke.138
+ ___97-[CatalogViewController dismissCompletionDetailWindowAndResumeEditingIfNeeded:completionHandler:]_block_invoke.173
+ ___Block_byref_object_copy_.457
+ ___Block_byref_object_copy_.630
+ ___Block_byref_object_dispose_.458
+ ___Block_byref_object_dispose_.631
+ ___block_descriptor_40_e8_32bs_e36_v32?0"<TabCollectionItem>"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_40_e8_32s_e48_v24?0"<TabSnapshotCacheObserving>"8"NSUUID"16ls32l8
+ ___block_descriptor_40_e8_32s_e63_v24?0"UICollectionViewListCell"8"UICellConfigurationState"16ls32l8
+ ___block_descriptor_40_ea8_32s_e63_v32?0?<v?"<NSSecureCoding>""NSError">8#16"NSDictionary"24ls32l8
+ ___block_descriptor_64_e8_32s40s48s56s_e43_"NSArray"24?0"NSArray"8"NSDictionary"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_ea8_32s40s48s56w_e20_v16?0"WBSCGImage"8ls32l8s40l8s48l8w56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72w_e5_v8?0ls32l8s40l8s48l8s56l8s64l8w72l8
+ ___block_descriptor_80_ea8_32s40s48s56w_e20_v16?0"WBSCGImage"8ls32l8s40l8s48l8w56l8
+ ___block_descriptor_82_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
+ ___block_literal_global.110
+ ___block_literal_global.123
+ ___block_literal_global.128
+ ___block_literal_global.140
+ ___block_literal_global.142
+ ___block_literal_global.149
+ ___block_literal_global.159
+ ___block_literal_global.161
+ ___block_literal_global.163
+ ___block_literal_global.164
+ ___block_literal_global.170
+ ___block_literal_global.175
+ ___block_literal_global.183
+ ___block_literal_global.185
+ ___block_literal_global.188
+ ___block_literal_global.204
+ ___block_literal_global.206
+ ___block_literal_global.211
+ ___block_literal_global.212
+ ___block_literal_global.213
+ ___block_literal_global.219
+ ___block_literal_global.221
+ ___block_literal_global.243
+ ___block_literal_global.251
+ ___block_literal_global.2525
+ ___block_literal_global.259
+ ___block_literal_global.277
+ ___block_literal_global.284
+ ___block_literal_global.285
+ ___block_literal_global.286
+ ___block_literal_global.291
+ ___block_literal_global.297
+ ___block_literal_global.298
+ ___block_literal_global.299
+ ___block_literal_global.306
+ ___block_literal_global.313
+ ___block_literal_global.318
+ ___block_literal_global.319
+ ___block_literal_global.325
+ ___block_literal_global.333
+ ___block_literal_global.340
+ ___block_literal_global.355
+ ___block_literal_global.357
+ ___block_literal_global.37
+ ___block_literal_global.45
+ ___block_literal_global.47
+ ___block_literal_global.482
+ ___block_literal_global.491
+ ___block_literal_global.510
+ ___block_literal_global.513
+ ___block_literal_global.525
+ ___block_literal_global.592
+ ___block_literal_global.611
+ ___block_literal_global.626
+ ___block_literal_global.641
+ ___block_literal_global.645
+ ___block_literal_global.653
+ ___block_literal_global.661
+ ___block_literal_global.68
+ ___block_literal_global.687
+ ___block_literal_global.732
+ ___block_literal_global.75
+ ___block_literal_global.77
+ ___block_literal_global.784
+ ___block_literal_global.817
+ ___block_literal_global.821
+ ___block_literal_global.833
+ ___block_literal_global.84
+ ___block_literal_global.853
+ ___block_literal_global.858
+ ___block_literal_global.878
+ ___block_literal_global.890
+ ___block_literal_global.904
+ ___block_literal_global.906
+ ___block_literal_global.908
+ ___block_literal_global.909
+ ___block_literal_global.912
+ ___block_literal_global.94
+ ___internalQueue_block_invoke
+ __unnamed_array_storage.169
+ __unnamed_array_storage.21
+ __unnamed_array_storage.268
+ __unnamed_array_storage.282
+ _abort
+ _internalQueue
+ _internalQueue.internalQueue
+ _internalQueue.onceToken
+ _objc_msgSend$_debugAutoFillConsoleLoggingEnabledPreferenceDidChange:
+ _objc_msgSend$_dragItemsForItemAtIndexPath:session:
+ _objc_msgSend$_effectiveTransitionProgress
+ _objc_msgSend$_enumerateIdentifiersForEntry:respondingToSelector:withBlock:
+ _objc_msgSend$_layOutSubviewsDependentOnContentView
+ _objc_msgSend$_performAdvancedPrivacyProtectionPreferenceReport
+ _objc_msgSend$_performNewTabBehaviorReport
+ _objc_msgSend$_performSyncSuccessesCountReport
+ _objc_msgSend$_saveFrequentlyVisitedListsToDatabaseIfNeeded
+ _objc_msgSend$_settingsAnalyticsLogger_updatePeriodicCoreAnalyticsLastReportTime
+ _objc_msgSend$_updateMaximumContentSizeCategory
+ _objc_msgSend$addTabCollectionItemObserver:
+ _objc_msgSend$attachedView
+ _objc_msgSend$attachedViewReferenceRect
+ _objc_msgSend$attributedTitleForTabGroup:inProfile:primaryColor:secondaryColor:
+ _objc_msgSend$browserContentController
+ _objc_msgSend$browserController:didConnectToScene:session:options:
+ _objc_msgSend$cachedTopBarTheme
+ _objc_msgSend$callStackSymbols
+ _objc_msgSend$canAddTabDocument:toSessionWithDragItems:
+ _objc_msgSend$clearWithCompletionHandler:
+ _objc_msgSend$command
+ _objc_msgSend$contentViewDidLayOutSubviews:
+ _objc_msgSend$currentSearchEngineHostSuffixes
+ _objc_msgSend$didActivateVoiceSearchAccidentally:
+ _objc_msgSend$didEngageWithStartPageSection:
+ _objc_msgSend$didSelectFavoritesRow:
+ _objc_msgSend$donatePageLoadWithUserAgent:wasSearch:wasPrivateBrowsing:wasActualized:provenance:
+ _objc_msgSend$donateSameDocumentNavigationIfNecessary
+ _objc_msgSend$dropTabDocuments:intoCurrentTabDocumentsAtIndex:pinned:transitionToDragStateWithBlock:
+ _objc_msgSend$fluidCollectionView:layout:visibleTopBackdropHeightForItemsInSection:
+ _objc_msgSend$fluidCollectionView:layout:visibleTopBackdropHeightForZoomedItemsInSection:
+ _objc_msgSend$fluidCollectionView:numberOfItemsInSection:
+ _objc_msgSend$headerBackgroundView
+ _objc_msgSend$hostSuffixes
+ _objc_msgSend$indexPathsOfVisibleItems
+ _objc_msgSend$initWithSearchEngineSuggestion:userQuery:forPrivateBrowsing:isOfflineSearchSuggestion:
+ _objc_msgSend$initWithTabGroupManager:activeProfileIdentifier:
+ _objc_msgSend$isSearchEvaluationLoggingEnabled
+ _objc_msgSend$isSearchPage
+ _objc_msgSend$navigationSource
+ _objc_msgSend$nextLoadComesFromSearchPage
+ _objc_msgSend$numberOfTabsToBeClosedForProfilesWithIdentifiers:
+ _objc_msgSend$participantsBackgroundView
+ _objc_msgSend$placeholderView
+ _objc_msgSend$preferredOpenableURL
+ _objc_msgSend$providersMatchingQueryString:excludingSearchEngineHostSuffixes:
+ _objc_msgSend$recordingIndicatorView
+ _objc_msgSend$registerForTraitChanges:withTarget:action:
+ _objc_msgSend$removeTabCollectionItemObserver:
+ _objc_msgSend$reportAdvancedPrivacyProtectionPreference
+ _objc_msgSend$reportCustomizationSyncEnablement:
+ _objc_msgSend$reportNewTabBehavior:
+ _objc_msgSend$reportTabGroupSyncSuccessesWithCount:
+ _objc_msgSend$reportTabUpdatedWithUpdateType:
+ _objc_msgSend$resolvedColor
+ _objc_msgSend$safari_accessingSecurityScopedResource:
+ _objc_msgSend$safari_addObserver:selector:forUserDefaultKey:
+ _objc_msgSend$safari_caseAndDiacriticInsensitiveStandardRangeOfString:additionalOptions:
+ _objc_msgSend$safari_hasFeedScheme
+ _objc_msgSend$safari_hostCompare:
+ _objc_msgSend$safari_isXWebSearchURL
+ _objc_msgSend$safari_monospacedDigitFontForTextStyle:
+ _objc_msgSend$safari_stringByAddingSoftBreaksBeforePeriods
+ _objc_msgSend$safari_stringHasLeadingEmoji:
+ _objc_msgSend$safari_topLevelDomain
+ _objc_msgSend$safari_traitsAffectingTextAppearance
+ _objc_msgSend$safari_urlHashesOfComponents
+ _objc_msgSend$safari_usesWhiteText
+ _objc_msgSend$schedulePeriodicSettingsReport
+ _objc_msgSend$searchProviderForURL:
+ _objc_msgSend$setAutomaticallyAdjustsScrollIndicatorInsets:
+ _objc_msgSend$setCachedTopBarTheme:
+ _objc_msgSend$setEnableDelegateLayoutNotification:
+ _objc_msgSend$setHidesCompletionArrowView:
+ _objc_msgSend$setMinYMatchesTopBarMaxYWhenZoomed:
+ _objc_msgSend$setNSIntegerValue:forTrait:
+ _objc_msgSend$setNextLoadComesFromSearchPage:
+ _objc_msgSend$setSearchURLTemplateFromForm:forSourcePageURLString:completionHandler:
+ _objc_msgSend$setTestController:
+ _objc_msgSend$setTitleRevealPercent:
+ _objc_msgSend$setUsesWebProcessCache:
+ _objc_msgSend$setVisibleTopBackdropHeight:
+ _objc_msgSend$showsLockedPrivateBrowsingView
+ _objc_msgSend$snapshotClipperView
+ _objc_msgSend$snapshotImage
+ _objc_msgSend$symbolImage
+ _objc_msgSend$tabCollectionItemDidChangeIcon:
+ _objc_msgSend$tabCollectionItemDidChangeTitle:
+ _objc_msgSend$tabCollectionViewItemHeaderHeightIncludedInSnapshot:
+ _objc_msgSend$titleRevealPercent
+ _objc_msgSend$titleText
+ _objc_msgSend$titleView
+ _objc_msgSend$topBarTheme
+ _objc_msgSend$topBarThemeForTabOverviewShowingThemeColor:
+ _objc_msgSend$transitionProgress
+ _objc_msgSend$uuidString
+ _objc_msgSend$visibleTopBackdropHeight
- +[BrowserController _sendParsecABTestingEnabledStateToProcessPool:]
- +[NSValue safari_valueWithTabOverviewLocation:]
- +[TabOverviewItemView initialize]
- -[BookmarksBarView _createAllLabelButtonsIfNeededForLayout:]
- -[BookmarksBarView traitCollectionDidChange:]
- -[BookmarksNavigationBar .cxx_destruct]
- -[BookmarksNavigationBar initWithFrame:]
- -[BookmarksNavigationBar layoutSubviews]
- -[BookmarksNavigationBar traitCollectionDidChange:]
- -[BookmarksNavigationController traitCollectionDidChange:]
- -[BookmarksTableViewController tableView:estimatedHeightForHeaderInSection:]
- -[BookmarksTableViewController traitCollectionDidChange:]
- -[BookmarksToolbar .cxx_destruct]
- -[BookmarksToolbar initWithFrame:]
- -[BookmarksToolbar layoutSubviews]
- -[BookmarksToolbar traitCollectionDidChange:]
- -[BrowserController _parsecABGroupIdentifierDidChange:]
- -[BrowserController _parsecBagDidLoad:]
- -[BrowserController toggleBookmarksPresentationWithCollection:completion:]
- -[CatalogViewController traitCollectionDidChange:]
- -[CloudTabStore closeTabs:onDevice:]
- -[DownloadTableViewCell traitCollectionDidChange:]
- -[PageTitleAndAddressTableViewCell traitCollectionDidChange:]
- -[PrivateBrowsingObfuscationViewController traitCollectionDidChange:]
- -[ReadingListTableViewCell _detailLabelFont]
- -[ReadingListTableViewCell _scaledFontForTextStyle:addingSymbolicTraits:]
- -[ReadingListTableViewCell _siteNameFont]
- -[ReadingListTableViewCell _titleLabelFont]
- -[ReadingListTableViewCell dealloc]
- -[ReadingListTableViewCell traitCollectionDidChange:]
- -[ReadingListViewController _separatorEffect]
- -[ReadingListViewController tableView:estimatedHeightForHeaderInSection:]
- -[ReadingListViewController traitCollectionDidChange:]
- -[SFFluidTabOverviewItemView label]
- -[SFFluidTabOverviewItemView setHighlighted:]
- -[SFFluidTabOverviewViewController fluidCollectionView:canHandleDropSession:]
- -[SFFluidTabOverviewViewController fluidCollectionView:itemsForAddingToDragSession:atIndexPath:]
- -[SFFluidTabOverviewViewController fluidCollectionView:itemsForBeginningDragSession:atIndexPath:]
- -[SFFluidTabOverviewViewController fluidCollectionView:performDropWithCoordinator:]
- -[SFFluidTabOverviewViewController itemsFullyInView]
- -[SafariClearBrowsingDataController clearHistoryVisitsAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeAllTabs:]
- -[SearchSuggestion initWithSearchEngineSuggestion:userQuery:forPrivateBrowsing:]
- -[SearchSuggestionTableViewCell hidesAccessoryView]
- -[SearchSuggestionTableViewCell setHidesAccessoryView:]
- -[SearchSuggestionTableViewCell traitCollectionDidChange:]
- -[StartPageController startPageViewController:didSelectItemWithIdentifier:]
- -[StartPageController tabGroupProviderForCustomizationViewController:]
- -[TabController didTransitionTabView]
- -[TabController imageForProfile:]
- -[TabController itemsToKeepVisibleForTabOverview:]
- -[TabController tabOverviewAdditionalItemHeaderHeight:]
- -[TabController tabSnapshotCache:shouldRequestSavedSnapshotWithIdentifier:]
- -[TabController willTransitionTabView]
- -[TabDocument _webView:runWebAuthenticationPanel:initiatedByFrame:completionHandler:]
- -[TabDocument panel:decidePolicyForLocalAuthenticatorWithCompletionHandler:]
- -[TabDocument panel:dismissWebAuthenticationPanelWithResult:]
- -[TabDocument panel:requestPINWithRemainingRetries:completionHandler:]
- -[TabDocument panel:selectAssertionResponse:source:completionHandler:]
- -[TabDocument panel:updateWebAuthenticationPanel:]
- -[TabExplanationView traitCollectionDidChange:]
- -[TabIconAndTitleView traitCollectionDidChange:]
- -[TabOverview itemsFullyInView]
- -[TabOverview traitCollectionDidChange:]
- -[TabOverviewDataSourceAdaptor itemsToKeepVisibleForTabOverview:]
- -[TabOverviewItemView _headerBackgroundColor]
- -[TabOverviewItemView _updateContentSizeCategory]
- -[TabOverviewItemView canBecomeFocused]
- -[TabOverviewItemView effectiveHeaderMode]
- -[TabOverviewItemView focusEffect]
- -[TabOverviewItemView pointInside:withEvent:]
- -[TabOverviewItemView setDimmingView:]
- -[TabOverviewItemView setSnapshotView:]
- -[TabOverviewItemView titleHeight]
- -[TabOverviewItemView titlePadding]
- -[TabOverviewItemView traitCollectionDidChange:]
- -[TabOverviewToolbar traitCollectionDidChange:]
- -[TabSnapshotCache _enumerateDelegatesAndIdentifiersForEntry:usingBlock:]
- -[TabSnapshotCacheStressTestRunner tabSnapshotCache:shouldRequestSavedSnapshotWithIdentifier:]
- -[VibrantLabelView .cxx_destruct]
- -[VibrantLabelView _reduceTransparencyStatusDidChange:]
- -[VibrantLabelView _updateVibrancy]
- -[VibrantLabelView setTextColor:]
- -[VibrantLabelView setUsesVibrantAppearance:]
- -[VibrantLabelView traitCollectionDidChange:]
- GCC_except_table1000
- GCC_except_table1006
- GCC_except_table1007
- GCC_except_table1008
- GCC_except_table1010
- GCC_except_table1021
- GCC_except_table1022
- GCC_except_table1028
- GCC_except_table1030
- GCC_except_table1043
- GCC_except_table1044
- GCC_except_table1046
- GCC_except_table1047
- GCC_except_table1053
- GCC_except_table1055
- GCC_except_table1059
- GCC_except_table1065
- GCC_except_table1068
- GCC_except_table1072
- GCC_except_table1074
- GCC_except_table1088
- GCC_except_table1091
- GCC_except_table1094
- GCC_except_table1097
- GCC_except_table1098
- GCC_except_table1115
- GCC_except_table1121
- GCC_except_table1122
- GCC_except_table1123
- GCC_except_table227
- GCC_except_table323
- GCC_except_table324
- GCC_except_table332
- GCC_except_table339
- GCC_except_table351
- GCC_except_table353
- GCC_except_table370
- GCC_except_table372
- GCC_except_table380
- GCC_except_table392
- GCC_except_table412
- GCC_except_table436
- GCC_except_table437
- GCC_except_table442
- GCC_except_table460
- GCC_except_table461
- GCC_except_table484
- GCC_except_table487
- GCC_except_table489
- GCC_except_table499
- GCC_except_table530
- GCC_except_table534
- GCC_except_table540
- GCC_except_table576
- GCC_except_table588
- GCC_except_table592
- GCC_except_table615
- GCC_except_table622
- GCC_except_table643
- GCC_except_table650
- GCC_except_table659
- GCC_except_table660
- GCC_except_table675
- GCC_except_table703
- GCC_except_table717
- GCC_except_table721
- GCC_except_table724
- GCC_except_table743
- GCC_except_table746
- GCC_except_table753
- GCC_except_table759
- GCC_except_table762
- GCC_except_table766
- GCC_except_table771
- GCC_except_table799
- GCC_except_table802
- GCC_except_table808
- GCC_except_table824
- GCC_except_table827
- GCC_except_table831
- GCC_except_table834
- GCC_except_table837
- GCC_except_table843
- GCC_except_table856
- GCC_except_table863
- GCC_except_table876
- GCC_except_table884
- GCC_except_table896
- GCC_except_table900
- GCC_except_table902
- GCC_except_table906
- GCC_except_table908
- GCC_except_table918
- GCC_except_table919
- GCC_except_table920
- GCC_except_table921
- GCC_except_table932
- GCC_except_table933
- GCC_except_table935
- GCC_except_table939
- GCC_except_table965
- GCC_except_table967
- GCC_except_table971
- GCC_except_table982
- GCC_except_table983
- GCC_except_table994
- GCC_except_table996
- _CGRectContainsRect
- _OBJC_CLASS_$_BookmarksNavigationBar
- _OBJC_CLASS_$_BookmarksToolbar
- _OBJC_CLASS_$_SFVibrantSeparatorView
- _OBJC_CLASS_$_UINavigationBar
- _OBJC_CLASS_$_VibrantLabelView
- _OBJC_IVAR_$_BookmarksNavigationBar._separator
- _OBJC_IVAR_$_BookmarksToolbar._separatorView
- _OBJC_IVAR_$_CloudTabStore._internalQueue
- _OBJC_IVAR_$_SFFluidTabOverviewItemView._borrowedContentView
- _OBJC_IVAR_$_SFFluidTabOverviewItemView._borrowedContentViewContainer
- _OBJC_IVAR_$_SFFluidTabOverviewItemView._deleteButton
- _OBJC_IVAR_$_SFFluidTabOverviewItemView._deleteButtonConstraints
- _OBJC_IVAR_$_SFFluidTabOverviewItemView._highlightView
- _OBJC_IVAR_$_SFFluidTabOverviewItemView._label
- _OBJC_IVAR_$_SearchSuggestionTableViewCell._accessoryView
- _OBJC_IVAR_$_SearchSuggestionTableViewCell._hidesAccessoryView
- _OBJC_IVAR_$_TabController._switchingActiveDocument
- _OBJC_IVAR_$_TabController._tabDocumentsToKeepVisible
- _OBJC_IVAR_$_TabOverviewItemView._attachedView
- _OBJC_IVAR_$_TabOverviewItemView._attachedViewReferenceRect
- _OBJC_IVAR_$_TabOverviewItemView._borrowedContentView
- _OBJC_IVAR_$_TabOverviewItemView._closeButton
- _OBJC_IVAR_$_TabOverviewItemView._contentSizeIsAccessibilityCategory
- _OBJC_IVAR_$_TabOverviewItemView._dimmingView
- _OBJC_IVAR_$_TabOverviewItemView._headerBackgroundView
- _OBJC_IVAR_$_TabOverviewItemView._mediaStateIcon
- _OBJC_IVAR_$_TabOverviewItemView._participantsBackgroundView
- _OBJC_IVAR_$_TabOverviewItemView._participantsView
- _OBJC_IVAR_$_TabOverviewItemView._placeholderView
- _OBJC_IVAR_$_TabOverviewItemView._preferredHeaderMode
- _OBJC_IVAR_$_TabOverviewItemView._recording
- _OBJC_IVAR_$_TabOverviewItemView._recordingIndicatorView
- _OBJC_IVAR_$_TabOverviewItemView._snapshotClipperView
- _OBJC_IVAR_$_TabOverviewItemView._snapshotView
- _OBJC_IVAR_$_TabOverviewItemView._titleHeight
- _OBJC_IVAR_$_TabOverviewItemView._titleView
- _OBJC_IVAR_$_TabOverviewItemView._topBarTheme
- _OBJC_IVAR_$_VibrantLabelView._nonVibrantTextColor
- _OBJC_IVAR_$_VibrantLabelView._usesVibrantAppearance
- _OBJC_METACLASS_$_BookmarksNavigationBar
- _OBJC_METACLASS_$_BookmarksToolbar
- _OBJC_METACLASS_$_UILabel
- _OBJC_METACLASS_$_UINavigationBar
- _OBJC_METACLASS_$_UIToolbar
- _OBJC_METACLASS_$_VibrantLabelView
- _SafariLegacyRecentSearchPath
- _UIAccessibilityIsReduceTransparencyEnabled
- _UIAccessibilityReduceTransparencyStatusDidChangeNotification
- _UIContentSizeCategoryUnspecified
- _UIFontTextStyleSubheadline1
- _WBSChromeExtensionURLScheme
- _WBSParsecDSessionDidLoadBagNotification
- _WBSWebProcessPlugInParsecABTestingEnabledKey
- __OBJC_$_CLASS_METHODS_TabOverviewItemView
- __OBJC_$_INSTANCE_METHODS_BookmarksNavigationBar
- __OBJC_$_INSTANCE_METHODS_BookmarksToolbar
- __OBJC_$_INSTANCE_METHODS_VibrantLabelView
- __OBJC_$_INSTANCE_METHODS_WBSAnalyticsLogger(TabGroupsAnalyticsLogger|PrivateBrowsingAnalyticsLogger|StandaloneTabBarAnalyticsLogger)
- __OBJC_$_INSTANCE_VARIABLES_BookmarksNavigationBar
- __OBJC_$_INSTANCE_VARIABLES_BookmarksToolbar
- __OBJC_$_INSTANCE_VARIABLES_VibrantLabelView
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TabOverviewDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__WKWebAuthenticationPanelDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TabSnapshotCacheObserving
- __OBJC_$_PROTOCOL_METHOD_TYPES__WKWebAuthenticationPanelDelegate
- __OBJC_$_PROTOCOL_REFS__WKWebAuthenticationPanelDelegate
- __OBJC_CLASS_RO_$_BookmarksNavigationBar
- __OBJC_CLASS_RO_$_BookmarksToolbar
- __OBJC_CLASS_RO_$_VibrantLabelView
- __OBJC_LABEL_PROTOCOL_$__WKWebAuthenticationPanelDelegate
- __OBJC_METACLASS_RO_$_BookmarksNavigationBar
- __OBJC_METACLASS_RO_$_BookmarksToolbar
- __OBJC_METACLASS_RO_$_VibrantLabelView
- __OBJC_PROTOCOL_$__WKWebAuthenticationPanelDelegate
- __ZN3WTF9RetainPtrIP7CGImageED1Ev
- ___108-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestorationIfNeededAfterCloudTabsFinishedSyncing:]_block_invoke.27
- ___116-[URLCompletionDatabase enumerateMatchDataForTypedStringHint:filterResultsUsingProfileIdentifier:options:withBlock:]_block_invoke.267
- ___116-[URLCompletionDatabase enumerateMatchDataForTypedStringHint:filterResultsUsingProfileIdentifier:options:withBlock:]_block_invoke_2.270
- ___29-[TabOverview layoutSubviews]_block_invoke.107
- ___29-[TabOverview layoutSubviews]_block_invoke_2.108
- ___29-[TabOverview layoutSubviews]_block_invoke_3.109
- ___29-[TabOverview layoutSubviews]_block_invoke_4.110
- ___31-[TabOverview itemsFullyInView]_block_invoke
- ___32-[BrowserController closeWindow]_block_invoke.731
- ___32-[BrowserController closeWindow]_block_invoke.731.cold.1
- ___32-[TabDocument _runURLClassifier]_block_invoke.633
- ___32-[TabDocument _runURLClassifier]_block_invoke.633.cold.1
- ___33+[TabOverviewItemView initialize]_block_invoke
- ___34-[TabDocument _showDownload:path:]_block_invoke.280
- ___34-[TabDocument _showDownload:path:]_block_invoke.287
- ___34-[TabDocument _showDownload:path:]_block_invoke.287.cold.1
- ___38-[TabController willTransitionTabView]_block_invoke
- ___39-[BrowserController _parsecBagDidLoad:]_block_invoke
- ___41-[StartPageController _highlightsSection]_block_invoke.269
- ___41-[StartPageController _highlightsSection]_block_invoke_2.274
- ___41-[StartPageController _highlightsSection]_block_invoke_3.276
- ___41-[StartPageController _highlightsSection]_block_invoke_4.277
- ___41-[TabOverviewItemView setMediaStateIcon:]_block_invoke
- ___43-[CloudTabStore synchronizeCloudTabDevices]_block_invoke.55
- ___44-[BrowserController editBookmarksKeyPressed]_block_invoke
- ___44-[TabOverviewItemView setShareParticipants:]_block_invoke
- ___44-[URLCompletionProvider setQueryToComplete:]_block_invoke.195
- ___45-[TabOverview _targetLocationForPresentation]_block_invoke
- ___46-[Application _updateCloudFeatureAvailability]_block_invoke.298
- ___46-[Application _updateCloudFeatureAvailability]_block_invoke_2.300
- ___46-[Application _updateCloudFeatureAvailability]_block_invoke_2.300.cold.1
- ___47-[SearchSuggestionProvider setQueryToComplete:]_block_invoke.227
- ___47-[SearchSuggestionProvider setQueryToComplete:]_block_invoke_2.228
- ___47-[SearchSuggestionProvider setQueryToComplete:]_block_invoke_3.229
- ___48-[TabController _updateTabDocumentsForTabGroup:]_block_invoke.435
- ___48-[TabController _updateTabDocumentsForTabGroup:]_block_invoke.437
- ___48-[TabController _updateTabDocumentsForTabGroup:]_block_invoke.439
- ___50-[TabController itemsToKeepVisibleForTabOverview:]_block_invoke
- ___51-[Application databaseLockAcquisitor:acquiredLock:]_block_invoke_3
- ___52-[BrowserWindowController windowForSceneID:options:]_block_invoke.44
- ___54-[ReadingListViewController traitCollectionDidChange:]_block_invoke
- ___56-[Application prewarmAndRemoveOrphanedProfileDataStores]_block_invoke.217
- ___56-[Application prewarmAndRemoveOrphanedProfileDataStores]_block_invoke.217.cold.1
- ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.901
- ___56-[BrowserController scene:willConnectToSession:options:]_block_invoke.905
- ___57-[BookmarksTableViewController traitCollectionDidChange:]_block_invoke
- ___59-[BookmarksBarView bookmarksNavigationControllerDidReload:]_block_invoke
- ___62-[BrowserWindowController _mergeWindowStates:intoWindowState:]_block_invoke.71
- ___63+[ToolbarItemConfiguration configurationForTabGroup:inProfile:]_block_invoke
- ___63-[BrowserWindowController updateCloudTabsForEnteringBackground]_block_invoke.22
- ___63-[TabSnapshotCache _requestNextSnapshotIfNecessaryForDelegate:]_block_invoke.154
- ___71-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestoration:]_block_invoke.34
- ___73-[TabDocument _presentTranslationConsentAlertWithType:completionHandler:]_block_invoke.632
- ___74-[BrowserController toggleBookmarksPresentationWithCollection:completion:]_block_invoke
- ___74-[BrowserController toggleBookmarksPresentationWithCollection:completion:]_block_invoke.820
- ___74-[BrowserController toggleBookmarksPresentationWithCollection:completion:]_block_invoke_2
- ___75-[BrowserController addBookmarkNavController:didFinishWithResult:bookmark:]_block_invoke.794
- ___75-[TabOverview _updateIndexesMatchingSearchAndPerformLayout:includingItems:]_block_invoke.133
- ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.68
- ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.68.cold.1
- ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.68.cold.2
- ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.68.cold.3
- ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.68.cold.4
- ___76-[CloudTabStore saveCurrentDeviceCloudTabsForEnteringBackground:completion:]_block_invoke.68.cold.5
- ___77-[TabDocument _showFinanceKitOrderPreviewControllerWithURL:dismissalHandler:]_block_invoke.271
- ___91-[StartPageController startPageCustomizationViewController:didSelectCustomBackgroundImage:]_block_invoke.310
- ___91-[StartPageController startPageCustomizationViewController:didSelectCustomBackgroundImage:]_block_invoke.310.cold.1
- ___91-[StartPageController startPageCustomizationViewController:didSelectCustomBackgroundImage:]_block_invoke.311
- ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke.194
- ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke.195
- ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke.205
- ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke.244
- ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke.245
- ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke_2.206
- ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke_2.254
- ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke_3.225
- ___94-[ReadingListViewController _createAction:forRowAtIndexPath:allowingNewlineInTitle:withBlock:]_block_invoke_3.256
- ___95-[TabController replacePlaceholderTabDocument:withTabDocuments:transitionToDragStateWithBlock:]_block_invoke
- ___95-[TabController replacePlaceholderTabDocument:withTabDocuments:transitionToDragStateWithBlock:]_block_invoke_2
- ___95-[TabController replacePlaceholderTabDocument:withTabDocuments:transitionToDragStateWithBlock:]_block_invoke_3
- ___95-[TabController replacePlaceholderTabDocument:withTabDocuments:transitionToDragStateWithBlock:]_block_invoke_4
- ___95-[TabController replacePlaceholderTabDocument:withTabDocuments:transitionToDragStateWithBlock:]_block_invoke_5
- ___96-[BrowserController catalogViewController:presentViewControllerWithinPopover:completionHandler:]_block_invoke.140
- ___97-[CatalogViewController dismissCompletionDetailWindowAndResumeEditingIfNeeded:completionHandler:]_block_invoke.170
- ___Block_byref_object_copy_.456
- ___Block_byref_object_copy_.629
- ___Block_byref_object_dispose_.457
- ___Block_byref_object_dispose_.630
- ___block_descriptor_32_e38_"TabOverviewItem"16?0"TabDocument"8l
- ___block_descriptor_40_e8_32s_e25_16?0"TabOverviewItem"8ls32l8
- ___block_descriptor_40_e8_32s_e27_v40?08{_NSRange=QQ}16^B32ls32l8
- ___block_descriptor_40_e8_32s_e47_v24?0"<TabSnapshotCacheDelegate>"8"NSUUID"16ls32l8
- ___block_descriptor_40_ea8_32c31_ZTSN3WTF9RetainPtrIP7CGImageEE_e63_v32?0?<v?"<NSSecureCoding>""NSError">8#16"NSDictionary"24l
- ___block_descriptor_50_ea8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e25_B16?0"TabOverviewItem"8l
- ___block_descriptor_72_e8_32s40s48s56s64w_e5_v8?0ls32l8s40l8s48l8s56l8w64l8
- ___block_descriptor_72_ea8_32s40s48s56w_e32_v16?0{RetainPtr<CGImage *>=^v}8ls32l8s40l8s48l8w56l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_ea8_32s40s48s56w72c31_ZTSN3WTF9RetainPtrIP7CGImageEE_e5_v8?0l
- ___block_descriptor_80_ea8_32s40s48s56w_e32_v16?0{RetainPtr<CGImage *>=^v}8ls32l8s40l8s48l8w56l8
- ___block_literal_global.119
- ___block_literal_global.145
- ___block_literal_global.158
- ___block_literal_global.162
- ___block_literal_global.169
- ___block_literal_global.177
- ___block_literal_global.179
- ___block_literal_global.187
- ___block_literal_global.203
- ___block_literal_global.205
- ___block_literal_global.208
- ___block_literal_global.209
- ___block_literal_global.218
- ___block_literal_global.227
- ___block_literal_global.245
- ___block_literal_global.246
- ___block_literal_global.2514
- ___block_literal_global.258
- ___block_literal_global.263
- ___block_literal_global.273
- ___block_literal_global.280
- ___block_literal_global.282
- ___block_literal_global.289
- ___block_literal_global.295
- ___block_literal_global.300
- ___block_literal_global.302
- ___block_literal_global.309
- ___block_literal_global.311
- ___block_literal_global.317
- ___block_literal_global.321
- ___block_literal_global.329
- ___block_literal_global.336
- ___block_literal_global.339
- ___block_literal_global.353
- ___block_literal_global.36
- ___block_literal_global.42
- ___block_literal_global.487
- ___block_literal_global.493
- ___block_literal_global.515
- ___block_literal_global.518
- ___block_literal_global.524
- ___block_literal_global.53
- ___block_literal_global.591
- ___block_literal_global.613
- ___block_literal_global.625
- ___block_literal_global.640
- ___block_literal_global.644
- ___block_literal_global.649
- ___block_literal_global.663
- ___block_literal_global.67
- ___block_literal_global.689
- ___block_literal_global.70
- ___block_literal_global.734
- ___block_literal_global.74
- ___block_literal_global.786
- ___block_literal_global.819
- ___block_literal_global.824
- ___block_literal_global.836
- ___block_literal_global.85
- ___block_literal_global.856
- ___block_literal_global.86
- ___block_literal_global.861
- ___block_literal_global.881
- ___block_literal_global.888
- ___block_literal_global.893
- ___block_literal_global.894
- ___block_literal_global.896
- ___block_literal_global.899
- ___block_literal_global.900
- ___block_literal_global.903
- ___block_literal_global.97
- ___block_literal_global.99
- ___copy_helper_block_ea8_32c31_ZTSN3WTF9RetainPtrIP7CGImageEE
- ___copy_helper_block_ea8_72c31_ZTSN3WTF9RetainPtrIP7CGImageEE
- ___destroy_helper_block_ea8_32c31_ZTSN3WTF9RetainPtrIP7CGImageEE
- ___destroy_helper_block_ea8_72c31_ZTSN3WTF9RetainPtrIP7CGImageEE
- __unnamed_array_storage.166
- __unnamed_array_storage.264
- __unnamed_array_storage.279
- _kCAFilterVibrantDark
- _kCAFilterVibrantLight
- _objc_msgSend$_detailLabelFont
- _objc_msgSend$_enumerateDelegatesAndIdentifiersForEntry:usingBlock:
- _objc_msgSend$_scaledFontForTextStyle:addingSymbolicTraits:
- _objc_msgSend$_separatorEffect
- _objc_msgSend$_sf_accessingSecurityScopedResource:
- _objc_msgSend$_sf_topLevelDomain
- _objc_msgSend$_siteNameFont
- _objc_msgSend$_titleLabelFont
- _objc_msgSend$_vibrantLightDividerBurnColor
- _objc_msgSend$_vibrantLightDividerDarkeningColor
- _objc_msgSend$authenticatorDialogForPanel:dialogController:
- _objc_msgSend$clear
- _objc_msgSend$constraintEqualToSystemSpacingAfterAnchor:multiplier:
- _objc_msgSend$decidePolicyForLocalAuthenticatorWithCompletionHandler:
- _objc_msgSend$defaultFontDescriptorWithTextStyle:addingSymbolicTraits:options:
- _objc_msgSend$effectForBlurEffect:
- _objc_msgSend$enumerateAttribute:inRange:options:usingBlock:
- _objc_msgSend$grayColor
- _objc_msgSend$imageForProfile:
- _objc_msgSend$initWithPathToLegacySearchesFile:
- _objc_msgSend$initWithSearchEngineSuggestion:userQuery:forPrivateBrowsing:
- _objc_msgSend$itemsFullyInView
- _objc_msgSend$itemsToKeepVisibleForTabOverview:
- _objc_msgSend$label
- _objc_msgSend$localizedAttributedStringWithFormat:
- _objc_msgSend$monospacedDigitSystemFontOfSize:weight:
- _objc_msgSend$panel
- _objc_msgSend$presentedAuthenticatorDialog
- _objc_msgSend$providersMatchingQueryString:
- _objc_msgSend$requestPINWithRemainingRetries:completionHandler:
- _objc_msgSend$safari_favoritesTitleWithEmojiForRTL:
- _objc_msgSend$safari_objectBefore:
- _objc_msgSend$scaledFontForFont:compatibleWithTraitCollection:
- _objc_msgSend$scaledValueForValue:compatibleWithTraitCollection:
- _objc_msgSend$selectAssertionResponse:source:completionHandler:
- _objc_msgSend$setBackgroundImage:forBarMetrics:
- _objc_msgSend$setBackgroundImage:forToolbarPosition:barMetrics:
- _objc_msgSend$setHidesAccessoryView:
- _objc_msgSend$setIsForUpdateOnly:
- _objc_msgSend$setOverrideTraitCollection:forChildViewController:
- _objc_msgSend$setSearchURLTemplateFromForm:forSourcePageURLString:
- _objc_msgSend$setShadowImage:
- _objc_msgSend$setShadowImage:forToolbarPosition:
- _objc_msgSend$setSymbolImageName:
- _objc_msgSend$sf_backgroundBlurEffect
- _objc_msgSend$sf_hasSameTextAppearanceAs:
- _objc_msgSend$sf_isFeedScheme
- _objc_msgSend$sf_isWebSearchURL
- _objc_msgSend$sf_stringByAddingSoftBreaksBeforePeriods
- _objc_msgSend$sf_traitCollectionUsingVibrantAppearance
- _objc_msgSend$sf_traitCollectionWithSidebarPresentation:
- _objc_msgSend$tabOverviewAdditionalItemHeaderHeight:
- _objc_msgSend$tabSnapshotCache:shouldRequestSavedSnapshotWithIdentifier:
- _objc_msgSend$traitCollectionWithPreferredContentSizeCategory:
- _objc_msgSend$traitCollectionWithTraitsFromCollections:
- _objc_msgSend$updateWebAuthenticationPanel:
- _objc_msgSend$value:withObjCType:
- _preferredHeaderModeForSnapshot
- _resolvedContentSizeCategoryForTraitCollection
CStrings:
+ "\x01\x12\x11"
+ "\x01#\x12!B\x12\x15\x1b\x131A\x12C\x11\x15\x16D\x17\x18\x14"
+ "\x01\xf0\xf0\xf0b"
+ "\x02\x14\x13\x11!2"
+ "\x03\x11"
+ "\v\x11S1"
+ "\x11\x15\x14\x14\x1c\x15\x12\x11\x13"
+ "\x13\x11\x11\x11\x11"
+ "\x15\x12\x13!\x11\x15#\"#\x13\x11\x15\x11C"
+ "!q\xa1\xf0a\x11\x11\xf0\xf0!\xf0a"
+ "%@\n%@"
+ "%@: "
+ "%@[%@], "
+ ", %@"
+ "-[BrowserController _debugAutoFillConsoleLoggingEnabledPreferenceDidChange:]"
+ ".*\x11\x1d\x19\x11'\x11\x11\x12\x11\x141\"T\x17\x11j\x12!\x13\x13?\x02\x19&"
+ "/Library/Caches/com.apple.xbs/Sources/Safari/iOS/MobileSafari/BrowserController.mm"
+ "<%@ %p: UUID = %@; title = %@>"
+ "@\"<SFStartPageCustomizationProfileProviding>\"24@0:8@\"SFStartPageCustomizationViewController\"16"
+ "@\"<SFTabOverviewItemContentViewDelegate>\""
+ "@\"SFFluidTabOverviewDragDropHandler\""
+ "@\"SFTabOverviewItemContentView\""
+ "@44@0:8@16Q24B32@?36"
+ "ASSERTION FAILURE: \"%s\" in %s, %@:%d%@"
+ "Active tab document is not present in the list of tab documents; private browsing enabled: %{public}@"
+ "Background task expired while waiting for MobileSafari to save frequently visited sites."
+ "E\x11"
+ "LastPeriodicSettingsReportTime"
+ "Parsec TopHit <%{public}@> query:\"%@\""
+ "Q32@0:8@\"SFClearHistoryViewController\"16@\"NSSet\"24"
+ "SFFluidTabOverviewDragDropHandler"
+ "SFFluidTabOverviewZoomableGridLayoutDelegate"
+ "SFStartPageCustomizationProfileProviding"
+ "SFTabOverviewItemContentView"
+ "SFTabOverviewItemContentViewDelegate"
+ "SafariCompletionListOfflineSearchEngineSuggestion"
+ "SettingsAnalyticsLogger"
+ "Skipped generating feedback for cell at %@ due to nil completion list item"
+ "StartPageSectionClearAllButton"
+ "T@\"<SFTabOverviewItemContentViewDelegate>\",W,N,V_delegate"
+ "T@\"<TabCollectionItem>\",&,N,V_item"
+ "T@\"SFFluidTabOverviewDataSource\",R,N,V_dataSource"
+ "T@\"SFFluidTabOverviewViewController\",W,N,V_fluidTabOverviewViewController"
+ "T@\"TabIconAndTitleView\",R,N,V_titleView"
+ "T@\"UIView\",R,N,V_headerBackgroundView"
+ "T@\"UIView\",R,N,V_participantsBackgroundView"
+ "T@\"UIView\",R,N,V_placeholderView"
+ "T@\"UIView\",R,N,V_recordingIndicatorView"
+ "T@\"UIView\",R,N,V_snapshotClipperView"
+ "T@\"_SFBarTheme\",&,N"
+ "T@\"_SFBarTheme\",&,N,V_cachedTopBarTheme"
+ "T@?,C,N,Stest_setMetadataHandler:,V_test_metadataHandler"
+ "TB,N,GisRecording"
+ "TB,N,V_enableDelegateLayoutNotification"
+ "TB,N,V_focusProfileUpdateIsForInactiveFocusMode"
+ "TB,N,V_hidesCompletionArrowView"
+ "TB,N,V_minYMatchesTopBarMaxYWhenZoomed"
+ "TB,N,V_nextLoadComesFromSearchPage"
+ "TB,R,N,GisSearchPage"
+ "TabCollectionItemObserving"
+ "Td,N,V_shadowOpacity"
+ "Td,N,V_titleRevealPercent"
+ "Td,N,V_visibleTopBackdropHeight"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N"
+ "User typed string is nil for query: %{sensitive}@"
+ "WBSFeatureAvailability.isInternalInstall"
+ "_ABGroupIdentifierDidChange:"
+ "_SFFormAutoFillTestController"
+ "_cachedTopBarTheme"
+ "_completionArrowView"
+ "_debugAutoFillConsoleLoggingEnabledPreferenceDidChange:"
+ "_didChangeHorizontalSizeClass"
+ "_dragDropHandler"
+ "_dragItemsForItemAtIndexPath:session:"
+ "_effectiveTransitionProgress"
+ "_enableDelegateLayoutNotification"
+ "_enumerateIdentifiersForEntry:respondingToSelector:withBlock:"
+ "_focusProfileUpdateIsForInactiveFocusMode"
+ "_hidesCompletionArrowView"
+ "_isPerformingLayout"
+ "_item"
+ "_lastBottomInset"
+ "_lastVisibleIndexPaths"
+ "_layOutSubviewsDependentOnContentView"
+ "_minYMatchesTopBarMaxYWhenZoomed"
+ "_needsRepositionNavigationController"
+ "_nextLoadComesFromSearchPage"
+ "_offlineSearchEngineSuggestion"
+ "_performAdvancedPrivacyProtectionPreferenceReport"
+ "_performNewTabBehaviorReport"
+ "_performSyncSuccessesCountReport"
+ "_preferredContentSizeCategoryDidChange"
+ "_preferredContentSizeCategoryDidChange:previousTraitCollection:"
+ "_saveFrequentlyVisitedListsToDatabaseIfNeeded"
+ "_setNeedsResizeHeaderItems"
+ "_setNeedsResizeItems"
+ "_settingsAnalyticsLogger_updatePeriodicCoreAnalyticsLastReportTime"
+ "_shadowOpacity"
+ "_shouldDonatePageLoad"
+ "_shouldUpdateSnapshotsForTabSwitch"
+ "_test_metadataHandler"
+ "_titleRevealPercent"
+ "_updateMaximumContentSizeCategory"
+ "_visibleTopBackdropHeight"
+ "_wasPageLoadUserInitiated"
+ "addTabCollectionItemObserver:"
+ "anySizeClassDidChange"
+ "attributedTitleForTabGroup:inProfile:primaryColor:secondaryColor:"
+ "autoFillController:didCollectFormMetadataForTesting:forURL:"
+ "autoFillControllerShouldCollectFormMetadataForTesting:"
+ "browserContentController"
+ "browserController:didConnectToScene:session:options:"
+ "cachedTopBarTheme"
+ "callStackSymbols"
+ "canAddTabDocument:toSessionWithDragItems:"
+ "clearHistoryViewController:clearHistoryVisitsAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeAllTabs:"
+ "clearHistoryViewController:numberOfTabsToBeClosedForProfilesWithIdentifiers:"
+ "clearWithCompletionHandler:"
+ "com.apple.mobilesafari.PerformFrequentlyVisitedSitesTasks"
+ "command"
+ "contentViewClass"
+ "contentViewDidLayOutSubviews:"
+ "currentSearchEngineHostSuffixes"
+ "d40@0:8@\"SFFluidCollectionView\"16@\"SFFluidTabOverviewZoomableGridLayout\"24Q32"
+ "didActivateVoiceSearchAccidentally:"
+ "didEngageWithStartPageSection:"
+ "didSelectFavoritesRow:"
+ "donatePageLoadWithUserAgent:wasSearch:wasPrivateBrowsing:wasActualized:provenance:"
+ "donateSameDocumentNavigationIfNecessary"
+ "dropTabDocuments:intoCurrentTabDocumentsAtIndex:pinned:transitionToDragStateWithBlock:"
+ "enableDelegateLayoutNotification"
+ "fluidCollectionView:didEndDisplayingView:forItemAtIndexPath:"
+ "fluidCollectionView:layout:visibleTopBackdropHeightForItemsInSection:"
+ "fluidCollectionView:layout:visibleTopBackdropHeightForZoomedItemsInSection:"
+ "fluidCollectionView:willDisplayView:forItemAtIndexPath:"
+ "fluidTabOverviewViewController"
+ "focusProfileUpdateIsForInactiveFocusMode"
+ "headerBackgroundView"
+ "hidesCompletionArrowView"
+ "horizontalSizeClassDidChange:previousTraitCollection:"
+ "hostSuffixes"
+ "indexPathsOfVisibleItems"
+ "initWithSearchEngineSuggestion:userQuery:forPrivateBrowsing:isOfflineSearchSuggestion:"
+ "initWithTabGroupManager:activeProfileIdentifier:"
+ "isSearchEvaluationLoggingEnabled"
+ "isSearchPage"
+ "minYMatchesTopBarMaxYWhenZoomed"
+ "navigationSource"
+ "nextLoadComesFromSearchPage"
+ "numberOfTabsToBeClosedForProfilesWithIdentifiers:"
+ "participantsBackgroundView"
+ "placeholderView"
+ "preferredContentSizeCategoryDidChange"
+ "preferredOpenableURL"
+ "profileProviderForCustomizationViewController:"
+ "providersMatchingQueryString:excludingSearchEngineHostSuffixes:"
+ "recordingIndicatorView"
+ "registerForTraitChanges:withTarget:action:"
+ "removeTabCollectionItemObserver:"
+ "reportAdvancedPrivacyProtectionPreference"
+ "reportCustomizationSyncEnablement:"
+ "reportNewTabBehavior:"
+ "reportTabGroupSyncSuccessesWithCount:"
+ "reportTabUpdatedWithUpdateType:"
+ "resolvedColor"
+ "safari_accessingSecurityScopedResource:"
+ "safari_addObserver:selector:forUserDefaultKey:"
+ "safari_caseAndDiacriticInsensitiveStandardRangeOfString:additionalOptions:"
+ "safari_hasFeedScheme"
+ "safari_hostCompare:"
+ "safari_isXWebSearchURL"
+ "safari_monospacedDigitFontForTextStyle:"
+ "safari_stringByAddingSoftBreaksBeforePeriods"
+ "safari_stringHasLeadingEmoji:"
+ "safari_topLevelDomain"
+ "safari_traitsAffectingTextAppearance"
+ "safari_urlHashesOfComponents"
+ "safari_usesWhiteText"
+ "schedulePeriodicSettingsReport"
+ "searchProviderForURL:"
+ "setAutomaticallyAdjustsScrollIndicatorInsets:"
+ "setCachedTopBarTheme:"
+ "setEnableDelegateLayoutNotification:"
+ "setFluidTabOverviewViewController:"
+ "setFocusProfileUpdateIsForInactiveFocusMode:"
+ "setHidesCompletionArrowView:"
+ "setMinYMatchesTopBarMaxYWhenZoomed:"
+ "setNSIntegerValue:forTrait:"
+ "setNextLoadComesFromSearchPage:"
+ "setSearchURLTemplateFromForm:forSourcePageURLString:completionHandler:"
+ "setTestController:"
+ "setTitleRevealPercent:"
+ "setUsesWebProcessCache:"
+ "setVisibleTopBackdropHeight:"
+ "showsLockedPrivateBrowsingView"
+ "snapshotClipperView"
+ "snapshotImage"
+ "startPageViewController:didSelectItemWithIdentifier:atGridLocation:"
+ "symbolImage"
+ "tabCollectionItemDidChangeIcon:"
+ "tabCollectionItemDidChangeTitle:"
+ "tabCollectionViewItemHeaderHeightIncludedInSnapshot:"
+ "test_metadataHandler"
+ "test_setMetadataHandler:"
+ "titleRevealPercent"
+ "titleView"
+ "topBarThemeForTabOverviewShowingThemeColor:"
+ "updateColorSchemeForExplanationView"
+ "updateSeparatorInsetForTraitChange"
+ "v16@?0@\"WBSCGImage\"8"
+ "v24@0:8@\"<TabCollectionItemObserving>\"16"
+ "v24@0:8@\"SFTabOverviewItemContentView\"16"
+ "v24@?0@\"<TabSnapshotCacheObserving>\"8@\"NSUUID\"16"
+ "v24@?0@\"UICollectionViewListCell\"8@\"UICellConfigurationState\"16"
+ "v28@0:8B16@?<v@?>20"
+ "v32@?0@\"<TabCollectionItem>\"8Q16^B24"
+ "v40@0:8@\"SFFluidCollectionView\"16@\"SFFluidCollectionReuseableView\"24@\"NSIndexPath\"32"
+ "v40@0:8@\"_SFFormAutoFillController\"16@\"<WBSFormsMetadataProvider>\"24@\"NSURL\"32"
+ "v40@0:8@16:24@?32"
+ "v48@0:8@\"SFStartPageViewController\"16@24{?=qq}32"
+ "v48@0:8@16@24{?=qq}32"
+ "v56@0:8@\"SFClearHistoryViewController\"16@\"NSDate\"24@\"NSDate\"32@\"NSString\"40B48B52"
+ "v56@0:8@16@24@32@40B48B52"
+ "visibleTopBackdropHeight"
+ "\xf0!"
+ "\xf0!Q\x11"
- "\x01#\x12!2\x12\x15\x1b\x131A\x12C\x11%\x16D\x17\x18\x14"
- "\x01\xf0\xf0\xf0r"
- "\x04\x13"
- "\n\x11C"
- "\x11\x11"
- "\x11\x12\x15\x14\x1e\x15\x12\x11\x13"
- "\x12\x11\x11\x11\x11"
- "\x12\x16\x14\x11!B"
- "\x15\x12\x13!\x11\x16#\"#\x13\x11\x15\x11C"
- "!q\x91\xf0a\x11\x11\xf0\xf01\xf0a"
- ".*\x11\x1d\x19\x11'\x11\x11\x12\x11\x141\"T\x17\x11j\x12!\x13\x13?\x02\x19%"
- "5\x11"
- "@\"<TabGroupProvider>\"24@0:8@\"SFStartPageCustomizationViewController\"16"
- "@\"NSArray\"24@0:8@\"TabOverview\"16"
- "@\"SFVibrantSeparatorView\""
- "@\"UIImage\"24@0:8@\"WBProfile\"16"
- "@\"VibrantLabelView\""
- "@16@?0@\"TabOverviewItem\"8"
- "B32@0:8@\"TabSnapshotCache\"16@\"NSUUID\"24"
- "BookmarksNavigationBar"
- "BookmarksToolbar"
- "T@\"UILabel\",R,N,V_label"
- "T@\"UIView\",&,N,V_borrowedContentView"
- "TB,N,V_hidesAccessoryView"
- "VibrantLabelView"
- "_WKWebAuthenticationPanelDelegate"
- "_borrowedContentViewContainer"
- "_deleteButton"
- "_deleteButtonConstraints"
- "_detailLabelFont"
- "_enumerateDelegatesAndIdentifiersForEntry:usingBlock:"
- "_hidesAccessoryView"
- "_nonVibrantTextColor"
- "_parsecABGroupIdentifierDidChange:"
- "_reduceTransparencyStatusDidChange:"
- "_scaledFontForTextStyle:addingSymbolicTraits:"
- "_separatorEffect"
- "_separatorView"
- "_sf_accessingSecurityScopedResource:"
- "_sf_topLevelDomain"
- "_siteNameFont"
- "_switchingActiveDocument"
- "_tabDocumentsToKeepVisible"
- "_titleLabelFont"
- "_usesVibrantAppearance"
- "_vibrantLightDividerBurnColor"
- "_vibrantLightDividerDarkeningColor"
- "authenticatorDialogForPanel:dialogController:"
- "clear"
- "clearHistoryVisitsAddedAfterDate:beforeDate:profileIdentifier:clearAllProfiles:closeAllTabs:"
- "closeTabs:onDevice:"
- "constraintEqualToSystemSpacingAfterAnchor:multiplier:"
- "d24@0:8@\"TabOverview\"16"
- "decidePolicyForLocalAuthenticatorWithCompletionHandler:"
- "defaultFontDescriptorWithTextStyle:addingSymbolicTraits:options:"
- "effectForBlurEffect:"
- "enumerateAttribute:inRange:options:usingBlock:"
- "grayColor"
- "hidesAccessoryView"
- "imageForProfile:"
- "initWithPathToLegacySearchesFile:"
- "initWithSearchEngineSuggestion:userQuery:forPrivateBrowsing:"
- "inputColor0"
- "inputColor1"
- "inputReversed"
- "itemsFullyInView"
- "itemsToKeepVisibleForTabOverview:"
- "label"
- "localizedAttributedStringWithFormat:"
- "monospacedDigitSystemFontOfSize:weight:"
- "panel"
- "panel:decidePolicyForLocalAuthenticatorWithCompletionHandler:"
- "panel:dismissWebAuthenticationPanelWithResult:"
- "panel:requestLAContextForUserVerificationWithCompletionHandler:"
- "panel:requestPINWithRemainingRetries:completionHandler:"
- "panel:selectAssertionResponse:source:completionHandler:"
- "panel:updateWebAuthenticationPanel:"
- "person.fill"
- "presentedAuthenticatorDialog"
- "providersMatchingQueryString:"
- "requestPINWithRemainingRetries:completionHandler:"
- "safari_favoritesTitleWithEmojiForRTL:"
- "safari_objectBefore:"
- "scaledFontForFont:compatibleWithTraitCollection:"
- "scaledValueForValue:compatibleWithTraitCollection:"
- "selectAssertionResponse:source:completionHandler:"
- "setBackgroundImage:forBarMetrics:"
- "setBackgroundImage:forToolbarPosition:barMetrics:"
- "setHidesAccessoryView:"
- "setIsForUpdateOnly:"
- "setOverrideTraitCollection:forChildViewController:"
- "setSearchURLTemplateFromForm:forSourcePageURLString:"
- "setShadowImage:"
- "setShadowImage:forToolbarPosition:"
- "setSymbolImageName:"
- "sf_backgroundBlurEffect"
- "sf_hasSameTextAppearanceAs:"
- "sf_isFeedScheme"
- "sf_isWebSearchURL"
- "sf_stringByAddingSoftBreaksBeforePeriods"
- "sf_traitCollectionUsingVibrantAppearance"
- "sf_traitCollectionWithSidebarPresentation:"
- "startPageViewController:didSelectItemWithIdentifier:"
- "tabGroupProviderForCustomizationViewController:"
- "tabOverviewAdditionalItemHeaderHeight:"
- "tabSnapshotCache:shouldRequestSavedSnapshotWithIdentifier:"
- "traitCollectionWithPreferredContentSizeCategory:"
- "traitCollectionWithTraitsFromCollections:"
- "updateWebAuthenticationPanel:"
- "v16@?0{RetainPtr<CGImage *>=^v}8"
- "v24@?0@\"<TabSnapshotCacheDelegate>\"8@\"NSUUID\"16"
- "v28@0:8B16@?<v@?B>20"
- "v32@0:8@\"SFStartPageViewController\"16@24"
- "v32@0:8@\"_WKWebAuthenticationPanel\"16@?<v@?@\"LAContext\">24"
- "v32@0:8@\"_WKWebAuthenticationPanel\"16@?<v@?q>24"
- "v32@0:8@\"_WKWebAuthenticationPanel\"16q24"
- "v40@0:8@\"_WKWebAuthenticationPanel\"16Q24@?<v@?@\"NSString\">32"
- "v40@?0@8{_NSRange=QQ}16^B32"
- "v48@0:8@\"NSDate\"16@\"NSDate\"24@\"NSString\"32B40B44"
- "v48@0:8@\"_WKWebAuthenticationPanel\"16@\"NSArray\"24q32@?<v@?@\"_WKWebAuthenticationAssertionResponse\">40"
- "value:withObjCType:"
- "visionTitle"
- "visionURL"
- "{?={CGPoint=dd}dd}"
- "\xf1R"

```
