## com.apple.iCal

> `/System/Library/Accessibility/BundlesBase/com.apple.iCal.axbundle/Versions/A/com.apple.iCal`

```diff

-287.6.0.0.0
-  __TEXT.__text: 0xdb8c
+287.6.4.0.0
+  __TEXT.__text: 0xdc4c
   __TEXT.__auth_stubs: 0x340
   __TEXT.__objc_stubs: 0x1a60
   __TEXT.__objc_methlist: 0xa9c
   __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0x460
+  __TEXT.__gcc_except_tab: 0x424
   __TEXT.__cstring: 0x1795
   __TEXT.__objc_classname: 0x678
   __TEXT.__objc_methname: 0x17dd

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F601B435-E399-39EF-AE17-1B07052F6D0C
+  UUID: 750F1553-E5B6-3854-A869-5F045A316DAD
   Functions: 260
   Symbols:   858
   CStrings:  889
Functions:
~ +[AXCalAvailabilityScanner elementWithController:] : 236 -> 240
~ -[AXCalAvailabilityScanner accessibilityPerformPress] : 456 -> 460
~ -[AXCalAvailabilityScanner accessibilityCustomActions] : 1008 -> 1004
~ ___54-[AXCalAvailabilityScanner accessibilityCustomActions]_block_invoke : 304 -> 296
~ -[AXCalAvailabilityScanner accessibilityLinkedUIElements] : 260 -> 264
~ -[AXCalAvailabilityScanner _contentView] : 172 -> 176
~ -[AXCalAvailabilityScanner _currentEventView] : 172 -> 176
~ -[AXCalAvailabilityScanner _validCurrentEventView] : 468 -> 476
~ -[AXCalAvailabilityScanner _participantAtRow:] : 236 -> 244
~ -[AXCalAvailabilityScanner _participantAvailabilitySpansAtRow:] : 284 -> 288
~ ___63-[AXCalAvailabilityScanner _participantAvailabilitySpansAtRow:]_block_invoke : 152 -> 156
~ -[AXCalAvailabilityScanner _contentInterval] : 292 -> 296
~ -[AXCalAvailabilityScanner _eventInterval] : 304 -> 308
~ -[AXCalAvailabilityScanner _defaultStartDate] : 244 -> 248
~ -[AXCalAvailabilityScanner _customActions] : 1424 -> 1400
~ ___42-[AXCalAvailabilityScanner _customActions]_block_invoke : 176 -> 172
~ __42-[AXCalAvailabilityScanner _customActions]_block_invoke.394 : 180 -> 176
~ ___42-[AXCalAvailabilityScanner _customActions]_block_invoke_2 : 332 -> 340
~ -[AXCalAvailabilityScanner _resetScannerPosition] : 128 -> 124
~ -[AXCalAvailabilityScanner _isEnabled] : 196 -> 200
~ -[CalUIMonthDayViewAccessibility accessibilitySetValue:forAttribute:] : 856 -> 868
~ ___69-[CalUIMonthDayViewAccessibility accessibilitySetValue:forAttribute:]_block_invoke : 156 -> 160
~ -[CalUIMonthDayViewAccessibility accessibilityAttributeValue:] : 2636 -> 2604
~ ___62-[CalUIMonthDayViewAccessibility accessibilityAttributeValue:]_block_invoke : 236 -> 240
~ -[CalUIMonthDayViewAccessibility accessibilityPerformShowMenu] : 628 -> 640
~ -[CalUICanvasFrameViewAccessibility accessibilityLabel] : 440 -> 448
~ -[CalUIViewControllerAccessibility handleOccurrenceModificationForMouseEvent:] : 968 -> 972
~ ___78-[CalUIViewControllerAccessibility handleOccurrenceModificationForMouseEvent:]_block_invoke : 164 -> 168
~ -[CalUIViewControllerAccessibility _accessibilityTodayOccurenceElement] : 1764 -> 1756
~ -[CalAvailabilityWindowControllerAccessibility setSearchingForNextAvailableTime:] : 672 -> 676
~ -[CalAvailabilityWindowControllerAccessibility _axcInitAccessibility] : 876 -> 896
~ +[CalUICalendarSidebarAccessibility accessibilitySetupExistingObjects] : 512 -> 520
~ -[CalUICalendarSidebarAccessibility _axbUpdateScrollAreaLabel] : 264 -> 268
~ -[CalParticipantContainerAccessibility accessibilityLabel] : 372 -> 380
~ ___66-[CalParticipantContainerAccessibility accessibilityCustomContent]_block_invoke : 332 -> 336
~ -[CalParticipantContainerAccessibility _axParticipantRowView] : 552 -> 560
~ ___61-[CalParticipantContainerAccessibility _axParticipantRowView]_block_invoke : 196 -> 200
~ -[CalUICalendarViewsControllerAccessibility _accessibilityPostLayoutChanged] : 1212 -> 1200
~ +[CalUICalendarViewsControllerAccessibility accessibilitySetupExistingObjects] : 548 -> 556
~ -[CalAvailabilityContentViewAccessibility accessibilityValueDescription] : 828 -> 840
~ -[CalAvailabilityContentViewAccessibility accessibilityLabel] : 292 -> 296
~ -[CalAvailabilityContentViewAccessibility accessibilityChildren] : 396 -> 400
~ -[CalAvailabilityContentViewAccessibility accessibilityFrame] : 192 -> 196
~ -[CalAvailabilityContentViewAccessibility findNextFreeSpan] : 1012 -> 1024
~ -[CalAvailabilityContentViewAccessibility _axClearScannerWithNotification:] : 208 -> 212
~ -[CalUICalendarListViewAccessibility accessibilityPerformShowMenu] : 500 -> 504
~ -[CalUICalendarListViewAccessibility _axcSelfAsTableView] : 108 -> 112
~ -[CalUICalendarContainerViewAccessibility accessibilityChildren] : 592 -> 600
~ ___64-[CalUICalendarContainerViewAccessibility accessibilityChildren]_block_invoke : 320 -> 328
~ -[CalUIDotOccurrenceAccessibility accessibilityParent] : 168 -> 172
~ -[CalUIDotOccurrenceAccessibility accessibilityCustomContent] : 1700 -> 1716
~ _AXCalActiveDescription : 516 -> 512
~ -[CalUISearchFieldAccessibility accessibilityLinkedUIElements] : 356 -> 364
~ -[CalUIDayLayerViewAccessibility accessibilityLabel] : 312 -> 316
~ -[CalUIDayLayerViewAccessibility accessibilitySelectedChildren] : 1420 -> 1396
~ -[CalUIDayLayerViewAccessibility setAccessibilitySelectedChildren:] : 768 -> 780
~ -[CalUIDayLayerViewAccessibility accessibilityPerformShowMenu] : 996 -> 1008
~ -[CALMainControllerAccessibility showUIOccurrence:event:openInspector:inspectorType:restoreDraft:] : 384 -> 388
~ -[CalUICalendarListBaseCellViewAccessibility _axcUpdateAlertButtonAccessibility] : 404 -> 408
~ -[CalUIToolbarAccessibility _accessibilityUpdateToolbarSegments] : 452 -> 456
~ -[CalUIInspectorManagerAccessibility openPopoverInspectorForEvent:relativeToView:onMainController:isProposed:] : 368 -> 372

```
