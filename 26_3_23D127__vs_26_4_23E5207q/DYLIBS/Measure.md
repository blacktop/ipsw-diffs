## Measure

> `/System/Library/AccessibilityBundles/Measure.axbundle/Measure`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x5e14
-  __TEXT.__auth_stubs: 0x410
+3005.16.0.0.0
+  __TEXT.__text: 0x61a0
+  __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_methlist: 0xcd8
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0xe54

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x598
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x218
+  __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x1560
   __AUTH_CONST.__objc_const: 0x21c0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 16CEFFCE-D55D-332B-9E7B-749CF433F3F9
-  Functions: 253
-  Symbols:   1076
+  UUID: 6514DC81-CB35-300F-A904-0C580709C7AB
+  Functions: 254
+  Symbols:   1077
   CStrings:  625
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x8
Functions:
~ +[AXMeasureGlue accessibilityInitializeBundle] : 148 -> 152
~ ___46+[AXMeasureGlue accessibilityInitializeBundle]_block_invoke : 256 -> 260
~ ___46+[AXMeasureGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___46+[AXMeasureGlue accessibilityInitializeBundle]_block_invoke_3 : 612 -> 620
~ _accessibilityLocalizedString : 176 -> 184
~ _AXMeasureAccessibilityStateObserver : 156 -> 164
~ _AXMeasureLabelView : 168 -> 180
~ _AXMeasureViewController : 232 -> 260
~ _AXMeasureReticleView : 168 -> 180
~ _AXMeasureTabBarController : 264 -> 288
~ _AXMeasureSpeakableDescriptionForLastSavedMeasurement : 76 -> 84
~ _AXMeasureSpeakableDescriptionForCurrentMeasurement : 76 -> 84
~ _AXMeasureIsMeasuring : 92 -> 100
~ _AXMeasureAnnounceUpdatedMeasurement : 196 -> 188
~ ___AXMeasureAnnounceUpdatedMeasurement_block_invoke : 232 -> 252
~ _AXMeasureDidPotentiallyShowCardViewWithAncestorClass : 224 -> 240
~ +[PersonHeightViewAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ -[PersonHeightViewAccessibility toggleViewVisibilityWithIsVisible:] : 180 -> 192
~ +[AccessibilityStateObserverAccessibility _accessibilityPerformValidations:] : 476 -> 488
~ -[AccessibilityStateObserverAccessibility axDescriptionForNumberOfPointsAndLines] : 984 -> 1044
~ -[AccessibilityStateObserverAccessibility _axHasRectangleWithState:] : 300 -> 308
~ -[AccessibilityStateObserverAccessibility _axUpdateForState] : 884 -> 956
+ _OUTLINED_FUNCTION_0
~ +[CalloutViewAccessibility _accessibilityPerformValidations:] : 200 -> 208
~ -[CalloutViewAccessibility axCalloutText] : 180 -> 192
~ -[CalloutViewAccessibility axDidUpdateFromPreviousCalloutText:] : 136 -> 140
~ -[CalloutViewAccessibility _axSetIsActuallyVisible:] : 176 -> 184
~ -[CalloutViewAccessibility _axUpdateIsVisible] : 208 -> 212
~ -[CalloutViewAccessibility setAlpha:] : 188 -> 192
~ -[CalloutViewRegularAccessibility updateText:] : 112 -> 116
~ +[CalloutViewSpatialAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ -[CalloutViewSpatialAccessibility accessibilityFrame] : 396 -> 412
~ -[CalloutViewSpatialAccessibility updateText:] : 112 -> 116
~ -[CardTitleViewAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 116
~ +[DeleteButtonAccessibility _accessibilityPerformValidations:] : 236 -> 244
~ -[DeleteButtonAccessibility _axAnnotateActualButton] : 116 -> 124
~ -[DeleteButtonAccessibility tapDeleteFrom:] : 92 -> 96
~ +[EditButtonAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[EditButtonAccessibility accessibilityValue] : 148 -> 160
~ +[EditViewAccessibility _accessibilityPerformValidations:] : 172 -> 180
~ -[EditViewAccessibility setAlpha:] : 200 -> 204
~ -[EditViewAccessibility didTapEditButton] : 136 -> 144
~ +[HistoryButtonAccessibility _accessibilityPerformValidations:] : 112 -> 120
~ +[LabelDetailsPlatterAccessibility _accessibilityPerformValidations:] : 224 -> 232
~ -[LabelDetailsPlatterAccessibility _axAnnotateCloseButton] : 140 -> 148
~ ___58-[LabelDetailsPlatterAccessibility _axAnnotateCloseButton]_block_invoke : 332 -> 336
~ -[LabelDetailsPlatterAccessibility accessibilityViewIsModal] : 120 -> 124
~ -[LabelDetailsPlatterAccessibility setAlpha:] : 228 -> 232
~ +[LabelRenderAccessibility _accessibilityPerformValidations:] : 104 -> 112
~ -[AXMeasureLabelAccessibilityElement isAccessibilityElement] : 192 -> 204
~ -[AXMeasureLabelAccessibilityElement accessibilityLabel] : 168 -> 176
~ -[AXMeasureLabelAccessibilityElement accessibilityValue] : 84 -> 92
~ -[AXMeasureLabelAccessibilityElement accessibilityFrameInContainerSpace] : 104 -> 108
~ -[AXMeasureLabelAccessibilityElement accessibilityTraits] : 112 -> 116
~ +[LabelViewAccessibility _accessibilityPerformValidations:] : 256 -> 268
~ -[LabelViewAccessibility _axLabelElementForMeasureID:accessibilityContainer:] : 316 -> 328
~ -[LabelViewAccessibility _accessibilityLastSavedMeasurementString] : 432 -> 440
~ ___66-[LabelViewAccessibility _accessibilityLastSavedMeasurementString]_block_invoke : 156 -> 164
~ -[LabelViewAccessibility _accessibilityCurrentMeasurementString] : 292 -> 320
~ -[LabelViewAccessibility _accessibilityLabelElementsWithAccessibilityContainer:] : 596 -> 636
~ +[LevelPageViewControllerAccessibility _accessibilityPerformValidations:] : 296 -> 304
~ -[LevelPageViewControllerAccessibility _axShouldAnnounce] : 136 -> 144
~ -[LevelPageViewControllerAccessibility _axAnnounceDegreesIfNeeded:] : 224 -> 232
~ -[LevelPageViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 256 -> 268
~ -[LevelPageViewControllerAccessibility _updateForRotation:shiftAngle:] : 232 -> 236
~ +[ModeControlAccessibility _accessibilityPerformValidations:] : 160 -> 172
~ -[ModeControlAccessibility _axAnnotateSelectedButton] : 156 -> 160
~ ___53-[ModeControlAccessibility _axAnnotateSelectedButton]_block_invoke : 140 -> 144
~ -[ModeControlAccessibility _accessibilityLoadAccessibilityInformation] : 300 -> 304
~ +[RectangleFillAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[RectangleFillAccessibility setState:] : 188 -> 192
~ +[RectangleLabelDetailsPlatterAccessibility _accessibilityPerformValidations:] : 224 -> 232
~ -[RectangleLabelDetailsPlatterAccessibility _axAnnotateCloseButton] : 140 -> 148
~ ___67-[RectangleLabelDetailsPlatterAccessibility _axAnnotateCloseButton]_block_invoke : 332 -> 336
~ -[RectangleLabelDetailsPlatterAccessibility accessibilityViewIsModal] : 120 -> 124
~ -[RectangleLabelDetailsPlatterAccessibility setAlpha:] : 228 -> 232
~ +[ReticleViewAccessibility _accessibilityPerformValidations:] : 240 -> 248
~ -[ReticleViewAccessibility axFirstLabelElement] : 108 -> 120
~ -[ReticleViewAccessibility axIsFocusedOnRectangle] : 56 -> 60
~ -[ReticleViewAccessibility accessibilityElements] : 732 -> 748
~ ___49-[ReticleViewAccessibility accessibilityElements]_block_invoke_2 : 76 -> 80
~ ___49-[ReticleViewAccessibility accessibilityElements]_block_invoke_4 : 76 -> 80
~ -[ReticleViewAccessibility _axFrameForReticleElement] : 228 -> 232
~ -[ReticleViewAccessibility _axHintForReticleElement] : 136 -> 144
~ -[ReticleViewAccessibility _axStringForReticleState] : 172 -> 176
~ -[ReticleViewAccessibility _axAnnounceReticleState] : 136 -> 144
~ -[ReticleViewAccessibility setState:] : 196 -> 200
~ -[ReticleViewAccessibility setAlpha:] : 180 -> 184
~ -[SpatialGenericPlatterAccessibility accessibilityPerformEscape] : 168 -> 172
~ +[MeasureUIApplicationAccessibility _accessibilityPerformValidations:] : 120 -> 132
~ -[MeasureUIApplicationAccessibility _accessibilityOrientationForCompareGeometry] : 64 -> 68
~ ___65-[MeasureUIApplicationAccessibility accessibilityPerformMagicTap]_block_invoke : 96 -> 104
~ -[MeasureUIButtonAccessibility _axIsDeleteButton] : 68 -> 72
~ -[MeasureUIButtonAccessibility accessibilityLabel] : 116 -> 124
~ +[UndoButtonAccessibility _accessibilityPerformValidations:] : 136 -> 144
~ -[UndoButtonAccessibility accessibilityTraits] : 96 -> 100
~ -[UndoButtonAccessibility undoFrom:] : 180 -> 192
~ -[AccessibilityStateObserverAccessibility _axUpdateForState].cold.1 : 68 -> 56
~ -[AccessibilityStateObserverAccessibility _axUpdateForState].cold.2 : 68 -> 56

```
