## Clock

> `/System/iOSSupport/System/Library/AccessibilityBundles/Clock.axbundle/Contents/MacOS/Clock`

```diff

-2963.3.13.1.0
-  __TEXT.__text: 0xa2d4
+2963.10.10.0.0
+  __TEXT.__text: 0xa3b0
   __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x1090
-  __TEXT.__cstring: 0x17e7
+  __TEXT.__objc_methlist: 0x10a0
+  __TEXT.__cstring: 0x17f7
   __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0x228
-  __TEXT.__unwind_info: 0x488
+  __TEXT.__gcc_except_tab: 0x224
+  __TEXT.__unwind_info: 0x480
   __TEXT.__objc_classname: 0xb81
   __TEXT.__objc_methname: 0x16fd
   __TEXT.__objc_methtype: 0x18d
   __TEXT.__objc_stubs: 0x1940
   __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x308
+  __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0xe0
   __AUTH_CONST.__auth_got: 0x280
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x26a0
+  __AUTH_CONST.__cfstring: 0x26c0
   __AUTH_CONST.__objc_const: 0x2a90
   __AUTH.__objc_data: 0x1720
   __DATA.__objc_ivar: 0xc

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 10328FA5-2C38-30C1-9A58-90DEE3767536
-  Functions: 334
-  Symbols:   1119
-  CStrings:  1015
+  UUID: 739852DA-21AF-348D-97D2-03552498D107
+  Functions: 335
+  Symbols:   1121
+  CStrings:  1017
 
Symbols:
+ -[MTAStopwatchViewControllerAccessibility startLapTimer]
+ -[MobileTimerUIButtonAccessibility _isAlarmTableViewCellDescendantDisclosureButton].cold.1
Functions:
- sub_262c47cd4
~ +[AXMobileTimerGlue playStopSound] : 184 -> 200
~ +[AXMobileTimerGlue playStartSound] : 184 -> 200
~ -[UIApplication(MobileTimerUIApplicationAccessibility) accessibilityPerformMagicTap] : 1040 -> 1016
~ -[MTAAlarmCollectionViewCellAccessibility _axToggleSwitch] : 248 -> 244
~ ___58-[MTAAlarmCollectionViewCellAccessibility _axToggleSwitch]_block_invoke : 200 -> 204
~ -[MTAAlarmTableViewCellAccessibility _axSetDetailLabelForAlarm:] : 296 -> 292
~ -[MTAAlarmTableViewCellAccessibility accessibilityCustomActions] : 316 -> 312
~ -[MTAAlarmTableViewCellAccessibility _axEnabledSwitch] : 156 -> 160
~ -[MTAAlarmTableViewControllerAccessibility _axSetDetailLabelsForVisibleCells] : 1064 -> 1048
~ -[MTAAlarmTableViewControllerAccessibility _axSetHeaderLabelForSleepSection:] : 252 -> 256
~ -[MTAAlarmTableViewControllerAccessibility tableView:viewForHeaderInSection:] : 376 -> 384
~ -[MTAEditAlarmVolumeCellAccessibility accessibilityIncrement] : 172 -> 176
~ -[MTAEditAlarmVolumeCellAccessibility accessibilityDecrement] : 172 -> 176
~ -[MTAStopwatchLapCellAccessibility accessibilityValue] : 316 -> 320
~ -[MTAAppControllerAccessibility _axRemoveFlexibleSpaceItems] : 400 -> 404
~ -[MTAAppControllerAccessibility _axUpdateAddButtonItem] : 388 -> 396
~ +[MTAStopwatchViewControllerAccessibility _accessibilityPerformValidations:] : 236 -> 268
+ -[MTAStopwatchViewControllerAccessibility startLapTimer]
~ -[MTAAlarmCollectionViewControllerAccessibility _axDataSource] : 156 -> 160
~ -[MTATimerButtonsControllerAccessibility _updateCancelButtonState] : 208 -> 212
~ -[MTATimerControlsViewAccessibility _axModifyTableView] : 152 -> 156
~ -[MTATimerIntervalPickerViewAccessibility _axModifyTimePicker] : 700 -> 712
~ ___62-[MTATimerIntervalPickerViewAccessibility _axModifyTimePicker]_block_invoke : 468 -> 476
~ -[MTAWorldClockCollectionViewControllerAccessibility nameForWorldClockCell:] : 264 -> 268
~ -[MTAWorldClockCollectionViewControllerAccessibility collectionView:moveItemAtIndexPath:toIndexPath:] : 788 -> 804
~ -[MTAWorldClockCollectionViewControllerAccessibility movedItemAtIndexPath:toIndexPath:] : 352 -> 356
~ -[MTAWorldClockCollectionViewControllerAccessibility _axModifyReorderingGesture] : 164 -> 168
~ -[MTAWorldClockViewAccessibility isAccessibilityElement] : 88 -> 92
~ -[AXMTACountDownPickerElement accessibilityFrame] : 288 -> 260
~ -[MTACountDownPickerAccessibility accessibilityCustomActions] : 568 -> 560
~ -[MTATimerRecentViewAccessibility accessibilityLabel] : 264 -> 268
~ -[MT_UICollectionViewAccessibility moveItemAtIndexPath:toIndexPath:] : 268 -> 272
~ -[MT_UICollectionViewAccessibility accessibilityElementsHidden] : 256 -> 260
~ -[MT_UIPageControlAccessibility _axPagingController] : 232 -> 240
~ -[MT_UIPageControlAccessibility _axStopWatchAdjustPage:] : 316 -> 320
~ -[MobileTimerUIButtonAccessibility _isAlarmTableViewCellDescendantDisclosureButton] : 152 -> 136
CStrings:
+ "startStopButton"

```
