## Animoji

> `/System/Library/AccessibilityBundles/Animoji.axbundle/Animoji`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x24d0
-  __TEXT.__auth_stubs: 0x2b0
+3005.16.0.0.0
+  __TEXT.__text: 0x2608
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__objc_methlist: 0x354
   __TEXT.__cstring: 0x9b0
   __TEXT.__const: 0x18

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2e8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x168
+  __AUTH_CONST.__auth_got: 0x158
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xda0
   __AUTH_CONST.__objc_const: 0x700

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FAA972C0-C9F5-3FA4-BA70-FF812309BA2F
+  UUID: F14EAAE2-FB62-365A-8363-63839FF69AA7
   Functions: 71
-  Symbols:   357
+  Symbols:   355
   CStrings:  362
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x8
Functions:
~ +[AXJellyfishGlue accessibilityInitializeBundle] : 144 -> 148
~ ___48+[AXJellyfishGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___48+[AXJellyfishGlue accessibilityInitializeBundle]_block_invoke_3 : 152 -> 160
~ _accessibilityJellyfishLocalizedString : 160 -> 168
~ +[LaunchViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[LaunchViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 440 -> 476
~ +[PuppetCollectionViewControllerAccessibility _accessibilityPerformValidations:] : 276 -> 284
~ -[PuppetCollectionViewControllerAccessibility collectionView:cellForItemAtIndexPath:] : 644 -> 648
~ ___85-[PuppetCollectionViewControllerAccessibility collectionView:cellForItemAtIndexPath:]_block_invoke.325 : 116 -> 124
~ +[RecordButtonAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ ___71-[AX_AvatarCarousel initWithMessagesController:accessibilityContainer:]_block_invoke : 116 -> 124
~ -[AX_AvatarCarousel _axContainerAvatarController] : 84 -> 92
~ -[AX_AvatarCarousel _axMessagesControllerIsExpanded] : 68 -> 72
~ -[AX_AvatarCarousel isAccessibilityElement] : 72 -> 76
~ -[AX_AvatarCarousel accessibilityValue] : 396 -> 440
~ -[AX_AvatarCarousel accessibilityHint] : 124 -> 132
~ ___50-[AX_AvatarCarousel _accessibilityScrollCarousel:]_block_invoke : 256 -> 264
~ -[AX_AvatarCarousel accessibilityFrameInContainerSpace] : 96 -> 100
~ +[MessagesViewControllerAccessibility _accessibilityPerformValidations:] : 1712 -> 1720
~ -[MessagesViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 1092 -> 1168
~ ___81-[MessagesViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 156 -> 160
~ -[MessagesViewControllerAccessibility _accessibilityUpdateRecordButtonLabel] : 212 -> 224
~ -[MessagesViewControllerAccessibility _accessibilityUpdateCollectionViewAccessibilityForPresentationStyle:] : 148 -> 156
~ -[MessagesViewControllerAccessibility observeValueForKeyPath:ofObject:change:context:] : 416 -> 428
~ -[MessagesViewControllerAccessibility showUserInfoLabelWithText:] : 152 -> 156

```
