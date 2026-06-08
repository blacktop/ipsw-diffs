## GameCenterPrivateUIFramework

> `/System/Library/AccessibilityBundles/GameCenterPrivateUIFramework.axbundle/GameCenterPrivateUIFramework`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x1e24
-  __TEXT.__auth_stubs: 0x270
+3036.2.0.0.0
+  __TEXT.__text: 0x1c94
   __TEXT.__objc_methlist: 0x4e8
-  __TEXT.__cstring: 0x6b0
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x18
+  __TEXT.__cstring: 0x6b0
   __TEXT.__unwind_info: 0x158
-  __TEXT.__objc_classname: 0x4ec
-  __TEXT.__objc_methname: 0x508
-  __TEXT.__objc_methtype: 0x73
-  __TEXT.__objc_stubs: 0x420
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_const: 0x1290
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa50
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F92AFB71-9801-318F-87EB-6A46409F1961
-  Functions: 89
-  Symbols:   451
-  CStrings:  248
+  UUID: 50768E2B-5A96-3734-8ABB-81FE0013F6EB
+  Functions: 86
+  Symbols:   446
+  CStrings:  157
 
Symbols:
+ GCC_except_table23
+ ___block_literal_global.26
+ ___block_literal_global.3
+ ___block_literal_global.360
+ ___block_literal_global.364
+ ___block_literal_global.378
+ ___block_literal_global.387
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXGameCenterPrivateUIFrameworkGlue accessibilityInitializeBundle].cold.1
- GCC_except_table4
- _AXGameCenterPrivateUIFrameworkLocString.cold.1
- _AXGameCenterUIFrameworkLocString.cold.1
- ___block_literal_global.339
- ___block_literal_global.343
- ___block_literal_global.357
- ___block_literal_global.366
- _objc_retain_x19
- _objc_retain_x21
Functions:
~ _AXGameCenterUIFrameworkLocString : 140 -> 152
~ ___AXGameCenterUIFrameworkLocString_block_invoke : 144 -> 132
~ _AXGameCenterPrivateUIFrameworkLocString : 140 -> 152
~ ___AXGameCenterPrivateUIFrameworkLocString_block_invoke : 76 -> 72
~ +[AXGameCenterPrivateUIFrameworkGlue accessibilityInitializeBundle] : 44 -> 40
~ ___67+[AXGameCenterPrivateUIFrameworkGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___67+[AXGameCenterPrivateUIFrameworkGlue accessibilityInitializeBundle]_block_invoke_2 : 92 -> 88
~ ___67+[AXGameCenterPrivateUIFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ ___67+[AXGameCenterPrivateUIFrameworkGlue accessibilityInitializeBundle]_block_invoke_4 : 380 -> 372
~ -[GKBasePlayerCellAccessibility accessibilityLabel] : 92 -> 84
~ +[GKCollectionViewCellAccessibility _accessibilityPerformValidations:] : 228 -> 220
~ -[GKCollectionViewCellAccessibility accessibilityCustomActions] : 536 -> 524
~ -[GKCollectionViewCellAccessibility accessibilityPerformCustomAction:] : 660 -> 636
~ ___70-[GKCollectionViewCellAccessibility accessibilityPerformCustomAction:]_block_invoke_2 : 96 -> 92
~ -[GKCollectionViewCellAccessibility _accessibilitySupplementaryFooterViews] : 180 -> 172
~ -[GKBaseGameCellAccessibility accessibilityLabel] : 92 -> 84
~ +[GKPlayerGameCellAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[GKPlayerGameCellAccessibility accessibilityLabel] : 252 -> 228
~ +[GKPurchasableGameCellAccessibility _accessibilityPerformValidations:] : 228 -> 216
~ -[GKPurchasableGameCellAccessibility accessibilityLabel] : 400 -> 360
~ -[GKShowMoreViewAccessibility accessibilityLabel] : 92 -> 84
~ -[GKRatingViewAccessibility accessibilityLabel] : 108 -> 100
~ +[GKSectionHeaderViewAccessibility _accessibilityPerformValidations:] : 144 -> 136
~ -[GKSectionHeaderViewAccessibility initWithFrame:] : 128 -> 124
~ +[GKTurnGameCellAccessibility _accessibilityPerformValidations:] : 172 -> 160
~ -[GKTurnGameCellAccessibility accessibilityLabel] : 272 -> 244
~ +[GKTurnParticipantCellAccessibility _accessibilityPerformValidations:] : 172 -> 160
~ -[GKTurnParticipantCellAccessibility accessibilityLabel] : 272 -> 244
~ +[GKValueWithCaptionBubbleControlAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[GKValueWithCaptionBubbleControlAccessibility accessibilityLabel] : 160 -> 148
~ -[GKValueWithCaptionBubbleControlAccessibility isAccessibilityElement] : 96 -> 92
~ -[_GKBubbleFlowPseudoModalViewControllerAccessibility viewWillAppear:] : 108 -> 104
~ -[_GKBubbleFlowPseudoModalViewControllerAccessibility viewWillDisappear:] : 108 -> 104
~ +[GKComposeHeaderFieldAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[GKComposeHeaderFieldAccessibility initWithFrame:] : 184 -> 176
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "AXGameCenterPrivateUIFrameworkGlue"
- "B16@0:8"
- "B24@0:8q16"
- "Q16@0:8"
- "SafeCategory"
- "__GKBaseGameCellAccessibility_super"
- "__GKBasePlayerCellAccessibility_super"
- "__GKBubbleFlowAnimatorAccessibility_super"
- "__GKBubbleFlowOverlayViewAccessibility_super"
- "__GKCollectionViewCellAccessibility_super"
- "__GKComposeHeaderFieldAccessibility_super"
- "__GKPlayerGameCellAccessibility_super"
- "__GKPurchasableGameCellAccessibility_super"
- "__GKRatingViewAccessibility_super"
- "__GKSectionHeaderViewAccessibility_super"
- "__GKShowMoreViewAccessibility_super"
- "__GKTextBubbleControlAccessibility_super"
- "__GKTurnGameCellAccessibility_super"
- "__GKTurnParticipantCellAccessibility_super"
- "__GKValueWithCaptionBubbleControlAccessibility_super"
- "___GKBubbleFlowPseudoModalViewControllerAccessibility_super"
- "_accessibilityAllowsSiblingsWhenOvergrown"
- "_accessibilityPerformValidations:"
- "_accessibilitySupplementaryFooterViews"
- "_gkSendAction:viaResponder:withObject:"
- "accessibilityCustomActions"
- "accessibilityFrame"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityPath"
- "accessibilityPerformCustomAction:"
- "accessibilityTraits"
- "array"
- "arrayWithObjects:count:"
- "axSafelyAddObject:"
- "bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:"
- "bundleWithIdentifier:"
- "bundleWithPath:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "floatValue"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "length"
- "localizedStringForKey:value:table:"
- "objectAtIndex:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "setAccessibilityIdentifier:"
- "setAccessibilityTraits:"
- "setAccessibilityViewIsModal:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedApplication"
- "sharedInstance"
- "stringByAppendingPathComponent:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "viewWillAppear:"
- "viewWillDisappear:"

```
