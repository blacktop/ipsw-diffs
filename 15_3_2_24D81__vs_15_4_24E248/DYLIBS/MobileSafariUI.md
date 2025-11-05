## MobileSafariUI

> `/System/iOSSupport/System/Library/AccessibilityBundles/MobileSafariUI.axbundle/Contents/MacOS/MobileSafariUI`

```diff

-2963.3.13.1.0
-  __TEXT.__text: 0x97c8
+2963.10.10.0.0
+  __TEXT.__text: 0x87f4
   __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0xc40
-  __TEXT.__cstring: 0x1db2
-  __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x1f8
+  __TEXT.__objc_methlist: 0xb20
+  __TEXT.__cstring: 0x1b2a
+  __TEXT.__const: 0x30
+  __TEXT.__gcc_except_tab: 0x194
   __TEXT.__oslogstring: 0x80
-  __TEXT.__unwind_info: 0x3c8
-  __TEXT.__objc_classname: 0x8d8
-  __TEXT.__objc_methname: 0x1835
-  __TEXT.__objc_methtype: 0x22b
-  __TEXT.__objc_stubs: 0x1500
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x2d8
-  __DATA_CONST.__objc_classlist: 0x1d0
+  __TEXT.__unwind_info: 0x330
+  __TEXT.__objc_classname: 0x847
+  __TEXT.__objc_methname: 0x1631
+  __TEXT.__objc_methtype: 0x1b7
+  __TEXT.__objc_stubs: 0x13a0
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__const: 0x2b0
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x780
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_selrefs: 0x6e0
+  __DATA_CONST.__objc_superrefs: 0xb0
   __AUTH_CONST.__auth_got: 0x2e0
-  __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x2600
-  __AUTH_CONST.__objc_const: 0x20c8
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x2280
+  __AUTH_CONST.__objc_const: 0x1e88
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1220
+  __AUTH.__objc_data: 0x10e0
   __DATA.__objc_ivar: 0x4
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C75C75B-607C-32F7-BF7B-49050CC8F9E5
-  Functions: 259
-  Symbols:   908
-  CStrings:  984
+  UUID: 39601608-C980-3630-B10D-AE7C794BBA4F
+  Functions: 231
+  Symbols:   842
+  CStrings:  897
 
Symbols:
+ +[AXMobileSafariUIGlue accessibilityInitializeBundle].cold.1
+ +[CompletionArrowViewAccessibility _accessibilityPerformValidations:]
+ +[CompletionArrowViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[CompletionArrowViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[BrowserRootViewControllerAccessibility _axGetResetRefreshTimer]
+ -[BrowserRootViewControllerAccessibility _axResetRefreshTimer]
+ -[BrowserRootViewControllerAccessibility _axSetResetRefreshTimer:]
+ -[BrowserRootViewControllerAccessibility _axSetShouldRefresh:]
+ -[BrowserRootViewControllerAccessibility _axShouldRefresh]
+ -[CompletionArrowViewAccessibility accessibilityLabel]
+ _OBJC_CLASS_$_CompletionArrowViewAccessibility
+ _OBJC_CLASS_$___CompletionArrowViewAccessibility_super
+ _OBJC_METACLASS_$_CompletionArrowViewAccessibility
+ _OBJC_METACLASS_$___CompletionArrowViewAccessibility_super
+ _UIAccessibilitySpeakAndDoNotBeInterrupted
+ __OBJC_$_CLASS_METHODS_CompletionArrowViewAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_CompletionArrowViewAccessibility
+ __OBJC_CLASS_RO_$_CompletionArrowViewAccessibility
+ __OBJC_CLASS_RO_$___CompletionArrowViewAccessibility_super
+ __OBJC_METACLASS_RO_$_CompletionArrowViewAccessibility
+ __OBJC_METACLASS_RO_$___CompletionArrowViewAccessibility_super
+ ___62-[BrowserRootViewControllerAccessibility accessibilityScroll:]_block_invoke_2
+ ___BrowserRootViewControllerAccessibility___axResetRefreshTimer
+ ___BrowserRootViewControllerAccessibility___axShouldRefresh
+ ___UIAccessibilityGetAssociatedBool
+ ___UIAccessibilitySetAssociatedBool
+ __block_literal_global.304
+ __block_literal_global.313
+ _objc_msgSend$_axGetResetRefreshTimer
+ _objc_msgSend$_axResetRefreshTimer
+ _objc_msgSend$_axSetResetRefreshTimer:
+ _objc_msgSend$_axSetShouldRefresh:
+ _objc_msgSend$_axShouldRefresh
- +[StepperViewControllerAccessibility _accessibilityPerformValidations:]
- +[StepperViewControllerAccessibility(SafeCategory) safeCategoryBaseClass]
- +[StepperViewControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[TabOverviewAccessibility _accessibilityPerformValidations:]
- +[TabOverviewAccessibility(SafeCategory) safeCategoryBaseClass]
- +[TabOverviewAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[TabThumbnailCloseButtonAccessibility _accessibilityPerformValidations:]
- +[TabThumbnailCloseButtonAccessibility(SafeCategory) safeCategoryBaseClass]
- +[TabThumbnailCloseButtonAccessibility(SafeCategory) safeCategoryTargetClassName]
- -[StepperViewControllerAccessibility _accessibilityLoadAccessibilityInformation]
- -[StepperViewControllerAccessibility _axMarkupStepperButtons]
- -[StepperViewControllerAccessibility loadView]
- -[TabOverviewAccessibility _accessibilityAdjustedScrollOffset:]
- -[TabOverviewAccessibility _accessibilityIsScrollAncestor]
- -[TabOverviewAccessibility _accessibilityLoadAccessibilityInformation]
- -[TabOverviewAccessibility _accessibilityScrollStatusFormatString]
- -[TabOverviewAccessibility _accessibilityScrollStatus]
- -[TabOverviewAccessibility _accessibilityScrollToView:]
- -[TabOverviewAccessibility _accessibilityThumbnailApplyScrollOffset:]
- -[TabOverviewAccessibility _accessibilityThumbnailOffset]
- -[TabOverviewAccessibility _dismissWithItemAtCurrentDecelerationFactor:]
- -[TabOverviewAccessibility _isClosingLastItem]
- -[TabOverviewAccessibility accessibilityScroll:]
- -[TabOverviewAccessibility initWithFrame:]
- -[TabOverviewAccessibility isAccessibilityOpaqueElementProvider]
- -[TabOverviewAccessibility layoutSubviews]
- -[TabOverviewAccessibility shouldGroupAccessibilityChildren]
- -[TabThumbnailCloseButtonAccessibility accessibilityIdentifier]
- -[TabThumbnailCloseButtonAccessibility accessibilityLabel]
- GCC_except_table14
- GCC_except_table8
- _AXFormatInteger
- _AX_CGRectGetCenter
- _OBJC_CLASS_$_StepperViewControllerAccessibility
- _OBJC_CLASS_$_TabOverviewAccessibility
- _OBJC_CLASS_$_TabThumbnailCloseButtonAccessibility
- _OBJC_CLASS_$___StepperViewControllerAccessibility_super
- _OBJC_CLASS_$___TabOverviewAccessibility_super
- _OBJC_CLASS_$___TabThumbnailCloseButtonAccessibility_super
- _OBJC_METACLASS_$_StepperViewControllerAccessibility
- _OBJC_METACLASS_$_TabOverviewAccessibility
- _OBJC_METACLASS_$_TabThumbnailCloseButtonAccessibility
- _OBJC_METACLASS_$___StepperViewControllerAccessibility_super
- _OBJC_METACLASS_$___TabOverviewAccessibility_super
- _OBJC_METACLASS_$___TabThumbnailCloseButtonAccessibility_super
- _UIAccessibilityPageScrolledNotification
- __OBJC_$_CLASS_METHODS_StepperViewControllerAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_TabOverviewAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_TabThumbnailCloseButtonAccessibility(SafeCategory)
- __OBJC_$_INSTANCE_METHODS_StepperViewControllerAccessibility
- __OBJC_$_INSTANCE_METHODS_TabOverviewAccessibility
- __OBJC_$_INSTANCE_METHODS_TabThumbnailCloseButtonAccessibility
- __OBJC_CLASS_RO_$_StepperViewControllerAccessibility
- __OBJC_CLASS_RO_$_TabOverviewAccessibility
- __OBJC_CLASS_RO_$_TabThumbnailCloseButtonAccessibility
- __OBJC_CLASS_RO_$___StepperViewControllerAccessibility_super
- __OBJC_CLASS_RO_$___TabOverviewAccessibility_super
- __OBJC_CLASS_RO_$___TabThumbnailCloseButtonAccessibility_super
- __OBJC_METACLASS_RO_$_StepperViewControllerAccessibility
- __OBJC_METACLASS_RO_$_TabOverviewAccessibility
- __OBJC_METACLASS_RO_$_TabThumbnailCloseButtonAccessibility
- __OBJC_METACLASS_RO_$___StepperViewControllerAccessibility_super
- __OBJC_METACLASS_RO_$___TabOverviewAccessibility_super
- __OBJC_METACLASS_RO_$___TabThumbnailCloseButtonAccessibility_super
- ___55-[TabOverviewAccessibility _accessibilityScrollToView:]_block_invoke
- ___57-[TabOverviewAccessibility _accessibilityThumbnailOffset]_block_invoke
- ___61-[StepperViewControllerAccessibility _axMarkupStepperButtons]_block_invoke
- ___61-[StepperViewControllerAccessibility _axMarkupStepperButtons]_block_invoke_2
- ___69-[TabOverviewAccessibility _accessibilityThumbnailApplyScrollOffset:]_block_invoke
- ___69-[TabOverviewAccessibility _accessibilityThumbnailApplyScrollOffset:]_block_invoke_2
- ___69-[TabOverviewAccessibility _accessibilityThumbnailApplyScrollOffset:]_block_invoke_3
- ___72-[TabOverviewAccessibility _dismissWithItemAtCurrentDecelerationFactor:]_block_invoke
- ___block_descriptor_64_e8_32s40s_e5_v8?0ls32l8s40l8
- __block_literal_global.328
- __block_literal_global.337
- __block_literal_global.353
- _accessibilityUIKitLocalizedString
- _kAXPerformElementUpdateImmediatelyToken
- _objc_msgSend$CGSizeValue
- _objc_msgSend$_accessibilityAdjustedScrollOffset:
- _objc_msgSend$_accessibilityScrollStatusFormatString
- _objc_msgSend$_accessibilitySetOnlyComparesByXAxis:
- _objc_msgSend$_accessibilityThumbnailApplyScrollOffset:
- _objc_msgSend$_accessibilityThumbnailOffset
- _objc_msgSend$_axMarkupStepperButtons
- _objc_msgSend$_buttonForStepperButton:
- _objc_msgSend$frame
- _objc_msgSend$location
- _objc_msgSend$rectValue
- _objc_msgSend$resetToLocation:
- _objc_msgSend$resignFirstResponder
- _objc_msgSend$setAccessibilityContainerType:
- _objc_msgSend$setNeedsLayout
- _objc_msgSend$setShouldGroupAccessibilityChildren:
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias5/MobileSafariAccessibility/MobileSafariUI/CapsuleNavigationBarRegistrationAccessibility.m"
+ "CONFIRM_REFRESH"
+ "CompletionArrowView"
+ "CompletionArrowViewAccessibility"
+ "__CompletionArrowViewAccessibility_super"
+ "_axGetResetRefreshTimer"
+ "_axResetRefreshTimer"
+ "_axSetResetRefreshTimer:"
+ "_axSetShouldRefresh:"
+ "_axShouldRefresh"
+ "complete.search"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles_Alias5/MobileSafariAccessibility/MobileSafariUI/CapsuleNavigationBarRegistrationAccessibility.m"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "BarButton"
- "CGSizeValue"
- "Close"
- "SFTabOverviewSearchBar"
- "StepperViewController"
- "StepperViewControllerAccessibility"
- "TabGroupSwitcherViewController"
- "TabOverview"
- "TabOverviewAccessibility"
- "TabOverviewInterpolatedLocation"
- "TabOverviewToolbar"
- "TabThumbnailCloseButton"
- "TabThumbnailCloseButtonAccessibility"
- "__StepperViewControllerAccessibility_super"
- "__TabOverviewAccessibility_super"
- "__TabThumbnailCloseButtonAccessibility_super"
- "_accessibilityAdjustedScrollOffset:"
- "_accessibilityIsScrollAncestor"
- "_accessibilityScrollStatusFormatString"
- "_accessibilityScrollToView:"
- "_accessibilitySetOnlyComparesByXAxis:"
- "_accessibilityThumbnailApplyScrollOffset:"
- "_accessibilityThumbnailOffset"
- "_axMarkupStepperButtons"
- "_buttonForStepperButton:"
- "_contentSize"
- "_dismissWithItemAtCurrentDecelerationFactor:"
- "_header"
- "_interpolatedLocation"
- "_isClosingLastItem"
- "_tabGroups"
- "_tabOverview"
- "_updateDisplayLink"
- "capsuleCollectionView:contentViewForItemAtIndex:"
- "close.button"
- "decrease.font.size"
- "frame"
- "increase.font.size"
- "initWithFrame:"
- "isAccessibilityOpaqueElementProvider"
- "layoutSubviews"
- "loadView"
- "location"
- "performUpdatesWithoutTabCloseAnimation:"
- "presentationState"
- "rectValue"
- "resetToLocation:"
- "resignFirstResponder"
- "scroll.page.summary"
- "setAccessibilityContainerType:"
- "setNeedsLayout"
- "setShouldGroupAccessibilityChildren:"
- "shouldGroupAccessibilityChildren"
- "tabCollectionViewProvider"
- "v32@0:8{CGPoint=dd}16"
- "{?={CGPoint=dd}dd}"
- "{CGPoint=dd}16@0:8"
- "{CGPoint=dd}32@0:8{CGPoint=dd}16"
- "{CGSize=dd}"

```
