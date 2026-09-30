## com.apple.CalendarUI

> `/System/Library/Accessibility/BundlesBase/com.apple.CalendarUI.axbundle/Versions/A/com.apple.CalendarUI`

```diff

-287.6.0.0.0
-  __TEXT.__text: 0xa8e8
+287.6.4.0.0
+  __TEXT.__text: 0xa9d4
   __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_stubs: 0x19a0
-  __TEXT.__objc_methlist: 0xe4c
+  __TEXT.__objc_methlist: 0xf94
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x2f4
   __TEXT.__objc_classname: 0xb55

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2ce0
-  __DATA.__objc_selrefs: 0x808
+  __DATA.__objc_const: 0x2a80
+  __DATA.__objc_selrefs: 0x898
   __DATA.__objc_data: 0x1680
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ABB0FE30-FF46-3726-B406-2D3CCB611575
+  UUID: B5FC7603-80E8-365B-A5EE-AF39ED0BEE38
   Functions: 307
   Symbols:   1032
   CStrings:  874
Functions:
~ -[EKUIAlarmButtonAccessibility isHidden] : 76 -> 80
~ -[EKUIAlarmButtonAccessibility resignFirstResponder] : 160 -> 164
~ -[CalUITextFieldEditorAccessibility _axcWindow] : 168 -> 172
~ -[EKUIAttendeesGadgetAccessibility control:textView:doCommandBySelector:] : 996 -> 992
~ -[EKUITokenButtonAccessibility accessibilityLabel] : 820 -> 832
~ -[EKUITokenButtonAccessibility accessibilityPerformPress] : 492 -> 496
~ -[CalUIDayViewAllDayViewAccessibility _axcAllDayLabel] : 332 -> 336
~ -[CalUIDayViewAllDayViewAccessibility _axcAllDayEvents] : 540 -> 544
~ -[CalUITextFieldCellAccessibility _axcFieldEditor] : 168 -> 172
~ -[CalUITextFieldCellAccessibility _axcControlView] : 216 -> 224
~ -[CalUITextFieldCellAccessibility isAccessibilityFocused] : 436 -> 432
~ -[CalUITextFieldCellAccessibility accessibilitySelectedTextRange] : 460 -> 464
~ -[CalUITextFieldCellAccessibility setAccessibilitySelectedTextRange:] : 368 -> 372
~ -[CalUITextFieldCellAccessibility setAccessibilityFocused:] : 560 -> 564
~ -[CalUITextFieldCellAccessibility isAccessibilitySelectorAllowed:] : 384 -> 392
~ -[CalUIDateItemViewAccessibility initWithDelegate:date:unit:] : 668 -> 672
~ -[EKUIAttachmentTableViewAccessibility accessibilitySelectedRows] : 288 -> 292
~ -[EKUIAttachmentTableViewAccessibility _axcSelectedCell] : 368 -> 384
~ -[CalUIAXMiniMonthProxyAccessibility _axcMonthView] : 200 -> 204
~ -[EKUIEndRepeatGadgetAccessibility _axcLabel] : 332 -> 336
~ -[EKUIEndRepeatGadgetAccessibility _axcDatePicker] : 168 -> 172
~ -[EKUIEndRepeatGadgetAccessibility _axcNumberOfTimesField] : 168 -> 172
~ -[EKUIEndRepeatGadgetAccessibility _axcEndRepeatTypePicker] : 168 -> 172
~ -[EKUIEndRepeatGadgetAccessibility addSubviewsIfNeeded] : 584 -> 588
~ -[CalUIVoiceOverFriendlyMatrixAccessibility accessibilityLabel] : 240 -> 244
~ -[CalUIVoiceOverFriendlyMatrixAccessibility accessibilityArrayAttributeCount:] : 216 -> 220
~ -[CalUIVoiceOverFriendlyMatrixAccessibility accessibilitySelectedChildren] : 392 -> 396
~ -[CalUIVoiceOverFriendlyMatrixAccessibility _axcHideUnusedDayCells] : 256 -> 260
~ -[EKUIAlarmGadgetAccessibility _axcAlarmPicker] : 332 -> 336
~ -[EKUIRecurrenceSummaryGadgetAccessibility _accessibilityLoadAccessibilityInformation] : 344 -> 352
~ -[CalUIColorPickerButtonAccessibility _axcHumanReadableColorName] : 256 -> 260
~ -[CalUIColorPickerButtonAccessibility _axcInitAccessibility] : 228 -> 232
~ -[EKUIAttachmentCellViewAccessibility _axcTokenField:menuForRepresentedObject:] : 448 -> 452
~ -[EKUIAttachmentCellViewAccessibility _axcTokenField:displayStringForRepresentedObject:] : 384 -> 388
~ -[CalUISuggestionsFieldAccessibility _axcSelfAsTextField] : 108 -> 112
~ -[CalUIBoxOccurrenceContentViewAccessibility _axcStyledTitle] : 1516 -> 1528
~ -[CalUIBoxOccurrenceContentViewAccessibility _axcCalendar] : 372 -> 376
~ -[CalUIBoxOccurrenceContentViewAccessibility _axcAllDay] : 348 -> 352
~ -[CalUIBoxOccurrenceContentViewAccessibility _axcNewEvent] : 440 -> 432
~ -[CalUIBoxOccurrenceContentViewAccessibility _axcEventTitle] : 372 -> 376
~ -[CalUIBoxOccurrenceContentViewAccessibility _axcEventLocation] : 372 -> 376
~ +[CalUIEventViewTouchBarAccessibility _CalUIEventViewTouchBarInstance] : 244 -> 248
~ -[CalUIEventViewTouchBarAccessibility _axcInspectorFieldsTouchBarItem] : 168 -> 172
~ -[CalUIDayMiniMonthDayCellAccessibility _axcMonthProxy] : 168 -> 172
~ -[CalUIDayMiniMonthDayCellAccessibility isAccessibilitySelectorAllowed:] : 104 -> 108
~ -[EKUIMapViewAccessibility accessibilityChildrenInNavigationOrder] : 556 -> 560
~ -[AXBCalendarTimeTrackMockElement accessibilityFrame] : 204 -> 208
~ -[EKUILabeledGadgetAccessibility _axcControlView] : 168 -> 172
~ -[EKUILabeledGadgetAccessibility _axcLabel] : 332 -> 336
~ -[EKUILocationTableCellViewAccessibility _axcTitleField] : 168 -> 172
~ -[EKUILocationTableCellViewAccessibility _axcAccessibilityChildrenInNavigationOrder] : 168 -> 172
~ -[EKUIGadgetContainerViewAccessibility isAccessibilityElement] : 440 -> 444
~ -[CalUIDayMiniMonthViewAccessibility _axcAxFrame] : 356 -> 364
~ -[CalUIDayMiniMonthViewAccessibility _axcCalendar] : 168 -> 172
~ -[CalUIDayMiniMonthViewAccessibility _accessibilityMoveFocusToDay:] : 2256 -> 2240
~ -[CalUIDayMiniMonthViewAccessibility mouseDown:] : 532 -> 536
~ -[CalUIDayViewGadgetAccessibility accessibilityLabel] : 388 -> 392
~ -[CalUIDayViewGadgetAccessibility accessibilityChildren] : 424 -> 428
~ -[CalUIDayViewGadgetAccessibility _axcAllDayChildren] : 596 -> 604

```
