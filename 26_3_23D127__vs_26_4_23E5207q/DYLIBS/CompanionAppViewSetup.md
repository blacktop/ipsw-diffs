## CompanionAppViewSetup

> `/System/Library/AccessibilityBundles/CompanionAppViewSetup.axbundle/CompanionAppViewSetup`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x1c68
-  __TEXT.__auth_stubs: 0x2a0
+3005.16.0.0.0
+  __TEXT.__text: 0x1d5c
+  __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__cstring: 0x587
+  __TEXT.__cstring: 0x5c6
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x28
   __TEXT.__unwind_info: 0x120

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x278
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x160
+  __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0x630

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF138F6E-3545-3732-96C7-98CEDD88A48D
+  UUID: BC748C05-5368-3F39-A0F8-B87DE9A251EA
   Functions: 59
-  Symbols:   314
+  Symbols:   311
   CStrings:  232
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x23
Functions:
~ +[AXCarouselAppViewSharedGlue accessibilityInitializeBundle] : 148 -> 152
~ ___60+[AXCarouselAppViewSharedGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ -[CSLUILayoutIconViewAccessibility accessibilityPath] : 200 -> 212
~ +[CSLUIFieldOfIconsViewAccessibility _accessibilityPerformValidations:] : 600 -> 612
~ ___63-[CSLUIFieldOfIconsViewAccessibility accessibilityScrollUpPage]_block_invoke_3 : 92 -> 96
~ ___65-[CSLUIFieldOfIconsViewAccessibility accessibilityScrollDownPage]_block_invoke_2 : 92 -> 96
~ -[CSLUIFieldOfIconsViewAccessibility _axHexForIconView:] : 88 -> 92
~ -[CSLUIFieldOfIconsViewAccessibility _axUpdateIconElements] : 920 -> 960
~ -[CSLUIFieldOfIconsViewAccessibility accessibilityElements] : 96 -> 104
~ -[CSLUIFieldOfIconsViewAccessibility _accessibilityHitTestSubviews] : 400 -> 416
~ -[CSLUIFieldOfIconsViewAccessibility _accessibilityStartJiggleMode:] : 88 -> 92
~ -[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveElement:left:] : 416 -> 428
~ ___69-[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveElement:left:]_block_invoke : 96 -> 100
~ -[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveIconLeft:] : 104 -> 108
~ -[CSLUIFieldOfIconsViewAccessibility _accessibilityMoveIconRight:] : 128 -> 132
~ -[CSLUIFieldOfIconsViewAccessibility _accessibilityAnnounceUpdatedPositionForElement:] : 428 -> 468
~ -[CSLUIFieldOfIconsViewAccessibility setLayout:percentComplete:animated:options:] : 144 -> 148
~ +[CSLPRFWatchChoiceViewAccessibility _accessibilityPerformValidations:] : 152 -> 160
~ -[CSLPRFWatchChoiceViewAccessibility accessibilityLabel] : 216 -> 232
~ -[CSLPRFWatchChoiceViewAccessibility accessibilityTraits] : 232 -> 240
~ -[CSLUINanoResourceGrabberIconViewAccessibility accessibilityLabel] : 292 -> 316
CStrings:
+ "/Library/Caches/com.apple.xbs/D796EB7F-4AEA-4A12-AB49-AB256E569E81/TemporaryDirectory.1bWS40/Sources/AccessibilityBundles/CarouselAppViewSettingsAccessibility/CSLUINanoResourceGrabberIconViewAccessibility.m"
- "/Library/Caches/com.apple.xbs/Sources/AccessibilityBundles/CarouselAppViewSettingsAccessibility/CSLUINanoResourceGrabberIconViewAccessibility.m"

```
