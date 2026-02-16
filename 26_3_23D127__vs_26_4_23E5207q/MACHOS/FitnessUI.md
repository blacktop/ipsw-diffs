## FitnessUI

> `/System/Library/AccessibilityBundles/FitnessUI.axbundle/FitnessUI`

```diff

-1001.4.8.0.0
-  __TEXT.__text: 0x3940
-  __TEXT.__auth_stubs: 0x400
+1001.12.0.0.0
+  __TEXT.__text: 0x3b8c
+  __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_stubs: 0xbc0
   __TEXT.__objc_methlist: 0x66c
   __TEXT.__objc_classname: 0x4ed

   __TEXT.__objc_methtype: 0x180
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__unwind_info: 0x230
-  __DATA_CONST.__auth_got: 0x210
+  __TEXT.__unwind_info: 0x220
+  __DATA_CONST.__auth_got: 0x1f0
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__const: 0x308
   __DATA_CONST.__cfstring: 0xa80

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B7107B4-85E1-3754-ABA6-548F5978EAB9
+  UUID: C6E0A8FB-07B6-3A58-9BB3-176A326DCCAA
   Functions: 148
-  Symbols:   557
+  Symbols:   553
   CStrings:  364
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ +[FIUIWorkoutCompletionPercentageRingViewCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[FIUIWorkoutCompletionPercentageRingViewCellAccessibility accessibilityLabel] : 240 -> 268
~ -[FIUIPageViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ -[FIUIChartBarAccessibilityElement initWithAccessibilityContainer:barSeries:index:plotPoint:] : 236 -> 232
~ -[FIUIChartBarAccessibilityElement accessibilityFrame] : 120 -> 124
~ -[FIUIChartBarAccessibilityElement _accessibilityFrameUniform] : 268 -> 276
~ -[FIUIChartBarAccessibilityElement _accessibilityFrameStandardBar] : 296 -> 304
~ -[FIUIChartBarAccessibilityElement accessibilityLabel] : 616 -> 648
~ ___54-[FIUIChartBarAccessibilityElement accessibilityLabel]_block_invoke : 120 -> 128
~ +[FIUIChartBarAccessibilityElement accessibilityElementsForBarSeries:] : 372 -> 380
~ -[FIUIActionButtonAccessibility accessibilityPath] : 244 -> 260
~ -[FitnessUI_UICollectionViewAccessibility accessibilityCollectionViewBehavesLikeUIViewAccessibility] : 120 -> 124
~ +[FIUIChartSeriesAccessibility _accessibilityPerformValidations:] : 116 -> 128
~ -[FIUIChartSeriesAccessibility _accessibilityChartPointForDataSetAtIndex:] : 336 -> 340
~ ___74-[FIUIChartSeriesAccessibility _accessibilityChartPointForDataSetAtIndex:]_block_invoke : 80 -> 84
~ +[FIUIChartViewAccessibility _accessibilityPerformValidations:] : 248 -> 260
~ -[FIUIChartViewAccessibility _axUpdateChartSlices] : 368 -> 384
~ -[FIUIChartViewAccessibility dealloc] : 272 -> 276
~ -[FIUIChartViewAccessibility accessibilityFrame:] : 316 -> 328
~ -[FIUIChartViewAccessibility accessibilityLabel:] : 528 -> 580
~ -[FIUIWorkoutSummaryColoredDetailTableViewCellAccessibility accessibilityLabel] : 344 -> 348
~ ___79-[FIUIWorkoutSummaryColoredDetailTableViewCellAccessibility accessibilityLabel]_block_invoke : 104 -> 108
~ -[FIUIWorkoutSummaryColoredDetailTableViewCellAccessibility accessibilityActivationPoint] : 340 -> 352
~ +[FUDatePickerAccessibility _accessibilityPerformValidations:] : 228 -> 236
~ -[FUDatePickerAccessibility _accessibilityLoadAccessibilityInformation] : 468 -> 516
~ +[FIUIChartUniformBarSeriesAccessibility _accessibilityPerformValidations:] : 188 -> 196
~ -[FIUIChartUniformBarSeriesAccessibility _accessibilityLabelForBarYPoint:withValue:] : 68 -> 72
~ -[FIUIChartUniformBarSeriesAccessibility _axUpdateAccessibilityElements] : 104 -> 108
~ +[FIUIChartBarSeriesAccessibility _accessibilityPerformValidations:] : 272 -> 280
~ -[FIUIChartBarSeriesAccessibility _accessibilityLabelForBarYPoint:withValue:] : 240 -> 256
~ -[FIUIChartBarSeriesAccessibility _axUpdateAccessibilityElements] : 104 -> 108
~ -[FIUIChartBarSeriesAccessibility _accessibilityLocalizedStringForUnit:value:] : 256 -> 288
~ ___48+[AXFitnessUIGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___48+[AXFitnessUIGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___48+[AXFitnessUIGlue accessibilityInitializeBundle]_block_invoke_4 : 332 -> 340
~ _accessibilityDescriptionForPercentages : 760 -> 816
~ _accessibilityLocalizedString : 160 -> 168
~ _accessibilityFormattingManager : 68 -> 84
~ ___accessibilityFormattingManager_block_invoke : 140 -> 144
~ _accessibilityHealthStore : 68 -> 84
~ _accessibilityUnitManager : 68 -> 84
~ ___accessibilityUnitManager_block_invoke : 112 -> 116
~ ____userIsWheelchairUserWithVoiceOverOn_block_invoke : 112 -> 116
~ +[FUScrollWheelAccessibility _accessibilityPerformValidations:] : 268 -> 276
~ ___48-[FUScrollWheelAccessibility accessibilityValue]_block_invoke : 112 -> 116
~ -[FUScrollWheelAccessibility accessibilityIncrement] : 364 -> 368
~ -[FUScrollWheelAccessibility scrollViewDidEndDecelerating:] : 212 -> 216
~ +[FIUIPushyLabelViewAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ -[FIUIPushyLabelViewAccessibility accessibilityLabel] : 176 -> 188
~ -[FIUIPushyLabelViewAccessibility isAccessibilityElement] : 216 -> 228

```
