## MobileCal

> `/System/Library/AccessibilityBundles/MobileCal.axbundle/MobileCal`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xc874
-  __TEXT.__auth_stubs: 0x5e0
+3005.16.0.0.0
+  __TEXT.__text: 0xd0e8
+  __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_methlist: 0x15c0
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x1b8
-  __TEXT.__cstring: 0x2a1e
-  __TEXT.__unwind_info: 0x4e0
+  __TEXT.__gcc_except_tab: 0x1ac
+  __TEXT.__cstring: 0x2c94
+  __TEXT.__unwind_info: 0x4e8
   __TEXT.__objc_classname: 0xf42
   __TEXT.__objc_methname: 0x2559
   __TEXT.__objc_methtype: 0x51d

   __DATA_CONST.__objc_selrefs: 0xb00
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x118
-  __AUTH_CONST.__auth_got: 0x300
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x2c60
   __AUTH_CONST.__objc_const: 0x3a48

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1B1646AB-64FE-39F2-BBFF-1A1588C6E617
+  UUID: BBB4E367-2A5B-3144-8C8E-AF2C41005413
   Functions: 381
-  Symbols:   1727
+  Symbols:   1724
   CStrings:  1310
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
Functions:
~ +[AXMobileCalGlue accessibilityInitializeBundle] : 208 -> 216
~ ___48+[AXMobileCalGlue accessibilityInitializeBundle]_block_invoke : 852 -> 856
~ ___48+[AXMobileCalGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___48+[AXMobileCalGlue accessibilityInitializeBundle]_block_invoke_3 : 872 -> 880
~ ___48+[AXMobileCalGlue accessibilityInitializeBundle]_block_invoke_5 : 108 -> 112
~ __AXDateComponentsFromDate : 216 -> 228
~ __AXGetStringsForDate : 428 -> 436
~ ____AXGetStringsForDate_block_invoke : 128 -> 136
~ -[LargeYearMonthViewAccessibility _accessibilityHitTest:withEvent:] : 160 -> 164
~ +[MainWindowContentContainerViewControllerAccessibility _accessibilityPerformValidations:] : 304 -> 312
~ -[MainWindowContentContainerViewControllerAccessibility splitViewController:willChangeToDisplayMode:] : 184 -> 192
~ -[MainWindowContentContainerViewControllerAccessibility _accessibilitySetAccessibilityElements] : 292 -> 308
~ +[MainWindowRootViewControllerAccessibility _accessibilityPerformValidations:] : 564 -> 572
~ -[MainWindowRootViewControllerAccessibility _accessibilitySetAccessibilityElementsForDisplayMode:searchDisplayMode:] : 852 -> 920
~ -[MainWindowRootViewControllerAccessibility _accessibilityAddSwitcherSearchToAccessibilityViews:] : 176 -> 188
~ -[MainWindowRootViewControllerAccessibility _accessibilityAddSearchToAccessibilityViews:] : 536 -> 576
~ -[MainWindowRootViewControllerAccessibility _accessibilityRefreshSearchElementIfNeeded] : 144 -> 152
~ +[MainWindowControlHeaderViewAccessibility _accessibilityPerformValidations:] : 264 -> 272
~ -[MainWindowControlHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 276 -> 300
~ -[MainWindowControlHeaderViewAccessibility _accessibilitySetupBadgedButtonsLabelsValues] : 316 -> 344
~ -[CalendarMonthControlAccessibility _accessibilityUpdateOcurrenceTileCount:] : 800 -> 824
~ ___76-[CalendarMonthControlAccessibility _accessibilityUpdateOcurrenceTileCount:]_block_invoke_2 : 204 -> 208
~ ___76-[CalendarMonthControlAccessibility _accessibilityUpdateOcurrenceTileCount:]_block_invoke_4 : 124 -> 132
~ +[CUIKCalendarModelAccessibility__MobileCal__CalendarUIKit _accessibilityPerformValidations:] : 128 -> 140
~ -[CUIKCalendarModelAccessibility__MobileCal__CalendarUIKit setSelectedDate:] : 296 -> 312
~ -[CompactDayNavigationViewCellAccessibility accessibilityUserInputLabels] : 84 -> 92
~ +[CompactMonthViewControllerAccessibility _accessibilityPerformValidations:] : 224 -> 232
~ ___77-[CompactMonthViewControllerAccessibility showDate:animated:completionBlock:]_block_invoke : 156 -> 168
~ ___77-[CompactMonthViewControllerAccessibility showDate:animated:completionBlock:]_block_invoke_2 : 112 -> 116
~ +[CompactMonthWeekDayNumberAccessibility _accessibilityPerformValidations:] : 296 -> 304
~ -[CompactMonthWeekDayNumberAccessibility isAccessibilityElement] : 60 -> 64
~ -[CompactMonthWeekDayNumberAccessibility accessibilityFrame] : 192 -> 204
~ -[CompactMonthWeekDayNumberAccessibility accessibilityLabel] : 236 -> 264
~ -[CompactMonthWeekDayNumberAccessibility accessibilityUserInputLabels] : 200 -> 216
~ -[CompactMonthWeekDayNumberAccessibility accessibilityTraits] : 108 -> 112
~ -[CompactMonthWeekDayNumberAccessibility _axCalendarModel] : 264 -> 280
~ -[CompactMonthWeekDayNumberAccessibility _axEventStore] : 84 -> 92
~ -[CompactMonthWeekDayNumberAccessibility _axStringForNumberOfEvents:] : 124 -> 132
~ -[CompactMonthWeekDayNumberAccessibility accessibilityValue] : 496 -> 552
~ -[CompactMonthWeekDayNumberAccessibility accessibilityCustomContent] : 1056 -> 1152
~ -[CompactMonthWeekDayNumberAccessibility _accessibilityIsSpeakThisElement] : 96 -> 104
~ -[CompactMonthWeekDayNumberAccessibility(UIFocusConformance) focusGroupIdentifier] : 184 -> 212
~ -[CompactMonthWeekDayNumberAccessibility(UIFocusConformance) setNeedsFocusUpdate] : 100 -> 104
~ -[CompactMonthWeekDayNumberAccessibility(UIFocusConformance) updateFocusIfNeeded] : 96 -> 100
~ -[CompactMonthWeekDayNumberAccessibility(UIFocusConformance) didUpdateFocusInContext:withAnimationCoordinator:] : 156 -> 164
~ ___111-[CompactMonthWeekDayNumberAccessibility(UIFocusConformance) didUpdateFocusInContext:withAnimationCoordinator:]_block_invoke : 180 -> 188
~ -[CompactMonthWeekDayNumberAccessibility(UIFocusConformance) _preferredFocusRegionCoordinateSpace] : 100 -> 112
~ -[CompactMonthWeekDayNumberAccessibility(UIFocusConformance) focusItemsInRect:] : 436 -> 464
~ ___79-[CompactMonthWeekDayNumberAccessibility(UIFocusConformance) focusItemsInRect:]_block_invoke : 120 -> 124
~ +[CompactMonthWeekViewAccessibility _accessibilityPerformValidations:] : 540 -> 548
~ -[CompactMonthWeekViewAccessibility _axDate] : 92 -> 100
~ -[CompactMonthWeekViewAccessibility _axAnnotateMonthHeader] : 456 -> 496
~ -[CompactMonthWeekViewAccessibility _axAnnotateDayNumbers] : 252 -> 256
~ -[CompactMonthWeekViewAccessibility accessibilityElements] : 652 -> 688
~ -[CompactMonthWeekViewAccessibility accessibilityElementsHidden] : 304 -> 320
~ -[CompactMonthWeekViewAccessibility dealloc] : 280 -> 284
~ -[CompactMonthWeekViewAccessibility _accessibilityMonthViewController] : 160 -> 168
~ +[CompactWidthMonthViewControllerAccessibility _accessibilityPerformValidations:] : 516 -> 528
~ -[CompactWidthMonthViewControllerAccessibility showDate:animated:completionBlock:] : 228 -> 224
~ ___82-[CompactWidthMonthViewControllerAccessibility showDate:animated:completionBlock:]_block_invoke : 256 -> 268
~ ___82-[CompactWidthMonthViewControllerAccessibility showDate:animated:completionBlock:]_block_invoke_2 : 112 -> 116
~ -[CompactWidthMonthViewControllerAccessibility accessibilityScroll:] : 392 -> 408
~ ___68-[CompactWidthMonthViewControllerAccessibility accessibilityScroll:]_block_invoke : 300 -> 304
~ +[DayNavigationViewCellAccessibility _accessibilityPerformValidations:] : 160 -> 172
~ -[DayNavigationViewCellAccessibility accessibilityLabel] : 180 -> 196
~ -[DayNavigationViewCellAccessibility accessibilityHint] : 156 -> 168
~ +[DayNavigationViewControllerAccessibility _accessibilityPerformValidations:] : 304 -> 312
~ -[DayNavigationViewControllerAccessibility accessibilityScroll:] : 932 -> 924
~ ___64-[DayNavigationViewControllerAccessibility accessibilityScroll:]_block_invoke : 84 -> 88
~ +[DayNavigationWeekScrollViewAccessibility _accessibilityPerformValidations:] : 280 -> 288
~ -[DayNavigationWeekScrollViewAccessibility _axVisibleCells] : 336 -> 348
~ ___59-[DayNavigationWeekScrollViewAccessibility _axVisibleCells]_block_invoke : 348 -> 352
~ -[DayNavigationWeekScrollViewAccessibility accessibilityElementCount] : 56 -> 60
~ -[DayNavigationWeekScrollViewAccessibility indexOfAccessibilityElement:] : 88 -> 92
~ -[DayNavigationWeekScrollViewAccessibility accessibilityElementAtIndex:] : 84 -> 92
~ -[DayNavigationWeekScrollViewAccessibility _accessibilityScrollStatus] : 328 -> 340
~ ___70-[DayNavigationWeekScrollViewAccessibility _accessibilityScrollStatus]_block_invoke : 124 -> 132
~ -[DayNavigationWeekScrollViewAccessibility accessibilityScroll:] : 332 -> 340
~ ___64-[DayNavigationWeekScrollViewAccessibility accessibilityScroll:]_block_invoke : 100 -> 104
~ -[LargeTextLargeMonthWeekViewAccessibility _accessibilityHitTest:withEvent:] : 124 -> 128
~ -[DayViewControllerAccessibility _accessibilitySpeakThisElementsAndStrings] : 216 -> 228
~ +[LargeDayNavigationViewCellAccessibility _accessibilityPerformValidations:] : 116 -> 128
~ -[LargeDayNavigationViewCellAccessibility accessibilityUserInputLabels] : 384 -> 420
~ +[LargeMonthViewControllerAccessibility _accessibilityPerformValidations:] : 300 -> 308
~ -[LargeMonthViewControllerAccessibility _axTopWeekViewWithTopPoint:] : 364 -> 376
~ ___75-[LargeMonthViewControllerAccessibility showDate:animated:completionBlock:]_block_invoke : 216 -> 236
~ ___75-[LargeMonthViewControllerAccessibility showDate:animated:completionBlock:]_block_invoke_2 : 128 -> 132
~ +[LargeMonthWeekViewAccessibility _accessibilityPerformValidations:] : 748 -> 756
~ -[LargeMonthWeekViewAccessibility _axUpdateDayNumberLabels] : 1276 -> 1344
~ -[LargeMonthWeekViewAccessibility _axMonthHeader] : 152 -> 168
~ -[LargeMonthWeekViewAccessibility _axUpdateMonthAXLabel] : 192 -> 208
~ -[LargeMonthWeekViewAccessibility _accessibilityHitTest:withEvent:] : 124 -> 128
~ +[LargeWeekViewControllerAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ ___60-[LargeWeekViewControllerAccessibility selectDate:animated:]_block_invoke : 248 -> 264
~ ___60-[LargeWeekViewControllerAccessibility selectDate:animated:]_block_invoke_2 : 128 -> 132
~ -[ListTableViewAccessibility _accessibilityFirstContainedElementForTechnology:honoringGroups:shouldAlwaysScroll:] : 212 -> 228
~ +[ListViewControllerAccessibility _accessibilityPerformValidations:] : 240 -> 252
~ -[ListViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 116 -> 120
~ -[ListViewControllerAccessibility _accessibilityIsDateInCurrentYear:] : 396 -> 436
~ -[ListViewControllerAccessibility tableView:viewForHeaderInSection:] : 244 -> 256
~ ___68-[ListViewControllerAccessibility tableView:viewForHeaderInSection:]_block_invoke : 188 -> 200
~ _accessibilityLocalizedString : 156 -> 164
~ +[MonthViewControllerAccessibility _accessibilityPerformValidations:] : 396 -> 404
~ -[MonthViewControllerAccessibility _axTopWeekViewWithTopPoint:] : 456 -> 472
~ -[MonthViewControllerAccessibility accessibilityScrollStatusForScrollView:] : 156 -> 172
~ -[MonthViewControllerAccessibility _axAnnotateView] : 132 -> 140
~ -[MonthViewControllerAccessibility scrollView] : 136 -> 144
~ -[MonthViewControllerAccessibility eventGestureController:setUpAtPoint:withOccurrence:forceNewEvent:] : 476 -> 500
~ -[MonthViewControllerAccessibility _updateDraggingOffsetTimesForPoint:] : 592 -> 640
~ +[RootNavigationControllerAccessibility _accessibilityPerformValidations:] : 336 -> 344
~ -[RootNavigationControllerAccessibility _accessibilityLoadAccessibilityInformation] : 472 -> 484
~ ___83-[RootNavigationControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 76 -> 80
~ ___83-[RootNavigationControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 76 -> 80
~ -[RootNavigationControllerAccessibility todayPressed] : 428 -> 432
~ ___53-[RootNavigationControllerAccessibility todayPressed]_block_invoke : 272 -> 276
~ -[RootNavigationControllerAccessibility _compactMonthDividedListSwitchBarButtonItem] : 128 -> 136
~ -[RootNavigationControllerAccessibility _axCurrentDayViewMode] : 84 -> 88
~ -[RootNavigationControllerAccessibility _axCurrentMonthViewMode] : 184 -> 196
~ -[RootNavigationControllerAccessibility _listViewSwitchBarButtonItem] : 244 -> 248
~ ___69-[RootNavigationControllerAccessibility _listViewSwitchBarButtonItem]_block_invoke : 76 -> 80
~ +[SearchResultsViewControllerAccessibility _accessibilityPerformValidations:] : 144 -> 152
~ -[SearchResultsViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 132 -> 140
~ -[SplashScreenViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 156 -> 164
~ -[MobileCalUIAccessibilityElementMockViewAccessibility accessibilityActivate] : 136 -> 144
~ +[MobileCalUIDimmingViewAccessibility _accessibilityPerformValidations:] : 104 -> 112
~ -[MobileCalUIDimmingViewAccessibility _accessibilityObscuredScreenAllowedViews] : 332 -> 348
~ +[MobileCalUIScrollViewAccessibility _accessibilityPerformValidations:] : 112 -> 120
~ -[MobileCalUIScrollViewAccessibility _accessibilityVisibleContentInset] : 388 -> 408
~ -[MobileCalUIScrollViewAccessibility _accessibilityDrawsFocusRingWhenChildrenFocused] : 84 -> 88
~ -[MobileCalUIScrollViewAccessibility _accessibilityFirstContainedElementForTechnology:honoringGroups:shouldAlwaysScroll:] : 260 -> 276
~ +[MobileCalUITransitionViewAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[MobileCalUITransitionViewAccessibility _accessibilityObscuredScreenAllowedViews] : 576 -> 608
~ -[MobileCalUIViewAccessibility _accessibilitySupportsContentSizeCategory:] : 312 -> 320
~ -[MobileCalUIViewAccessibility _accessibilityDrawsFocusRingWhenChildrenFocused] : 148 -> 156
~ -[WeekAllDayLabelAccessibilityElement accessibilityFrame] : 244 -> 260
~ -[WeekAllDayDayContainerAccessibilityElement dealloc] : 272 -> 276
~ -[WeekAllDayDayContainerAccessibilityElement accessibilityContainerType] : 156 -> 168
~ -[WeekAllDayDayContainerAccessibilityElement accessibilityLabel] : 76 -> 84
~ -[WeekAllDayDayContainerAccessibilityElement accessibilityFrame] : 196 -> 204
~ -[WeekAllDayDayContainerAccessibilityElement setDate:] : 20 -> 80
~ +[WeekAllDayViewAccessibility _accessibilityPerformValidations:] : 272 -> 280
~ -[WeekAllDayViewAccessibility accessibilityElements] : 1420 -> 1532
~ +[WeekViewAccessibility _accessibilityPerformValidations:] : 376 -> 384
~ -[WeekViewAccessibility _axAnnotateScrollView] : 84 -> 88
~ -[WeekViewAccessibility accessibilityElements] : 496 -> 532
~ -[WeekViewAccessibility accessibilityCustomRotors] : 420 -> 432
~ ___50-[WeekViewAccessibility accessibilityCustomRotors]_block_invoke : 304 -> 324
~ +[WeekViewControllerAccessibility _accessibilityPerformValidations:] : 300 -> 308
~ -[WeekViewControllerAccessibility _axAnnotateWeekScroller] : 96 -> 100
~ -[WeekViewControllerAccessibility accessibilityScrollStatusForScrollView:] : 1160 -> 1188
~ ___74-[WeekViewControllerAccessibility accessibilityScrollStatusForScrollView:]_block_invoke.331 : 80 -> 84
~ +[YearMonthAnimatorAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ +[YearViewControllerAccessibility _accessibilityPerformValidations:] : 300 -> 308
~ -[YearViewControllerAccessibility _axAnnotateView] : 132 -> 140
~ -[YearViewControllerAccessibility accessibilityScrollStatusForScrollView:] : 204 -> 216
~ -[YearViewControllerAccessibility showDate:animated:completionBlock:] : 228 -> 224
~ ___69-[YearViewControllerAccessibility showDate:animated:completionBlock:]_block_invoke : 188 -> 196
~ ___69-[YearViewControllerAccessibility showDate:animated:completionBlock:]_block_invoke_2 : 128 -> 132
~ -[YearViewControllerAccessibility scrollView] : 136 -> 144
~ +[YearViewYearHeaderAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ -[YearViewYearHeaderAccessibility _axAnnotateYearNumber] : 108 -> 112
~ +[InfiniteScrollViewControllerAccessibility _accessibilityPerformValidations:] : 112 -> 120
~ -[InfiniteScrollViewControllerAccessibility _axAnnotateViews] : 88 -> 92
CStrings:
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/CompactMonthWeekDayNumberAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/CompactMonthWeekViewAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/CompactWidthMonthViewControllerAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/DayNavigationViewControllerAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/LargeMonthWeekViewAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/MonthViewControllerAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/UIScrollViewAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/WeekViewAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/WeekViewControllerAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/YearViewControllerAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/CompactMonthWeekDayNumberAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/CompactMonthWeekViewAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/CompactWidthMonthViewControllerAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/DayNavigationViewControllerAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/LargeMonthWeekViewAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/MonthViewControllerAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/UIScrollViewAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/WeekViewAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/WeekViewControllerAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/MobileCalAccessibility/Accessibility/YearViewControllerAccessibility.m"

```
