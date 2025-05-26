## UIKit

> `/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit`

```diff

-2905.4.0.0.0
-  __TEXT.__text: 0xcdd7c
-  __TEXT.__auth_stubs: 0x1630
-  __TEXT.__objc_methlist: 0xded0
-  __TEXT.__const: 0x190
-  __TEXT.__cstring: 0x1713b
-  __TEXT.__oslogstring: 0x206c
-  __TEXT.__gcc_except_tab: 0x18cc
+2909.1.4.3.0
+  __TEXT.__text: 0x16e660
+  __TEXT.__auth_stubs: 0x1440
+  __TEXT.__objc_methlist: 0xdef8
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x171ab
+  __TEXT.__oslogstring: 0x2075
+  __TEXT.__gcc_except_tab: 0x1e84
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x3d94
+  __TEXT.__unwind_info: 0x2a74
   __TEXT.__objc_classname: 0x86cc
-  __TEXT.__objc_methname: 0x14ee8
-  __TEXT.__objc_methtype: 0x214b
-  __TEXT.__objc_stubs: 0xf860
+  __TEXT.__objc_methname: 0x14f3e
+  __TEXT.__objc_methtype: 0x216d
+  __TEXT.__objc_stubs: 0xf8c0
   __DATA_CONST.__got: 0x708
-  __DATA_CONST.__const: 0x1f20
+  __DATA_CONST.__const: 0x1cf8
   __DATA_CONST.__objc_classlist: 0x1990
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x11498
-  __DATA_CONST.__objc_selrefs: 0x5350
+  __DATA_CONST.__objc_selrefs: 0x5360
   __DATA_CONST.__objc_arraydata: 0x170
   __AUTH_CONST.__objc_const: 0xe5e0
-  __AUTH_CONST.__cfstring: 0x1bd20
+  __AUTH_CONST.__cfstring: 0x1bd80
   __AUTH_CONST.__const: 0x1380
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0xb28
+  __AUTH_CONST.__auth_got: 0xa30
   __AUTH.__objc_data: 0xa00
   __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x7e0
+  __DATA.__objc_classrefs: 0x7e8
   __DATA.__objc_superrefs: 0x9c8
   __DATA.__objc_ivar: 0x110
-  __DATA.__data: 0x600
+  __DATA.__data: 0x620
   __DATA.__bss: 0x266
   __DATA_DIRTY.__objc_data: 0xf5a0
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5350
-  Symbols:   18485
-  CStrings:  7959
+  Functions: 5479
+  Symbols:   18701
+  CStrings:  7966
 
Symbols:
+ -[AXCollectionViewData childCount]
+ -[AXCollectionViewData children]
+ -[AXCollectionViewData setChildCount:]
+ -[AXPlatterContentMockElement sourceElement]
+ -[AXPlatterContentMockElement sourceView]
+ -[AXSFFocusRingShapeLayer innerBorder]
+ -[AXSFFocusRingShapeLayer outerBorder]
+ -[TIPreferencesControllerAccessibility__UIKit__TextInput _accessibilitySetMouseKeysEnabled:]
+ -[UIAccessibilityCustomRotorAccessibility _accessibilityApplyAttributes]
+ -[UIAccessibilityElementKBEmojiCategory categoryIndex]
+ -[UIAccessibilityElementKBEmojiCategory categoryView]
+ -[UIAccessibilityElementKBEmojiCategory category]
+ -[UIAccessibilityElementKBEmojiCategory setCategoryIndex:]
+ -[UIAccessibilityElementKBKey _accessibilityActivateForPanAlternate:isSecondAlternate:]
+ -[UIAccessibilityElementKBKey _accessibilityIsKeySelected]
+ -[UIAccessibilityElementKBKey _accessibilityWasForcedToUseForeignKB]
+ -[UIAccessibilityElementKBKey cachedVariantKeys]
+ -[UIAccessibilityElementKBKey changesOnShiftDown]
+ -[UIAccessibilityElementKBKey setChangesOnShiftDown:]
+ -[UIAccessibilityPanAlternateCustomAction isSecondAlternate]
+ -[UIAccessibilityPanAlternateCustomAction setIsSecondAlternate:]
+ -[UIAccessibilityPickerComponent component]
+ -[UIApplicationAccessibility _accessibilityCancelRewindOrFastForward]
+ -[UIApplicationAccessibility _accessibilityShowKeyboardHints]
+ -[UIBarButtonItemAccessibility _setAXBarButtonImagePath:]
+ -[UICollectionViewAccessibility _accessibilityShouldDisableCellReuse]
+ -[UICollectionViewAccessibility _axGetShouldIgnorePromiseRegions]
+ -[UICollectionViewAccessibility _axIsReorderingItems]
+ -[UICollectionViewAccessibility _axResetData]
+ -[UICollectionViewAccessibility _axSetIsReorderingItems:]
+ -[UICollectionViewAccessibility _axSetSpeakItemReorderEvents:]
+ -[UICollectionViewListCellAccessibility _axCellSelectionTogglesExpansionState]
+ -[UIColorAccessibility _accessibilitySetCachedColorDescriptions:]
+ -[UIDimmingViewAccessibility _accessibilityCoversScreen]
+ -[UIHoverGestureRecognizerAccessibility _axIsListeningForNotifications]
+ -[UIHoverGestureRecognizerAccessibility _axSetIsListeningForNotifications:]
+ -[UIHoverGestureRecognizerAccessibility _axSetSimulatedState:]
+ -[UIHoverGestureRecognizerAccessibility _axSimulatedState]
+ -[UIInputSwitcherViewAccessibility _accessibilitySetLastHandednessBiasAnnouncement:]
+ -[UIKeyboardAccessibility _axAdvanceInternationalKeyboard:]
+ -[UIKeyboardAccessibility _axAdvanceKeyboardPlane:]
+ -[UIKeyboardAccessibility _axAdvanceKeyboardSuggestion:]
+ -[UIKeyboardAccessibility _axCommitWord]
+ -[UIKeyboardEmojiCategoryBarAccessibility _accessibilityTraitsForElementAtIndex:]
+ -[UIKeyboardEmojiCollectionViewCellAccessibility _accessibilitySetCachedVariantKeys:]
+ -[UIKeyboardImplAccessibility _axIsObservingAppLifecycleNotifications]
+ -[UIKeyboardImplAccessibility _axSetIsObservingAppLifecycleNotifications:]
+ -[UIKeyboardImplAccessibility _axShouldShowKeyboard]
+ -[UIKeyboardImplAccessibility showKeyboardWithoutSuppressionPolicy]
+ -[UIKeyboardLayoutStarAccessibility _accessibilitySetStickyPopupKeys:]
+ -[UIKeyboardLayoutStarAccessibility _axIsWaitingForEmojiPopupAnnouncement]
+ -[UIKeyboardLayoutStarAccessibility _axSetIsWaitingForEmojiPopupAnnouncement:]
+ -[UINavigationBarAccessibility _accessibilitySetFauxBackButton:]
+ -[UINavigationBarAccessibility _axSetCachedStaticNavBarButton:]
+ -[UINavigationItemAccessibility _axDidOverrideHidesSearchBarWhenScrolling]
+ -[UINavigationItemAccessibility _axSetDidOverrideHidesSearchBarWhenScrolling:]
+ -[UINavigationItemAccessibility _axSetOriginalHidesSearchBarWhenScrolling:]
+ -[UINavigationItemAccessibility _axSetShouldHideSearchBarWhenScrolling:]
+ -[UINavigationItemAccessibility _axShouldHideSearchBarWhenScrolling]
+ -[UIPageControlAccessibility _accessibilityIsUserInteractionEnabled]
+ -[UIPanelBorderViewAccessibility _axIsPrimaryBorder]
+ -[UIScrollBarIndicatorAccessibilityElement orientation]
+ -[UIScrollBarIndicatorAccessibilityElement setOrientation:]
+ -[UIScrollViewAccessibility _accessibilitySetStoredShouldUseFallbackForVisibleContentInset:]
+ -[UIScrollViewAccessibility _accessibilitySetStoredVisibleContentInset:]
+ -[UIScrollViewAccessibility _axBaseScrollLeftPageSupported]
+ -[UIScrollViewAccessibility _axBaseScrollRightPageSupported]
+ -[UIScrollViewAccessibility _axHandleScrollViewPullDown]
+ -[UIScrollViewAccessibility _axMaximumContentOffset]
+ -[UIScrollViewAccessibility _axMinimumContentOffset]
+ -[UISplitKeyboardSupportAccessibility _axSetLastLocationDescription:]
+ -[UIStatusBarBatteryItemViewAccessibility _accessibilityNonQuantizedBatteryLevel]
+ -[UIStatusBarBatteryItemViewAccessibility _accessibilitySetNonQuantizedBatteryLevel:]
+ -[UIStatusBarBatteryItemViewAccessibility _axSetCachedAXLabel:]
+ -[UIStepperAccessibility _axSetMacIdiomDecrementElement:]
+ -[UIStepperAccessibility _axSetMacIdiomIncrementElement:]
+ -[UITableTextAccessibilityElement attributeDelegate]
+ -[UITableViewAccessibility _accessibilityInternalDataRetrieveOnly]
+ -[UITableViewAccessibility _accessibilityShouldConsiderSwipeDeletionCommitted]
+ -[UITableViewAccessibility _accessibilitySwappedWithRowForInitialGlobalRow:oldGlobalRow:globalRow:]
+ -[UITableViewAccessibility _axSetIndexGuide:]
+ -[UITableViewCellAccessibility _accessibilityIsButtonAccessoryType:]
+ -[UITableViewCellAccessibility _accessibilityIsRemoveConfirmVisible]
+ -[UITableViewCellAccessibility _accessibilityRemoveInternalData]
+ -[UITableViewCellAccessibility _accessibilityRetrieveTableViewCellTextForReorderControl]
+ -[UITableViewCellAccessibility _accessibilityRetrieveTableViewCellTextWithLocalizationOptions:shouldExcludeDetailText:forReorderControl:]
+ -[UITableViewCellAccessibility _accessibilityShouldBeEmptyIfHidden]
+ -[UITableViewCellAccessibility _axReorderElementsByMovingIndexPaths:tableView:currentPath:]
+ -[UITableViewCellAccessibility _axSubviewIgnoredDueToHiddenOrZeroAlphaAncestry:]
+ -[UITableViewCellAccessibility accessibilitySetIsFetchingChildren:]
+ -[UITextFieldAccessibility _axShowsLeadingView]
+ -[UITextFieldAccessibility _axShowsTrailingView]
+ -[UITextFieldAccessibility _axTextFieldIsHidden]
+ -[UITextViewAccessibility _axClearCachedLinkData]
+ -[UITextViewAccessibility _axDidRegisterForDDNotification]
+ -[UITextViewAccessibility _axSetDidRegisterForDDNotification:]
+ -[UIViewAccessibility _accessibilityDidLoadAccessibilityInformation]
+ -[UIViewAccessibility _accessibilityIsIgnored]
+ -[UIViewAccessibility _setAccessibilityDidLoadAccessibilityInformation:]
+ -[UIViewAnimationStateAccessibility _accessibilityMarkAnimationNotInProgress:]
+ -[UIViewAnimationStateAccessibility _accessibilitySetAnimationTracker:]
+ -[UIViewControllerAccessibility _accessibilityDidLoadAccessibilityInformation]
+ -[UIViewControllerAccessibility _setAccessibilityDidLoadAccessibilityInformation:]
+ -[UIWindowAccessibility _accessibilitySetFirstResponderCoalesceTimer:]
+ -[UIWindowAccessibility _accessibilitySetRemoteElement:]
+ -[_AXTableViewInternal accessibleElementCount]
+ -[_AXTableViewInternal children]
+ -[_AXTableViewInternal indexMap]
+ -[_AXTableViewInternal searchControllerDimmingViewVisible]
+ -[_AXTableViewInternal searchTableViewVisible]
+ -[_AXTableViewInternal sectionFooters]
+ -[_AXTableViewInternal sectionHeaders]
+ -[_AXTableViewInternal setAccessibleElementCount:]
+ -[_AXTableViewInternal setReusableCellsEnabled:]
+ -[_AXTableViewInternal setSearchControllerDimmingViewVisible:]
+ -[_AXTableViewInternal setSearchTableViewVisible:]
+ -[_AXUITextViewParagraphElement _accessibilityContent]
+ -[_AXUITextViewParagraphElement links]
+ -[_AXUITextViewParagraphElement textRange]
+ -[_UIAccessibilityNavigationViewInfo barButtonItem]
+ -[_UIAccessibilityNavigationViewInfo isCancelItem]
+ -[_UIAccessibilityNavigationViewInfo isRightItem]
+ -[_UIAccessibilityNavigationViewInfo navigationBar]
+ -[_UIAccessibilityNavigationViewInfo setBarButtonItem:]
+ -[_UIAccessibilityNavigationViewInfo setIsCancelItem:]
+ -[_UIAccessibilityNavigationViewInfo setIsRightItem:]
+ -[_UIAccessibilityNavigationViewInfo setNavigationBar:]
+ -[_UIAccessibilityNavigationViewInfo setNavigationItem:]
+ -[_UIContextMenuContainerViewAccessibility _axCurrentDetentIndexForPanController:]
+ -[_UINavigationBarTitleControlAccessibility canBecomeFocused]
+ -[_UIPlatterTransformViewAccessibility _accessibilityIsExpandedTransformView]
+ -[_UIPlatterTransformViewAccessibility _axSetCachedPlatterElements:]
+ -[_UIPlatterTransformViewAccessibility _axShowsSourceViewDirectly]
+ -[_UIRemoteViewAccessibility _accessibilityRemoteMachPort]
+ -[_UIRemoteViewAccessibility _accessibilityRemoteViewPid]
+ -[_UIRemoteViewAccessibility _accessibilitySetRemoteElementArray:]
+ -[_UIRemoteViewControllerAccessibility _accessibilityLoadAccessibilityInformation:]
+ -[_UIScenePresentationViewAccessibility _accessibilitySetRemoteElementArray:]
+ -[_UIScrollViewScrollIndicatorAccessibility setAccessibilityScrollIndicatorIsFocused:]
+ -[_UIStatusBarAccessibility _axGetIsHitTesting]
+ -[_UIStatusBarBackgroundActivityItemAccessibility _accessibilityHasRequestedForceUpdate]
+ -[_UIStatusBarBackgroundActivityItemAccessibility _accessibilitySetHasRequestedForceUpdate:]
+ -[_UIStatusBarIndicatorItemAccessibility _axLabelKeyForClassNameDict]
+ GCC_except_table105
+ GCC_except_table110
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table115
+ GCC_except_table122
+ GCC_except_table136
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table148
+ GCC_except_table161
+ GCC_except_table162
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table168
+ GCC_except_table176
+ GCC_except_table188
+ GCC_except_table192
+ GCC_except_table195
+ GCC_except_table200
+ GCC_except_table208
+ GCC_except_table23
+ GCC_except_table35
+ GCC_except_table43
+ GCC_except_table44
+ GCC_except_table49
+ GCC_except_table57
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table75
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table85
+ GCC_except_table87
+ _AXCGFAbs
+ _AXIgnoresTextOperations
+ _AXNoLoc
+ _AX_CGSizeIsEmpty
+ _AX_CGSizeIsProbablyEmpty
+ _AX_IS_DEBUG_BUILD
+ _CAPoint3DMakeWithCGPoint
+ _CGCeiling
+ _CGFAbs
+ _CGFloatMax
+ _CGFloatMin
+ _CGFloatMinMax
+ _CGFloor
+ _CGPointMake
+ _CGRectMake
+ _CGSizeMake
+ _EmojiFoundationLibrary
+ _EmojiFoundationLibraryCore
+ _LargeStepMultiplier
+ _MACancelDownloadErrorDomain_block_invoke.BaseImplementation
+ _MACancelDownloadErrorDomain_block_invoke.onceToken
+ _OBJC_CLASS_$_UICellAccessoryCustomView
+ _RemoteTextInputLibrary
+ _RemoteTextInputLibraryCore
+ _UIEdgeInsetsEqualToEdgeInsets
+ _UIEdgeInsetsInsetRect
+ _UIEdgeInsetsMake
+ _UIInterfaceOrientationIsLandscape
+ _UIRectGetHeight
+ _UIRectGetMaxX
+ _UIRectGetMaxY
+ _UIRectGetMinX
+ _UIRectGetMinY
+ _UIRectGetWidth
+ __TraditionalStrokeDictionary
+ ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.715
+ ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.716
+ ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.717
+ ___137-[UITableViewCellAccessibility _accessibilityRetrieveTableViewCellTextWithLocalizationOptions:shouldExcludeDetailText:forReorderControl:]_block_invoke
+ ___137-[UITableViewCellAccessibility _accessibilityRetrieveTableViewCellTextWithLocalizationOptions:shouldExcludeDetailText:forReorderControl:]_block_invoke_2
+ ___60-[UITextViewAccessibility _accessibilityUserTestingChildren]_block_invoke.489
+ ___66-[UITableViewCellAccessibility _privateAccessibilityCustomActions]_block_invoke
+ ___66-[UITableViewCellAccessibility _privateAccessibilityCustomActions]_block_invoke_2
+ ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.240
+ ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.253
+ ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.479
+ ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.480
+ ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke.349
+ ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke_2.350
+ ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.337
+ ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke_2.338
+ ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.621
+ ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.622
+ ___76-[UICollectionViewAccessibility accessibilityCreatePrepareCellForIndexPath:]_block_invoke.436
+ ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.499
+ ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.500
+ ___80-[UITextInputUIResponderAccessibility _accessibilityInsertTextWithAlternatives:]_block_invoke.557
+ ___82-[_UIRemoteDictionaryViewControllerAccessibility tableView:cellForRowAtIndexPath:]_block_invoke.267
+ ___88-[UIKeyboardEmojiCollectionViewAccessibility _accessibilityLocalizedVisibleSectionNames]_block_invoke.279
+ ___88-[UITableViewAccessibility _axOpaqueHeaderElementInDirection:withinElements:startIndex:]_block_invoke
+ ___89-[UITableViewAccessibility _axFirstLastOpaqueHeaderElementFromSection:options:direction:]_block_invoke.485
+ ___91-[UITableViewCellAccessibility _axReorderElementsByMovingIndexPaths:tableView:currentPath:]_block_invoke
+ ___92-[UITableViewAccessibility _axOffScreenOpaqueHeaderElementInDirection:options:childElement:]_block_invoke.495
+ ___93-[_UIRemoteViewControllerAccessibility _accessibilityLoadAccessibilityInformation:retryTime:]_block_invoke.306
+ ___CGPointEqualToPoint
+ ___CGSizeEqualToSize
+ ___block_descriptor_32_e73_Q72?0{CGRect={CGPoint=dd}{CGSize=dd}}8{CGRect={CGPoint=dd}{CGSize=dd}}40l
+ ___block_descriptor_40_e8_32w_e37_B16?0"UIAccessibilityCustomAction"8lw32l8
+ ___block_descriptor_56_e8_32s_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32ls32l8
+ ___block_descriptor_72_e8_32s_e15_v32?0816^B24ls32l8
+ ___block_literal_global.1834
+ ___block_literal_global.219
+ ___block_literal_global.223
+ ___block_literal_global.228
+ ___block_literal_global.233
+ ___block_literal_global.2397
+ ___block_literal_global.247
+ ___block_literal_global.267
+ ___block_literal_global.271
+ ___block_literal_global.276
+ ___block_literal_global.289
+ ___block_literal_global.2987
+ ___block_literal_global.2989
+ ___block_literal_global.2994
+ ___block_literal_global.3006
+ ___block_literal_global.3008
+ ___block_literal_global.3032
+ ___block_literal_global.3040
+ ___block_literal_global.325
+ ___block_literal_global.327
+ ___block_literal_global.328
+ ___block_literal_global.335
+ ___block_literal_global.336
+ ___block_literal_global.340
+ ___block_literal_global.344
+ ___block_literal_global.348
+ ___block_literal_global.352
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.367
+ ___block_literal_global.370
+ ___block_literal_global.381
+ ___block_literal_global.389
+ ___block_literal_global.418
+ ___block_literal_global.419
+ ___block_literal_global.420
+ ___block_literal_global.442
+ ___block_literal_global.444
+ ___block_literal_global.451
+ ___block_literal_global.455
+ ___block_literal_global.473
+ ___block_literal_global.475
+ ___block_literal_global.478
+ ___block_literal_global.482
+ ___block_literal_global.492
+ ___block_literal_global.502
+ ___block_literal_global.512
+ ___block_literal_global.516
+ ___block_literal_global.524
+ ___block_literal_global.534
+ ___block_literal_global.546
+ ___block_literal_global.550
+ ___block_literal_global.559
+ ___block_literal_global.563
+ ___block_literal_global.566
+ ___block_literal_global.571
+ ___block_literal_global.584
+ ___block_literal_global.585
+ ___block_literal_global.589
+ ___block_literal_global.607
+ ___block_literal_global.614
+ ___block_literal_global.624
+ ___block_literal_global.652
+ ___block_literal_global.655
+ ___block_literal_global.658
+ ___block_literal_global.674
+ ___block_literal_global.703
+ ___block_literal_global.766
+ ___block_literal_global.823
+ ___block_literal_global.825
+ ___block_literal_global.869
+ ___block_literal_global.881
+ ___block_literal_global.883
+ ___block_literal_global.884
+ ___block_literal_global.886
+ ___block_literal_global.901
+ ___block_literal_global.906
+ ___block_literal_global.928
+ ___block_literal_global.937
+ ___block_literal_global.971
+ ___os_log_helper_16_0_0
+ ___os_log_helper_16_0_1_4_0
+ ___os_log_helper_16_0_1_8_0
+ ___os_log_helper_16_0_2_4_0_4_0
+ ___os_log_helper_16_0_2_8_0_8_0
+ ___os_log_helper_16_0_4_4_0_4_0_4_0_4_0
+ ___os_log_helper_16_2_1_8_64
+ ___os_log_helper_16_2_1_8_66
+ ___os_log_helper_16_2_2_4_0_8_64
+ ___os_log_helper_16_2_2_8_0_8_66
+ ___os_log_helper_16_2_2_8_64_4_0
+ ___os_log_helper_16_2_2_8_64_8_0
+ ___os_log_helper_16_2_2_8_64_8_64
+ ___os_log_helper_16_2_2_8_66_4_0
+ ___os_log_helper_16_2_2_8_66_8_66
+ ___os_log_helper_16_2_3_8_64_4_0_4_0
+ ___os_log_helper_16_2_3_8_64_4_0_8_64
+ ___os_log_helper_16_2_3_8_64_8_64_4_0
+ ___os_log_helper_16_2_3_8_64_8_64_8_64
+ ___os_log_helper_16_2_3_8_66_8_0_8_66
+ ___os_log_helper_16_2_3_8_66_8_66_8_66
+ ___os_log_helper_16_2_4_4_0_4_0_8_64_8_64
+ ___os_log_helper_16_2_4_8_64_4_0_8_0_8_64
+ ___os_log_helper_16_3_1_8_65
+ ___os_log_helper_16_3_1_8_69
+ ___os_log_helper_16_3_2_8_69_8_64
+ ___os_log_helper_16_3_3_4_0_4_0_8_65
+ __accessibilityFindDurationRangeInString
+ __accessibilityRetrieveTableViewCellTextWithLocalizationOptions:shouldExcludeDetailText:forReorderControl:.InSortingSentinel
+ __isDevicePasscodeLocked
+ __unnamed_array_storage.250
+ __unnamed_array_storage.314
+ __unnamed_array_storage.384
+ __unnamed_array_storage.394
+ __unnamed_array_storage.395
+ __unnamed_array_storage.944
+ __unnamed_array_storage.951
+ __unnamed_array_storage.952
+ __unnamed_array_storage.966
+ __unnamed_array_storage.967
+ _axShouldDisableHitpointWarping
+ _getEMFEmojiTokenClass
+ _getRTIInputUIServiceMachNameiOSSymbolLoc
+ _kAXLastDictationMagicTapTime
+ _memcpy
+ _memset
+ _objc_msgSend$_accessibilityRetrieveTableViewCellTextForReorderControl
+ _objc_msgSend$_accessibilityRetrieveTableViewCellTextWithLocalizationOptions:shouldExcludeDetailText:forReorderControl:
+ _objc_msgSend$_axReorderElementsByMovingIndexPaths:tableView:currentPath:
+ _objc_msgSend$_interactionShouldBeginAtPoint:completion:
+ _objc_msgSend$beginUpdates
+ _objc_msgSend$editControlWasClicked:
+ _objc_msgSend$endUpdates
+ _objc_msgSend$moveRowAtIndexPath:toIndexPath:
+ _setTitleView:.AXIsAccessingTitleView
+ _trimWhitespaceToNil
- +[AXUIKitGlue _accessibilityInitializeSubclassRuntimeOverrides].cold.1
- -[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:].cold.1
- -[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:].cold.2
- -[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:].cold.3
- -[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:].cold.4
- -[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:].cold.5
- -[UIApplicationAccessibility _accessibilityResetAndClearNativeFocusSystem].cold.1
- -[UIApplicationAccessibility _accessibilityResponderElement:].cold.1
- -[UIApplicationAccessibility _accessibilitySetFocusEnabledInApplication:].cold.1
- -[UIApplicationAccessibility _iosAccessibilitySetValue:forAttribute:].cold.1
- -[UIApplicationAccessibility _iosAccessibilitySetValue:forAttribute:].cold.2
- -[UIApplicationAccessibility _iosAccessibilitySetValue:forAttribute:].cold.3
- -[UIApplicationAccessibility _iosAccessibilitySetValue:forAttribute:].cold.4
- -[UIApplicationAccessibility _iosAccessibilitySetValue:forAttribute:].cold.5
- -[UIBarButtonItemAccessibility _axRememberTargetter:]
- -[UICollectionViewAccessibility _accessibilityOpaqueHeaderElementInDirection:childElement:].cold.1
- -[UICollectionViewAccessibility _accessibilityOpaqueHeaderElementInDirection:childElement:].cold.2
- -[UICollectionViewAccessibility _axFirstLastOpaqueHeaderElementInDirection:options:].cold.1
- -[UICollectionViewAccessibility _axOffScreenOpaqueHeaderElementInDirection:options:childElement:].cold.1
- -[UICollectionViewAccessibility _axOffScreenOpaqueHeaderElementInDirection:options:childElement:].cold.2
- -[UICollectionViewAccessibility accessibilityCreatePrepareCellForIndexPath:].cold.1
- -[UIImageViewAccessibility accessibilityElements].cold.1
- -[UIIndexBarAccessoryViewAccessibility accessibilityIncrement].cold.1
- -[UIKeyboardImplAccessibility _axUnregisterForVoiceOverNotifications:].cold.1
- -[UINavigationBarAccessibility accessibilityIdentifier].cold.1
- -[UINavigationBarAccessibility accessibilityIdentifier].cold.2
- -[UINavigationBarAccessibility accessibilityIdentifier].cold.3
- -[UINavigationBarAccessibility accessibilityIdentifier].cold.4
- -[UINavigationBarAccessibility accessibilityIdentifier].cold.5
- -[UINavigationBarAccessibility accessibilityIdentifier].cold.6
- -[UIPresentationControllerAccessibility _accessibilityModalizePresentationView].cold.1
- -[UIScrollViewAccessibility _accessibilityScrollToFrame:forView:].cold.1
- -[UIScrollViewAccessibility _accessibilityScrollToFrame:forView:].cold.2
- -[UIScrollViewAccessibility _accessibilityScrollToFrame:forView:].cold.3
- -[UIScrollViewAccessibility _accessibilityScrollToFrame:forView:].cold.4
- -[UIScrollViewAccessibility _axContentOffsetForAddedProgress:inDirection:].cold.1
- -[UIScrollViewAccessibility _axProgressForDirection:].cold.1
- -[UIScrollViewAccessibility accessibilityApplyScrollContent:sendScrollStatus:animateWithDuration:animationCurve:].cold.1
- -[UIScrollViewAccessibility accessibilityNumberOfPagesForScrollIndicator:].cold.1
- -[UIScrollViewAccessibility accessibilityShouldEnableScrollIndicator:].cold.1
- -[UIScrollViewAccessibility accessibilityValidateScrollContentOffset:].cold.1
- -[UITableViewAccessibility _accessibilityOpaqueHeaderElementInDirection:childElement:].cold.1
- -[UITableViewAccessibility _accessibilityOpaqueHeaderElementInDirection:childElement:].cold.2
- -[UITableViewAccessibility _axFirstLastOpaqueHeaderElementFromSection:options:direction:].cold.1
- -[UITableViewAccessibility _axFirstLastOpaqueHeaderElementInDirection:options:].cold.1
- -[UITableViewAccessibility _axFirstLastOpaqueHeaderElementInDirection:options:].cold.2
- -[UITableViewAccessibility _axOffScreenOpaqueHeaderElementInDirection:options:childElement:].cold.1
- -[UITableViewAccessibility _axOffScreenOpaqueHeaderElementInDirection:options:childElement:].cold.2
- -[UITableViewAccessibility _axOpaqueHeaderElementInDirection:withinElements:startIndex:].cold.1
- -[UITableViewCellAccessibility _accessibilityChildren].cold.1
- -[UITableViewCellAccessibility _accessibilityHitTest:withEvent:].cold.1
- -[UITableViewCellAccessibility _accessibilityRetrieveTableViewCellTextWithLocalizationOptions:shouldExcludeDetailText:]
- -[UITableViewCellAccessibility accessibilityScrollToVisible].cold.1
- -[UITableViewCellAccessibility accessibilityScrollToVisible].cold.2
- -[UIViewAnimationStateAccessibility animationDidStart:].cold.1
- -[UIViewControllerAccessibility viewDidAppear:].cold.1
- -[UIViewControllerAccessibility viewDidDisappear:].cold.1
- -[UIWindowSceneAccessibility _accessibilityResetAndClearNativeFocusSystem].cold.1
- -[UIWindowSceneAccessibility _accessibilitySetFocusEnabledInApplication:].cold.1
- -[UIWindowSceneAccessibility _accessibilityUpdateNativeFocusImmediately].cold.1
- -[_UIScenePresentationViewAccessibility _accessibilitySetRemoteElementIfNecessary].cold.1
- GCC_except_table101
- GCC_except_table104
- GCC_except_table106
- GCC_except_table109
- GCC_except_table111
- GCC_except_table130
- GCC_except_table132
- GCC_except_table133
- GCC_except_table135
- GCC_except_table137
- GCC_except_table138
- GCC_except_table145
- GCC_except_table153
- GCC_except_table154
- GCC_except_table159
- GCC_except_table166
- GCC_except_table175
- GCC_except_table183
- GCC_except_table184
- GCC_except_table196
- GCC_except_table38
- GCC_except_table41
- GCC_except_table51
- GCC_except_table54
- GCC_except_table55
- GCC_except_table59
- GCC_except_table60
- GCC_except_table65
- GCC_except_table71
- GCC_except_table76
- GCC_except_table79
- GCC_except_table83
- GCC_except_table88
- GCC_except_table92
- _AVVoiceTriggerPort_BluetoothSpeaker_block_invoke.BaseImplementation
- _AVVoiceTriggerPort_BluetoothSpeaker_block_invoke.onceToken
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _UIAXNextKeyboardValue.cold.1
- _UIAXNextKeyboardValue.cold.2
- ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.721
- ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.722
- ___103-[UIApplicationAccessibility _accessibilityElementFirst:last:forFocus:allowScrolling:traversalOptions:]_block_invoke.723
- ___57-[UIViewAccessibility _accessibilitySortedElementsWithin]_block_invoke.cold.1
- ___57-[UIViewAccessibility _accessibilitySortedElementsWithin]_block_invoke_2.cold.1
- ___60-[UICollectionViewListCellAccessibility accessibilityTraits]_block_invoke
- ___60-[UICollectionViewListCellAccessibility accessibilityTraits]_block_invoke_2
- ___60-[UIScrollViewAccessibility _accessibilityLastOpaqueElement]_block_invoke.cold.1
- ___60-[UIScrollViewAccessibility _accessibilityLastOpaqueElement]_block_invoke_2.cold.1
- ___60-[UITextViewAccessibility _accessibilityUserTestingChildren]_block_invoke.495
- ___61-[UIScrollViewAccessibility _accessibilityFirstOpaqueElement]_block_invoke.cold.1
- ___61-[UIScrollViewAccessibility _accessibilityFirstOpaqueElement]_block_invoke_2.cold.1
- ___62-[UITableViewAccessibility _accessibilitySortedElementsWithin]_block_invoke.cold.1
- ___62-[UITableViewAccessibility _accessibilitySortedElementsWithin]_block_invoke_2.cold.1
- ___67-[UICollectionViewAccessibility _accessibilitySortedElementsWithin]_block_invoke.cold.1
- ___67-[UICollectionViewAccessibility _accessibilitySortedElementsWithin]_block_invoke_2.cold.1
- ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.246
- ___68-[UIAccessibilityPickerComponent _accessibilityDateTimePickerValues]_block_invoke.259
- ___68-[UIKeyboardImplAccessibility _axRegisterForVoiceOverNotifications:]_block_invoke.cold.1
- ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.485
- ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.485.cold.1
- ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.cold.1
- ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.486
- ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.486.cold.1
- ___69-[UIViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.cold.1
- ___71-[UIKeyboardLayoutStarAccessibility _accessibilityCreateElementForKey:]_block_invoke.cold.1
- ___71-[UITableViewCellAccessibility _accessibilityImplementsDefaultRowRange]_block_invoke.cold.1
- ___71-[UITableViewCellAccessibility _accessibilityImplementsDefaultRowRange]_block_invoke_2.cold.1
- ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke.355
- ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke.355.cold.1
- ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke.cold.1
- ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke_2.356
- ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke_2.356.cold.1
- ___72-[UIScrollViewAccessibility _accessibilityLastOpaqueElementWithOptions:]_block_invoke_2.cold.1
- ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.343
- ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.343.cold.1
- ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke.cold.1
- ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke_2.344
- ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke_2.344.cold.1
- ___73-[UIScrollViewAccessibility _accessibilityFirstOpaqueElementWithOptions:]_block_invoke_2.cold.1
- ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.627
- ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.627.cold.1
- ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.cold.1
- ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.628
- ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.628.cold.1
- ___74-[UITableViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.cold.1
- ___76-[UICollectionViewAccessibility accessibilityCreatePrepareCellForIndexPath:]_block_invoke.442
- ___76-[UICollectionViewCellAccessibility _accessibilityImplementsDefaultRowRange]_block_invoke.cold.1
- ___76-[UICollectionViewCellAccessibility _accessibilityImplementsDefaultRowRange]_block_invoke_2.cold.1
- ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.505
- ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.505.cold.1
- ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke.cold.1
- ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.506
- ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.506.cold.1
- ___79-[UICollectionViewAccessibility _accessibilitySortedElementsWithinWithOptions:]_block_invoke_2.cold.1
- ___80-[UITextInputUIResponderAccessibility _accessibilityInsertTextWithAlternatives:]_block_invoke.563
- ___82-[_UIRemoteDictionaryViewControllerAccessibility tableView:cellForRowAtIndexPath:]_block_invoke.273
- ___83-[_UIRemoteViewAccessibility _accessibilityTransmitRemoteUUIDToPid:machPort:value:]_block_invoke.cold.1
- ___88-[UIKeyboardEmojiCollectionViewAccessibility _accessibilityLocalizedVisibleSectionNames]_block_invoke.285
- ___89-[UITableViewAccessibility _axFirstLastOpaqueHeaderElementFromSection:options:direction:]_block_invoke.491
- ___89-[UITableViewAccessibility _axFirstLastOpaqueHeaderElementFromSection:options:direction:]_block_invoke.491.cold.1
- ___92-[UITableViewAccessibility _axOffScreenOpaqueHeaderElementInDirection:options:childElement:]_block_invoke.501
- ___93-[_UIRemoteViewControllerAccessibility _accessibilityLoadAccessibilityInformation:retryTime:]_block_invoke.312
- ___block_descriptor_32_e25_B16?0"UICellAccessory"8l
- ___block_literal_global.1846
- ___block_literal_global.231
- ___block_literal_global.234
- ___block_literal_global.235
- ___block_literal_global.239
- ___block_literal_global.2403
- ___block_literal_global.259
- ___block_literal_global.273
- ___block_literal_global.282
- ___block_literal_global.283
- ___block_literal_global.295
- ___block_literal_global.2993
- ___block_literal_global.2995
- ___block_literal_global.3000
- ___block_literal_global.3012
- ___block_literal_global.3014
- ___block_literal_global.3038
- ___block_literal_global.3046
- ___block_literal_global.331
- ___block_literal_global.334
- ___block_literal_global.339
- ___block_literal_global.341
- ___block_literal_global.342
- ___block_literal_global.346
- ___block_literal_global.350
- ___block_literal_global.353
- ___block_literal_global.358
- ___block_literal_global.360
- ___block_literal_global.363
- ___block_literal_global.365
- ___block_literal_global.373
- ___block_literal_global.376
- ___block_literal_global.387
- ___block_literal_global.395
- ___block_literal_global.424
- ___block_literal_global.425
- ___block_literal_global.426
- ___block_literal_global.448
- ___block_literal_global.450
- ___block_literal_global.461
- ___block_literal_global.479
- ___block_literal_global.481
- ___block_literal_global.484
- ___block_literal_global.488
- ___block_literal_global.504
- ___block_literal_global.508
- ___block_literal_global.518
- ___block_literal_global.528
- ___block_literal_global.530
- ___block_literal_global.540
- ___block_literal_global.552
- ___block_literal_global.556
- ___block_literal_global.565
- ___block_literal_global.572
- ___block_literal_global.575
- ___block_literal_global.577
- ___block_literal_global.590
- ___block_literal_global.591
- ___block_literal_global.595
- ___block_literal_global.600
- ___block_literal_global.613
- ___block_literal_global.626
- ___block_literal_global.630
- ___block_literal_global.650
- ___block_literal_global.661
- ___block_literal_global.664
- ___block_literal_global.680
- ___block_literal_global.709
- ___block_literal_global.778
- ___block_literal_global.829
- ___block_literal_global.831
- ___block_literal_global.872
- ___block_literal_global.874
- ___block_literal_global.887
- ___block_literal_global.890
- ___block_literal_global.892
- ___block_literal_global.907
- ___block_literal_global.912
- ___block_literal_global.934
- ___block_literal_global.943
- ___block_literal_global.977
- ___getEMFEmojiTokenClass_block_invoke.cold.1
- ___getEMFEmojiTokenClass_block_invoke.cold.2
- ___getRTIInputUIServiceMachNameiOSSymbolLoc_block_invoke.cold.1
- __unnamed_array_storage.253
- __unnamed_array_storage.320
- __unnamed_array_storage.390
- __unnamed_array_storage.400
- __unnamed_array_storage.401
- __unnamed_array_storage.950
- __unnamed_array_storage.957
- __unnamed_array_storage.958
- __unnamed_array_storage.972
- __unnamed_array_storage.973
- _getRTIInputUIServiceMachNameiOS.cold.1
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_accessibilityReorderMessageForNewIndexPath:swappedWithRow:movingDown:
- _objc_msgSend$_accessibilityRetrieveTableViewCellTextWithLocalizationOptions:shouldExcludeDetailText:
- _objc_msgSend$_interactionShouldBeginAtPlatformPoint:completion:
- _objc_msgSend$removeTarget:forEvents:
- _objc_msgSend$size
- _objc_release_x1
- _objc_release_x19
- _objc_release_x2
- _objc_release_x20
- _objc_release_x21
- _objc_release_x22
- _objc_release_x23
- _objc_release_x24
- _objc_release_x25
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_release_x8
- _objc_release_x9
- _objc_retain_x1
- _objc_retain_x19
- _objc_retain_x2
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ "@32@0:8q16B24B28"
+ "B36@0:8B16@20@28"
+ "Keyboard event handled - processed keyboardOutput: %@"
+ "Q72@?0{CGRect={CGPoint=dd}{CGSize=dd}}8{CGRect={CGPoint=dd}{CGSize=dd}}40"
+ "Starting keyboard task, blocking notifications: %{sensitive}@ - %@"
+ "Validated first responder: %{sensitive}@"
+ "_UICalendarHeaderTitleButton"
+ "_accessibilityRetrieveTableViewCellTextForReorderControl"
+ "_accessibilityRetrieveTableViewCellTextWithLocalizationOptions:shouldExcludeDetailText:forReorderControl:"
+ "_axReorderElementsByMovingIndexPaths:tableView:currentPath:"
+ "_hasEditingAccessoryView"
+ "_interactionShouldBeginAtPoint:completion:"
+ "_monthYearButton"
+ "beginUpdates"
+ "endUpdates"
+ "moveRowAtIndexPath:toIndexPath:"
- "AXTargetters"
- "B16@?0@\"UICellAccessory\"8"
- "Keyboard event handled - processed keyboardOutput: %@: %@"
- "Starting keyboard task, blocking notifications: %{private}@ - %@"
- "Validated first responder: %@"
- "_accessibilityReorderMessageForNewIndexPath:swappedWithRow:movingDown:"
- "_accessibilityRetrieveTableViewCellTextWithLocalizationOptions:shouldExcludeDetailText:"
- "_interactionShouldBeginAtPlatformPoint:completion:"
- "_monthYearContainer"
- "removeTarget:forEvents:"

```
