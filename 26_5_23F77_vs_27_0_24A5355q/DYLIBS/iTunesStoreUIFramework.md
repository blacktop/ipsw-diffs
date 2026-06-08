## iTunesStoreUIFramework

> `/System/Library/AccessibilityBundles/iTunesStoreUIFramework.axbundle/iTunesStoreUIFramework`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x4394
-  __TEXT.__auth_stubs: 0x2f0
+3036.2.0.0.0
+  __TEXT.__text: 0x40d4
   __TEXT.__objc_methlist: 0xa44
-  __TEXT.__cstring: 0x119f
   __TEXT.__const: 0x10
-  __TEXT.__unwind_info: 0x228
-  __TEXT.__objc_classname: 0xbf9
-  __TEXT.__objc_methname: 0xa9d
-  __TEXT.__objc_methtype: 0x8e
-  __TEXT.__objc_stubs: 0xa20
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__cstring: 0x119f
+  __TEXT.__unwind_info: 0x220
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x398
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0xd8
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1820
   __AUTH_CONST.__objc_const: 0x2b90
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x280
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x1590

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D57686F8-D446-395D-AC1D-B56B0F6CABA8
-  Functions: 170
-  Symbols:   903
-  CStrings:  604
+  UUID: 1AF47F84-373A-3702-A859-3AEE656C7369
+  Functions: 169
+  Symbols:   904
+  CStrings:  397
 
