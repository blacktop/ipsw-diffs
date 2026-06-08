## Measure

> `/System/Library/AccessibilityBundles/Measure.axbundle/Measure`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x61dc
-  __TEXT.__auth_stubs: 0x400
+3036.2.0.0.0
+  __TEXT.__text: 0x6244
   __TEXT.__objc_methlist: 0xcd8
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0xe81
-  __TEXT.__oslogstring: 0x96
+  __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__unwind_info: 0x2b8
-  __TEXT.__objc_classname: 0x7a1
-  __TEXT.__objc_methname: 0x1186
-  __TEXT.__objc_methtype: 0xe3
-  __TEXT.__objc_stubs: 0x1180
-  __DATA_CONST.__got: 0x140
+  __TEXT.__cstring: 0xe83
+  __TEXT.__oslogstring: 0x96
+  __TEXT.__unwind_info: 0x2b0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x590
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x15a0
   __AUTH_CONST.__objc_const: 0x21c0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1220
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24DFB7BC-B1DE-321B-A3BA-4604439BBA05
-  Functions: 254
-  Symbols:   1076
-  CStrings:  630
+  UUID: C1A13F86-391E-3101-81A5-F676970DDC82
+  Functions: 251
+  Symbols:   1073
+  CStrings:  365
 
Symbols:
+ GCC_except_table137
+ GCC_except_table197
+ ___block_literal_global.380
+ ___block_literal_global.387
+ ___block_literal_global.389
+ ___block_literal_global.682
+ ___block_literal_global.762
+ ___block_literal_global.900
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x8
- -[AccessibilityStateObserverAccessibility _axUpdateForState].cold.1
- -[AccessibilityStateObserverAccessibility _axUpdateForState].cold.2
- GCC_except_table16
- GCC_except_table7
- _OUTLINED_FUNCTION_0
- ___block_literal_global.359
- ___block_literal_global.368
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[AXMeasureGlue accessibilityInitializeBundle] : 152 -> 148
~ ___46+[AXMeasureGlue accessibilityInitializeBundle]_block_invoke : 260 -> 256
~ ___46+[AXMeasureGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___46+[AXMeasureGlue accessibilityInitializeBundle]_block_invoke_3 : 620 -> 612
~ _accessibilityLocalizedString : 184 -> 176
~ _AXMeasureAccessibilityStateObserver : 164 -> 156
~ _AXMeasureLabelView : 180 -> 168
~ _AXMeasureViewController : 260 -> 232
~ _AXMeasureReticleView : 180 -> 168
~ _AXMeasureTabBarController : 288 -> 264
~ _AXMeasureSpeakableDescriptionForLastSavedMeasurement : 84 -> 76
~ _AXMeasureSpeakableDescriptionForCurrentMeasurement : 84 -> 76
~ _AXMeasureIsMeasuring : 100 -> 92
~ ___AXMeasureSpeakMeasurementAnnouncement_block_invoke : 84 -> 144
~ _AXMeasureAnnounceUpdatedMeasurement : 188 -> 196
~ ___AXMeasureAnnounceUpdatedMeasurement_block_invoke : 252 -> 272
~ _AXMeasureDidPotentiallyShowCardViewWithAncestorClass : 240 -> 224
~ +[PersonHeightViewAccessibility _accessibilityPerformValidations:] : 148 -> 140
~ -[PersonHeightViewAccessibility toggleViewVisibilityWithIsVisible:] : 192 -> 276
~ +[AccessibilityStateObserverAccessibility _accessibilityPerformValidations:] : 488 -> 476
~ -[AccessibilityStateObserverAccessibility axDescriptionForNumberOfPointsAndLines] : 1044 -> 1020
~ -[AccessibilityStateObserverAccessibility _axHasRectangleWithState:] : 308 -> 304
~ -[AccessibilityStateObserverAccessibility _axUpdateForState] : 956 -> 1032
- _OUTLINED_FUNCTION_0
~ +[CalloutViewAccessibility _accessibilityPerformValidations:] : 208 -> 200
~ -[CalloutViewAccessibility axCalloutText] : 192 -> 180
~ -[CalloutViewAccessibility axDidUpdateFromPreviousCalloutText:] : 140 -> 232
~ -[CalloutViewAccessibility _axSetIsActuallyVisible:] : 184 -> 284
~ -[CalloutViewAccessibility _axUpdateIsVisible] : 212 -> 208
~ -[CalloutViewAccessibility setAlpha:] : 192 -> 188
~ -[CalloutViewRegularAccessibility updateText:] : 116 -> 112
~ +[CalloutViewSpatialAccessibility _accessibilityPerformValidations:] : 148 -> 140
~ -[CalloutViewSpatialAccessibility accessibilityFrame] : 412 -> 396
~ -[CalloutViewSpatialAccessibility updateText:] : 116 -> 112
~ -[CardTitleViewAccessibility _accessibilityLoadAccessibilityInformation] : 116 -> 112
~ +[DeleteButtonAccessibility _accessibilityPerformValidations:] : 244 -> 236
~ -[DeleteButtonAccessibility _axAnnotateActualButton] : 124 -> 112
~ -[DeleteButtonAccessibility initWithFrame:] : 84 -> 80
~ -[DeleteButtonAccessibility tapDeleteFrom:] : 96 -> 188
~ +[EditButtonAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[EditButtonAccessibility accessibilityValue] : 160 -> 164
~ +[EditViewAccessibility _accessibilityPerformValidations:] : 180 -> 172
~ -[EditViewAccessibility setAlpha:] : 204 -> 200
~ -[EditViewAccessibility didTapEditButton] : 144 -> 136
~ +[HistoryButtonAccessibility _accessibilityPerformValidations:] : 120 -> 112
~ +[LabelDetailsPlatterAccessibility _accessibilityPerformValidations:] : 232 -> 224
~ -[LabelDetailsPlatterAccessibility _axAnnotateCloseButton] : 148 -> 140
~ -[LabelDetailsPlatterAccessibility accessibilityViewIsModal] : 124 -> 120
~ -[LabelDetailsPlatterAccessibility setAlpha:] : 232 -> 228
~ +[LabelRenderAccessibility _accessibilityPerformValidations:] : 112 -> 104
~ -[AXMeasureLabelAccessibilityElement isAccessibilityElement] : 204 -> 192
~ -[AXMeasureLabelAccessibilityElement accessibilityLabel] : 176 -> 168
~ -[AXMeasureLabelAccessibilityElement accessibilityValue] : 92 -> 84
~ -[AXMeasureLabelAccessibilityElement accessibilityFrameInContainerSpace] : 108 -> 104
~ -[AXMeasureLabelAccessibilityElement accessibilityTraits] : 116 -> 112
~ -[AXMeasureLabelAccessibilityElement isRectangleArea] : 16 -> 20
~ -[AXMeasureLabelAccessibilityElement setIsRectangleArea:] : 16 -> 20
~ -[AXMeasureLabelAccessibilityElement isRectangleSideLength] : 16 -> 20
~ -[AXMeasureLabelAccessibilityElement setIsRectangleSideLength:] : 16 -> 20
~ +[LabelViewAccessibility _accessibilityPerformValidations:] : 268 -> 256
~ -[LabelViewAccessibility _axLabelElementForMeasureID:accessibilityContainer:] : 328 -> 316
~ -[LabelViewAccessibility _accessibilityLastSavedMeasurementString] : 440 -> 432
~ ___66-[LabelViewAccessibility _accessibilityLastSavedMeasurementString]_block_invoke : 164 -> 156
~ -[LabelViewAccessibility _accessibilityCurrentMeasurementString] : 320 -> 292
~ -[LabelViewAccessibility _accessibilityLabelElementsWithAccessibilityContainer:] : 636 -> 612
~ +[LevelPageViewControllerAccessibility _accessibilityPerformValidations:] : 336 -> 328
~ -[LevelPageViewControllerAccessibility _axShouldAnnounce] : 144 -> 136
~ -[LevelPageViewControllerAccessibility _axAnnounceDegreesIfNeeded:] : 260 -> 248
~ -[LevelPageViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 268 -> 256
~ -[LevelPageViewControllerAccessibility _updateForRotation:shiftAngle:] : 236 -> 232
~ +[ModeControlAccessibility _accessibilityPerformValidations:] : 172 -> 160
~ -[ModeControlAccessibility _axAnnotateSelectedButton] : 160 -> 156
~ ___53-[ModeControlAccessibility _axAnnotateSelectedButton]_block_invoke : 144 -> 140
~ -[ModeControlAccessibility _accessibilityLoadAccessibilityInformation] : 304 -> 316
~ +[RectangleFillAccessibility _accessibilityPerformValidations:] : 144 -> 136
~ -[RectangleFillAccessibility setState:] : 192 -> 284
~ +[RectangleLabelDetailsPlatterAccessibility _accessibilityPerformValidations:] : 232 -> 224
~ -[RectangleLabelDetailsPlatterAccessibility _axAnnotateCloseButton] : 148 -> 140
~ -[RectangleLabelDetailsPlatterAccessibility accessibilityViewIsModal] : 124 -> 120
~ -[RectangleLabelDetailsPlatterAccessibility setAlpha:] : 232 -> 228
~ +[ReticleViewAccessibility _accessibilityPerformValidations:] : 248 -> 240
~ -[ReticleViewAccessibility axFirstLabelElement] : 120 -> 108
~ -[ReticleViewAccessibility axIsFocusedOnRectangle] : 60 -> 56
~ -[ReticleViewAccessibility accessibilityElements] : 748 -> 732
~ ___49-[ReticleViewAccessibility accessibilityElements]_block_invoke_2 : 80 -> 76
~ ___49-[ReticleViewAccessibility accessibilityElements]_block_invoke_3 : 4 -> 76
~ ___49-[ReticleViewAccessibility accessibilityElements]_block_invoke_4 : 80 -> 76
~ -[ReticleViewAccessibility _axFrameForReticleElement] : 232 -> 228
~ -[ReticleViewAccessibility _axHintForReticleElement] : 144 -> 136
~ -[ReticleViewAccessibility _axStringForReticleState] : 176 -> 164
~ -[ReticleViewAccessibility _axAnnounceReticleState] : 144 -> 240
~ -[ReticleViewAccessibility _axAnnounceReticleStateAfterDelay] : 100 -> 104
~ -[ReticleViewAccessibility setState:] : 200 -> 196
~ -[ReticleViewAccessibility setAlpha:] : 184 -> 180
~ -[SpatialGenericPlatterAccessibility accessibilityPerformEscape] : 172 -> 256
~ +[MeasureUIApplicationAccessibility _accessibilityPerformValidations:] : 132 -> 120
~ -[MeasureUIApplicationAccessibility _accessibilityOrientationForCompareGeometry] : 68 -> 64
~ -[MeasureUIApplicationAccessibility accessibilityPerformMagicTap] : 56 -> 108
~ ___65-[MeasureUIApplicationAccessibility accessibilityPerformMagicTap]_block_invoke : 104 -> 96
~ -[MeasureUIButtonAccessibility _axIsDeleteButton] : 72 -> 64
~ -[MeasureUIButtonAccessibility accessibilityLabel] : 124 -> 116
~ +[UndoButtonAccessibility _accessibilityPerformValidations:] : 144 -> 136
~ -[UndoButtonAccessibility accessibilityTraits] : 100 -> 96
~ -[UndoButtonAccessibility undoFrom:] : 192 -> 180
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "AXMeasureGlue"
- "AXMeasureLabelAccessibilityElement"
- "B16@0:8"
- "B24@0:8q16"
- "B32@0:8d16d24"
- "Q16@0:8"
- "SafeCategory"
- "T@\"NSString\",R,N"
- "T@,R,N"
- "T@,W,N,V_labelRender"
- "TB,N,SaxSetIsActuallySelected:"
- "TB,N,V_isRectangleArea"
- "TB,N,V_isRectangleSideLength"
- "TB,R,N"
- "__AccessibilityStateObserverAccessibility_super"
- "__CalloutViewAccessibility_super"
- "__CalloutViewRegularAccessibility_super"
- "__CalloutViewSpatialAccessibility_super"
- "__CardContainerViewAccessibility_super"
- "__CardTitleViewAccessibility_super"
- "__DeleteButtonAccessibility_super"
- "__EditButtonAccessibility_super"
- "__EditViewAccessibility_super"
- "__HistoryButtonAccessibility_super"
- "__HistoryViewAccessibility_super"
- "__LabelDetailsPlatterAccessibility_super"
- "__LabelRenderAccessibility_super"
- "__LabelViewAccessibility_super"
- "__LevelPageViewControllerAccessibility_super"
- "__MeasureUIApplicationAccessibility_super"
- "__MeasureUIButtonAccessibility_super"
- "__ModeControlAccessibility_super"
- "__NonRotatingARSCNViewAccessibility_super"
- "__PersonHeightViewAccessibility_super"
- "__RectangleFillAccessibility_super"
- "__RectangleLabelDetailsPlatterAccessibility_super"
- "__ReticleViewAccessibility_super"
- "__RoundCloseButtonAccessibility_super"
- "__SketchSurfaceAccessibility_super"
- "__SpatialGenericPlatterAccessibility_super"
- "__SurfaceSideMeasurementStackAccessibility_super"
- "__UndoButtonAccessibility_super"
- "_accessibilityCurrentMeasurementString"
- "_accessibilityDescendantOfType:"
- "_accessibilityDidMoveToTabBar"
- "_accessibilityFindDescendant:"
- "_accessibilityLabelElementsWithAccessibilityContainer:"
- "_accessibilityLastSavedMeasurementString"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityOrientationForCompareGeometry"
- "_accessibilityPerformValidations:"
- "_accessibilitySetApplicationOrientation:"
- "_accessibilitySetRetainedValue:forKey:"
- "_accessibilityUseAccessibilityFrameForHittest"
- "_accessibilityValueForKey:"
- "_accessibilityViewIsVisible"
- "_appearState"
- "_applicationKeyWindow"
- "_axAnnotateActualButton"
- "_axAnnotateCloseButton"
- "_axAnnotateSelectedButton"
- "_axAnnounceDegreesIfNeeded:"
- "_axAnnounceReticleState"
- "_axAnnounceReticleStateAfterDelay"
- "_axButtons"
- "_axDidInitializeZeroAlpha"
- "_axFrameForReticleElement"
- "_axHasRectangleWithState:"
- "_axHintForReticleElement"
- "_axInternalIsActuallyVisible"
- "_axIsActuallyVisible"
- "_axIsDeleteButton"
- "_axLabelElementForMeasureID:accessibilityContainer:"
- "_axLastAnnouncementForReticleState"
- "_axLastSnapDivisionsDescription"
- "_axLastSnapDivisionsLineID"
- "_axLastWorldPointType"
- "_axNeedsAnnouncementForContinueMeasurement"
- "_axReticleElement"
- "_axReticleState"
- "_axSetDidInitializeZeroAlpha:"
- "_axSetInternalIsActuallyVisible:"
- "_axSetIsActuallyVisible:"
- "_axSetIsNotActuallyVisible"
- "_axSetLastAnnouncementForReticleState:"
- "_axSetLastSnapDivisionsDescription:"
- "_axSetLastSnapDivisionsLineID:"
- "_axSetLastWorldPointType:"
- "_axSetNeedsAnnouncementForContinueMeasurement:"
- "_axSetReticleElement:"
- "_axShouldAnnounce"
- "_axStringForReticleState"
- "_axTraitsForReticleElement"
- "_axUpdateForState"
- "_axUpdateIsVisible"
- "_isRectangleArea"
- "_isRectangleSideLength"
- "_labelRender"
- "_setAccessibilityFrameBlock:"
- "_setAccessibilityHintBlock:"
- "_setAccessibilityLabelBlock:"
- "_setAccessibilityTraitsBlock:"
- "_setAccessibilityValueBlock:"
- "_updateForRotation:shiftAngle:"
- "accessibilityElements"
- "accessibilityFrame"
- "accessibilityFrameInContainerSpace"
- "accessibilityHint"
- "accessibilityIdentification"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityPerformEscape"
- "accessibilityPerformMagicTap"
- "accessibilitySetIdentification:"
- "accessibilityTraits"
- "accessibilityValue"
- "accessibilityViewIsModal"
- "activeInterfaceOrientation"
- "addObject:"
- "addObjectsFromArray:"
- "allValues"
- "alpha"
- "array"
- "axCalloutText"
- "axDescriptionForNumberOfPointsAndLines"
- "axDidUpdateFromPreviousCalloutText:"
- "axFirstLabelElement"
- "axHasConfirmedRectangle"
- "axHasSuggestedRectangle"
- "axIsActuallySelected"
- "axIsFocusedOnRectangle"
- "axIsModeForMeasuring"
- "axOrderedWorldLineIDs"
- "axSafelyAddObject:"
- "axSetIsActuallySelected:"
- "axWorldLines"
- "axWorldRectangles"
- "bounds"
- "bundleForClass:"
- "cancelPreviousPerformRequestsWithTarget:selector:object:"
- "convertRect:fromLayer:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "enumerateObjectsUsingBlock:"
- "enumerateObjectsWithOptions:usingBlock:"
- "firstObject"
- "gestureRecognizers"
- "indexOfObject:"
- "init"
- "initWithAccessibilityContainer:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isEqual:"
- "isEqualToString:"
- "isRectangleArea"
- "isRectangleSideLength"
- "keyWindow"
- "labelRender"
- "lastObject"
- "layer"
- "length"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "objectForKeyedSubscript:"
- "path"
- "performSelector:withObject:afterDelay:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "q16@0:8"
- "rootViewController"
- "safeArrayForKey:"
- "safeBoolForKey:"
- "safeCGRectForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeDictionaryForKey:"
- "safeFloatForKey:"
- "safeIntegerForKey:"
- "safeStringForKey:"
- "safeSwiftValueForKey:"
- "safeUIViewForKey:"
- "safeUnsignedIntegerForKey:"
- "safeValueForKey:"
- "selectedIndex"
- "setAccessibilityIdentifier:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setDebugBuild:"
- "setIsAccessibilityElement:"
- "setIsRectangleArea:"
- "setIsRectangleSideLength:"
- "setLabelRender:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedApplication"
- "sharedInstance"
- "shouldGroupAccessibilityChildren"
- "text"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v24@0:8q16"
- "validateClass:"
- "validateClass:hasClassMethod:withFullSignature:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasSwiftField:withSwiftType:"
- "validateClass:isKindOfClass:"
- "view"
- "viewDidLoad"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
