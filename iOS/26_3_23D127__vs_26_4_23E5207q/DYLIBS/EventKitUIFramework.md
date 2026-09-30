## EventKitUIFramework

> `/System/Library/AccessibilityBundles/EventKitUIFramework.axbundle/EventKitUIFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xea24
-  __TEXT.__auth_stubs: 0x6e0
+3005.16.0.0.0
+  __TEXT.__text: 0xf6a8
+  __TEXT.__auth_stubs: 0x660
   __TEXT.__objc_methlist: 0x176c
-  __TEXT.__cstring: 0x2c49
+  __TEXT.__cstring: 0x2d84
   __TEXT.__const: 0x38
   __TEXT.__oslogstring: 0x40
-  __TEXT.__gcc_except_tab: 0x218
+  __TEXT.__gcc_except_tab: 0x214
   __TEXT.__dlopen_cstrs: 0x51
-  __TEXT.__unwind_info: 0x550
+  __TEXT.__unwind_info: 0x568
   __TEXT.__objc_classname: 0x11dd
   __TEXT.__objc_methname: 0x228b
   __TEXT.__objc_methtype: 0x333

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa88
   __DATA_CONST.__objc_superrefs: 0x130
-  __AUTH_CONST.__auth_got: 0x380
+  __AUTH_CONST.__auth_got: 0x340
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x3560
   __AUTH_CONST.__objc_const: 0x40c8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 49A6C129-E7DC-3B81-99AB-B61C92C335FF
+  UUID: 7536EDD3-47AE-375E-95D5-4C07842DB0FD
   Functions: 443
-  Symbols:   1966
+  Symbols:   1958
   CStrings:  1418
 
Symbols:
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
- _objc_retain_x9
Functions:
~ +[AXEventKitUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___49+[AXEventKitUIGlue accessibilityInitializeBundle]_block_invoke : 660 -> 664
~ ___49+[AXEventKitUIGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___49+[AXEventKitUIGlue accessibilityInitializeBundle]_block_invoke_3 : 1092 -> 1100
~ -[EKEvent(AccessibilityUtilities) _accessibilityDurationString] : 660 -> 756
~ -[NSDate(AccessibilityUtilities) _accessibilityTimeString] : 128 -> 136
~ -[UIView(AccessibilityDragAndDrop) _accessibilityDragAndDropTargetViewForDrop:eventGestureController:] : 480 -> 488
~ +[EKReminderTitleDetailCellAccessibility _accessibilityPerformValidations:] : 144 -> 152
~ -[EKReminderTitleDetailCellAccessibility _axEvent] : 132 -> 140
~ -[EKReminderTitleDetailCellAccessibility accessibilityActivationPoint] : 72 -> 76
~ -[EKReminderTitleDetailCellAccessibility accessibilityLabel] : 224 -> 240
~ ___60-[EKReminderTitleDetailCellAccessibility accessibilityLabel]_block_invoke : 116 -> 124
~ -[EKReminderTitleDetailCellAccessibility accessibilityValue] : 100 -> 108
~ -[EKReminderTitleDetailCellAccessibility accessibilityHint] : 124 -> 132
~ +[EKUIListViewTimedEventCellAccessibility _accessibilityPerformValidations:] : 300 -> 308
~ -[EKUIListViewTimedEventCellAccessibility _axSafeLabelForUILabelKey:] : 188 -> 200
~ -[EKUIListViewTimedEventCellAccessibility accessibilityLabel] : 600 -> 656
~ -[EKUIListViewTimedEventCellAccessibility accessibilityValue] : 184 -> 196
~ -[EKUIListViewTimedEventCellAccessibility updateWithEvent:isMultiday:occurrenceStartDate:dimmed:] : 148 -> 144
~ -[EKUIPopupTableViewCellAccessibility accessibilityValue] : 84 -> 92
~ +[EKUIParticipantContainerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[EKUIParticipantContainerAccessibility accessibilityLabel] : 188 -> 208
~ -[EKUIAvailabilityFreeSpanViewAccessibility accessibilityLabel] : 92 -> 100
~ +[EKUIAvailabilityViewControllerAccessibility _accessibilityPerformValidations:] : 152 -> 160
~ -[EKUIAvailabilityViewControllerAccessibility _accessibilitySetup] : 204 -> 212
~ ___66-[EKUIAvailabilityViewControllerAccessibility _accessibilitySetup]_block_invoke : 136 -> 144
~ -[EKUIAvailabilityViewControllerAccessibility layout] : 120 -> 124
~ +[CalendarMessageUIProxyAccessibility _accessibilityPerformValidations:] : 268 -> 280
~ +[CalendarMessageUIProxyAccessibility CalendarComposeRecipientClass] : 92 -> 96
~ +[CalendarMessageUIProxyAccessibility MailComposeRecipientClass] : 92 -> 96
~ +[CalendarMessageUIProxyAccessibility ComposeRecipientViewClass] : 92 -> 96
~ +[CalendarMessageUIProxyAccessibility RecipientTableViewCellClass] : 92 -> 96
~ +[CalendarMessageUIProxyAccessibility SearchShadowViewClass] : 92 -> 96
~ +[CalendarMessageUIProxyAccessibility MFContactsSearchManagerClass] : 92 -> 96
~ +[CalendarMessageUIProxyAccessibility MFContactsSearchResultsModelClass] : 92 -> 96
~ _LoadMessageUI : 112 -> 116
~ _MobileCalAXLocalizedString : 156 -> 164
~ _accessibilityLocalizedString : 156 -> 164
~ _accessibilityCalendarTitleForEventIfNecessary : 544 -> 576
~ -[EKCalendarChooserCellAccessibility accessibilityTraits] : 260 -> 268
~ +[EKDateTimeCellAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[EKDateTimeCellAccessibility accessibilityLabel] : 400 -> 452
~ -[EKCalendarItemCalendarEditItemAccessibility cellForSubitemAtIndex:] : 160 -> 176
~ -[EKCalendarItemEditorAccessibility tableView:cellForRowAtIndexPath:] : 176 -> 188
~ -[EKEventEditorAccessibility _accessibilityLoadAccessibilityInformation] : 180 -> 188
~ +[EKCalendarItemLocationInlineEditItemAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[EKCalendarItemLocationInlineEditItemAccessibility cellForSubitemAtIndex:] : 120 -> 124
~ -[EKCalendarItemLocationInlineEditItemAccessibility _updateClearButtonAndMakeVisible:index:] : 136 -> 140
~ +[EKDayAllDayViewAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[EKDayAllDayViewAccessibility _axAnnotateAllDayLabel] : 96 -> 100
~ -[MobileCalDayPlaceholderElement accessibilityFrame] : 132 -> 140
~ -[MobileCalHourAccessibilityElement accessibilityLabel] : 492 -> 536
~ -[MobileCalHourAccessibilityElement accessibilityUserInputLabels] : 200 -> 224
~ -[MobileCalHourAccessibilityElement _frameInDayGridView] : 428 -> 464
~ -[MobileCalHourAccessibilityElement accessibilityFrame] : 112 -> 116
~ -[MobileCalHourAccessibilityElement isAccessibilityElement] : 220 -> 228
~ -[MobileCalHourAccessibilityElement accessibilityFrameForScrolling] : 388 -> 404
~ -[MobileCalHourAccessibilityElement accessibilityDropPointDescriptors] : 612 -> 656
~ -[MobileCalHourAccessibilityElement setHourDate:] : 20 -> 80
~ -[MobileCalOccurrencyContainerAccessibilityElement dealloc] : 272 -> 276
~ -[MobileCalOccurrencyContainerAccessibilityElement accessibilityFrame] : 264 -> 284
~ -[MobileCalOccurrencyContainerAccessibilityElement setChildren:] : 20 -> 80
~ -[MobileCalDayContainerAccessibilityElement dealloc] : 272 -> 276
~ -[MobileCalDayContainerAccessibilityElement accessibilityLabel] : 228 -> 248
~ -[MobileCalDayContainerAccessibilityElement accessibilityFrame] : 212 -> 224
~ -[MobileCalDayContainerAccessibilityElement _accessibilityHitTest:withEvent:] : 616 -> 640
~ -[MobileCalDayContainerAccessibilityElement setChildren:] : 20 -> 80
~ -[MobileCalDayContainerAccessibilityElement setDate:] : 20 -> 80
~ +[EKDayGridViewAccessibility _accessibilityPerformValidations:] : 220 -> 228
~ -[EKDayGridViewAccessibility _axResetChildren] : 568 -> 576
~ -[EKDayGridViewAccessibility _accessibilityHideEmptyHours] : 76 -> 80
~ -[EKDayGridViewAccessibility accessibilityElements] : 3348 -> 3540
~ ___51-[EKDayGridViewAccessibility accessibilityElements]_block_invoke : 80 -> 84
~ -[EKDayGridViewAccessibility dealloc] : 108 -> 112
~ -[EKDayOccurrenceResizeHandleViewAccessibility _axIsStartHandle] : 64 -> 68
~ -[EKDayOccurrenceResizeHandleViewAccessibility _axIsEndHandle] : 64 -> 68
~ -[EKDayOccurrenceResizeHandleViewAccessibility accessibilityLabel] : 104 -> 108
~ -[EKDayOccurrenceResizeHandleViewAccessibility accessibilityHint] : 104 -> 108
~ +[DayTwoPartLabelAccessibility _accessibilityPerformValidations:] : 200 -> 208
~ -[DayTwoPartLabelAccessibility accessibilityLabel] : 236 -> 256
~ +[EKDayOccurrenceViewAccessibility _accessibilityPerformValidations:] : 852 -> 860
~ -[EKDayOccurrenceViewAccessibility _axIsInPreview] : 80 -> 84
~ -[EKDayOccurrenceViewAccessibility isAccessibilityElement] : 152 -> 160
~ -[EKDayOccurrenceViewAccessibility accessibilityFrameForScrolling] : 324 -> 340
~ -[EKDayOccurrenceViewAccessibility accessibilityLabel] : 1600 -> 1768
~ -[EKDayOccurrenceViewAccessibility accessibilityUserInputLabels] : 204 -> 220
~ -[EKDayOccurrenceViewAccessibility _accessibilitySupplementaryFooterViews] : 192 -> 204
~ -[EKDayOccurrenceViewAccessibility _accessibilitySupplementaryHeaderViews] : 192 -> 204
~ -[EKDayOccurrenceViewAccessibility setDrawsResizeHandles:] : 200 -> 208
~ -[EKDayOccurrenceViewAccessibility _axDraggingView] : 532 -> 572
~ -[EKDayOccurrenceViewAccessibility accessibilityCustomRotors] : 452 -> 468
~ ___61-[EKDayOccurrenceViewAccessibility accessibilityCustomRotors]_block_invoke : 236 -> 252
~ -[EKDayOccurrenceViewAccessibility accessibilityTraits] : 244 -> 248
~ -[EKDayOccurrenceViewAccessibility _accessibilityIsInWidget] : 52 -> 56
~ -[EKDayOccurrenceViewAccessibility accessibilityHint] : 148 -> 156
~ -[EKDayOccurrenceViewAccessibility accessibilityDragSourceDescriptors] : 456 -> 476
~ -[EKDayOccurrenceViewAccessibility accessibilityDropPointDescriptors] : 156 -> 172
~ -[EKDayOccurrenceViewAccessibility canBecomeFocused] : 216 -> 232
~ ___52-[EKDayOccurrenceViewAccessibility canBecomeFocused]_block_invoke : 80 -> 84
~ +[EKDayPreviewControllerAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[EKDayPreviewControllerAccessibility _axAnnotateDayView] : 368 -> 396
~ +[EKEventDetailTextCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[EKEventDetailTextCellAccessibility accessibilityValue] : 124 -> 140
~ -[EKEventDetailTextCellAccessibility _accessibilityDataDetectorScheme:] : 176 -> 188
~ -[EKEventDetailTextCellAccessibility _accessibilityLineNumberAndColumnForPoint:] : 108 -> 116
~ -[EKEventDetailTextCellAccessibility _accessibilityRangeForLineNumberAndColumn:] : 104 -> 108
~ -[EKEventDetailTextCellAccessibility _accessibilityChargedLineBoundsForRange:] : 128 -> 132
~ -[EKEventDetailTextCellAccessibility _accessibilityBoundsForRange:] : 128 -> 132
~ -[EKEventDetailTextCellAccessibility _accessibilityInternalTextLinks] : 84 -> 92
~ +[EKDayViewAccessibility _accessibilityPerformValidations:] : 292 -> 300
~ -[EKDayViewAccessibility accessibilityScrollView] : 52 -> 68
~ -[EKDayViewAccessibility _axAnnotateScroller] : 148 -> 156
~ -[EKDayViewAccessibility accessibilityCustomRotors] : 420 -> 432
~ ___51-[EKDayViewAccessibility accessibilityCustomRotors]_block_invoke : 304 -> 324
~ +[EKDayViewContentAccessibility _accessibilityPerformValidations:] : 180 -> 188
~ -[EKDayViewContentAccessibility applyLoadedOccurrencesWithBatching:animated:reverse:completion:] : 188 -> 192
~ -[EKDayViewContentAccessibility _accessibilityLoadAccessibilityInformation] : 428 -> 432
~ +[EKDayViewContentItemAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ -[EKDayViewContentItemAccessibility _axAnnotateOccurrenceView] : 200 -> 212
~ +[EKDayViewControllerAccessibility _accessibilityPerformValidations:] : 276 -> 284
~ -[EKDayViewControllerAccessibility _axDayString] : 180 -> 200
~ -[EKDayViewControllerAccessibility accessibilityScroll:] : 284 -> 316
~ -[EKDayViewControllerAccessibility _scrollViewDidEndDecelerating:] : 108 -> 112
~ -[EKDayViewControllerAccessibility _relayoutDaysDuringScrolling] : 268 -> 280
~ -[EKDayViewControllerAccessibility accessibilityScrollStatusForScrollView:] : 176 -> 196
~ -[EKEventAttachmentsEditItemAccessibility cellForSubitemAtIndex:] : 120 -> 124
~ -[EKEventCalendarDetailItemAccessibility cellForSubitemAtIndex:withTraitCollection:] : 268 -> 288
~ +[EKEventDateEditItemAccessibility _accessibilityPerformValidations:] : 476 -> 484
~ -[EKEventDateEditItemAccessibility _accessibilityLoadAccessibilityInformation] : 152 -> 156
~ ___60-[EKEventDateEditItemAccessibility editor:didSelectSubitem:]_block_invoke : 608 -> 628
~ -[EKEventDateEditItemAccessibility _axUpdateEndDateCellLabel] : 156 -> 164
~ -[EKEventDateEditItemAccessibility _accessibilitySetupDateCellForKey:] : 220 -> 240
~ +[EKEventDetailAttendeesCellAccessibility _accessibilityPerformValidations:] : 224 -> 232
~ -[EKEventDetailAttendeesCellAccessibility _axStringForParticipants:] : 636 -> 672
~ -[EKEventDetailAttendeesCellAccessibility accessibilityLabel] : 188 -> 208
~ -[EKEventDetailAttendeesCellAccessibility accessibilityValue] : 1876 -> 1956
~ ___61-[EKEventDetailAttendeesCellAccessibility accessibilityValue]_block_invoke : 80 -> 84
~ ___61-[EKEventDetailAttendeesCellAccessibility accessibilityValue]_block_invoke_2 : 80 -> 84
~ ___61-[EKEventDetailAttendeesCellAccessibility accessibilityValue]_block_invoke_3 : 80 -> 84
~ ___61-[EKEventDetailAttendeesCellAccessibility accessibilityValue]_block_invoke_4 : 80 -> 84
~ +[EKEventDetailTitleCellAccessibility _accessibilityPerformValidations:] : 632 -> 640
~ -[EKEventDetailTitleCellAccessibility _axAnnotateLocationViewsIfNeeded] : 572 -> 592
~ -[EKEventDetailTitleCellAccessibility accessibilityCustomActions] : 1080 -> 1140
~ ___93-[EKEventDetailTitleCellAccessibility _addCustomActionToActionsArray:forControl:actionBlock:]_block_invoke : 128 -> 136
~ -[EKEventDetailTitleCellAccessibility accessibilityCustomContent] : 1660 -> 1812
~ _getAXCustomContentClass : 224 -> 220
~ -[EKEventDetailTitleCellAccessibility accessibilityLabel] : 84 -> 92
~ -[EKEventDetailTitleCellAccessibility _accessibilitySupplementaryFooterViews] : 192 -> 212
~ ___107-[EKEventDetailTitleCellAccessibility _accessibilityImageLabelforAttributedLocationName:andLocationStatus:]_block_invoke : 88 -> 92
~ +[EKEventEstimatedTravelTimeResultCellAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[EKEventEstimatedTravelTimeResultCellAccessibility accessibilityLabel] : 424 -> 464
~ +[EKEventGestureControllerAccessibility _accessibilityPerformValidations:] : 468 -> 480
~ -[EKEventGestureControllerAccessibility _longPress:] : 184 -> 188
~ -[EKEventGestureControllerAccessibility _update] : 1060 -> 1108
~ -[EKEventGestureControllerAccessibility _commit] : 420 -> 452
~ -[EKEventGestureControllerAccessibility _speakNotificationIfNecessary:shouldSpeakWithoutInterruption:shouldSpeakOnlyIfNotSpeaking:] : 180 -> 188
~ -[EKEventGestureControllerAccessibility _createTemporaryView:animated:] : 100 -> 104
~ +[EKEventViewControllerDefaultImplAccessibility _accessibilityPerformValidations:] : 124 -> 136
~ -[EKEventViewControllerDefaultImplAccessibility _accessibilityLoadAccessibilityInformation] : 188 -> 196
~ -[EKExpandingTextViewAccessibility accessibilityLabel] : 208 -> 228
~ +[EKEventConferenceInformationDetailItemAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ -[EKEventConferenceInformationDetailItemAccessibility _accessibilityLoadAccessibilityInformation] : 224 -> 240
~ -[EKEventConferenceInformationDetailItemAccessibility cellForSubitemAtIndex:] : 104 -> 108
~ +[EKTextViewWithLabelTextMetricsAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ -[EKTextViewWithLabelTextMetricsAccessibility _axLocationItem] : 180 -> 188
~ -[EKTextViewWithLabelTextMetricsAccessibility accessibilityIsLocationLink] : 384 -> 400
~ -[EKTextViewWithLabelTextMetricsAccessibility isAccessibilityElement] : 104 -> 108
~ -[EKTextViewWithLabelTextMetricsAccessibility accessibilityFrame] : 148 -> 152
~ -[EKTextViewWithLabelTextMetricsAccessibility accessibilityLabel] : 168 -> 184
~ +[EKUIDividedGridViewCellAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ +[EKUIDividedGridViewTableViewCellAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[EKUIEventInviteesViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 164 -> 176
~ +[EKUIInviteesViewInviteesCellAccessibility _accessibilityPerformValidations:] : 264 -> 272
~ -[EKUIInviteesViewInviteesCellAccessibility updateWithParticipantForSorting:availabilityType:hideStatus:showSpinner:animated:] : 536 -> 568
~ -[EKUIInviteesViewInviteesCellAccessibility accessibilityValue] : 84 -> 92
~ -[EKUIInviteesViewInviteesCellAccessibility updateWithParticipantForSorting:hideStatus:] : 440 -> 472
~ +[EKUIInviteesViewTimeSlotCellAccessibility _accessibilityPerformValidations:] : 264 -> 272
~ -[EKUIInviteesViewTimeSlotCellAccessibility accessibilityLabel] : 212 -> 232
~ -[EKUIInviteesViewTimeSlotCellAccessibility _accessibilityLoadAccessibilityInformation] : 104 -> 108
~ -[UILabelAccessibility__EventKitUI__UIKit _accessibilitySupportsContentSizeCategory:] : 212 -> 216
~ +[EKUIYearMonthViewAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[EKUIYearMonthViewAccessibility _axIsCurrentMonth] : 68 -> 72
~ -[EKUIYearMonthViewAccessibility accessibilityLabel] : 264 -> 288
~ -[EKUIYearMonthViewAccessibility accessibilityUserInputLabels] : 200 -> 216
~ +[PreferencesTwoPartValueCellAccessibility _accessibilityPerformValidations:] : 248 -> 260
~ -[PreferencesTwoPartValueCellAccessibility accessibilityLabel] : 224 -> 248
~ -[PreferencesTwoPartValueCellAccessibility accessibilityUserInputLabels] : 108 -> 120
~ +[PreferencesDoubleTwoPartValueCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[PreferencesDoubleTwoPartValueCellAccessibility accessibilityLabel] : 228 -> 252
~ -[TwoPartTextLabelAccessibility accessibilityLabel] : 164 -> 176
~ +[UIScrollViewAccessibility_EventKit_UIKit _accessibilityPerformValidations:] : 224 -> 232
~ -[UIScrollViewAccessibility_EventKit_UIKit _accessibilityScrollStatus] : 664 -> 712
~ ___getAXCustomContentClass_block_invoke.cold.1 : 124 -> 132
~ ___getAXCustomContentClass_block_invoke.cold.2 : 128 -> 136
CStrings:
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/EventKitUIFrameworkAccessibility/Accessibility/EKDayGridViewAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/EventKitUIFrameworkAccessibility/Accessibility/EKDayOccurrenceViewAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/EventKitUIFrameworkAccessibility/Accessibility/EKEventDetailAttendeesCellAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/EventKitUIFrameworkAccessibility/Accessibility/EKEventEstimatedTravelTimeResultCellAccessibility.m"
+ "/Library/Caches/com.apple.xbs/E25FCDA8-0196-4EAD-B0B7-2A401D22FFAB/TemporaryDirectory.MA9nBj/Sources/AccessibilityBundles_Alias4/EventKitUIFrameworkAccessibility/Accessibility/UIScrollViewAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/EventKitUIFrameworkAccessibility/Accessibility/EKDayGridViewAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/EventKitUIFrameworkAccessibility/Accessibility/EKDayOccurrenceViewAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/EventKitUIFrameworkAccessibility/Accessibility/EKEventDetailAttendeesCellAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/EventKitUIFrameworkAccessibility/Accessibility/EKEventEstimatedTravelTimeResultCellAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias4/EventKitUIFrameworkAccessibility/Accessibility/UIScrollViewAccessibility.m"

```
