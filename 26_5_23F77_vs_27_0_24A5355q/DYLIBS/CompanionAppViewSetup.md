## CompanionAppViewSetup

> `/System/Library/AccessibilityBundles/CompanionAppViewSetup.axbundle/CompanionAppViewSetup`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x1d5c
-  __TEXT.__auth_stubs: 0x270
+3036.2.0.0.0
+  __TEXT.__text: 0x1c60
   __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__cstring: 0x5c6
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__cstring: 0x5c6
   __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0x1c6
-  __TEXT.__objc_methname: 0x892
-  __TEXT.__objc_methtype: 0xa6
-  __TEXT.__objc_stubs: 0x780
-  __DATA_CONST.__got: 0x88
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x278
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0x630
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x370
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F77366B4-4122-3454-A9FB-190DF7CF7711
+  UUID: C47FE787-7770-3F0E-A5A9-157004216C0A
   Functions: 59
-  Symbols:   311
-  CStrings:  232
+  Symbols:   314
+  CStrings:  128
 
Symbols:
+ GCC_except_table27
+ GCC_except_table30
+ ___block_literal_global.351
+ ___block_literal_global.360
+ ___block_literal_global.42
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
- GCC_except_table12
- GCC_except_table8
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[AXCarouselAppViewSharedGlue accessibilityInitializeBundle] : 152 -> 148
~ ___60+[AXCarouselAppViewSharedGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ _accessibilityLocalizedString : 184 -> 176
~ -[CSLUILayoutIconViewAccessibility accessibilityPath] : 212 -> 200
~ +[CSLUIFieldOfIconsViewAccessibility _accessibilityPerformValidations:] : 612 -> 600
~ -[CSLUIFieldOfIconsViewAccessibility accessibilityScrollUpPage] : 440 -> 420
~ ___63-[CSLUIFieldOfIconsViewAccessibility accessibilityScrollUpPage]_block_invoke_3 : 96 -> 92
~ -[CSLUIFieldOfIconsViewAccessibility accessibilityScrollDownPage] : 328 -> 316
~ ___65-[CSLUIFieldOfIconsViewAccessibility accessibilityScrollDownPage]_block_invoke_2 : 96 -> 92
~ -[CSLUIFieldOfIconsViewAccessibility _axHexForIconView:] : 92 -> 88
~ -[CSLUIFieldOfIconsViewAccessibility _axUpdateIconElements] : 960 -> 932
~ -[CSLUIFieldOfIconsViewAccessibility accessibilityElements] : 104 -> 96
~ -[CSLUIFieldOfIconsViewAccessibility _accessibilityStartJiggleMode:] : 92 -> 88
~ -[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveElement:left:] : 428 -> 416
~ ___69-[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveElement:left:]_block_invoke : 100 -> 96
~ -[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveIconLeft:] : 108 -> 104
~ -[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveIconRight:] : 132 -> 128
~ -[CSLUIFieldOfIconsViewAccessibility _accessibilityAnnounceUpdatedPositionForElement:] : 468 -> 428
~ -[CSLUIFieldOfIconsViewAccessibility setLayout:percentComplete:animated:options:] : 148 -> 144
~ +[CSLPRFWatchChoiceViewAccessibility _accessibilityPerformValidations:] : 160 -> 152
~ -[CSLPRFWatchChoiceViewAccessibility accessibilityLabel] : 232 -> 216
~ -[CSLPRFWatchChoiceViewAccessibility accessibilityTraits] : 240 -> 232
~ -[CSLUINanoResourceGrabberIconViewAccessibility accessibilityLabel] : 316 -> 288
CStrings:
- "#16@0:8"
- "@16@0:8"
- "AXCarouselAppViewSharedGlue"
- "B16@0:8"
- "B24@0:8@16"
- "B28@0:8@16B24"
- "CSLUIFieldOfIconsViewAccessibility"
- "CSLUILayoutCalendarViewAccessibility"
- "CSLUILayoutIconViewAccessibility"
- "CSLUINanoResourceGrabberIconViewAccessibility"
- "Q16@0:8"
- "SafeCategory"
- "__CSLPRFWatchChoiceViewAccessibility_super"
- "__CSLUIFieldOfIconsViewAccessibility_super"
- "__CSLUILayoutCalendarViewAccessibility_super"
- "__CSLUILayoutIconViewAccessibility_super"
- "__CSLUINanoResourceGrabberIconViewAccessibility_super"
- "_accessibilityAnnounceUpdatedPositionForElement:"
- "_accessibilityCirclePathBasedOnBoundsWidth"
- "_accessibilityFindSubviewDescendant:"
- "_accessibilityFirstElementForFocus"
- "_accessibilityHitTestShouldFallbackToNearestChild"
- "_accessibilityHitTestSubviews"
- "_accessibilityIsRTL"
- "_accessibilityIsScrollAncestor"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityMoveElement:left:"
- "_accessibilityMoveIconLeft:"
- "_accessibilityMoveIconRight:"
- "_accessibilityPerformValidations:"
- "_accessibilityScrollSize"
- "_accessibilityScrollToChild:animated:"
- "_accessibilitySetAssignedValue:forKey:"
- "_accessibilitySetRetainedValue:forKey:"
- "_accessibilityStartJiggleMode:"
- "_accessibilityValueForKey:"
- "_axHexForIconView:"
- "_axUpdateIconElements"
- "_setAccessibilityServesAsFirstElement:"
- "accessibilityElements"
- "accessibilityHint"
- "accessibilityIdentifier"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityPath"
- "accessibilityScrollDownPage"
- "accessibilityScrollToVisibleWithChild:"
- "accessibilityScrollUpPage"
- "accessibilityTraits"
- "addObjectsFromArray:"
- "allValues"
- "array"
- "arrayWithObjects:count:"
- "bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:"
- "bundleForClass:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "hexAppGraph:addedNodes:removedNodes:movedNodes:"
- "indexOfObject:"
- "init"
- "initWithName:target:selector:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isSelected"
- "length"
- "localizedStringForKey:value:table:"
- "moveNode:toHex:final:"
- "mutableCopy"
- "objectAtIndex:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "rectValue"
- "safeBoolForKey:"
- "safeCGPointForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntegerForKey:"
- "safeIvarForKey:"
- "safeValueForKey:"
- "setAccessibilityCustomActions:"
- "setDebugBuild:"
- "setLayout:percentComplete:animated:options:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "sortedArrayUsingComparator:"
- "stringWithFormat:"
- "v16@0:8"
- "v24@0:8@16"
- "v28@0:8@16B24"
- "v44@0:8@16d24B32Q36"
- "v48@0:8@16@24@32@40"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "validateProtocol:hasMethod:isInstanceMethod:isRequired:"
- "{CGSize=dd}16@0:8"
- "{Hex=ii}24@0:8@16"

```