Symbols:
+ ___block_literal_global.627
+ ___block_literal_global.636
+ ___block_literal_global.742
+ ___block_literal_global.753
+ ___block_literal_global.764
+ ___block_literal_global.772
+ ___block_literal_global.927
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- -[SUiBooksOverrideWebViewAccessibility _accessibilityIsScrollAncestor].cold.1
- ___block_literal_global.606
- ___block_literal_global.615
- ___block_literal_global.721
- ___block_literal_global.730
- ___block_literal_global.732
- ___block_literal_global.743
- _objc_retain_x22
- _objc_retain_x26
Functions:
~ +[AXiTunesStoreUIGlue accessibilityInitializeBundle] : 304 -> 296
~ ___52+[AXiTunesStoreUIGlue accessibilityInitializeBundle]_block_invoke : 2072 -> 2068
~ ___52+[AXiTunesStoreUIGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ ___52+[AXiTunesStoreUIGlue accessibilityInitializeBundle]_block_invoke_3 : 740 -> 732
~ ___41+[AXiTunesStoreUIGlue _webKitInitialized]_block_invoke : 104 -> 100
~ ___41+[AXiTunesStoreUIGlue _webKitInitialized]_block_invoke_2 : 104 -> 100
~ ___41+[AXiTunesStoreUIGlue _webKitInitialized]_block_invoke_3 : 88 -> 84
~ ___41+[AXiTunesStoreUIGlue _webKitInitialized]_block_invoke_4 : 140 -> 132
~ -[SUApplicationAccessibility _accessibilityContentLanguage] : 112 -> 104
~ -[SUBannerCellAccessibility _reloadButtons] : 624 -> 596
~ -[SUBannerCellConfigurationAccessibility accessibilityTableViewCellText] : 152 -> 140
~ -[SUButtonCellConfigurationAccessibility accessibilityLabel] : 104 -> 88
~ -[SUCellConfigurationCacheAccessibility configurationForRow:] : 220 -> 208
~ -[SUCompletionCellConfigurationAccessibility accessibilityLabel] : 104 -> 88
~ -[SUItemCellConfigurationAccessibility _accessibilityVideoIconString] : 136 -> 128
~ -[SUItemOfferButtonAccessibility accessibilityLabel] : 260 -> 240
~ -[SULoadMoreCellConfigurationAccessibility accessibilityLabel] : 104 -> 88
~ -[SULoadMoreMediaCellConfigurationAccessibility accessibilityLabel] : 140 -> 132
~ -[SUMaskedViewAccessibility accessibilityElementsHidden] : 196 -> 192
~ -[SUNavigationButtonAccessibility accessibilityLabel] : 248 -> 232
~ -[SUReviewCellConfigurationAccessibility accessibilityLabel] : 308 -> 284
~ -[SUReviewsButtonAccessibility accessibilityLabel] : 272 -> 252
~ -[SUReviewsHeaderCellConfigurationAccessibility accessibilityLabel] : 304 -> 280
~ -[SUShortLinkCellConfigurationAccessibility accessibilityLabel] : 172 -> 168
~ -[SUStorePageViewControllerAccessibility reloadForSectionsWithGroup:] : 168 -> 160
~ -[SUStorePageViewControllerAccessibility _setActiveChildViewController:shouldTearDown:] : 200 -> 196
~ -[SUSubtitledButtonAccessibility accessibilityLabel] : 176 -> 164
~ -[SUTableCellAccessibility accessibilityTableViewCellText] : 92 -> 84
~ -[SUTableCellAccessibility accessibilityHint] : 92 -> 84
~ -[SUTableCellAccessibility accessibilityValue] : 92 -> 84
~ -[SUTableCellAccessibility accessibilityTraits] : 208 -> 200
~ -[SUTableCellAccessibility description] : 184 -> 172
~ +[SURedeemCameraViewControllerAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[SURedeemCameraViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 140 -> 132
~ -[SUTableCellContentViewAccessibility accessibilityTraits] : 68 -> 64
~ -[SUTableCellContentViewAccessibility accessibilityHint] : 92 -> 84
~ -[SUTableCellContentViewAccessibility accessibilityLabel] : 92 -> 84
~ -[SUTableCellContentViewAccessibility accessibilityValue] : 92 -> 84
~ -[SUTableCellContentViewAccessibility description] : 136 -> 128
~ -[SUTableHeaderViewAccessibility accessibilityLabel] : 216 -> 204
~ -[SUTableViewAccessibility _accessibilityScrollStatus] : 212 -> 200
~ -[SUTallLinkCellConfigurationAccessibility accessibilityLabel] : 384 -> 364
~ -[SUTermsAndConditionsViewAccessibility _termsAndConditionsControl] : 152 -> 144
~ +[SUTextContentViewAccessibility _accessibilityPerformValidations:] : 168 -> 156
~ -[SUTextContentViewAccessibility _accessibilityPlaceholderValue:] : 344 -> 324
~ -[SUTextContentViewAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 104
~ -[SUTextContentViewAccessibility accessibilityValue] : 152 -> 140
~ -[SUTouchCaptureViewAccessibility _accessibilityHitTest:withEvent:] : 652 -> 644
~ -[SUTwoLineTrackCellConfigurationAccessibility accessibilityLabel] : 316 -> 308
~ -[SUUIScrollViewAccessibility setTopExtensionViewColor:] : 104 -> 100
~ -[SUUIWebDocumentViewAccessibility accessibilityScrollRightPage] : 644 -> 600
~ -[SUiBooksOverrideWebViewAccessibility _accessibilityIsScrollAncestor] : 228 -> 248
~ ___70-[SUiBooksOverrideWebViewAccessibility _accessibilityIsScrollAncestor]_block_invoke : 264 -> 244
~ -[SUWebViewAccessibility _accessibilitySUWebViewIsScrollAncestor] : 308 -> 292
~ -[SUWebViewAccessibility accessibilityScroll:] : 256 -> 244
~ -[SUWebViewAccessibility accessibilityPerformEscape] : 84 -> 80
~ -[SUWebViewAccessibility accessibilityScrollRightPage] : 572 -> 532
~ _accessibilityLocalizedString : 164 -> 156
~ _starStringForStarCount : 220 -> 204
~ ___69-[SUScriptNotificationObserverAccessibility _axActionOccurredForWeb:]_block_invoke : 280 -> 264
~ -[SUScriptNotificationObserverAccessibility dealloc] : 116 -> 112
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8Q16"
- "@40@0:8{CGPoint=dd}16@32"
- "AXPrivate"
- "AXiTunesStoreUIGlue"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8q16"
- "Q16@0:8"
- "SafeCategory"
- "__SUApplicationAccessibility_super"
- "__SUBannerCellAccessibility_super"
- "__SUBannerCellConfigurationAccessibility_super"
- "__SUButtonCellConfigurationAccessibility_super"
- "__SUCellConfigurationAccessibility_super"
- "__SUCellConfigurationCacheAccessibility_super"
- "__SUCompletionCellConfigurationAccessibility_super"
- "__SUDeferredUISegmentedControlAccessibility_super"
- "__SUItemCellConfigurationAccessibility_super"
- "__SUItemOfferButtonAccessibility_super"
- "__SULoadMoreCellConfigurationAccessibility_super"
- "__SULoadMoreMediaCellConfigurationAccessibility_super"
- "__SUMaskedViewAccessibility_super"
- "__SUNavigationButtonAccessibility_super"
- "__SURedeemCameraViewControllerAccessibility_super"
- "__SUReviewCellConfigurationAccessibility_super"
- "__SUReviewsButtonAccessibility_super"
- "__SUReviewsHeaderCellConfigurationAccessibility_super"
- "__SUScriptNotificationObserverAccessibility_super"
- "__SUShortLinkCellConfigurationAccessibility_super"
- "__SUStorePageViewControllerAccessibility_super"
- "__SUStructuredPageViewControllerAccessibility_super"
- "__SUSubtitledButtonAccessibility_super"
- "__SUTableCellAccessibility_super"
- "__SUTableCellContentViewAccessibility_super"
- "__SUTableHeaderViewAccessibility_super"
- "__SUTableViewAccessibility_super"
- "__SUTallLinkCellConfigurationAccessibility_super"
- "__SUTermsAndConditionsViewAccessibility_super"
- "__SUTextContentViewAccessibility_super"
- "__SUThreeLineTrackCellConfigurationAccessibility_super"
- "__SUTouchCaptureViewAccessibility_super"
- "__SUTwoLineTrackCellConfigurationAccessibility_super"
- "__SUUIScrollViewAccessibility_super"
- "__SUUIWebDocumentViewAccessibility_super"
- "__SUWebViewAccessibility_super"
- "__SUWebViewControllerAccessibility_super"
- "__SUiBooksOverrideWebViewAccessibility_super"
- "_accessibilityAllowsSiblingsWhenOvergrown"
- "_accessibilityBoolValueForKey:"
- "_accessibilityClearTable:"
- "_accessibilityContentSize"
- "_accessibilityHasDescendantOfType:"
- "_accessibilityHitTest:withEvent:"
- "_accessibilityIsScrollAncestor"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityPlaceholderValue:"
- "_accessibilityReloadMediaStrings"
- "_accessibilityRemoveValueForKey:"
- "_accessibilitySUWebViewIsScrollAncestor"
- "_accessibilityScrollStatus"
- "_axActionOccurredForWeb:"
- "_reloadButtons"
- "_setActiveChildViewController:shouldTearDown:"
- "_webKitInitialized"
- "accessibilityActivate"
- "accessibilityContainerType"
- "accessibilityElementsHidden"
- "accessibilityFrame"
- "accessibilityHint"
- "accessibilityIdentification"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityLanguage"
- "accessibilityPerformEscape"
- "accessibilityPlaceholderValue"
- "accessibilityScroll:"
- "accessibilityScrollRightPage"
- "accessibilityTableViewCellText"
- "accessibilityTraits"
- "accessibilityValue"
- "addObject:"
- "addObserver:selector:name:object:"
- "alpha"
- "appendFormat:"
- "axAttributedStringWithString:"
- "boolValue"
- "bounds"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "bytes"
- "compare:options:"
- "convertPoint:fromView:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentDevice"
- "dealloc"
- "defaultCenter"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "dismissOverlay:animated:"
- "floatValue"
- "hasSuffix:"
- "infoDictionary"
- "installSafeCategory:canInteractWithTargetClass:"
- "intValue"
- "integerValue"
- "isAccessibilityElement"
- "isEqualToString:"
- "isHidden"
- "length"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "mainBundle"
- "mainScreen"
- "numberWithInteger:"
- "objectAtIndex:"
- "objectForKey:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "pointInside:withEvent:"
- "postNotificationName:object:userInfo:"
- "q16@0:8"
- "reloadStrings"
- "removeObserver:name:object:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "sendActionsForControlEvents:"
- "setAccessibilityLabel:"
- "setAccessibilityLanguage:"
- "setAccessibilityTraits:"
- "setAccessibilityViewIsModal:"
- "setAttribute:forKey:"
- "setCellReuseSource:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "string"
- "stringWithFormat:"
- "superview"
- "userInfo"
- "userInterfaceIdiom"
- "v16@0:8"
- "v24@0:8@16"
- "v28@0:8@16B24"
- "validateClass:"
- "validateClass:hasClassMethod:withFullSignature:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "viewWithTag:"
- "visibleBounds"

```
