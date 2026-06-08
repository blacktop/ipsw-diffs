## Animoji

> `/System/Library/AccessibilityBundles/Animoji.axbundle/Animoji`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x2608
-  __TEXT.__auth_stubs: 0x290
+3036.2.0.0.0
+  __TEXT.__text: 0x24cc
   __TEXT.__objc_methlist: 0x354
-  __TEXT.__cstring: 0x9b0
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x78
+  __TEXT.__cstring: 0x9b2
   __TEXT.__unwind_info: 0x150
-  __TEXT.__objc_classname: 0x1bd
-  __TEXT.__objc_methname: 0x9c8
-  __TEXT.__objc_methtype: 0xe5
-  __TEXT.__objc_stubs: 0x800
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2e8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x158
+  __DATA_CONST.__got: 0xa0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xda0
   __AUTH_CONST.__objc_const: 0x700
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x3c0
   __DATA.__objc_ivar: 0x4
   __DATA.__bss: 0xc

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D7B0003-3293-3C9F-A886-B74B607A8E2E
+  UUID: 2584ED22-BD0E-3749-A9A8-645B81D94BB9
   Functions: 71
-  Symbols:   355
-  CStrings:  362
+  Symbols:   357
+  CStrings:  235
 
Symbols:
+ GCC_except_table15
+ GCC_except_table37
+ GCC_except_table62
+ ___85-[PuppetCollectionViewControllerAccessibility collectionView:cellForItemAtIndexPath:]_block_invoke.385
+ ___block_literal_global.351
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x8
- GCC_except_table28
- GCC_except_table3
- GCC_except_table9
- ___85-[PuppetCollectionViewControllerAccessibility collectionView:cellForItemAtIndexPath:]_block_invoke.364
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x23
Functions:
~ +[AXJellyfishGlue accessibilityInitializeBundle] : 148 -> 144
~ ___48+[AXJellyfishGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ ___48+[AXJellyfishGlue accessibilityInitializeBundle]_block_invoke_3 : 160 -> 152
~ _accessibilityJellyfishLocalizedString : 168 -> 160
~ +[LaunchViewControllerAccessibility _accessibilityPerformValidations:] : 140 -> 128
~ -[LaunchViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 476 -> 440
~ +[PuppetCollectionViewControllerAccessibility _accessibilityPerformValidations:] : 284 -> 276
~ -[PuppetCollectionViewControllerAccessibility collectionView:cellForItemAtIndexPath:] : 648 -> 644
~ ___85-[PuppetCollectionViewControllerAccessibility collectionView:cellForItemAtIndexPath:]_block_invoke.364 -> ___85-[PuppetCollectionViewControllerAccessibility collectionView:cellForItemAtIndexPath:]_block_invoke.385 : 124 -> 116
~ +[RecordButtonAccessibility _accessibilityPerformValidations:] : 128 -> 120
~ ___71-[AX_AvatarCarousel initWithMessagesController:accessibilityContainer:]_block_invoke : 124 -> 116
~ -[AX_AvatarCarousel _axContainerAvatarController] : 92 -> 84
~ -[AX_AvatarCarousel _axMessagesControllerIsExpanded] : 72 -> 68
~ -[AX_AvatarCarousel isAccessibilityElement] : 76 -> 72
~ -[AX_AvatarCarousel accessibilityValue] : 440 -> 392
~ -[AX_AvatarCarousel accessibilityHint] : 132 -> 124
~ ___50-[AX_AvatarCarousel _accessibilityScrollCarousel:]_block_invoke : 264 -> 256
~ -[AX_AvatarCarousel accessibilityFrameInContainerSpace] : 100 -> 96
~ +[MessagesViewControllerAccessibility _accessibilityPerformValidations:] : 1720 -> 1712
~ -[MessagesViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 1168 -> 1092
~ ___81-[MessagesViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 160 -> 156
~ -[MessagesViewControllerAccessibility _accessibilityUpdateRecordButtonLabel] : 224 -> 212
~ -[MessagesViewControllerAccessibility _accessibilityUpdateCollectionViewAccessibilityForPresentationStyle:] : 156 -> 148
~ -[MessagesViewControllerAccessibility observeValueForKeyPath:ofObject:change:context:] : 428 -> 416
~ -[MessagesViewControllerAccessibility showUserInfoLabelWithText:] : 156 -> 152
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@16@0:8"
- "@32@0:8@16@24"
- "AXJellyfishGlue"
- "AX_AvatarCarousel"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8q16"
- "B32@0:8@16@24"
- "Q16@0:8"
- "SafeCategory"
- "T@,W,N,V_messagesController"
- "__LaunchViewControllerAccessibility_super"
- "__MessagesViewControllerAccessibility_super"
- "__PuppetCollectionViewCellAccessibility_super"
- "__PuppetCollectionViewControllerAccessibility_super"
- "__RecordButtonAccessibility_super"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityScrollCarousel:"
- "_accessibilitySupportsActivateAction"
- "_accessibilityUpdateCollectionViewAccessibilityForPresentationStyle:"
- "_accessibilityUpdateRecordButtonLabel"
- "_axAvatarCarousel"
- "_axContainerAvatarController"
- "_axCurrentIndex"
- "_axLastUserInfoString"
- "_axLiveCell"
- "_axMessagesControllerIsExpanded"
- "_messagesController"
- "_setAXAvatarCarousel:"
- "_setAXCurrentIndex:"
- "_setAXLastUserInfoString:"
- "_setAXLiveCell:"
- "_setAccessibilityLabelBlock:"
- "accessibilityBundles"
- "accessibilityContainer"
- "accessibilityDecrement"
- "accessibilityFrameInContainerSpace"
- "accessibilityHint"
- "accessibilityIncrement"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityScroll:"
- "accessibilityTraits"
- "accessibilityValue"
- "alpha"
- "axArrayByIgnoringNilElementsWithCount:"
- "bundleForClass:"
- "count"
- "descriptionForAvatarWithRecord:includeVideoPrefix:"
- "frame"
- "initWithAccessibilityContainer:"
- "initWithMessagesController:accessibilityContainer:"
- "initWithString:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "isEqual:"
- "isEqualToString:"
- "localizedStringForKey:value:table:"
- "messagesController"
- "objectAtIndex:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "q16@0:8"
- "row"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntegerForKey:"
- "safeStringForKey:"
- "safeUIViewForKey:"
- "safeUnsignedIntegerForKey:"
- "safeValueForKey:"
- "safeValueForKeyPath:"
- "setAccessibilityElements:"
- "setAccessibilityElementsHidden:"
- "setAccessibilityHint:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setAccessibilityViewIsModal:"
- "setAttribute:forKey:"
- "setIsAccessibilityElement:"
- "setMessagesController:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8Q16@24"
- "v48@0:8@16@24@32^v40"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "validateProtocol:hasRequiredInstanceMethod:"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
