## MobileSafariUI

> `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-626.1.12.10.3
-  __TEXT.__text: 0x318f58
-  __TEXT.__objc_methlist: 0x25dec
-  __TEXT.__const: 0x9fa0
-  __TEXT.__gcc_except_tab: 0x2060c
-  __TEXT.__cstring: 0x11be4
+626.1.17.0.0
+  __TEXT.__text: 0x31bb84
+  __TEXT.__objc_methlist: 0x26094
+  __TEXT.__const: 0x9fc0
+  __TEXT.__gcc_except_tab: 0x20740
+  __TEXT.__cstring: 0x11c04
   __TEXT.__dlopen_cstrs: 0x7e6
-  __TEXT.__oslogstring: 0xb8bf
+  __TEXT.__oslogstring: 0xba7f
   __TEXT.__ustring: 0x1222
   __TEXT.__swift5_typeref: 0x7b8b
   __TEXT.__constg_swiftt: 0x2ba8

   __TEXT.__swift5_fieldmd: 0x1758
   __TEXT.__swift5_builtin: 0x1e0
   __TEXT.__swift5_assocty: 0xee8
-  __TEXT.__swift5_capture: 0x2558
+  __TEXT.__swift5_capture: 0x255c
   __TEXT.__swift5_proto: 0x59c
   __TEXT.__swift5_types: 0x234
   __TEXT.__swift_as_entry: 0x32c

   __TEXT.__swift_as_cont: 0x4a0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__unwind_info: 0x14010
+  __TEXT.__unwind_info: 0x14108
   __TEXT.__eh_frame: 0x57b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9d60
+  __DATA_CONST.__const: 0x9dd0
   __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xc38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x193b8
+  __DATA_CONST.__objc_selrefs: 0x19588
   __DATA_CONST.__objc_protorefs: 0x208
   __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_arraydata: 0x3a0
-  __DATA_CONST.__got: 0x3bd8
-  __AUTH_CONST.__const: 0x9a38
-  __AUTH_CONST.__cfstring: 0xe0c0
-  __AUTH_CONST.__objc_const: 0x34b00
+  __DATA_CONST.__got: 0x3bf0
+  __AUTH_CONST.__const: 0x9a58
+  __AUTH_CONST.__cfstring: 0xe140
+  __AUTH_CONST.__objc_const: 0x34d30
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x80
-  __AUTH_CONST.__auth_got: 0x3340
+  __AUTH_CONST.__auth_got: 0x3360
   __AUTH.__objc_data: 0x3568
   __AUTH.__data: 0x1450
-  __DATA.__objc_ivar: 0x21c8
-  __DATA.__data: 0xae48
+  __DATA.__objc_ivar: 0x21d8
+  __DATA.__data: 0xae38
   __DATA.__objc_stublist: 0x10
   __DATA.__common: 0x660
   __DATA_DIRTY.__objc_data: 0x46e0
-  __DATA_DIRTY.__data: 0x15a8
+  __DATA_DIRTY.__data: 0x1598
   __DATA_DIRTY.__bss: 0xf20
   __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17974
-  Symbols:   24247
-  CStrings:  3432
+  Functions: 18022
+  Symbols:   24293
+  CStrings:  3445
 
Symbols:
+ -[BrowserController catalogViewControllerWillUnfocusUnifiedField:searchFieldHasText:showingRecentSearches:]
+ -[BrowserRootViewController _splitViewControllerForInteractiveSidebarPresentation]
+ -[BrowserRootViewController _totalAdditionalLayoutHeightForBanners]
+ -[BrowserRootViewController _updateUnifiedBarContentUnderSidebarWidth]
+ -[BrowserRootViewController collapseVerticalTabBar]
+ -[BrowserRootViewController isPresentingSidebarInteractively]
+ -[BrowserRootViewController toggleVerticalBarExpanded]
+ -[BrowserRootViewController verticalTabBarIsCollapsed]
+ -[BrowserRootViewController verticalTabBarResizeInteraction:beginSidebarTransitionCollapsing:]
+ -[BrowserRootViewController verticalTabBarResizeInteraction:endSidebarTransitionCompleted:velocity:]
+ -[BrowserRootViewController verticalTabBarResizeInteraction:updateSidebarTransitionWithProgress:]
+ -[CatalogViewController _didMoveCompletionSelectionInTableView:]
+ -[CatalogViewController _presentPlatterForMultilineFieldVoiceSearchIfNeeded]
+ -[CatalogViewController _searchFieldDidEndEditingWithAddress:]
+ -[CatalogViewController _searchFieldDidEndEditingWithParsecTopHit:]
+ -[CatalogViewController _searchFieldDidEndEditingWithSearch:]
+ -[CatalogViewController _searchFieldExternalSearchDidEnd]
+ -[CatalogViewController _searchFieldIsReflectingAutocompletedSuggestionForSearch:]
+ -[CatalogViewController _userTypedString]
+ -[CatalogViewController multilineField:focusNextKeyView:]
+ -[CatalogViewController multilineField:moveCompletionSelectionByRowOffset:]
+ -[CatalogViewController multilineField:moveCompletionSelectionBySectionOffset:]
+ -[CatalogViewController multilineField:reflectedTextForSelectedCompletionWithUserTypedText:]
+ -[CatalogViewController multilineFieldHandleSubmission:]
+ -[CatalogViewController multilineFieldSelectCompletionItemIfAvailable:]
+ -[CatalogViewController multilineFieldShouldMoveCompletionSelection:]
+ -[ClusterContextMenuIdentifier targetedPreview]
+ -[OfflineSearchSuggestionsCompletionProvider disconnectFromSearchHelperIfNecessary]
+ -[TabController hasPendingTabsForTopicID:]
+ -[TabController shouldShowTopicGroups]
+ -[TabController updateCanShowClusters]
+ -[TabDocument _pageCanScrollAwayBannerOfHeight:]
+ -[TabDocument _setAppBannerAfterFirstPaint:]
+ -[TabDocument _setAppLinkBannerWhenPageHeightIsSettled:]
+ -[TabDocument _setAppLinkBannerWithSettledPageHeight:]
+ -[TabDocument _shouldSkipInputSessionFocusLifecycleForInputSession:]
+ -[TabDocument isPendingForTopicID:]
+ -[TabDocument updateAutoDarkModeStateForURL:isShowingErrorPage:]
+ -[UnifiedField sf_isUsingPencilInput]
+ -[UnifiedField sf_textInput]
+ GCC_except_table1011
+ GCC_except_table1014
+ GCC_except_table1017
+ GCC_except_table1039
+ GCC_except_table284
+ GCC_except_table410
+ GCC_except_table417
+ GCC_except_table424
+ GCC_except_table427
+ GCC_except_table431
+ GCC_except_table437
+ GCC_except_table440
+ GCC_except_table443
+ GCC_except_table445
+ GCC_except_table459
+ GCC_except_table462
+ GCC_except_table491
+ GCC_except_table505
+ GCC_except_table508
+ GCC_except_table520
+ GCC_except_table539
+ GCC_except_table565
+ GCC_except_table587
+ GCC_except_table589
+ GCC_except_table592
+ GCC_except_table596
+ GCC_except_table617
+ GCC_except_table626
+ GCC_except_table649
+ GCC_except_table694
+ GCC_except_table706
+ GCC_except_table714
+ GCC_except_table723
+ GCC_except_table730
+ GCC_except_table768
+ GCC_except_table784
+ GCC_except_table795
+ GCC_except_table814
+ GCC_except_table833
+ GCC_except_table884
+ GCC_except_table887
+ GCC_except_table917
+ GCC_except_table918
+ GCC_except_table941
+ GCC_except_table964
+ GCC_except_table972
+ GCC_except_table973
+ GCC_except_table997
+ GCC_except_table999
+ _OBJC_IVAR_$_BrowserRootViewController._verticalTabBarOverrideBackgroundColor
+ _OBJC_IVAR_$_CapsuleNavigationBarViewController._lastBoundTabUUIDForMultilineField
+ _OBJC_IVAR_$_CatalogViewController._presentedPlatterForVoiceSearch
+ _OBJC_IVAR_$_TabDocument._appLinkBannerPendingSettledPageHeight
+ _WBSAutoDarkModeSymbolName
+ ___38-[TabController reorderTabsWithUUIDs:]_block_invoke_2
+ ___42-[TabController hasPendingTabsForTopicID:]_block_invoke
+ ___57-[Application application:didFinishLaunchingWithOptions:]_block_invoke_20
+ ___57-[BrowserRootViewController _updateTopBarStylesAnimated:]_block_invoke_2
+ ___64-[TabDocument updateAutoDarkModeStateForURL:isShowingErrorPage:]_block_invoke
+ ___74-[BrowserController rootViewControllerViewDidTransitionFromSize:animated:]_block_invoke
+ ___block_descriptor_32_e26_B16?0"SFPinnableBanner"8l
+ ___block_descriptor_40_e8_32s_e25_"WBTab"16?0"NSString"8ls32l8
+ ___block_descriptor_41_e8_32r_e51_v32?0"<CollectionViewTab>"8"TabController"16^B24lr32l8
+ ___block_descriptor_57_e8_32s40s48s_e39_"SFTabSwitcherPage"16?0"WBTabGroup"8ls32l8s40l8s48l8
+ ___block_descriptor_57_ea8_32s40w_e37_v16?0"WBSAutoDarkModeWebsiteState"8lw40l8s32l8
- -[BrowserController catalogViewControllerWillUnfocusUnifiedField:showingRecentSearches:]
- -[TabDocument _setAppBannerWhenPainted:]
- -[TabDocument updateAutoDarkModeStateForURL:]
- GCC_except_table1001
- GCC_except_table1004
- GCC_except_table1013
- GCC_except_table1020
- GCC_except_table1021
- GCC_except_table1256
- GCC_except_table154
- GCC_except_table405
- GCC_except_table415
- GCC_except_table418
- GCC_except_table432
- GCC_except_table439
- GCC_except_table444
- GCC_except_table460
- GCC_except_table465
- GCC_except_table473
- GCC_except_table485
- GCC_except_table495
- GCC_except_table509
- GCC_except_table519
- GCC_except_table568
- GCC_except_table594
- GCC_except_table595
- GCC_except_table597
- GCC_except_table627
- GCC_except_table628
- GCC_except_table629
- GCC_except_table630
- GCC_except_table635
- GCC_except_table643
- GCC_except_table653
- GCC_except_table675
- GCC_except_table676
- GCC_except_table698
- GCC_except_table718
- GCC_except_table740
- GCC_except_table762
- GCC_except_table788
- GCC_except_table812
- GCC_except_table847
- GCC_except_table848
- GCC_except_table866
- GCC_except_table894
- GCC_except_table906
- GCC_except_table912
- GCC_except_table922
- GCC_except_table926
- GCC_except_table956
- GCC_except_table977
- GCC_except_table983
- GCC_except_table985
- _SFEnableStandaloneTabBarKey
- ___45-[TabDocument updateAutoDarkModeStateForURL:]_block_invoke
- ___block_descriptor_33_e51_v32?0"<CollectionViewTab>"8"TabController"16^B24l
- ___block_descriptor_56_e8_32s40s48s_e39_"SFTabSwitcherPage"16?0"WBTabGroup"8ls32l8s40l8s48l8
- ___block_descriptor_56_ea8_32s40w_e37_v16?0"WBSAutoDarkModeWebsiteState"8lw40l8s32l8
CStrings:
+ "\"\xf0\xf0\""
+ "@\"WBTab\"16@?0@\"NSString\"8"
+ "Adaptive Dark Mode Is Ready"
+ "B16@?0@\"SFPinnableBanner\"8"
+ "Beginning interactive sidebar transition to %{public}@ sidebar isAnimation=YES "
+ "Ended interactive sidebar transition to %{public}@ sidebar with empty width"
+ "Ended interactive sidebar transition to %{public}@ sidebar, which would overlay the vertical tab bar"
+ "Ending interactive sidebar transition, completed: %d, velocity: %.0f"
+ "None"
+ "Split view controller declined interactive sidebar transition to %{public}@ sidebar"
+ "Vertical"
+ "VerticalTabBarSidebarTransition"
+ "Websites will automatically get a dark appearance whenever your iPad is in Dark Mode."
+ "Websites will automatically get a dark appearance whenever your iPhone is in Dark Mode."
+ "hide"
+ "show"
+ "\xf0A\xf0\xf0\xe1\xc1\xf0\xf0\xf0\xf01\xf0a\x82\xf0Aq"
+ "\xf0s"
- "Adaptive Dark Mode Is On"
- "Your iPad is set to Light Mode. Safari will apply a dark appearance to websites when your iPad is in Dark Mode."
- "Your iPhone is set to Light Mode. Safari will apply a dark appearance to websites when your iPhone is in Dark Mode."
- "\xf0A\xf0\xf0\xd1\xc1\xf0\xf0\xf0\xf01\xf0a\x82\xf0Aq"
- "\xf0c"
```
